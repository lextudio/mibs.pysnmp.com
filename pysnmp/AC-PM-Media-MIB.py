# SNMP MIB module (AC-PM-Media-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-PM-Media-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:33 2024
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

(acBoardMibs,
 acGeneric,
 acPerformance,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acPerformance",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acPMMedia = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcPMMediaConfiguration_ObjectIdentity = ObjectIdentity
acPMMediaConfiguration = _AcPMMediaConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1)
)


class _AcPMMediaConfigurationPeriodLength_Type(Unsigned32):
    """Custom type acPMMediaConfigurationPeriodLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 894780),
    )


_AcPMMediaConfigurationPeriodLength_Type.__name__ = "Unsigned32"
_AcPMMediaConfigurationPeriodLength_Object = MibScalar
acPMMediaConfigurationPeriodLength = _AcPMMediaConfigurationPeriodLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 1),
    _AcPMMediaConfigurationPeriodLength_Type()
)
acPMMediaConfigurationPeriodLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaConfigurationPeriodLength.setStatus("current")


class _AcPMMediaConfigurationResetTotalCounters_Type(Integer32):
    """Custom type acPMMediaConfigurationResetTotalCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetCountersDone", 1),
          ("resetTotalCounters", 2))
    )


_AcPMMediaConfigurationResetTotalCounters_Type.__name__ = "Integer32"
_AcPMMediaConfigurationResetTotalCounters_Object = MibScalar
acPMMediaConfigurationResetTotalCounters = _AcPMMediaConfigurationResetTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 2),
    _AcPMMediaConfigurationResetTotalCounters_Type()
)
acPMMediaConfigurationResetTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaConfigurationResetTotalCounters.setStatus("current")
_AcPMDSPAttributes_ObjectIdentity = ObjectIdentity
acPMDSPAttributes = _AcPMDSPAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 31)
)


class _AcPMDSPAttributesDSPUtilHighThreshold_Type(Unsigned32):
    """Custom type acPMDSPAttributesDSPUtilHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMDSPAttributesDSPUtilHighThreshold_Type.__name__ = "Unsigned32"
_AcPMDSPAttributesDSPUtilHighThreshold_Object = MibScalar
acPMDSPAttributesDSPUtilHighThreshold = _AcPMDSPAttributesDSPUtilHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 31, 1),
    _AcPMDSPAttributesDSPUtilHighThreshold_Type()
)
acPMDSPAttributesDSPUtilHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMDSPAttributesDSPUtilHighThreshold.setStatus("current")


class _AcPMDSPAttributesDSPUtilLowThreshold_Type(Unsigned32):
    """Custom type acPMDSPAttributesDSPUtilLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMDSPAttributesDSPUtilLowThreshold_Type.__name__ = "Unsigned32"
_AcPMDSPAttributesDSPUtilLowThreshold_Object = MibScalar
acPMDSPAttributesDSPUtilLowThreshold = _AcPMDSPAttributesDSPUtilLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 31, 2),
    _AcPMDSPAttributesDSPUtilLowThreshold_Type()
)
acPMDSPAttributesDSPUtilLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMDSPAttributesDSPUtilLowThreshold.setStatus("current")
_AcPMCodersAttributes_ObjectIdentity = ObjectIdentity
acPMCodersAttributes = _AcPMCodersAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 32)
)


class _AcPMCodersAttributesChannelsPerCoderHighThreshold_Type(Unsigned32):
    """Custom type acPMCodersAttributesChannelsPerCoderHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCodersAttributesChannelsPerCoderHighThreshold_Type.__name__ = "Unsigned32"
_AcPMCodersAttributesChannelsPerCoderHighThreshold_Object = MibScalar
acPMCodersAttributesChannelsPerCoderHighThreshold = _AcPMCodersAttributesChannelsPerCoderHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 32, 1),
    _AcPMCodersAttributesChannelsPerCoderHighThreshold_Type()
)
acPMCodersAttributesChannelsPerCoderHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCodersAttributesChannelsPerCoderHighThreshold.setStatus("current")


class _AcPMCodersAttributesChannelsPerCoderLowThreshold_Type(Unsigned32):
    """Custom type acPMCodersAttributesChannelsPerCoderLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCodersAttributesChannelsPerCoderLowThreshold_Type.__name__ = "Unsigned32"
_AcPMCodersAttributesChannelsPerCoderLowThreshold_Object = MibScalar
acPMCodersAttributesChannelsPerCoderLowThreshold = _AcPMCodersAttributesChannelsPerCoderLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 32, 2),
    _AcPMCodersAttributesChannelsPerCoderLowThreshold_Type()
)
acPMCodersAttributesChannelsPerCoderLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCodersAttributesChannelsPerCoderLowThreshold.setStatus("current")
_AcPMNetworkingAttributes_ObjectIdentity = ObjectIdentity
acPMNetworkingAttributes = _AcPMNetworkingAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33)
)


class _AcPMNetworkingAttributesPacketDelayHighThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesPacketDelayHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesPacketDelayHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesPacketDelayHighThreshold_Object = MibScalar
acPMNetworkingAttributesPacketDelayHighThreshold = _AcPMNetworkingAttributesPacketDelayHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 1),
    _AcPMNetworkingAttributesPacketDelayHighThreshold_Type()
)
acPMNetworkingAttributesPacketDelayHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesPacketDelayHighThreshold.setStatus("current")


class _AcPMNetworkingAttributesPacketDelayLowThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesPacketDelayLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesPacketDelayLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesPacketDelayLowThreshold_Object = MibScalar
acPMNetworkingAttributesPacketDelayLowThreshold = _AcPMNetworkingAttributesPacketDelayLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 2),
    _AcPMNetworkingAttributesPacketDelayLowThreshold_Type()
)
acPMNetworkingAttributesPacketDelayLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesPacketDelayLowThreshold.setStatus("current")


class _AcPMNetworkingAttributesPacketJitterHighThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesPacketJitterHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesPacketJitterHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesPacketJitterHighThreshold_Object = MibScalar
acPMNetworkingAttributesPacketJitterHighThreshold = _AcPMNetworkingAttributesPacketJitterHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 3),
    _AcPMNetworkingAttributesPacketJitterHighThreshold_Type()
)
acPMNetworkingAttributesPacketJitterHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesPacketJitterHighThreshold.setStatus("current")


class _AcPMNetworkingAttributesPacketJitterLowThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesPacketJitterLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesPacketJitterLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesPacketJitterLowThreshold_Object = MibScalar
acPMNetworkingAttributesPacketJitterLowThreshold = _AcPMNetworkingAttributesPacketJitterLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 4),
    _AcPMNetworkingAttributesPacketJitterLowThreshold_Type()
)
acPMNetworkingAttributesPacketJitterLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesPacketJitterLowThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPBytesTxHighThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPBytesTxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPBytesTxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPBytesTxHighThreshold_Object = MibScalar
acPMNetworkingAttributesRTPBytesTxHighThreshold = _AcPMNetworkingAttributesRTPBytesTxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 5),
    _AcPMNetworkingAttributesRTPBytesTxHighThreshold_Type()
)
acPMNetworkingAttributesRTPBytesTxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPBytesTxHighThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPBytesTxLowThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPBytesTxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPBytesTxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPBytesTxLowThreshold_Object = MibScalar
acPMNetworkingAttributesRTPBytesTxLowThreshold = _AcPMNetworkingAttributesRTPBytesTxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 6),
    _AcPMNetworkingAttributesRTPBytesTxLowThreshold_Type()
)
acPMNetworkingAttributesRTPBytesTxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPBytesTxLowThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPBytesRxHighThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPBytesRxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPBytesRxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPBytesRxHighThreshold_Object = MibScalar
acPMNetworkingAttributesRTPBytesRxHighThreshold = _AcPMNetworkingAttributesRTPBytesRxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 7),
    _AcPMNetworkingAttributesRTPBytesRxHighThreshold_Type()
)
acPMNetworkingAttributesRTPBytesRxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPBytesRxHighThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPBytesRxLowThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPBytesRxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPBytesRxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPBytesRxLowThreshold_Object = MibScalar
acPMNetworkingAttributesRTPBytesRxLowThreshold = _AcPMNetworkingAttributesRTPBytesRxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 8),
    _AcPMNetworkingAttributesRTPBytesRxLowThreshold_Type()
)
acPMNetworkingAttributesRTPBytesRxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPBytesRxLowThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPPacketsTxHighThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPPacketsTxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPPacketsTxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPPacketsTxHighThreshold_Object = MibScalar
acPMNetworkingAttributesRTPPacketsTxHighThreshold = _AcPMNetworkingAttributesRTPPacketsTxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 9),
    _AcPMNetworkingAttributesRTPPacketsTxHighThreshold_Type()
)
acPMNetworkingAttributesRTPPacketsTxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPPacketsTxHighThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPPacketsTxLowThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPPacketsTxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPPacketsTxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPPacketsTxLowThreshold_Object = MibScalar
acPMNetworkingAttributesRTPPacketsTxLowThreshold = _AcPMNetworkingAttributesRTPPacketsTxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 10),
    _AcPMNetworkingAttributesRTPPacketsTxLowThreshold_Type()
)
acPMNetworkingAttributesRTPPacketsTxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPPacketsTxLowThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPPacketsRxHighThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPPacketsRxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPPacketsRxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPPacketsRxHighThreshold_Object = MibScalar
acPMNetworkingAttributesRTPPacketsRxHighThreshold = _AcPMNetworkingAttributesRTPPacketsRxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 11),
    _AcPMNetworkingAttributesRTPPacketsRxHighThreshold_Type()
)
acPMNetworkingAttributesRTPPacketsRxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPPacketsRxHighThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPPacketsRxLowThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPPacketsRxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPPacketsRxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPPacketsRxLowThreshold_Object = MibScalar
acPMNetworkingAttributesRTPPacketsRxLowThreshold = _AcPMNetworkingAttributesRTPPacketsRxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 12),
    _AcPMNetworkingAttributesRTPPacketsRxLowThreshold_Type()
)
acPMNetworkingAttributesRTPPacketsRxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPPacketsRxLowThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPPacketLossRxHighThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPPacketLossRxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPPacketLossRxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPPacketLossRxHighThreshold_Object = MibScalar
acPMNetworkingAttributesRTPPacketLossRxHighThreshold = _AcPMNetworkingAttributesRTPPacketLossRxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 13),
    _AcPMNetworkingAttributesRTPPacketLossRxHighThreshold_Type()
)
acPMNetworkingAttributesRTPPacketLossRxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPPacketLossRxHighThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPPacketLossRxLowThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPPacketLossRxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPPacketLossRxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPPacketLossRxLowThreshold_Object = MibScalar
acPMNetworkingAttributesRTPPacketLossRxLowThreshold = _AcPMNetworkingAttributesRTPPacketLossRxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 14),
    _AcPMNetworkingAttributesRTPPacketLossRxLowThreshold_Type()
)
acPMNetworkingAttributesRTPPacketLossRxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPPacketLossRxLowThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPPacketLossTxHighThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPPacketLossTxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPPacketLossTxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPPacketLossTxHighThreshold_Object = MibScalar
acPMNetworkingAttributesRTPPacketLossTxHighThreshold = _AcPMNetworkingAttributesRTPPacketLossTxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 15),
    _AcPMNetworkingAttributesRTPPacketLossTxHighThreshold_Type()
)
acPMNetworkingAttributesRTPPacketLossTxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPPacketLossTxHighThreshold.setStatus("current")


class _AcPMNetworkingAttributesRTPPacketLossTxLowThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesRTPPacketLossTxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesRTPPacketLossTxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesRTPPacketLossTxLowThreshold_Object = MibScalar
acPMNetworkingAttributesRTPPacketLossTxLowThreshold = _AcPMNetworkingAttributesRTPPacketLossTxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 16),
    _AcPMNetworkingAttributesRTPPacketLossTxLowThreshold_Type()
)
acPMNetworkingAttributesRTPPacketLossTxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesRTPPacketLossTxLowThreshold.setStatus("current")


class _AcPMNetworkingAttributesModuleRTPPacketLossRxHighThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesModuleRTPPacketLossRxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesModuleRTPPacketLossRxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesModuleRTPPacketLossRxHighThreshold_Object = MibScalar
acPMNetworkingAttributesModuleRTPPacketLossRxHighThreshold = _AcPMNetworkingAttributesModuleRTPPacketLossRxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 17),
    _AcPMNetworkingAttributesModuleRTPPacketLossRxHighThreshold_Type()
)
acPMNetworkingAttributesModuleRTPPacketLossRxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesModuleRTPPacketLossRxHighThreshold.setStatus("current")


class _AcPMNetworkingAttributesModuleRTPPacketLossRxLowThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesModuleRTPPacketLossRxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesModuleRTPPacketLossRxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesModuleRTPPacketLossRxLowThreshold_Object = MibScalar
acPMNetworkingAttributesModuleRTPPacketLossRxLowThreshold = _AcPMNetworkingAttributesModuleRTPPacketLossRxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 18),
    _AcPMNetworkingAttributesModuleRTPPacketLossRxLowThreshold_Type()
)
acPMNetworkingAttributesModuleRTPPacketLossRxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesModuleRTPPacketLossRxLowThreshold.setStatus("current")


class _AcPMNetworkingAttributesModuleRTPPacketLossTxHighThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesModuleRTPPacketLossTxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesModuleRTPPacketLossTxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesModuleRTPPacketLossTxHighThreshold_Object = MibScalar
acPMNetworkingAttributesModuleRTPPacketLossTxHighThreshold = _AcPMNetworkingAttributesModuleRTPPacketLossTxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 19),
    _AcPMNetworkingAttributesModuleRTPPacketLossTxHighThreshold_Type()
)
acPMNetworkingAttributesModuleRTPPacketLossTxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesModuleRTPPacketLossTxHighThreshold.setStatus("current")


class _AcPMNetworkingAttributesModuleRTPPacketLossTxLowThreshold_Type(Unsigned32):
    """Custom type acPMNetworkingAttributesModuleRTPPacketLossTxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkingAttributesModuleRTPPacketLossTxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkingAttributesModuleRTPPacketLossTxLowThreshold_Object = MibScalar
acPMNetworkingAttributesModuleRTPPacketLossTxLowThreshold = _AcPMNetworkingAttributesModuleRTPPacketLossTxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 20),
    _AcPMNetworkingAttributesModuleRTPPacketLossTxLowThreshold_Type()
)
acPMNetworkingAttributesModuleRTPPacketLossTxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkingAttributesModuleRTPPacketLossTxLowThreshold.setStatus("current")
_AcPMMediaNetworkingAggregatedAttributes_ObjectIdentity = ObjectIdentity
acPMMediaNetworkingAggregatedAttributes = _AcPMMediaNetworkingAggregatedAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21)
)


class _AcPMMediaNetworkingAggregatedAttributesPacketDelayHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesPacketDelayHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesPacketDelayHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesPacketDelayHighThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesPacketDelayHighThreshold = _AcPMMediaNetworkingAggregatedAttributesPacketDelayHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 1),
    _AcPMMediaNetworkingAggregatedAttributesPacketDelayHighThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesPacketDelayHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesPacketDelayHighThreshold.setStatus("current")


class _AcPMMediaNetworkingAggregatedAttributesPacketDelayLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesPacketDelayLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesPacketDelayLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesPacketDelayLowThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesPacketDelayLowThreshold = _AcPMMediaNetworkingAggregatedAttributesPacketDelayLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 2),
    _AcPMMediaNetworkingAggregatedAttributesPacketDelayLowThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesPacketDelayLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesPacketDelayLowThreshold.setStatus("current")


class _AcPMMediaNetworkingAggregatedAttributesPacketJitterHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesPacketJitterHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesPacketJitterHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesPacketJitterHighThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesPacketJitterHighThreshold = _AcPMMediaNetworkingAggregatedAttributesPacketJitterHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 3),
    _AcPMMediaNetworkingAggregatedAttributesPacketJitterHighThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesPacketJitterHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesPacketJitterHighThreshold.setStatus("current")


class _AcPMMediaNetworkingAggregatedAttributesPacketJitterLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesPacketJitterLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesPacketJitterLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesPacketJitterLowThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesPacketJitterLowThreshold = _AcPMMediaNetworkingAggregatedAttributesPacketJitterLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 4),
    _AcPMMediaNetworkingAggregatedAttributesPacketJitterLowThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesPacketJitterLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesPacketJitterLowThreshold.setStatus("current")


class _AcPMMediaNetworkingAggregatedAttributesRTPBytesTxHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesRTPBytesTxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesRTPBytesTxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesRTPBytesTxHighThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesRTPBytesTxHighThreshold = _AcPMMediaNetworkingAggregatedAttributesRTPBytesTxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 5),
    _AcPMMediaNetworkingAggregatedAttributesRTPBytesTxHighThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesRTPBytesTxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesRTPBytesTxHighThreshold.setStatus("current")


class _AcPMMediaNetworkingAggregatedAttributesRTPBytesTxLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesRTPBytesTxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesRTPBytesTxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesRTPBytesTxLowThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesRTPBytesTxLowThreshold = _AcPMMediaNetworkingAggregatedAttributesRTPBytesTxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 6),
    _AcPMMediaNetworkingAggregatedAttributesRTPBytesTxLowThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesRTPBytesTxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesRTPBytesTxLowThreshold.setStatus("current")


class _AcPMMediaNetworkingAggregatedAttributesRTPBytesRxHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesRTPBytesRxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesRTPBytesRxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesRTPBytesRxHighThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesRTPBytesRxHighThreshold = _AcPMMediaNetworkingAggregatedAttributesRTPBytesRxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 7),
    _AcPMMediaNetworkingAggregatedAttributesRTPBytesRxHighThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesRTPBytesRxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesRTPBytesRxHighThreshold.setStatus("current")


class _AcPMMediaNetworkingAggregatedAttributesRTPBytesRxLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesRTPBytesRxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesRTPBytesRxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesRTPBytesRxLowThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesRTPBytesRxLowThreshold = _AcPMMediaNetworkingAggregatedAttributesRTPBytesRxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 8),
    _AcPMMediaNetworkingAggregatedAttributesRTPBytesRxLowThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesRTPBytesRxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesRTPBytesRxLowThreshold.setStatus("current")


class _AcPMMediaNetworkingAggregatedAttributesRTPPacketsTxHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesRTPPacketsTxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesRTPPacketsTxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesRTPPacketsTxHighThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesRTPPacketsTxHighThreshold = _AcPMMediaNetworkingAggregatedAttributesRTPPacketsTxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 9),
    _AcPMMediaNetworkingAggregatedAttributesRTPPacketsTxHighThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesRTPPacketsTxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesRTPPacketsTxHighThreshold.setStatus("current")


class _AcPMMediaNetworkingAggregatedAttributesRTPPacketsTxLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesRTPPacketsTxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesRTPPacketsTxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesRTPPacketsTxLowThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesRTPPacketsTxLowThreshold = _AcPMMediaNetworkingAggregatedAttributesRTPPacketsTxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 10),
    _AcPMMediaNetworkingAggregatedAttributesRTPPacketsTxLowThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesRTPPacketsTxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesRTPPacketsTxLowThreshold.setStatus("current")


class _AcPMMediaNetworkingAggregatedAttributesRTPPacketsRxHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesRTPPacketsRxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesRTPPacketsRxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesRTPPacketsRxHighThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesRTPPacketsRxHighThreshold = _AcPMMediaNetworkingAggregatedAttributesRTPPacketsRxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 11),
    _AcPMMediaNetworkingAggregatedAttributesRTPPacketsRxHighThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesRTPPacketsRxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesRTPPacketsRxHighThreshold.setStatus("current")


class _AcPMMediaNetworkingAggregatedAttributesRTPPacketsRxLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaNetworkingAggregatedAttributesRTPPacketsRxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaNetworkingAggregatedAttributesRTPPacketsRxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaNetworkingAggregatedAttributesRTPPacketsRxLowThreshold_Object = MibScalar
acPMMediaNetworkingAggregatedAttributesRTPPacketsRxLowThreshold = _AcPMMediaNetworkingAggregatedAttributesRTPPacketsRxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 33, 21, 12),
    _AcPMMediaNetworkingAggregatedAttributesRTPPacketsRxLowThreshold_Type()
)
acPMMediaNetworkingAggregatedAttributesRTPPacketsRxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaNetworkingAggregatedAttributesRTPPacketsRxLowThreshold.setStatus("current")
_AcPMMediaChannelUtilizationAttr_ObjectIdentity = ObjectIdentity
acPMMediaChannelUtilizationAttr = _AcPMMediaChannelUtilizationAttr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34)
)


class _AcPMMediaChannelUtilizationAttrFaxChannelsHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrFaxChannelsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrFaxChannelsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrFaxChannelsHighThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrFaxChannelsHighThreshold = _AcPMMediaChannelUtilizationAttrFaxChannelsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 1),
    _AcPMMediaChannelUtilizationAttrFaxChannelsHighThreshold_Type()
)
acPMMediaChannelUtilizationAttrFaxChannelsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrFaxChannelsHighThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrFaxChannelsLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrFaxChannelsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrFaxChannelsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrFaxChannelsLowThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrFaxChannelsLowThreshold = _AcPMMediaChannelUtilizationAttrFaxChannelsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 2),
    _AcPMMediaChannelUtilizationAttrFaxChannelsLowThreshold_Type()
)
acPMMediaChannelUtilizationAttrFaxChannelsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrFaxChannelsLowThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrModemChannelsHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrModemChannelsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrModemChannelsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrModemChannelsHighThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrModemChannelsHighThreshold = _AcPMMediaChannelUtilizationAttrModemChannelsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 3),
    _AcPMMediaChannelUtilizationAttrModemChannelsHighThreshold_Type()
)
acPMMediaChannelUtilizationAttrModemChannelsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrModemChannelsHighThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrModemChannelsLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrModemChannelsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrModemChannelsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrModemChannelsLowThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrModemChannelsLowThreshold = _AcPMMediaChannelUtilizationAttrModemChannelsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 4),
    _AcPMMediaChannelUtilizationAttrModemChannelsLowThreshold_Type()
)
acPMMediaChannelUtilizationAttrModemChannelsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrModemChannelsLowThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrTDM2IPChannelsHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrTDM2IPChannelsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrTDM2IPChannelsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrTDM2IPChannelsHighThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrTDM2IPChannelsHighThreshold = _AcPMMediaChannelUtilizationAttrTDM2IPChannelsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 5),
    _AcPMMediaChannelUtilizationAttrTDM2IPChannelsHighThreshold_Type()
)
acPMMediaChannelUtilizationAttrTDM2IPChannelsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrTDM2IPChannelsHighThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrTDM2IPChannelsLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrTDM2IPChannelsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrTDM2IPChannelsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrTDM2IPChannelsLowThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrTDM2IPChannelsLowThreshold = _AcPMMediaChannelUtilizationAttrTDM2IPChannelsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 6),
    _AcPMMediaChannelUtilizationAttrTDM2IPChannelsLowThreshold_Type()
)
acPMMediaChannelUtilizationAttrTDM2IPChannelsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrTDM2IPChannelsLowThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrRTPStreamsHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrRTPStreamsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrRTPStreamsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrRTPStreamsHighThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrRTPStreamsHighThreshold = _AcPMMediaChannelUtilizationAttrRTPStreamsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 7),
    _AcPMMediaChannelUtilizationAttrRTPStreamsHighThreshold_Type()
)
acPMMediaChannelUtilizationAttrRTPStreamsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrRTPStreamsHighThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrRTPStreamsLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrRTPStreamsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrRTPStreamsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrRTPStreamsLowThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrRTPStreamsLowThreshold = _AcPMMediaChannelUtilizationAttrRTPStreamsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 8),
    _AcPMMediaChannelUtilizationAttrRTPStreamsLowThreshold_Type()
)
acPMMediaChannelUtilizationAttrRTPStreamsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrRTPStreamsLowThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrSRTPStreamsHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrSRTPStreamsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrSRTPStreamsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrSRTPStreamsHighThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrSRTPStreamsHighThreshold = _AcPMMediaChannelUtilizationAttrSRTPStreamsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 9),
    _AcPMMediaChannelUtilizationAttrSRTPStreamsHighThreshold_Type()
)
acPMMediaChannelUtilizationAttrSRTPStreamsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrSRTPStreamsHighThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrSRTPStreamsLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrSRTPStreamsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrSRTPStreamsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrSRTPStreamsLowThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrSRTPStreamsLowThreshold = _AcPMMediaChannelUtilizationAttrSRTPStreamsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 10),
    _AcPMMediaChannelUtilizationAttrSRTPStreamsLowThreshold_Type()
)
acPMMediaChannelUtilizationAttrSRTPStreamsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrSRTPStreamsLowThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrMulticastRegisChanHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrMulticastRegisChanHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrMulticastRegisChanHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrMulticastRegisChanHighThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrMulticastRegisChanHighThreshold = _AcPMMediaChannelUtilizationAttrMulticastRegisChanHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 11),
    _AcPMMediaChannelUtilizationAttrMulticastRegisChanHighThreshold_Type()
)
acPMMediaChannelUtilizationAttrMulticastRegisChanHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrMulticastRegisChanHighThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrMulticastRegisChanLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrMulticastRegisChanLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrMulticastRegisChanLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrMulticastRegisChanLowThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrMulticastRegisChanLowThreshold = _AcPMMediaChannelUtilizationAttrMulticastRegisChanLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 12),
    _AcPMMediaChannelUtilizationAttrMulticastRegisChanLowThreshold_Type()
)
acPMMediaChannelUtilizationAttrMulticastRegisChanLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrMulticastRegisChanLowThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrModemRelayHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrModemRelayHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrModemRelayHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrModemRelayHighThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrModemRelayHighThreshold = _AcPMMediaChannelUtilizationAttrModemRelayHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 13),
    _AcPMMediaChannelUtilizationAttrModemRelayHighThreshold_Type()
)
acPMMediaChannelUtilizationAttrModemRelayHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrModemRelayHighThreshold.setStatus("current")


class _AcPMMediaChannelUtilizationAttrModemRelayLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaChannelUtilizationAttrModemRelayLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaChannelUtilizationAttrModemRelayLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaChannelUtilizationAttrModemRelayLowThreshold_Object = MibScalar
acPMMediaChannelUtilizationAttrModemRelayLowThreshold = _AcPMMediaChannelUtilizationAttrModemRelayLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 1, 34, 14),
    _AcPMMediaChannelUtilizationAttrModemRelayLowThreshold_Type()
)
acPMMediaChannelUtilizationAttrModemRelayLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaChannelUtilizationAttrModemRelayLowThreshold.setStatus("current")
_AcPMMediaData_ObjectIdentity = ObjectIdentity
acPMMediaData = _AcPMMediaData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2)
)


class _AcPMMediaDataAcPMMediaTimeFromStartOfInterval_Type(Unsigned32):
    """Custom type acPMMediaDataAcPMMediaTimeFromStartOfInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaDataAcPMMediaTimeFromStartOfInterval_Type.__name__ = "Unsigned32"
_AcPMMediaDataAcPMMediaTimeFromStartOfInterval_Object = MibScalar
acPMMediaDataAcPMMediaTimeFromStartOfInterval = _AcPMMediaDataAcPMMediaTimeFromStartOfInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 1),
    _AcPMMediaDataAcPMMediaTimeFromStartOfInterval_Type()
)
acPMMediaDataAcPMMediaTimeFromStartOfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaDataAcPMMediaTimeFromStartOfInterval.setStatus("current")
_AcPMDSPUtilTable_Object = MibTable
acPMDSPUtilTable = _AcPMDSPUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21)
)
if mibBuilder.loadTexts:
    acPMDSPUtilTable.setStatus("current")
_AcPMDSPUtilEntry_Object = MibTableRow
acPMDSPUtilEntry = _AcPMDSPUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21, 1)
)
acPMDSPUtilEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMDSPUtilInterval"),
)
if mibBuilder.loadTexts:
    acPMDSPUtilEntry.setStatus("current")


class _AcPMDSPUtilInterval_Type(Unsigned32):
    """Custom type acPMDSPUtilInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMDSPUtilInterval_Type.__name__ = "Unsigned32"
_AcPMDSPUtilInterval_Object = MibTableColumn
acPMDSPUtilInterval = _AcPMDSPUtilInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21, 1, 1),
    _AcPMDSPUtilInterval_Type()
)
acPMDSPUtilInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMDSPUtilInterval.setStatus("current")
_AcPMDSPUtilVal_Type = Gauge32
_AcPMDSPUtilVal_Object = MibTableColumn
acPMDSPUtilVal = _AcPMDSPUtilVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21, 1, 2),
    _AcPMDSPUtilVal_Type()
)
acPMDSPUtilVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDSPUtilVal.setStatus("current")


class _AcPMDSPUtilAverage_Type(Integer32):
    """Custom type acPMDSPUtilAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMDSPUtilAverage_Type.__name__ = "Integer32"
_AcPMDSPUtilAverage_Object = MibTableColumn
acPMDSPUtilAverage = _AcPMDSPUtilAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21, 1, 3),
    _AcPMDSPUtilAverage_Type()
)
acPMDSPUtilAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDSPUtilAverage.setStatus("current")


class _AcPMDSPUtilMax_Type(Integer32):
    """Custom type acPMDSPUtilMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMDSPUtilMax_Type.__name__ = "Integer32"
_AcPMDSPUtilMax_Object = MibTableColumn
acPMDSPUtilMax = _AcPMDSPUtilMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21, 1, 4),
    _AcPMDSPUtilMax_Type()
)
acPMDSPUtilMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDSPUtilMax.setStatus("current")


class _AcPMDSPUtilMin_Type(Integer32):
    """Custom type acPMDSPUtilMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMDSPUtilMin_Type.__name__ = "Integer32"
_AcPMDSPUtilMin_Object = MibTableColumn
acPMDSPUtilMin = _AcPMDSPUtilMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21, 1, 5),
    _AcPMDSPUtilMin_Type()
)
acPMDSPUtilMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDSPUtilMin.setStatus("current")
_AcPMDSPUtilVolume_Type = Counter32
_AcPMDSPUtilVolume_Object = MibTableColumn
acPMDSPUtilVolume = _AcPMDSPUtilVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21, 1, 6),
    _AcPMDSPUtilVolume_Type()
)
acPMDSPUtilVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDSPUtilVolume.setStatus("current")


class _AcPMDSPUtilTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMDSPUtilTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMDSPUtilTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMDSPUtilTimeBelowLowThreshold_Object = MibTableColumn
acPMDSPUtilTimeBelowLowThreshold = _AcPMDSPUtilTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21, 1, 7),
    _AcPMDSPUtilTimeBelowLowThreshold_Type()
)
acPMDSPUtilTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDSPUtilTimeBelowLowThreshold.setStatus("current")


class _AcPMDSPUtilTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMDSPUtilTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMDSPUtilTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMDSPUtilTimeBetweenThresholds_Object = MibTableColumn
acPMDSPUtilTimeBetweenThresholds = _AcPMDSPUtilTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21, 1, 8),
    _AcPMDSPUtilTimeBetweenThresholds_Type()
)
acPMDSPUtilTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDSPUtilTimeBetweenThresholds.setStatus("current")


class _AcPMDSPUtilTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMDSPUtilTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMDSPUtilTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMDSPUtilTimeAboveHighThreshold_Object = MibTableColumn
acPMDSPUtilTimeAboveHighThreshold = _AcPMDSPUtilTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21, 1, 9),
    _AcPMDSPUtilTimeAboveHighThreshold_Type()
)
acPMDSPUtilTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDSPUtilTimeAboveHighThreshold.setStatus("current")


class _AcPMDSPUtilFullDayAverage_Type(Integer32):
    """Custom type acPMDSPUtilFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMDSPUtilFullDayAverage_Type.__name__ = "Integer32"
_AcPMDSPUtilFullDayAverage_Object = MibTableColumn
acPMDSPUtilFullDayAverage = _AcPMDSPUtilFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 21, 1, 10),
    _AcPMDSPUtilFullDayAverage_Type()
)
acPMDSPUtilFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDSPUtilFullDayAverage.setStatus("current")
_AcPMChannelsPerCoderTable_Object = MibTable
acPMChannelsPerCoderTable = _AcPMChannelsPerCoderTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22)
)
if mibBuilder.loadTexts:
    acPMChannelsPerCoderTable.setStatus("current")
_AcPMChannelsPerCoderEntry_Object = MibTableRow
acPMChannelsPerCoderEntry = _AcPMChannelsPerCoderEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1)
)
acPMChannelsPerCoderEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMChannelsPerCoderCoders"),
    (0, "AC-PM-Media-MIB", "acPMChannelsPerCoderInterval"),
)
if mibBuilder.loadTexts:
    acPMChannelsPerCoderEntry.setStatus("current")


class _AcPMChannelsPerCoderCoders_Type(Integer32):
    """Custom type acPMChannelsPerCoderCoders based on Integer32"""
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
        *(("aMR", 5),
          ("eVRC", 8),
          ("eg711", 7),
          ("g711", 0),
          ("g723", 1),
          ("g728", 2),
          ("g729EV", 6),
          ("g729a", 3),
          ("g729e", 4))
    )


_AcPMChannelsPerCoderCoders_Type.__name__ = "Integer32"
_AcPMChannelsPerCoderCoders_Object = MibTableColumn
acPMChannelsPerCoderCoders = _AcPMChannelsPerCoderCoders_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1, 1),
    _AcPMChannelsPerCoderCoders_Type()
)
acPMChannelsPerCoderCoders.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMChannelsPerCoderCoders.setStatus("current")


class _AcPMChannelsPerCoderInterval_Type(Unsigned32):
    """Custom type acPMChannelsPerCoderInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMChannelsPerCoderInterval_Type.__name__ = "Unsigned32"
_AcPMChannelsPerCoderInterval_Object = MibTableColumn
acPMChannelsPerCoderInterval = _AcPMChannelsPerCoderInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1, 2),
    _AcPMChannelsPerCoderInterval_Type()
)
acPMChannelsPerCoderInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMChannelsPerCoderInterval.setStatus("current")
_AcPMChannelsPerCoderVal_Type = Gauge32
_AcPMChannelsPerCoderVal_Object = MibTableColumn
acPMChannelsPerCoderVal = _AcPMChannelsPerCoderVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1, 3),
    _AcPMChannelsPerCoderVal_Type()
)
acPMChannelsPerCoderVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMChannelsPerCoderVal.setStatus("current")


class _AcPMChannelsPerCoderAverage_Type(Integer32):
    """Custom type acPMChannelsPerCoderAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMChannelsPerCoderAverage_Type.__name__ = "Integer32"
_AcPMChannelsPerCoderAverage_Object = MibTableColumn
acPMChannelsPerCoderAverage = _AcPMChannelsPerCoderAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1, 4),
    _AcPMChannelsPerCoderAverage_Type()
)
acPMChannelsPerCoderAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMChannelsPerCoderAverage.setStatus("current")


class _AcPMChannelsPerCoderMax_Type(Integer32):
    """Custom type acPMChannelsPerCoderMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMChannelsPerCoderMax_Type.__name__ = "Integer32"
_AcPMChannelsPerCoderMax_Object = MibTableColumn
acPMChannelsPerCoderMax = _AcPMChannelsPerCoderMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1, 5),
    _AcPMChannelsPerCoderMax_Type()
)
acPMChannelsPerCoderMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMChannelsPerCoderMax.setStatus("current")


class _AcPMChannelsPerCoderMin_Type(Integer32):
    """Custom type acPMChannelsPerCoderMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMChannelsPerCoderMin_Type.__name__ = "Integer32"
_AcPMChannelsPerCoderMin_Object = MibTableColumn
acPMChannelsPerCoderMin = _AcPMChannelsPerCoderMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1, 6),
    _AcPMChannelsPerCoderMin_Type()
)
acPMChannelsPerCoderMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMChannelsPerCoderMin.setStatus("current")
_AcPMChannelsPerCoderVolume_Type = Counter32
_AcPMChannelsPerCoderVolume_Object = MibTableColumn
acPMChannelsPerCoderVolume = _AcPMChannelsPerCoderVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1, 7),
    _AcPMChannelsPerCoderVolume_Type()
)
acPMChannelsPerCoderVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMChannelsPerCoderVolume.setStatus("current")


class _AcPMChannelsPerCoderTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMChannelsPerCoderTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMChannelsPerCoderTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMChannelsPerCoderTimeBelowLowThreshold_Object = MibTableColumn
acPMChannelsPerCoderTimeBelowLowThreshold = _AcPMChannelsPerCoderTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1, 8),
    _AcPMChannelsPerCoderTimeBelowLowThreshold_Type()
)
acPMChannelsPerCoderTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMChannelsPerCoderTimeBelowLowThreshold.setStatus("current")


class _AcPMChannelsPerCoderTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMChannelsPerCoderTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMChannelsPerCoderTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMChannelsPerCoderTimeBetweenThresholds_Object = MibTableColumn
acPMChannelsPerCoderTimeBetweenThresholds = _AcPMChannelsPerCoderTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1, 9),
    _AcPMChannelsPerCoderTimeBetweenThresholds_Type()
)
acPMChannelsPerCoderTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMChannelsPerCoderTimeBetweenThresholds.setStatus("current")


class _AcPMChannelsPerCoderTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMChannelsPerCoderTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMChannelsPerCoderTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMChannelsPerCoderTimeAboveHighThreshold_Object = MibTableColumn
acPMChannelsPerCoderTimeAboveHighThreshold = _AcPMChannelsPerCoderTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1, 10),
    _AcPMChannelsPerCoderTimeAboveHighThreshold_Type()
)
acPMChannelsPerCoderTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMChannelsPerCoderTimeAboveHighThreshold.setStatus("current")


class _AcPMChannelsPerCoderFullDayAverage_Type(Integer32):
    """Custom type acPMChannelsPerCoderFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMChannelsPerCoderFullDayAverage_Type.__name__ = "Integer32"
_AcPMChannelsPerCoderFullDayAverage_Object = MibTableColumn
acPMChannelsPerCoderFullDayAverage = _AcPMChannelsPerCoderFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 22, 1, 11),
    _AcPMChannelsPerCoderFullDayAverage_Type()
)
acPMChannelsPerCoderFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMChannelsPerCoderFullDayAverage.setStatus("current")
_AcPMRobustDiscardTable_Object = MibTable
acPMRobustDiscardTable = _AcPMRobustDiscardTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 23)
)
if mibBuilder.loadTexts:
    acPMRobustDiscardTable.setStatus("current")
_AcPMRobustDiscardEntry_Object = MibTableRow
acPMRobustDiscardEntry = _AcPMRobustDiscardEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 23, 1)
)
acPMRobustDiscardEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMRobustDiscardInterval"),
)
if mibBuilder.loadTexts:
    acPMRobustDiscardEntry.setStatus("current")


class _AcPMRobustDiscardInterval_Type(Unsigned32):
    """Custom type acPMRobustDiscardInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRobustDiscardInterval_Type.__name__ = "Unsigned32"
_AcPMRobustDiscardInterval_Object = MibTableColumn
acPMRobustDiscardInterval = _AcPMRobustDiscardInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 23, 1, 1),
    _AcPMRobustDiscardInterval_Type()
)
acPMRobustDiscardInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRobustDiscardInterval.setStatus("current")
_AcPMRobustDiscardVal_Type = Counter32
_AcPMRobustDiscardVal_Object = MibTableColumn
acPMRobustDiscardVal = _AcPMRobustDiscardVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 23, 1, 2),
    _AcPMRobustDiscardVal_Type()
)
acPMRobustDiscardVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRobustDiscardVal.setStatus("current")
_AcPMMediaNetworking_ObjectIdentity = ObjectIdentity
acPMMediaNetworking = _AcPMMediaNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31)
)
_AcPMPacketDelayTable_Object = MibTable
acPMPacketDelayTable = _AcPMPacketDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1)
)
if mibBuilder.loadTexts:
    acPMPacketDelayTable.setStatus("current")
_AcPMPacketDelayEntry_Object = MibTableRow
acPMPacketDelayEntry = _AcPMPacketDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1)
)
acPMPacketDelayEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMPacketDelayTrunkNum"),
    (0, "AC-PM-Media-MIB", "acPMPacketDelayInterval"),
)
if mibBuilder.loadTexts:
    acPMPacketDelayEntry.setStatus("current")


class _AcPMPacketDelayTrunkNum_Type(Unsigned32):
    """Custom type acPMPacketDelayTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMPacketDelayTrunkNum_Type.__name__ = "Unsigned32"
_AcPMPacketDelayTrunkNum_Object = MibTableColumn
acPMPacketDelayTrunkNum = _AcPMPacketDelayTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1, 1),
    _AcPMPacketDelayTrunkNum_Type()
)
acPMPacketDelayTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPacketDelayTrunkNum.setStatus("current")


class _AcPMPacketDelayInterval_Type(Unsigned32):
    """Custom type acPMPacketDelayInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMPacketDelayInterval_Type.__name__ = "Unsigned32"
_AcPMPacketDelayInterval_Object = MibTableColumn
acPMPacketDelayInterval = _AcPMPacketDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1, 2),
    _AcPMPacketDelayInterval_Type()
)
acPMPacketDelayInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPacketDelayInterval.setStatus("current")
_AcPMPacketDelayVal_Type = Gauge32
_AcPMPacketDelayVal_Object = MibTableColumn
acPMPacketDelayVal = _AcPMPacketDelayVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1, 3),
    _AcPMPacketDelayVal_Type()
)
acPMPacketDelayVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketDelayVal.setStatus("current")


class _AcPMPacketDelayAverage_Type(Integer32):
    """Custom type acPMPacketDelayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPacketDelayAverage_Type.__name__ = "Integer32"
_AcPMPacketDelayAverage_Object = MibTableColumn
acPMPacketDelayAverage = _AcPMPacketDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1, 4),
    _AcPMPacketDelayAverage_Type()
)
acPMPacketDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketDelayAverage.setStatus("current")


class _AcPMPacketDelayMax_Type(Integer32):
    """Custom type acPMPacketDelayMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPacketDelayMax_Type.__name__ = "Integer32"
_AcPMPacketDelayMax_Object = MibTableColumn
acPMPacketDelayMax = _AcPMPacketDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1, 5),
    _AcPMPacketDelayMax_Type()
)
acPMPacketDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketDelayMax.setStatus("current")


class _AcPMPacketDelayMin_Type(Integer32):
    """Custom type acPMPacketDelayMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPacketDelayMin_Type.__name__ = "Integer32"
_AcPMPacketDelayMin_Object = MibTableColumn
acPMPacketDelayMin = _AcPMPacketDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1, 6),
    _AcPMPacketDelayMin_Type()
)
acPMPacketDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketDelayMin.setStatus("current")
_AcPMPacketDelayVolume_Type = Counter32
_AcPMPacketDelayVolume_Object = MibTableColumn
acPMPacketDelayVolume = _AcPMPacketDelayVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1, 7),
    _AcPMPacketDelayVolume_Type()
)
acPMPacketDelayVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketDelayVolume.setStatus("current")


class _AcPMPacketDelayTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMPacketDelayTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMPacketDelayTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMPacketDelayTimeBelowLowThreshold_Object = MibTableColumn
acPMPacketDelayTimeBelowLowThreshold = _AcPMPacketDelayTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1, 8),
    _AcPMPacketDelayTimeBelowLowThreshold_Type()
)
acPMPacketDelayTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketDelayTimeBelowLowThreshold.setStatus("current")


class _AcPMPacketDelayTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMPacketDelayTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMPacketDelayTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMPacketDelayTimeBetweenThresholds_Object = MibTableColumn
acPMPacketDelayTimeBetweenThresholds = _AcPMPacketDelayTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1, 9),
    _AcPMPacketDelayTimeBetweenThresholds_Type()
)
acPMPacketDelayTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketDelayTimeBetweenThresholds.setStatus("current")


class _AcPMPacketDelayTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMPacketDelayTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMPacketDelayTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMPacketDelayTimeAboveHighThreshold_Object = MibTableColumn
acPMPacketDelayTimeAboveHighThreshold = _AcPMPacketDelayTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1, 10),
    _AcPMPacketDelayTimeAboveHighThreshold_Type()
)
acPMPacketDelayTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketDelayTimeAboveHighThreshold.setStatus("current")


class _AcPMPacketDelayFullDayAverage_Type(Integer32):
    """Custom type acPMPacketDelayFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPacketDelayFullDayAverage_Type.__name__ = "Integer32"
_AcPMPacketDelayFullDayAverage_Object = MibTableColumn
acPMPacketDelayFullDayAverage = _AcPMPacketDelayFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 1, 1, 11),
    _AcPMPacketDelayFullDayAverage_Type()
)
acPMPacketDelayFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketDelayFullDayAverage.setStatus("current")
_AcPMPacketJitterTable_Object = MibTable
acPMPacketJitterTable = _AcPMPacketJitterTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2)
)
if mibBuilder.loadTexts:
    acPMPacketJitterTable.setStatus("current")
_AcPMPacketJitterEntry_Object = MibTableRow
acPMPacketJitterEntry = _AcPMPacketJitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1)
)
acPMPacketJitterEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMPacketJitterTrunkNum"),
    (0, "AC-PM-Media-MIB", "acPMPacketJitterInterval"),
)
if mibBuilder.loadTexts:
    acPMPacketJitterEntry.setStatus("current")


class _AcPMPacketJitterTrunkNum_Type(Unsigned32):
    """Custom type acPMPacketJitterTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMPacketJitterTrunkNum_Type.__name__ = "Unsigned32"
_AcPMPacketJitterTrunkNum_Object = MibTableColumn
acPMPacketJitterTrunkNum = _AcPMPacketJitterTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1, 1),
    _AcPMPacketJitterTrunkNum_Type()
)
acPMPacketJitterTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPacketJitterTrunkNum.setStatus("current")


class _AcPMPacketJitterInterval_Type(Unsigned32):
    """Custom type acPMPacketJitterInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMPacketJitterInterval_Type.__name__ = "Unsigned32"
_AcPMPacketJitterInterval_Object = MibTableColumn
acPMPacketJitterInterval = _AcPMPacketJitterInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1, 2),
    _AcPMPacketJitterInterval_Type()
)
acPMPacketJitterInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMPacketJitterInterval.setStatus("current")
_AcPMPacketJitterVal_Type = Gauge32
_AcPMPacketJitterVal_Object = MibTableColumn
acPMPacketJitterVal = _AcPMPacketJitterVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1, 3),
    _AcPMPacketJitterVal_Type()
)
acPMPacketJitterVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketJitterVal.setStatus("current")


class _AcPMPacketJitterAverage_Type(Integer32):
    """Custom type acPMPacketJitterAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPacketJitterAverage_Type.__name__ = "Integer32"
_AcPMPacketJitterAverage_Object = MibTableColumn
acPMPacketJitterAverage = _AcPMPacketJitterAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1, 4),
    _AcPMPacketJitterAverage_Type()
)
acPMPacketJitterAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketJitterAverage.setStatus("current")


class _AcPMPacketJitterMax_Type(Integer32):
    """Custom type acPMPacketJitterMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPacketJitterMax_Type.__name__ = "Integer32"
_AcPMPacketJitterMax_Object = MibTableColumn
acPMPacketJitterMax = _AcPMPacketJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1, 5),
    _AcPMPacketJitterMax_Type()
)
acPMPacketJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketJitterMax.setStatus("current")


class _AcPMPacketJitterMin_Type(Integer32):
    """Custom type acPMPacketJitterMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPacketJitterMin_Type.__name__ = "Integer32"
_AcPMPacketJitterMin_Object = MibTableColumn
acPMPacketJitterMin = _AcPMPacketJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1, 6),
    _AcPMPacketJitterMin_Type()
)
acPMPacketJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketJitterMin.setStatus("current")
_AcPMPacketJitterVolume_Type = Counter32
_AcPMPacketJitterVolume_Object = MibTableColumn
acPMPacketJitterVolume = _AcPMPacketJitterVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1, 7),
    _AcPMPacketJitterVolume_Type()
)
acPMPacketJitterVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketJitterVolume.setStatus("current")


class _AcPMPacketJitterTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMPacketJitterTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMPacketJitterTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMPacketJitterTimeBelowLowThreshold_Object = MibTableColumn
acPMPacketJitterTimeBelowLowThreshold = _AcPMPacketJitterTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1, 8),
    _AcPMPacketJitterTimeBelowLowThreshold_Type()
)
acPMPacketJitterTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketJitterTimeBelowLowThreshold.setStatus("current")


class _AcPMPacketJitterTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMPacketJitterTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMPacketJitterTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMPacketJitterTimeBetweenThresholds_Object = MibTableColumn
acPMPacketJitterTimeBetweenThresholds = _AcPMPacketJitterTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1, 9),
    _AcPMPacketJitterTimeBetweenThresholds_Type()
)
acPMPacketJitterTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketJitterTimeBetweenThresholds.setStatus("current")


class _AcPMPacketJitterTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMPacketJitterTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMPacketJitterTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMPacketJitterTimeAboveHighThreshold_Object = MibTableColumn
acPMPacketJitterTimeAboveHighThreshold = _AcPMPacketJitterTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1, 10),
    _AcPMPacketJitterTimeAboveHighThreshold_Type()
)
acPMPacketJitterTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketJitterTimeAboveHighThreshold.setStatus("current")


class _AcPMPacketJitterFullDayAverage_Type(Integer32):
    """Custom type acPMPacketJitterFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMPacketJitterFullDayAverage_Type.__name__ = "Integer32"
_AcPMPacketJitterFullDayAverage_Object = MibTableColumn
acPMPacketJitterFullDayAverage = _AcPMPacketJitterFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 2, 1, 11),
    _AcPMPacketJitterFullDayAverage_Type()
)
acPMPacketJitterFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMPacketJitterFullDayAverage.setStatus("current")
_AcPMRTPBytesTxTable_Object = MibTable
acPMRTPBytesTxTable = _AcPMRTPBytesTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3)
)
if mibBuilder.loadTexts:
    acPMRTPBytesTxTable.setStatus("current")
_AcPMRTPBytesTxEntry_Object = MibTableRow
acPMRTPBytesTxEntry = _AcPMRTPBytesTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1)
)
acPMRTPBytesTxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMRTPBytesTxTrunkNum"),
    (0, "AC-PM-Media-MIB", "acPMRTPBytesTxInterval"),
)
if mibBuilder.loadTexts:
    acPMRTPBytesTxEntry.setStatus("current")


class _AcPMRTPBytesTxTrunkNum_Type(Unsigned32):
    """Custom type acPMRTPBytesTxTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMRTPBytesTxTrunkNum_Type.__name__ = "Unsigned32"
_AcPMRTPBytesTxTrunkNum_Object = MibTableColumn
acPMRTPBytesTxTrunkNum = _AcPMRTPBytesTxTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1, 1),
    _AcPMRTPBytesTxTrunkNum_Type()
)
acPMRTPBytesTxTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPBytesTxTrunkNum.setStatus("current")


class _AcPMRTPBytesTxInterval_Type(Unsigned32):
    """Custom type acPMRTPBytesTxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRTPBytesTxInterval_Type.__name__ = "Unsigned32"
_AcPMRTPBytesTxInterval_Object = MibTableColumn
acPMRTPBytesTxInterval = _AcPMRTPBytesTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1, 2),
    _AcPMRTPBytesTxInterval_Type()
)
acPMRTPBytesTxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPBytesTxInterval.setStatus("current")
_AcPMRTPBytesTxVal_Type = Gauge32
_AcPMRTPBytesTxVal_Object = MibTableColumn
acPMRTPBytesTxVal = _AcPMRTPBytesTxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1, 3),
    _AcPMRTPBytesTxVal_Type()
)
acPMRTPBytesTxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesTxVal.setStatus("current")


class _AcPMRTPBytesTxAverage_Type(Integer32):
    """Custom type acPMRTPBytesTxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPBytesTxAverage_Type.__name__ = "Integer32"
_AcPMRTPBytesTxAverage_Object = MibTableColumn
acPMRTPBytesTxAverage = _AcPMRTPBytesTxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1, 4),
    _AcPMRTPBytesTxAverage_Type()
)
acPMRTPBytesTxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesTxAverage.setStatus("current")


class _AcPMRTPBytesTxMax_Type(Integer32):
    """Custom type acPMRTPBytesTxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPBytesTxMax_Type.__name__ = "Integer32"
_AcPMRTPBytesTxMax_Object = MibTableColumn
acPMRTPBytesTxMax = _AcPMRTPBytesTxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1, 5),
    _AcPMRTPBytesTxMax_Type()
)
acPMRTPBytesTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesTxMax.setStatus("current")


class _AcPMRTPBytesTxMin_Type(Integer32):
    """Custom type acPMRTPBytesTxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPBytesTxMin_Type.__name__ = "Integer32"
_AcPMRTPBytesTxMin_Object = MibTableColumn
acPMRTPBytesTxMin = _AcPMRTPBytesTxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1, 6),
    _AcPMRTPBytesTxMin_Type()
)
acPMRTPBytesTxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesTxMin.setStatus("current")
_AcPMRTPBytesTxVolume_Type = Counter32
_AcPMRTPBytesTxVolume_Object = MibTableColumn
acPMRTPBytesTxVolume = _AcPMRTPBytesTxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1, 7),
    _AcPMRTPBytesTxVolume_Type()
)
acPMRTPBytesTxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesTxVolume.setStatus("current")


class _AcPMRTPBytesTxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRTPBytesTxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPBytesTxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRTPBytesTxTimeBelowLowThreshold_Object = MibTableColumn
acPMRTPBytesTxTimeBelowLowThreshold = _AcPMRTPBytesTxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1, 8),
    _AcPMRTPBytesTxTimeBelowLowThreshold_Type()
)
acPMRTPBytesTxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesTxTimeBelowLowThreshold.setStatus("current")


class _AcPMRTPBytesTxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRTPBytesTxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPBytesTxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRTPBytesTxTimeBetweenThresholds_Object = MibTableColumn
acPMRTPBytesTxTimeBetweenThresholds = _AcPMRTPBytesTxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1, 9),
    _AcPMRTPBytesTxTimeBetweenThresholds_Type()
)
acPMRTPBytesTxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesTxTimeBetweenThresholds.setStatus("current")


class _AcPMRTPBytesTxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRTPBytesTxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPBytesTxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRTPBytesTxTimeAboveHighThreshold_Object = MibTableColumn
acPMRTPBytesTxTimeAboveHighThreshold = _AcPMRTPBytesTxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1, 10),
    _AcPMRTPBytesTxTimeAboveHighThreshold_Type()
)
acPMRTPBytesTxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesTxTimeAboveHighThreshold.setStatus("current")


class _AcPMRTPBytesTxFullDayAverage_Type(Integer32):
    """Custom type acPMRTPBytesTxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPBytesTxFullDayAverage_Type.__name__ = "Integer32"
_AcPMRTPBytesTxFullDayAverage_Object = MibTableColumn
acPMRTPBytesTxFullDayAverage = _AcPMRTPBytesTxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 3, 1, 11),
    _AcPMRTPBytesTxFullDayAverage_Type()
)
acPMRTPBytesTxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesTxFullDayAverage.setStatus("current")
_AcPMRTPBytesRxTable_Object = MibTable
acPMRTPBytesRxTable = _AcPMRTPBytesRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4)
)
if mibBuilder.loadTexts:
    acPMRTPBytesRxTable.setStatus("current")
_AcPMRTPBytesRxEntry_Object = MibTableRow
acPMRTPBytesRxEntry = _AcPMRTPBytesRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1)
)
acPMRTPBytesRxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMRTPBytesRxTrunkNum"),
    (0, "AC-PM-Media-MIB", "acPMRTPBytesRxInterval"),
)
if mibBuilder.loadTexts:
    acPMRTPBytesRxEntry.setStatus("current")


class _AcPMRTPBytesRxTrunkNum_Type(Unsigned32):
    """Custom type acPMRTPBytesRxTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMRTPBytesRxTrunkNum_Type.__name__ = "Unsigned32"
_AcPMRTPBytesRxTrunkNum_Object = MibTableColumn
acPMRTPBytesRxTrunkNum = _AcPMRTPBytesRxTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1, 1),
    _AcPMRTPBytesRxTrunkNum_Type()
)
acPMRTPBytesRxTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPBytesRxTrunkNum.setStatus("current")


class _AcPMRTPBytesRxInterval_Type(Unsigned32):
    """Custom type acPMRTPBytesRxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRTPBytesRxInterval_Type.__name__ = "Unsigned32"
_AcPMRTPBytesRxInterval_Object = MibTableColumn
acPMRTPBytesRxInterval = _AcPMRTPBytesRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1, 2),
    _AcPMRTPBytesRxInterval_Type()
)
acPMRTPBytesRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPBytesRxInterval.setStatus("current")
_AcPMRTPBytesRxVal_Type = Gauge32
_AcPMRTPBytesRxVal_Object = MibTableColumn
acPMRTPBytesRxVal = _AcPMRTPBytesRxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1, 3),
    _AcPMRTPBytesRxVal_Type()
)
acPMRTPBytesRxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesRxVal.setStatus("current")


class _AcPMRTPBytesRxAverage_Type(Integer32):
    """Custom type acPMRTPBytesRxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPBytesRxAverage_Type.__name__ = "Integer32"
_AcPMRTPBytesRxAverage_Object = MibTableColumn
acPMRTPBytesRxAverage = _AcPMRTPBytesRxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1, 4),
    _AcPMRTPBytesRxAverage_Type()
)
acPMRTPBytesRxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesRxAverage.setStatus("current")


class _AcPMRTPBytesRxMax_Type(Integer32):
    """Custom type acPMRTPBytesRxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPBytesRxMax_Type.__name__ = "Integer32"
_AcPMRTPBytesRxMax_Object = MibTableColumn
acPMRTPBytesRxMax = _AcPMRTPBytesRxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1, 5),
    _AcPMRTPBytesRxMax_Type()
)
acPMRTPBytesRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesRxMax.setStatus("current")


class _AcPMRTPBytesRxMin_Type(Integer32):
    """Custom type acPMRTPBytesRxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPBytesRxMin_Type.__name__ = "Integer32"
_AcPMRTPBytesRxMin_Object = MibTableColumn
acPMRTPBytesRxMin = _AcPMRTPBytesRxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1, 6),
    _AcPMRTPBytesRxMin_Type()
)
acPMRTPBytesRxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesRxMin.setStatus("current")
_AcPMRTPBytesRxVolume_Type = Counter32
_AcPMRTPBytesRxVolume_Object = MibTableColumn
acPMRTPBytesRxVolume = _AcPMRTPBytesRxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1, 7),
    _AcPMRTPBytesRxVolume_Type()
)
acPMRTPBytesRxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesRxVolume.setStatus("current")


class _AcPMRTPBytesRxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRTPBytesRxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPBytesRxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRTPBytesRxTimeBelowLowThreshold_Object = MibTableColumn
acPMRTPBytesRxTimeBelowLowThreshold = _AcPMRTPBytesRxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1, 8),
    _AcPMRTPBytesRxTimeBelowLowThreshold_Type()
)
acPMRTPBytesRxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesRxTimeBelowLowThreshold.setStatus("current")


class _AcPMRTPBytesRxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRTPBytesRxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPBytesRxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRTPBytesRxTimeBetweenThresholds_Object = MibTableColumn
acPMRTPBytesRxTimeBetweenThresholds = _AcPMRTPBytesRxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1, 9),
    _AcPMRTPBytesRxTimeBetweenThresholds_Type()
)
acPMRTPBytesRxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesRxTimeBetweenThresholds.setStatus("current")


class _AcPMRTPBytesRxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRTPBytesRxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPBytesRxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRTPBytesRxTimeAboveHighThreshold_Object = MibTableColumn
acPMRTPBytesRxTimeAboveHighThreshold = _AcPMRTPBytesRxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1, 10),
    _AcPMRTPBytesRxTimeAboveHighThreshold_Type()
)
acPMRTPBytesRxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesRxTimeAboveHighThreshold.setStatus("current")


class _AcPMRTPBytesRxFullDayAverage_Type(Integer32):
    """Custom type acPMRTPBytesRxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPBytesRxFullDayAverage_Type.__name__ = "Integer32"
_AcPMRTPBytesRxFullDayAverage_Object = MibTableColumn
acPMRTPBytesRxFullDayAverage = _AcPMRTPBytesRxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 4, 1, 11),
    _AcPMRTPBytesRxFullDayAverage_Type()
)
acPMRTPBytesRxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPBytesRxFullDayAverage.setStatus("current")
_AcPMRTPPacketsTxTable_Object = MibTable
acPMRTPPacketsTxTable = _AcPMRTPPacketsTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5)
)
if mibBuilder.loadTexts:
    acPMRTPPacketsTxTable.setStatus("current")
_AcPMRTPPacketsTxEntry_Object = MibTableRow
acPMRTPPacketsTxEntry = _AcPMRTPPacketsTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1)
)
acPMRTPPacketsTxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMRTPPacketsTxTrunkNum"),
    (0, "AC-PM-Media-MIB", "acPMRTPPacketsTxInterval"),
)
if mibBuilder.loadTexts:
    acPMRTPPacketsTxEntry.setStatus("current")


class _AcPMRTPPacketsTxTrunkNum_Type(Unsigned32):
    """Custom type acPMRTPPacketsTxTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMRTPPacketsTxTrunkNum_Type.__name__ = "Unsigned32"
_AcPMRTPPacketsTxTrunkNum_Object = MibTableColumn
acPMRTPPacketsTxTrunkNum = _AcPMRTPPacketsTxTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 1),
    _AcPMRTPPacketsTxTrunkNum_Type()
)
acPMRTPPacketsTxTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxTrunkNum.setStatus("current")


class _AcPMRTPPacketsTxInterval_Type(Unsigned32):
    """Custom type acPMRTPPacketsTxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRTPPacketsTxInterval_Type.__name__ = "Unsigned32"
_AcPMRTPPacketsTxInterval_Object = MibTableColumn
acPMRTPPacketsTxInterval = _AcPMRTPPacketsTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 2),
    _AcPMRTPPacketsTxInterval_Type()
)
acPMRTPPacketsTxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxInterval.setStatus("current")
_AcPMRTPPacketsTxVal_Type = Gauge32
_AcPMRTPPacketsTxVal_Object = MibTableColumn
acPMRTPPacketsTxVal = _AcPMRTPPacketsTxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 3),
    _AcPMRTPPacketsTxVal_Type()
)
acPMRTPPacketsTxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxVal.setStatus("current")


class _AcPMRTPPacketsTxAverage_Type(Integer32):
    """Custom type acPMRTPPacketsTxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketsTxAverage_Type.__name__ = "Integer32"
_AcPMRTPPacketsTxAverage_Object = MibTableColumn
acPMRTPPacketsTxAverage = _AcPMRTPPacketsTxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 4),
    _AcPMRTPPacketsTxAverage_Type()
)
acPMRTPPacketsTxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxAverage.setStatus("current")


class _AcPMRTPPacketsTxMax_Type(Integer32):
    """Custom type acPMRTPPacketsTxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketsTxMax_Type.__name__ = "Integer32"
_AcPMRTPPacketsTxMax_Object = MibTableColumn
acPMRTPPacketsTxMax = _AcPMRTPPacketsTxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 5),
    _AcPMRTPPacketsTxMax_Type()
)
acPMRTPPacketsTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxMax.setStatus("current")


class _AcPMRTPPacketsTxMin_Type(Integer32):
    """Custom type acPMRTPPacketsTxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketsTxMin_Type.__name__ = "Integer32"
_AcPMRTPPacketsTxMin_Object = MibTableColumn
acPMRTPPacketsTxMin = _AcPMRTPPacketsTxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 6),
    _AcPMRTPPacketsTxMin_Type()
)
acPMRTPPacketsTxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxMin.setStatus("current")
_AcPMRTPPacketsTxVolume_Type = Counter32
_AcPMRTPPacketsTxVolume_Object = MibTableColumn
acPMRTPPacketsTxVolume = _AcPMRTPPacketsTxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 7),
    _AcPMRTPPacketsTxVolume_Type()
)
acPMRTPPacketsTxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxVolume.setStatus("current")


class _AcPMRTPPacketsTxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRTPPacketsTxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketsTxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRTPPacketsTxTimeBelowLowThreshold_Object = MibTableColumn
acPMRTPPacketsTxTimeBelowLowThreshold = _AcPMRTPPacketsTxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 8),
    _AcPMRTPPacketsTxTimeBelowLowThreshold_Type()
)
acPMRTPPacketsTxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxTimeBelowLowThreshold.setStatus("current")


class _AcPMRTPPacketsTxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRTPPacketsTxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketsTxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRTPPacketsTxTimeBetweenThresholds_Object = MibTableColumn
acPMRTPPacketsTxTimeBetweenThresholds = _AcPMRTPPacketsTxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 9),
    _AcPMRTPPacketsTxTimeBetweenThresholds_Type()
)
acPMRTPPacketsTxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxTimeBetweenThresholds.setStatus("current")


class _AcPMRTPPacketsTxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRTPPacketsTxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketsTxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRTPPacketsTxTimeAboveHighThreshold_Object = MibTableColumn
acPMRTPPacketsTxTimeAboveHighThreshold = _AcPMRTPPacketsTxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 10),
    _AcPMRTPPacketsTxTimeAboveHighThreshold_Type()
)
acPMRTPPacketsTxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxTimeAboveHighThreshold.setStatus("current")


class _AcPMRTPPacketsTxFullDayAverage_Type(Integer32):
    """Custom type acPMRTPPacketsTxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketsTxFullDayAverage_Type.__name__ = "Integer32"
_AcPMRTPPacketsTxFullDayAverage_Object = MibTableColumn
acPMRTPPacketsTxFullDayAverage = _AcPMRTPPacketsTxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 11),
    _AcPMRTPPacketsTxFullDayAverage_Type()
)
acPMRTPPacketsTxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxFullDayAverage.setStatus("current")


class _AcPMRTPPacketsTxTotal_Type(Integer32):
    """Custom type acPMRTPPacketsTxTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketsTxTotal_Type.__name__ = "Integer32"
_AcPMRTPPacketsTxTotal_Object = MibTableColumn
acPMRTPPacketsTxTotal = _AcPMRTPPacketsTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 5, 1, 12),
    _AcPMRTPPacketsTxTotal_Type()
)
acPMRTPPacketsTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsTxTotal.setStatus("current")
_AcPMRTPPacketsRxTable_Object = MibTable
acPMRTPPacketsRxTable = _AcPMRTPPacketsRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6)
)
if mibBuilder.loadTexts:
    acPMRTPPacketsRxTable.setStatus("current")
_AcPMRTPPacketsRxEntry_Object = MibTableRow
acPMRTPPacketsRxEntry = _AcPMRTPPacketsRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1)
)
acPMRTPPacketsRxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMRTPPacketsRxTrunkNum"),
    (0, "AC-PM-Media-MIB", "acPMRTPPacketsRxInterval"),
)
if mibBuilder.loadTexts:
    acPMRTPPacketsRxEntry.setStatus("current")


class _AcPMRTPPacketsRxTrunkNum_Type(Unsigned32):
    """Custom type acPMRTPPacketsRxTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMRTPPacketsRxTrunkNum_Type.__name__ = "Unsigned32"
_AcPMRTPPacketsRxTrunkNum_Object = MibTableColumn
acPMRTPPacketsRxTrunkNum = _AcPMRTPPacketsRxTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 1),
    _AcPMRTPPacketsRxTrunkNum_Type()
)
acPMRTPPacketsRxTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxTrunkNum.setStatus("current")


class _AcPMRTPPacketsRxInterval_Type(Unsigned32):
    """Custom type acPMRTPPacketsRxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRTPPacketsRxInterval_Type.__name__ = "Unsigned32"
_AcPMRTPPacketsRxInterval_Object = MibTableColumn
acPMRTPPacketsRxInterval = _AcPMRTPPacketsRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 2),
    _AcPMRTPPacketsRxInterval_Type()
)
acPMRTPPacketsRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxInterval.setStatus("current")
_AcPMRTPPacketsRxVal_Type = Gauge32
_AcPMRTPPacketsRxVal_Object = MibTableColumn
acPMRTPPacketsRxVal = _AcPMRTPPacketsRxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 3),
    _AcPMRTPPacketsRxVal_Type()
)
acPMRTPPacketsRxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxVal.setStatus("current")


class _AcPMRTPPacketsRxAverage_Type(Integer32):
    """Custom type acPMRTPPacketsRxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketsRxAverage_Type.__name__ = "Integer32"
_AcPMRTPPacketsRxAverage_Object = MibTableColumn
acPMRTPPacketsRxAverage = _AcPMRTPPacketsRxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 4),
    _AcPMRTPPacketsRxAverage_Type()
)
acPMRTPPacketsRxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxAverage.setStatus("current")


class _AcPMRTPPacketsRxMax_Type(Integer32):
    """Custom type acPMRTPPacketsRxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketsRxMax_Type.__name__ = "Integer32"
_AcPMRTPPacketsRxMax_Object = MibTableColumn
acPMRTPPacketsRxMax = _AcPMRTPPacketsRxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 5),
    _AcPMRTPPacketsRxMax_Type()
)
acPMRTPPacketsRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxMax.setStatus("current")


class _AcPMRTPPacketsRxMin_Type(Integer32):
    """Custom type acPMRTPPacketsRxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketsRxMin_Type.__name__ = "Integer32"
_AcPMRTPPacketsRxMin_Object = MibTableColumn
acPMRTPPacketsRxMin = _AcPMRTPPacketsRxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 6),
    _AcPMRTPPacketsRxMin_Type()
)
acPMRTPPacketsRxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxMin.setStatus("current")
_AcPMRTPPacketsRxVolume_Type = Counter32
_AcPMRTPPacketsRxVolume_Object = MibTableColumn
acPMRTPPacketsRxVolume = _AcPMRTPPacketsRxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 7),
    _AcPMRTPPacketsRxVolume_Type()
)
acPMRTPPacketsRxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxVolume.setStatus("current")


class _AcPMRTPPacketsRxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRTPPacketsRxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketsRxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRTPPacketsRxTimeBelowLowThreshold_Object = MibTableColumn
acPMRTPPacketsRxTimeBelowLowThreshold = _AcPMRTPPacketsRxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 8),
    _AcPMRTPPacketsRxTimeBelowLowThreshold_Type()
)
acPMRTPPacketsRxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxTimeBelowLowThreshold.setStatus("current")


class _AcPMRTPPacketsRxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRTPPacketsRxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketsRxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRTPPacketsRxTimeBetweenThresholds_Object = MibTableColumn
acPMRTPPacketsRxTimeBetweenThresholds = _AcPMRTPPacketsRxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 9),
    _AcPMRTPPacketsRxTimeBetweenThresholds_Type()
)
acPMRTPPacketsRxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxTimeBetweenThresholds.setStatus("current")


class _AcPMRTPPacketsRxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRTPPacketsRxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketsRxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRTPPacketsRxTimeAboveHighThreshold_Object = MibTableColumn
acPMRTPPacketsRxTimeAboveHighThreshold = _AcPMRTPPacketsRxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 10),
    _AcPMRTPPacketsRxTimeAboveHighThreshold_Type()
)
acPMRTPPacketsRxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxTimeAboveHighThreshold.setStatus("current")


class _AcPMRTPPacketsRxFullDayAverage_Type(Integer32):
    """Custom type acPMRTPPacketsRxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketsRxFullDayAverage_Type.__name__ = "Integer32"
_AcPMRTPPacketsRxFullDayAverage_Object = MibTableColumn
acPMRTPPacketsRxFullDayAverage = _AcPMRTPPacketsRxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 11),
    _AcPMRTPPacketsRxFullDayAverage_Type()
)
acPMRTPPacketsRxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxFullDayAverage.setStatus("current")


class _AcPMRTPPacketsRxTotal_Type(Integer32):
    """Custom type acPMRTPPacketsRxTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketsRxTotal_Type.__name__ = "Integer32"
_AcPMRTPPacketsRxTotal_Object = MibTableColumn
acPMRTPPacketsRxTotal = _AcPMRTPPacketsRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 6, 1, 12),
    _AcPMRTPPacketsRxTotal_Type()
)
acPMRTPPacketsRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketsRxTotal.setStatus("current")
_AcPMRTPPacketLossRxTable_Object = MibTable
acPMRTPPacketLossRxTable = _AcPMRTPPacketLossRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7)
)
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxTable.setStatus("current")
_AcPMRTPPacketLossRxEntry_Object = MibTableRow
acPMRTPPacketLossRxEntry = _AcPMRTPPacketLossRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1)
)
acPMRTPPacketLossRxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMRTPPacketLossRxTrunkNum"),
    (0, "AC-PM-Media-MIB", "acPMRTPPacketLossRxInterval"),
)
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxEntry.setStatus("current")


class _AcPMRTPPacketLossRxTrunkNum_Type(Unsigned32):
    """Custom type acPMRTPPacketLossRxTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMRTPPacketLossRxTrunkNum_Type.__name__ = "Unsigned32"
_AcPMRTPPacketLossRxTrunkNum_Object = MibTableColumn
acPMRTPPacketLossRxTrunkNum = _AcPMRTPPacketLossRxTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1, 1),
    _AcPMRTPPacketLossRxTrunkNum_Type()
)
acPMRTPPacketLossRxTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxTrunkNum.setStatus("current")


class _AcPMRTPPacketLossRxInterval_Type(Unsigned32):
    """Custom type acPMRTPPacketLossRxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRTPPacketLossRxInterval_Type.__name__ = "Unsigned32"
_AcPMRTPPacketLossRxInterval_Object = MibTableColumn
acPMRTPPacketLossRxInterval = _AcPMRTPPacketLossRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1, 2),
    _AcPMRTPPacketLossRxInterval_Type()
)
acPMRTPPacketLossRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxInterval.setStatus("current")
_AcPMRTPPacketLossRxVal_Type = Gauge32
_AcPMRTPPacketLossRxVal_Object = MibTableColumn
acPMRTPPacketLossRxVal = _AcPMRTPPacketLossRxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1, 3),
    _AcPMRTPPacketLossRxVal_Type()
)
acPMRTPPacketLossRxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxVal.setStatus("current")


class _AcPMRTPPacketLossRxAverage_Type(Integer32):
    """Custom type acPMRTPPacketLossRxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketLossRxAverage_Type.__name__ = "Integer32"
_AcPMRTPPacketLossRxAverage_Object = MibTableColumn
acPMRTPPacketLossRxAverage = _AcPMRTPPacketLossRxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1, 4),
    _AcPMRTPPacketLossRxAverage_Type()
)
acPMRTPPacketLossRxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxAverage.setStatus("current")


class _AcPMRTPPacketLossRxMax_Type(Integer32):
    """Custom type acPMRTPPacketLossRxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketLossRxMax_Type.__name__ = "Integer32"
_AcPMRTPPacketLossRxMax_Object = MibTableColumn
acPMRTPPacketLossRxMax = _AcPMRTPPacketLossRxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1, 5),
    _AcPMRTPPacketLossRxMax_Type()
)
acPMRTPPacketLossRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxMax.setStatus("current")


class _AcPMRTPPacketLossRxMin_Type(Integer32):
    """Custom type acPMRTPPacketLossRxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketLossRxMin_Type.__name__ = "Integer32"
_AcPMRTPPacketLossRxMin_Object = MibTableColumn
acPMRTPPacketLossRxMin = _AcPMRTPPacketLossRxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1, 6),
    _AcPMRTPPacketLossRxMin_Type()
)
acPMRTPPacketLossRxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxMin.setStatus("current")
_AcPMRTPPacketLossRxVolume_Type = Counter32
_AcPMRTPPacketLossRxVolume_Object = MibTableColumn
acPMRTPPacketLossRxVolume = _AcPMRTPPacketLossRxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1, 7),
    _AcPMRTPPacketLossRxVolume_Type()
)
acPMRTPPacketLossRxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxVolume.setStatus("current")


class _AcPMRTPPacketLossRxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRTPPacketLossRxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketLossRxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRTPPacketLossRxTimeBelowLowThreshold_Object = MibTableColumn
acPMRTPPacketLossRxTimeBelowLowThreshold = _AcPMRTPPacketLossRxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1, 8),
    _AcPMRTPPacketLossRxTimeBelowLowThreshold_Type()
)
acPMRTPPacketLossRxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxTimeBelowLowThreshold.setStatus("current")


class _AcPMRTPPacketLossRxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRTPPacketLossRxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketLossRxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRTPPacketLossRxTimeBetweenThresholds_Object = MibTableColumn
acPMRTPPacketLossRxTimeBetweenThresholds = _AcPMRTPPacketLossRxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1, 9),
    _AcPMRTPPacketLossRxTimeBetweenThresholds_Type()
)
acPMRTPPacketLossRxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxTimeBetweenThresholds.setStatus("current")


class _AcPMRTPPacketLossRxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRTPPacketLossRxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketLossRxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRTPPacketLossRxTimeAboveHighThreshold_Object = MibTableColumn
acPMRTPPacketLossRxTimeAboveHighThreshold = _AcPMRTPPacketLossRxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1, 10),
    _AcPMRTPPacketLossRxTimeAboveHighThreshold_Type()
)
acPMRTPPacketLossRxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxTimeAboveHighThreshold.setStatus("current")


class _AcPMRTPPacketLossRxFullDayAverage_Type(Integer32):
    """Custom type acPMRTPPacketLossRxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketLossRxFullDayAverage_Type.__name__ = "Integer32"
_AcPMRTPPacketLossRxFullDayAverage_Object = MibTableColumn
acPMRTPPacketLossRxFullDayAverage = _AcPMRTPPacketLossRxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 7, 1, 11),
    _AcPMRTPPacketLossRxFullDayAverage_Type()
)
acPMRTPPacketLossRxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossRxFullDayAverage.setStatus("current")
_AcPMRTPPacketLossTxTable_Object = MibTable
acPMRTPPacketLossTxTable = _AcPMRTPPacketLossTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8)
)
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxTable.setStatus("current")
_AcPMRTPPacketLossTxEntry_Object = MibTableRow
acPMRTPPacketLossTxEntry = _AcPMRTPPacketLossTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1)
)
acPMRTPPacketLossTxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMRTPPacketLossTxTrunkNum"),
    (0, "AC-PM-Media-MIB", "acPMRTPPacketLossTxInterval"),
)
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxEntry.setStatus("current")


class _AcPMRTPPacketLossTxTrunkNum_Type(Unsigned32):
    """Custom type acPMRTPPacketLossTxTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMRTPPacketLossTxTrunkNum_Type.__name__ = "Unsigned32"
_AcPMRTPPacketLossTxTrunkNum_Object = MibTableColumn
acPMRTPPacketLossTxTrunkNum = _AcPMRTPPacketLossTxTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1, 1),
    _AcPMRTPPacketLossTxTrunkNum_Type()
)
acPMRTPPacketLossTxTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxTrunkNum.setStatus("current")


class _AcPMRTPPacketLossTxInterval_Type(Unsigned32):
    """Custom type acPMRTPPacketLossTxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRTPPacketLossTxInterval_Type.__name__ = "Unsigned32"
_AcPMRTPPacketLossTxInterval_Object = MibTableColumn
acPMRTPPacketLossTxInterval = _AcPMRTPPacketLossTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1, 2),
    _AcPMRTPPacketLossTxInterval_Type()
)
acPMRTPPacketLossTxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxInterval.setStatus("current")
_AcPMRTPPacketLossTxVal_Type = Gauge32
_AcPMRTPPacketLossTxVal_Object = MibTableColumn
acPMRTPPacketLossTxVal = _AcPMRTPPacketLossTxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1, 3),
    _AcPMRTPPacketLossTxVal_Type()
)
acPMRTPPacketLossTxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxVal.setStatus("current")


class _AcPMRTPPacketLossTxAverage_Type(Integer32):
    """Custom type acPMRTPPacketLossTxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketLossTxAverage_Type.__name__ = "Integer32"
_AcPMRTPPacketLossTxAverage_Object = MibTableColumn
acPMRTPPacketLossTxAverage = _AcPMRTPPacketLossTxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1, 4),
    _AcPMRTPPacketLossTxAverage_Type()
)
acPMRTPPacketLossTxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxAverage.setStatus("current")


class _AcPMRTPPacketLossTxMax_Type(Integer32):
    """Custom type acPMRTPPacketLossTxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketLossTxMax_Type.__name__ = "Integer32"
_AcPMRTPPacketLossTxMax_Object = MibTableColumn
acPMRTPPacketLossTxMax = _AcPMRTPPacketLossTxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1, 5),
    _AcPMRTPPacketLossTxMax_Type()
)
acPMRTPPacketLossTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxMax.setStatus("current")


class _AcPMRTPPacketLossTxMin_Type(Integer32):
    """Custom type acPMRTPPacketLossTxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketLossTxMin_Type.__name__ = "Integer32"
_AcPMRTPPacketLossTxMin_Object = MibTableColumn
acPMRTPPacketLossTxMin = _AcPMRTPPacketLossTxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1, 6),
    _AcPMRTPPacketLossTxMin_Type()
)
acPMRTPPacketLossTxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxMin.setStatus("current")
_AcPMRTPPacketLossTxVolume_Type = Counter32
_AcPMRTPPacketLossTxVolume_Object = MibTableColumn
acPMRTPPacketLossTxVolume = _AcPMRTPPacketLossTxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1, 7),
    _AcPMRTPPacketLossTxVolume_Type()
)
acPMRTPPacketLossTxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxVolume.setStatus("current")


class _AcPMRTPPacketLossTxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRTPPacketLossTxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketLossTxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRTPPacketLossTxTimeBelowLowThreshold_Object = MibTableColumn
acPMRTPPacketLossTxTimeBelowLowThreshold = _AcPMRTPPacketLossTxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1, 8),
    _AcPMRTPPacketLossTxTimeBelowLowThreshold_Type()
)
acPMRTPPacketLossTxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxTimeBelowLowThreshold.setStatus("current")


class _AcPMRTPPacketLossTxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRTPPacketLossTxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketLossTxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRTPPacketLossTxTimeBetweenThresholds_Object = MibTableColumn
acPMRTPPacketLossTxTimeBetweenThresholds = _AcPMRTPPacketLossTxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1, 9),
    _AcPMRTPPacketLossTxTimeBetweenThresholds_Type()
)
acPMRTPPacketLossTxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxTimeBetweenThresholds.setStatus("current")


class _AcPMRTPPacketLossTxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRTPPacketLossTxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPPacketLossTxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRTPPacketLossTxTimeAboveHighThreshold_Object = MibTableColumn
acPMRTPPacketLossTxTimeAboveHighThreshold = _AcPMRTPPacketLossTxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1, 10),
    _AcPMRTPPacketLossTxTimeAboveHighThreshold_Type()
)
acPMRTPPacketLossTxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxTimeAboveHighThreshold.setStatus("current")


class _AcPMRTPPacketLossTxFullDayAverage_Type(Integer32):
    """Custom type acPMRTPPacketLossTxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPPacketLossTxFullDayAverage_Type.__name__ = "Integer32"
_AcPMRTPPacketLossTxFullDayAverage_Object = MibTableColumn
acPMRTPPacketLossTxFullDayAverage = _AcPMRTPPacketLossTxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 8, 1, 11),
    _AcPMRTPPacketLossTxFullDayAverage_Type()
)
acPMRTPPacketLossTxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPPacketLossTxFullDayAverage.setStatus("current")
_AcPMModuleRTPPacketLossRxTable_Object = MibTable
acPMModuleRTPPacketLossRxTable = _AcPMModuleRTPPacketLossRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9)
)
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxTable.setStatus("current")
_AcPMModuleRTPPacketLossRxEntry_Object = MibTableRow
acPMModuleRTPPacketLossRxEntry = _AcPMModuleRTPPacketLossRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9, 1)
)
acPMModuleRTPPacketLossRxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMModuleRTPPacketLossRxInterval"),
)
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxEntry.setStatus("current")


class _AcPMModuleRTPPacketLossRxInterval_Type(Unsigned32):
    """Custom type acPMModuleRTPPacketLossRxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMModuleRTPPacketLossRxInterval_Type.__name__ = "Unsigned32"
_AcPMModuleRTPPacketLossRxInterval_Object = MibTableColumn
acPMModuleRTPPacketLossRxInterval = _AcPMModuleRTPPacketLossRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9, 1, 1),
    _AcPMModuleRTPPacketLossRxInterval_Type()
)
acPMModuleRTPPacketLossRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxInterval.setStatus("current")


class _AcPMModuleRTPPacketLossRxAverage_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossRxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketLossRxAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossRxAverage_Object = MibTableColumn
acPMModuleRTPPacketLossRxAverage = _AcPMModuleRTPPacketLossRxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9, 1, 2),
    _AcPMModuleRTPPacketLossRxAverage_Type()
)
acPMModuleRTPPacketLossRxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxAverage.setStatus("current")


class _AcPMModuleRTPPacketLossRxMax_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossRxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketLossRxMax_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossRxMax_Object = MibTableColumn
acPMModuleRTPPacketLossRxMax = _AcPMModuleRTPPacketLossRxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9, 1, 3),
    _AcPMModuleRTPPacketLossRxMax_Type()
)
acPMModuleRTPPacketLossRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxMax.setStatus("current")


class _AcPMModuleRTPPacketLossRxMin_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossRxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketLossRxMin_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossRxMin_Object = MibTableColumn
acPMModuleRTPPacketLossRxMin = _AcPMModuleRTPPacketLossRxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9, 1, 4),
    _AcPMModuleRTPPacketLossRxMin_Type()
)
acPMModuleRTPPacketLossRxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxMin.setStatus("current")
_AcPMModuleRTPPacketLossRxVolume_Type = Counter32
_AcPMModuleRTPPacketLossRxVolume_Object = MibTableColumn
acPMModuleRTPPacketLossRxVolume = _AcPMModuleRTPPacketLossRxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9, 1, 5),
    _AcPMModuleRTPPacketLossRxVolume_Type()
)
acPMModuleRTPPacketLossRxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxVolume.setStatus("current")


class _AcPMModuleRTPPacketLossRxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossRxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketLossRxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossRxTimeBelowLowThreshold_Object = MibTableColumn
acPMModuleRTPPacketLossRxTimeBelowLowThreshold = _AcPMModuleRTPPacketLossRxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9, 1, 6),
    _AcPMModuleRTPPacketLossRxTimeBelowLowThreshold_Type()
)
acPMModuleRTPPacketLossRxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxTimeBelowLowThreshold.setStatus("current")


class _AcPMModuleRTPPacketLossRxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossRxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketLossRxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossRxTimeBetweenThresholds_Object = MibTableColumn
acPMModuleRTPPacketLossRxTimeBetweenThresholds = _AcPMModuleRTPPacketLossRxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9, 1, 7),
    _AcPMModuleRTPPacketLossRxTimeBetweenThresholds_Type()
)
acPMModuleRTPPacketLossRxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxTimeBetweenThresholds.setStatus("current")


class _AcPMModuleRTPPacketLossRxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossRxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketLossRxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossRxTimeAboveHighThreshold_Object = MibTableColumn
acPMModuleRTPPacketLossRxTimeAboveHighThreshold = _AcPMModuleRTPPacketLossRxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9, 1, 8),
    _AcPMModuleRTPPacketLossRxTimeAboveHighThreshold_Type()
)
acPMModuleRTPPacketLossRxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxTimeAboveHighThreshold.setStatus("current")


class _AcPMModuleRTPPacketLossRxFullDayAverage_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossRxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketLossRxFullDayAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossRxFullDayAverage_Object = MibTableColumn
acPMModuleRTPPacketLossRxFullDayAverage = _AcPMModuleRTPPacketLossRxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9, 1, 9),
    _AcPMModuleRTPPacketLossRxFullDayAverage_Type()
)
acPMModuleRTPPacketLossRxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxFullDayAverage.setStatus("current")


class _AcPMModuleRTPPacketLossRxTotal_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossRxTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketLossRxTotal_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossRxTotal_Object = MibTableColumn
acPMModuleRTPPacketLossRxTotal = _AcPMModuleRTPPacketLossRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 9, 1, 10),
    _AcPMModuleRTPPacketLossRxTotal_Type()
)
acPMModuleRTPPacketLossRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossRxTotal.setStatus("current")
_AcPMModuleRTPPacketLossTxTable_Object = MibTable
acPMModuleRTPPacketLossTxTable = _AcPMModuleRTPPacketLossTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10)
)
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxTable.setStatus("current")
_AcPMModuleRTPPacketLossTxEntry_Object = MibTableRow
acPMModuleRTPPacketLossTxEntry = _AcPMModuleRTPPacketLossTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10, 1)
)
acPMModuleRTPPacketLossTxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMModuleRTPPacketLossTxInterval"),
)
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxEntry.setStatus("current")


class _AcPMModuleRTPPacketLossTxInterval_Type(Unsigned32):
    """Custom type acPMModuleRTPPacketLossTxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMModuleRTPPacketLossTxInterval_Type.__name__ = "Unsigned32"
_AcPMModuleRTPPacketLossTxInterval_Object = MibTableColumn
acPMModuleRTPPacketLossTxInterval = _AcPMModuleRTPPacketLossTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10, 1, 1),
    _AcPMModuleRTPPacketLossTxInterval_Type()
)
acPMModuleRTPPacketLossTxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxInterval.setStatus("current")


class _AcPMModuleRTPPacketLossTxAverage_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossTxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketLossTxAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossTxAverage_Object = MibTableColumn
acPMModuleRTPPacketLossTxAverage = _AcPMModuleRTPPacketLossTxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10, 1, 2),
    _AcPMModuleRTPPacketLossTxAverage_Type()
)
acPMModuleRTPPacketLossTxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxAverage.setStatus("current")


class _AcPMModuleRTPPacketLossTxMax_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossTxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketLossTxMax_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossTxMax_Object = MibTableColumn
acPMModuleRTPPacketLossTxMax = _AcPMModuleRTPPacketLossTxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10, 1, 3),
    _AcPMModuleRTPPacketLossTxMax_Type()
)
acPMModuleRTPPacketLossTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxMax.setStatus("current")


class _AcPMModuleRTPPacketLossTxMin_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossTxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketLossTxMin_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossTxMin_Object = MibTableColumn
acPMModuleRTPPacketLossTxMin = _AcPMModuleRTPPacketLossTxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10, 1, 4),
    _AcPMModuleRTPPacketLossTxMin_Type()
)
acPMModuleRTPPacketLossTxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxMin.setStatus("current")
_AcPMModuleRTPPacketLossTxVolume_Type = Counter32
_AcPMModuleRTPPacketLossTxVolume_Object = MibTableColumn
acPMModuleRTPPacketLossTxVolume = _AcPMModuleRTPPacketLossTxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10, 1, 5),
    _AcPMModuleRTPPacketLossTxVolume_Type()
)
acPMModuleRTPPacketLossTxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxVolume.setStatus("current")


class _AcPMModuleRTPPacketLossTxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossTxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketLossTxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossTxTimeBelowLowThreshold_Object = MibTableColumn
acPMModuleRTPPacketLossTxTimeBelowLowThreshold = _AcPMModuleRTPPacketLossTxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10, 1, 6),
    _AcPMModuleRTPPacketLossTxTimeBelowLowThreshold_Type()
)
acPMModuleRTPPacketLossTxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxTimeBelowLowThreshold.setStatus("current")


class _AcPMModuleRTPPacketLossTxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossTxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketLossTxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossTxTimeBetweenThresholds_Object = MibTableColumn
acPMModuleRTPPacketLossTxTimeBetweenThresholds = _AcPMModuleRTPPacketLossTxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10, 1, 7),
    _AcPMModuleRTPPacketLossTxTimeBetweenThresholds_Type()
)
acPMModuleRTPPacketLossTxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxTimeBetweenThresholds.setStatus("current")


class _AcPMModuleRTPPacketLossTxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossTxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketLossTxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossTxTimeAboveHighThreshold_Object = MibTableColumn
acPMModuleRTPPacketLossTxTimeAboveHighThreshold = _AcPMModuleRTPPacketLossTxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10, 1, 8),
    _AcPMModuleRTPPacketLossTxTimeAboveHighThreshold_Type()
)
acPMModuleRTPPacketLossTxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxTimeAboveHighThreshold.setStatus("current")


class _AcPMModuleRTPPacketLossTxFullDayAverage_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossTxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketLossTxFullDayAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossTxFullDayAverage_Object = MibTableColumn
acPMModuleRTPPacketLossTxFullDayAverage = _AcPMModuleRTPPacketLossTxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10, 1, 9),
    _AcPMModuleRTPPacketLossTxFullDayAverage_Type()
)
acPMModuleRTPPacketLossTxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxFullDayAverage.setStatus("current")


class _AcPMModuleRTPPacketLossTxTotal_Type(Integer32):
    """Custom type acPMModuleRTPPacketLossTxTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketLossTxTotal_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketLossTxTotal_Object = MibTableColumn
acPMModuleRTPPacketLossTxTotal = _AcPMModuleRTPPacketLossTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 10, 1, 10),
    _AcPMModuleRTPPacketLossTxTotal_Type()
)
acPMModuleRTPPacketLossTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketLossTxTotal.setStatus("current")
_AcPMMediaNetworkingAggregated_ObjectIdentity = ObjectIdentity
acPMMediaNetworkingAggregated = _AcPMMediaNetworkingAggregated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21)
)
_AcPMModulePacketDelayTable_Object = MibTable
acPMModulePacketDelayTable = _AcPMModulePacketDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1)
)
if mibBuilder.loadTexts:
    acPMModulePacketDelayTable.setStatus("current")
_AcPMModulePacketDelayEntry_Object = MibTableRow
acPMModulePacketDelayEntry = _AcPMModulePacketDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1, 1)
)
acPMModulePacketDelayEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMModulePacketDelayInterval"),
)
if mibBuilder.loadTexts:
    acPMModulePacketDelayEntry.setStatus("current")


class _AcPMModulePacketDelayInterval_Type(Unsigned32):
    """Custom type acPMModulePacketDelayInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMModulePacketDelayInterval_Type.__name__ = "Unsigned32"
_AcPMModulePacketDelayInterval_Object = MibTableColumn
acPMModulePacketDelayInterval = _AcPMModulePacketDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1, 1, 1),
    _AcPMModulePacketDelayInterval_Type()
)
acPMModulePacketDelayInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMModulePacketDelayInterval.setStatus("current")
_AcPMModulePacketDelayVal_Type = Gauge32
_AcPMModulePacketDelayVal_Object = MibTableColumn
acPMModulePacketDelayVal = _AcPMModulePacketDelayVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1, 1, 2),
    _AcPMModulePacketDelayVal_Type()
)
acPMModulePacketDelayVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketDelayVal.setStatus("current")


class _AcPMModulePacketDelayAverage_Type(Integer32):
    """Custom type acPMModulePacketDelayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModulePacketDelayAverage_Type.__name__ = "Integer32"
_AcPMModulePacketDelayAverage_Object = MibTableColumn
acPMModulePacketDelayAverage = _AcPMModulePacketDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1, 1, 3),
    _AcPMModulePacketDelayAverage_Type()
)
acPMModulePacketDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketDelayAverage.setStatus("current")


class _AcPMModulePacketDelayMax_Type(Integer32):
    """Custom type acPMModulePacketDelayMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModulePacketDelayMax_Type.__name__ = "Integer32"
_AcPMModulePacketDelayMax_Object = MibTableColumn
acPMModulePacketDelayMax = _AcPMModulePacketDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1, 1, 4),
    _AcPMModulePacketDelayMax_Type()
)
acPMModulePacketDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketDelayMax.setStatus("current")


class _AcPMModulePacketDelayMin_Type(Integer32):
    """Custom type acPMModulePacketDelayMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModulePacketDelayMin_Type.__name__ = "Integer32"
_AcPMModulePacketDelayMin_Object = MibTableColumn
acPMModulePacketDelayMin = _AcPMModulePacketDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1, 1, 5),
    _AcPMModulePacketDelayMin_Type()
)
acPMModulePacketDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketDelayMin.setStatus("current")


class _AcPMModulePacketDelayTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMModulePacketDelayTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModulePacketDelayTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMModulePacketDelayTimeBelowLowThreshold_Object = MibTableColumn
acPMModulePacketDelayTimeBelowLowThreshold = _AcPMModulePacketDelayTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1, 1, 6),
    _AcPMModulePacketDelayTimeBelowLowThreshold_Type()
)
acPMModulePacketDelayTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketDelayTimeBelowLowThreshold.setStatus("current")


class _AcPMModulePacketDelayTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMModulePacketDelayTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModulePacketDelayTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMModulePacketDelayTimeBetweenThresholds_Object = MibTableColumn
acPMModulePacketDelayTimeBetweenThresholds = _AcPMModulePacketDelayTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1, 1, 7),
    _AcPMModulePacketDelayTimeBetweenThresholds_Type()
)
acPMModulePacketDelayTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketDelayTimeBetweenThresholds.setStatus("current")


class _AcPMModulePacketDelayTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMModulePacketDelayTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModulePacketDelayTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMModulePacketDelayTimeAboveHighThreshold_Object = MibTableColumn
acPMModulePacketDelayTimeAboveHighThreshold = _AcPMModulePacketDelayTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1, 1, 8),
    _AcPMModulePacketDelayTimeAboveHighThreshold_Type()
)
acPMModulePacketDelayTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketDelayTimeAboveHighThreshold.setStatus("current")


class _AcPMModulePacketDelayFullDayAverage_Type(Integer32):
    """Custom type acPMModulePacketDelayFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModulePacketDelayFullDayAverage_Type.__name__ = "Integer32"
_AcPMModulePacketDelayFullDayAverage_Object = MibTableColumn
acPMModulePacketDelayFullDayAverage = _AcPMModulePacketDelayFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1, 1, 9),
    _AcPMModulePacketDelayFullDayAverage_Type()
)
acPMModulePacketDelayFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketDelayFullDayAverage.setStatus("current")
_AcPMModulePacketDelayVolume_Type = Counter32
_AcPMModulePacketDelayVolume_Object = MibTableColumn
acPMModulePacketDelayVolume = _AcPMModulePacketDelayVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 1, 1, 10),
    _AcPMModulePacketDelayVolume_Type()
)
acPMModulePacketDelayVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketDelayVolume.setStatus("current")
_AcPMModulePacketJitterTable_Object = MibTable
acPMModulePacketJitterTable = _AcPMModulePacketJitterTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2)
)
if mibBuilder.loadTexts:
    acPMModulePacketJitterTable.setStatus("current")
_AcPMModulePacketJitterEntry_Object = MibTableRow
acPMModulePacketJitterEntry = _AcPMModulePacketJitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2, 1)
)
acPMModulePacketJitterEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMModulePacketJitterInterval"),
)
if mibBuilder.loadTexts:
    acPMModulePacketJitterEntry.setStatus("current")


class _AcPMModulePacketJitterInterval_Type(Unsigned32):
    """Custom type acPMModulePacketJitterInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMModulePacketJitterInterval_Type.__name__ = "Unsigned32"
_AcPMModulePacketJitterInterval_Object = MibTableColumn
acPMModulePacketJitterInterval = _AcPMModulePacketJitterInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2, 1, 1),
    _AcPMModulePacketJitterInterval_Type()
)
acPMModulePacketJitterInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMModulePacketJitterInterval.setStatus("current")
_AcPMModulePacketJitterVal_Type = Gauge32
_AcPMModulePacketJitterVal_Object = MibTableColumn
acPMModulePacketJitterVal = _AcPMModulePacketJitterVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2, 1, 2),
    _AcPMModulePacketJitterVal_Type()
)
acPMModulePacketJitterVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketJitterVal.setStatus("current")


class _AcPMModulePacketJitterAverage_Type(Integer32):
    """Custom type acPMModulePacketJitterAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModulePacketJitterAverage_Type.__name__ = "Integer32"
_AcPMModulePacketJitterAverage_Object = MibTableColumn
acPMModulePacketJitterAverage = _AcPMModulePacketJitterAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2, 1, 3),
    _AcPMModulePacketJitterAverage_Type()
)
acPMModulePacketJitterAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketJitterAverage.setStatus("current")


class _AcPMModulePacketJitterMax_Type(Integer32):
    """Custom type acPMModulePacketJitterMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModulePacketJitterMax_Type.__name__ = "Integer32"
_AcPMModulePacketJitterMax_Object = MibTableColumn
acPMModulePacketJitterMax = _AcPMModulePacketJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2, 1, 4),
    _AcPMModulePacketJitterMax_Type()
)
acPMModulePacketJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketJitterMax.setStatus("current")


class _AcPMModulePacketJitterMin_Type(Integer32):
    """Custom type acPMModulePacketJitterMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModulePacketJitterMin_Type.__name__ = "Integer32"
_AcPMModulePacketJitterMin_Object = MibTableColumn
acPMModulePacketJitterMin = _AcPMModulePacketJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2, 1, 5),
    _AcPMModulePacketJitterMin_Type()
)
acPMModulePacketJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketJitterMin.setStatus("current")


class _AcPMModulePacketJitterTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMModulePacketJitterTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModulePacketJitterTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMModulePacketJitterTimeBelowLowThreshold_Object = MibTableColumn
acPMModulePacketJitterTimeBelowLowThreshold = _AcPMModulePacketJitterTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2, 1, 6),
    _AcPMModulePacketJitterTimeBelowLowThreshold_Type()
)
acPMModulePacketJitterTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketJitterTimeBelowLowThreshold.setStatus("current")


class _AcPMModulePacketJitterTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMModulePacketJitterTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModulePacketJitterTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMModulePacketJitterTimeBetweenThresholds_Object = MibTableColumn
acPMModulePacketJitterTimeBetweenThresholds = _AcPMModulePacketJitterTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2, 1, 7),
    _AcPMModulePacketJitterTimeBetweenThresholds_Type()
)
acPMModulePacketJitterTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketJitterTimeBetweenThresholds.setStatus("current")


class _AcPMModulePacketJitterTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMModulePacketJitterTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModulePacketJitterTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMModulePacketJitterTimeAboveHighThreshold_Object = MibTableColumn
acPMModulePacketJitterTimeAboveHighThreshold = _AcPMModulePacketJitterTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2, 1, 8),
    _AcPMModulePacketJitterTimeAboveHighThreshold_Type()
)
acPMModulePacketJitterTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketJitterTimeAboveHighThreshold.setStatus("current")


class _AcPMModulePacketJitterFullDayAverage_Type(Integer32):
    """Custom type acPMModulePacketJitterFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModulePacketJitterFullDayAverage_Type.__name__ = "Integer32"
_AcPMModulePacketJitterFullDayAverage_Object = MibTableColumn
acPMModulePacketJitterFullDayAverage = _AcPMModulePacketJitterFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2, 1, 9),
    _AcPMModulePacketJitterFullDayAverage_Type()
)
acPMModulePacketJitterFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketJitterFullDayAverage.setStatus("current")
_AcPMModulePacketJitterVolume_Type = Counter32
_AcPMModulePacketJitterVolume_Object = MibTableColumn
acPMModulePacketJitterVolume = _AcPMModulePacketJitterVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 2, 1, 10),
    _AcPMModulePacketJitterVolume_Type()
)
acPMModulePacketJitterVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModulePacketJitterVolume.setStatus("current")
_AcPMModuleRTPBytesTxTable_Object = MibTable
acPMModuleRTPBytesTxTable = _AcPMModuleRTPBytesTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 3)
)
if mibBuilder.loadTexts:
    acPMModuleRTPBytesTxTable.setStatus("current")
_AcPMModuleRTPBytesTxEntry_Object = MibTableRow
acPMModuleRTPBytesTxEntry = _AcPMModuleRTPBytesTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 3, 1)
)
acPMModuleRTPBytesTxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMModuleRTPBytesTxInterval"),
)
if mibBuilder.loadTexts:
    acPMModuleRTPBytesTxEntry.setStatus("current")


class _AcPMModuleRTPBytesTxInterval_Type(Unsigned32):
    """Custom type acPMModuleRTPBytesTxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMModuleRTPBytesTxInterval_Type.__name__ = "Unsigned32"
_AcPMModuleRTPBytesTxInterval_Object = MibTableColumn
acPMModuleRTPBytesTxInterval = _AcPMModuleRTPBytesTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 3, 1, 1),
    _AcPMModuleRTPBytesTxInterval_Type()
)
acPMModuleRTPBytesTxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesTxInterval.setStatus("current")


class _AcPMModuleRTPBytesTxAverage_Type(Integer32):
    """Custom type acPMModuleRTPBytesTxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPBytesTxAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesTxAverage_Object = MibTableColumn
acPMModuleRTPBytesTxAverage = _AcPMModuleRTPBytesTxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 3, 1, 2),
    _AcPMModuleRTPBytesTxAverage_Type()
)
acPMModuleRTPBytesTxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesTxAverage.setStatus("current")


class _AcPMModuleRTPBytesTxMax_Type(Integer32):
    """Custom type acPMModuleRTPBytesTxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPBytesTxMax_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesTxMax_Object = MibTableColumn
acPMModuleRTPBytesTxMax = _AcPMModuleRTPBytesTxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 3, 1, 3),
    _AcPMModuleRTPBytesTxMax_Type()
)
acPMModuleRTPBytesTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesTxMax.setStatus("current")


class _AcPMModuleRTPBytesTxMin_Type(Integer32):
    """Custom type acPMModuleRTPBytesTxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPBytesTxMin_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesTxMin_Object = MibTableColumn
acPMModuleRTPBytesTxMin = _AcPMModuleRTPBytesTxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 3, 1, 4),
    _AcPMModuleRTPBytesTxMin_Type()
)
acPMModuleRTPBytesTxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesTxMin.setStatus("current")


class _AcPMModuleRTPBytesTxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMModuleRTPBytesTxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPBytesTxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesTxTimeBelowLowThreshold_Object = MibTableColumn
acPMModuleRTPBytesTxTimeBelowLowThreshold = _AcPMModuleRTPBytesTxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 3, 1, 5),
    _AcPMModuleRTPBytesTxTimeBelowLowThreshold_Type()
)
acPMModuleRTPBytesTxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesTxTimeBelowLowThreshold.setStatus("current")


class _AcPMModuleRTPBytesTxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMModuleRTPBytesTxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPBytesTxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesTxTimeBetweenThresholds_Object = MibTableColumn
acPMModuleRTPBytesTxTimeBetweenThresholds = _AcPMModuleRTPBytesTxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 3, 1, 6),
    _AcPMModuleRTPBytesTxTimeBetweenThresholds_Type()
)
acPMModuleRTPBytesTxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesTxTimeBetweenThresholds.setStatus("current")


class _AcPMModuleRTPBytesTxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMModuleRTPBytesTxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPBytesTxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesTxTimeAboveHighThreshold_Object = MibTableColumn
acPMModuleRTPBytesTxTimeAboveHighThreshold = _AcPMModuleRTPBytesTxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 3, 1, 7),
    _AcPMModuleRTPBytesTxTimeAboveHighThreshold_Type()
)
acPMModuleRTPBytesTxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesTxTimeAboveHighThreshold.setStatus("current")


class _AcPMModuleRTPBytesTxFullDayAverage_Type(Integer32):
    """Custom type acPMModuleRTPBytesTxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPBytesTxFullDayAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesTxFullDayAverage_Object = MibTableColumn
acPMModuleRTPBytesTxFullDayAverage = _AcPMModuleRTPBytesTxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 3, 1, 8),
    _AcPMModuleRTPBytesTxFullDayAverage_Type()
)
acPMModuleRTPBytesTxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesTxFullDayAverage.setStatus("current")
_AcPMModuleRTPBytesTxVolume_Type = Counter32
_AcPMModuleRTPBytesTxVolume_Object = MibTableColumn
acPMModuleRTPBytesTxVolume = _AcPMModuleRTPBytesTxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 3, 1, 9),
    _AcPMModuleRTPBytesTxVolume_Type()
)
acPMModuleRTPBytesTxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesTxVolume.setStatus("current")
_AcPMModuleRTPBytesRxTable_Object = MibTable
acPMModuleRTPBytesRxTable = _AcPMModuleRTPBytesRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 4)
)
if mibBuilder.loadTexts:
    acPMModuleRTPBytesRxTable.setStatus("current")
_AcPMModuleRTPBytesRxEntry_Object = MibTableRow
acPMModuleRTPBytesRxEntry = _AcPMModuleRTPBytesRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 4, 1)
)
acPMModuleRTPBytesRxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMModuleRTPBytesRxInterval"),
)
if mibBuilder.loadTexts:
    acPMModuleRTPBytesRxEntry.setStatus("current")


class _AcPMModuleRTPBytesRxInterval_Type(Unsigned32):
    """Custom type acPMModuleRTPBytesRxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMModuleRTPBytesRxInterval_Type.__name__ = "Unsigned32"
_AcPMModuleRTPBytesRxInterval_Object = MibTableColumn
acPMModuleRTPBytesRxInterval = _AcPMModuleRTPBytesRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 4, 1, 1),
    _AcPMModuleRTPBytesRxInterval_Type()
)
acPMModuleRTPBytesRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesRxInterval.setStatus("current")


class _AcPMModuleRTPBytesRxAverage_Type(Integer32):
    """Custom type acPMModuleRTPBytesRxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPBytesRxAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesRxAverage_Object = MibTableColumn
acPMModuleRTPBytesRxAverage = _AcPMModuleRTPBytesRxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 4, 1, 2),
    _AcPMModuleRTPBytesRxAverage_Type()
)
acPMModuleRTPBytesRxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesRxAverage.setStatus("current")


class _AcPMModuleRTPBytesRxMax_Type(Integer32):
    """Custom type acPMModuleRTPBytesRxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPBytesRxMax_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesRxMax_Object = MibTableColumn
acPMModuleRTPBytesRxMax = _AcPMModuleRTPBytesRxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 4, 1, 3),
    _AcPMModuleRTPBytesRxMax_Type()
)
acPMModuleRTPBytesRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesRxMax.setStatus("current")


class _AcPMModuleRTPBytesRxMin_Type(Integer32):
    """Custom type acPMModuleRTPBytesRxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPBytesRxMin_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesRxMin_Object = MibTableColumn
acPMModuleRTPBytesRxMin = _AcPMModuleRTPBytesRxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 4, 1, 4),
    _AcPMModuleRTPBytesRxMin_Type()
)
acPMModuleRTPBytesRxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesRxMin.setStatus("current")


class _AcPMModuleRTPBytesRxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMModuleRTPBytesRxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPBytesRxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesRxTimeBelowLowThreshold_Object = MibTableColumn
acPMModuleRTPBytesRxTimeBelowLowThreshold = _AcPMModuleRTPBytesRxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 4, 1, 5),
    _AcPMModuleRTPBytesRxTimeBelowLowThreshold_Type()
)
acPMModuleRTPBytesRxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesRxTimeBelowLowThreshold.setStatus("current")


class _AcPMModuleRTPBytesRxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMModuleRTPBytesRxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPBytesRxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesRxTimeBetweenThresholds_Object = MibTableColumn
acPMModuleRTPBytesRxTimeBetweenThresholds = _AcPMModuleRTPBytesRxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 4, 1, 6),
    _AcPMModuleRTPBytesRxTimeBetweenThresholds_Type()
)
acPMModuleRTPBytesRxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesRxTimeBetweenThresholds.setStatus("current")


class _AcPMModuleRTPBytesRxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMModuleRTPBytesRxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPBytesRxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesRxTimeAboveHighThreshold_Object = MibTableColumn
acPMModuleRTPBytesRxTimeAboveHighThreshold = _AcPMModuleRTPBytesRxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 4, 1, 7),
    _AcPMModuleRTPBytesRxTimeAboveHighThreshold_Type()
)
acPMModuleRTPBytesRxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesRxTimeAboveHighThreshold.setStatus("current")


class _AcPMModuleRTPBytesRxFullDayAverage_Type(Integer32):
    """Custom type acPMModuleRTPBytesRxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPBytesRxFullDayAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPBytesRxFullDayAverage_Object = MibTableColumn
acPMModuleRTPBytesRxFullDayAverage = _AcPMModuleRTPBytesRxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 4, 1, 8),
    _AcPMModuleRTPBytesRxFullDayAverage_Type()
)
acPMModuleRTPBytesRxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesRxFullDayAverage.setStatus("current")
_AcPMModuleRTPBytesRxVolume_Type = Counter32
_AcPMModuleRTPBytesRxVolume_Object = MibTableColumn
acPMModuleRTPBytesRxVolume = _AcPMModuleRTPBytesRxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 4, 1, 9),
    _AcPMModuleRTPBytesRxVolume_Type()
)
acPMModuleRTPBytesRxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPBytesRxVolume.setStatus("current")
_AcPMModuleRTPPacketsTxTable_Object = MibTable
acPMModuleRTPPacketsTxTable = _AcPMModuleRTPPacketsTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5)
)
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxTable.setStatus("current")
_AcPMModuleRTPPacketsTxEntry_Object = MibTableRow
acPMModuleRTPPacketsTxEntry = _AcPMModuleRTPPacketsTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5, 1)
)
acPMModuleRTPPacketsTxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMModuleRTPPacketsTxInterval"),
)
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxEntry.setStatus("current")


class _AcPMModuleRTPPacketsTxInterval_Type(Unsigned32):
    """Custom type acPMModuleRTPPacketsTxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMModuleRTPPacketsTxInterval_Type.__name__ = "Unsigned32"
_AcPMModuleRTPPacketsTxInterval_Object = MibTableColumn
acPMModuleRTPPacketsTxInterval = _AcPMModuleRTPPacketsTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5, 1, 1),
    _AcPMModuleRTPPacketsTxInterval_Type()
)
acPMModuleRTPPacketsTxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxInterval.setStatus("current")


class _AcPMModuleRTPPacketsTxAverage_Type(Integer32):
    """Custom type acPMModuleRTPPacketsTxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketsTxAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsTxAverage_Object = MibTableColumn
acPMModuleRTPPacketsTxAverage = _AcPMModuleRTPPacketsTxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5, 1, 2),
    _AcPMModuleRTPPacketsTxAverage_Type()
)
acPMModuleRTPPacketsTxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxAverage.setStatus("current")


class _AcPMModuleRTPPacketsTxMax_Type(Integer32):
    """Custom type acPMModuleRTPPacketsTxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketsTxMax_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsTxMax_Object = MibTableColumn
acPMModuleRTPPacketsTxMax = _AcPMModuleRTPPacketsTxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5, 1, 3),
    _AcPMModuleRTPPacketsTxMax_Type()
)
acPMModuleRTPPacketsTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxMax.setStatus("current")


class _AcPMModuleRTPPacketsTxMin_Type(Integer32):
    """Custom type acPMModuleRTPPacketsTxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketsTxMin_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsTxMin_Object = MibTableColumn
acPMModuleRTPPacketsTxMin = _AcPMModuleRTPPacketsTxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5, 1, 4),
    _AcPMModuleRTPPacketsTxMin_Type()
)
acPMModuleRTPPacketsTxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxMin.setStatus("current")


class _AcPMModuleRTPPacketsTxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMModuleRTPPacketsTxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketsTxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsTxTimeBelowLowThreshold_Object = MibTableColumn
acPMModuleRTPPacketsTxTimeBelowLowThreshold = _AcPMModuleRTPPacketsTxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5, 1, 5),
    _AcPMModuleRTPPacketsTxTimeBelowLowThreshold_Type()
)
acPMModuleRTPPacketsTxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxTimeBelowLowThreshold.setStatus("current")


class _AcPMModuleRTPPacketsTxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMModuleRTPPacketsTxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketsTxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsTxTimeBetweenThresholds_Object = MibTableColumn
acPMModuleRTPPacketsTxTimeBetweenThresholds = _AcPMModuleRTPPacketsTxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5, 1, 6),
    _AcPMModuleRTPPacketsTxTimeBetweenThresholds_Type()
)
acPMModuleRTPPacketsTxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxTimeBetweenThresholds.setStatus("current")


class _AcPMModuleRTPPacketsTxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMModuleRTPPacketsTxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketsTxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsTxTimeAboveHighThreshold_Object = MibTableColumn
acPMModuleRTPPacketsTxTimeAboveHighThreshold = _AcPMModuleRTPPacketsTxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5, 1, 7),
    _AcPMModuleRTPPacketsTxTimeAboveHighThreshold_Type()
)
acPMModuleRTPPacketsTxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxTimeAboveHighThreshold.setStatus("current")


class _AcPMModuleRTPPacketsTxFullDayAverage_Type(Integer32):
    """Custom type acPMModuleRTPPacketsTxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketsTxFullDayAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsTxFullDayAverage_Object = MibTableColumn
acPMModuleRTPPacketsTxFullDayAverage = _AcPMModuleRTPPacketsTxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5, 1, 8),
    _AcPMModuleRTPPacketsTxFullDayAverage_Type()
)
acPMModuleRTPPacketsTxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxFullDayAverage.setStatus("current")


class _AcPMModuleRTPPacketsTxTotal_Type(Integer32):
    """Custom type acPMModuleRTPPacketsTxTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketsTxTotal_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsTxTotal_Object = MibTableColumn
acPMModuleRTPPacketsTxTotal = _AcPMModuleRTPPacketsTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5, 1, 9),
    _AcPMModuleRTPPacketsTxTotal_Type()
)
acPMModuleRTPPacketsTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxTotal.setStatus("current")
_AcPMModuleRTPPacketsTxVolume_Type = Counter32
_AcPMModuleRTPPacketsTxVolume_Object = MibTableColumn
acPMModuleRTPPacketsTxVolume = _AcPMModuleRTPPacketsTxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 5, 1, 10),
    _AcPMModuleRTPPacketsTxVolume_Type()
)
acPMModuleRTPPacketsTxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsTxVolume.setStatus("current")
_AcPMModuleRTPPacketsRxTable_Object = MibTable
acPMModuleRTPPacketsRxTable = _AcPMModuleRTPPacketsRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6)
)
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxTable.setStatus("current")
_AcPMModuleRTPPacketsRxEntry_Object = MibTableRow
acPMModuleRTPPacketsRxEntry = _AcPMModuleRTPPacketsRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6, 1)
)
acPMModuleRTPPacketsRxEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMModuleRTPPacketsRxInterval"),
)
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxEntry.setStatus("current")


class _AcPMModuleRTPPacketsRxInterval_Type(Unsigned32):
    """Custom type acPMModuleRTPPacketsRxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMModuleRTPPacketsRxInterval_Type.__name__ = "Unsigned32"
_AcPMModuleRTPPacketsRxInterval_Object = MibTableColumn
acPMModuleRTPPacketsRxInterval = _AcPMModuleRTPPacketsRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6, 1, 1),
    _AcPMModuleRTPPacketsRxInterval_Type()
)
acPMModuleRTPPacketsRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxInterval.setStatus("current")


class _AcPMModuleRTPPacketsRxAverage_Type(Integer32):
    """Custom type acPMModuleRTPPacketsRxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketsRxAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsRxAverage_Object = MibTableColumn
acPMModuleRTPPacketsRxAverage = _AcPMModuleRTPPacketsRxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6, 1, 2),
    _AcPMModuleRTPPacketsRxAverage_Type()
)
acPMModuleRTPPacketsRxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxAverage.setStatus("current")


class _AcPMModuleRTPPacketsRxMax_Type(Integer32):
    """Custom type acPMModuleRTPPacketsRxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketsRxMax_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsRxMax_Object = MibTableColumn
acPMModuleRTPPacketsRxMax = _AcPMModuleRTPPacketsRxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6, 1, 3),
    _AcPMModuleRTPPacketsRxMax_Type()
)
acPMModuleRTPPacketsRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxMax.setStatus("current")


class _AcPMModuleRTPPacketsRxMin_Type(Integer32):
    """Custom type acPMModuleRTPPacketsRxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketsRxMin_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsRxMin_Object = MibTableColumn
acPMModuleRTPPacketsRxMin = _AcPMModuleRTPPacketsRxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6, 1, 4),
    _AcPMModuleRTPPacketsRxMin_Type()
)
acPMModuleRTPPacketsRxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxMin.setStatus("current")


class _AcPMModuleRTPPacketsRxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMModuleRTPPacketsRxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketsRxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsRxTimeBelowLowThreshold_Object = MibTableColumn
acPMModuleRTPPacketsRxTimeBelowLowThreshold = _AcPMModuleRTPPacketsRxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6, 1, 5),
    _AcPMModuleRTPPacketsRxTimeBelowLowThreshold_Type()
)
acPMModuleRTPPacketsRxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxTimeBelowLowThreshold.setStatus("current")


class _AcPMModuleRTPPacketsRxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMModuleRTPPacketsRxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketsRxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsRxTimeBetweenThresholds_Object = MibTableColumn
acPMModuleRTPPacketsRxTimeBetweenThresholds = _AcPMModuleRTPPacketsRxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6, 1, 6),
    _AcPMModuleRTPPacketsRxTimeBetweenThresholds_Type()
)
acPMModuleRTPPacketsRxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxTimeBetweenThresholds.setStatus("current")


class _AcPMModuleRTPPacketsRxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMModuleRTPPacketsRxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModuleRTPPacketsRxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsRxTimeAboveHighThreshold_Object = MibTableColumn
acPMModuleRTPPacketsRxTimeAboveHighThreshold = _AcPMModuleRTPPacketsRxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6, 1, 7),
    _AcPMModuleRTPPacketsRxTimeAboveHighThreshold_Type()
)
acPMModuleRTPPacketsRxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxTimeAboveHighThreshold.setStatus("current")


class _AcPMModuleRTPPacketsRxFullDayAverage_Type(Integer32):
    """Custom type acPMModuleRTPPacketsRxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketsRxFullDayAverage_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsRxFullDayAverage_Object = MibTableColumn
acPMModuleRTPPacketsRxFullDayAverage = _AcPMModuleRTPPacketsRxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6, 1, 8),
    _AcPMModuleRTPPacketsRxFullDayAverage_Type()
)
acPMModuleRTPPacketsRxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxFullDayAverage.setStatus("current")


class _AcPMModuleRTPPacketsRxTotal_Type(Integer32):
    """Custom type acPMModuleRTPPacketsRxTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModuleRTPPacketsRxTotal_Type.__name__ = "Integer32"
_AcPMModuleRTPPacketsRxTotal_Object = MibTableColumn
acPMModuleRTPPacketsRxTotal = _AcPMModuleRTPPacketsRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6, 1, 9),
    _AcPMModuleRTPPacketsRxTotal_Type()
)
acPMModuleRTPPacketsRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxTotal.setStatus("current")
_AcPMModuleRTPPacketsRxVolume_Type = Counter32
_AcPMModuleRTPPacketsRxVolume_Object = MibTableColumn
acPMModuleRTPPacketsRxVolume = _AcPMModuleRTPPacketsRxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 31, 21, 6, 1, 10),
    _AcPMModuleRTPPacketsRxVolume_Type()
)
acPMModuleRTPPacketsRxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModuleRTPPacketsRxVolume.setStatus("current")
_AcPMChannelUtilization_ObjectIdentity = ObjectIdentity
acPMChannelUtilization = _AcPMChannelUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41)
)
_AcPMFaxChannelsTable_Object = MibTable
acPMFaxChannelsTable = _AcPMFaxChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1)
)
if mibBuilder.loadTexts:
    acPMFaxChannelsTable.setStatus("current")
_AcPMFaxChannelsEntry_Object = MibTableRow
acPMFaxChannelsEntry = _AcPMFaxChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1, 1)
)
acPMFaxChannelsEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMFaxChannelsInterval"),
)
if mibBuilder.loadTexts:
    acPMFaxChannelsEntry.setStatus("current")


class _AcPMFaxChannelsInterval_Type(Unsigned32):
    """Custom type acPMFaxChannelsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMFaxChannelsInterval_Type.__name__ = "Unsigned32"
_AcPMFaxChannelsInterval_Object = MibTableColumn
acPMFaxChannelsInterval = _AcPMFaxChannelsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1, 1, 1),
    _AcPMFaxChannelsInterval_Type()
)
acPMFaxChannelsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMFaxChannelsInterval.setStatus("current")
_AcPMFaxChannelsVal_Type = Gauge32
_AcPMFaxChannelsVal_Object = MibTableColumn
acPMFaxChannelsVal = _AcPMFaxChannelsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1, 1, 2),
    _AcPMFaxChannelsVal_Type()
)
acPMFaxChannelsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMFaxChannelsVal.setStatus("current")


class _AcPMFaxChannelsAverage_Type(Integer32):
    """Custom type acPMFaxChannelsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMFaxChannelsAverage_Type.__name__ = "Integer32"
_AcPMFaxChannelsAverage_Object = MibTableColumn
acPMFaxChannelsAverage = _AcPMFaxChannelsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1, 1, 3),
    _AcPMFaxChannelsAverage_Type()
)
acPMFaxChannelsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMFaxChannelsAverage.setStatus("current")


class _AcPMFaxChannelsMax_Type(Integer32):
    """Custom type acPMFaxChannelsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMFaxChannelsMax_Type.__name__ = "Integer32"
_AcPMFaxChannelsMax_Object = MibTableColumn
acPMFaxChannelsMax = _AcPMFaxChannelsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1, 1, 4),
    _AcPMFaxChannelsMax_Type()
)
acPMFaxChannelsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMFaxChannelsMax.setStatus("current")


class _AcPMFaxChannelsMin_Type(Integer32):
    """Custom type acPMFaxChannelsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMFaxChannelsMin_Type.__name__ = "Integer32"
_AcPMFaxChannelsMin_Object = MibTableColumn
acPMFaxChannelsMin = _AcPMFaxChannelsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1, 1, 5),
    _AcPMFaxChannelsMin_Type()
)
acPMFaxChannelsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMFaxChannelsMin.setStatus("current")


class _AcPMFaxChannelsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMFaxChannelsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMFaxChannelsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMFaxChannelsTimeBelowLowThreshold_Object = MibTableColumn
acPMFaxChannelsTimeBelowLowThreshold = _AcPMFaxChannelsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1, 1, 6),
    _AcPMFaxChannelsTimeBelowLowThreshold_Type()
)
acPMFaxChannelsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMFaxChannelsTimeBelowLowThreshold.setStatus("current")


class _AcPMFaxChannelsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMFaxChannelsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMFaxChannelsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMFaxChannelsTimeBetweenThresholds_Object = MibTableColumn
acPMFaxChannelsTimeBetweenThresholds = _AcPMFaxChannelsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1, 1, 7),
    _AcPMFaxChannelsTimeBetweenThresholds_Type()
)
acPMFaxChannelsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMFaxChannelsTimeBetweenThresholds.setStatus("current")


class _AcPMFaxChannelsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMFaxChannelsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMFaxChannelsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMFaxChannelsTimeAboveHighThreshold_Object = MibTableColumn
acPMFaxChannelsTimeAboveHighThreshold = _AcPMFaxChannelsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1, 1, 8),
    _AcPMFaxChannelsTimeAboveHighThreshold_Type()
)
acPMFaxChannelsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMFaxChannelsTimeAboveHighThreshold.setStatus("current")


class _AcPMFaxChannelsFullDayAverage_Type(Integer32):
    """Custom type acPMFaxChannelsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMFaxChannelsFullDayAverage_Type.__name__ = "Integer32"
_AcPMFaxChannelsFullDayAverage_Object = MibTableColumn
acPMFaxChannelsFullDayAverage = _AcPMFaxChannelsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1, 1, 9),
    _AcPMFaxChannelsFullDayAverage_Type()
)
acPMFaxChannelsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMFaxChannelsFullDayAverage.setStatus("current")
_AcPMFaxChannelsVolume_Type = Counter32
_AcPMFaxChannelsVolume_Object = MibTableColumn
acPMFaxChannelsVolume = _AcPMFaxChannelsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 1, 1, 10),
    _AcPMFaxChannelsVolume_Type()
)
acPMFaxChannelsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMFaxChannelsVolume.setStatus("current")
_AcPMModemChannelsTable_Object = MibTable
acPMModemChannelsTable = _AcPMModemChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 2)
)
if mibBuilder.loadTexts:
    acPMModemChannelsTable.setStatus("current")
_AcPMModemChannelsEntry_Object = MibTableRow
acPMModemChannelsEntry = _AcPMModemChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 2, 1)
)
acPMModemChannelsEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMModemChannelsInterval"),
)
if mibBuilder.loadTexts:
    acPMModemChannelsEntry.setStatus("current")


class _AcPMModemChannelsInterval_Type(Unsigned32):
    """Custom type acPMModemChannelsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMModemChannelsInterval_Type.__name__ = "Unsigned32"
_AcPMModemChannelsInterval_Object = MibTableColumn
acPMModemChannelsInterval = _AcPMModemChannelsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 2, 1, 1),
    _AcPMModemChannelsInterval_Type()
)
acPMModemChannelsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMModemChannelsInterval.setStatus("current")
_AcPMModemChannelsVal_Type = Gauge32
_AcPMModemChannelsVal_Object = MibTableColumn
acPMModemChannelsVal = _AcPMModemChannelsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 2, 1, 2),
    _AcPMModemChannelsVal_Type()
)
acPMModemChannelsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemChannelsVal.setStatus("current")


class _AcPMModemChannelsAverage_Type(Integer32):
    """Custom type acPMModemChannelsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModemChannelsAverage_Type.__name__ = "Integer32"
_AcPMModemChannelsAverage_Object = MibTableColumn
acPMModemChannelsAverage = _AcPMModemChannelsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 2, 1, 3),
    _AcPMModemChannelsAverage_Type()
)
acPMModemChannelsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemChannelsAverage.setStatus("current")


class _AcPMModemChannelsMax_Type(Integer32):
    """Custom type acPMModemChannelsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModemChannelsMax_Type.__name__ = "Integer32"
_AcPMModemChannelsMax_Object = MibTableColumn
acPMModemChannelsMax = _AcPMModemChannelsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 2, 1, 4),
    _AcPMModemChannelsMax_Type()
)
acPMModemChannelsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemChannelsMax.setStatus("current")


class _AcPMModemChannelsMin_Type(Integer32):
    """Custom type acPMModemChannelsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModemChannelsMin_Type.__name__ = "Integer32"
_AcPMModemChannelsMin_Object = MibTableColumn
acPMModemChannelsMin = _AcPMModemChannelsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 2, 1, 5),
    _AcPMModemChannelsMin_Type()
)
acPMModemChannelsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemChannelsMin.setStatus("current")


class _AcPMModemChannelsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMModemChannelsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModemChannelsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMModemChannelsTimeBelowLowThreshold_Object = MibTableColumn
acPMModemChannelsTimeBelowLowThreshold = _AcPMModemChannelsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 2, 1, 6),
    _AcPMModemChannelsTimeBelowLowThreshold_Type()
)
acPMModemChannelsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemChannelsTimeBelowLowThreshold.setStatus("current")


class _AcPMModemChannelsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMModemChannelsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModemChannelsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMModemChannelsTimeBetweenThresholds_Object = MibTableColumn
acPMModemChannelsTimeBetweenThresholds = _AcPMModemChannelsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 2, 1, 7),
    _AcPMModemChannelsTimeBetweenThresholds_Type()
)
acPMModemChannelsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemChannelsTimeBetweenThresholds.setStatus("current")


class _AcPMModemChannelsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMModemChannelsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModemChannelsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMModemChannelsTimeAboveHighThreshold_Object = MibTableColumn
acPMModemChannelsTimeAboveHighThreshold = _AcPMModemChannelsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 2, 1, 8),
    _AcPMModemChannelsTimeAboveHighThreshold_Type()
)
acPMModemChannelsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemChannelsTimeAboveHighThreshold.setStatus("current")


class _AcPMModemChannelsFullDayAverage_Type(Integer32):
    """Custom type acPMModemChannelsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModemChannelsFullDayAverage_Type.__name__ = "Integer32"
_AcPMModemChannelsFullDayAverage_Object = MibTableColumn
acPMModemChannelsFullDayAverage = _AcPMModemChannelsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 2, 1, 9),
    _AcPMModemChannelsFullDayAverage_Type()
)
acPMModemChannelsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemChannelsFullDayAverage.setStatus("current")
_AcPMTdm2IpChannelsTable_Object = MibTable
acPMTdm2IpChannelsTable = _AcPMTdm2IpChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3)
)
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsTable.setStatus("current")
_AcPMTdm2IpChannelsEntry_Object = MibTableRow
acPMTdm2IpChannelsEntry = _AcPMTdm2IpChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3, 1)
)
acPMTdm2IpChannelsEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMTdm2IpChannelsInterval"),
)
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsEntry.setStatus("current")


class _AcPMTdm2IpChannelsInterval_Type(Unsigned32):
    """Custom type acPMTdm2IpChannelsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMTdm2IpChannelsInterval_Type.__name__ = "Unsigned32"
_AcPMTdm2IpChannelsInterval_Object = MibTableColumn
acPMTdm2IpChannelsInterval = _AcPMTdm2IpChannelsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3, 1, 1),
    _AcPMTdm2IpChannelsInterval_Type()
)
acPMTdm2IpChannelsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsInterval.setStatus("current")
_AcPMTdm2IpChannelsVal_Type = Gauge32
_AcPMTdm2IpChannelsVal_Object = MibTableColumn
acPMTdm2IpChannelsVal = _AcPMTdm2IpChannelsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3, 1, 2),
    _AcPMTdm2IpChannelsVal_Type()
)
acPMTdm2IpChannelsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsVal.setStatus("current")


class _AcPMTdm2IpChannelsAverage_Type(Integer32):
    """Custom type acPMTdm2IpChannelsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTdm2IpChannelsAverage_Type.__name__ = "Integer32"
_AcPMTdm2IpChannelsAverage_Object = MibTableColumn
acPMTdm2IpChannelsAverage = _AcPMTdm2IpChannelsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3, 1, 3),
    _AcPMTdm2IpChannelsAverage_Type()
)
acPMTdm2IpChannelsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsAverage.setStatus("current")


class _AcPMTdm2IpChannelsMax_Type(Integer32):
    """Custom type acPMTdm2IpChannelsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTdm2IpChannelsMax_Type.__name__ = "Integer32"
_AcPMTdm2IpChannelsMax_Object = MibTableColumn
acPMTdm2IpChannelsMax = _AcPMTdm2IpChannelsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3, 1, 4),
    _AcPMTdm2IpChannelsMax_Type()
)
acPMTdm2IpChannelsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsMax.setStatus("current")


class _AcPMTdm2IpChannelsMin_Type(Integer32):
    """Custom type acPMTdm2IpChannelsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTdm2IpChannelsMin_Type.__name__ = "Integer32"
_AcPMTdm2IpChannelsMin_Object = MibTableColumn
acPMTdm2IpChannelsMin = _AcPMTdm2IpChannelsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3, 1, 5),
    _AcPMTdm2IpChannelsMin_Type()
)
acPMTdm2IpChannelsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsMin.setStatus("current")
_AcPMTdm2IpChannelsVolume_Type = Counter32
_AcPMTdm2IpChannelsVolume_Object = MibTableColumn
acPMTdm2IpChannelsVolume = _AcPMTdm2IpChannelsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3, 1, 6),
    _AcPMTdm2IpChannelsVolume_Type()
)
acPMTdm2IpChannelsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsVolume.setStatus("current")


class _AcPMTdm2IpChannelsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMTdm2IpChannelsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTdm2IpChannelsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMTdm2IpChannelsTimeBelowLowThreshold_Object = MibTableColumn
acPMTdm2IpChannelsTimeBelowLowThreshold = _AcPMTdm2IpChannelsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3, 1, 7),
    _AcPMTdm2IpChannelsTimeBelowLowThreshold_Type()
)
acPMTdm2IpChannelsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsTimeBelowLowThreshold.setStatus("current")


class _AcPMTdm2IpChannelsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMTdm2IpChannelsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTdm2IpChannelsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMTdm2IpChannelsTimeBetweenThresholds_Object = MibTableColumn
acPMTdm2IpChannelsTimeBetweenThresholds = _AcPMTdm2IpChannelsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3, 1, 8),
    _AcPMTdm2IpChannelsTimeBetweenThresholds_Type()
)
acPMTdm2IpChannelsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsTimeBetweenThresholds.setStatus("current")


class _AcPMTdm2IpChannelsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMTdm2IpChannelsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTdm2IpChannelsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMTdm2IpChannelsTimeAboveHighThreshold_Object = MibTableColumn
acPMTdm2IpChannelsTimeAboveHighThreshold = _AcPMTdm2IpChannelsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3, 1, 9),
    _AcPMTdm2IpChannelsTimeAboveHighThreshold_Type()
)
acPMTdm2IpChannelsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsTimeAboveHighThreshold.setStatus("current")


class _AcPMTdm2IpChannelsFullDayAverage_Type(Integer32):
    """Custom type acPMTdm2IpChannelsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTdm2IpChannelsFullDayAverage_Type.__name__ = "Integer32"
_AcPMTdm2IpChannelsFullDayAverage_Object = MibTableColumn
acPMTdm2IpChannelsFullDayAverage = _AcPMTdm2IpChannelsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 3, 1, 10),
    _AcPMTdm2IpChannelsFullDayAverage_Type()
)
acPMTdm2IpChannelsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTdm2IpChannelsFullDayAverage.setStatus("current")
_AcPMRTPStreamsTable_Object = MibTable
acPMRTPStreamsTable = _AcPMRTPStreamsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4)
)
if mibBuilder.loadTexts:
    acPMRTPStreamsTable.setStatus("current")
_AcPMRTPStreamsEntry_Object = MibTableRow
acPMRTPStreamsEntry = _AcPMRTPStreamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4, 1)
)
acPMRTPStreamsEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMRTPStreamsInterval"),
)
if mibBuilder.loadTexts:
    acPMRTPStreamsEntry.setStatus("current")


class _AcPMRTPStreamsInterval_Type(Unsigned32):
    """Custom type acPMRTPStreamsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRTPStreamsInterval_Type.__name__ = "Unsigned32"
_AcPMRTPStreamsInterval_Object = MibTableColumn
acPMRTPStreamsInterval = _AcPMRTPStreamsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4, 1, 1),
    _AcPMRTPStreamsInterval_Type()
)
acPMRTPStreamsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRTPStreamsInterval.setStatus("current")
_AcPMRTPStreamsVal_Type = Gauge32
_AcPMRTPStreamsVal_Object = MibTableColumn
acPMRTPStreamsVal = _AcPMRTPStreamsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4, 1, 2),
    _AcPMRTPStreamsVal_Type()
)
acPMRTPStreamsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPStreamsVal.setStatus("current")


class _AcPMRTPStreamsAverage_Type(Integer32):
    """Custom type acPMRTPStreamsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPStreamsAverage_Type.__name__ = "Integer32"
_AcPMRTPStreamsAverage_Object = MibTableColumn
acPMRTPStreamsAverage = _AcPMRTPStreamsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4, 1, 3),
    _AcPMRTPStreamsAverage_Type()
)
acPMRTPStreamsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPStreamsAverage.setStatus("current")


class _AcPMRTPStreamsMax_Type(Integer32):
    """Custom type acPMRTPStreamsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPStreamsMax_Type.__name__ = "Integer32"
_AcPMRTPStreamsMax_Object = MibTableColumn
acPMRTPStreamsMax = _AcPMRTPStreamsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4, 1, 4),
    _AcPMRTPStreamsMax_Type()
)
acPMRTPStreamsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPStreamsMax.setStatus("current")


class _AcPMRTPStreamsMin_Type(Integer32):
    """Custom type acPMRTPStreamsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPStreamsMin_Type.__name__ = "Integer32"
_AcPMRTPStreamsMin_Object = MibTableColumn
acPMRTPStreamsMin = _AcPMRTPStreamsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4, 1, 5),
    _AcPMRTPStreamsMin_Type()
)
acPMRTPStreamsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPStreamsMin.setStatus("current")
_AcPMRTPStreamsVolume_Type = Counter32
_AcPMRTPStreamsVolume_Object = MibTableColumn
acPMRTPStreamsVolume = _AcPMRTPStreamsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4, 1, 6),
    _AcPMRTPStreamsVolume_Type()
)
acPMRTPStreamsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPStreamsVolume.setStatus("current")


class _AcPMRTPStreamsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRTPStreamsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPStreamsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRTPStreamsTimeBelowLowThreshold_Object = MibTableColumn
acPMRTPStreamsTimeBelowLowThreshold = _AcPMRTPStreamsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4, 1, 7),
    _AcPMRTPStreamsTimeBelowLowThreshold_Type()
)
acPMRTPStreamsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPStreamsTimeBelowLowThreshold.setStatus("current")


class _AcPMRTPStreamsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRTPStreamsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPStreamsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRTPStreamsTimeBetweenThresholds_Object = MibTableColumn
acPMRTPStreamsTimeBetweenThresholds = _AcPMRTPStreamsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4, 1, 8),
    _AcPMRTPStreamsTimeBetweenThresholds_Type()
)
acPMRTPStreamsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPStreamsTimeBetweenThresholds.setStatus("current")


class _AcPMRTPStreamsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRTPStreamsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRTPStreamsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRTPStreamsTimeAboveHighThreshold_Object = MibTableColumn
acPMRTPStreamsTimeAboveHighThreshold = _AcPMRTPStreamsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4, 1, 9),
    _AcPMRTPStreamsTimeAboveHighThreshold_Type()
)
acPMRTPStreamsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPStreamsTimeAboveHighThreshold.setStatus("current")


class _AcPMRTPStreamsFullDayAverage_Type(Integer32):
    """Custom type acPMRTPStreamsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRTPStreamsFullDayAverage_Type.__name__ = "Integer32"
_AcPMRTPStreamsFullDayAverage_Object = MibTableColumn
acPMRTPStreamsFullDayAverage = _AcPMRTPStreamsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 4, 1, 10),
    _AcPMRTPStreamsFullDayAverage_Type()
)
acPMRTPStreamsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRTPStreamsFullDayAverage.setStatus("current")
_AcPMSRTPStreamsTable_Object = MibTable
acPMSRTPStreamsTable = _AcPMSRTPStreamsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5)
)
if mibBuilder.loadTexts:
    acPMSRTPStreamsTable.setStatus("current")
_AcPMSRTPStreamsEntry_Object = MibTableRow
acPMSRTPStreamsEntry = _AcPMSRTPStreamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5, 1)
)
acPMSRTPStreamsEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMSRTPStreamsInterval"),
)
if mibBuilder.loadTexts:
    acPMSRTPStreamsEntry.setStatus("current")


class _AcPMSRTPStreamsInterval_Type(Unsigned32):
    """Custom type acPMSRTPStreamsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSRTPStreamsInterval_Type.__name__ = "Unsigned32"
_AcPMSRTPStreamsInterval_Object = MibTableColumn
acPMSRTPStreamsInterval = _AcPMSRTPStreamsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5, 1, 1),
    _AcPMSRTPStreamsInterval_Type()
)
acPMSRTPStreamsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSRTPStreamsInterval.setStatus("current")
_AcPMSRTPStreamsVal_Type = Gauge32
_AcPMSRTPStreamsVal_Object = MibTableColumn
acPMSRTPStreamsVal = _AcPMSRTPStreamsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5, 1, 2),
    _AcPMSRTPStreamsVal_Type()
)
acPMSRTPStreamsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSRTPStreamsVal.setStatus("current")


class _AcPMSRTPStreamsAverage_Type(Integer32):
    """Custom type acPMSRTPStreamsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSRTPStreamsAverage_Type.__name__ = "Integer32"
_AcPMSRTPStreamsAverage_Object = MibTableColumn
acPMSRTPStreamsAverage = _AcPMSRTPStreamsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5, 1, 3),
    _AcPMSRTPStreamsAverage_Type()
)
acPMSRTPStreamsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSRTPStreamsAverage.setStatus("current")


class _AcPMSRTPStreamsMax_Type(Integer32):
    """Custom type acPMSRTPStreamsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSRTPStreamsMax_Type.__name__ = "Integer32"
_AcPMSRTPStreamsMax_Object = MibTableColumn
acPMSRTPStreamsMax = _AcPMSRTPStreamsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5, 1, 4),
    _AcPMSRTPStreamsMax_Type()
)
acPMSRTPStreamsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSRTPStreamsMax.setStatus("current")


class _AcPMSRTPStreamsMin_Type(Integer32):
    """Custom type acPMSRTPStreamsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSRTPStreamsMin_Type.__name__ = "Integer32"
_AcPMSRTPStreamsMin_Object = MibTableColumn
acPMSRTPStreamsMin = _AcPMSRTPStreamsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5, 1, 5),
    _AcPMSRTPStreamsMin_Type()
)
acPMSRTPStreamsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSRTPStreamsMin.setStatus("current")
_AcPMSRTPStreamsVolume_Type = Counter32
_AcPMSRTPStreamsVolume_Object = MibTableColumn
acPMSRTPStreamsVolume = _AcPMSRTPStreamsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5, 1, 6),
    _AcPMSRTPStreamsVolume_Type()
)
acPMSRTPStreamsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSRTPStreamsVolume.setStatus("current")


class _AcPMSRTPStreamsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMSRTPStreamsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSRTPStreamsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMSRTPStreamsTimeBelowLowThreshold_Object = MibTableColumn
acPMSRTPStreamsTimeBelowLowThreshold = _AcPMSRTPStreamsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5, 1, 7),
    _AcPMSRTPStreamsTimeBelowLowThreshold_Type()
)
acPMSRTPStreamsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSRTPStreamsTimeBelowLowThreshold.setStatus("current")


class _AcPMSRTPStreamsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMSRTPStreamsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSRTPStreamsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMSRTPStreamsTimeBetweenThresholds_Object = MibTableColumn
acPMSRTPStreamsTimeBetweenThresholds = _AcPMSRTPStreamsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5, 1, 8),
    _AcPMSRTPStreamsTimeBetweenThresholds_Type()
)
acPMSRTPStreamsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSRTPStreamsTimeBetweenThresholds.setStatus("current")


class _AcPMSRTPStreamsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMSRTPStreamsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSRTPStreamsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMSRTPStreamsTimeAboveHighThreshold_Object = MibTableColumn
acPMSRTPStreamsTimeAboveHighThreshold = _AcPMSRTPStreamsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5, 1, 9),
    _AcPMSRTPStreamsTimeAboveHighThreshold_Type()
)
acPMSRTPStreamsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSRTPStreamsTimeAboveHighThreshold.setStatus("current")


class _AcPMSRTPStreamsFullDayAverage_Type(Integer32):
    """Custom type acPMSRTPStreamsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSRTPStreamsFullDayAverage_Type.__name__ = "Integer32"
_AcPMSRTPStreamsFullDayAverage_Object = MibTableColumn
acPMSRTPStreamsFullDayAverage = _AcPMSRTPStreamsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 5, 1, 10),
    _AcPMSRTPStreamsFullDayAverage_Type()
)
acPMSRTPStreamsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSRTPStreamsFullDayAverage.setStatus("current")
_AcPMMulticastRegisteredChannelsTable_Object = MibTable
acPMMulticastRegisteredChannelsTable = _AcPMMulticastRegisteredChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6)
)
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsTable.setStatus("current")
_AcPMMulticastRegisteredChannelsEntry_Object = MibTableRow
acPMMulticastRegisteredChannelsEntry = _AcPMMulticastRegisteredChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6, 1)
)
acPMMulticastRegisteredChannelsEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMMulticastRegisteredChannelsInterval"),
)
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsEntry.setStatus("current")


class _AcPMMulticastRegisteredChannelsInterval_Type(Unsigned32):
    """Custom type acPMMulticastRegisteredChannelsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMulticastRegisteredChannelsInterval_Type.__name__ = "Unsigned32"
_AcPMMulticastRegisteredChannelsInterval_Object = MibTableColumn
acPMMulticastRegisteredChannelsInterval = _AcPMMulticastRegisteredChannelsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6, 1, 1),
    _AcPMMulticastRegisteredChannelsInterval_Type()
)
acPMMulticastRegisteredChannelsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsInterval.setStatus("current")
_AcPMMulticastRegisteredChannelsVal_Type = Gauge32
_AcPMMulticastRegisteredChannelsVal_Object = MibTableColumn
acPMMulticastRegisteredChannelsVal = _AcPMMulticastRegisteredChannelsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6, 1, 2),
    _AcPMMulticastRegisteredChannelsVal_Type()
)
acPMMulticastRegisteredChannelsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsVal.setStatus("current")


class _AcPMMulticastRegisteredChannelsAverage_Type(Integer32):
    """Custom type acPMMulticastRegisteredChannelsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastRegisteredChannelsAverage_Type.__name__ = "Integer32"
_AcPMMulticastRegisteredChannelsAverage_Object = MibTableColumn
acPMMulticastRegisteredChannelsAverage = _AcPMMulticastRegisteredChannelsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6, 1, 3),
    _AcPMMulticastRegisteredChannelsAverage_Type()
)
acPMMulticastRegisteredChannelsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsAverage.setStatus("current")


class _AcPMMulticastRegisteredChannelsMax_Type(Integer32):
    """Custom type acPMMulticastRegisteredChannelsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastRegisteredChannelsMax_Type.__name__ = "Integer32"
_AcPMMulticastRegisteredChannelsMax_Object = MibTableColumn
acPMMulticastRegisteredChannelsMax = _AcPMMulticastRegisteredChannelsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6, 1, 4),
    _AcPMMulticastRegisteredChannelsMax_Type()
)
acPMMulticastRegisteredChannelsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsMax.setStatus("current")


class _AcPMMulticastRegisteredChannelsMin_Type(Integer32):
    """Custom type acPMMulticastRegisteredChannelsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastRegisteredChannelsMin_Type.__name__ = "Integer32"
_AcPMMulticastRegisteredChannelsMin_Object = MibTableColumn
acPMMulticastRegisteredChannelsMin = _AcPMMulticastRegisteredChannelsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6, 1, 5),
    _AcPMMulticastRegisteredChannelsMin_Type()
)
acPMMulticastRegisteredChannelsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsMin.setStatus("current")
_AcPMMulticastRegisteredChannelsVolume_Type = Counter32
_AcPMMulticastRegisteredChannelsVolume_Object = MibTableColumn
acPMMulticastRegisteredChannelsVolume = _AcPMMulticastRegisteredChannelsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6, 1, 6),
    _AcPMMulticastRegisteredChannelsVolume_Type()
)
acPMMulticastRegisteredChannelsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsVolume.setStatus("current")


class _AcPMMulticastRegisteredChannelsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMMulticastRegisteredChannelsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMMulticastRegisteredChannelsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMMulticastRegisteredChannelsTimeBelowLowThreshold_Object = MibTableColumn
acPMMulticastRegisteredChannelsTimeBelowLowThreshold = _AcPMMulticastRegisteredChannelsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6, 1, 7),
    _AcPMMulticastRegisteredChannelsTimeBelowLowThreshold_Type()
)
acPMMulticastRegisteredChannelsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsTimeBelowLowThreshold.setStatus("current")


class _AcPMMulticastRegisteredChannelsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMMulticastRegisteredChannelsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMMulticastRegisteredChannelsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMMulticastRegisteredChannelsTimeBetweenThresholds_Object = MibTableColumn
acPMMulticastRegisteredChannelsTimeBetweenThresholds = _AcPMMulticastRegisteredChannelsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6, 1, 8),
    _AcPMMulticastRegisteredChannelsTimeBetweenThresholds_Type()
)
acPMMulticastRegisteredChannelsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsTimeBetweenThresholds.setStatus("current")


class _AcPMMulticastRegisteredChannelsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMMulticastRegisteredChannelsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMMulticastRegisteredChannelsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMMulticastRegisteredChannelsTimeAboveHighThreshold_Object = MibTableColumn
acPMMulticastRegisteredChannelsTimeAboveHighThreshold = _AcPMMulticastRegisteredChannelsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6, 1, 9),
    _AcPMMulticastRegisteredChannelsTimeAboveHighThreshold_Type()
)
acPMMulticastRegisteredChannelsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsTimeAboveHighThreshold.setStatus("current")


class _AcPMMulticastRegisteredChannelsFullDayAverage_Type(Integer32):
    """Custom type acPMMulticastRegisteredChannelsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastRegisteredChannelsFullDayAverage_Type.__name__ = "Integer32"
_AcPMMulticastRegisteredChannelsFullDayAverage_Object = MibTableColumn
acPMMulticastRegisteredChannelsFullDayAverage = _AcPMMulticastRegisteredChannelsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 6, 1, 10),
    _AcPMMulticastRegisteredChannelsFullDayAverage_Type()
)
acPMMulticastRegisteredChannelsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastRegisteredChannelsFullDayAverage.setStatus("current")
_AcPMModemRelayActiveChannelsTable_Object = MibTable
acPMModemRelayActiveChannelsTable = _AcPMModemRelayActiveChannelsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7)
)
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsTable.setStatus("current")
_AcPMModemRelayActiveChannelsEntry_Object = MibTableRow
acPMModemRelayActiveChannelsEntry = _AcPMModemRelayActiveChannelsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7, 1)
)
acPMModemRelayActiveChannelsEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMModemRelayActiveChannelsInterval"),
)
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsEntry.setStatus("current")


class _AcPMModemRelayActiveChannelsInterval_Type(Unsigned32):
    """Custom type acPMModemRelayActiveChannelsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMModemRelayActiveChannelsInterval_Type.__name__ = "Unsigned32"
_AcPMModemRelayActiveChannelsInterval_Object = MibTableColumn
acPMModemRelayActiveChannelsInterval = _AcPMModemRelayActiveChannelsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7, 1, 1),
    _AcPMModemRelayActiveChannelsInterval_Type()
)
acPMModemRelayActiveChannelsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsInterval.setStatus("current")
_AcPMModemRelayActiveChannelsVal_Type = Gauge32
_AcPMModemRelayActiveChannelsVal_Object = MibTableColumn
acPMModemRelayActiveChannelsVal = _AcPMModemRelayActiveChannelsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7, 1, 2),
    _AcPMModemRelayActiveChannelsVal_Type()
)
acPMModemRelayActiveChannelsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsVal.setStatus("current")


class _AcPMModemRelayActiveChannelsAverage_Type(Integer32):
    """Custom type acPMModemRelayActiveChannelsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModemRelayActiveChannelsAverage_Type.__name__ = "Integer32"
_AcPMModemRelayActiveChannelsAverage_Object = MibTableColumn
acPMModemRelayActiveChannelsAverage = _AcPMModemRelayActiveChannelsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7, 1, 3),
    _AcPMModemRelayActiveChannelsAverage_Type()
)
acPMModemRelayActiveChannelsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsAverage.setStatus("current")


class _AcPMModemRelayActiveChannelsMax_Type(Integer32):
    """Custom type acPMModemRelayActiveChannelsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModemRelayActiveChannelsMax_Type.__name__ = "Integer32"
_AcPMModemRelayActiveChannelsMax_Object = MibTableColumn
acPMModemRelayActiveChannelsMax = _AcPMModemRelayActiveChannelsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7, 1, 4),
    _AcPMModemRelayActiveChannelsMax_Type()
)
acPMModemRelayActiveChannelsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsMax.setStatus("current")


class _AcPMModemRelayActiveChannelsMin_Type(Integer32):
    """Custom type acPMModemRelayActiveChannelsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModemRelayActiveChannelsMin_Type.__name__ = "Integer32"
_AcPMModemRelayActiveChannelsMin_Object = MibTableColumn
acPMModemRelayActiveChannelsMin = _AcPMModemRelayActiveChannelsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7, 1, 5),
    _AcPMModemRelayActiveChannelsMin_Type()
)
acPMModemRelayActiveChannelsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsMin.setStatus("current")
_AcPMModemRelayActiveChannelsVolume_Type = Counter32
_AcPMModemRelayActiveChannelsVolume_Object = MibTableColumn
acPMModemRelayActiveChannelsVolume = _AcPMModemRelayActiveChannelsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7, 1, 6),
    _AcPMModemRelayActiveChannelsVolume_Type()
)
acPMModemRelayActiveChannelsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsVolume.setStatus("current")


class _AcPMModemRelayActiveChannelsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMModemRelayActiveChannelsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModemRelayActiveChannelsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMModemRelayActiveChannelsTimeBelowLowThreshold_Object = MibTableColumn
acPMModemRelayActiveChannelsTimeBelowLowThreshold = _AcPMModemRelayActiveChannelsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7, 1, 7),
    _AcPMModemRelayActiveChannelsTimeBelowLowThreshold_Type()
)
acPMModemRelayActiveChannelsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsTimeBelowLowThreshold.setStatus("current")


class _AcPMModemRelayActiveChannelsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMModemRelayActiveChannelsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModemRelayActiveChannelsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMModemRelayActiveChannelsTimeBetweenThresholds_Object = MibTableColumn
acPMModemRelayActiveChannelsTimeBetweenThresholds = _AcPMModemRelayActiveChannelsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7, 1, 8),
    _AcPMModemRelayActiveChannelsTimeBetweenThresholds_Type()
)
acPMModemRelayActiveChannelsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsTimeBetweenThresholds.setStatus("current")


class _AcPMModemRelayActiveChannelsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMModemRelayActiveChannelsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMModemRelayActiveChannelsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMModemRelayActiveChannelsTimeAboveHighThreshold_Object = MibTableColumn
acPMModemRelayActiveChannelsTimeAboveHighThreshold = _AcPMModemRelayActiveChannelsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7, 1, 9),
    _AcPMModemRelayActiveChannelsTimeAboveHighThreshold_Type()
)
acPMModemRelayActiveChannelsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsTimeAboveHighThreshold.setStatus("current")


class _AcPMModemRelayActiveChannelsFullDayAverage_Type(Integer32):
    """Custom type acPMModemRelayActiveChannelsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMModemRelayActiveChannelsFullDayAverage_Type.__name__ = "Integer32"
_AcPMModemRelayActiveChannelsFullDayAverage_Object = MibTableColumn
acPMModemRelayActiveChannelsFullDayAverage = _AcPMModemRelayActiveChannelsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 41, 7, 1, 10),
    _AcPMModemRelayActiveChannelsFullDayAverage_Type()
)
acPMModemRelayActiveChannelsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMModemRelayActiveChannelsFullDayAverage.setStatus("current")
_AcPMStreamingCache_ObjectIdentity = ObjectIdentity
acPMStreamingCache = _AcPMStreamingCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42)
)
_AcPMStreamingCacheHitRateTable_Object = MibTable
acPMStreamingCacheHitRateTable = _AcPMStreamingCacheHitRateTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 1)
)
if mibBuilder.loadTexts:
    acPMStreamingCacheHitRateTable.setStatus("current")
_AcPMStreamingCacheHitRateEntry_Object = MibTableRow
acPMStreamingCacheHitRateEntry = _AcPMStreamingCacheHitRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 1, 1)
)
acPMStreamingCacheHitRateEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMStreamingCacheHitRateInterval"),
)
if mibBuilder.loadTexts:
    acPMStreamingCacheHitRateEntry.setStatus("current")


class _AcPMStreamingCacheHitRateInterval_Type(Unsigned32):
    """Custom type acPMStreamingCacheHitRateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMStreamingCacheHitRateInterval_Type.__name__ = "Unsigned32"
_AcPMStreamingCacheHitRateInterval_Object = MibTableColumn
acPMStreamingCacheHitRateInterval = _AcPMStreamingCacheHitRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 1, 1, 1),
    _AcPMStreamingCacheHitRateInterval_Type()
)
acPMStreamingCacheHitRateInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMStreamingCacheHitRateInterval.setStatus("current")


class _AcPMStreamingCacheHitRateAverage_Type(Integer32):
    """Custom type acPMStreamingCacheHitRateAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheHitRateAverage_Type.__name__ = "Integer32"
_AcPMStreamingCacheHitRateAverage_Object = MibTableColumn
acPMStreamingCacheHitRateAverage = _AcPMStreamingCacheHitRateAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 1, 1, 2),
    _AcPMStreamingCacheHitRateAverage_Type()
)
acPMStreamingCacheHitRateAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheHitRateAverage.setStatus("current")


class _AcPMStreamingCacheHitRateMax_Type(Integer32):
    """Custom type acPMStreamingCacheHitRateMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheHitRateMax_Type.__name__ = "Integer32"
_AcPMStreamingCacheHitRateMax_Object = MibTableColumn
acPMStreamingCacheHitRateMax = _AcPMStreamingCacheHitRateMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 1, 1, 3),
    _AcPMStreamingCacheHitRateMax_Type()
)
acPMStreamingCacheHitRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheHitRateMax.setStatus("current")


class _AcPMStreamingCacheHitRateMin_Type(Integer32):
    """Custom type acPMStreamingCacheHitRateMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheHitRateMin_Type.__name__ = "Integer32"
_AcPMStreamingCacheHitRateMin_Object = MibTableColumn
acPMStreamingCacheHitRateMin = _AcPMStreamingCacheHitRateMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 1, 1, 4),
    _AcPMStreamingCacheHitRateMin_Type()
)
acPMStreamingCacheHitRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheHitRateMin.setStatus("current")
_AcPMStreamingCacheHitRateVolume_Type = Counter32
_AcPMStreamingCacheHitRateVolume_Object = MibTableColumn
acPMStreamingCacheHitRateVolume = _AcPMStreamingCacheHitRateVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 1, 1, 5),
    _AcPMStreamingCacheHitRateVolume_Type()
)
acPMStreamingCacheHitRateVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheHitRateVolume.setStatus("current")


class _AcPMStreamingCacheHitRateTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMStreamingCacheHitRateTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMStreamingCacheHitRateTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMStreamingCacheHitRateTimeBelowLowThreshold_Object = MibTableColumn
acPMStreamingCacheHitRateTimeBelowLowThreshold = _AcPMStreamingCacheHitRateTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 1, 1, 6),
    _AcPMStreamingCacheHitRateTimeBelowLowThreshold_Type()
)
acPMStreamingCacheHitRateTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheHitRateTimeBelowLowThreshold.setStatus("current")


class _AcPMStreamingCacheHitRateTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMStreamingCacheHitRateTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMStreamingCacheHitRateTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMStreamingCacheHitRateTimeBetweenThresholds_Object = MibTableColumn
acPMStreamingCacheHitRateTimeBetweenThresholds = _AcPMStreamingCacheHitRateTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 1, 1, 7),
    _AcPMStreamingCacheHitRateTimeBetweenThresholds_Type()
)
acPMStreamingCacheHitRateTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheHitRateTimeBetweenThresholds.setStatus("current")


class _AcPMStreamingCacheHitRateTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMStreamingCacheHitRateTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMStreamingCacheHitRateTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMStreamingCacheHitRateTimeAboveHighThreshold_Object = MibTableColumn
acPMStreamingCacheHitRateTimeAboveHighThreshold = _AcPMStreamingCacheHitRateTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 1, 1, 8),
    _AcPMStreamingCacheHitRateTimeAboveHighThreshold_Type()
)
acPMStreamingCacheHitRateTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheHitRateTimeAboveHighThreshold.setStatus("current")


class _AcPMStreamingCacheHitRateFullDayAverage_Type(Integer32):
    """Custom type acPMStreamingCacheHitRateFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheHitRateFullDayAverage_Type.__name__ = "Integer32"
_AcPMStreamingCacheHitRateFullDayAverage_Object = MibTableColumn
acPMStreamingCacheHitRateFullDayAverage = _AcPMStreamingCacheHitRateFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 1, 1, 9),
    _AcPMStreamingCacheHitRateFullDayAverage_Type()
)
acPMStreamingCacheHitRateFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheHitRateFullDayAverage.setStatus("current")
_AcPMStreamingCacheMissRateTable_Object = MibTable
acPMStreamingCacheMissRateTable = _AcPMStreamingCacheMissRateTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 2)
)
if mibBuilder.loadTexts:
    acPMStreamingCacheMissRateTable.setStatus("current")
_AcPMStreamingCacheMissRateEntry_Object = MibTableRow
acPMStreamingCacheMissRateEntry = _AcPMStreamingCacheMissRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 2, 1)
)
acPMStreamingCacheMissRateEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMStreamingCacheMissRateInterval"),
)
if mibBuilder.loadTexts:
    acPMStreamingCacheMissRateEntry.setStatus("current")


class _AcPMStreamingCacheMissRateInterval_Type(Unsigned32):
    """Custom type acPMStreamingCacheMissRateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMStreamingCacheMissRateInterval_Type.__name__ = "Unsigned32"
_AcPMStreamingCacheMissRateInterval_Object = MibTableColumn
acPMStreamingCacheMissRateInterval = _AcPMStreamingCacheMissRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 2, 1, 1),
    _AcPMStreamingCacheMissRateInterval_Type()
)
acPMStreamingCacheMissRateInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMStreamingCacheMissRateInterval.setStatus("current")


class _AcPMStreamingCacheMissRateAverage_Type(Integer32):
    """Custom type acPMStreamingCacheMissRateAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheMissRateAverage_Type.__name__ = "Integer32"
_AcPMStreamingCacheMissRateAverage_Object = MibTableColumn
acPMStreamingCacheMissRateAverage = _AcPMStreamingCacheMissRateAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 2, 1, 2),
    _AcPMStreamingCacheMissRateAverage_Type()
)
acPMStreamingCacheMissRateAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheMissRateAverage.setStatus("current")


class _AcPMStreamingCacheMissRateMax_Type(Integer32):
    """Custom type acPMStreamingCacheMissRateMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheMissRateMax_Type.__name__ = "Integer32"
_AcPMStreamingCacheMissRateMax_Object = MibTableColumn
acPMStreamingCacheMissRateMax = _AcPMStreamingCacheMissRateMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 2, 1, 3),
    _AcPMStreamingCacheMissRateMax_Type()
)
acPMStreamingCacheMissRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheMissRateMax.setStatus("current")


class _AcPMStreamingCacheMissRateMin_Type(Integer32):
    """Custom type acPMStreamingCacheMissRateMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheMissRateMin_Type.__name__ = "Integer32"
_AcPMStreamingCacheMissRateMin_Object = MibTableColumn
acPMStreamingCacheMissRateMin = _AcPMStreamingCacheMissRateMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 2, 1, 4),
    _AcPMStreamingCacheMissRateMin_Type()
)
acPMStreamingCacheMissRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheMissRateMin.setStatus("current")
_AcPMStreamingCacheMissRateVolume_Type = Counter32
_AcPMStreamingCacheMissRateVolume_Object = MibTableColumn
acPMStreamingCacheMissRateVolume = _AcPMStreamingCacheMissRateVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 2, 1, 5),
    _AcPMStreamingCacheMissRateVolume_Type()
)
acPMStreamingCacheMissRateVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheMissRateVolume.setStatus("current")


class _AcPMStreamingCacheMissRateTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMStreamingCacheMissRateTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMStreamingCacheMissRateTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMStreamingCacheMissRateTimeBelowLowThreshold_Object = MibTableColumn
acPMStreamingCacheMissRateTimeBelowLowThreshold = _AcPMStreamingCacheMissRateTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 2, 1, 6),
    _AcPMStreamingCacheMissRateTimeBelowLowThreshold_Type()
)
acPMStreamingCacheMissRateTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheMissRateTimeBelowLowThreshold.setStatus("current")


class _AcPMStreamingCacheMissRateTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMStreamingCacheMissRateTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMStreamingCacheMissRateTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMStreamingCacheMissRateTimeBetweenThresholds_Object = MibTableColumn
acPMStreamingCacheMissRateTimeBetweenThresholds = _AcPMStreamingCacheMissRateTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 2, 1, 7),
    _AcPMStreamingCacheMissRateTimeBetweenThresholds_Type()
)
acPMStreamingCacheMissRateTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheMissRateTimeBetweenThresholds.setStatus("current")


class _AcPMStreamingCacheMissRateTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMStreamingCacheMissRateTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMStreamingCacheMissRateTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMStreamingCacheMissRateTimeAboveHighThreshold_Object = MibTableColumn
acPMStreamingCacheMissRateTimeAboveHighThreshold = _AcPMStreamingCacheMissRateTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 2, 1, 8),
    _AcPMStreamingCacheMissRateTimeAboveHighThreshold_Type()
)
acPMStreamingCacheMissRateTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheMissRateTimeAboveHighThreshold.setStatus("current")


class _AcPMStreamingCacheMissRateFullDayAverage_Type(Integer32):
    """Custom type acPMStreamingCacheMissRateFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheMissRateFullDayAverage_Type.__name__ = "Integer32"
_AcPMStreamingCacheMissRateFullDayAverage_Object = MibTableColumn
acPMStreamingCacheMissRateFullDayAverage = _AcPMStreamingCacheMissRateFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 2, 1, 9),
    _AcPMStreamingCacheMissRateFullDayAverage_Type()
)
acPMStreamingCacheMissRateFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheMissRateFullDayAverage.setStatus("current")
_AcPMStreamingCacheServerRequestsRateTable_Object = MibTable
acPMStreamingCacheServerRequestsRateTable = _AcPMStreamingCacheServerRequestsRateTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 3)
)
if mibBuilder.loadTexts:
    acPMStreamingCacheServerRequestsRateTable.setStatus("current")
_AcPMStreamingCacheServerRequestsRateEntry_Object = MibTableRow
acPMStreamingCacheServerRequestsRateEntry = _AcPMStreamingCacheServerRequestsRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 3, 1)
)
acPMStreamingCacheServerRequestsRateEntry.setIndexNames(
    (0, "AC-PM-Media-MIB", "acPMStreamingCacheServerRequestsRateInterval"),
)
if mibBuilder.loadTexts:
    acPMStreamingCacheServerRequestsRateEntry.setStatus("current")


class _AcPMStreamingCacheServerRequestsRateInterval_Type(Unsigned32):
    """Custom type acPMStreamingCacheServerRequestsRateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMStreamingCacheServerRequestsRateInterval_Type.__name__ = "Unsigned32"
_AcPMStreamingCacheServerRequestsRateInterval_Object = MibTableColumn
acPMStreamingCacheServerRequestsRateInterval = _AcPMStreamingCacheServerRequestsRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 3, 1, 1),
    _AcPMStreamingCacheServerRequestsRateInterval_Type()
)
acPMStreamingCacheServerRequestsRateInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMStreamingCacheServerRequestsRateInterval.setStatus("current")


class _AcPMStreamingCacheServerRequestsRateAverage_Type(Integer32):
    """Custom type acPMStreamingCacheServerRequestsRateAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheServerRequestsRateAverage_Type.__name__ = "Integer32"
_AcPMStreamingCacheServerRequestsRateAverage_Object = MibTableColumn
acPMStreamingCacheServerRequestsRateAverage = _AcPMStreamingCacheServerRequestsRateAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 3, 1, 2),
    _AcPMStreamingCacheServerRequestsRateAverage_Type()
)
acPMStreamingCacheServerRequestsRateAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheServerRequestsRateAverage.setStatus("current")


class _AcPMStreamingCacheServerRequestsRateMax_Type(Integer32):
    """Custom type acPMStreamingCacheServerRequestsRateMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheServerRequestsRateMax_Type.__name__ = "Integer32"
_AcPMStreamingCacheServerRequestsRateMax_Object = MibTableColumn
acPMStreamingCacheServerRequestsRateMax = _AcPMStreamingCacheServerRequestsRateMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 3, 1, 3),
    _AcPMStreamingCacheServerRequestsRateMax_Type()
)
acPMStreamingCacheServerRequestsRateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheServerRequestsRateMax.setStatus("current")


class _AcPMStreamingCacheServerRequestsRateMin_Type(Integer32):
    """Custom type acPMStreamingCacheServerRequestsRateMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheServerRequestsRateMin_Type.__name__ = "Integer32"
_AcPMStreamingCacheServerRequestsRateMin_Object = MibTableColumn
acPMStreamingCacheServerRequestsRateMin = _AcPMStreamingCacheServerRequestsRateMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 3, 1, 4),
    _AcPMStreamingCacheServerRequestsRateMin_Type()
)
acPMStreamingCacheServerRequestsRateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheServerRequestsRateMin.setStatus("current")
_AcPMStreamingCacheServerRequestsRateVolume_Type = Counter32
_AcPMStreamingCacheServerRequestsRateVolume_Object = MibTableColumn
acPMStreamingCacheServerRequestsRateVolume = _AcPMStreamingCacheServerRequestsRateVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 3, 1, 5),
    _AcPMStreamingCacheServerRequestsRateVolume_Type()
)
acPMStreamingCacheServerRequestsRateVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheServerRequestsRateVolume.setStatus("current")


class _AcPMStreamingCacheServerRequestsRateTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMStreamingCacheServerRequestsRateTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMStreamingCacheServerRequestsRateTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMStreamingCacheServerRequestsRateTimeBelowLowThreshold_Object = MibTableColumn
acPMStreamingCacheServerRequestsRateTimeBelowLowThreshold = _AcPMStreamingCacheServerRequestsRateTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 3, 1, 6),
    _AcPMStreamingCacheServerRequestsRateTimeBelowLowThreshold_Type()
)
acPMStreamingCacheServerRequestsRateTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheServerRequestsRateTimeBelowLowThreshold.setStatus("current")


class _AcPMStreamingCacheServerRequestsRateTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMStreamingCacheServerRequestsRateTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMStreamingCacheServerRequestsRateTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMStreamingCacheServerRequestsRateTimeBetweenThresholds_Object = MibTableColumn
acPMStreamingCacheServerRequestsRateTimeBetweenThresholds = _AcPMStreamingCacheServerRequestsRateTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 3, 1, 7),
    _AcPMStreamingCacheServerRequestsRateTimeBetweenThresholds_Type()
)
acPMStreamingCacheServerRequestsRateTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheServerRequestsRateTimeBetweenThresholds.setStatus("current")


class _AcPMStreamingCacheServerRequestsRateTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMStreamingCacheServerRequestsRateTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMStreamingCacheServerRequestsRateTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMStreamingCacheServerRequestsRateTimeAboveHighThreshold_Object = MibTableColumn
acPMStreamingCacheServerRequestsRateTimeAboveHighThreshold = _AcPMStreamingCacheServerRequestsRateTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 3, 1, 8),
    _AcPMStreamingCacheServerRequestsRateTimeAboveHighThreshold_Type()
)
acPMStreamingCacheServerRequestsRateTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheServerRequestsRateTimeAboveHighThreshold.setStatus("current")


class _AcPMStreamingCacheServerRequestsRateFullDayAverage_Type(Integer32):
    """Custom type acPMStreamingCacheServerRequestsRateFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMStreamingCacheServerRequestsRateFullDayAverage_Type.__name__ = "Integer32"
_AcPMStreamingCacheServerRequestsRateFullDayAverage_Object = MibTableColumn
acPMStreamingCacheServerRequestsRateFullDayAverage = _AcPMStreamingCacheServerRequestsRateFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 7, 2, 42, 3, 1, 9),
    _AcPMStreamingCacheServerRequestsRateFullDayAverage_Type()
)
acPMStreamingCacheServerRequestsRateFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStreamingCacheServerRequestsRateFullDayAverage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-PM-Media-MIB",
    **{"acPMMedia": acPMMedia,
       "acPMMediaConfiguration": acPMMediaConfiguration,
       "acPMMediaConfigurationPeriodLength": acPMMediaConfigurationPeriodLength,
       "acPMMediaConfigurationResetTotalCounters": acPMMediaConfigurationResetTotalCounters,
       "acPMDSPAttributes": acPMDSPAttributes,
       "acPMDSPAttributesDSPUtilHighThreshold": acPMDSPAttributesDSPUtilHighThreshold,
       "acPMDSPAttributesDSPUtilLowThreshold": acPMDSPAttributesDSPUtilLowThreshold,
       "acPMCodersAttributes": acPMCodersAttributes,
       "acPMCodersAttributesChannelsPerCoderHighThreshold": acPMCodersAttributesChannelsPerCoderHighThreshold,
       "acPMCodersAttributesChannelsPerCoderLowThreshold": acPMCodersAttributesChannelsPerCoderLowThreshold,
       "acPMNetworkingAttributes": acPMNetworkingAttributes,
       "acPMNetworkingAttributesPacketDelayHighThreshold": acPMNetworkingAttributesPacketDelayHighThreshold,
       "acPMNetworkingAttributesPacketDelayLowThreshold": acPMNetworkingAttributesPacketDelayLowThreshold,
       "acPMNetworkingAttributesPacketJitterHighThreshold": acPMNetworkingAttributesPacketJitterHighThreshold,
       "acPMNetworkingAttributesPacketJitterLowThreshold": acPMNetworkingAttributesPacketJitterLowThreshold,
       "acPMNetworkingAttributesRTPBytesTxHighThreshold": acPMNetworkingAttributesRTPBytesTxHighThreshold,
       "acPMNetworkingAttributesRTPBytesTxLowThreshold": acPMNetworkingAttributesRTPBytesTxLowThreshold,
       "acPMNetworkingAttributesRTPBytesRxHighThreshold": acPMNetworkingAttributesRTPBytesRxHighThreshold,
       "acPMNetworkingAttributesRTPBytesRxLowThreshold": acPMNetworkingAttributesRTPBytesRxLowThreshold,
       "acPMNetworkingAttributesRTPPacketsTxHighThreshold": acPMNetworkingAttributesRTPPacketsTxHighThreshold,
       "acPMNetworkingAttributesRTPPacketsTxLowThreshold": acPMNetworkingAttributesRTPPacketsTxLowThreshold,
       "acPMNetworkingAttributesRTPPacketsRxHighThreshold": acPMNetworkingAttributesRTPPacketsRxHighThreshold,
       "acPMNetworkingAttributesRTPPacketsRxLowThreshold": acPMNetworkingAttributesRTPPacketsRxLowThreshold,
       "acPMNetworkingAttributesRTPPacketLossRxHighThreshold": acPMNetworkingAttributesRTPPacketLossRxHighThreshold,
       "acPMNetworkingAttributesRTPPacketLossRxLowThreshold": acPMNetworkingAttributesRTPPacketLossRxLowThreshold,
       "acPMNetworkingAttributesRTPPacketLossTxHighThreshold": acPMNetworkingAttributesRTPPacketLossTxHighThreshold,
       "acPMNetworkingAttributesRTPPacketLossTxLowThreshold": acPMNetworkingAttributesRTPPacketLossTxLowThreshold,
       "acPMNetworkingAttributesModuleRTPPacketLossRxHighThreshold": acPMNetworkingAttributesModuleRTPPacketLossRxHighThreshold,
       "acPMNetworkingAttributesModuleRTPPacketLossRxLowThreshold": acPMNetworkingAttributesModuleRTPPacketLossRxLowThreshold,
       "acPMNetworkingAttributesModuleRTPPacketLossTxHighThreshold": acPMNetworkingAttributesModuleRTPPacketLossTxHighThreshold,
       "acPMNetworkingAttributesModuleRTPPacketLossTxLowThreshold": acPMNetworkingAttributesModuleRTPPacketLossTxLowThreshold,
       "acPMMediaNetworkingAggregatedAttributes": acPMMediaNetworkingAggregatedAttributes,
       "acPMMediaNetworkingAggregatedAttributesPacketDelayHighThreshold": acPMMediaNetworkingAggregatedAttributesPacketDelayHighThreshold,
       "acPMMediaNetworkingAggregatedAttributesPacketDelayLowThreshold": acPMMediaNetworkingAggregatedAttributesPacketDelayLowThreshold,
       "acPMMediaNetworkingAggregatedAttributesPacketJitterHighThreshold": acPMMediaNetworkingAggregatedAttributesPacketJitterHighThreshold,
       "acPMMediaNetworkingAggregatedAttributesPacketJitterLowThreshold": acPMMediaNetworkingAggregatedAttributesPacketJitterLowThreshold,
       "acPMMediaNetworkingAggregatedAttributesRTPBytesTxHighThreshold": acPMMediaNetworkingAggregatedAttributesRTPBytesTxHighThreshold,
       "acPMMediaNetworkingAggregatedAttributesRTPBytesTxLowThreshold": acPMMediaNetworkingAggregatedAttributesRTPBytesTxLowThreshold,
       "acPMMediaNetworkingAggregatedAttributesRTPBytesRxHighThreshold": acPMMediaNetworkingAggregatedAttributesRTPBytesRxHighThreshold,
       "acPMMediaNetworkingAggregatedAttributesRTPBytesRxLowThreshold": acPMMediaNetworkingAggregatedAttributesRTPBytesRxLowThreshold,
       "acPMMediaNetworkingAggregatedAttributesRTPPacketsTxHighThreshold": acPMMediaNetworkingAggregatedAttributesRTPPacketsTxHighThreshold,
       "acPMMediaNetworkingAggregatedAttributesRTPPacketsTxLowThreshold": acPMMediaNetworkingAggregatedAttributesRTPPacketsTxLowThreshold,
       "acPMMediaNetworkingAggregatedAttributesRTPPacketsRxHighThreshold": acPMMediaNetworkingAggregatedAttributesRTPPacketsRxHighThreshold,
       "acPMMediaNetworkingAggregatedAttributesRTPPacketsRxLowThreshold": acPMMediaNetworkingAggregatedAttributesRTPPacketsRxLowThreshold,
       "acPMMediaChannelUtilizationAttr": acPMMediaChannelUtilizationAttr,
       "acPMMediaChannelUtilizationAttrFaxChannelsHighThreshold": acPMMediaChannelUtilizationAttrFaxChannelsHighThreshold,
       "acPMMediaChannelUtilizationAttrFaxChannelsLowThreshold": acPMMediaChannelUtilizationAttrFaxChannelsLowThreshold,
       "acPMMediaChannelUtilizationAttrModemChannelsHighThreshold": acPMMediaChannelUtilizationAttrModemChannelsHighThreshold,
       "acPMMediaChannelUtilizationAttrModemChannelsLowThreshold": acPMMediaChannelUtilizationAttrModemChannelsLowThreshold,
       "acPMMediaChannelUtilizationAttrTDM2IPChannelsHighThreshold": acPMMediaChannelUtilizationAttrTDM2IPChannelsHighThreshold,
       "acPMMediaChannelUtilizationAttrTDM2IPChannelsLowThreshold": acPMMediaChannelUtilizationAttrTDM2IPChannelsLowThreshold,
       "acPMMediaChannelUtilizationAttrRTPStreamsHighThreshold": acPMMediaChannelUtilizationAttrRTPStreamsHighThreshold,
       "acPMMediaChannelUtilizationAttrRTPStreamsLowThreshold": acPMMediaChannelUtilizationAttrRTPStreamsLowThreshold,
       "acPMMediaChannelUtilizationAttrSRTPStreamsHighThreshold": acPMMediaChannelUtilizationAttrSRTPStreamsHighThreshold,
       "acPMMediaChannelUtilizationAttrSRTPStreamsLowThreshold": acPMMediaChannelUtilizationAttrSRTPStreamsLowThreshold,
       "acPMMediaChannelUtilizationAttrMulticastRegisChanHighThreshold": acPMMediaChannelUtilizationAttrMulticastRegisChanHighThreshold,
       "acPMMediaChannelUtilizationAttrMulticastRegisChanLowThreshold": acPMMediaChannelUtilizationAttrMulticastRegisChanLowThreshold,
       "acPMMediaChannelUtilizationAttrModemRelayHighThreshold": acPMMediaChannelUtilizationAttrModemRelayHighThreshold,
       "acPMMediaChannelUtilizationAttrModemRelayLowThreshold": acPMMediaChannelUtilizationAttrModemRelayLowThreshold,
       "acPMMediaData": acPMMediaData,
       "acPMMediaDataAcPMMediaTimeFromStartOfInterval": acPMMediaDataAcPMMediaTimeFromStartOfInterval,
       "acPMDSPUtilTable": acPMDSPUtilTable,
       "acPMDSPUtilEntry": acPMDSPUtilEntry,
       "acPMDSPUtilInterval": acPMDSPUtilInterval,
       "acPMDSPUtilVal": acPMDSPUtilVal,
       "acPMDSPUtilAverage": acPMDSPUtilAverage,
       "acPMDSPUtilMax": acPMDSPUtilMax,
       "acPMDSPUtilMin": acPMDSPUtilMin,
       "acPMDSPUtilVolume": acPMDSPUtilVolume,
       "acPMDSPUtilTimeBelowLowThreshold": acPMDSPUtilTimeBelowLowThreshold,
       "acPMDSPUtilTimeBetweenThresholds": acPMDSPUtilTimeBetweenThresholds,
       "acPMDSPUtilTimeAboveHighThreshold": acPMDSPUtilTimeAboveHighThreshold,
       "acPMDSPUtilFullDayAverage": acPMDSPUtilFullDayAverage,
       "acPMChannelsPerCoderTable": acPMChannelsPerCoderTable,
       "acPMChannelsPerCoderEntry": acPMChannelsPerCoderEntry,
       "acPMChannelsPerCoderCoders": acPMChannelsPerCoderCoders,
       "acPMChannelsPerCoderInterval": acPMChannelsPerCoderInterval,
       "acPMChannelsPerCoderVal": acPMChannelsPerCoderVal,
       "acPMChannelsPerCoderAverage": acPMChannelsPerCoderAverage,
       "acPMChannelsPerCoderMax": acPMChannelsPerCoderMax,
       "acPMChannelsPerCoderMin": acPMChannelsPerCoderMin,
       "acPMChannelsPerCoderVolume": acPMChannelsPerCoderVolume,
       "acPMChannelsPerCoderTimeBelowLowThreshold": acPMChannelsPerCoderTimeBelowLowThreshold,
       "acPMChannelsPerCoderTimeBetweenThresholds": acPMChannelsPerCoderTimeBetweenThresholds,
       "acPMChannelsPerCoderTimeAboveHighThreshold": acPMChannelsPerCoderTimeAboveHighThreshold,
       "acPMChannelsPerCoderFullDayAverage": acPMChannelsPerCoderFullDayAverage,
       "acPMRobustDiscardTable": acPMRobustDiscardTable,
       "acPMRobustDiscardEntry": acPMRobustDiscardEntry,
       "acPMRobustDiscardInterval": acPMRobustDiscardInterval,
       "acPMRobustDiscardVal": acPMRobustDiscardVal,
       "acPMMediaNetworking": acPMMediaNetworking,
       "acPMPacketDelayTable": acPMPacketDelayTable,
       "acPMPacketDelayEntry": acPMPacketDelayEntry,
       "acPMPacketDelayTrunkNum": acPMPacketDelayTrunkNum,
       "acPMPacketDelayInterval": acPMPacketDelayInterval,
       "acPMPacketDelayVal": acPMPacketDelayVal,
       "acPMPacketDelayAverage": acPMPacketDelayAverage,
       "acPMPacketDelayMax": acPMPacketDelayMax,
       "acPMPacketDelayMin": acPMPacketDelayMin,
       "acPMPacketDelayVolume": acPMPacketDelayVolume,
       "acPMPacketDelayTimeBelowLowThreshold": acPMPacketDelayTimeBelowLowThreshold,
       "acPMPacketDelayTimeBetweenThresholds": acPMPacketDelayTimeBetweenThresholds,
       "acPMPacketDelayTimeAboveHighThreshold": acPMPacketDelayTimeAboveHighThreshold,
       "acPMPacketDelayFullDayAverage": acPMPacketDelayFullDayAverage,
       "acPMPacketJitterTable": acPMPacketJitterTable,
       "acPMPacketJitterEntry": acPMPacketJitterEntry,
       "acPMPacketJitterTrunkNum": acPMPacketJitterTrunkNum,
       "acPMPacketJitterInterval": acPMPacketJitterInterval,
       "acPMPacketJitterVal": acPMPacketJitterVal,
       "acPMPacketJitterAverage": acPMPacketJitterAverage,
       "acPMPacketJitterMax": acPMPacketJitterMax,
       "acPMPacketJitterMin": acPMPacketJitterMin,
       "acPMPacketJitterVolume": acPMPacketJitterVolume,
       "acPMPacketJitterTimeBelowLowThreshold": acPMPacketJitterTimeBelowLowThreshold,
       "acPMPacketJitterTimeBetweenThresholds": acPMPacketJitterTimeBetweenThresholds,
       "acPMPacketJitterTimeAboveHighThreshold": acPMPacketJitterTimeAboveHighThreshold,
       "acPMPacketJitterFullDayAverage": acPMPacketJitterFullDayAverage,
       "acPMRTPBytesTxTable": acPMRTPBytesTxTable,
       "acPMRTPBytesTxEntry": acPMRTPBytesTxEntry,
       "acPMRTPBytesTxTrunkNum": acPMRTPBytesTxTrunkNum,
       "acPMRTPBytesTxInterval": acPMRTPBytesTxInterval,
       "acPMRTPBytesTxVal": acPMRTPBytesTxVal,
       "acPMRTPBytesTxAverage": acPMRTPBytesTxAverage,
       "acPMRTPBytesTxMax": acPMRTPBytesTxMax,
       "acPMRTPBytesTxMin": acPMRTPBytesTxMin,
       "acPMRTPBytesTxVolume": acPMRTPBytesTxVolume,
       "acPMRTPBytesTxTimeBelowLowThreshold": acPMRTPBytesTxTimeBelowLowThreshold,
       "acPMRTPBytesTxTimeBetweenThresholds": acPMRTPBytesTxTimeBetweenThresholds,
       "acPMRTPBytesTxTimeAboveHighThreshold": acPMRTPBytesTxTimeAboveHighThreshold,
       "acPMRTPBytesTxFullDayAverage": acPMRTPBytesTxFullDayAverage,
       "acPMRTPBytesRxTable": acPMRTPBytesRxTable,
       "acPMRTPBytesRxEntry": acPMRTPBytesRxEntry,
       "acPMRTPBytesRxTrunkNum": acPMRTPBytesRxTrunkNum,
       "acPMRTPBytesRxInterval": acPMRTPBytesRxInterval,
       "acPMRTPBytesRxVal": acPMRTPBytesRxVal,
       "acPMRTPBytesRxAverage": acPMRTPBytesRxAverage,
       "acPMRTPBytesRxMax": acPMRTPBytesRxMax,
       "acPMRTPBytesRxMin": acPMRTPBytesRxMin,
       "acPMRTPBytesRxVolume": acPMRTPBytesRxVolume,
       "acPMRTPBytesRxTimeBelowLowThreshold": acPMRTPBytesRxTimeBelowLowThreshold,
       "acPMRTPBytesRxTimeBetweenThresholds": acPMRTPBytesRxTimeBetweenThresholds,
       "acPMRTPBytesRxTimeAboveHighThreshold": acPMRTPBytesRxTimeAboveHighThreshold,
       "acPMRTPBytesRxFullDayAverage": acPMRTPBytesRxFullDayAverage,
       "acPMRTPPacketsTxTable": acPMRTPPacketsTxTable,
       "acPMRTPPacketsTxEntry": acPMRTPPacketsTxEntry,
       "acPMRTPPacketsTxTrunkNum": acPMRTPPacketsTxTrunkNum,
       "acPMRTPPacketsTxInterval": acPMRTPPacketsTxInterval,
       "acPMRTPPacketsTxVal": acPMRTPPacketsTxVal,
       "acPMRTPPacketsTxAverage": acPMRTPPacketsTxAverage,
       "acPMRTPPacketsTxMax": acPMRTPPacketsTxMax,
       "acPMRTPPacketsTxMin": acPMRTPPacketsTxMin,
       "acPMRTPPacketsTxVolume": acPMRTPPacketsTxVolume,
       "acPMRTPPacketsTxTimeBelowLowThreshold": acPMRTPPacketsTxTimeBelowLowThreshold,
       "acPMRTPPacketsTxTimeBetweenThresholds": acPMRTPPacketsTxTimeBetweenThresholds,
       "acPMRTPPacketsTxTimeAboveHighThreshold": acPMRTPPacketsTxTimeAboveHighThreshold,
       "acPMRTPPacketsTxFullDayAverage": acPMRTPPacketsTxFullDayAverage,
       "acPMRTPPacketsTxTotal": acPMRTPPacketsTxTotal,
       "acPMRTPPacketsRxTable": acPMRTPPacketsRxTable,
       "acPMRTPPacketsRxEntry": acPMRTPPacketsRxEntry,
       "acPMRTPPacketsRxTrunkNum": acPMRTPPacketsRxTrunkNum,
       "acPMRTPPacketsRxInterval": acPMRTPPacketsRxInterval,
       "acPMRTPPacketsRxVal": acPMRTPPacketsRxVal,
       "acPMRTPPacketsRxAverage": acPMRTPPacketsRxAverage,
       "acPMRTPPacketsRxMax": acPMRTPPacketsRxMax,
       "acPMRTPPacketsRxMin": acPMRTPPacketsRxMin,
       "acPMRTPPacketsRxVolume": acPMRTPPacketsRxVolume,
       "acPMRTPPacketsRxTimeBelowLowThreshold": acPMRTPPacketsRxTimeBelowLowThreshold,
       "acPMRTPPacketsRxTimeBetweenThresholds": acPMRTPPacketsRxTimeBetweenThresholds,
       "acPMRTPPacketsRxTimeAboveHighThreshold": acPMRTPPacketsRxTimeAboveHighThreshold,
       "acPMRTPPacketsRxFullDayAverage": acPMRTPPacketsRxFullDayAverage,
       "acPMRTPPacketsRxTotal": acPMRTPPacketsRxTotal,
       "acPMRTPPacketLossRxTable": acPMRTPPacketLossRxTable,
       "acPMRTPPacketLossRxEntry": acPMRTPPacketLossRxEntry,
       "acPMRTPPacketLossRxTrunkNum": acPMRTPPacketLossRxTrunkNum,
       "acPMRTPPacketLossRxInterval": acPMRTPPacketLossRxInterval,
       "acPMRTPPacketLossRxVal": acPMRTPPacketLossRxVal,
       "acPMRTPPacketLossRxAverage": acPMRTPPacketLossRxAverage,
       "acPMRTPPacketLossRxMax": acPMRTPPacketLossRxMax,
       "acPMRTPPacketLossRxMin": acPMRTPPacketLossRxMin,
       "acPMRTPPacketLossRxVolume": acPMRTPPacketLossRxVolume,
       "acPMRTPPacketLossRxTimeBelowLowThreshold": acPMRTPPacketLossRxTimeBelowLowThreshold,
       "acPMRTPPacketLossRxTimeBetweenThresholds": acPMRTPPacketLossRxTimeBetweenThresholds,
       "acPMRTPPacketLossRxTimeAboveHighThreshold": acPMRTPPacketLossRxTimeAboveHighThreshold,
       "acPMRTPPacketLossRxFullDayAverage": acPMRTPPacketLossRxFullDayAverage,
       "acPMRTPPacketLossTxTable": acPMRTPPacketLossTxTable,
       "acPMRTPPacketLossTxEntry": acPMRTPPacketLossTxEntry,
       "acPMRTPPacketLossTxTrunkNum": acPMRTPPacketLossTxTrunkNum,
       "acPMRTPPacketLossTxInterval": acPMRTPPacketLossTxInterval,
       "acPMRTPPacketLossTxVal": acPMRTPPacketLossTxVal,
       "acPMRTPPacketLossTxAverage": acPMRTPPacketLossTxAverage,
       "acPMRTPPacketLossTxMax": acPMRTPPacketLossTxMax,
       "acPMRTPPacketLossTxMin": acPMRTPPacketLossTxMin,
       "acPMRTPPacketLossTxVolume": acPMRTPPacketLossTxVolume,
       "acPMRTPPacketLossTxTimeBelowLowThreshold": acPMRTPPacketLossTxTimeBelowLowThreshold,
       "acPMRTPPacketLossTxTimeBetweenThresholds": acPMRTPPacketLossTxTimeBetweenThresholds,
       "acPMRTPPacketLossTxTimeAboveHighThreshold": acPMRTPPacketLossTxTimeAboveHighThreshold,
       "acPMRTPPacketLossTxFullDayAverage": acPMRTPPacketLossTxFullDayAverage,
       "acPMModuleRTPPacketLossRxTable": acPMModuleRTPPacketLossRxTable,
       "acPMModuleRTPPacketLossRxEntry": acPMModuleRTPPacketLossRxEntry,
       "acPMModuleRTPPacketLossRxInterval": acPMModuleRTPPacketLossRxInterval,
       "acPMModuleRTPPacketLossRxAverage": acPMModuleRTPPacketLossRxAverage,
       "acPMModuleRTPPacketLossRxMax": acPMModuleRTPPacketLossRxMax,
       "acPMModuleRTPPacketLossRxMin": acPMModuleRTPPacketLossRxMin,
       "acPMModuleRTPPacketLossRxVolume": acPMModuleRTPPacketLossRxVolume,
       "acPMModuleRTPPacketLossRxTimeBelowLowThreshold": acPMModuleRTPPacketLossRxTimeBelowLowThreshold,
       "acPMModuleRTPPacketLossRxTimeBetweenThresholds": acPMModuleRTPPacketLossRxTimeBetweenThresholds,
       "acPMModuleRTPPacketLossRxTimeAboveHighThreshold": acPMModuleRTPPacketLossRxTimeAboveHighThreshold,
       "acPMModuleRTPPacketLossRxFullDayAverage": acPMModuleRTPPacketLossRxFullDayAverage,
       "acPMModuleRTPPacketLossRxTotal": acPMModuleRTPPacketLossRxTotal,
       "acPMModuleRTPPacketLossTxTable": acPMModuleRTPPacketLossTxTable,
       "acPMModuleRTPPacketLossTxEntry": acPMModuleRTPPacketLossTxEntry,
       "acPMModuleRTPPacketLossTxInterval": acPMModuleRTPPacketLossTxInterval,
       "acPMModuleRTPPacketLossTxAverage": acPMModuleRTPPacketLossTxAverage,
       "acPMModuleRTPPacketLossTxMax": acPMModuleRTPPacketLossTxMax,
       "acPMModuleRTPPacketLossTxMin": acPMModuleRTPPacketLossTxMin,
       "acPMModuleRTPPacketLossTxVolume": acPMModuleRTPPacketLossTxVolume,
       "acPMModuleRTPPacketLossTxTimeBelowLowThreshold": acPMModuleRTPPacketLossTxTimeBelowLowThreshold,
       "acPMModuleRTPPacketLossTxTimeBetweenThresholds": acPMModuleRTPPacketLossTxTimeBetweenThresholds,
       "acPMModuleRTPPacketLossTxTimeAboveHighThreshold": acPMModuleRTPPacketLossTxTimeAboveHighThreshold,
       "acPMModuleRTPPacketLossTxFullDayAverage": acPMModuleRTPPacketLossTxFullDayAverage,
       "acPMModuleRTPPacketLossTxTotal": acPMModuleRTPPacketLossTxTotal,
       "acPMMediaNetworkingAggregated": acPMMediaNetworkingAggregated,
       "acPMModulePacketDelayTable": acPMModulePacketDelayTable,
       "acPMModulePacketDelayEntry": acPMModulePacketDelayEntry,
       "acPMModulePacketDelayInterval": acPMModulePacketDelayInterval,
       "acPMModulePacketDelayVal": acPMModulePacketDelayVal,
       "acPMModulePacketDelayAverage": acPMModulePacketDelayAverage,
       "acPMModulePacketDelayMax": acPMModulePacketDelayMax,
       "acPMModulePacketDelayMin": acPMModulePacketDelayMin,
       "acPMModulePacketDelayTimeBelowLowThreshold": acPMModulePacketDelayTimeBelowLowThreshold,
       "acPMModulePacketDelayTimeBetweenThresholds": acPMModulePacketDelayTimeBetweenThresholds,
       "acPMModulePacketDelayTimeAboveHighThreshold": acPMModulePacketDelayTimeAboveHighThreshold,
       "acPMModulePacketDelayFullDayAverage": acPMModulePacketDelayFullDayAverage,
       "acPMModulePacketDelayVolume": acPMModulePacketDelayVolume,
       "acPMModulePacketJitterTable": acPMModulePacketJitterTable,
       "acPMModulePacketJitterEntry": acPMModulePacketJitterEntry,
       "acPMModulePacketJitterInterval": acPMModulePacketJitterInterval,
       "acPMModulePacketJitterVal": acPMModulePacketJitterVal,
       "acPMModulePacketJitterAverage": acPMModulePacketJitterAverage,
       "acPMModulePacketJitterMax": acPMModulePacketJitterMax,
       "acPMModulePacketJitterMin": acPMModulePacketJitterMin,
       "acPMModulePacketJitterTimeBelowLowThreshold": acPMModulePacketJitterTimeBelowLowThreshold,
       "acPMModulePacketJitterTimeBetweenThresholds": acPMModulePacketJitterTimeBetweenThresholds,
       "acPMModulePacketJitterTimeAboveHighThreshold": acPMModulePacketJitterTimeAboveHighThreshold,
       "acPMModulePacketJitterFullDayAverage": acPMModulePacketJitterFullDayAverage,
       "acPMModulePacketJitterVolume": acPMModulePacketJitterVolume,
       "acPMModuleRTPBytesTxTable": acPMModuleRTPBytesTxTable,
       "acPMModuleRTPBytesTxEntry": acPMModuleRTPBytesTxEntry,
       "acPMModuleRTPBytesTxInterval": acPMModuleRTPBytesTxInterval,
       "acPMModuleRTPBytesTxAverage": acPMModuleRTPBytesTxAverage,
       "acPMModuleRTPBytesTxMax": acPMModuleRTPBytesTxMax,
       "acPMModuleRTPBytesTxMin": acPMModuleRTPBytesTxMin,
       "acPMModuleRTPBytesTxTimeBelowLowThreshold": acPMModuleRTPBytesTxTimeBelowLowThreshold,
       "acPMModuleRTPBytesTxTimeBetweenThresholds": acPMModuleRTPBytesTxTimeBetweenThresholds,
       "acPMModuleRTPBytesTxTimeAboveHighThreshold": acPMModuleRTPBytesTxTimeAboveHighThreshold,
       "acPMModuleRTPBytesTxFullDayAverage": acPMModuleRTPBytesTxFullDayAverage,
       "acPMModuleRTPBytesTxVolume": acPMModuleRTPBytesTxVolume,
       "acPMModuleRTPBytesRxTable": acPMModuleRTPBytesRxTable,
       "acPMModuleRTPBytesRxEntry": acPMModuleRTPBytesRxEntry,
       "acPMModuleRTPBytesRxInterval": acPMModuleRTPBytesRxInterval,
       "acPMModuleRTPBytesRxAverage": acPMModuleRTPBytesRxAverage,
       "acPMModuleRTPBytesRxMax": acPMModuleRTPBytesRxMax,
       "acPMModuleRTPBytesRxMin": acPMModuleRTPBytesRxMin,
       "acPMModuleRTPBytesRxTimeBelowLowThreshold": acPMModuleRTPBytesRxTimeBelowLowThreshold,
       "acPMModuleRTPBytesRxTimeBetweenThresholds": acPMModuleRTPBytesRxTimeBetweenThresholds,
       "acPMModuleRTPBytesRxTimeAboveHighThreshold": acPMModuleRTPBytesRxTimeAboveHighThreshold,
       "acPMModuleRTPBytesRxFullDayAverage": acPMModuleRTPBytesRxFullDayAverage,
       "acPMModuleRTPBytesRxVolume": acPMModuleRTPBytesRxVolume,
       "acPMModuleRTPPacketsTxTable": acPMModuleRTPPacketsTxTable,
       "acPMModuleRTPPacketsTxEntry": acPMModuleRTPPacketsTxEntry,
       "acPMModuleRTPPacketsTxInterval": acPMModuleRTPPacketsTxInterval,
       "acPMModuleRTPPacketsTxAverage": acPMModuleRTPPacketsTxAverage,
       "acPMModuleRTPPacketsTxMax": acPMModuleRTPPacketsTxMax,
       "acPMModuleRTPPacketsTxMin": acPMModuleRTPPacketsTxMin,
       "acPMModuleRTPPacketsTxTimeBelowLowThreshold": acPMModuleRTPPacketsTxTimeBelowLowThreshold,
       "acPMModuleRTPPacketsTxTimeBetweenThresholds": acPMModuleRTPPacketsTxTimeBetweenThresholds,
       "acPMModuleRTPPacketsTxTimeAboveHighThreshold": acPMModuleRTPPacketsTxTimeAboveHighThreshold,
       "acPMModuleRTPPacketsTxFullDayAverage": acPMModuleRTPPacketsTxFullDayAverage,
       "acPMModuleRTPPacketsTxTotal": acPMModuleRTPPacketsTxTotal,
       "acPMModuleRTPPacketsTxVolume": acPMModuleRTPPacketsTxVolume,
       "acPMModuleRTPPacketsRxTable": acPMModuleRTPPacketsRxTable,
       "acPMModuleRTPPacketsRxEntry": acPMModuleRTPPacketsRxEntry,
       "acPMModuleRTPPacketsRxInterval": acPMModuleRTPPacketsRxInterval,
       "acPMModuleRTPPacketsRxAverage": acPMModuleRTPPacketsRxAverage,
       "acPMModuleRTPPacketsRxMax": acPMModuleRTPPacketsRxMax,
       "acPMModuleRTPPacketsRxMin": acPMModuleRTPPacketsRxMin,
       "acPMModuleRTPPacketsRxTimeBelowLowThreshold": acPMModuleRTPPacketsRxTimeBelowLowThreshold,
       "acPMModuleRTPPacketsRxTimeBetweenThresholds": acPMModuleRTPPacketsRxTimeBetweenThresholds,
       "acPMModuleRTPPacketsRxTimeAboveHighThreshold": acPMModuleRTPPacketsRxTimeAboveHighThreshold,
       "acPMModuleRTPPacketsRxFullDayAverage": acPMModuleRTPPacketsRxFullDayAverage,
       "acPMModuleRTPPacketsRxTotal": acPMModuleRTPPacketsRxTotal,
       "acPMModuleRTPPacketsRxVolume": acPMModuleRTPPacketsRxVolume,
       "acPMChannelUtilization": acPMChannelUtilization,
       "acPMFaxChannelsTable": acPMFaxChannelsTable,
       "acPMFaxChannelsEntry": acPMFaxChannelsEntry,
       "acPMFaxChannelsInterval": acPMFaxChannelsInterval,
       "acPMFaxChannelsVal": acPMFaxChannelsVal,
       "acPMFaxChannelsAverage": acPMFaxChannelsAverage,
       "acPMFaxChannelsMax": acPMFaxChannelsMax,
       "acPMFaxChannelsMin": acPMFaxChannelsMin,
       "acPMFaxChannelsTimeBelowLowThreshold": acPMFaxChannelsTimeBelowLowThreshold,
       "acPMFaxChannelsTimeBetweenThresholds": acPMFaxChannelsTimeBetweenThresholds,
       "acPMFaxChannelsTimeAboveHighThreshold": acPMFaxChannelsTimeAboveHighThreshold,
       "acPMFaxChannelsFullDayAverage": acPMFaxChannelsFullDayAverage,
       "acPMFaxChannelsVolume": acPMFaxChannelsVolume,
       "acPMModemChannelsTable": acPMModemChannelsTable,
       "acPMModemChannelsEntry": acPMModemChannelsEntry,
       "acPMModemChannelsInterval": acPMModemChannelsInterval,
       "acPMModemChannelsVal": acPMModemChannelsVal,
       "acPMModemChannelsAverage": acPMModemChannelsAverage,
       "acPMModemChannelsMax": acPMModemChannelsMax,
       "acPMModemChannelsMin": acPMModemChannelsMin,
       "acPMModemChannelsTimeBelowLowThreshold": acPMModemChannelsTimeBelowLowThreshold,
       "acPMModemChannelsTimeBetweenThresholds": acPMModemChannelsTimeBetweenThresholds,
       "acPMModemChannelsTimeAboveHighThreshold": acPMModemChannelsTimeAboveHighThreshold,
       "acPMModemChannelsFullDayAverage": acPMModemChannelsFullDayAverage,
       "acPMTdm2IpChannelsTable": acPMTdm2IpChannelsTable,
       "acPMTdm2IpChannelsEntry": acPMTdm2IpChannelsEntry,
       "acPMTdm2IpChannelsInterval": acPMTdm2IpChannelsInterval,
       "acPMTdm2IpChannelsVal": acPMTdm2IpChannelsVal,
       "acPMTdm2IpChannelsAverage": acPMTdm2IpChannelsAverage,
       "acPMTdm2IpChannelsMax": acPMTdm2IpChannelsMax,
       "acPMTdm2IpChannelsMin": acPMTdm2IpChannelsMin,
       "acPMTdm2IpChannelsVolume": acPMTdm2IpChannelsVolume,
       "acPMTdm2IpChannelsTimeBelowLowThreshold": acPMTdm2IpChannelsTimeBelowLowThreshold,
       "acPMTdm2IpChannelsTimeBetweenThresholds": acPMTdm2IpChannelsTimeBetweenThresholds,
       "acPMTdm2IpChannelsTimeAboveHighThreshold": acPMTdm2IpChannelsTimeAboveHighThreshold,
       "acPMTdm2IpChannelsFullDayAverage": acPMTdm2IpChannelsFullDayAverage,
       "acPMRTPStreamsTable": acPMRTPStreamsTable,
       "acPMRTPStreamsEntry": acPMRTPStreamsEntry,
       "acPMRTPStreamsInterval": acPMRTPStreamsInterval,
       "acPMRTPStreamsVal": acPMRTPStreamsVal,
       "acPMRTPStreamsAverage": acPMRTPStreamsAverage,
       "acPMRTPStreamsMax": acPMRTPStreamsMax,
       "acPMRTPStreamsMin": acPMRTPStreamsMin,
       "acPMRTPStreamsVolume": acPMRTPStreamsVolume,
       "acPMRTPStreamsTimeBelowLowThreshold": acPMRTPStreamsTimeBelowLowThreshold,
       "acPMRTPStreamsTimeBetweenThresholds": acPMRTPStreamsTimeBetweenThresholds,
       "acPMRTPStreamsTimeAboveHighThreshold": acPMRTPStreamsTimeAboveHighThreshold,
       "acPMRTPStreamsFullDayAverage": acPMRTPStreamsFullDayAverage,
       "acPMSRTPStreamsTable": acPMSRTPStreamsTable,
       "acPMSRTPStreamsEntry": acPMSRTPStreamsEntry,
       "acPMSRTPStreamsInterval": acPMSRTPStreamsInterval,
       "acPMSRTPStreamsVal": acPMSRTPStreamsVal,
       "acPMSRTPStreamsAverage": acPMSRTPStreamsAverage,
       "acPMSRTPStreamsMax": acPMSRTPStreamsMax,
       "acPMSRTPStreamsMin": acPMSRTPStreamsMin,
       "acPMSRTPStreamsVolume": acPMSRTPStreamsVolume,
       "acPMSRTPStreamsTimeBelowLowThreshold": acPMSRTPStreamsTimeBelowLowThreshold,
       "acPMSRTPStreamsTimeBetweenThresholds": acPMSRTPStreamsTimeBetweenThresholds,
       "acPMSRTPStreamsTimeAboveHighThreshold": acPMSRTPStreamsTimeAboveHighThreshold,
       "acPMSRTPStreamsFullDayAverage": acPMSRTPStreamsFullDayAverage,
       "acPMMulticastRegisteredChannelsTable": acPMMulticastRegisteredChannelsTable,
       "acPMMulticastRegisteredChannelsEntry": acPMMulticastRegisteredChannelsEntry,
       "acPMMulticastRegisteredChannelsInterval": acPMMulticastRegisteredChannelsInterval,
       "acPMMulticastRegisteredChannelsVal": acPMMulticastRegisteredChannelsVal,
       "acPMMulticastRegisteredChannelsAverage": acPMMulticastRegisteredChannelsAverage,
       "acPMMulticastRegisteredChannelsMax": acPMMulticastRegisteredChannelsMax,
       "acPMMulticastRegisteredChannelsMin": acPMMulticastRegisteredChannelsMin,
       "acPMMulticastRegisteredChannelsVolume": acPMMulticastRegisteredChannelsVolume,
       "acPMMulticastRegisteredChannelsTimeBelowLowThreshold": acPMMulticastRegisteredChannelsTimeBelowLowThreshold,
       "acPMMulticastRegisteredChannelsTimeBetweenThresholds": acPMMulticastRegisteredChannelsTimeBetweenThresholds,
       "acPMMulticastRegisteredChannelsTimeAboveHighThreshold": acPMMulticastRegisteredChannelsTimeAboveHighThreshold,
       "acPMMulticastRegisteredChannelsFullDayAverage": acPMMulticastRegisteredChannelsFullDayAverage,
       "acPMModemRelayActiveChannelsTable": acPMModemRelayActiveChannelsTable,
       "acPMModemRelayActiveChannelsEntry": acPMModemRelayActiveChannelsEntry,
       "acPMModemRelayActiveChannelsInterval": acPMModemRelayActiveChannelsInterval,
       "acPMModemRelayActiveChannelsVal": acPMModemRelayActiveChannelsVal,
       "acPMModemRelayActiveChannelsAverage": acPMModemRelayActiveChannelsAverage,
       "acPMModemRelayActiveChannelsMax": acPMModemRelayActiveChannelsMax,
       "acPMModemRelayActiveChannelsMin": acPMModemRelayActiveChannelsMin,
       "acPMModemRelayActiveChannelsVolume": acPMModemRelayActiveChannelsVolume,
       "acPMModemRelayActiveChannelsTimeBelowLowThreshold": acPMModemRelayActiveChannelsTimeBelowLowThreshold,
       "acPMModemRelayActiveChannelsTimeBetweenThresholds": acPMModemRelayActiveChannelsTimeBetweenThresholds,
       "acPMModemRelayActiveChannelsTimeAboveHighThreshold": acPMModemRelayActiveChannelsTimeAboveHighThreshold,
       "acPMModemRelayActiveChannelsFullDayAverage": acPMModemRelayActiveChannelsFullDayAverage,
       "acPMStreamingCache": acPMStreamingCache,
       "acPMStreamingCacheHitRateTable": acPMStreamingCacheHitRateTable,
       "acPMStreamingCacheHitRateEntry": acPMStreamingCacheHitRateEntry,
       "acPMStreamingCacheHitRateInterval": acPMStreamingCacheHitRateInterval,
       "acPMStreamingCacheHitRateAverage": acPMStreamingCacheHitRateAverage,
       "acPMStreamingCacheHitRateMax": acPMStreamingCacheHitRateMax,
       "acPMStreamingCacheHitRateMin": acPMStreamingCacheHitRateMin,
       "acPMStreamingCacheHitRateVolume": acPMStreamingCacheHitRateVolume,
       "acPMStreamingCacheHitRateTimeBelowLowThreshold": acPMStreamingCacheHitRateTimeBelowLowThreshold,
       "acPMStreamingCacheHitRateTimeBetweenThresholds": acPMStreamingCacheHitRateTimeBetweenThresholds,
       "acPMStreamingCacheHitRateTimeAboveHighThreshold": acPMStreamingCacheHitRateTimeAboveHighThreshold,
       "acPMStreamingCacheHitRateFullDayAverage": acPMStreamingCacheHitRateFullDayAverage,
       "acPMStreamingCacheMissRateTable": acPMStreamingCacheMissRateTable,
       "acPMStreamingCacheMissRateEntry": acPMStreamingCacheMissRateEntry,
       "acPMStreamingCacheMissRateInterval": acPMStreamingCacheMissRateInterval,
       "acPMStreamingCacheMissRateAverage": acPMStreamingCacheMissRateAverage,
       "acPMStreamingCacheMissRateMax": acPMStreamingCacheMissRateMax,
       "acPMStreamingCacheMissRateMin": acPMStreamingCacheMissRateMin,
       "acPMStreamingCacheMissRateVolume": acPMStreamingCacheMissRateVolume,
       "acPMStreamingCacheMissRateTimeBelowLowThreshold": acPMStreamingCacheMissRateTimeBelowLowThreshold,
       "acPMStreamingCacheMissRateTimeBetweenThresholds": acPMStreamingCacheMissRateTimeBetweenThresholds,
       "acPMStreamingCacheMissRateTimeAboveHighThreshold": acPMStreamingCacheMissRateTimeAboveHighThreshold,
       "acPMStreamingCacheMissRateFullDayAverage": acPMStreamingCacheMissRateFullDayAverage,
       "acPMStreamingCacheServerRequestsRateTable": acPMStreamingCacheServerRequestsRateTable,
       "acPMStreamingCacheServerRequestsRateEntry": acPMStreamingCacheServerRequestsRateEntry,
       "acPMStreamingCacheServerRequestsRateInterval": acPMStreamingCacheServerRequestsRateInterval,
       "acPMStreamingCacheServerRequestsRateAverage": acPMStreamingCacheServerRequestsRateAverage,
       "acPMStreamingCacheServerRequestsRateMax": acPMStreamingCacheServerRequestsRateMax,
       "acPMStreamingCacheServerRequestsRateMin": acPMStreamingCacheServerRequestsRateMin,
       "acPMStreamingCacheServerRequestsRateVolume": acPMStreamingCacheServerRequestsRateVolume,
       "acPMStreamingCacheServerRequestsRateTimeBelowLowThreshold": acPMStreamingCacheServerRequestsRateTimeBelowLowThreshold,
       "acPMStreamingCacheServerRequestsRateTimeBetweenThresholds": acPMStreamingCacheServerRequestsRateTimeBetweenThresholds,
       "acPMStreamingCacheServerRequestsRateTimeAboveHighThreshold": acPMStreamingCacheServerRequestsRateTimeAboveHighThreshold,
       "acPMStreamingCacheServerRequestsRateFullDayAverage": acPMStreamingCacheServerRequestsRateFullDayAverage}
)
