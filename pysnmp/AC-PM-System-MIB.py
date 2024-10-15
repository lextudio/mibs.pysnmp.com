# SNMP MIB module (AC-PM-System-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-PM-System-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:36 2024
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

acPMSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcPMSystemConfiguration_ObjectIdentity = ObjectIdentity
acPMSystemConfiguration = _AcPMSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1)
)


class _AcPMSystemConfigurationPeriodLength_Type(Unsigned32):
    """Custom type acPMSystemConfigurationPeriodLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 894780),
    )


_AcPMSystemConfigurationPeriodLength_Type.__name__ = "Unsigned32"
_AcPMSystemConfigurationPeriodLength_Object = MibScalar
acPMSystemConfigurationPeriodLength = _AcPMSystemConfigurationPeriodLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 1),
    _AcPMSystemConfigurationPeriodLength_Type()
)
acPMSystemConfigurationPeriodLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSystemConfigurationPeriodLength.setStatus("current")


class _AcPMSystemConfigurationResetTotalCounters_Type(Integer32):
    """Custom type acPMSystemConfigurationResetTotalCounters based on Integer32"""
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


_AcPMSystemConfigurationResetTotalCounters_Type.__name__ = "Integer32"
_AcPMSystemConfigurationResetTotalCounters_Object = MibScalar
acPMSystemConfigurationResetTotalCounters = _AcPMSystemConfigurationResetTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 2),
    _AcPMSystemConfigurationResetTotalCounters_Type()
)
acPMSystemConfigurationResetTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSystemConfigurationResetTotalCounters.setStatus("current")
_AcPMNetConnectionAttributes_ObjectIdentity = ObjectIdentity
acPMNetConnectionAttributes = _AcPMNetConnectionAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 31)
)


class _AcPMNetConnectionAttributesStateHighThreshold_Type(Unsigned32):
    """Custom type acPMNetConnectionAttributesStateHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetConnectionAttributesStateHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetConnectionAttributesStateHighThreshold_Object = MibScalar
acPMNetConnectionAttributesStateHighThreshold = _AcPMNetConnectionAttributesStateHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 31, 1),
    _AcPMNetConnectionAttributesStateHighThreshold_Type()
)
acPMNetConnectionAttributesStateHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetConnectionAttributesStateHighThreshold.setStatus("current")


class _AcPMNetConnectionAttributesStateLowThreshold_Type(Unsigned32):
    """Custom type acPMNetConnectionAttributesStateLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetConnectionAttributesStateLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetConnectionAttributesStateLowThreshold_Object = MibScalar
acPMNetConnectionAttributesStateLowThreshold = _AcPMNetConnectionAttributesStateLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 31, 2),
    _AcPMNetConnectionAttributesStateLowThreshold_Type()
)
acPMNetConnectionAttributesStateLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetConnectionAttributesStateLowThreshold.setStatus("current")
_AcPMNetAttributes_ObjectIdentity = ObjectIdentity
acPMNetAttributes = _AcPMNetAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 32)
)


class _AcPMNetAttributesUnknownUDPPortCounterHighThreshold_Type(Unsigned32):
    """Custom type acPMNetAttributesUnknownUDPPortCounterHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetAttributesUnknownUDPPortCounterHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetAttributesUnknownUDPPortCounterHighThreshold_Object = MibScalar
acPMNetAttributesUnknownUDPPortCounterHighThreshold = _AcPMNetAttributesUnknownUDPPortCounterHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 32, 1),
    _AcPMNetAttributesUnknownUDPPortCounterHighThreshold_Type()
)
acPMNetAttributesUnknownUDPPortCounterHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetAttributesUnknownUDPPortCounterHighThreshold.setStatus("current")


class _AcPMNetAttributesUnknownUDPPortCounterLowThreshold_Type(Unsigned32):
    """Custom type acPMNetAttributesUnknownUDPPortCounterLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetAttributesUnknownUDPPortCounterLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetAttributesUnknownUDPPortCounterLowThreshold_Object = MibScalar
acPMNetAttributesUnknownUDPPortCounterLowThreshold = _AcPMNetAttributesUnknownUDPPortCounterLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 32, 2),
    _AcPMNetAttributesUnknownUDPPortCounterLowThreshold_Type()
)
acPMNetAttributesUnknownUDPPortCounterLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetAttributesUnknownUDPPortCounterLowThreshold.setStatus("current")
_AcPMNetUtilsAttributes_ObjectIdentity = ObjectIdentity
acPMNetUtilsAttributes = _AcPMNetUtilsAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 33)
)


class _AcPMNetUtilsAttributesKBytesHighThreshold_Type(Unsigned32):
    """Custom type acPMNetUtilsAttributesKBytesHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetUtilsAttributesKBytesHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetUtilsAttributesKBytesHighThreshold_Object = MibScalar
acPMNetUtilsAttributesKBytesHighThreshold = _AcPMNetUtilsAttributesKBytesHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 33, 1),
    _AcPMNetUtilsAttributesKBytesHighThreshold_Type()
)
acPMNetUtilsAttributesKBytesHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetUtilsAttributesKBytesHighThreshold.setStatus("current")


class _AcPMNetUtilsAttributesKBytesLowThreshold_Type(Unsigned32):
    """Custom type acPMNetUtilsAttributesKBytesLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetUtilsAttributesKBytesLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetUtilsAttributesKBytesLowThreshold_Object = MibScalar
acPMNetUtilsAttributesKBytesLowThreshold = _AcPMNetUtilsAttributesKBytesLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 33, 2),
    _AcPMNetUtilsAttributesKBytesLowThreshold_Type()
)
acPMNetUtilsAttributesKBytesLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetUtilsAttributesKBytesLowThreshold.setStatus("current")


class _AcPMNetUtilsAttributesPacketsHighThreshold_Type(Unsigned32):
    """Custom type acPMNetUtilsAttributesPacketsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetUtilsAttributesPacketsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetUtilsAttributesPacketsHighThreshold_Object = MibScalar
acPMNetUtilsAttributesPacketsHighThreshold = _AcPMNetUtilsAttributesPacketsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 33, 3),
    _AcPMNetUtilsAttributesPacketsHighThreshold_Type()
)
acPMNetUtilsAttributesPacketsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetUtilsAttributesPacketsHighThreshold.setStatus("current")


class _AcPMNetUtilsAttributesPacketsLowThreshold_Type(Unsigned32):
    """Custom type acPMNetUtilsAttributesPacketsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetUtilsAttributesPacketsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetUtilsAttributesPacketsLowThreshold_Object = MibScalar
acPMNetUtilsAttributesPacketsLowThreshold = _AcPMNetUtilsAttributesPacketsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 33, 4),
    _AcPMNetUtilsAttributesPacketsLowThreshold_Type()
)
acPMNetUtilsAttributesPacketsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetUtilsAttributesPacketsLowThreshold.setStatus("current")


class _AcPMNetUtilsAttributesDiscardedPacketsHighThreshold_Type(Unsigned32):
    """Custom type acPMNetUtilsAttributesDiscardedPacketsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetUtilsAttributesDiscardedPacketsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetUtilsAttributesDiscardedPacketsHighThreshold_Object = MibScalar
acPMNetUtilsAttributesDiscardedPacketsHighThreshold = _AcPMNetUtilsAttributesDiscardedPacketsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 33, 5),
    _AcPMNetUtilsAttributesDiscardedPacketsHighThreshold_Type()
)
acPMNetUtilsAttributesDiscardedPacketsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetUtilsAttributesDiscardedPacketsHighThreshold.setStatus("current")


class _AcPMNetUtilsAttributesDiscardedPacketsLowThreshold_Type(Unsigned32):
    """Custom type acPMNetUtilsAttributesDiscardedPacketsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetUtilsAttributesDiscardedPacketsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetUtilsAttributesDiscardedPacketsLowThreshold_Object = MibScalar
acPMNetUtilsAttributesDiscardedPacketsLowThreshold = _AcPMNetUtilsAttributesDiscardedPacketsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 33, 6),
    _AcPMNetUtilsAttributesDiscardedPacketsLowThreshold_Type()
)
acPMNetUtilsAttributesDiscardedPacketsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetUtilsAttributesDiscardedPacketsLowThreshold.setStatus("current")
_AcPMNetworkAttributes_ObjectIdentity = ObjectIdentity
acPMNetworkAttributes = _AcPMNetworkAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 34)
)


class _AcPMNetworkAttributesDhcpResponseTimeHighThreshold_Type(Unsigned32):
    """Custom type acPMNetworkAttributesDhcpResponseTimeHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkAttributesDhcpResponseTimeHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkAttributesDhcpResponseTimeHighThreshold_Object = MibScalar
acPMNetworkAttributesDhcpResponseTimeHighThreshold = _AcPMNetworkAttributesDhcpResponseTimeHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 34, 1),
    _AcPMNetworkAttributesDhcpResponseTimeHighThreshold_Type()
)
acPMNetworkAttributesDhcpResponseTimeHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkAttributesDhcpResponseTimeHighThreshold.setStatus("current")


class _AcPMNetworkAttributesDhcpResponseTimeLowThreshold_Type(Unsigned32):
    """Custom type acPMNetworkAttributesDhcpResponseTimeLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNetworkAttributesDhcpResponseTimeLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNetworkAttributesDhcpResponseTimeLowThreshold_Object = MibScalar
acPMNetworkAttributesDhcpResponseTimeLowThreshold = _AcPMNetworkAttributesDhcpResponseTimeLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 34, 2),
    _AcPMNetworkAttributesDhcpResponseTimeLowThreshold_Type()
)
acPMNetworkAttributesDhcpResponseTimeLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNetworkAttributesDhcpResponseTimeLowThreshold.setStatus("current")
_AcPMCongestionAttributes_ObjectIdentity = ObjectIdentity
acPMCongestionAttributes = _AcPMCongestionAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 35)
)


class _AcPMCongestionAttributesHighThreshold_Type(Unsigned32):
    """Custom type acPMCongestionAttributesHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMCongestionAttributesHighThreshold_Type.__name__ = "Unsigned32"
_AcPMCongestionAttributesHighThreshold_Object = MibScalar
acPMCongestionAttributesHighThreshold = _AcPMCongestionAttributesHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 35, 1),
    _AcPMCongestionAttributesHighThreshold_Type()
)
acPMCongestionAttributesHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCongestionAttributesHighThreshold.setStatus("current")


class _AcPMCongestionAttributesLowThreshold_Type(Unsigned32):
    """Custom type acPMCongestionAttributesLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMCongestionAttributesLowThreshold_Type.__name__ = "Unsigned32"
_AcPMCongestionAttributesLowThreshold_Object = MibScalar
acPMCongestionAttributesLowThreshold = _AcPMCongestionAttributesLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 35, 2),
    _AcPMCongestionAttributesLowThreshold_Type()
)
acPMCongestionAttributesLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCongestionAttributesLowThreshold.setStatus("current")
_AcPMNFSAttributes_ObjectIdentity = ObjectIdentity
acPMNFSAttributes = _AcPMNFSAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 36)
)


class _AcPMNFSAttributesRoundTripTimeMsHighThreshold_Type(Unsigned32):
    """Custom type acPMNFSAttributesRoundTripTimeMsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNFSAttributesRoundTripTimeMsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNFSAttributesRoundTripTimeMsHighThreshold_Object = MibScalar
acPMNFSAttributesRoundTripTimeMsHighThreshold = _AcPMNFSAttributesRoundTripTimeMsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 36, 1),
    _AcPMNFSAttributesRoundTripTimeMsHighThreshold_Type()
)
acPMNFSAttributesRoundTripTimeMsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNFSAttributesRoundTripTimeMsHighThreshold.setStatus("current")


class _AcPMNFSAttributesRoundTripTimeMsLowThreshold_Type(Unsigned32):
    """Custom type acPMNFSAttributesRoundTripTimeMsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNFSAttributesRoundTripTimeMsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNFSAttributesRoundTripTimeMsLowThreshold_Object = MibScalar
acPMNFSAttributesRoundTripTimeMsLowThreshold = _AcPMNFSAttributesRoundTripTimeMsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 36, 2),
    _AcPMNFSAttributesRoundTripTimeMsLowThreshold_Type()
)
acPMNFSAttributesRoundTripTimeMsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNFSAttributesRoundTripTimeMsLowThreshold.setStatus("current")


class _AcPMNFSAttributesRetriesHighThreshold_Type(Unsigned32):
    """Custom type acPMNFSAttributesRetriesHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNFSAttributesRetriesHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNFSAttributesRetriesHighThreshold_Object = MibScalar
acPMNFSAttributesRetriesHighThreshold = _AcPMNFSAttributesRetriesHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 36, 3),
    _AcPMNFSAttributesRetriesHighThreshold_Type()
)
acPMNFSAttributesRetriesHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNFSAttributesRetriesHighThreshold.setStatus("current")


class _AcPMNFSAttributesRetriesLowThreshold_Type(Unsigned32):
    """Custom type acPMNFSAttributesRetriesLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNFSAttributesRetriesLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNFSAttributesRetriesLowThreshold_Object = MibScalar
acPMNFSAttributesRetriesLowThreshold = _AcPMNFSAttributesRetriesLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 36, 4),
    _AcPMNFSAttributesRetriesLowThreshold_Type()
)
acPMNFSAttributesRetriesLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNFSAttributesRetriesLowThreshold.setStatus("current")


class _AcPMNFSAttributesAbortDueToMaxRetriesExceededHighThreshold_Type(Unsigned32):
    """Custom type acPMNFSAttributesAbortDueToMaxRetriesExceededHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNFSAttributesAbortDueToMaxRetriesExceededHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNFSAttributesAbortDueToMaxRetriesExceededHighThreshold_Object = MibScalar
acPMNFSAttributesAbortDueToMaxRetriesExceededHighThreshold = _AcPMNFSAttributesAbortDueToMaxRetriesExceededHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 36, 5),
    _AcPMNFSAttributesAbortDueToMaxRetriesExceededHighThreshold_Type()
)
acPMNFSAttributesAbortDueToMaxRetriesExceededHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNFSAttributesAbortDueToMaxRetriesExceededHighThreshold.setStatus("current")


class _AcPMNFSAttributesAbortDueToMaxRetriesExceededLowThreshold_Type(Unsigned32):
    """Custom type acPMNFSAttributesAbortDueToMaxRetriesExceededLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNFSAttributesAbortDueToMaxRetriesExceededLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNFSAttributesAbortDueToMaxRetriesExceededLowThreshold_Object = MibScalar
acPMNFSAttributesAbortDueToMaxRetriesExceededLowThreshold = _AcPMNFSAttributesAbortDueToMaxRetriesExceededLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 36, 6),
    _AcPMNFSAttributesAbortDueToMaxRetriesExceededLowThreshold_Type()
)
acPMNFSAttributesAbortDueToMaxRetriesExceededLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNFSAttributesAbortDueToMaxRetriesExceededLowThreshold.setStatus("current")


class _AcPMNFSAttributesDelayedResponsesHighThreshold_Type(Unsigned32):
    """Custom type acPMNFSAttributesDelayedResponsesHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNFSAttributesDelayedResponsesHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNFSAttributesDelayedResponsesHighThreshold_Object = MibScalar
acPMNFSAttributesDelayedResponsesHighThreshold = _AcPMNFSAttributesDelayedResponsesHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 36, 7),
    _AcPMNFSAttributesDelayedResponsesHighThreshold_Type()
)
acPMNFSAttributesDelayedResponsesHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNFSAttributesDelayedResponsesHighThreshold.setStatus("current")


class _AcPMNFSAttributesDelayedResponsesLowThreshold_Type(Unsigned32):
    """Custom type acPMNFSAttributesDelayedResponsesLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNFSAttributesDelayedResponsesLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNFSAttributesDelayedResponsesLowThreshold_Object = MibScalar
acPMNFSAttributesDelayedResponsesLowThreshold = _AcPMNFSAttributesDelayedResponsesLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 36, 8),
    _AcPMNFSAttributesDelayedResponsesLowThreshold_Type()
)
acPMNFSAttributesDelayedResponsesLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNFSAttributesDelayedResponsesLowThreshold.setStatus("current")


class _AcPMNFSAttributesBytesDroppedOnRecordHighThreshold_Type(Unsigned32):
    """Custom type acPMNFSAttributesBytesDroppedOnRecordHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNFSAttributesBytesDroppedOnRecordHighThreshold_Type.__name__ = "Unsigned32"
_AcPMNFSAttributesBytesDroppedOnRecordHighThreshold_Object = MibScalar
acPMNFSAttributesBytesDroppedOnRecordHighThreshold = _AcPMNFSAttributesBytesDroppedOnRecordHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 36, 9),
    _AcPMNFSAttributesBytesDroppedOnRecordHighThreshold_Type()
)
acPMNFSAttributesBytesDroppedOnRecordHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNFSAttributesBytesDroppedOnRecordHighThreshold.setStatus("current")


class _AcPMNFSAttributesBytesDroppedOnRecordLowThreshold_Type(Unsigned32):
    """Custom type acPMNFSAttributesBytesDroppedOnRecordLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMNFSAttributesBytesDroppedOnRecordLowThreshold_Type.__name__ = "Unsigned32"
_AcPMNFSAttributesBytesDroppedOnRecordLowThreshold_Object = MibScalar
acPMNFSAttributesBytesDroppedOnRecordLowThreshold = _AcPMNFSAttributesBytesDroppedOnRecordLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 36, 10),
    _AcPMNFSAttributesBytesDroppedOnRecordLowThreshold_Type()
)
acPMNFSAttributesBytesDroppedOnRecordLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMNFSAttributesBytesDroppedOnRecordLowThreshold.setStatus("current")
_AcPMMSBGAttributes_ObjectIdentity = ObjectIdentity
acPMMSBGAttributes = _AcPMMSBGAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37)
)


class _AcPMMSBGAttributesRXGoodOctetsHighThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXGoodOctetsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXGoodOctetsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXGoodOctetsHighThreshold_Object = MibScalar
acPMMSBGAttributesRXGoodOctetsHighThreshold = _AcPMMSBGAttributesRXGoodOctetsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 1),
    _AcPMMSBGAttributesRXGoodOctetsHighThreshold_Type()
)
acPMMSBGAttributesRXGoodOctetsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXGoodOctetsHighThreshold.setStatus("current")


class _AcPMMSBGAttributesRXGoodOctetsLowThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXGoodOctetsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXGoodOctetsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXGoodOctetsLowThreshold_Object = MibScalar
acPMMSBGAttributesRXGoodOctetsLowThreshold = _AcPMMSBGAttributesRXGoodOctetsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 2),
    _AcPMMSBGAttributesRXGoodOctetsLowThreshold_Type()
)
acPMMSBGAttributesRXGoodOctetsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXGoodOctetsLowThreshold.setStatus("current")


class _AcPMMSBGAttributesRXBadOctetsHighThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXBadOctetsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXBadOctetsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXBadOctetsHighThreshold_Object = MibScalar
acPMMSBGAttributesRXBadOctetsHighThreshold = _AcPMMSBGAttributesRXBadOctetsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 3),
    _AcPMMSBGAttributesRXBadOctetsHighThreshold_Type()
)
acPMMSBGAttributesRXBadOctetsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXBadOctetsHighThreshold.setStatus("current")


class _AcPMMSBGAttributesRXBadOctetsLowThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXBadOctetsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXBadOctetsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXBadOctetsLowThreshold_Object = MibScalar
acPMMSBGAttributesRXBadOctetsLowThreshold = _AcPMMSBGAttributesRXBadOctetsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 4),
    _AcPMMSBGAttributesRXBadOctetsLowThreshold_Type()
)
acPMMSBGAttributesRXBadOctetsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXBadOctetsLowThreshold.setStatus("current")


class _AcPMMSBGAttributesRXUndersizePacketsHighThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXUndersizePacketsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXUndersizePacketsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXUndersizePacketsHighThreshold_Object = MibScalar
acPMMSBGAttributesRXUndersizePacketsHighThreshold = _AcPMMSBGAttributesRXUndersizePacketsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 5),
    _AcPMMSBGAttributesRXUndersizePacketsHighThreshold_Type()
)
acPMMSBGAttributesRXUndersizePacketsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXUndersizePacketsHighThreshold.setStatus("current")


class _AcPMMSBGAttributesRXUndersizePacketsLowThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXUndersizePacketsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXUndersizePacketsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXUndersizePacketsLowThreshold_Object = MibScalar
acPMMSBGAttributesRXUndersizePacketsLowThreshold = _AcPMMSBGAttributesRXUndersizePacketsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 6),
    _AcPMMSBGAttributesRXUndersizePacketsLowThreshold_Type()
)
acPMMSBGAttributesRXUndersizePacketsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXUndersizePacketsLowThreshold.setStatus("current")


class _AcPMMSBGAttributesRXOversizePacketsHighThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXOversizePacketsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXOversizePacketsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXOversizePacketsHighThreshold_Object = MibScalar
acPMMSBGAttributesRXOversizePacketsHighThreshold = _AcPMMSBGAttributesRXOversizePacketsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 7),
    _AcPMMSBGAttributesRXOversizePacketsHighThreshold_Type()
)
acPMMSBGAttributesRXOversizePacketsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXOversizePacketsHighThreshold.setStatus("current")


class _AcPMMSBGAttributesRXOversizePacketsLowThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXOversizePacketsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXOversizePacketsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXOversizePacketsLowThreshold_Object = MibScalar
acPMMSBGAttributesRXOversizePacketsLowThreshold = _AcPMMSBGAttributesRXOversizePacketsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 8),
    _AcPMMSBGAttributesRXOversizePacketsLowThreshold_Type()
)
acPMMSBGAttributesRXOversizePacketsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXOversizePacketsLowThreshold.setStatus("current")


class _AcPMMSBGAttributesRXMacErrorsHighThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXMacErrorsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXMacErrorsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXMacErrorsHighThreshold_Object = MibScalar
acPMMSBGAttributesRXMacErrorsHighThreshold = _AcPMMSBGAttributesRXMacErrorsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 9),
    _AcPMMSBGAttributesRXMacErrorsHighThreshold_Type()
)
acPMMSBGAttributesRXMacErrorsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXMacErrorsHighThreshold.setStatus("current")


class _AcPMMSBGAttributesRXMacErrorsLowThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXMacErrorsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXMacErrorsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXMacErrorsLowThreshold_Object = MibScalar
acPMMSBGAttributesRXMacErrorsLowThreshold = _AcPMMSBGAttributesRXMacErrorsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 10),
    _AcPMMSBGAttributesRXMacErrorsLowThreshold_Type()
)
acPMMSBGAttributesRXMacErrorsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXMacErrorsLowThreshold.setStatus("current")


class _AcPMMSBGAttributesRXFCSErroredPacketsHighThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXFCSErroredPacketsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXFCSErroredPacketsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXFCSErroredPacketsHighThreshold_Object = MibScalar
acPMMSBGAttributesRXFCSErroredPacketsHighThreshold = _AcPMMSBGAttributesRXFCSErroredPacketsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 11),
    _AcPMMSBGAttributesRXFCSErroredPacketsHighThreshold_Type()
)
acPMMSBGAttributesRXFCSErroredPacketsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXFCSErroredPacketsHighThreshold.setStatus("current")


class _AcPMMSBGAttributesRXFCSErroredPacketsLowThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXFCSErroredPacketsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXFCSErroredPacketsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXFCSErroredPacketsLowThreshold_Object = MibScalar
acPMMSBGAttributesRXFCSErroredPacketsLowThreshold = _AcPMMSBGAttributesRXFCSErroredPacketsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 12),
    _AcPMMSBGAttributesRXFCSErroredPacketsLowThreshold_Type()
)
acPMMSBGAttributesRXFCSErroredPacketsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXFCSErroredPacketsLowThreshold.setStatus("current")


class _AcPMMSBGAttributesRXDiscardPacketsHighThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXDiscardPacketsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXDiscardPacketsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXDiscardPacketsHighThreshold_Object = MibScalar
acPMMSBGAttributesRXDiscardPacketsHighThreshold = _AcPMMSBGAttributesRXDiscardPacketsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 13),
    _AcPMMSBGAttributesRXDiscardPacketsHighThreshold_Type()
)
acPMMSBGAttributesRXDiscardPacketsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXDiscardPacketsHighThreshold.setStatus("current")


class _AcPMMSBGAttributesRXDiscardPacketsLowThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesRXDiscardPacketsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesRXDiscardPacketsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesRXDiscardPacketsLowThreshold_Object = MibScalar
acPMMSBGAttributesRXDiscardPacketsLowThreshold = _AcPMMSBGAttributesRXDiscardPacketsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 14),
    _AcPMMSBGAttributesRXDiscardPacketsLowThreshold_Type()
)
acPMMSBGAttributesRXDiscardPacketsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesRXDiscardPacketsLowThreshold.setStatus("current")


class _AcPMMSBGAttributesTXOctetsHighThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesTXOctetsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesTXOctetsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesTXOctetsHighThreshold_Object = MibScalar
acPMMSBGAttributesTXOctetsHighThreshold = _AcPMMSBGAttributesTXOctetsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 15),
    _AcPMMSBGAttributesTXOctetsHighThreshold_Type()
)
acPMMSBGAttributesTXOctetsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesTXOctetsHighThreshold.setStatus("current")


class _AcPMMSBGAttributesTXOctetsLowThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesTXOctetsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesTXOctetsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesTXOctetsLowThreshold_Object = MibScalar
acPMMSBGAttributesTXOctetsLowThreshold = _AcPMMSBGAttributesTXOctetsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 16),
    _AcPMMSBGAttributesTXOctetsLowThreshold_Type()
)
acPMMSBGAttributesTXOctetsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesTXOctetsLowThreshold.setStatus("current")


class _AcPMMSBGAttributesTXPacketsHighThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesTXPacketsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesTXPacketsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesTXPacketsHighThreshold_Object = MibScalar
acPMMSBGAttributesTXPacketsHighThreshold = _AcPMMSBGAttributesTXPacketsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 17),
    _AcPMMSBGAttributesTXPacketsHighThreshold_Type()
)
acPMMSBGAttributesTXPacketsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesTXPacketsHighThreshold.setStatus("current")


class _AcPMMSBGAttributesTXPacketsLowThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesTXPacketsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesTXPacketsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesTXPacketsLowThreshold_Object = MibScalar
acPMMSBGAttributesTXPacketsLowThreshold = _AcPMMSBGAttributesTXPacketsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 18),
    _AcPMMSBGAttributesTXPacketsLowThreshold_Type()
)
acPMMSBGAttributesTXPacketsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesTXPacketsLowThreshold.setStatus("current")


class _AcPMMSBGAttributesTXCollisionsHighThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesTXCollisionsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesTXCollisionsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesTXCollisionsHighThreshold_Object = MibScalar
acPMMSBGAttributesTXCollisionsHighThreshold = _AcPMMSBGAttributesTXCollisionsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 19),
    _AcPMMSBGAttributesTXCollisionsHighThreshold_Type()
)
acPMMSBGAttributesTXCollisionsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesTXCollisionsHighThreshold.setStatus("current")


class _AcPMMSBGAttributesTXCollisionsLowThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesTXCollisionsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesTXCollisionsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesTXCollisionsLowThreshold_Object = MibScalar
acPMMSBGAttributesTXCollisionsLowThreshold = _AcPMMSBGAttributesTXCollisionsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 20),
    _AcPMMSBGAttributesTXCollisionsLowThreshold_Type()
)
acPMMSBGAttributesTXCollisionsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesTXCollisionsLowThreshold.setStatus("current")


class _AcPMMSBGAttributesTXLatePacketsHighThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesTXLatePacketsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesTXLatePacketsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesTXLatePacketsHighThreshold_Object = MibScalar
acPMMSBGAttributesTXLatePacketsHighThreshold = _AcPMMSBGAttributesTXLatePacketsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 21),
    _AcPMMSBGAttributesTXLatePacketsHighThreshold_Type()
)
acPMMSBGAttributesTXLatePacketsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesTXLatePacketsHighThreshold.setStatus("current")


class _AcPMMSBGAttributesTXLatePacketsLowThreshold_Type(Unsigned32):
    """Custom type acPMMSBGAttributesTXLatePacketsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMSBGAttributesTXLatePacketsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMSBGAttributesTXLatePacketsLowThreshold_Object = MibScalar
acPMMSBGAttributesTXLatePacketsLowThreshold = _AcPMMSBGAttributesTXLatePacketsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 1, 37, 22),
    _AcPMMSBGAttributesTXLatePacketsLowThreshold_Type()
)
acPMMSBGAttributesTXLatePacketsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMSBGAttributesTXLatePacketsLowThreshold.setStatus("current")
_AcPMSystemData_ObjectIdentity = ObjectIdentity
acPMSystemData = _AcPMSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2)
)


class _AcPMSystemDataAcPMSystemTimeFromStartOfInterval_Type(Unsigned32):
    """Custom type acPMSystemDataAcPMSystemTimeFromStartOfInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSystemDataAcPMSystemTimeFromStartOfInterval_Type.__name__ = "Unsigned32"
_AcPMSystemDataAcPMSystemTimeFromStartOfInterval_Object = MibScalar
acPMSystemDataAcPMSystemTimeFromStartOfInterval = _AcPMSystemDataAcPMSystemTimeFromStartOfInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 1),
    _AcPMSystemDataAcPMSystemTimeFromStartOfInterval_Type()
)
acPMSystemDataAcPMSystemTimeFromStartOfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSystemDataAcPMSystemTimeFromStartOfInterval.setStatus("current")
_AcPMNetConnectionStateTable_Object = MibTable
acPMNetConnectionStateTable = _AcPMNetConnectionStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 21)
)
if mibBuilder.loadTexts:
    acPMNetConnectionStateTable.setStatus("current")
_AcPMNetConnectionStateEntry_Object = MibTableRow
acPMNetConnectionStateEntry = _AcPMNetConnectionStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 21, 1)
)
acPMNetConnectionStateEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNetConnectionStateInterval"),
)
if mibBuilder.loadTexts:
    acPMNetConnectionStateEntry.setStatus("current")


class _AcPMNetConnectionStateInterval_Type(Unsigned32):
    """Custom type acPMNetConnectionStateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNetConnectionStateInterval_Type.__name__ = "Unsigned32"
_AcPMNetConnectionStateInterval_Object = MibTableColumn
acPMNetConnectionStateInterval = _AcPMNetConnectionStateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 21, 1, 1),
    _AcPMNetConnectionStateInterval_Type()
)
acPMNetConnectionStateInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNetConnectionStateInterval.setStatus("current")
_AcPMNetConnectionStateChanges_Type = Counter32
_AcPMNetConnectionStateChanges_Object = MibTableColumn
acPMNetConnectionStateChanges = _AcPMNetConnectionStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 21, 1, 2),
    _AcPMNetConnectionStateChanges_Type()
)
acPMNetConnectionStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetConnectionStateChanges.setStatus("current")


class _AcPMNetConnectionStateActiveTime_Type(Integer32):
    """Custom type acPMNetConnectionStateActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNetConnectionStateActiveTime_Type.__name__ = "Integer32"
_AcPMNetConnectionStateActiveTime_Object = MibTableColumn
acPMNetConnectionStateActiveTime = _AcPMNetConnectionStateActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 21, 1, 3),
    _AcPMNetConnectionStateActiveTime_Type()
)
acPMNetConnectionStateActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetConnectionStateActiveTime.setStatus("current")
_AcPMNetUnknownUDPPortCounterTable_Object = MibTable
acPMNetUnknownUDPPortCounterTable = _AcPMNetUnknownUDPPortCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 22)
)
if mibBuilder.loadTexts:
    acPMNetUnknownUDPPortCounterTable.setStatus("current")
_AcPMNetUnknownUDPPortCounterEntry_Object = MibTableRow
acPMNetUnknownUDPPortCounterEntry = _AcPMNetUnknownUDPPortCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 22, 1)
)
acPMNetUnknownUDPPortCounterEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNetUnknownUDPPortCounterInterval"),
)
if mibBuilder.loadTexts:
    acPMNetUnknownUDPPortCounterEntry.setStatus("current")


class _AcPMNetUnknownUDPPortCounterInterval_Type(Unsigned32):
    """Custom type acPMNetUnknownUDPPortCounterInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNetUnknownUDPPortCounterInterval_Type.__name__ = "Unsigned32"
_AcPMNetUnknownUDPPortCounterInterval_Object = MibTableColumn
acPMNetUnknownUDPPortCounterInterval = _AcPMNetUnknownUDPPortCounterInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 22, 1, 1),
    _AcPMNetUnknownUDPPortCounterInterval_Type()
)
acPMNetUnknownUDPPortCounterInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNetUnknownUDPPortCounterInterval.setStatus("current")
_AcPMNetUnknownUDPPortCounterVal_Type = Counter32
_AcPMNetUnknownUDPPortCounterVal_Object = MibTableColumn
acPMNetUnknownUDPPortCounterVal = _AcPMNetUnknownUDPPortCounterVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 22, 1, 2),
    _AcPMNetUnknownUDPPortCounterVal_Type()
)
acPMNetUnknownUDPPortCounterVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUnknownUDPPortCounterVal.setStatus("current")
_AcPMSystemNetUtils_ObjectIdentity = ObjectIdentity
acPMSystemNetUtils = _AcPMSystemNetUtils_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31)
)
_AcPMNetUtilKBytesTable_Object = MibTable
acPMNetUtilKBytesTable = _AcPMNetUtilKBytesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1)
)
if mibBuilder.loadTexts:
    acPMNetUtilKBytesTable.setStatus("current")
_AcPMNetUtilKBytesEntry_Object = MibTableRow
acPMNetUtilKBytesEntry = _AcPMNetUtilKBytesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1)
)
acPMNetUtilKBytesEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNetUtilKBytesDirection"),
    (0, "AC-PM-System-MIB", "acPMNetUtilKBytesInterval"),
)
if mibBuilder.loadTexts:
    acPMNetUtilKBytesEntry.setStatus("current")


class _AcPMNetUtilKBytesDirection_Type(Integer32):
    """Custom type acPMNetUtilKBytesDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 0))
    )


_AcPMNetUtilKBytesDirection_Type.__name__ = "Integer32"
_AcPMNetUtilKBytesDirection_Object = MibTableColumn
acPMNetUtilKBytesDirection = _AcPMNetUtilKBytesDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 1),
    _AcPMNetUtilKBytesDirection_Type()
)
acPMNetUtilKBytesDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesDirection.setStatus("current")


class _AcPMNetUtilKBytesInterval_Type(Unsigned32):
    """Custom type acPMNetUtilKBytesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNetUtilKBytesInterval_Type.__name__ = "Unsigned32"
_AcPMNetUtilKBytesInterval_Object = MibTableColumn
acPMNetUtilKBytesInterval = _AcPMNetUtilKBytesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 2),
    _AcPMNetUtilKBytesInterval_Type()
)
acPMNetUtilKBytesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesInterval.setStatus("current")
_AcPMNetUtilKBytesVal_Type = Gauge32
_AcPMNetUtilKBytesVal_Object = MibTableColumn
acPMNetUtilKBytesVal = _AcPMNetUtilKBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 3),
    _AcPMNetUtilKBytesVal_Type()
)
acPMNetUtilKBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesVal.setStatus("current")


class _AcPMNetUtilKBytesAverage_Type(Integer32):
    """Custom type acPMNetUtilKBytesAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNetUtilKBytesAverage_Type.__name__ = "Integer32"
_AcPMNetUtilKBytesAverage_Object = MibTableColumn
acPMNetUtilKBytesAverage = _AcPMNetUtilKBytesAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 4),
    _AcPMNetUtilKBytesAverage_Type()
)
acPMNetUtilKBytesAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesAverage.setStatus("current")


class _AcPMNetUtilKBytesMax_Type(Integer32):
    """Custom type acPMNetUtilKBytesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNetUtilKBytesMax_Type.__name__ = "Integer32"
_AcPMNetUtilKBytesMax_Object = MibTableColumn
acPMNetUtilKBytesMax = _AcPMNetUtilKBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 5),
    _AcPMNetUtilKBytesMax_Type()
)
acPMNetUtilKBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesMax.setStatus("current")


class _AcPMNetUtilKBytesMin_Type(Integer32):
    """Custom type acPMNetUtilKBytesMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNetUtilKBytesMin_Type.__name__ = "Integer32"
_AcPMNetUtilKBytesMin_Object = MibTableColumn
acPMNetUtilKBytesMin = _AcPMNetUtilKBytesMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 6),
    _AcPMNetUtilKBytesMin_Type()
)
acPMNetUtilKBytesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesMin.setStatus("current")
_AcPMNetUtilKBytesVolume_Type = Counter32
_AcPMNetUtilKBytesVolume_Object = MibTableColumn
acPMNetUtilKBytesVolume = _AcPMNetUtilKBytesVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 7),
    _AcPMNetUtilKBytesVolume_Type()
)
acPMNetUtilKBytesVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesVolume.setStatus("current")


class _AcPMNetUtilKBytesTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMNetUtilKBytesTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNetUtilKBytesTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMNetUtilKBytesTimeBelowLowThreshold_Object = MibTableColumn
acPMNetUtilKBytesTimeBelowLowThreshold = _AcPMNetUtilKBytesTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 8),
    _AcPMNetUtilKBytesTimeBelowLowThreshold_Type()
)
acPMNetUtilKBytesTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesTimeBelowLowThreshold.setStatus("current")


class _AcPMNetUtilKBytesTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMNetUtilKBytesTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNetUtilKBytesTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMNetUtilKBytesTimeBetweenThresholds_Object = MibTableColumn
acPMNetUtilKBytesTimeBetweenThresholds = _AcPMNetUtilKBytesTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 9),
    _AcPMNetUtilKBytesTimeBetweenThresholds_Type()
)
acPMNetUtilKBytesTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesTimeBetweenThresholds.setStatus("current")


class _AcPMNetUtilKBytesTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMNetUtilKBytesTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNetUtilKBytesTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMNetUtilKBytesTimeAboveHighThreshold_Object = MibTableColumn
acPMNetUtilKBytesTimeAboveHighThreshold = _AcPMNetUtilKBytesTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 10),
    _AcPMNetUtilKBytesTimeAboveHighThreshold_Type()
)
acPMNetUtilKBytesTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesTimeAboveHighThreshold.setStatus("current")


class _AcPMNetUtilKBytesFullDayAverage_Type(Integer32):
    """Custom type acPMNetUtilKBytesFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNetUtilKBytesFullDayAverage_Type.__name__ = "Integer32"
_AcPMNetUtilKBytesFullDayAverage_Object = MibTableColumn
acPMNetUtilKBytesFullDayAverage = _AcPMNetUtilKBytesFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 11),
    _AcPMNetUtilKBytesFullDayAverage_Type()
)
acPMNetUtilKBytesFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesFullDayAverage.setStatus("current")


class _AcPMNetUtilKBytesTotal_Type(Integer32):
    """Custom type acPMNetUtilKBytesTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNetUtilKBytesTotal_Type.__name__ = "Integer32"
_AcPMNetUtilKBytesTotal_Object = MibTableColumn
acPMNetUtilKBytesTotal = _AcPMNetUtilKBytesTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 1, 1, 12),
    _AcPMNetUtilKBytesTotal_Type()
)
acPMNetUtilKBytesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilKBytesTotal.setStatus("current")
_AcPMNetUtilPacketsTable_Object = MibTable
acPMNetUtilPacketsTable = _AcPMNetUtilPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2)
)
if mibBuilder.loadTexts:
    acPMNetUtilPacketsTable.setStatus("current")
_AcPMNetUtilPacketsEntry_Object = MibTableRow
acPMNetUtilPacketsEntry = _AcPMNetUtilPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1)
)
acPMNetUtilPacketsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNetUtilPacketsDirection"),
    (0, "AC-PM-System-MIB", "acPMNetUtilPacketsInterval"),
)
if mibBuilder.loadTexts:
    acPMNetUtilPacketsEntry.setStatus("current")


class _AcPMNetUtilPacketsDirection_Type(Integer32):
    """Custom type acPMNetUtilPacketsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 0))
    )


_AcPMNetUtilPacketsDirection_Type.__name__ = "Integer32"
_AcPMNetUtilPacketsDirection_Object = MibTableColumn
acPMNetUtilPacketsDirection = _AcPMNetUtilPacketsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 1),
    _AcPMNetUtilPacketsDirection_Type()
)
acPMNetUtilPacketsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsDirection.setStatus("current")


class _AcPMNetUtilPacketsInterval_Type(Unsigned32):
    """Custom type acPMNetUtilPacketsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNetUtilPacketsInterval_Type.__name__ = "Unsigned32"
_AcPMNetUtilPacketsInterval_Object = MibTableColumn
acPMNetUtilPacketsInterval = _AcPMNetUtilPacketsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 2),
    _AcPMNetUtilPacketsInterval_Type()
)
acPMNetUtilPacketsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsInterval.setStatus("current")
_AcPMNetUtilPacketsVal_Type = Gauge32
_AcPMNetUtilPacketsVal_Object = MibTableColumn
acPMNetUtilPacketsVal = _AcPMNetUtilPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 3),
    _AcPMNetUtilPacketsVal_Type()
)
acPMNetUtilPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsVal.setStatus("current")


class _AcPMNetUtilPacketsAverage_Type(Integer32):
    """Custom type acPMNetUtilPacketsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNetUtilPacketsAverage_Type.__name__ = "Integer32"
_AcPMNetUtilPacketsAverage_Object = MibTableColumn
acPMNetUtilPacketsAverage = _AcPMNetUtilPacketsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 4),
    _AcPMNetUtilPacketsAverage_Type()
)
acPMNetUtilPacketsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsAverage.setStatus("current")


class _AcPMNetUtilPacketsMax_Type(Integer32):
    """Custom type acPMNetUtilPacketsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNetUtilPacketsMax_Type.__name__ = "Integer32"
_AcPMNetUtilPacketsMax_Object = MibTableColumn
acPMNetUtilPacketsMax = _AcPMNetUtilPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 5),
    _AcPMNetUtilPacketsMax_Type()
)
acPMNetUtilPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsMax.setStatus("current")


class _AcPMNetUtilPacketsMin_Type(Integer32):
    """Custom type acPMNetUtilPacketsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNetUtilPacketsMin_Type.__name__ = "Integer32"
_AcPMNetUtilPacketsMin_Object = MibTableColumn
acPMNetUtilPacketsMin = _AcPMNetUtilPacketsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 6),
    _AcPMNetUtilPacketsMin_Type()
)
acPMNetUtilPacketsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsMin.setStatus("current")
_AcPMNetUtilPacketsVolume_Type = Counter32
_AcPMNetUtilPacketsVolume_Object = MibTableColumn
acPMNetUtilPacketsVolume = _AcPMNetUtilPacketsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 7),
    _AcPMNetUtilPacketsVolume_Type()
)
acPMNetUtilPacketsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsVolume.setStatus("current")


class _AcPMNetUtilPacketsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMNetUtilPacketsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNetUtilPacketsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMNetUtilPacketsTimeBelowLowThreshold_Object = MibTableColumn
acPMNetUtilPacketsTimeBelowLowThreshold = _AcPMNetUtilPacketsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 8),
    _AcPMNetUtilPacketsTimeBelowLowThreshold_Type()
)
acPMNetUtilPacketsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsTimeBelowLowThreshold.setStatus("current")


class _AcPMNetUtilPacketsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMNetUtilPacketsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNetUtilPacketsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMNetUtilPacketsTimeBetweenThresholds_Object = MibTableColumn
acPMNetUtilPacketsTimeBetweenThresholds = _AcPMNetUtilPacketsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 9),
    _AcPMNetUtilPacketsTimeBetweenThresholds_Type()
)
acPMNetUtilPacketsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsTimeBetweenThresholds.setStatus("current")


class _AcPMNetUtilPacketsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMNetUtilPacketsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNetUtilPacketsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMNetUtilPacketsTimeAboveHighThreshold_Object = MibTableColumn
acPMNetUtilPacketsTimeAboveHighThreshold = _AcPMNetUtilPacketsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 10),
    _AcPMNetUtilPacketsTimeAboveHighThreshold_Type()
)
acPMNetUtilPacketsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsTimeAboveHighThreshold.setStatus("current")


class _AcPMNetUtilPacketsFullDayAverage_Type(Integer32):
    """Custom type acPMNetUtilPacketsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNetUtilPacketsFullDayAverage_Type.__name__ = "Integer32"
_AcPMNetUtilPacketsFullDayAverage_Object = MibTableColumn
acPMNetUtilPacketsFullDayAverage = _AcPMNetUtilPacketsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 11),
    _AcPMNetUtilPacketsFullDayAverage_Type()
)
acPMNetUtilPacketsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsFullDayAverage.setStatus("current")


class _AcPMNetUtilPacketsTotal_Type(Integer32):
    """Custom type acPMNetUtilPacketsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNetUtilPacketsTotal_Type.__name__ = "Integer32"
_AcPMNetUtilPacketsTotal_Object = MibTableColumn
acPMNetUtilPacketsTotal = _AcPMNetUtilPacketsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 2, 1, 12),
    _AcPMNetUtilPacketsTotal_Type()
)
acPMNetUtilPacketsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilPacketsTotal.setStatus("current")
_AcPMNetUtilDiscardedPacketsTable_Object = MibTable
acPMNetUtilDiscardedPacketsTable = _AcPMNetUtilDiscardedPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 3)
)
if mibBuilder.loadTexts:
    acPMNetUtilDiscardedPacketsTable.setStatus("current")
_AcPMNetUtilDiscardedPacketsEntry_Object = MibTableRow
acPMNetUtilDiscardedPacketsEntry = _AcPMNetUtilDiscardedPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 3, 1)
)
acPMNetUtilDiscardedPacketsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNetUtilDiscardedPacketsInterval"),
)
if mibBuilder.loadTexts:
    acPMNetUtilDiscardedPacketsEntry.setStatus("current")


class _AcPMNetUtilDiscardedPacketsInterval_Type(Unsigned32):
    """Custom type acPMNetUtilDiscardedPacketsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNetUtilDiscardedPacketsInterval_Type.__name__ = "Unsigned32"
_AcPMNetUtilDiscardedPacketsInterval_Object = MibTableColumn
acPMNetUtilDiscardedPacketsInterval = _AcPMNetUtilDiscardedPacketsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 3, 1, 1),
    _AcPMNetUtilDiscardedPacketsInterval_Type()
)
acPMNetUtilDiscardedPacketsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNetUtilDiscardedPacketsInterval.setStatus("current")
_AcPMNetUtilDiscardedPacketsVal_Type = Counter32
_AcPMNetUtilDiscardedPacketsVal_Object = MibTableColumn
acPMNetUtilDiscardedPacketsVal = _AcPMNetUtilDiscardedPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 3, 1, 2),
    _AcPMNetUtilDiscardedPacketsVal_Type()
)
acPMNetUtilDiscardedPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilDiscardedPacketsVal.setStatus("current")


class _AcPMNetUtilDiscardedPacketsTotal_Type(Integer32):
    """Custom type acPMNetUtilDiscardedPacketsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNetUtilDiscardedPacketsTotal_Type.__name__ = "Integer32"
_AcPMNetUtilDiscardedPacketsTotal_Object = MibTableColumn
acPMNetUtilDiscardedPacketsTotal = _AcPMNetUtilDiscardedPacketsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 31, 3, 1, 3),
    _AcPMNetUtilDiscardedPacketsTotal_Type()
)
acPMNetUtilDiscardedPacketsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNetUtilDiscardedPacketsTotal.setStatus("current")
_AcPMSystemNetwork_ObjectIdentity = ObjectIdentity
acPMSystemNetwork = _AcPMSystemNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41)
)
_AcPMDhcpResponseTimeTable_Object = MibTable
acPMDhcpResponseTimeTable = _AcPMDhcpResponseTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1)
)
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeTable.setStatus("current")
_AcPMDhcpResponseTimeEntry_Object = MibTableRow
acPMDhcpResponseTimeEntry = _AcPMDhcpResponseTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1, 1)
)
acPMDhcpResponseTimeEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMDhcpResponseTimeInterval"),
)
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeEntry.setStatus("current")


class _AcPMDhcpResponseTimeInterval_Type(Unsigned32):
    """Custom type acPMDhcpResponseTimeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMDhcpResponseTimeInterval_Type.__name__ = "Unsigned32"
_AcPMDhcpResponseTimeInterval_Object = MibTableColumn
acPMDhcpResponseTimeInterval = _AcPMDhcpResponseTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1, 1, 1),
    _AcPMDhcpResponseTimeInterval_Type()
)
acPMDhcpResponseTimeInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeInterval.setStatus("current")
_AcPMDhcpResponseTimeVal_Type = Gauge32
_AcPMDhcpResponseTimeVal_Object = MibTableColumn
acPMDhcpResponseTimeVal = _AcPMDhcpResponseTimeVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1, 1, 2),
    _AcPMDhcpResponseTimeVal_Type()
)
acPMDhcpResponseTimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeVal.setStatus("current")


class _AcPMDhcpResponseTimeAverage_Type(Integer32):
    """Custom type acPMDhcpResponseTimeAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMDhcpResponseTimeAverage_Type.__name__ = "Integer32"
_AcPMDhcpResponseTimeAverage_Object = MibTableColumn
acPMDhcpResponseTimeAverage = _AcPMDhcpResponseTimeAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1, 1, 3),
    _AcPMDhcpResponseTimeAverage_Type()
)
acPMDhcpResponseTimeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeAverage.setStatus("current")


class _AcPMDhcpResponseTimeMax_Type(Integer32):
    """Custom type acPMDhcpResponseTimeMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMDhcpResponseTimeMax_Type.__name__ = "Integer32"
_AcPMDhcpResponseTimeMax_Object = MibTableColumn
acPMDhcpResponseTimeMax = _AcPMDhcpResponseTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1, 1, 4),
    _AcPMDhcpResponseTimeMax_Type()
)
acPMDhcpResponseTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeMax.setStatus("current")


class _AcPMDhcpResponseTimeMin_Type(Integer32):
    """Custom type acPMDhcpResponseTimeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMDhcpResponseTimeMin_Type.__name__ = "Integer32"
_AcPMDhcpResponseTimeMin_Object = MibTableColumn
acPMDhcpResponseTimeMin = _AcPMDhcpResponseTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1, 1, 5),
    _AcPMDhcpResponseTimeMin_Type()
)
acPMDhcpResponseTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeMin.setStatus("current")
_AcPMDhcpResponseTimeVolume_Type = Counter32
_AcPMDhcpResponseTimeVolume_Object = MibTableColumn
acPMDhcpResponseTimeVolume = _AcPMDhcpResponseTimeVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1, 1, 6),
    _AcPMDhcpResponseTimeVolume_Type()
)
acPMDhcpResponseTimeVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeVolume.setStatus("current")


class _AcPMDhcpResponseTimeTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMDhcpResponseTimeTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMDhcpResponseTimeTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMDhcpResponseTimeTimeBelowLowThreshold_Object = MibTableColumn
acPMDhcpResponseTimeTimeBelowLowThreshold = _AcPMDhcpResponseTimeTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1, 1, 7),
    _AcPMDhcpResponseTimeTimeBelowLowThreshold_Type()
)
acPMDhcpResponseTimeTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeTimeBelowLowThreshold.setStatus("current")


class _AcPMDhcpResponseTimeTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMDhcpResponseTimeTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMDhcpResponseTimeTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMDhcpResponseTimeTimeBetweenThresholds_Object = MibTableColumn
acPMDhcpResponseTimeTimeBetweenThresholds = _AcPMDhcpResponseTimeTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1, 1, 8),
    _AcPMDhcpResponseTimeTimeBetweenThresholds_Type()
)
acPMDhcpResponseTimeTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeTimeBetweenThresholds.setStatus("current")


class _AcPMDhcpResponseTimeTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMDhcpResponseTimeTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMDhcpResponseTimeTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMDhcpResponseTimeTimeAboveHighThreshold_Object = MibTableColumn
acPMDhcpResponseTimeTimeAboveHighThreshold = _AcPMDhcpResponseTimeTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1, 1, 9),
    _AcPMDhcpResponseTimeTimeAboveHighThreshold_Type()
)
acPMDhcpResponseTimeTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeTimeAboveHighThreshold.setStatus("current")


class _AcPMDhcpResponseTimeFullDayAverage_Type(Integer32):
    """Custom type acPMDhcpResponseTimeFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMDhcpResponseTimeFullDayAverage_Type.__name__ = "Integer32"
_AcPMDhcpResponseTimeFullDayAverage_Object = MibTableColumn
acPMDhcpResponseTimeFullDayAverage = _AcPMDhcpResponseTimeFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 1, 1, 10),
    _AcPMDhcpResponseTimeFullDayAverage_Type()
)
acPMDhcpResponseTimeFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDhcpResponseTimeFullDayAverage.setStatus("current")
_AcPMDhcpRequestTable_Object = MibTable
acPMDhcpRequestTable = _AcPMDhcpRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 2)
)
if mibBuilder.loadTexts:
    acPMDhcpRequestTable.setStatus("current")
_AcPMDhcpRequestEntry_Object = MibTableRow
acPMDhcpRequestEntry = _AcPMDhcpRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 2, 1)
)
acPMDhcpRequestEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMDhcpRequestInterval"),
)
if mibBuilder.loadTexts:
    acPMDhcpRequestEntry.setStatus("current")


class _AcPMDhcpRequestInterval_Type(Unsigned32):
    """Custom type acPMDhcpRequestInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMDhcpRequestInterval_Type.__name__ = "Unsigned32"
_AcPMDhcpRequestInterval_Object = MibTableColumn
acPMDhcpRequestInterval = _AcPMDhcpRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 2, 1, 1),
    _AcPMDhcpRequestInterval_Type()
)
acPMDhcpRequestInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMDhcpRequestInterval.setStatus("current")
_AcPMDhcpRequestVal_Type = Counter32
_AcPMDhcpRequestVal_Object = MibTableColumn
acPMDhcpRequestVal = _AcPMDhcpRequestVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 2, 1, 2),
    _AcPMDhcpRequestVal_Type()
)
acPMDhcpRequestVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDhcpRequestVal.setStatus("current")


class _AcPMDhcpRequestTotal_Type(Integer32):
    """Custom type acPMDhcpRequestTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMDhcpRequestTotal_Type.__name__ = "Integer32"
_AcPMDhcpRequestTotal_Object = MibTableColumn
acPMDhcpRequestTotal = _AcPMDhcpRequestTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 2, 1, 3),
    _AcPMDhcpRequestTotal_Type()
)
acPMDhcpRequestTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMDhcpRequestTotal.setStatus("current")
_AcPMStunQueryTable_Object = MibTable
acPMStunQueryTable = _AcPMStunQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 3)
)
if mibBuilder.loadTexts:
    acPMStunQueryTable.setStatus("current")
_AcPMStunQueryEntry_Object = MibTableRow
acPMStunQueryEntry = _AcPMStunQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 3, 1)
)
acPMStunQueryEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMStunQueryInterval"),
)
if mibBuilder.loadTexts:
    acPMStunQueryEntry.setStatus("current")


class _AcPMStunQueryInterval_Type(Unsigned32):
    """Custom type acPMStunQueryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMStunQueryInterval_Type.__name__ = "Unsigned32"
_AcPMStunQueryInterval_Object = MibTableColumn
acPMStunQueryInterval = _AcPMStunQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 3, 1, 1),
    _AcPMStunQueryInterval_Type()
)
acPMStunQueryInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMStunQueryInterval.setStatus("current")
_AcPMStunQueryVal_Type = Counter32
_AcPMStunQueryVal_Object = MibTableColumn
acPMStunQueryVal = _AcPMStunQueryVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 3, 1, 2),
    _AcPMStunQueryVal_Type()
)
acPMStunQueryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStunQueryVal.setStatus("current")
_AcPMStunDiscoveryTable_Object = MibTable
acPMStunDiscoveryTable = _AcPMStunDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 4)
)
if mibBuilder.loadTexts:
    acPMStunDiscoveryTable.setStatus("current")
_AcPMStunDiscoveryEntry_Object = MibTableRow
acPMStunDiscoveryEntry = _AcPMStunDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 4, 1)
)
acPMStunDiscoveryEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMStunDiscoveryInterval"),
)
if mibBuilder.loadTexts:
    acPMStunDiscoveryEntry.setStatus("current")


class _AcPMStunDiscoveryInterval_Type(Unsigned32):
    """Custom type acPMStunDiscoveryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMStunDiscoveryInterval_Type.__name__ = "Unsigned32"
_AcPMStunDiscoveryInterval_Object = MibTableColumn
acPMStunDiscoveryInterval = _AcPMStunDiscoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 4, 1, 1),
    _AcPMStunDiscoveryInterval_Type()
)
acPMStunDiscoveryInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMStunDiscoveryInterval.setStatus("current")
_AcPMStunDiscoveryVal_Type = Counter32
_AcPMStunDiscoveryVal_Object = MibTableColumn
acPMStunDiscoveryVal = _AcPMStunDiscoveryVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 4, 1, 2),
    _AcPMStunDiscoveryVal_Type()
)
acPMStunDiscoveryVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStunDiscoveryVal.setStatus("current")
_AcPMStunRetransmissionTable_Object = MibTable
acPMStunRetransmissionTable = _AcPMStunRetransmissionTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 5)
)
if mibBuilder.loadTexts:
    acPMStunRetransmissionTable.setStatus("current")
_AcPMStunRetransmissionEntry_Object = MibTableRow
acPMStunRetransmissionEntry = _AcPMStunRetransmissionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 5, 1)
)
acPMStunRetransmissionEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMStunRetransmissionInterval"),
)
if mibBuilder.loadTexts:
    acPMStunRetransmissionEntry.setStatus("current")


class _AcPMStunRetransmissionInterval_Type(Unsigned32):
    """Custom type acPMStunRetransmissionInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMStunRetransmissionInterval_Type.__name__ = "Unsigned32"
_AcPMStunRetransmissionInterval_Object = MibTableColumn
acPMStunRetransmissionInterval = _AcPMStunRetransmissionInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 5, 1, 1),
    _AcPMStunRetransmissionInterval_Type()
)
acPMStunRetransmissionInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMStunRetransmissionInterval.setStatus("current")
_AcPMStunRetransmissionVal_Type = Counter32
_AcPMStunRetransmissionVal_Object = MibTableColumn
acPMStunRetransmissionVal = _AcPMStunRetransmissionVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 41, 5, 1, 2),
    _AcPMStunRetransmissionVal_Type()
)
acPMStunRetransmissionVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMStunRetransmissionVal.setStatus("current")
_AcPMSystemSctp_ObjectIdentity = ObjectIdentity
acPMSystemSctp = _AcPMSystemSctp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51)
)
_AcPMSctpRcvBytesLastSecondTable_Object = MibTable
acPMSctpRcvBytesLastSecondTable = _AcPMSctpRcvBytesLastSecondTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 1)
)
if mibBuilder.loadTexts:
    acPMSctpRcvBytesLastSecondTable.setStatus("current")
_AcPMSctpRcvBytesLastSecondEntry_Object = MibTableRow
acPMSctpRcvBytesLastSecondEntry = _AcPMSctpRcvBytesLastSecondEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 1, 1)
)
acPMSctpRcvBytesLastSecondEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMSctpRcvBytesLastSecondInterval"),
)
if mibBuilder.loadTexts:
    acPMSctpRcvBytesLastSecondEntry.setStatus("current")


class _AcPMSctpRcvBytesLastSecondInterval_Type(Unsigned32):
    """Custom type acPMSctpRcvBytesLastSecondInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSctpRcvBytesLastSecondInterval_Type.__name__ = "Unsigned32"
_AcPMSctpRcvBytesLastSecondInterval_Object = MibTableColumn
acPMSctpRcvBytesLastSecondInterval = _AcPMSctpRcvBytesLastSecondInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 1, 1, 1),
    _AcPMSctpRcvBytesLastSecondInterval_Type()
)
acPMSctpRcvBytesLastSecondInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSctpRcvBytesLastSecondInterval.setStatus("current")
_AcPMSctpRcvBytesLastSecondVal_Type = Gauge32
_AcPMSctpRcvBytesLastSecondVal_Object = MibTableColumn
acPMSctpRcvBytesLastSecondVal = _AcPMSctpRcvBytesLastSecondVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 1, 1, 2),
    _AcPMSctpRcvBytesLastSecondVal_Type()
)
acPMSctpRcvBytesLastSecondVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRcvBytesLastSecondVal.setStatus("current")


class _AcPMSctpRcvBytesLastSecondAverage_Type(Integer32):
    """Custom type acPMSctpRcvBytesLastSecondAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRcvBytesLastSecondAverage_Type.__name__ = "Integer32"
_AcPMSctpRcvBytesLastSecondAverage_Object = MibTableColumn
acPMSctpRcvBytesLastSecondAverage = _AcPMSctpRcvBytesLastSecondAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 1, 1, 3),
    _AcPMSctpRcvBytesLastSecondAverage_Type()
)
acPMSctpRcvBytesLastSecondAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRcvBytesLastSecondAverage.setStatus("current")


class _AcPMSctpRcvBytesLastSecondMax_Type(Integer32):
    """Custom type acPMSctpRcvBytesLastSecondMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRcvBytesLastSecondMax_Type.__name__ = "Integer32"
_AcPMSctpRcvBytesLastSecondMax_Object = MibTableColumn
acPMSctpRcvBytesLastSecondMax = _AcPMSctpRcvBytesLastSecondMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 1, 1, 4),
    _AcPMSctpRcvBytesLastSecondMax_Type()
)
acPMSctpRcvBytesLastSecondMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRcvBytesLastSecondMax.setStatus("current")


class _AcPMSctpRcvBytesLastSecondMin_Type(Integer32):
    """Custom type acPMSctpRcvBytesLastSecondMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRcvBytesLastSecondMin_Type.__name__ = "Integer32"
_AcPMSctpRcvBytesLastSecondMin_Object = MibTableColumn
acPMSctpRcvBytesLastSecondMin = _AcPMSctpRcvBytesLastSecondMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 1, 1, 5),
    _AcPMSctpRcvBytesLastSecondMin_Type()
)
acPMSctpRcvBytesLastSecondMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRcvBytesLastSecondMin.setStatus("current")


class _AcPMSctpRcvBytesLastSecondFullDayAverage_Type(Integer32):
    """Custom type acPMSctpRcvBytesLastSecondFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRcvBytesLastSecondFullDayAverage_Type.__name__ = "Integer32"
_AcPMSctpRcvBytesLastSecondFullDayAverage_Object = MibTableColumn
acPMSctpRcvBytesLastSecondFullDayAverage = _AcPMSctpRcvBytesLastSecondFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 1, 1, 6),
    _AcPMSctpRcvBytesLastSecondFullDayAverage_Type()
)
acPMSctpRcvBytesLastSecondFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRcvBytesLastSecondFullDayAverage.setStatus("current")
_AcPMSctpSentBytesLastSecondTable_Object = MibTable
acPMSctpSentBytesLastSecondTable = _AcPMSctpSentBytesLastSecondTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 2)
)
if mibBuilder.loadTexts:
    acPMSctpSentBytesLastSecondTable.setStatus("current")
_AcPMSctpSentBytesLastSecondEntry_Object = MibTableRow
acPMSctpSentBytesLastSecondEntry = _AcPMSctpSentBytesLastSecondEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 2, 1)
)
acPMSctpSentBytesLastSecondEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMSctpSentBytesLastSecondInterval"),
)
if mibBuilder.loadTexts:
    acPMSctpSentBytesLastSecondEntry.setStatus("current")


class _AcPMSctpSentBytesLastSecondInterval_Type(Unsigned32):
    """Custom type acPMSctpSentBytesLastSecondInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSctpSentBytesLastSecondInterval_Type.__name__ = "Unsigned32"
_AcPMSctpSentBytesLastSecondInterval_Object = MibTableColumn
acPMSctpSentBytesLastSecondInterval = _AcPMSctpSentBytesLastSecondInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 2, 1, 1),
    _AcPMSctpSentBytesLastSecondInterval_Type()
)
acPMSctpSentBytesLastSecondInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSctpSentBytesLastSecondInterval.setStatus("current")
_AcPMSctpSentBytesLastSecondVal_Type = Gauge32
_AcPMSctpSentBytesLastSecondVal_Object = MibTableColumn
acPMSctpSentBytesLastSecondVal = _AcPMSctpSentBytesLastSecondVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 2, 1, 2),
    _AcPMSctpSentBytesLastSecondVal_Type()
)
acPMSctpSentBytesLastSecondVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpSentBytesLastSecondVal.setStatus("current")


class _AcPMSctpSentBytesLastSecondAverage_Type(Integer32):
    """Custom type acPMSctpSentBytesLastSecondAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpSentBytesLastSecondAverage_Type.__name__ = "Integer32"
_AcPMSctpSentBytesLastSecondAverage_Object = MibTableColumn
acPMSctpSentBytesLastSecondAverage = _AcPMSctpSentBytesLastSecondAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 2, 1, 3),
    _AcPMSctpSentBytesLastSecondAverage_Type()
)
acPMSctpSentBytesLastSecondAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpSentBytesLastSecondAverage.setStatus("current")


class _AcPMSctpSentBytesLastSecondMax_Type(Integer32):
    """Custom type acPMSctpSentBytesLastSecondMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpSentBytesLastSecondMax_Type.__name__ = "Integer32"
_AcPMSctpSentBytesLastSecondMax_Object = MibTableColumn
acPMSctpSentBytesLastSecondMax = _AcPMSctpSentBytesLastSecondMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 2, 1, 4),
    _AcPMSctpSentBytesLastSecondMax_Type()
)
acPMSctpSentBytesLastSecondMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpSentBytesLastSecondMax.setStatus("current")


class _AcPMSctpSentBytesLastSecondMin_Type(Integer32):
    """Custom type acPMSctpSentBytesLastSecondMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpSentBytesLastSecondMin_Type.__name__ = "Integer32"
_AcPMSctpSentBytesLastSecondMin_Object = MibTableColumn
acPMSctpSentBytesLastSecondMin = _AcPMSctpSentBytesLastSecondMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 2, 1, 5),
    _AcPMSctpSentBytesLastSecondMin_Type()
)
acPMSctpSentBytesLastSecondMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpSentBytesLastSecondMin.setStatus("current")


class _AcPMSctpSentBytesLastSecondFullDayAverage_Type(Integer32):
    """Custom type acPMSctpSentBytesLastSecondFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpSentBytesLastSecondFullDayAverage_Type.__name__ = "Integer32"
_AcPMSctpSentBytesLastSecondFullDayAverage_Object = MibTableColumn
acPMSctpSentBytesLastSecondFullDayAverage = _AcPMSctpSentBytesLastSecondFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 2, 1, 6),
    _AcPMSctpSentBytesLastSecondFullDayAverage_Type()
)
acPMSctpSentBytesLastSecondFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpSentBytesLastSecondFullDayAverage.setStatus("current")
_AcPMSctpRetransBytesTable_Object = MibTable
acPMSctpRetransBytesTable = _AcPMSctpRetransBytesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 3)
)
if mibBuilder.loadTexts:
    acPMSctpRetransBytesTable.setStatus("current")
_AcPMSctpRetransBytesEntry_Object = MibTableRow
acPMSctpRetransBytesEntry = _AcPMSctpRetransBytesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 3, 1)
)
acPMSctpRetransBytesEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMSctpRetransBytesInterval"),
)
if mibBuilder.loadTexts:
    acPMSctpRetransBytesEntry.setStatus("current")


class _AcPMSctpRetransBytesInterval_Type(Unsigned32):
    """Custom type acPMSctpRetransBytesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSctpRetransBytesInterval_Type.__name__ = "Unsigned32"
_AcPMSctpRetransBytesInterval_Object = MibTableColumn
acPMSctpRetransBytesInterval = _AcPMSctpRetransBytesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 3, 1, 1),
    _AcPMSctpRetransBytesInterval_Type()
)
acPMSctpRetransBytesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSctpRetransBytesInterval.setStatus("current")
_AcPMSctpRetransBytesVal_Type = Gauge32
_AcPMSctpRetransBytesVal_Object = MibTableColumn
acPMSctpRetransBytesVal = _AcPMSctpRetransBytesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 3, 1, 2),
    _AcPMSctpRetransBytesVal_Type()
)
acPMSctpRetransBytesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRetransBytesVal.setStatus("current")


class _AcPMSctpRetransBytesAverage_Type(Integer32):
    """Custom type acPMSctpRetransBytesAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRetransBytesAverage_Type.__name__ = "Integer32"
_AcPMSctpRetransBytesAverage_Object = MibTableColumn
acPMSctpRetransBytesAverage = _AcPMSctpRetransBytesAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 3, 1, 3),
    _AcPMSctpRetransBytesAverage_Type()
)
acPMSctpRetransBytesAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRetransBytesAverage.setStatus("current")


class _AcPMSctpRetransBytesMax_Type(Integer32):
    """Custom type acPMSctpRetransBytesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRetransBytesMax_Type.__name__ = "Integer32"
_AcPMSctpRetransBytesMax_Object = MibTableColumn
acPMSctpRetransBytesMax = _AcPMSctpRetransBytesMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 3, 1, 4),
    _AcPMSctpRetransBytesMax_Type()
)
acPMSctpRetransBytesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRetransBytesMax.setStatus("current")


class _AcPMSctpRetransBytesMin_Type(Integer32):
    """Custom type acPMSctpRetransBytesMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRetransBytesMin_Type.__name__ = "Integer32"
_AcPMSctpRetransBytesMin_Object = MibTableColumn
acPMSctpRetransBytesMin = _AcPMSctpRetransBytesMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 3, 1, 5),
    _AcPMSctpRetransBytesMin_Type()
)
acPMSctpRetransBytesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRetransBytesMin.setStatus("current")


class _AcPMSctpRetransBytesFullDayAverage_Type(Integer32):
    """Custom type acPMSctpRetransBytesFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRetransBytesFullDayAverage_Type.__name__ = "Integer32"
_AcPMSctpRetransBytesFullDayAverage_Object = MibTableColumn
acPMSctpRetransBytesFullDayAverage = _AcPMSctpRetransBytesFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 3, 1, 6),
    _AcPMSctpRetransBytesFullDayAverage_Type()
)
acPMSctpRetransBytesFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRetransBytesFullDayAverage.setStatus("current")
_AcPMSctpRetransAttemptsTable_Object = MibTable
acPMSctpRetransAttemptsTable = _AcPMSctpRetransAttemptsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 4)
)
if mibBuilder.loadTexts:
    acPMSctpRetransAttemptsTable.setStatus("current")
_AcPMSctpRetransAttemptsEntry_Object = MibTableRow
acPMSctpRetransAttemptsEntry = _AcPMSctpRetransAttemptsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 4, 1)
)
acPMSctpRetransAttemptsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMSctpRetransAttemptsInterval"),
)
if mibBuilder.loadTexts:
    acPMSctpRetransAttemptsEntry.setStatus("current")


class _AcPMSctpRetransAttemptsInterval_Type(Unsigned32):
    """Custom type acPMSctpRetransAttemptsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSctpRetransAttemptsInterval_Type.__name__ = "Unsigned32"
_AcPMSctpRetransAttemptsInterval_Object = MibTableColumn
acPMSctpRetransAttemptsInterval = _AcPMSctpRetransAttemptsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 4, 1, 1),
    _AcPMSctpRetransAttemptsInterval_Type()
)
acPMSctpRetransAttemptsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSctpRetransAttemptsInterval.setStatus("current")
_AcPMSctpRetransAttemptsVal_Type = Gauge32
_AcPMSctpRetransAttemptsVal_Object = MibTableColumn
acPMSctpRetransAttemptsVal = _AcPMSctpRetransAttemptsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 4, 1, 2),
    _AcPMSctpRetransAttemptsVal_Type()
)
acPMSctpRetransAttemptsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRetransAttemptsVal.setStatus("current")


class _AcPMSctpRetransAttemptsAverage_Type(Integer32):
    """Custom type acPMSctpRetransAttemptsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRetransAttemptsAverage_Type.__name__ = "Integer32"
_AcPMSctpRetransAttemptsAverage_Object = MibTableColumn
acPMSctpRetransAttemptsAverage = _AcPMSctpRetransAttemptsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 4, 1, 3),
    _AcPMSctpRetransAttemptsAverage_Type()
)
acPMSctpRetransAttemptsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRetransAttemptsAverage.setStatus("current")


class _AcPMSctpRetransAttemptsMax_Type(Integer32):
    """Custom type acPMSctpRetransAttemptsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRetransAttemptsMax_Type.__name__ = "Integer32"
_AcPMSctpRetransAttemptsMax_Object = MibTableColumn
acPMSctpRetransAttemptsMax = _AcPMSctpRetransAttemptsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 4, 1, 4),
    _AcPMSctpRetransAttemptsMax_Type()
)
acPMSctpRetransAttemptsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRetransAttemptsMax.setStatus("current")


class _AcPMSctpRetransAttemptsMin_Type(Integer32):
    """Custom type acPMSctpRetransAttemptsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRetransAttemptsMin_Type.__name__ = "Integer32"
_AcPMSctpRetransAttemptsMin_Object = MibTableColumn
acPMSctpRetransAttemptsMin = _AcPMSctpRetransAttemptsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 4, 1, 5),
    _AcPMSctpRetransAttemptsMin_Type()
)
acPMSctpRetransAttemptsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRetransAttemptsMin.setStatus("current")


class _AcPMSctpRetransAttemptsFullDayAverage_Type(Integer32):
    """Custom type acPMSctpRetransAttemptsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSctpRetransAttemptsFullDayAverage_Type.__name__ = "Integer32"
_AcPMSctpRetransAttemptsFullDayAverage_Object = MibTableColumn
acPMSctpRetransAttemptsFullDayAverage = _AcPMSctpRetransAttemptsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 51, 4, 1, 6),
    _AcPMSctpRetransAttemptsFullDayAverage_Type()
)
acPMSctpRetransAttemptsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSctpRetransAttemptsFullDayAverage.setStatus("current")
_AcPMSystemSecurity_ObjectIdentity = ObjectIdentity
acPMSystemSecurity = _AcPMSystemSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 61)
)
_AcPMIPsecCurrentSAsTable_Object = MibTable
acPMIPsecCurrentSAsTable = _AcPMIPsecCurrentSAsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 61, 1)
)
if mibBuilder.loadTexts:
    acPMIPsecCurrentSAsTable.setStatus("current")
_AcPMIPsecCurrentSAsEntry_Object = MibTableRow
acPMIPsecCurrentSAsEntry = _AcPMIPsecCurrentSAsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 61, 1, 1)
)
acPMIPsecCurrentSAsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMIPsecCurrentSAsInterval"),
)
if mibBuilder.loadTexts:
    acPMIPsecCurrentSAsEntry.setStatus("current")


class _AcPMIPsecCurrentSAsInterval_Type(Unsigned32):
    """Custom type acPMIPsecCurrentSAsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIPsecCurrentSAsInterval_Type.__name__ = "Unsigned32"
_AcPMIPsecCurrentSAsInterval_Object = MibTableColumn
acPMIPsecCurrentSAsInterval = _AcPMIPsecCurrentSAsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 61, 1, 1, 1),
    _AcPMIPsecCurrentSAsInterval_Type()
)
acPMIPsecCurrentSAsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIPsecCurrentSAsInterval.setStatus("current")
_AcPMIPsecCurrentSAsVal_Type = Gauge32
_AcPMIPsecCurrentSAsVal_Object = MibTableColumn
acPMIPsecCurrentSAsVal = _AcPMIPsecCurrentSAsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 61, 1, 1, 2),
    _AcPMIPsecCurrentSAsVal_Type()
)
acPMIPsecCurrentSAsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIPsecCurrentSAsVal.setStatus("current")


class _AcPMIPsecCurrentSAsAverage_Type(Integer32):
    """Custom type acPMIPsecCurrentSAsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIPsecCurrentSAsAverage_Type.__name__ = "Integer32"
_AcPMIPsecCurrentSAsAverage_Object = MibTableColumn
acPMIPsecCurrentSAsAverage = _AcPMIPsecCurrentSAsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 61, 1, 1, 3),
    _AcPMIPsecCurrentSAsAverage_Type()
)
acPMIPsecCurrentSAsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIPsecCurrentSAsAverage.setStatus("current")


class _AcPMIPsecCurrentSAsMax_Type(Integer32):
    """Custom type acPMIPsecCurrentSAsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIPsecCurrentSAsMax_Type.__name__ = "Integer32"
_AcPMIPsecCurrentSAsMax_Object = MibTableColumn
acPMIPsecCurrentSAsMax = _AcPMIPsecCurrentSAsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 61, 1, 1, 4),
    _AcPMIPsecCurrentSAsMax_Type()
)
acPMIPsecCurrentSAsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIPsecCurrentSAsMax.setStatus("current")


class _AcPMIPsecCurrentSAsMin_Type(Integer32):
    """Custom type acPMIPsecCurrentSAsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIPsecCurrentSAsMin_Type.__name__ = "Integer32"
_AcPMIPsecCurrentSAsMin_Object = MibTableColumn
acPMIPsecCurrentSAsMin = _AcPMIPsecCurrentSAsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 61, 1, 1, 5),
    _AcPMIPsecCurrentSAsMin_Type()
)
acPMIPsecCurrentSAsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIPsecCurrentSAsMin.setStatus("current")


class _AcPMIPsecCurrentSAsFullDayAverage_Type(Integer32):
    """Custom type acPMIPsecCurrentSAsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIPsecCurrentSAsFullDayAverage_Type.__name__ = "Integer32"
_AcPMIPsecCurrentSAsFullDayAverage_Object = MibTableColumn
acPMIPsecCurrentSAsFullDayAverage = _AcPMIPsecCurrentSAsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 61, 1, 1, 6),
    _AcPMIPsecCurrentSAsFullDayAverage_Type()
)
acPMIPsecCurrentSAsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIPsecCurrentSAsFullDayAverage.setStatus("current")


class _AcPMIPsecCurrentSAsTotal_Type(Integer32):
    """Custom type acPMIPsecCurrentSAsTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIPsecCurrentSAsTotal_Type.__name__ = "Integer32"
_AcPMIPsecCurrentSAsTotal_Object = MibTableColumn
acPMIPsecCurrentSAsTotal = _AcPMIPsecCurrentSAsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 61, 1, 1, 7),
    _AcPMIPsecCurrentSAsTotal_Type()
)
acPMIPsecCurrentSAsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIPsecCurrentSAsTotal.setStatus("current")
_AcPMSystemMulticast_ObjectIdentity = ObjectIdentity
acPMSystemMulticast = _AcPMSystemMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71)
)
_AcPMMulticastIPPacketsReceivedTable_Object = MibTable
acPMMulticastIPPacketsReceivedTable = _AcPMMulticastIPPacketsReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 1)
)
if mibBuilder.loadTexts:
    acPMMulticastIPPacketsReceivedTable.setStatus("current")
_AcPMMulticastIPPacketsReceivedEntry_Object = MibTableRow
acPMMulticastIPPacketsReceivedEntry = _AcPMMulticastIPPacketsReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 1, 1)
)
acPMMulticastIPPacketsReceivedEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMMulticastIPPacketsReceivedInterval"),
)
if mibBuilder.loadTexts:
    acPMMulticastIPPacketsReceivedEntry.setStatus("current")


class _AcPMMulticastIPPacketsReceivedInterval_Type(Unsigned32):
    """Custom type acPMMulticastIPPacketsReceivedInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMulticastIPPacketsReceivedInterval_Type.__name__ = "Unsigned32"
_AcPMMulticastIPPacketsReceivedInterval_Object = MibTableColumn
acPMMulticastIPPacketsReceivedInterval = _AcPMMulticastIPPacketsReceivedInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 1, 1, 1),
    _AcPMMulticastIPPacketsReceivedInterval_Type()
)
acPMMulticastIPPacketsReceivedInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMulticastIPPacketsReceivedInterval.setStatus("current")
_AcPMMulticastIPPacketsReceivedVal_Type = Counter32
_AcPMMulticastIPPacketsReceivedVal_Object = MibTableColumn
acPMMulticastIPPacketsReceivedVal = _AcPMMulticastIPPacketsReceivedVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 1, 1, 2),
    _AcPMMulticastIPPacketsReceivedVal_Type()
)
acPMMulticastIPPacketsReceivedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastIPPacketsReceivedVal.setStatus("current")


class _AcPMMulticastIPPacketsReceivedAverage_Type(Integer32):
    """Custom type acPMMulticastIPPacketsReceivedAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastIPPacketsReceivedAverage_Type.__name__ = "Integer32"
_AcPMMulticastIPPacketsReceivedAverage_Object = MibTableColumn
acPMMulticastIPPacketsReceivedAverage = _AcPMMulticastIPPacketsReceivedAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 1, 1, 3),
    _AcPMMulticastIPPacketsReceivedAverage_Type()
)
acPMMulticastIPPacketsReceivedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastIPPacketsReceivedAverage.setStatus("current")


class _AcPMMulticastIPPacketsReceivedMax_Type(Integer32):
    """Custom type acPMMulticastIPPacketsReceivedMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastIPPacketsReceivedMax_Type.__name__ = "Integer32"
_AcPMMulticastIPPacketsReceivedMax_Object = MibTableColumn
acPMMulticastIPPacketsReceivedMax = _AcPMMulticastIPPacketsReceivedMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 1, 1, 4),
    _AcPMMulticastIPPacketsReceivedMax_Type()
)
acPMMulticastIPPacketsReceivedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastIPPacketsReceivedMax.setStatus("current")


class _AcPMMulticastIPPacketsReceivedMin_Type(Integer32):
    """Custom type acPMMulticastIPPacketsReceivedMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastIPPacketsReceivedMin_Type.__name__ = "Integer32"
_AcPMMulticastIPPacketsReceivedMin_Object = MibTableColumn
acPMMulticastIPPacketsReceivedMin = _AcPMMulticastIPPacketsReceivedMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 1, 1, 5),
    _AcPMMulticastIPPacketsReceivedMin_Type()
)
acPMMulticastIPPacketsReceivedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastIPPacketsReceivedMin.setStatus("current")


class _AcPMMulticastIPPacketsReceivedFullDayAverage_Type(Integer32):
    """Custom type acPMMulticastIPPacketsReceivedFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastIPPacketsReceivedFullDayAverage_Type.__name__ = "Integer32"
_AcPMMulticastIPPacketsReceivedFullDayAverage_Object = MibTableColumn
acPMMulticastIPPacketsReceivedFullDayAverage = _AcPMMulticastIPPacketsReceivedFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 1, 1, 6),
    _AcPMMulticastIPPacketsReceivedFullDayAverage_Type()
)
acPMMulticastIPPacketsReceivedFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastIPPacketsReceivedFullDayAverage.setStatus("current")
_AcPMMulticastUDPPacketsReceivedTable_Object = MibTable
acPMMulticastUDPPacketsReceivedTable = _AcPMMulticastUDPPacketsReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 2)
)
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsReceivedTable.setStatus("current")
_AcPMMulticastUDPPacketsReceivedEntry_Object = MibTableRow
acPMMulticastUDPPacketsReceivedEntry = _AcPMMulticastUDPPacketsReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 2, 1)
)
acPMMulticastUDPPacketsReceivedEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMMulticastUDPPacketsReceivedInterval"),
)
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsReceivedEntry.setStatus("current")


class _AcPMMulticastUDPPacketsReceivedInterval_Type(Unsigned32):
    """Custom type acPMMulticastUDPPacketsReceivedInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMulticastUDPPacketsReceivedInterval_Type.__name__ = "Unsigned32"
_AcPMMulticastUDPPacketsReceivedInterval_Object = MibTableColumn
acPMMulticastUDPPacketsReceivedInterval = _AcPMMulticastUDPPacketsReceivedInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 2, 1, 1),
    _AcPMMulticastUDPPacketsReceivedInterval_Type()
)
acPMMulticastUDPPacketsReceivedInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsReceivedInterval.setStatus("current")
_AcPMMulticastUDPPacketsReceivedVal_Type = Counter32
_AcPMMulticastUDPPacketsReceivedVal_Object = MibTableColumn
acPMMulticastUDPPacketsReceivedVal = _AcPMMulticastUDPPacketsReceivedVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 2, 1, 2),
    _AcPMMulticastUDPPacketsReceivedVal_Type()
)
acPMMulticastUDPPacketsReceivedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsReceivedVal.setStatus("current")


class _AcPMMulticastUDPPacketsReceivedAverage_Type(Integer32):
    """Custom type acPMMulticastUDPPacketsReceivedAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastUDPPacketsReceivedAverage_Type.__name__ = "Integer32"
_AcPMMulticastUDPPacketsReceivedAverage_Object = MibTableColumn
acPMMulticastUDPPacketsReceivedAverage = _AcPMMulticastUDPPacketsReceivedAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 2, 1, 3),
    _AcPMMulticastUDPPacketsReceivedAverage_Type()
)
acPMMulticastUDPPacketsReceivedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsReceivedAverage.setStatus("current")


class _AcPMMulticastUDPPacketsReceivedMax_Type(Integer32):
    """Custom type acPMMulticastUDPPacketsReceivedMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastUDPPacketsReceivedMax_Type.__name__ = "Integer32"
_AcPMMulticastUDPPacketsReceivedMax_Object = MibTableColumn
acPMMulticastUDPPacketsReceivedMax = _AcPMMulticastUDPPacketsReceivedMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 2, 1, 4),
    _AcPMMulticastUDPPacketsReceivedMax_Type()
)
acPMMulticastUDPPacketsReceivedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsReceivedMax.setStatus("current")


class _AcPMMulticastUDPPacketsReceivedMin_Type(Integer32):
    """Custom type acPMMulticastUDPPacketsReceivedMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastUDPPacketsReceivedMin_Type.__name__ = "Integer32"
_AcPMMulticastUDPPacketsReceivedMin_Object = MibTableColumn
acPMMulticastUDPPacketsReceivedMin = _AcPMMulticastUDPPacketsReceivedMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 2, 1, 5),
    _AcPMMulticastUDPPacketsReceivedMin_Type()
)
acPMMulticastUDPPacketsReceivedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsReceivedMin.setStatus("current")


class _AcPMMulticastUDPPacketsReceivedFullDayAverage_Type(Integer32):
    """Custom type acPMMulticastUDPPacketsReceivedFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastUDPPacketsReceivedFullDayAverage_Type.__name__ = "Integer32"
_AcPMMulticastUDPPacketsReceivedFullDayAverage_Object = MibTableColumn
acPMMulticastUDPPacketsReceivedFullDayAverage = _AcPMMulticastUDPPacketsReceivedFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 2, 1, 6),
    _AcPMMulticastUDPPacketsReceivedFullDayAverage_Type()
)
acPMMulticastUDPPacketsReceivedFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsReceivedFullDayAverage.setStatus("current")
_AcPMMulticastUDPPacketsRejectedTable_Object = MibTable
acPMMulticastUDPPacketsRejectedTable = _AcPMMulticastUDPPacketsRejectedTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 3)
)
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsRejectedTable.setStatus("current")
_AcPMMulticastUDPPacketsRejectedEntry_Object = MibTableRow
acPMMulticastUDPPacketsRejectedEntry = _AcPMMulticastUDPPacketsRejectedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 3, 1)
)
acPMMulticastUDPPacketsRejectedEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMMulticastUDPPacketsRejectedInterval"),
)
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsRejectedEntry.setStatus("current")


class _AcPMMulticastUDPPacketsRejectedInterval_Type(Unsigned32):
    """Custom type acPMMulticastUDPPacketsRejectedInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMulticastUDPPacketsRejectedInterval_Type.__name__ = "Unsigned32"
_AcPMMulticastUDPPacketsRejectedInterval_Object = MibTableColumn
acPMMulticastUDPPacketsRejectedInterval = _AcPMMulticastUDPPacketsRejectedInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 3, 1, 1),
    _AcPMMulticastUDPPacketsRejectedInterval_Type()
)
acPMMulticastUDPPacketsRejectedInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsRejectedInterval.setStatus("current")
_AcPMMulticastUDPPacketsRejectedVal_Type = Counter32
_AcPMMulticastUDPPacketsRejectedVal_Object = MibTableColumn
acPMMulticastUDPPacketsRejectedVal = _AcPMMulticastUDPPacketsRejectedVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 3, 1, 2),
    _AcPMMulticastUDPPacketsRejectedVal_Type()
)
acPMMulticastUDPPacketsRejectedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsRejectedVal.setStatus("current")


class _AcPMMulticastUDPPacketsRejectedAverage_Type(Integer32):
    """Custom type acPMMulticastUDPPacketsRejectedAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastUDPPacketsRejectedAverage_Type.__name__ = "Integer32"
_AcPMMulticastUDPPacketsRejectedAverage_Object = MibTableColumn
acPMMulticastUDPPacketsRejectedAverage = _AcPMMulticastUDPPacketsRejectedAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 3, 1, 3),
    _AcPMMulticastUDPPacketsRejectedAverage_Type()
)
acPMMulticastUDPPacketsRejectedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsRejectedAverage.setStatus("current")


class _AcPMMulticastUDPPacketsRejectedMax_Type(Integer32):
    """Custom type acPMMulticastUDPPacketsRejectedMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastUDPPacketsRejectedMax_Type.__name__ = "Integer32"
_AcPMMulticastUDPPacketsRejectedMax_Object = MibTableColumn
acPMMulticastUDPPacketsRejectedMax = _AcPMMulticastUDPPacketsRejectedMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 3, 1, 4),
    _AcPMMulticastUDPPacketsRejectedMax_Type()
)
acPMMulticastUDPPacketsRejectedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsRejectedMax.setStatus("current")


class _AcPMMulticastUDPPacketsRejectedMin_Type(Integer32):
    """Custom type acPMMulticastUDPPacketsRejectedMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastUDPPacketsRejectedMin_Type.__name__ = "Integer32"
_AcPMMulticastUDPPacketsRejectedMin_Object = MibTableColumn
acPMMulticastUDPPacketsRejectedMin = _AcPMMulticastUDPPacketsRejectedMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 3, 1, 5),
    _AcPMMulticastUDPPacketsRejectedMin_Type()
)
acPMMulticastUDPPacketsRejectedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsRejectedMin.setStatus("current")


class _AcPMMulticastUDPPacketsRejectedFullDayAverage_Type(Integer32):
    """Custom type acPMMulticastUDPPacketsRejectedFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastUDPPacketsRejectedFullDayAverage_Type.__name__ = "Integer32"
_AcPMMulticastUDPPacketsRejectedFullDayAverage_Object = MibTableColumn
acPMMulticastUDPPacketsRejectedFullDayAverage = _AcPMMulticastUDPPacketsRejectedFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 3, 1, 6),
    _AcPMMulticastUDPPacketsRejectedFullDayAverage_Type()
)
acPMMulticastUDPPacketsRejectedFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastUDPPacketsRejectedFullDayAverage.setStatus("current")
_AcPMMulticastIGMPPacketsReceivedTable_Object = MibTable
acPMMulticastIGMPPacketsReceivedTable = _AcPMMulticastIGMPPacketsReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 4)
)
if mibBuilder.loadTexts:
    acPMMulticastIGMPPacketsReceivedTable.setStatus("current")
_AcPMMulticastIGMPPacketsReceivedEntry_Object = MibTableRow
acPMMulticastIGMPPacketsReceivedEntry = _AcPMMulticastIGMPPacketsReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 4, 1)
)
acPMMulticastIGMPPacketsReceivedEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMMulticastIGMPPacketsReceivedInterval"),
)
if mibBuilder.loadTexts:
    acPMMulticastIGMPPacketsReceivedEntry.setStatus("current")


class _AcPMMulticastIGMPPacketsReceivedInterval_Type(Unsigned32):
    """Custom type acPMMulticastIGMPPacketsReceivedInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMulticastIGMPPacketsReceivedInterval_Type.__name__ = "Unsigned32"
_AcPMMulticastIGMPPacketsReceivedInterval_Object = MibTableColumn
acPMMulticastIGMPPacketsReceivedInterval = _AcPMMulticastIGMPPacketsReceivedInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 4, 1, 1),
    _AcPMMulticastIGMPPacketsReceivedInterval_Type()
)
acPMMulticastIGMPPacketsReceivedInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMulticastIGMPPacketsReceivedInterval.setStatus("current")
_AcPMMulticastIGMPPacketsReceivedVal_Type = Counter32
_AcPMMulticastIGMPPacketsReceivedVal_Object = MibTableColumn
acPMMulticastIGMPPacketsReceivedVal = _AcPMMulticastIGMPPacketsReceivedVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 4, 1, 2),
    _AcPMMulticastIGMPPacketsReceivedVal_Type()
)
acPMMulticastIGMPPacketsReceivedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastIGMPPacketsReceivedVal.setStatus("current")


class _AcPMMulticastIGMPPacketsReceivedAverage_Type(Integer32):
    """Custom type acPMMulticastIGMPPacketsReceivedAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastIGMPPacketsReceivedAverage_Type.__name__ = "Integer32"
_AcPMMulticastIGMPPacketsReceivedAverage_Object = MibTableColumn
acPMMulticastIGMPPacketsReceivedAverage = _AcPMMulticastIGMPPacketsReceivedAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 4, 1, 3),
    _AcPMMulticastIGMPPacketsReceivedAverage_Type()
)
acPMMulticastIGMPPacketsReceivedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastIGMPPacketsReceivedAverage.setStatus("current")


class _AcPMMulticastIGMPPacketsReceivedMax_Type(Integer32):
    """Custom type acPMMulticastIGMPPacketsReceivedMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastIGMPPacketsReceivedMax_Type.__name__ = "Integer32"
_AcPMMulticastIGMPPacketsReceivedMax_Object = MibTableColumn
acPMMulticastIGMPPacketsReceivedMax = _AcPMMulticastIGMPPacketsReceivedMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 4, 1, 4),
    _AcPMMulticastIGMPPacketsReceivedMax_Type()
)
acPMMulticastIGMPPacketsReceivedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastIGMPPacketsReceivedMax.setStatus("current")


class _AcPMMulticastIGMPPacketsReceivedMin_Type(Integer32):
    """Custom type acPMMulticastIGMPPacketsReceivedMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastIGMPPacketsReceivedMin_Type.__name__ = "Integer32"
_AcPMMulticastIGMPPacketsReceivedMin_Object = MibTableColumn
acPMMulticastIGMPPacketsReceivedMin = _AcPMMulticastIGMPPacketsReceivedMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 4, 1, 5),
    _AcPMMulticastIGMPPacketsReceivedMin_Type()
)
acPMMulticastIGMPPacketsReceivedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastIGMPPacketsReceivedMin.setStatus("current")


class _AcPMMulticastIGMPPacketsReceivedFullDayAverage_Type(Integer32):
    """Custom type acPMMulticastIGMPPacketsReceivedFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMulticastIGMPPacketsReceivedFullDayAverage_Type.__name__ = "Integer32"
_AcPMMulticastIGMPPacketsReceivedFullDayAverage_Object = MibTableColumn
acPMMulticastIGMPPacketsReceivedFullDayAverage = _AcPMMulticastIGMPPacketsReceivedFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 4, 1, 6),
    _AcPMMulticastIGMPPacketsReceivedFullDayAverage_Type()
)
acPMMulticastIGMPPacketsReceivedFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMulticastIGMPPacketsReceivedFullDayAverage.setStatus("current")
_AcPMIGMPGeneralQueryReceivedTable_Object = MibTable
acPMIGMPGeneralQueryReceivedTable = _AcPMIGMPGeneralQueryReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 5)
)
if mibBuilder.loadTexts:
    acPMIGMPGeneralQueryReceivedTable.setStatus("current")
_AcPMIGMPGeneralQueryReceivedEntry_Object = MibTableRow
acPMIGMPGeneralQueryReceivedEntry = _AcPMIGMPGeneralQueryReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 5, 1)
)
acPMIGMPGeneralQueryReceivedEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMIGMPGeneralQueryReceivedInterval"),
)
if mibBuilder.loadTexts:
    acPMIGMPGeneralQueryReceivedEntry.setStatus("current")


class _AcPMIGMPGeneralQueryReceivedInterval_Type(Unsigned32):
    """Custom type acPMIGMPGeneralQueryReceivedInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIGMPGeneralQueryReceivedInterval_Type.__name__ = "Unsigned32"
_AcPMIGMPGeneralQueryReceivedInterval_Object = MibTableColumn
acPMIGMPGeneralQueryReceivedInterval = _AcPMIGMPGeneralQueryReceivedInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 5, 1, 1),
    _AcPMIGMPGeneralQueryReceivedInterval_Type()
)
acPMIGMPGeneralQueryReceivedInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIGMPGeneralQueryReceivedInterval.setStatus("current")
_AcPMIGMPGeneralQueryReceivedVal_Type = Counter32
_AcPMIGMPGeneralQueryReceivedVal_Object = MibTableColumn
acPMIGMPGeneralQueryReceivedVal = _AcPMIGMPGeneralQueryReceivedVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 5, 1, 2),
    _AcPMIGMPGeneralQueryReceivedVal_Type()
)
acPMIGMPGeneralQueryReceivedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPGeneralQueryReceivedVal.setStatus("current")


class _AcPMIGMPGeneralQueryReceivedAverage_Type(Integer32):
    """Custom type acPMIGMPGeneralQueryReceivedAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPGeneralQueryReceivedAverage_Type.__name__ = "Integer32"
_AcPMIGMPGeneralQueryReceivedAverage_Object = MibTableColumn
acPMIGMPGeneralQueryReceivedAverage = _AcPMIGMPGeneralQueryReceivedAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 5, 1, 3),
    _AcPMIGMPGeneralQueryReceivedAverage_Type()
)
acPMIGMPGeneralQueryReceivedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPGeneralQueryReceivedAverage.setStatus("current")


class _AcPMIGMPGeneralQueryReceivedMax_Type(Integer32):
    """Custom type acPMIGMPGeneralQueryReceivedMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPGeneralQueryReceivedMax_Type.__name__ = "Integer32"
_AcPMIGMPGeneralQueryReceivedMax_Object = MibTableColumn
acPMIGMPGeneralQueryReceivedMax = _AcPMIGMPGeneralQueryReceivedMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 5, 1, 4),
    _AcPMIGMPGeneralQueryReceivedMax_Type()
)
acPMIGMPGeneralQueryReceivedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPGeneralQueryReceivedMax.setStatus("current")


class _AcPMIGMPGeneralQueryReceivedMin_Type(Integer32):
    """Custom type acPMIGMPGeneralQueryReceivedMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPGeneralQueryReceivedMin_Type.__name__ = "Integer32"
_AcPMIGMPGeneralQueryReceivedMin_Object = MibTableColumn
acPMIGMPGeneralQueryReceivedMin = _AcPMIGMPGeneralQueryReceivedMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 5, 1, 5),
    _AcPMIGMPGeneralQueryReceivedMin_Type()
)
acPMIGMPGeneralQueryReceivedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPGeneralQueryReceivedMin.setStatus("current")


class _AcPMIGMPGeneralQueryReceivedFullDayAverage_Type(Integer32):
    """Custom type acPMIGMPGeneralQueryReceivedFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPGeneralQueryReceivedFullDayAverage_Type.__name__ = "Integer32"
_AcPMIGMPGeneralQueryReceivedFullDayAverage_Object = MibTableColumn
acPMIGMPGeneralQueryReceivedFullDayAverage = _AcPMIGMPGeneralQueryReceivedFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 5, 1, 6),
    _AcPMIGMPGeneralQueryReceivedFullDayAverage_Type()
)
acPMIGMPGeneralQueryReceivedFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPGeneralQueryReceivedFullDayAverage.setStatus("current")
_AcPMIGMPSpecificQueryReceivedTable_Object = MibTable
acPMIGMPSpecificQueryReceivedTable = _AcPMIGMPSpecificQueryReceivedTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 6)
)
if mibBuilder.loadTexts:
    acPMIGMPSpecificQueryReceivedTable.setStatus("current")
_AcPMIGMPSpecificQueryReceivedEntry_Object = MibTableRow
acPMIGMPSpecificQueryReceivedEntry = _AcPMIGMPSpecificQueryReceivedEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 6, 1)
)
acPMIGMPSpecificQueryReceivedEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMIGMPSpecificQueryReceivedInterval"),
)
if mibBuilder.loadTexts:
    acPMIGMPSpecificQueryReceivedEntry.setStatus("current")


class _AcPMIGMPSpecificQueryReceivedInterval_Type(Unsigned32):
    """Custom type acPMIGMPSpecificQueryReceivedInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIGMPSpecificQueryReceivedInterval_Type.__name__ = "Unsigned32"
_AcPMIGMPSpecificQueryReceivedInterval_Object = MibTableColumn
acPMIGMPSpecificQueryReceivedInterval = _AcPMIGMPSpecificQueryReceivedInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 6, 1, 1),
    _AcPMIGMPSpecificQueryReceivedInterval_Type()
)
acPMIGMPSpecificQueryReceivedInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIGMPSpecificQueryReceivedInterval.setStatus("current")
_AcPMIGMPSpecificQueryReceivedVal_Type = Counter32
_AcPMIGMPSpecificQueryReceivedVal_Object = MibTableColumn
acPMIGMPSpecificQueryReceivedVal = _AcPMIGMPSpecificQueryReceivedVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 6, 1, 2),
    _AcPMIGMPSpecificQueryReceivedVal_Type()
)
acPMIGMPSpecificQueryReceivedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPSpecificQueryReceivedVal.setStatus("current")


class _AcPMIGMPSpecificQueryReceivedAverage_Type(Integer32):
    """Custom type acPMIGMPSpecificQueryReceivedAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPSpecificQueryReceivedAverage_Type.__name__ = "Integer32"
_AcPMIGMPSpecificQueryReceivedAverage_Object = MibTableColumn
acPMIGMPSpecificQueryReceivedAverage = _AcPMIGMPSpecificQueryReceivedAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 6, 1, 3),
    _AcPMIGMPSpecificQueryReceivedAverage_Type()
)
acPMIGMPSpecificQueryReceivedAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPSpecificQueryReceivedAverage.setStatus("current")


class _AcPMIGMPSpecificQueryReceivedMax_Type(Integer32):
    """Custom type acPMIGMPSpecificQueryReceivedMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPSpecificQueryReceivedMax_Type.__name__ = "Integer32"
_AcPMIGMPSpecificQueryReceivedMax_Object = MibTableColumn
acPMIGMPSpecificQueryReceivedMax = _AcPMIGMPSpecificQueryReceivedMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 6, 1, 4),
    _AcPMIGMPSpecificQueryReceivedMax_Type()
)
acPMIGMPSpecificQueryReceivedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPSpecificQueryReceivedMax.setStatus("current")


class _AcPMIGMPSpecificQueryReceivedMin_Type(Integer32):
    """Custom type acPMIGMPSpecificQueryReceivedMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPSpecificQueryReceivedMin_Type.__name__ = "Integer32"
_AcPMIGMPSpecificQueryReceivedMin_Object = MibTableColumn
acPMIGMPSpecificQueryReceivedMin = _AcPMIGMPSpecificQueryReceivedMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 6, 1, 5),
    _AcPMIGMPSpecificQueryReceivedMin_Type()
)
acPMIGMPSpecificQueryReceivedMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPSpecificQueryReceivedMin.setStatus("current")


class _AcPMIGMPSpecificQueryReceivedFullDayAverage_Type(Integer32):
    """Custom type acPMIGMPSpecificQueryReceivedFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPSpecificQueryReceivedFullDayAverage_Type.__name__ = "Integer32"
_AcPMIGMPSpecificQueryReceivedFullDayAverage_Object = MibTableColumn
acPMIGMPSpecificQueryReceivedFullDayAverage = _AcPMIGMPSpecificQueryReceivedFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 6, 1, 6),
    _AcPMIGMPSpecificQueryReceivedFullDayAverage_Type()
)
acPMIGMPSpecificQueryReceivedFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPSpecificQueryReceivedFullDayAverage.setStatus("current")
_AcPMIGMPMembershipReportsSentTable_Object = MibTable
acPMIGMPMembershipReportsSentTable = _AcPMIGMPMembershipReportsSentTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 7)
)
if mibBuilder.loadTexts:
    acPMIGMPMembershipReportsSentTable.setStatus("current")
_AcPMIGMPMembershipReportsSentEntry_Object = MibTableRow
acPMIGMPMembershipReportsSentEntry = _AcPMIGMPMembershipReportsSentEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 7, 1)
)
acPMIGMPMembershipReportsSentEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMIGMPMembershipReportsSentInterval"),
)
if mibBuilder.loadTexts:
    acPMIGMPMembershipReportsSentEntry.setStatus("current")


class _AcPMIGMPMembershipReportsSentInterval_Type(Unsigned32):
    """Custom type acPMIGMPMembershipReportsSentInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIGMPMembershipReportsSentInterval_Type.__name__ = "Unsigned32"
_AcPMIGMPMembershipReportsSentInterval_Object = MibTableColumn
acPMIGMPMembershipReportsSentInterval = _AcPMIGMPMembershipReportsSentInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 7, 1, 1),
    _AcPMIGMPMembershipReportsSentInterval_Type()
)
acPMIGMPMembershipReportsSentInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIGMPMembershipReportsSentInterval.setStatus("current")
_AcPMIGMPMembershipReportsSentVal_Type = Counter32
_AcPMIGMPMembershipReportsSentVal_Object = MibTableColumn
acPMIGMPMembershipReportsSentVal = _AcPMIGMPMembershipReportsSentVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 7, 1, 2),
    _AcPMIGMPMembershipReportsSentVal_Type()
)
acPMIGMPMembershipReportsSentVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPMembershipReportsSentVal.setStatus("current")


class _AcPMIGMPMembershipReportsSentAverage_Type(Integer32):
    """Custom type acPMIGMPMembershipReportsSentAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPMembershipReportsSentAverage_Type.__name__ = "Integer32"
_AcPMIGMPMembershipReportsSentAverage_Object = MibTableColumn
acPMIGMPMembershipReportsSentAverage = _AcPMIGMPMembershipReportsSentAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 7, 1, 3),
    _AcPMIGMPMembershipReportsSentAverage_Type()
)
acPMIGMPMembershipReportsSentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPMembershipReportsSentAverage.setStatus("current")


class _AcPMIGMPMembershipReportsSentMax_Type(Integer32):
    """Custom type acPMIGMPMembershipReportsSentMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPMembershipReportsSentMax_Type.__name__ = "Integer32"
_AcPMIGMPMembershipReportsSentMax_Object = MibTableColumn
acPMIGMPMembershipReportsSentMax = _AcPMIGMPMembershipReportsSentMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 7, 1, 4),
    _AcPMIGMPMembershipReportsSentMax_Type()
)
acPMIGMPMembershipReportsSentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPMembershipReportsSentMax.setStatus("current")


class _AcPMIGMPMembershipReportsSentMin_Type(Integer32):
    """Custom type acPMIGMPMembershipReportsSentMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPMembershipReportsSentMin_Type.__name__ = "Integer32"
_AcPMIGMPMembershipReportsSentMin_Object = MibTableColumn
acPMIGMPMembershipReportsSentMin = _AcPMIGMPMembershipReportsSentMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 7, 1, 5),
    _AcPMIGMPMembershipReportsSentMin_Type()
)
acPMIGMPMembershipReportsSentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPMembershipReportsSentMin.setStatus("current")


class _AcPMIGMPMembershipReportsSentFullDayAverage_Type(Integer32):
    """Custom type acPMIGMPMembershipReportsSentFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPMembershipReportsSentFullDayAverage_Type.__name__ = "Integer32"
_AcPMIGMPMembershipReportsSentFullDayAverage_Object = MibTableColumn
acPMIGMPMembershipReportsSentFullDayAverage = _AcPMIGMPMembershipReportsSentFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 7, 1, 6),
    _AcPMIGMPMembershipReportsSentFullDayAverage_Type()
)
acPMIGMPMembershipReportsSentFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPMembershipReportsSentFullDayAverage.setStatus("current")
_AcPMIGMPLeaveGroupSentTable_Object = MibTable
acPMIGMPLeaveGroupSentTable = _AcPMIGMPLeaveGroupSentTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 8)
)
if mibBuilder.loadTexts:
    acPMIGMPLeaveGroupSentTable.setStatus("current")
_AcPMIGMPLeaveGroupSentEntry_Object = MibTableRow
acPMIGMPLeaveGroupSentEntry = _AcPMIGMPLeaveGroupSentEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 8, 1)
)
acPMIGMPLeaveGroupSentEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMIGMPLeaveGroupSentInterval"),
)
if mibBuilder.loadTexts:
    acPMIGMPLeaveGroupSentEntry.setStatus("current")


class _AcPMIGMPLeaveGroupSentInterval_Type(Unsigned32):
    """Custom type acPMIGMPLeaveGroupSentInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMIGMPLeaveGroupSentInterval_Type.__name__ = "Unsigned32"
_AcPMIGMPLeaveGroupSentInterval_Object = MibTableColumn
acPMIGMPLeaveGroupSentInterval = _AcPMIGMPLeaveGroupSentInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 8, 1, 1),
    _AcPMIGMPLeaveGroupSentInterval_Type()
)
acPMIGMPLeaveGroupSentInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMIGMPLeaveGroupSentInterval.setStatus("current")
_AcPMIGMPLeaveGroupSentVal_Type = Counter32
_AcPMIGMPLeaveGroupSentVal_Object = MibTableColumn
acPMIGMPLeaveGroupSentVal = _AcPMIGMPLeaveGroupSentVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 8, 1, 2),
    _AcPMIGMPLeaveGroupSentVal_Type()
)
acPMIGMPLeaveGroupSentVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPLeaveGroupSentVal.setStatus("current")


class _AcPMIGMPLeaveGroupSentAverage_Type(Integer32):
    """Custom type acPMIGMPLeaveGroupSentAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPLeaveGroupSentAverage_Type.__name__ = "Integer32"
_AcPMIGMPLeaveGroupSentAverage_Object = MibTableColumn
acPMIGMPLeaveGroupSentAverage = _AcPMIGMPLeaveGroupSentAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 8, 1, 3),
    _AcPMIGMPLeaveGroupSentAverage_Type()
)
acPMIGMPLeaveGroupSentAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPLeaveGroupSentAverage.setStatus("current")


class _AcPMIGMPLeaveGroupSentMax_Type(Integer32):
    """Custom type acPMIGMPLeaveGroupSentMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPLeaveGroupSentMax_Type.__name__ = "Integer32"
_AcPMIGMPLeaveGroupSentMax_Object = MibTableColumn
acPMIGMPLeaveGroupSentMax = _AcPMIGMPLeaveGroupSentMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 8, 1, 4),
    _AcPMIGMPLeaveGroupSentMax_Type()
)
acPMIGMPLeaveGroupSentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPLeaveGroupSentMax.setStatus("current")


class _AcPMIGMPLeaveGroupSentMin_Type(Integer32):
    """Custom type acPMIGMPLeaveGroupSentMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPLeaveGroupSentMin_Type.__name__ = "Integer32"
_AcPMIGMPLeaveGroupSentMin_Object = MibTableColumn
acPMIGMPLeaveGroupSentMin = _AcPMIGMPLeaveGroupSentMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 8, 1, 5),
    _AcPMIGMPLeaveGroupSentMin_Type()
)
acPMIGMPLeaveGroupSentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPLeaveGroupSentMin.setStatus("current")


class _AcPMIGMPLeaveGroupSentFullDayAverage_Type(Integer32):
    """Custom type acPMIGMPLeaveGroupSentFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMIGMPLeaveGroupSentFullDayAverage_Type.__name__ = "Integer32"
_AcPMIGMPLeaveGroupSentFullDayAverage_Object = MibTableColumn
acPMIGMPLeaveGroupSentFullDayAverage = _AcPMIGMPLeaveGroupSentFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 71, 8, 1, 6),
    _AcPMIGMPLeaveGroupSentFullDayAverage_Type()
)
acPMIGMPLeaveGroupSentFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMIGMPLeaveGroupSentFullDayAverage.setStatus("current")
_AcPMSystemCongestion_ObjectIdentity = ObjectIdentity
acPMSystemCongestion = _AcPMSystemCongestion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81)
)
_AcPMCongestionGeneralResourcesTable_Object = MibTable
acPMCongestionGeneralResourcesTable = _AcPMCongestionGeneralResourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 1)
)
if mibBuilder.loadTexts:
    acPMCongestionGeneralResourcesTable.setStatus("current")
_AcPMCongestionGeneralResourcesEntry_Object = MibTableRow
acPMCongestionGeneralResourcesEntry = _AcPMCongestionGeneralResourcesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 1, 1)
)
acPMCongestionGeneralResourcesEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMCongestionGeneralResourcesInterval"),
)
if mibBuilder.loadTexts:
    acPMCongestionGeneralResourcesEntry.setStatus("current")


class _AcPMCongestionGeneralResourcesInterval_Type(Unsigned32):
    """Custom type acPMCongestionGeneralResourcesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCongestionGeneralResourcesInterval_Type.__name__ = "Unsigned32"
_AcPMCongestionGeneralResourcesInterval_Object = MibTableColumn
acPMCongestionGeneralResourcesInterval = _AcPMCongestionGeneralResourcesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 1, 1, 1),
    _AcPMCongestionGeneralResourcesInterval_Type()
)
acPMCongestionGeneralResourcesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCongestionGeneralResourcesInterval.setStatus("current")
_AcPMCongestionGeneralResourcesVal_Type = Counter32
_AcPMCongestionGeneralResourcesVal_Object = MibTableColumn
acPMCongestionGeneralResourcesVal = _AcPMCongestionGeneralResourcesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 1, 1, 2),
    _AcPMCongestionGeneralResourcesVal_Type()
)
acPMCongestionGeneralResourcesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionGeneralResourcesVal.setStatus("current")


class _AcPMCongestionGeneralResourcesAverage_Type(Integer32):
    """Custom type acPMCongestionGeneralResourcesAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionGeneralResourcesAverage_Type.__name__ = "Integer32"
_AcPMCongestionGeneralResourcesAverage_Object = MibTableColumn
acPMCongestionGeneralResourcesAverage = _AcPMCongestionGeneralResourcesAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 1, 1, 3),
    _AcPMCongestionGeneralResourcesAverage_Type()
)
acPMCongestionGeneralResourcesAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionGeneralResourcesAverage.setStatus("current")


class _AcPMCongestionGeneralResourcesMax_Type(Integer32):
    """Custom type acPMCongestionGeneralResourcesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionGeneralResourcesMax_Type.__name__ = "Integer32"
_AcPMCongestionGeneralResourcesMax_Object = MibTableColumn
acPMCongestionGeneralResourcesMax = _AcPMCongestionGeneralResourcesMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 1, 1, 4),
    _AcPMCongestionGeneralResourcesMax_Type()
)
acPMCongestionGeneralResourcesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionGeneralResourcesMax.setStatus("current")


class _AcPMCongestionGeneralResourcesMin_Type(Integer32):
    """Custom type acPMCongestionGeneralResourcesMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionGeneralResourcesMin_Type.__name__ = "Integer32"
_AcPMCongestionGeneralResourcesMin_Object = MibTableColumn
acPMCongestionGeneralResourcesMin = _AcPMCongestionGeneralResourcesMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 1, 1, 5),
    _AcPMCongestionGeneralResourcesMin_Type()
)
acPMCongestionGeneralResourcesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionGeneralResourcesMin.setStatus("current")


class _AcPMCongestionGeneralResourcesFullDayAverage_Type(Integer32):
    """Custom type acPMCongestionGeneralResourcesFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionGeneralResourcesFullDayAverage_Type.__name__ = "Integer32"
_AcPMCongestionGeneralResourcesFullDayAverage_Object = MibTableColumn
acPMCongestionGeneralResourcesFullDayAverage = _AcPMCongestionGeneralResourcesFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 1, 1, 6),
    _AcPMCongestionGeneralResourcesFullDayAverage_Type()
)
acPMCongestionGeneralResourcesFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionGeneralResourcesFullDayAverage.setStatus("current")
_AcPMCongestionDSPresourcesTable_Object = MibTable
acPMCongestionDSPresourcesTable = _AcPMCongestionDSPresourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 2)
)
if mibBuilder.loadTexts:
    acPMCongestionDSPresourcesTable.setStatus("current")
_AcPMCongestionDSPresourcesEntry_Object = MibTableRow
acPMCongestionDSPresourcesEntry = _AcPMCongestionDSPresourcesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 2, 1)
)
acPMCongestionDSPresourcesEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMCongestionDSPresourcesInterval"),
)
if mibBuilder.loadTexts:
    acPMCongestionDSPresourcesEntry.setStatus("current")


class _AcPMCongestionDSPresourcesInterval_Type(Unsigned32):
    """Custom type acPMCongestionDSPresourcesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCongestionDSPresourcesInterval_Type.__name__ = "Unsigned32"
_AcPMCongestionDSPresourcesInterval_Object = MibTableColumn
acPMCongestionDSPresourcesInterval = _AcPMCongestionDSPresourcesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 2, 1, 1),
    _AcPMCongestionDSPresourcesInterval_Type()
)
acPMCongestionDSPresourcesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCongestionDSPresourcesInterval.setStatus("current")
_AcPMCongestionDSPresourcesVal_Type = Counter32
_AcPMCongestionDSPresourcesVal_Object = MibTableColumn
acPMCongestionDSPresourcesVal = _AcPMCongestionDSPresourcesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 2, 1, 2),
    _AcPMCongestionDSPresourcesVal_Type()
)
acPMCongestionDSPresourcesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionDSPresourcesVal.setStatus("current")


class _AcPMCongestionDSPresourcesAverage_Type(Integer32):
    """Custom type acPMCongestionDSPresourcesAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionDSPresourcesAverage_Type.__name__ = "Integer32"
_AcPMCongestionDSPresourcesAverage_Object = MibTableColumn
acPMCongestionDSPresourcesAverage = _AcPMCongestionDSPresourcesAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 2, 1, 3),
    _AcPMCongestionDSPresourcesAverage_Type()
)
acPMCongestionDSPresourcesAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionDSPresourcesAverage.setStatus("current")


class _AcPMCongestionDSPresourcesMax_Type(Integer32):
    """Custom type acPMCongestionDSPresourcesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionDSPresourcesMax_Type.__name__ = "Integer32"
_AcPMCongestionDSPresourcesMax_Object = MibTableColumn
acPMCongestionDSPresourcesMax = _AcPMCongestionDSPresourcesMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 2, 1, 4),
    _AcPMCongestionDSPresourcesMax_Type()
)
acPMCongestionDSPresourcesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionDSPresourcesMax.setStatus("current")


class _AcPMCongestionDSPresourcesMin_Type(Integer32):
    """Custom type acPMCongestionDSPresourcesMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionDSPresourcesMin_Type.__name__ = "Integer32"
_AcPMCongestionDSPresourcesMin_Object = MibTableColumn
acPMCongestionDSPresourcesMin = _AcPMCongestionDSPresourcesMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 2, 1, 5),
    _AcPMCongestionDSPresourcesMin_Type()
)
acPMCongestionDSPresourcesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionDSPresourcesMin.setStatus("current")


class _AcPMCongestionDSPresourcesFullDayAverage_Type(Integer32):
    """Custom type acPMCongestionDSPresourcesFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionDSPresourcesFullDayAverage_Type.__name__ = "Integer32"
_AcPMCongestionDSPresourcesFullDayAverage_Object = MibTableColumn
acPMCongestionDSPresourcesFullDayAverage = _AcPMCongestionDSPresourcesFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 2, 1, 6),
    _AcPMCongestionDSPresourcesFullDayAverage_Type()
)
acPMCongestionDSPresourcesFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionDSPresourcesFullDayAverage.setStatus("current")
_AcPMCongestionIPresourcesTable_Object = MibTable
acPMCongestionIPresourcesTable = _AcPMCongestionIPresourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 3)
)
if mibBuilder.loadTexts:
    acPMCongestionIPresourcesTable.setStatus("current")
_AcPMCongestionIPresourcesEntry_Object = MibTableRow
acPMCongestionIPresourcesEntry = _AcPMCongestionIPresourcesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 3, 1)
)
acPMCongestionIPresourcesEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMCongestionIPresourcesInterval"),
)
if mibBuilder.loadTexts:
    acPMCongestionIPresourcesEntry.setStatus("current")


class _AcPMCongestionIPresourcesInterval_Type(Unsigned32):
    """Custom type acPMCongestionIPresourcesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCongestionIPresourcesInterval_Type.__name__ = "Unsigned32"
_AcPMCongestionIPresourcesInterval_Object = MibTableColumn
acPMCongestionIPresourcesInterval = _AcPMCongestionIPresourcesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 3, 1, 1),
    _AcPMCongestionIPresourcesInterval_Type()
)
acPMCongestionIPresourcesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCongestionIPresourcesInterval.setStatus("current")
_AcPMCongestionIPresourcesVal_Type = Counter32
_AcPMCongestionIPresourcesVal_Object = MibTableColumn
acPMCongestionIPresourcesVal = _AcPMCongestionIPresourcesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 3, 1, 2),
    _AcPMCongestionIPresourcesVal_Type()
)
acPMCongestionIPresourcesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionIPresourcesVal.setStatus("current")


class _AcPMCongestionIPresourcesAverage_Type(Integer32):
    """Custom type acPMCongestionIPresourcesAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionIPresourcesAverage_Type.__name__ = "Integer32"
_AcPMCongestionIPresourcesAverage_Object = MibTableColumn
acPMCongestionIPresourcesAverage = _AcPMCongestionIPresourcesAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 3, 1, 3),
    _AcPMCongestionIPresourcesAverage_Type()
)
acPMCongestionIPresourcesAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionIPresourcesAverage.setStatus("current")


class _AcPMCongestionIPresourcesMax_Type(Integer32):
    """Custom type acPMCongestionIPresourcesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionIPresourcesMax_Type.__name__ = "Integer32"
_AcPMCongestionIPresourcesMax_Object = MibTableColumn
acPMCongestionIPresourcesMax = _AcPMCongestionIPresourcesMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 3, 1, 4),
    _AcPMCongestionIPresourcesMax_Type()
)
acPMCongestionIPresourcesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionIPresourcesMax.setStatus("current")


class _AcPMCongestionIPresourcesMin_Type(Integer32):
    """Custom type acPMCongestionIPresourcesMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionIPresourcesMin_Type.__name__ = "Integer32"
_AcPMCongestionIPresourcesMin_Object = MibTableColumn
acPMCongestionIPresourcesMin = _AcPMCongestionIPresourcesMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 3, 1, 5),
    _AcPMCongestionIPresourcesMin_Type()
)
acPMCongestionIPresourcesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionIPresourcesMin.setStatus("current")


class _AcPMCongestionIPresourcesFullDayAverage_Type(Integer32):
    """Custom type acPMCongestionIPresourcesFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionIPresourcesFullDayAverage_Type.__name__ = "Integer32"
_AcPMCongestionIPresourcesFullDayAverage_Object = MibTableColumn
acPMCongestionIPresourcesFullDayAverage = _AcPMCongestionIPresourcesFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 3, 1, 6),
    _AcPMCongestionIPresourcesFullDayAverage_Type()
)
acPMCongestionIPresourcesFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionIPresourcesFullDayAverage.setStatus("current")
_AcPMCongestionATMresourcesTable_Object = MibTable
acPMCongestionATMresourcesTable = _AcPMCongestionATMresourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 4)
)
if mibBuilder.loadTexts:
    acPMCongestionATMresourcesTable.setStatus("current")
_AcPMCongestionATMresourcesEntry_Object = MibTableRow
acPMCongestionATMresourcesEntry = _AcPMCongestionATMresourcesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 4, 1)
)
acPMCongestionATMresourcesEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMCongestionATMresourcesInterval"),
)
if mibBuilder.loadTexts:
    acPMCongestionATMresourcesEntry.setStatus("current")


class _AcPMCongestionATMresourcesInterval_Type(Unsigned32):
    """Custom type acPMCongestionATMresourcesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCongestionATMresourcesInterval_Type.__name__ = "Unsigned32"
_AcPMCongestionATMresourcesInterval_Object = MibTableColumn
acPMCongestionATMresourcesInterval = _AcPMCongestionATMresourcesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 4, 1, 1),
    _AcPMCongestionATMresourcesInterval_Type()
)
acPMCongestionATMresourcesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCongestionATMresourcesInterval.setStatus("current")
_AcPMCongestionATMresourcesVal_Type = Counter32
_AcPMCongestionATMresourcesVal_Object = MibTableColumn
acPMCongestionATMresourcesVal = _AcPMCongestionATMresourcesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 4, 1, 2),
    _AcPMCongestionATMresourcesVal_Type()
)
acPMCongestionATMresourcesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionATMresourcesVal.setStatus("current")


class _AcPMCongestionATMresourcesAverage_Type(Integer32):
    """Custom type acPMCongestionATMresourcesAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionATMresourcesAverage_Type.__name__ = "Integer32"
_AcPMCongestionATMresourcesAverage_Object = MibTableColumn
acPMCongestionATMresourcesAverage = _AcPMCongestionATMresourcesAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 4, 1, 3),
    _AcPMCongestionATMresourcesAverage_Type()
)
acPMCongestionATMresourcesAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionATMresourcesAverage.setStatus("current")


class _AcPMCongestionATMresourcesMax_Type(Integer32):
    """Custom type acPMCongestionATMresourcesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionATMresourcesMax_Type.__name__ = "Integer32"
_AcPMCongestionATMresourcesMax_Object = MibTableColumn
acPMCongestionATMresourcesMax = _AcPMCongestionATMresourcesMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 4, 1, 4),
    _AcPMCongestionATMresourcesMax_Type()
)
acPMCongestionATMresourcesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionATMresourcesMax.setStatus("current")


class _AcPMCongestionATMresourcesMin_Type(Integer32):
    """Custom type acPMCongestionATMresourcesMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionATMresourcesMin_Type.__name__ = "Integer32"
_AcPMCongestionATMresourcesMin_Object = MibTableColumn
acPMCongestionATMresourcesMin = _AcPMCongestionATMresourcesMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 4, 1, 5),
    _AcPMCongestionATMresourcesMin_Type()
)
acPMCongestionATMresourcesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionATMresourcesMin.setStatus("current")


class _AcPMCongestionATMresourcesFullDayAverage_Type(Integer32):
    """Custom type acPMCongestionATMresourcesFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionATMresourcesFullDayAverage_Type.__name__ = "Integer32"
_AcPMCongestionATMresourcesFullDayAverage_Object = MibTableColumn
acPMCongestionATMresourcesFullDayAverage = _AcPMCongestionATMresourcesFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 4, 1, 6),
    _AcPMCongestionATMresourcesFullDayAverage_Type()
)
acPMCongestionATMresourcesFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionATMresourcesFullDayAverage.setStatus("current")
_AcPMCongestionConferenceResourcesTable_Object = MibTable
acPMCongestionConferenceResourcesTable = _AcPMCongestionConferenceResourcesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 5)
)
if mibBuilder.loadTexts:
    acPMCongestionConferenceResourcesTable.setStatus("current")
_AcPMCongestionConferenceResourcesEntry_Object = MibTableRow
acPMCongestionConferenceResourcesEntry = _AcPMCongestionConferenceResourcesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 5, 1)
)
acPMCongestionConferenceResourcesEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMCongestionConferenceResourcesInterval"),
)
if mibBuilder.loadTexts:
    acPMCongestionConferenceResourcesEntry.setStatus("current")


class _AcPMCongestionConferenceResourcesInterval_Type(Unsigned32):
    """Custom type acPMCongestionConferenceResourcesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCongestionConferenceResourcesInterval_Type.__name__ = "Unsigned32"
_AcPMCongestionConferenceResourcesInterval_Object = MibTableColumn
acPMCongestionConferenceResourcesInterval = _AcPMCongestionConferenceResourcesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 5, 1, 1),
    _AcPMCongestionConferenceResourcesInterval_Type()
)
acPMCongestionConferenceResourcesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCongestionConferenceResourcesInterval.setStatus("current")
_AcPMCongestionConferenceResourcesVal_Type = Counter32
_AcPMCongestionConferenceResourcesVal_Object = MibTableColumn
acPMCongestionConferenceResourcesVal = _AcPMCongestionConferenceResourcesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 5, 1, 2),
    _AcPMCongestionConferenceResourcesVal_Type()
)
acPMCongestionConferenceResourcesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionConferenceResourcesVal.setStatus("current")


class _AcPMCongestionConferenceResourcesAverage_Type(Integer32):
    """Custom type acPMCongestionConferenceResourcesAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionConferenceResourcesAverage_Type.__name__ = "Integer32"
_AcPMCongestionConferenceResourcesAverage_Object = MibTableColumn
acPMCongestionConferenceResourcesAverage = _AcPMCongestionConferenceResourcesAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 5, 1, 3),
    _AcPMCongestionConferenceResourcesAverage_Type()
)
acPMCongestionConferenceResourcesAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionConferenceResourcesAverage.setStatus("current")


class _AcPMCongestionConferenceResourcesMax_Type(Integer32):
    """Custom type acPMCongestionConferenceResourcesMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionConferenceResourcesMax_Type.__name__ = "Integer32"
_AcPMCongestionConferenceResourcesMax_Object = MibTableColumn
acPMCongestionConferenceResourcesMax = _AcPMCongestionConferenceResourcesMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 5, 1, 4),
    _AcPMCongestionConferenceResourcesMax_Type()
)
acPMCongestionConferenceResourcesMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionConferenceResourcesMax.setStatus("current")


class _AcPMCongestionConferenceResourcesMin_Type(Integer32):
    """Custom type acPMCongestionConferenceResourcesMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionConferenceResourcesMin_Type.__name__ = "Integer32"
_AcPMCongestionConferenceResourcesMin_Object = MibTableColumn
acPMCongestionConferenceResourcesMin = _AcPMCongestionConferenceResourcesMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 5, 1, 5),
    _AcPMCongestionConferenceResourcesMin_Type()
)
acPMCongestionConferenceResourcesMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionConferenceResourcesMin.setStatus("current")


class _AcPMCongestionConferenceResourcesFullDayAverage_Type(Integer32):
    """Custom type acPMCongestionConferenceResourcesFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCongestionConferenceResourcesFullDayAverage_Type.__name__ = "Integer32"
_AcPMCongestionConferenceResourcesFullDayAverage_Object = MibTableColumn
acPMCongestionConferenceResourcesFullDayAverage = _AcPMCongestionConferenceResourcesFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 81, 5, 1, 6),
    _AcPMCongestionConferenceResourcesFullDayAverage_Type()
)
acPMCongestionConferenceResourcesFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCongestionConferenceResourcesFullDayAverage.setStatus("current")
_AcPMSystemNFS_ObjectIdentity = ObjectIdentity
acPMSystemNFS = _AcPMSystemNFS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91)
)
_AcPMNFSCurrentRequestsTable_Object = MibTable
acPMNFSCurrentRequestsTable = _AcPMNFSCurrentRequestsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 1)
)
if mibBuilder.loadTexts:
    acPMNFSCurrentRequestsTable.setStatus("current")
_AcPMNFSCurrentRequestsEntry_Object = MibTableRow
acPMNFSCurrentRequestsEntry = _AcPMNFSCurrentRequestsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 1, 1)
)
acPMNFSCurrentRequestsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNFSCurrentRequestsType"),
    (0, "AC-PM-System-MIB", "acPMNFSCurrentRequestsInterval"),
)
if mibBuilder.loadTexts:
    acPMNFSCurrentRequestsEntry.setStatus("current")


class _AcPMNFSCurrentRequestsType_Type(Integer32):
    """Custom type acPMNFSCurrentRequestsType based on Integer32"""
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
        *(("other", 4),
          ("play", 2),
          ("readFile", 0),
          ("record", 3),
          ("writeFile", 1))
    )


_AcPMNFSCurrentRequestsType_Type.__name__ = "Integer32"
_AcPMNFSCurrentRequestsType_Object = MibTableColumn
acPMNFSCurrentRequestsType = _AcPMNFSCurrentRequestsType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 1, 1, 1),
    _AcPMNFSCurrentRequestsType_Type()
)
acPMNFSCurrentRequestsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSCurrentRequestsType.setStatus("current")


class _AcPMNFSCurrentRequestsInterval_Type(Unsigned32):
    """Custom type acPMNFSCurrentRequestsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNFSCurrentRequestsInterval_Type.__name__ = "Unsigned32"
_AcPMNFSCurrentRequestsInterval_Object = MibTableColumn
acPMNFSCurrentRequestsInterval = _AcPMNFSCurrentRequestsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 1, 1, 2),
    _AcPMNFSCurrentRequestsInterval_Type()
)
acPMNFSCurrentRequestsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSCurrentRequestsInterval.setStatus("current")
_AcPMNFSCurrentRequestsVal_Type = Gauge32
_AcPMNFSCurrentRequestsVal_Object = MibTableColumn
acPMNFSCurrentRequestsVal = _AcPMNFSCurrentRequestsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 1, 1, 3),
    _AcPMNFSCurrentRequestsVal_Type()
)
acPMNFSCurrentRequestsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSCurrentRequestsVal.setStatus("current")


class _AcPMNFSCurrentRequestsAverage_Type(Integer32):
    """Custom type acPMNFSCurrentRequestsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSCurrentRequestsAverage_Type.__name__ = "Integer32"
_AcPMNFSCurrentRequestsAverage_Object = MibTableColumn
acPMNFSCurrentRequestsAverage = _AcPMNFSCurrentRequestsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 1, 1, 4),
    _AcPMNFSCurrentRequestsAverage_Type()
)
acPMNFSCurrentRequestsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSCurrentRequestsAverage.setStatus("current")


class _AcPMNFSCurrentRequestsMax_Type(Integer32):
    """Custom type acPMNFSCurrentRequestsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSCurrentRequestsMax_Type.__name__ = "Integer32"
_AcPMNFSCurrentRequestsMax_Object = MibTableColumn
acPMNFSCurrentRequestsMax = _AcPMNFSCurrentRequestsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 1, 1, 5),
    _AcPMNFSCurrentRequestsMax_Type()
)
acPMNFSCurrentRequestsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSCurrentRequestsMax.setStatus("current")


class _AcPMNFSCurrentRequestsMin_Type(Integer32):
    """Custom type acPMNFSCurrentRequestsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSCurrentRequestsMin_Type.__name__ = "Integer32"
_AcPMNFSCurrentRequestsMin_Object = MibTableColumn
acPMNFSCurrentRequestsMin = _AcPMNFSCurrentRequestsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 1, 1, 6),
    _AcPMNFSCurrentRequestsMin_Type()
)
acPMNFSCurrentRequestsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSCurrentRequestsMin.setStatus("current")


class _AcPMNFSCurrentRequestsFullDayAverage_Type(Integer32):
    """Custom type acPMNFSCurrentRequestsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSCurrentRequestsFullDayAverage_Type.__name__ = "Integer32"
_AcPMNFSCurrentRequestsFullDayAverage_Object = MibTableColumn
acPMNFSCurrentRequestsFullDayAverage = _AcPMNFSCurrentRequestsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 1, 1, 7),
    _AcPMNFSCurrentRequestsFullDayAverage_Type()
)
acPMNFSCurrentRequestsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSCurrentRequestsFullDayAverage.setStatus("current")
_AcPMNFSRequestsTable_Object = MibTable
acPMNFSRequestsTable = _AcPMNFSRequestsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 2)
)
if mibBuilder.loadTexts:
    acPMNFSRequestsTable.setStatus("current")
_AcPMNFSRequestsEntry_Object = MibTableRow
acPMNFSRequestsEntry = _AcPMNFSRequestsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 2, 1)
)
acPMNFSRequestsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNFSRequestsType"),
    (0, "AC-PM-System-MIB", "acPMNFSRequestsInterval"),
)
if mibBuilder.loadTexts:
    acPMNFSRequestsEntry.setStatus("current")


class _AcPMNFSRequestsType_Type(Integer32):
    """Custom type acPMNFSRequestsType based on Integer32"""
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
        *(("other", 4),
          ("play", 2),
          ("readFile", 0),
          ("record", 3),
          ("writeFile", 1))
    )


_AcPMNFSRequestsType_Type.__name__ = "Integer32"
_AcPMNFSRequestsType_Object = MibTableColumn
acPMNFSRequestsType = _AcPMNFSRequestsType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 2, 1, 1),
    _AcPMNFSRequestsType_Type()
)
acPMNFSRequestsType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSRequestsType.setStatus("current")


class _AcPMNFSRequestsInterval_Type(Unsigned32):
    """Custom type acPMNFSRequestsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNFSRequestsInterval_Type.__name__ = "Unsigned32"
_AcPMNFSRequestsInterval_Object = MibTableColumn
acPMNFSRequestsInterval = _AcPMNFSRequestsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 2, 1, 2),
    _AcPMNFSRequestsInterval_Type()
)
acPMNFSRequestsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSRequestsInterval.setStatus("current")
_AcPMNFSRequestsVal_Type = Counter32
_AcPMNFSRequestsVal_Object = MibTableColumn
acPMNFSRequestsVal = _AcPMNFSRequestsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 2, 1, 3),
    _AcPMNFSRequestsVal_Type()
)
acPMNFSRequestsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRequestsVal.setStatus("current")


class _AcPMNFSRequestsFullDayAverage_Type(Integer32):
    """Custom type acPMNFSRequestsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSRequestsFullDayAverage_Type.__name__ = "Integer32"
_AcPMNFSRequestsFullDayAverage_Object = MibTableColumn
acPMNFSRequestsFullDayAverage = _AcPMNFSRequestsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 2, 1, 4),
    _AcPMNFSRequestsFullDayAverage_Type()
)
acPMNFSRequestsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRequestsFullDayAverage.setStatus("current")
_AcPMNFSRoundTripTimeMsTable_Object = MibTable
acPMNFSRoundTripTimeMsTable = _AcPMNFSRoundTripTimeMsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3)
)
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsTable.setStatus("current")
_AcPMNFSRoundTripTimeMsEntry_Object = MibTableRow
acPMNFSRoundTripTimeMsEntry = _AcPMNFSRoundTripTimeMsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1)
)
acPMNFSRoundTripTimeMsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNFSRoundTripTimeMsRfsNumber"),
    (0, "AC-PM-System-MIB", "acPMNFSRoundTripTimeMsInterval"),
)
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsEntry.setStatus("current")


class _AcPMNFSRoundTripTimeMsRfsNumber_Type(Unsigned32):
    """Custom type acPMNFSRoundTripTimeMsRfsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcPMNFSRoundTripTimeMsRfsNumber_Type.__name__ = "Unsigned32"
_AcPMNFSRoundTripTimeMsRfsNumber_Object = MibTableColumn
acPMNFSRoundTripTimeMsRfsNumber = _AcPMNFSRoundTripTimeMsRfsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1, 1),
    _AcPMNFSRoundTripTimeMsRfsNumber_Type()
)
acPMNFSRoundTripTimeMsRfsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsRfsNumber.setStatus("current")


class _AcPMNFSRoundTripTimeMsInterval_Type(Unsigned32):
    """Custom type acPMNFSRoundTripTimeMsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNFSRoundTripTimeMsInterval_Type.__name__ = "Unsigned32"
_AcPMNFSRoundTripTimeMsInterval_Object = MibTableColumn
acPMNFSRoundTripTimeMsInterval = _AcPMNFSRoundTripTimeMsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1, 2),
    _AcPMNFSRoundTripTimeMsInterval_Type()
)
acPMNFSRoundTripTimeMsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsInterval.setStatus("current")
_AcPMNFSRoundTripTimeMsVal_Type = Gauge32
_AcPMNFSRoundTripTimeMsVal_Object = MibTableColumn
acPMNFSRoundTripTimeMsVal = _AcPMNFSRoundTripTimeMsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1, 3),
    _AcPMNFSRoundTripTimeMsVal_Type()
)
acPMNFSRoundTripTimeMsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsVal.setStatus("current")


class _AcPMNFSRoundTripTimeMsAverage_Type(Integer32):
    """Custom type acPMNFSRoundTripTimeMsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSRoundTripTimeMsAverage_Type.__name__ = "Integer32"
_AcPMNFSRoundTripTimeMsAverage_Object = MibTableColumn
acPMNFSRoundTripTimeMsAverage = _AcPMNFSRoundTripTimeMsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1, 4),
    _AcPMNFSRoundTripTimeMsAverage_Type()
)
acPMNFSRoundTripTimeMsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsAverage.setStatus("current")


class _AcPMNFSRoundTripTimeMsMax_Type(Integer32):
    """Custom type acPMNFSRoundTripTimeMsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSRoundTripTimeMsMax_Type.__name__ = "Integer32"
_AcPMNFSRoundTripTimeMsMax_Object = MibTableColumn
acPMNFSRoundTripTimeMsMax = _AcPMNFSRoundTripTimeMsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1, 5),
    _AcPMNFSRoundTripTimeMsMax_Type()
)
acPMNFSRoundTripTimeMsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsMax.setStatus("current")


class _AcPMNFSRoundTripTimeMsMin_Type(Integer32):
    """Custom type acPMNFSRoundTripTimeMsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSRoundTripTimeMsMin_Type.__name__ = "Integer32"
_AcPMNFSRoundTripTimeMsMin_Object = MibTableColumn
acPMNFSRoundTripTimeMsMin = _AcPMNFSRoundTripTimeMsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1, 6),
    _AcPMNFSRoundTripTimeMsMin_Type()
)
acPMNFSRoundTripTimeMsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsMin.setStatus("current")
_AcPMNFSRoundTripTimeMsVolume_Type = Counter32
_AcPMNFSRoundTripTimeMsVolume_Object = MibTableColumn
acPMNFSRoundTripTimeMsVolume = _AcPMNFSRoundTripTimeMsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1, 7),
    _AcPMNFSRoundTripTimeMsVolume_Type()
)
acPMNFSRoundTripTimeMsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsVolume.setStatus("current")


class _AcPMNFSRoundTripTimeMsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMNFSRoundTripTimeMsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSRoundTripTimeMsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMNFSRoundTripTimeMsTimeBelowLowThreshold_Object = MibTableColumn
acPMNFSRoundTripTimeMsTimeBelowLowThreshold = _AcPMNFSRoundTripTimeMsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1, 8),
    _AcPMNFSRoundTripTimeMsTimeBelowLowThreshold_Type()
)
acPMNFSRoundTripTimeMsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsTimeBelowLowThreshold.setStatus("current")


class _AcPMNFSRoundTripTimeMsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMNFSRoundTripTimeMsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSRoundTripTimeMsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMNFSRoundTripTimeMsTimeBetweenThresholds_Object = MibTableColumn
acPMNFSRoundTripTimeMsTimeBetweenThresholds = _AcPMNFSRoundTripTimeMsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1, 9),
    _AcPMNFSRoundTripTimeMsTimeBetweenThresholds_Type()
)
acPMNFSRoundTripTimeMsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsTimeBetweenThresholds.setStatus("current")


class _AcPMNFSRoundTripTimeMsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMNFSRoundTripTimeMsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSRoundTripTimeMsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMNFSRoundTripTimeMsTimeAboveHighThreshold_Object = MibTableColumn
acPMNFSRoundTripTimeMsTimeAboveHighThreshold = _AcPMNFSRoundTripTimeMsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1, 10),
    _AcPMNFSRoundTripTimeMsTimeAboveHighThreshold_Type()
)
acPMNFSRoundTripTimeMsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsTimeAboveHighThreshold.setStatus("current")


class _AcPMNFSRoundTripTimeMsFullDayAverage_Type(Integer32):
    """Custom type acPMNFSRoundTripTimeMsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSRoundTripTimeMsFullDayAverage_Type.__name__ = "Integer32"
_AcPMNFSRoundTripTimeMsFullDayAverage_Object = MibTableColumn
acPMNFSRoundTripTimeMsFullDayAverage = _AcPMNFSRoundTripTimeMsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 3, 1, 11),
    _AcPMNFSRoundTripTimeMsFullDayAverage_Type()
)
acPMNFSRoundTripTimeMsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRoundTripTimeMsFullDayAverage.setStatus("current")
_AcPMNFSRetriesTable_Object = MibTable
acPMNFSRetriesTable = _AcPMNFSRetriesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 4)
)
if mibBuilder.loadTexts:
    acPMNFSRetriesTable.setStatus("current")
_AcPMNFSRetriesEntry_Object = MibTableRow
acPMNFSRetriesEntry = _AcPMNFSRetriesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 4, 1)
)
acPMNFSRetriesEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNFSRetriesRfsNumber"),
    (0, "AC-PM-System-MIB", "acPMNFSRetriesInterval"),
)
if mibBuilder.loadTexts:
    acPMNFSRetriesEntry.setStatus("current")


class _AcPMNFSRetriesRfsNumber_Type(Unsigned32):
    """Custom type acPMNFSRetriesRfsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcPMNFSRetriesRfsNumber_Type.__name__ = "Unsigned32"
_AcPMNFSRetriesRfsNumber_Object = MibTableColumn
acPMNFSRetriesRfsNumber = _AcPMNFSRetriesRfsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 4, 1, 1),
    _AcPMNFSRetriesRfsNumber_Type()
)
acPMNFSRetriesRfsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSRetriesRfsNumber.setStatus("current")


class _AcPMNFSRetriesInterval_Type(Unsigned32):
    """Custom type acPMNFSRetriesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNFSRetriesInterval_Type.__name__ = "Unsigned32"
_AcPMNFSRetriesInterval_Object = MibTableColumn
acPMNFSRetriesInterval = _AcPMNFSRetriesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 4, 1, 2),
    _AcPMNFSRetriesInterval_Type()
)
acPMNFSRetriesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSRetriesInterval.setStatus("current")
_AcPMNFSRetriesVal_Type = Gauge32
_AcPMNFSRetriesVal_Object = MibTableColumn
acPMNFSRetriesVal = _AcPMNFSRetriesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 4, 1, 3),
    _AcPMNFSRetriesVal_Type()
)
acPMNFSRetriesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRetriesVal.setStatus("current")
_AcPMNFSRetriesVolume_Type = Counter32
_AcPMNFSRetriesVolume_Object = MibTableColumn
acPMNFSRetriesVolume = _AcPMNFSRetriesVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 4, 1, 4),
    _AcPMNFSRetriesVolume_Type()
)
acPMNFSRetriesVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRetriesVolume.setStatus("current")


class _AcPMNFSRetriesTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMNFSRetriesTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSRetriesTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMNFSRetriesTimeBelowLowThreshold_Object = MibTableColumn
acPMNFSRetriesTimeBelowLowThreshold = _AcPMNFSRetriesTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 4, 1, 5),
    _AcPMNFSRetriesTimeBelowLowThreshold_Type()
)
acPMNFSRetriesTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRetriesTimeBelowLowThreshold.setStatus("current")


class _AcPMNFSRetriesTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMNFSRetriesTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSRetriesTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMNFSRetriesTimeBetweenThresholds_Object = MibTableColumn
acPMNFSRetriesTimeBetweenThresholds = _AcPMNFSRetriesTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 4, 1, 6),
    _AcPMNFSRetriesTimeBetweenThresholds_Type()
)
acPMNFSRetriesTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRetriesTimeBetweenThresholds.setStatus("current")


class _AcPMNFSRetriesTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMNFSRetriesTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSRetriesTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMNFSRetriesTimeAboveHighThreshold_Object = MibTableColumn
acPMNFSRetriesTimeAboveHighThreshold = _AcPMNFSRetriesTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 4, 1, 7),
    _AcPMNFSRetriesTimeAboveHighThreshold_Type()
)
acPMNFSRetriesTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRetriesTimeAboveHighThreshold.setStatus("current")


class _AcPMNFSRetriesFullDayAverage_Type(Integer32):
    """Custom type acPMNFSRetriesFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSRetriesFullDayAverage_Type.__name__ = "Integer32"
_AcPMNFSRetriesFullDayAverage_Object = MibTableColumn
acPMNFSRetriesFullDayAverage = _AcPMNFSRetriesFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 4, 1, 8),
    _AcPMNFSRetriesFullDayAverage_Type()
)
acPMNFSRetriesFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSRetriesFullDayAverage.setStatus("current")
_AcPMNFSAbortDueToMaxRetriesExceededTable_Object = MibTable
acPMNFSAbortDueToMaxRetriesExceededTable = _AcPMNFSAbortDueToMaxRetriesExceededTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 5)
)
if mibBuilder.loadTexts:
    acPMNFSAbortDueToMaxRetriesExceededTable.setStatus("current")
_AcPMNFSAbortDueToMaxRetriesExceededEntry_Object = MibTableRow
acPMNFSAbortDueToMaxRetriesExceededEntry = _AcPMNFSAbortDueToMaxRetriesExceededEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 5, 1)
)
acPMNFSAbortDueToMaxRetriesExceededEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNFSAbortDueToMaxRetriesExceededRfsNumber"),
    (0, "AC-PM-System-MIB", "acPMNFSAbortDueToMaxRetriesExceededInterval"),
)
if mibBuilder.loadTexts:
    acPMNFSAbortDueToMaxRetriesExceededEntry.setStatus("current")


class _AcPMNFSAbortDueToMaxRetriesExceededRfsNumber_Type(Unsigned32):
    """Custom type acPMNFSAbortDueToMaxRetriesExceededRfsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcPMNFSAbortDueToMaxRetriesExceededRfsNumber_Type.__name__ = "Unsigned32"
_AcPMNFSAbortDueToMaxRetriesExceededRfsNumber_Object = MibTableColumn
acPMNFSAbortDueToMaxRetriesExceededRfsNumber = _AcPMNFSAbortDueToMaxRetriesExceededRfsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 5, 1, 1),
    _AcPMNFSAbortDueToMaxRetriesExceededRfsNumber_Type()
)
acPMNFSAbortDueToMaxRetriesExceededRfsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSAbortDueToMaxRetriesExceededRfsNumber.setStatus("current")


class _AcPMNFSAbortDueToMaxRetriesExceededInterval_Type(Unsigned32):
    """Custom type acPMNFSAbortDueToMaxRetriesExceededInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNFSAbortDueToMaxRetriesExceededInterval_Type.__name__ = "Unsigned32"
_AcPMNFSAbortDueToMaxRetriesExceededInterval_Object = MibTableColumn
acPMNFSAbortDueToMaxRetriesExceededInterval = _AcPMNFSAbortDueToMaxRetriesExceededInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 5, 1, 2),
    _AcPMNFSAbortDueToMaxRetriesExceededInterval_Type()
)
acPMNFSAbortDueToMaxRetriesExceededInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSAbortDueToMaxRetriesExceededInterval.setStatus("current")
_AcPMNFSAbortDueToMaxRetriesExceededVal_Type = Gauge32
_AcPMNFSAbortDueToMaxRetriesExceededVal_Object = MibTableColumn
acPMNFSAbortDueToMaxRetriesExceededVal = _AcPMNFSAbortDueToMaxRetriesExceededVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 5, 1, 3),
    _AcPMNFSAbortDueToMaxRetriesExceededVal_Type()
)
acPMNFSAbortDueToMaxRetriesExceededVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSAbortDueToMaxRetriesExceededVal.setStatus("current")
_AcPMNFSAbortDueToMaxRetriesExceededVolume_Type = Counter32
_AcPMNFSAbortDueToMaxRetriesExceededVolume_Object = MibTableColumn
acPMNFSAbortDueToMaxRetriesExceededVolume = _AcPMNFSAbortDueToMaxRetriesExceededVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 5, 1, 4),
    _AcPMNFSAbortDueToMaxRetriesExceededVolume_Type()
)
acPMNFSAbortDueToMaxRetriesExceededVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSAbortDueToMaxRetriesExceededVolume.setStatus("current")


class _AcPMNFSAbortDueToMaxRetriesExceededTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMNFSAbortDueToMaxRetriesExceededTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSAbortDueToMaxRetriesExceededTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMNFSAbortDueToMaxRetriesExceededTimeBelowLowThreshold_Object = MibTableColumn
acPMNFSAbortDueToMaxRetriesExceededTimeBelowLowThreshold = _AcPMNFSAbortDueToMaxRetriesExceededTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 5, 1, 5),
    _AcPMNFSAbortDueToMaxRetriesExceededTimeBelowLowThreshold_Type()
)
acPMNFSAbortDueToMaxRetriesExceededTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSAbortDueToMaxRetriesExceededTimeBelowLowThreshold.setStatus("current")


class _AcPMNFSAbortDueToMaxRetriesExceededTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMNFSAbortDueToMaxRetriesExceededTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSAbortDueToMaxRetriesExceededTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMNFSAbortDueToMaxRetriesExceededTimeBetweenThresholds_Object = MibTableColumn
acPMNFSAbortDueToMaxRetriesExceededTimeBetweenThresholds = _AcPMNFSAbortDueToMaxRetriesExceededTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 5, 1, 6),
    _AcPMNFSAbortDueToMaxRetriesExceededTimeBetweenThresholds_Type()
)
acPMNFSAbortDueToMaxRetriesExceededTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSAbortDueToMaxRetriesExceededTimeBetweenThresholds.setStatus("current")


class _AcPMNFSAbortDueToMaxRetriesExceededTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMNFSAbortDueToMaxRetriesExceededTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSAbortDueToMaxRetriesExceededTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMNFSAbortDueToMaxRetriesExceededTimeAboveHighThreshold_Object = MibTableColumn
acPMNFSAbortDueToMaxRetriesExceededTimeAboveHighThreshold = _AcPMNFSAbortDueToMaxRetriesExceededTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 5, 1, 7),
    _AcPMNFSAbortDueToMaxRetriesExceededTimeAboveHighThreshold_Type()
)
acPMNFSAbortDueToMaxRetriesExceededTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSAbortDueToMaxRetriesExceededTimeAboveHighThreshold.setStatus("current")


class _AcPMNFSAbortDueToMaxRetriesExceededFullDayAverage_Type(Integer32):
    """Custom type acPMNFSAbortDueToMaxRetriesExceededFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSAbortDueToMaxRetriesExceededFullDayAverage_Type.__name__ = "Integer32"
_AcPMNFSAbortDueToMaxRetriesExceededFullDayAverage_Object = MibTableColumn
acPMNFSAbortDueToMaxRetriesExceededFullDayAverage = _AcPMNFSAbortDueToMaxRetriesExceededFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 5, 1, 8),
    _AcPMNFSAbortDueToMaxRetriesExceededFullDayAverage_Type()
)
acPMNFSAbortDueToMaxRetriesExceededFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSAbortDueToMaxRetriesExceededFullDayAverage.setStatus("current")
_AcPMNFSDelayedResponsesTable_Object = MibTable
acPMNFSDelayedResponsesTable = _AcPMNFSDelayedResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 6)
)
if mibBuilder.loadTexts:
    acPMNFSDelayedResponsesTable.setStatus("current")
_AcPMNFSDelayedResponsesEntry_Object = MibTableRow
acPMNFSDelayedResponsesEntry = _AcPMNFSDelayedResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 6, 1)
)
acPMNFSDelayedResponsesEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNFSDelayedResponsesRfsNumber"),
    (0, "AC-PM-System-MIB", "acPMNFSDelayedResponsesInterval"),
)
if mibBuilder.loadTexts:
    acPMNFSDelayedResponsesEntry.setStatus("current")


class _AcPMNFSDelayedResponsesRfsNumber_Type(Unsigned32):
    """Custom type acPMNFSDelayedResponsesRfsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcPMNFSDelayedResponsesRfsNumber_Type.__name__ = "Unsigned32"
_AcPMNFSDelayedResponsesRfsNumber_Object = MibTableColumn
acPMNFSDelayedResponsesRfsNumber = _AcPMNFSDelayedResponsesRfsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 6, 1, 1),
    _AcPMNFSDelayedResponsesRfsNumber_Type()
)
acPMNFSDelayedResponsesRfsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSDelayedResponsesRfsNumber.setStatus("current")


class _AcPMNFSDelayedResponsesInterval_Type(Unsigned32):
    """Custom type acPMNFSDelayedResponsesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNFSDelayedResponsesInterval_Type.__name__ = "Unsigned32"
_AcPMNFSDelayedResponsesInterval_Object = MibTableColumn
acPMNFSDelayedResponsesInterval = _AcPMNFSDelayedResponsesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 6, 1, 2),
    _AcPMNFSDelayedResponsesInterval_Type()
)
acPMNFSDelayedResponsesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSDelayedResponsesInterval.setStatus("current")
_AcPMNFSDelayedResponsesVal_Type = Gauge32
_AcPMNFSDelayedResponsesVal_Object = MibTableColumn
acPMNFSDelayedResponsesVal = _AcPMNFSDelayedResponsesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 6, 1, 3),
    _AcPMNFSDelayedResponsesVal_Type()
)
acPMNFSDelayedResponsesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSDelayedResponsesVal.setStatus("current")
_AcPMNFSDelayedResponsesVolume_Type = Counter32
_AcPMNFSDelayedResponsesVolume_Object = MibTableColumn
acPMNFSDelayedResponsesVolume = _AcPMNFSDelayedResponsesVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 6, 1, 4),
    _AcPMNFSDelayedResponsesVolume_Type()
)
acPMNFSDelayedResponsesVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSDelayedResponsesVolume.setStatus("current")


class _AcPMNFSDelayedResponsesTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMNFSDelayedResponsesTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSDelayedResponsesTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMNFSDelayedResponsesTimeBelowLowThreshold_Object = MibTableColumn
acPMNFSDelayedResponsesTimeBelowLowThreshold = _AcPMNFSDelayedResponsesTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 6, 1, 5),
    _AcPMNFSDelayedResponsesTimeBelowLowThreshold_Type()
)
acPMNFSDelayedResponsesTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSDelayedResponsesTimeBelowLowThreshold.setStatus("current")


class _AcPMNFSDelayedResponsesTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMNFSDelayedResponsesTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSDelayedResponsesTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMNFSDelayedResponsesTimeBetweenThresholds_Object = MibTableColumn
acPMNFSDelayedResponsesTimeBetweenThresholds = _AcPMNFSDelayedResponsesTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 6, 1, 6),
    _AcPMNFSDelayedResponsesTimeBetweenThresholds_Type()
)
acPMNFSDelayedResponsesTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSDelayedResponsesTimeBetweenThresholds.setStatus("current")


class _AcPMNFSDelayedResponsesTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMNFSDelayedResponsesTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSDelayedResponsesTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMNFSDelayedResponsesTimeAboveHighThreshold_Object = MibTableColumn
acPMNFSDelayedResponsesTimeAboveHighThreshold = _AcPMNFSDelayedResponsesTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 6, 1, 7),
    _AcPMNFSDelayedResponsesTimeAboveHighThreshold_Type()
)
acPMNFSDelayedResponsesTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSDelayedResponsesTimeAboveHighThreshold.setStatus("current")


class _AcPMNFSDelayedResponsesFullDayAverage_Type(Integer32):
    """Custom type acPMNFSDelayedResponsesFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSDelayedResponsesFullDayAverage_Type.__name__ = "Integer32"
_AcPMNFSDelayedResponsesFullDayAverage_Object = MibTableColumn
acPMNFSDelayedResponsesFullDayAverage = _AcPMNFSDelayedResponsesFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 6, 1, 8),
    _AcPMNFSDelayedResponsesFullDayAverage_Type()
)
acPMNFSDelayedResponsesFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSDelayedResponsesFullDayAverage.setStatus("current")
_AcPMNFSBytesDroppedOnRecordTable_Object = MibTable
acPMNFSBytesDroppedOnRecordTable = _AcPMNFSBytesDroppedOnRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 7)
)
if mibBuilder.loadTexts:
    acPMNFSBytesDroppedOnRecordTable.setStatus("current")
_AcPMNFSBytesDroppedOnRecordEntry_Object = MibTableRow
acPMNFSBytesDroppedOnRecordEntry = _AcPMNFSBytesDroppedOnRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 7, 1)
)
acPMNFSBytesDroppedOnRecordEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNFSBytesDroppedOnRecordRfsNumber"),
    (0, "AC-PM-System-MIB", "acPMNFSBytesDroppedOnRecordInterval"),
)
if mibBuilder.loadTexts:
    acPMNFSBytesDroppedOnRecordEntry.setStatus("current")


class _AcPMNFSBytesDroppedOnRecordRfsNumber_Type(Unsigned32):
    """Custom type acPMNFSBytesDroppedOnRecordRfsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcPMNFSBytesDroppedOnRecordRfsNumber_Type.__name__ = "Unsigned32"
_AcPMNFSBytesDroppedOnRecordRfsNumber_Object = MibTableColumn
acPMNFSBytesDroppedOnRecordRfsNumber = _AcPMNFSBytesDroppedOnRecordRfsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 7, 1, 1),
    _AcPMNFSBytesDroppedOnRecordRfsNumber_Type()
)
acPMNFSBytesDroppedOnRecordRfsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSBytesDroppedOnRecordRfsNumber.setStatus("current")


class _AcPMNFSBytesDroppedOnRecordInterval_Type(Unsigned32):
    """Custom type acPMNFSBytesDroppedOnRecordInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNFSBytesDroppedOnRecordInterval_Type.__name__ = "Unsigned32"
_AcPMNFSBytesDroppedOnRecordInterval_Object = MibTableColumn
acPMNFSBytesDroppedOnRecordInterval = _AcPMNFSBytesDroppedOnRecordInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 7, 1, 2),
    _AcPMNFSBytesDroppedOnRecordInterval_Type()
)
acPMNFSBytesDroppedOnRecordInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSBytesDroppedOnRecordInterval.setStatus("current")
_AcPMNFSBytesDroppedOnRecordVal_Type = Gauge32
_AcPMNFSBytesDroppedOnRecordVal_Object = MibTableColumn
acPMNFSBytesDroppedOnRecordVal = _AcPMNFSBytesDroppedOnRecordVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 7, 1, 3),
    _AcPMNFSBytesDroppedOnRecordVal_Type()
)
acPMNFSBytesDroppedOnRecordVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSBytesDroppedOnRecordVal.setStatus("current")
_AcPMNFSBytesDroppedOnRecordVolume_Type = Counter32
_AcPMNFSBytesDroppedOnRecordVolume_Object = MibTableColumn
acPMNFSBytesDroppedOnRecordVolume = _AcPMNFSBytesDroppedOnRecordVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 7, 1, 4),
    _AcPMNFSBytesDroppedOnRecordVolume_Type()
)
acPMNFSBytesDroppedOnRecordVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSBytesDroppedOnRecordVolume.setStatus("current")


class _AcPMNFSBytesDroppedOnRecordTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMNFSBytesDroppedOnRecordTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSBytesDroppedOnRecordTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMNFSBytesDroppedOnRecordTimeBelowLowThreshold_Object = MibTableColumn
acPMNFSBytesDroppedOnRecordTimeBelowLowThreshold = _AcPMNFSBytesDroppedOnRecordTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 7, 1, 5),
    _AcPMNFSBytesDroppedOnRecordTimeBelowLowThreshold_Type()
)
acPMNFSBytesDroppedOnRecordTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSBytesDroppedOnRecordTimeBelowLowThreshold.setStatus("current")


class _AcPMNFSBytesDroppedOnRecordTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMNFSBytesDroppedOnRecordTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSBytesDroppedOnRecordTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMNFSBytesDroppedOnRecordTimeBetweenThresholds_Object = MibTableColumn
acPMNFSBytesDroppedOnRecordTimeBetweenThresholds = _AcPMNFSBytesDroppedOnRecordTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 7, 1, 6),
    _AcPMNFSBytesDroppedOnRecordTimeBetweenThresholds_Type()
)
acPMNFSBytesDroppedOnRecordTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSBytesDroppedOnRecordTimeBetweenThresholds.setStatus("current")


class _AcPMNFSBytesDroppedOnRecordTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMNFSBytesDroppedOnRecordTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMNFSBytesDroppedOnRecordTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMNFSBytesDroppedOnRecordTimeAboveHighThreshold_Object = MibTableColumn
acPMNFSBytesDroppedOnRecordTimeAboveHighThreshold = _AcPMNFSBytesDroppedOnRecordTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 7, 1, 7),
    _AcPMNFSBytesDroppedOnRecordTimeAboveHighThreshold_Type()
)
acPMNFSBytesDroppedOnRecordTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSBytesDroppedOnRecordTimeAboveHighThreshold.setStatus("current")


class _AcPMNFSBytesDroppedOnRecordFullDayAverage_Type(Integer32):
    """Custom type acPMNFSBytesDroppedOnRecordFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSBytesDroppedOnRecordFullDayAverage_Type.__name__ = "Integer32"
_AcPMNFSBytesDroppedOnRecordFullDayAverage_Object = MibTableColumn
acPMNFSBytesDroppedOnRecordFullDayAverage = _AcPMNFSBytesDroppedOnRecordFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 7, 1, 8),
    _AcPMNFSBytesDroppedOnRecordFullDayAverage_Type()
)
acPMNFSBytesDroppedOnRecordFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSBytesDroppedOnRecordFullDayAverage.setStatus("current")
_AcPMNFSLookupCallsTable_Object = MibTable
acPMNFSLookupCallsTable = _AcPMNFSLookupCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 8)
)
if mibBuilder.loadTexts:
    acPMNFSLookupCallsTable.setStatus("current")
_AcPMNFSLookupCallsEntry_Object = MibTableRow
acPMNFSLookupCallsEntry = _AcPMNFSLookupCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 8, 1)
)
acPMNFSLookupCallsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNFSLookupCallsRfsNumber"),
    (0, "AC-PM-System-MIB", "acPMNFSLookupCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMNFSLookupCallsEntry.setStatus("current")


class _AcPMNFSLookupCallsRfsNumber_Type(Unsigned32):
    """Custom type acPMNFSLookupCallsRfsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcPMNFSLookupCallsRfsNumber_Type.__name__ = "Unsigned32"
_AcPMNFSLookupCallsRfsNumber_Object = MibTableColumn
acPMNFSLookupCallsRfsNumber = _AcPMNFSLookupCallsRfsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 8, 1, 1),
    _AcPMNFSLookupCallsRfsNumber_Type()
)
acPMNFSLookupCallsRfsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSLookupCallsRfsNumber.setStatus("current")


class _AcPMNFSLookupCallsInterval_Type(Unsigned32):
    """Custom type acPMNFSLookupCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNFSLookupCallsInterval_Type.__name__ = "Unsigned32"
_AcPMNFSLookupCallsInterval_Object = MibTableColumn
acPMNFSLookupCallsInterval = _AcPMNFSLookupCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 8, 1, 2),
    _AcPMNFSLookupCallsInterval_Type()
)
acPMNFSLookupCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSLookupCallsInterval.setStatus("current")
_AcPMNFSLookupCallsVal_Type = Counter32
_AcPMNFSLookupCallsVal_Object = MibTableColumn
acPMNFSLookupCallsVal = _AcPMNFSLookupCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 8, 1, 3),
    _AcPMNFSLookupCallsVal_Type()
)
acPMNFSLookupCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSLookupCallsVal.setStatus("current")
_AcPMNFSLookupCallsVolume_Type = Counter32
_AcPMNFSLookupCallsVolume_Object = MibTableColumn
acPMNFSLookupCallsVolume = _AcPMNFSLookupCallsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 8, 1, 4),
    _AcPMNFSLookupCallsVolume_Type()
)
acPMNFSLookupCallsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSLookupCallsVolume.setStatus("current")


class _AcPMNFSLookupCallsFullDayAverage_Type(Integer32):
    """Custom type acPMNFSLookupCallsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSLookupCallsFullDayAverage_Type.__name__ = "Integer32"
_AcPMNFSLookupCallsFullDayAverage_Object = MibTableColumn
acPMNFSLookupCallsFullDayAverage = _AcPMNFSLookupCallsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 8, 1, 5),
    _AcPMNFSLookupCallsFullDayAverage_Type()
)
acPMNFSLookupCallsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSLookupCallsFullDayAverage.setStatus("current")
_AcPMNFSCreateCallsTable_Object = MibTable
acPMNFSCreateCallsTable = _AcPMNFSCreateCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 9)
)
if mibBuilder.loadTexts:
    acPMNFSCreateCallsTable.setStatus("current")
_AcPMNFSCreateCallsEntry_Object = MibTableRow
acPMNFSCreateCallsEntry = _AcPMNFSCreateCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 9, 1)
)
acPMNFSCreateCallsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNFSCreateCallsRfsNumber"),
    (0, "AC-PM-System-MIB", "acPMNFSCreateCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMNFSCreateCallsEntry.setStatus("current")


class _AcPMNFSCreateCallsRfsNumber_Type(Unsigned32):
    """Custom type acPMNFSCreateCallsRfsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcPMNFSCreateCallsRfsNumber_Type.__name__ = "Unsigned32"
_AcPMNFSCreateCallsRfsNumber_Object = MibTableColumn
acPMNFSCreateCallsRfsNumber = _AcPMNFSCreateCallsRfsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 9, 1, 1),
    _AcPMNFSCreateCallsRfsNumber_Type()
)
acPMNFSCreateCallsRfsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSCreateCallsRfsNumber.setStatus("current")


class _AcPMNFSCreateCallsInterval_Type(Unsigned32):
    """Custom type acPMNFSCreateCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNFSCreateCallsInterval_Type.__name__ = "Unsigned32"
_AcPMNFSCreateCallsInterval_Object = MibTableColumn
acPMNFSCreateCallsInterval = _AcPMNFSCreateCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 9, 1, 2),
    _AcPMNFSCreateCallsInterval_Type()
)
acPMNFSCreateCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSCreateCallsInterval.setStatus("current")
_AcPMNFSCreateCallsVal_Type = Counter32
_AcPMNFSCreateCallsVal_Object = MibTableColumn
acPMNFSCreateCallsVal = _AcPMNFSCreateCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 9, 1, 3),
    _AcPMNFSCreateCallsVal_Type()
)
acPMNFSCreateCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSCreateCallsVal.setStatus("current")
_AcPMNFSCreateCallsVolume_Type = Counter32
_AcPMNFSCreateCallsVolume_Object = MibTableColumn
acPMNFSCreateCallsVolume = _AcPMNFSCreateCallsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 9, 1, 4),
    _AcPMNFSCreateCallsVolume_Type()
)
acPMNFSCreateCallsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSCreateCallsVolume.setStatus("current")


class _AcPMNFSCreateCallsFullDayAverage_Type(Integer32):
    """Custom type acPMNFSCreateCallsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSCreateCallsFullDayAverage_Type.__name__ = "Integer32"
_AcPMNFSCreateCallsFullDayAverage_Object = MibTableColumn
acPMNFSCreateCallsFullDayAverage = _AcPMNFSCreateCallsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 9, 1, 5),
    _AcPMNFSCreateCallsFullDayAverage_Type()
)
acPMNFSCreateCallsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSCreateCallsFullDayAverage.setStatus("current")
_AcPMNFSReadCallsTable_Object = MibTable
acPMNFSReadCallsTable = _AcPMNFSReadCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 10)
)
if mibBuilder.loadTexts:
    acPMNFSReadCallsTable.setStatus("current")
_AcPMNFSReadCallsEntry_Object = MibTableRow
acPMNFSReadCallsEntry = _AcPMNFSReadCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 10, 1)
)
acPMNFSReadCallsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNFSReadCallsRfsNumber"),
    (0, "AC-PM-System-MIB", "acPMNFSReadCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMNFSReadCallsEntry.setStatus("current")


class _AcPMNFSReadCallsRfsNumber_Type(Unsigned32):
    """Custom type acPMNFSReadCallsRfsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcPMNFSReadCallsRfsNumber_Type.__name__ = "Unsigned32"
_AcPMNFSReadCallsRfsNumber_Object = MibTableColumn
acPMNFSReadCallsRfsNumber = _AcPMNFSReadCallsRfsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 10, 1, 1),
    _AcPMNFSReadCallsRfsNumber_Type()
)
acPMNFSReadCallsRfsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSReadCallsRfsNumber.setStatus("current")


class _AcPMNFSReadCallsInterval_Type(Unsigned32):
    """Custom type acPMNFSReadCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNFSReadCallsInterval_Type.__name__ = "Unsigned32"
_AcPMNFSReadCallsInterval_Object = MibTableColumn
acPMNFSReadCallsInterval = _AcPMNFSReadCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 10, 1, 2),
    _AcPMNFSReadCallsInterval_Type()
)
acPMNFSReadCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSReadCallsInterval.setStatus("current")
_AcPMNFSReadCallsVal_Type = Counter32
_AcPMNFSReadCallsVal_Object = MibTableColumn
acPMNFSReadCallsVal = _AcPMNFSReadCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 10, 1, 3),
    _AcPMNFSReadCallsVal_Type()
)
acPMNFSReadCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSReadCallsVal.setStatus("current")
_AcPMNFSReadCallsVolume_Type = Counter32
_AcPMNFSReadCallsVolume_Object = MibTableColumn
acPMNFSReadCallsVolume = _AcPMNFSReadCallsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 10, 1, 4),
    _AcPMNFSReadCallsVolume_Type()
)
acPMNFSReadCallsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSReadCallsVolume.setStatus("current")


class _AcPMNFSReadCallsFullDayAverage_Type(Integer32):
    """Custom type acPMNFSReadCallsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSReadCallsFullDayAverage_Type.__name__ = "Integer32"
_AcPMNFSReadCallsFullDayAverage_Object = MibTableColumn
acPMNFSReadCallsFullDayAverage = _AcPMNFSReadCallsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 10, 1, 5),
    _AcPMNFSReadCallsFullDayAverage_Type()
)
acPMNFSReadCallsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSReadCallsFullDayAverage.setStatus("current")
_AcPMNFSWriteCallsTable_Object = MibTable
acPMNFSWriteCallsTable = _AcPMNFSWriteCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 11)
)
if mibBuilder.loadTexts:
    acPMNFSWriteCallsTable.setStatus("current")
_AcPMNFSWriteCallsEntry_Object = MibTableRow
acPMNFSWriteCallsEntry = _AcPMNFSWriteCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 11, 1)
)
acPMNFSWriteCallsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMNFSWriteCallsRfsNumber"),
    (0, "AC-PM-System-MIB", "acPMNFSWriteCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMNFSWriteCallsEntry.setStatus("current")


class _AcPMNFSWriteCallsRfsNumber_Type(Unsigned32):
    """Custom type acPMNFSWriteCallsRfsNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcPMNFSWriteCallsRfsNumber_Type.__name__ = "Unsigned32"
_AcPMNFSWriteCallsRfsNumber_Object = MibTableColumn
acPMNFSWriteCallsRfsNumber = _AcPMNFSWriteCallsRfsNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 11, 1, 1),
    _AcPMNFSWriteCallsRfsNumber_Type()
)
acPMNFSWriteCallsRfsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSWriteCallsRfsNumber.setStatus("current")


class _AcPMNFSWriteCallsInterval_Type(Unsigned32):
    """Custom type acPMNFSWriteCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMNFSWriteCallsInterval_Type.__name__ = "Unsigned32"
_AcPMNFSWriteCallsInterval_Object = MibTableColumn
acPMNFSWriteCallsInterval = _AcPMNFSWriteCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 11, 1, 2),
    _AcPMNFSWriteCallsInterval_Type()
)
acPMNFSWriteCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMNFSWriteCallsInterval.setStatus("current")
_AcPMNFSWriteCallsVal_Type = Counter32
_AcPMNFSWriteCallsVal_Object = MibTableColumn
acPMNFSWriteCallsVal = _AcPMNFSWriteCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 11, 1, 3),
    _AcPMNFSWriteCallsVal_Type()
)
acPMNFSWriteCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSWriteCallsVal.setStatus("current")
_AcPMNFSWriteCallsVolume_Type = Counter32
_AcPMNFSWriteCallsVolume_Object = MibTableColumn
acPMNFSWriteCallsVolume = _AcPMNFSWriteCallsVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 11, 1, 4),
    _AcPMNFSWriteCallsVolume_Type()
)
acPMNFSWriteCallsVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSWriteCallsVolume.setStatus("current")


class _AcPMNFSWriteCallsFullDayAverage_Type(Integer32):
    """Custom type acPMNFSWriteCallsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMNFSWriteCallsFullDayAverage_Type.__name__ = "Integer32"
_AcPMNFSWriteCallsFullDayAverage_Object = MibTableColumn
acPMNFSWriteCallsFullDayAverage = _AcPMNFSWriteCallsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 91, 11, 1, 5),
    _AcPMNFSWriteCallsFullDayAverage_Type()
)
acPMNFSWriteCallsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMNFSWriteCallsFullDayAverage.setStatus("current")
_AcPMSystemMSBG_ObjectIdentity = ObjectIdentity
acPMSystemMSBG = _AcPMSystemMSBG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101)
)
_AcPMRXGoodOctetsTable_Object = MibTable
acPMRXGoodOctetsTable = _AcPMRXGoodOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1)
)
if mibBuilder.loadTexts:
    acPMRXGoodOctetsTable.setStatus("current")
_AcPMRXGoodOctetsEntry_Object = MibTableRow
acPMRXGoodOctetsEntry = _AcPMRXGoodOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1, 1)
)
acPMRXGoodOctetsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMRXGoodOctetsInterfaceNum"),
    (0, "AC-PM-System-MIB", "acPMRXGoodOctetsInterval"),
)
if mibBuilder.loadTexts:
    acPMRXGoodOctetsEntry.setStatus("current")


class _AcPMRXGoodOctetsInterfaceNum_Type(Unsigned32):
    """Custom type acPMRXGoodOctetsInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcPMRXGoodOctetsInterfaceNum_Type.__name__ = "Unsigned32"
_AcPMRXGoodOctetsInterfaceNum_Object = MibTableColumn
acPMRXGoodOctetsInterfaceNum = _AcPMRXGoodOctetsInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1, 1, 1),
    _AcPMRXGoodOctetsInterfaceNum_Type()
)
acPMRXGoodOctetsInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXGoodOctetsInterfaceNum.setStatus("current")


class _AcPMRXGoodOctetsInterval_Type(Unsigned32):
    """Custom type acPMRXGoodOctetsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRXGoodOctetsInterval_Type.__name__ = "Unsigned32"
_AcPMRXGoodOctetsInterval_Object = MibTableColumn
acPMRXGoodOctetsInterval = _AcPMRXGoodOctetsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1, 1, 2),
    _AcPMRXGoodOctetsInterval_Type()
)
acPMRXGoodOctetsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXGoodOctetsInterval.setStatus("current")
_AcPMRXGoodOctetsVal_Type = Gauge32
_AcPMRXGoodOctetsVal_Object = MibTableColumn
acPMRXGoodOctetsVal = _AcPMRXGoodOctetsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1, 1, 3),
    _AcPMRXGoodOctetsVal_Type()
)
acPMRXGoodOctetsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXGoodOctetsVal.setStatus("current")


class _AcPMRXGoodOctetsAverage_Type(Integer32):
    """Custom type acPMRXGoodOctetsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXGoodOctetsAverage_Type.__name__ = "Integer32"
_AcPMRXGoodOctetsAverage_Object = MibTableColumn
acPMRXGoodOctetsAverage = _AcPMRXGoodOctetsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1, 1, 4),
    _AcPMRXGoodOctetsAverage_Type()
)
acPMRXGoodOctetsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXGoodOctetsAverage.setStatus("current")


class _AcPMRXGoodOctetsMax_Type(Integer32):
    """Custom type acPMRXGoodOctetsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXGoodOctetsMax_Type.__name__ = "Integer32"
_AcPMRXGoodOctetsMax_Object = MibTableColumn
acPMRXGoodOctetsMax = _AcPMRXGoodOctetsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1, 1, 5),
    _AcPMRXGoodOctetsMax_Type()
)
acPMRXGoodOctetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXGoodOctetsMax.setStatus("current")


class _AcPMRXGoodOctetsMin_Type(Integer32):
    """Custom type acPMRXGoodOctetsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXGoodOctetsMin_Type.__name__ = "Integer32"
_AcPMRXGoodOctetsMin_Object = MibTableColumn
acPMRXGoodOctetsMin = _AcPMRXGoodOctetsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1, 1, 6),
    _AcPMRXGoodOctetsMin_Type()
)
acPMRXGoodOctetsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXGoodOctetsMin.setStatus("current")


class _AcPMRXGoodOctetsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRXGoodOctetsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXGoodOctetsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRXGoodOctetsTimeBelowLowThreshold_Object = MibTableColumn
acPMRXGoodOctetsTimeBelowLowThreshold = _AcPMRXGoodOctetsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1, 1, 7),
    _AcPMRXGoodOctetsTimeBelowLowThreshold_Type()
)
acPMRXGoodOctetsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXGoodOctetsTimeBelowLowThreshold.setStatus("current")


class _AcPMRXGoodOctetsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRXGoodOctetsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXGoodOctetsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRXGoodOctetsTimeBetweenThresholds_Object = MibTableColumn
acPMRXGoodOctetsTimeBetweenThresholds = _AcPMRXGoodOctetsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1, 1, 8),
    _AcPMRXGoodOctetsTimeBetweenThresholds_Type()
)
acPMRXGoodOctetsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXGoodOctetsTimeBetweenThresholds.setStatus("current")


class _AcPMRXGoodOctetsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRXGoodOctetsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXGoodOctetsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRXGoodOctetsTimeAboveHighThreshold_Object = MibTableColumn
acPMRXGoodOctetsTimeAboveHighThreshold = _AcPMRXGoodOctetsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1, 1, 9),
    _AcPMRXGoodOctetsTimeAboveHighThreshold_Type()
)
acPMRXGoodOctetsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXGoodOctetsTimeAboveHighThreshold.setStatus("current")


class _AcPMRXGoodOctetsFullDayAverage_Type(Integer32):
    """Custom type acPMRXGoodOctetsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXGoodOctetsFullDayAverage_Type.__name__ = "Integer32"
_AcPMRXGoodOctetsFullDayAverage_Object = MibTableColumn
acPMRXGoodOctetsFullDayAverage = _AcPMRXGoodOctetsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 1, 1, 10),
    _AcPMRXGoodOctetsFullDayAverage_Type()
)
acPMRXGoodOctetsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXGoodOctetsFullDayAverage.setStatus("current")
_AcPMRXBadOctetsTable_Object = MibTable
acPMRXBadOctetsTable = _AcPMRXBadOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2)
)
if mibBuilder.loadTexts:
    acPMRXBadOctetsTable.setStatus("current")
_AcPMRXBadOctetsEntry_Object = MibTableRow
acPMRXBadOctetsEntry = _AcPMRXBadOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2, 1)
)
acPMRXBadOctetsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMRXBadOctetsInterfaceNum"),
    (0, "AC-PM-System-MIB", "acPMRXBadOctetsInterval"),
)
if mibBuilder.loadTexts:
    acPMRXBadOctetsEntry.setStatus("current")


class _AcPMRXBadOctetsInterfaceNum_Type(Unsigned32):
    """Custom type acPMRXBadOctetsInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcPMRXBadOctetsInterfaceNum_Type.__name__ = "Unsigned32"
_AcPMRXBadOctetsInterfaceNum_Object = MibTableColumn
acPMRXBadOctetsInterfaceNum = _AcPMRXBadOctetsInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2, 1, 1),
    _AcPMRXBadOctetsInterfaceNum_Type()
)
acPMRXBadOctetsInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXBadOctetsInterfaceNum.setStatus("current")


class _AcPMRXBadOctetsInterval_Type(Unsigned32):
    """Custom type acPMRXBadOctetsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRXBadOctetsInterval_Type.__name__ = "Unsigned32"
_AcPMRXBadOctetsInterval_Object = MibTableColumn
acPMRXBadOctetsInterval = _AcPMRXBadOctetsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2, 1, 2),
    _AcPMRXBadOctetsInterval_Type()
)
acPMRXBadOctetsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXBadOctetsInterval.setStatus("current")
_AcPMRXBadOctetsVal_Type = Gauge32
_AcPMRXBadOctetsVal_Object = MibTableColumn
acPMRXBadOctetsVal = _AcPMRXBadOctetsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2, 1, 3),
    _AcPMRXBadOctetsVal_Type()
)
acPMRXBadOctetsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXBadOctetsVal.setStatus("current")


class _AcPMRXBadOctetsAverage_Type(Integer32):
    """Custom type acPMRXBadOctetsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXBadOctetsAverage_Type.__name__ = "Integer32"
_AcPMRXBadOctetsAverage_Object = MibTableColumn
acPMRXBadOctetsAverage = _AcPMRXBadOctetsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2, 1, 4),
    _AcPMRXBadOctetsAverage_Type()
)
acPMRXBadOctetsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXBadOctetsAverage.setStatus("current")


class _AcPMRXBadOctetsMax_Type(Integer32):
    """Custom type acPMRXBadOctetsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXBadOctetsMax_Type.__name__ = "Integer32"
_AcPMRXBadOctetsMax_Object = MibTableColumn
acPMRXBadOctetsMax = _AcPMRXBadOctetsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2, 1, 5),
    _AcPMRXBadOctetsMax_Type()
)
acPMRXBadOctetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXBadOctetsMax.setStatus("current")


class _AcPMRXBadOctetsMin_Type(Integer32):
    """Custom type acPMRXBadOctetsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXBadOctetsMin_Type.__name__ = "Integer32"
_AcPMRXBadOctetsMin_Object = MibTableColumn
acPMRXBadOctetsMin = _AcPMRXBadOctetsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2, 1, 6),
    _AcPMRXBadOctetsMin_Type()
)
acPMRXBadOctetsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXBadOctetsMin.setStatus("current")


class _AcPMRXBadOctetsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRXBadOctetsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXBadOctetsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRXBadOctetsTimeBelowLowThreshold_Object = MibTableColumn
acPMRXBadOctetsTimeBelowLowThreshold = _AcPMRXBadOctetsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2, 1, 7),
    _AcPMRXBadOctetsTimeBelowLowThreshold_Type()
)
acPMRXBadOctetsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXBadOctetsTimeBelowLowThreshold.setStatus("current")


class _AcPMRXBadOctetsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRXBadOctetsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXBadOctetsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRXBadOctetsTimeBetweenThresholds_Object = MibTableColumn
acPMRXBadOctetsTimeBetweenThresholds = _AcPMRXBadOctetsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2, 1, 8),
    _AcPMRXBadOctetsTimeBetweenThresholds_Type()
)
acPMRXBadOctetsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXBadOctetsTimeBetweenThresholds.setStatus("current")


class _AcPMRXBadOctetsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRXBadOctetsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXBadOctetsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRXBadOctetsTimeAboveHighThreshold_Object = MibTableColumn
acPMRXBadOctetsTimeAboveHighThreshold = _AcPMRXBadOctetsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2, 1, 9),
    _AcPMRXBadOctetsTimeAboveHighThreshold_Type()
)
acPMRXBadOctetsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXBadOctetsTimeAboveHighThreshold.setStatus("current")


class _AcPMRXBadOctetsFullDayAverage_Type(Integer32):
    """Custom type acPMRXBadOctetsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXBadOctetsFullDayAverage_Type.__name__ = "Integer32"
_AcPMRXBadOctetsFullDayAverage_Object = MibTableColumn
acPMRXBadOctetsFullDayAverage = _AcPMRXBadOctetsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 2, 1, 10),
    _AcPMRXBadOctetsFullDayAverage_Type()
)
acPMRXBadOctetsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXBadOctetsFullDayAverage.setStatus("current")
_AcPMRXUndersizePacketsTable_Object = MibTable
acPMRXUndersizePacketsTable = _AcPMRXUndersizePacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3)
)
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsTable.setStatus("current")
_AcPMRXUndersizePacketsEntry_Object = MibTableRow
acPMRXUndersizePacketsEntry = _AcPMRXUndersizePacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3, 1)
)
acPMRXUndersizePacketsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMRXUndersizePacketsInterfaceNum"),
    (0, "AC-PM-System-MIB", "acPMRXUndersizePacketsInterval"),
)
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsEntry.setStatus("current")


class _AcPMRXUndersizePacketsInterfaceNum_Type(Unsigned32):
    """Custom type acPMRXUndersizePacketsInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcPMRXUndersizePacketsInterfaceNum_Type.__name__ = "Unsigned32"
_AcPMRXUndersizePacketsInterfaceNum_Object = MibTableColumn
acPMRXUndersizePacketsInterfaceNum = _AcPMRXUndersizePacketsInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3, 1, 1),
    _AcPMRXUndersizePacketsInterfaceNum_Type()
)
acPMRXUndersizePacketsInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsInterfaceNum.setStatus("current")


class _AcPMRXUndersizePacketsInterval_Type(Unsigned32):
    """Custom type acPMRXUndersizePacketsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRXUndersizePacketsInterval_Type.__name__ = "Unsigned32"
_AcPMRXUndersizePacketsInterval_Object = MibTableColumn
acPMRXUndersizePacketsInterval = _AcPMRXUndersizePacketsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3, 1, 2),
    _AcPMRXUndersizePacketsInterval_Type()
)
acPMRXUndersizePacketsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsInterval.setStatus("current")
_AcPMRXUndersizePacketsVal_Type = Gauge32
_AcPMRXUndersizePacketsVal_Object = MibTableColumn
acPMRXUndersizePacketsVal = _AcPMRXUndersizePacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3, 1, 3),
    _AcPMRXUndersizePacketsVal_Type()
)
acPMRXUndersizePacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsVal.setStatus("current")


class _AcPMRXUndersizePacketsAverage_Type(Integer32):
    """Custom type acPMRXUndersizePacketsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXUndersizePacketsAverage_Type.__name__ = "Integer32"
_AcPMRXUndersizePacketsAverage_Object = MibTableColumn
acPMRXUndersizePacketsAverage = _AcPMRXUndersizePacketsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3, 1, 4),
    _AcPMRXUndersizePacketsAverage_Type()
)
acPMRXUndersizePacketsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsAverage.setStatus("current")


class _AcPMRXUndersizePacketsMax_Type(Integer32):
    """Custom type acPMRXUndersizePacketsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXUndersizePacketsMax_Type.__name__ = "Integer32"
_AcPMRXUndersizePacketsMax_Object = MibTableColumn
acPMRXUndersizePacketsMax = _AcPMRXUndersizePacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3, 1, 5),
    _AcPMRXUndersizePacketsMax_Type()
)
acPMRXUndersizePacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsMax.setStatus("current")


class _AcPMRXUndersizePacketsMin_Type(Integer32):
    """Custom type acPMRXUndersizePacketsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXUndersizePacketsMin_Type.__name__ = "Integer32"
_AcPMRXUndersizePacketsMin_Object = MibTableColumn
acPMRXUndersizePacketsMin = _AcPMRXUndersizePacketsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3, 1, 6),
    _AcPMRXUndersizePacketsMin_Type()
)
acPMRXUndersizePacketsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsMin.setStatus("current")


class _AcPMRXUndersizePacketsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRXUndersizePacketsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXUndersizePacketsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRXUndersizePacketsTimeBelowLowThreshold_Object = MibTableColumn
acPMRXUndersizePacketsTimeBelowLowThreshold = _AcPMRXUndersizePacketsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3, 1, 7),
    _AcPMRXUndersizePacketsTimeBelowLowThreshold_Type()
)
acPMRXUndersizePacketsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsTimeBelowLowThreshold.setStatus("current")


class _AcPMRXUndersizePacketsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRXUndersizePacketsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXUndersizePacketsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRXUndersizePacketsTimeBetweenThresholds_Object = MibTableColumn
acPMRXUndersizePacketsTimeBetweenThresholds = _AcPMRXUndersizePacketsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3, 1, 8),
    _AcPMRXUndersizePacketsTimeBetweenThresholds_Type()
)
acPMRXUndersizePacketsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsTimeBetweenThresholds.setStatus("current")


class _AcPMRXUndersizePacketsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRXUndersizePacketsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXUndersizePacketsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRXUndersizePacketsTimeAboveHighThreshold_Object = MibTableColumn
acPMRXUndersizePacketsTimeAboveHighThreshold = _AcPMRXUndersizePacketsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3, 1, 9),
    _AcPMRXUndersizePacketsTimeAboveHighThreshold_Type()
)
acPMRXUndersizePacketsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsTimeAboveHighThreshold.setStatus("current")


class _AcPMRXUndersizePacketsFullDayAverage_Type(Integer32):
    """Custom type acPMRXUndersizePacketsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXUndersizePacketsFullDayAverage_Type.__name__ = "Integer32"
_AcPMRXUndersizePacketsFullDayAverage_Object = MibTableColumn
acPMRXUndersizePacketsFullDayAverage = _AcPMRXUndersizePacketsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 3, 1, 10),
    _AcPMRXUndersizePacketsFullDayAverage_Type()
)
acPMRXUndersizePacketsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXUndersizePacketsFullDayAverage.setStatus("current")
_AcPMRXOversizePacketsTable_Object = MibTable
acPMRXOversizePacketsTable = _AcPMRXOversizePacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4)
)
if mibBuilder.loadTexts:
    acPMRXOversizePacketsTable.setStatus("current")
_AcPMRXOversizePacketsEntry_Object = MibTableRow
acPMRXOversizePacketsEntry = _AcPMRXOversizePacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4, 1)
)
acPMRXOversizePacketsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMRXOversizePacketsInterfaceNum"),
    (0, "AC-PM-System-MIB", "acPMRXOversizePacketsInterval"),
)
if mibBuilder.loadTexts:
    acPMRXOversizePacketsEntry.setStatus("current")


class _AcPMRXOversizePacketsInterfaceNum_Type(Unsigned32):
    """Custom type acPMRXOversizePacketsInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcPMRXOversizePacketsInterfaceNum_Type.__name__ = "Unsigned32"
_AcPMRXOversizePacketsInterfaceNum_Object = MibTableColumn
acPMRXOversizePacketsInterfaceNum = _AcPMRXOversizePacketsInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4, 1, 1),
    _AcPMRXOversizePacketsInterfaceNum_Type()
)
acPMRXOversizePacketsInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXOversizePacketsInterfaceNum.setStatus("current")


class _AcPMRXOversizePacketsInterval_Type(Unsigned32):
    """Custom type acPMRXOversizePacketsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRXOversizePacketsInterval_Type.__name__ = "Unsigned32"
_AcPMRXOversizePacketsInterval_Object = MibTableColumn
acPMRXOversizePacketsInterval = _AcPMRXOversizePacketsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4, 1, 2),
    _AcPMRXOversizePacketsInterval_Type()
)
acPMRXOversizePacketsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXOversizePacketsInterval.setStatus("current")
_AcPMRXOversizePacketsVal_Type = Gauge32
_AcPMRXOversizePacketsVal_Object = MibTableColumn
acPMRXOversizePacketsVal = _AcPMRXOversizePacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4, 1, 3),
    _AcPMRXOversizePacketsVal_Type()
)
acPMRXOversizePacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXOversizePacketsVal.setStatus("current")


class _AcPMRXOversizePacketsAverage_Type(Integer32):
    """Custom type acPMRXOversizePacketsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXOversizePacketsAverage_Type.__name__ = "Integer32"
_AcPMRXOversizePacketsAverage_Object = MibTableColumn
acPMRXOversizePacketsAverage = _AcPMRXOversizePacketsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4, 1, 4),
    _AcPMRXOversizePacketsAverage_Type()
)
acPMRXOversizePacketsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXOversizePacketsAverage.setStatus("current")


class _AcPMRXOversizePacketsMax_Type(Integer32):
    """Custom type acPMRXOversizePacketsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXOversizePacketsMax_Type.__name__ = "Integer32"
_AcPMRXOversizePacketsMax_Object = MibTableColumn
acPMRXOversizePacketsMax = _AcPMRXOversizePacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4, 1, 5),
    _AcPMRXOversizePacketsMax_Type()
)
acPMRXOversizePacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXOversizePacketsMax.setStatus("current")


class _AcPMRXOversizePacketsMin_Type(Integer32):
    """Custom type acPMRXOversizePacketsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXOversizePacketsMin_Type.__name__ = "Integer32"
_AcPMRXOversizePacketsMin_Object = MibTableColumn
acPMRXOversizePacketsMin = _AcPMRXOversizePacketsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4, 1, 6),
    _AcPMRXOversizePacketsMin_Type()
)
acPMRXOversizePacketsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXOversizePacketsMin.setStatus("current")


class _AcPMRXOversizePacketsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRXOversizePacketsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXOversizePacketsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRXOversizePacketsTimeBelowLowThreshold_Object = MibTableColumn
acPMRXOversizePacketsTimeBelowLowThreshold = _AcPMRXOversizePacketsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4, 1, 7),
    _AcPMRXOversizePacketsTimeBelowLowThreshold_Type()
)
acPMRXOversizePacketsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXOversizePacketsTimeBelowLowThreshold.setStatus("current")


class _AcPMRXOversizePacketsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRXOversizePacketsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXOversizePacketsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRXOversizePacketsTimeBetweenThresholds_Object = MibTableColumn
acPMRXOversizePacketsTimeBetweenThresholds = _AcPMRXOversizePacketsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4, 1, 8),
    _AcPMRXOversizePacketsTimeBetweenThresholds_Type()
)
acPMRXOversizePacketsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXOversizePacketsTimeBetweenThresholds.setStatus("current")


class _AcPMRXOversizePacketsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRXOversizePacketsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXOversizePacketsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRXOversizePacketsTimeAboveHighThreshold_Object = MibTableColumn
acPMRXOversizePacketsTimeAboveHighThreshold = _AcPMRXOversizePacketsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4, 1, 9),
    _AcPMRXOversizePacketsTimeAboveHighThreshold_Type()
)
acPMRXOversizePacketsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXOversizePacketsTimeAboveHighThreshold.setStatus("current")


class _AcPMRXOversizePacketsFullDayAverage_Type(Integer32):
    """Custom type acPMRXOversizePacketsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXOversizePacketsFullDayAverage_Type.__name__ = "Integer32"
_AcPMRXOversizePacketsFullDayAverage_Object = MibTableColumn
acPMRXOversizePacketsFullDayAverage = _AcPMRXOversizePacketsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 4, 1, 10),
    _AcPMRXOversizePacketsFullDayAverage_Type()
)
acPMRXOversizePacketsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXOversizePacketsFullDayAverage.setStatus("current")
_AcPMRXMacErrorsTable_Object = MibTable
acPMRXMacErrorsTable = _AcPMRXMacErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5)
)
if mibBuilder.loadTexts:
    acPMRXMacErrorsTable.setStatus("current")
_AcPMRXMacErrorsEntry_Object = MibTableRow
acPMRXMacErrorsEntry = _AcPMRXMacErrorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5, 1)
)
acPMRXMacErrorsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMRXMacErrorsInterfaceNum"),
    (0, "AC-PM-System-MIB", "acPMRXMacErrorsInterval"),
)
if mibBuilder.loadTexts:
    acPMRXMacErrorsEntry.setStatus("current")


class _AcPMRXMacErrorsInterfaceNum_Type(Unsigned32):
    """Custom type acPMRXMacErrorsInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcPMRXMacErrorsInterfaceNum_Type.__name__ = "Unsigned32"
_AcPMRXMacErrorsInterfaceNum_Object = MibTableColumn
acPMRXMacErrorsInterfaceNum = _AcPMRXMacErrorsInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5, 1, 1),
    _AcPMRXMacErrorsInterfaceNum_Type()
)
acPMRXMacErrorsInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXMacErrorsInterfaceNum.setStatus("current")


class _AcPMRXMacErrorsInterval_Type(Unsigned32):
    """Custom type acPMRXMacErrorsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRXMacErrorsInterval_Type.__name__ = "Unsigned32"
_AcPMRXMacErrorsInterval_Object = MibTableColumn
acPMRXMacErrorsInterval = _AcPMRXMacErrorsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5, 1, 2),
    _AcPMRXMacErrorsInterval_Type()
)
acPMRXMacErrorsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXMacErrorsInterval.setStatus("current")
_AcPMRXMacErrorsVal_Type = Gauge32
_AcPMRXMacErrorsVal_Object = MibTableColumn
acPMRXMacErrorsVal = _AcPMRXMacErrorsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5, 1, 3),
    _AcPMRXMacErrorsVal_Type()
)
acPMRXMacErrorsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXMacErrorsVal.setStatus("current")


class _AcPMRXMacErrorsAverage_Type(Integer32):
    """Custom type acPMRXMacErrorsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXMacErrorsAverage_Type.__name__ = "Integer32"
_AcPMRXMacErrorsAverage_Object = MibTableColumn
acPMRXMacErrorsAverage = _AcPMRXMacErrorsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5, 1, 4),
    _AcPMRXMacErrorsAverage_Type()
)
acPMRXMacErrorsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXMacErrorsAverage.setStatus("current")


class _AcPMRXMacErrorsMax_Type(Integer32):
    """Custom type acPMRXMacErrorsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXMacErrorsMax_Type.__name__ = "Integer32"
_AcPMRXMacErrorsMax_Object = MibTableColumn
acPMRXMacErrorsMax = _AcPMRXMacErrorsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5, 1, 5),
    _AcPMRXMacErrorsMax_Type()
)
acPMRXMacErrorsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXMacErrorsMax.setStatus("current")


class _AcPMRXMacErrorsMin_Type(Integer32):
    """Custom type acPMRXMacErrorsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXMacErrorsMin_Type.__name__ = "Integer32"
_AcPMRXMacErrorsMin_Object = MibTableColumn
acPMRXMacErrorsMin = _AcPMRXMacErrorsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5, 1, 6),
    _AcPMRXMacErrorsMin_Type()
)
acPMRXMacErrorsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXMacErrorsMin.setStatus("current")


class _AcPMRXMacErrorsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRXMacErrorsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXMacErrorsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRXMacErrorsTimeBelowLowThreshold_Object = MibTableColumn
acPMRXMacErrorsTimeBelowLowThreshold = _AcPMRXMacErrorsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5, 1, 7),
    _AcPMRXMacErrorsTimeBelowLowThreshold_Type()
)
acPMRXMacErrorsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXMacErrorsTimeBelowLowThreshold.setStatus("current")


class _AcPMRXMacErrorsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRXMacErrorsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXMacErrorsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRXMacErrorsTimeBetweenThresholds_Object = MibTableColumn
acPMRXMacErrorsTimeBetweenThresholds = _AcPMRXMacErrorsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5, 1, 8),
    _AcPMRXMacErrorsTimeBetweenThresholds_Type()
)
acPMRXMacErrorsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXMacErrorsTimeBetweenThresholds.setStatus("current")


class _AcPMRXMacErrorsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRXMacErrorsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXMacErrorsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRXMacErrorsTimeAboveHighThreshold_Object = MibTableColumn
acPMRXMacErrorsTimeAboveHighThreshold = _AcPMRXMacErrorsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5, 1, 9),
    _AcPMRXMacErrorsTimeAboveHighThreshold_Type()
)
acPMRXMacErrorsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXMacErrorsTimeAboveHighThreshold.setStatus("current")


class _AcPMRXMacErrorsFullDayAverage_Type(Integer32):
    """Custom type acPMRXMacErrorsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXMacErrorsFullDayAverage_Type.__name__ = "Integer32"
_AcPMRXMacErrorsFullDayAverage_Object = MibTableColumn
acPMRXMacErrorsFullDayAverage = _AcPMRXMacErrorsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 5, 1, 10),
    _AcPMRXMacErrorsFullDayAverage_Type()
)
acPMRXMacErrorsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXMacErrorsFullDayAverage.setStatus("current")
_AcPMRXFCSErroredPacketsTable_Object = MibTable
acPMRXFCSErroredPacketsTable = _AcPMRXFCSErroredPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6)
)
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsTable.setStatus("current")
_AcPMRXFCSErroredPacketsEntry_Object = MibTableRow
acPMRXFCSErroredPacketsEntry = _AcPMRXFCSErroredPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6, 1)
)
acPMRXFCSErroredPacketsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMRXFCSErroredPacketsInterfaceNum"),
    (0, "AC-PM-System-MIB", "acPMRXFCSErroredPacketsInterval"),
)
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsEntry.setStatus("current")


class _AcPMRXFCSErroredPacketsInterfaceNum_Type(Unsigned32):
    """Custom type acPMRXFCSErroredPacketsInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcPMRXFCSErroredPacketsInterfaceNum_Type.__name__ = "Unsigned32"
_AcPMRXFCSErroredPacketsInterfaceNum_Object = MibTableColumn
acPMRXFCSErroredPacketsInterfaceNum = _AcPMRXFCSErroredPacketsInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6, 1, 1),
    _AcPMRXFCSErroredPacketsInterfaceNum_Type()
)
acPMRXFCSErroredPacketsInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsInterfaceNum.setStatus("current")


class _AcPMRXFCSErroredPacketsInterval_Type(Unsigned32):
    """Custom type acPMRXFCSErroredPacketsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRXFCSErroredPacketsInterval_Type.__name__ = "Unsigned32"
_AcPMRXFCSErroredPacketsInterval_Object = MibTableColumn
acPMRXFCSErroredPacketsInterval = _AcPMRXFCSErroredPacketsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6, 1, 2),
    _AcPMRXFCSErroredPacketsInterval_Type()
)
acPMRXFCSErroredPacketsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsInterval.setStatus("current")
_AcPMRXFCSErroredPacketsVal_Type = Gauge32
_AcPMRXFCSErroredPacketsVal_Object = MibTableColumn
acPMRXFCSErroredPacketsVal = _AcPMRXFCSErroredPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6, 1, 3),
    _AcPMRXFCSErroredPacketsVal_Type()
)
acPMRXFCSErroredPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsVal.setStatus("current")


class _AcPMRXFCSErroredPacketsAverage_Type(Integer32):
    """Custom type acPMRXFCSErroredPacketsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXFCSErroredPacketsAverage_Type.__name__ = "Integer32"
_AcPMRXFCSErroredPacketsAverage_Object = MibTableColumn
acPMRXFCSErroredPacketsAverage = _AcPMRXFCSErroredPacketsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6, 1, 4),
    _AcPMRXFCSErroredPacketsAverage_Type()
)
acPMRXFCSErroredPacketsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsAverage.setStatus("current")


class _AcPMRXFCSErroredPacketsMax_Type(Integer32):
    """Custom type acPMRXFCSErroredPacketsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXFCSErroredPacketsMax_Type.__name__ = "Integer32"
_AcPMRXFCSErroredPacketsMax_Object = MibTableColumn
acPMRXFCSErroredPacketsMax = _AcPMRXFCSErroredPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6, 1, 5),
    _AcPMRXFCSErroredPacketsMax_Type()
)
acPMRXFCSErroredPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsMax.setStatus("current")


class _AcPMRXFCSErroredPacketsMin_Type(Integer32):
    """Custom type acPMRXFCSErroredPacketsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXFCSErroredPacketsMin_Type.__name__ = "Integer32"
_AcPMRXFCSErroredPacketsMin_Object = MibTableColumn
acPMRXFCSErroredPacketsMin = _AcPMRXFCSErroredPacketsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6, 1, 6),
    _AcPMRXFCSErroredPacketsMin_Type()
)
acPMRXFCSErroredPacketsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsMin.setStatus("current")


class _AcPMRXFCSErroredPacketsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRXFCSErroredPacketsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXFCSErroredPacketsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRXFCSErroredPacketsTimeBelowLowThreshold_Object = MibTableColumn
acPMRXFCSErroredPacketsTimeBelowLowThreshold = _AcPMRXFCSErroredPacketsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6, 1, 7),
    _AcPMRXFCSErroredPacketsTimeBelowLowThreshold_Type()
)
acPMRXFCSErroredPacketsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsTimeBelowLowThreshold.setStatus("current")


class _AcPMRXFCSErroredPacketsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRXFCSErroredPacketsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXFCSErroredPacketsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRXFCSErroredPacketsTimeBetweenThresholds_Object = MibTableColumn
acPMRXFCSErroredPacketsTimeBetweenThresholds = _AcPMRXFCSErroredPacketsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6, 1, 8),
    _AcPMRXFCSErroredPacketsTimeBetweenThresholds_Type()
)
acPMRXFCSErroredPacketsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsTimeBetweenThresholds.setStatus("current")


class _AcPMRXFCSErroredPacketsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRXFCSErroredPacketsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXFCSErroredPacketsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRXFCSErroredPacketsTimeAboveHighThreshold_Object = MibTableColumn
acPMRXFCSErroredPacketsTimeAboveHighThreshold = _AcPMRXFCSErroredPacketsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6, 1, 9),
    _AcPMRXFCSErroredPacketsTimeAboveHighThreshold_Type()
)
acPMRXFCSErroredPacketsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsTimeAboveHighThreshold.setStatus("current")


class _AcPMRXFCSErroredPacketsFullDayAverage_Type(Integer32):
    """Custom type acPMRXFCSErroredPacketsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXFCSErroredPacketsFullDayAverage_Type.__name__ = "Integer32"
_AcPMRXFCSErroredPacketsFullDayAverage_Object = MibTableColumn
acPMRXFCSErroredPacketsFullDayAverage = _AcPMRXFCSErroredPacketsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 6, 1, 10),
    _AcPMRXFCSErroredPacketsFullDayAverage_Type()
)
acPMRXFCSErroredPacketsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXFCSErroredPacketsFullDayAverage.setStatus("current")
_AcPMRXDiscardPacketsTable_Object = MibTable
acPMRXDiscardPacketsTable = _AcPMRXDiscardPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7)
)
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsTable.setStatus("current")
_AcPMRXDiscardPacketsEntry_Object = MibTableRow
acPMRXDiscardPacketsEntry = _AcPMRXDiscardPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7, 1)
)
acPMRXDiscardPacketsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMRXDiscardPacketsInterfaceNum"),
    (0, "AC-PM-System-MIB", "acPMRXDiscardPacketsInterval"),
)
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsEntry.setStatus("current")


class _AcPMRXDiscardPacketsInterfaceNum_Type(Unsigned32):
    """Custom type acPMRXDiscardPacketsInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcPMRXDiscardPacketsInterfaceNum_Type.__name__ = "Unsigned32"
_AcPMRXDiscardPacketsInterfaceNum_Object = MibTableColumn
acPMRXDiscardPacketsInterfaceNum = _AcPMRXDiscardPacketsInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7, 1, 1),
    _AcPMRXDiscardPacketsInterfaceNum_Type()
)
acPMRXDiscardPacketsInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsInterfaceNum.setStatus("current")


class _AcPMRXDiscardPacketsInterval_Type(Unsigned32):
    """Custom type acPMRXDiscardPacketsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMRXDiscardPacketsInterval_Type.__name__ = "Unsigned32"
_AcPMRXDiscardPacketsInterval_Object = MibTableColumn
acPMRXDiscardPacketsInterval = _AcPMRXDiscardPacketsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7, 1, 2),
    _AcPMRXDiscardPacketsInterval_Type()
)
acPMRXDiscardPacketsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsInterval.setStatus("current")
_AcPMRXDiscardPacketsVal_Type = Gauge32
_AcPMRXDiscardPacketsVal_Object = MibTableColumn
acPMRXDiscardPacketsVal = _AcPMRXDiscardPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7, 1, 3),
    _AcPMRXDiscardPacketsVal_Type()
)
acPMRXDiscardPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsVal.setStatus("current")


class _AcPMRXDiscardPacketsAverage_Type(Integer32):
    """Custom type acPMRXDiscardPacketsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXDiscardPacketsAverage_Type.__name__ = "Integer32"
_AcPMRXDiscardPacketsAverage_Object = MibTableColumn
acPMRXDiscardPacketsAverage = _AcPMRXDiscardPacketsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7, 1, 4),
    _AcPMRXDiscardPacketsAverage_Type()
)
acPMRXDiscardPacketsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsAverage.setStatus("current")


class _AcPMRXDiscardPacketsMax_Type(Integer32):
    """Custom type acPMRXDiscardPacketsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXDiscardPacketsMax_Type.__name__ = "Integer32"
_AcPMRXDiscardPacketsMax_Object = MibTableColumn
acPMRXDiscardPacketsMax = _AcPMRXDiscardPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7, 1, 5),
    _AcPMRXDiscardPacketsMax_Type()
)
acPMRXDiscardPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsMax.setStatus("current")


class _AcPMRXDiscardPacketsMin_Type(Integer32):
    """Custom type acPMRXDiscardPacketsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXDiscardPacketsMin_Type.__name__ = "Integer32"
_AcPMRXDiscardPacketsMin_Object = MibTableColumn
acPMRXDiscardPacketsMin = _AcPMRXDiscardPacketsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7, 1, 6),
    _AcPMRXDiscardPacketsMin_Type()
)
acPMRXDiscardPacketsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsMin.setStatus("current")


class _AcPMRXDiscardPacketsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMRXDiscardPacketsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXDiscardPacketsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMRXDiscardPacketsTimeBelowLowThreshold_Object = MibTableColumn
acPMRXDiscardPacketsTimeBelowLowThreshold = _AcPMRXDiscardPacketsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7, 1, 7),
    _AcPMRXDiscardPacketsTimeBelowLowThreshold_Type()
)
acPMRXDiscardPacketsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsTimeBelowLowThreshold.setStatus("current")


class _AcPMRXDiscardPacketsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMRXDiscardPacketsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXDiscardPacketsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMRXDiscardPacketsTimeBetweenThresholds_Object = MibTableColumn
acPMRXDiscardPacketsTimeBetweenThresholds = _AcPMRXDiscardPacketsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7, 1, 8),
    _AcPMRXDiscardPacketsTimeBetweenThresholds_Type()
)
acPMRXDiscardPacketsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsTimeBetweenThresholds.setStatus("current")


class _AcPMRXDiscardPacketsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMRXDiscardPacketsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMRXDiscardPacketsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMRXDiscardPacketsTimeAboveHighThreshold_Object = MibTableColumn
acPMRXDiscardPacketsTimeAboveHighThreshold = _AcPMRXDiscardPacketsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7, 1, 9),
    _AcPMRXDiscardPacketsTimeAboveHighThreshold_Type()
)
acPMRXDiscardPacketsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsTimeAboveHighThreshold.setStatus("current")


class _AcPMRXDiscardPacketsFullDayAverage_Type(Integer32):
    """Custom type acPMRXDiscardPacketsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMRXDiscardPacketsFullDayAverage_Type.__name__ = "Integer32"
_AcPMRXDiscardPacketsFullDayAverage_Object = MibTableColumn
acPMRXDiscardPacketsFullDayAverage = _AcPMRXDiscardPacketsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 7, 1, 10),
    _AcPMRXDiscardPacketsFullDayAverage_Type()
)
acPMRXDiscardPacketsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMRXDiscardPacketsFullDayAverage.setStatus("current")
_AcPMTXOctetsTable_Object = MibTable
acPMTXOctetsTable = _AcPMTXOctetsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8)
)
if mibBuilder.loadTexts:
    acPMTXOctetsTable.setStatus("current")
_AcPMTXOctetsEntry_Object = MibTableRow
acPMTXOctetsEntry = _AcPMTXOctetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8, 1)
)
acPMTXOctetsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMTXOctetsInterfaceNum"),
    (0, "AC-PM-System-MIB", "acPMTXOctetsInterval"),
)
if mibBuilder.loadTexts:
    acPMTXOctetsEntry.setStatus("current")


class _AcPMTXOctetsInterfaceNum_Type(Unsigned32):
    """Custom type acPMTXOctetsInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcPMTXOctetsInterfaceNum_Type.__name__ = "Unsigned32"
_AcPMTXOctetsInterfaceNum_Object = MibTableColumn
acPMTXOctetsInterfaceNum = _AcPMTXOctetsInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8, 1, 1),
    _AcPMTXOctetsInterfaceNum_Type()
)
acPMTXOctetsInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTXOctetsInterfaceNum.setStatus("current")


class _AcPMTXOctetsInterval_Type(Unsigned32):
    """Custom type acPMTXOctetsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMTXOctetsInterval_Type.__name__ = "Unsigned32"
_AcPMTXOctetsInterval_Object = MibTableColumn
acPMTXOctetsInterval = _AcPMTXOctetsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8, 1, 2),
    _AcPMTXOctetsInterval_Type()
)
acPMTXOctetsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTXOctetsInterval.setStatus("current")
_AcPMTXOctetsVal_Type = Gauge32
_AcPMTXOctetsVal_Object = MibTableColumn
acPMTXOctetsVal = _AcPMTXOctetsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8, 1, 3),
    _AcPMTXOctetsVal_Type()
)
acPMTXOctetsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXOctetsVal.setStatus("current")


class _AcPMTXOctetsAverage_Type(Integer32):
    """Custom type acPMTXOctetsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXOctetsAverage_Type.__name__ = "Integer32"
_AcPMTXOctetsAverage_Object = MibTableColumn
acPMTXOctetsAverage = _AcPMTXOctetsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8, 1, 4),
    _AcPMTXOctetsAverage_Type()
)
acPMTXOctetsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXOctetsAverage.setStatus("current")


class _AcPMTXOctetsMax_Type(Integer32):
    """Custom type acPMTXOctetsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXOctetsMax_Type.__name__ = "Integer32"
_AcPMTXOctetsMax_Object = MibTableColumn
acPMTXOctetsMax = _AcPMTXOctetsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8, 1, 5),
    _AcPMTXOctetsMax_Type()
)
acPMTXOctetsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXOctetsMax.setStatus("current")


class _AcPMTXOctetsMin_Type(Integer32):
    """Custom type acPMTXOctetsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXOctetsMin_Type.__name__ = "Integer32"
_AcPMTXOctetsMin_Object = MibTableColumn
acPMTXOctetsMin = _AcPMTXOctetsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8, 1, 6),
    _AcPMTXOctetsMin_Type()
)
acPMTXOctetsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXOctetsMin.setStatus("current")


class _AcPMTXOctetsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMTXOctetsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXOctetsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMTXOctetsTimeBelowLowThreshold_Object = MibTableColumn
acPMTXOctetsTimeBelowLowThreshold = _AcPMTXOctetsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8, 1, 7),
    _AcPMTXOctetsTimeBelowLowThreshold_Type()
)
acPMTXOctetsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXOctetsTimeBelowLowThreshold.setStatus("current")


class _AcPMTXOctetsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMTXOctetsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXOctetsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMTXOctetsTimeBetweenThresholds_Object = MibTableColumn
acPMTXOctetsTimeBetweenThresholds = _AcPMTXOctetsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8, 1, 8),
    _AcPMTXOctetsTimeBetweenThresholds_Type()
)
acPMTXOctetsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXOctetsTimeBetweenThresholds.setStatus("current")


class _AcPMTXOctetsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMTXOctetsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXOctetsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMTXOctetsTimeAboveHighThreshold_Object = MibTableColumn
acPMTXOctetsTimeAboveHighThreshold = _AcPMTXOctetsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8, 1, 9),
    _AcPMTXOctetsTimeAboveHighThreshold_Type()
)
acPMTXOctetsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXOctetsTimeAboveHighThreshold.setStatus("current")


class _AcPMTXOctetsFullDayAverage_Type(Integer32):
    """Custom type acPMTXOctetsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXOctetsFullDayAverage_Type.__name__ = "Integer32"
_AcPMTXOctetsFullDayAverage_Object = MibTableColumn
acPMTXOctetsFullDayAverage = _AcPMTXOctetsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 8, 1, 10),
    _AcPMTXOctetsFullDayAverage_Type()
)
acPMTXOctetsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXOctetsFullDayAverage.setStatus("current")
_AcPMTXPacketsTable_Object = MibTable
acPMTXPacketsTable = _AcPMTXPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9)
)
if mibBuilder.loadTexts:
    acPMTXPacketsTable.setStatus("current")
_AcPMTXPacketsEntry_Object = MibTableRow
acPMTXPacketsEntry = _AcPMTXPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9, 1)
)
acPMTXPacketsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMTXPacketsInterfaceNum"),
    (0, "AC-PM-System-MIB", "acPMTXPacketsInterval"),
)
if mibBuilder.loadTexts:
    acPMTXPacketsEntry.setStatus("current")


class _AcPMTXPacketsInterfaceNum_Type(Unsigned32):
    """Custom type acPMTXPacketsInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcPMTXPacketsInterfaceNum_Type.__name__ = "Unsigned32"
_AcPMTXPacketsInterfaceNum_Object = MibTableColumn
acPMTXPacketsInterfaceNum = _AcPMTXPacketsInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9, 1, 1),
    _AcPMTXPacketsInterfaceNum_Type()
)
acPMTXPacketsInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTXPacketsInterfaceNum.setStatus("current")


class _AcPMTXPacketsInterval_Type(Unsigned32):
    """Custom type acPMTXPacketsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMTXPacketsInterval_Type.__name__ = "Unsigned32"
_AcPMTXPacketsInterval_Object = MibTableColumn
acPMTXPacketsInterval = _AcPMTXPacketsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9, 1, 2),
    _AcPMTXPacketsInterval_Type()
)
acPMTXPacketsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTXPacketsInterval.setStatus("current")
_AcPMTXPacketsVal_Type = Gauge32
_AcPMTXPacketsVal_Object = MibTableColumn
acPMTXPacketsVal = _AcPMTXPacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9, 1, 3),
    _AcPMTXPacketsVal_Type()
)
acPMTXPacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXPacketsVal.setStatus("current")


class _AcPMTXPacketsAverage_Type(Integer32):
    """Custom type acPMTXPacketsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXPacketsAverage_Type.__name__ = "Integer32"
_AcPMTXPacketsAverage_Object = MibTableColumn
acPMTXPacketsAverage = _AcPMTXPacketsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9, 1, 4),
    _AcPMTXPacketsAverage_Type()
)
acPMTXPacketsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXPacketsAverage.setStatus("current")


class _AcPMTXPacketsMax_Type(Integer32):
    """Custom type acPMTXPacketsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXPacketsMax_Type.__name__ = "Integer32"
_AcPMTXPacketsMax_Object = MibTableColumn
acPMTXPacketsMax = _AcPMTXPacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9, 1, 5),
    _AcPMTXPacketsMax_Type()
)
acPMTXPacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXPacketsMax.setStatus("current")


class _AcPMTXPacketsMin_Type(Integer32):
    """Custom type acPMTXPacketsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXPacketsMin_Type.__name__ = "Integer32"
_AcPMTXPacketsMin_Object = MibTableColumn
acPMTXPacketsMin = _AcPMTXPacketsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9, 1, 6),
    _AcPMTXPacketsMin_Type()
)
acPMTXPacketsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXPacketsMin.setStatus("current")


class _AcPMTXPacketsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMTXPacketsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXPacketsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMTXPacketsTimeBelowLowThreshold_Object = MibTableColumn
acPMTXPacketsTimeBelowLowThreshold = _AcPMTXPacketsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9, 1, 7),
    _AcPMTXPacketsTimeBelowLowThreshold_Type()
)
acPMTXPacketsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXPacketsTimeBelowLowThreshold.setStatus("current")


class _AcPMTXPacketsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMTXPacketsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXPacketsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMTXPacketsTimeBetweenThresholds_Object = MibTableColumn
acPMTXPacketsTimeBetweenThresholds = _AcPMTXPacketsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9, 1, 8),
    _AcPMTXPacketsTimeBetweenThresholds_Type()
)
acPMTXPacketsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXPacketsTimeBetweenThresholds.setStatus("current")


class _AcPMTXPacketsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMTXPacketsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXPacketsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMTXPacketsTimeAboveHighThreshold_Object = MibTableColumn
acPMTXPacketsTimeAboveHighThreshold = _AcPMTXPacketsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9, 1, 9),
    _AcPMTXPacketsTimeAboveHighThreshold_Type()
)
acPMTXPacketsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXPacketsTimeAboveHighThreshold.setStatus("current")


class _AcPMTXPacketsFullDayAverage_Type(Integer32):
    """Custom type acPMTXPacketsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXPacketsFullDayAverage_Type.__name__ = "Integer32"
_AcPMTXPacketsFullDayAverage_Object = MibTableColumn
acPMTXPacketsFullDayAverage = _AcPMTXPacketsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 9, 1, 10),
    _AcPMTXPacketsFullDayAverage_Type()
)
acPMTXPacketsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXPacketsFullDayAverage.setStatus("current")
_AcPMTXCollisionsTable_Object = MibTable
acPMTXCollisionsTable = _AcPMTXCollisionsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10)
)
if mibBuilder.loadTexts:
    acPMTXCollisionsTable.setStatus("current")
_AcPMTXCollisionsEntry_Object = MibTableRow
acPMTXCollisionsEntry = _AcPMTXCollisionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10, 1)
)
acPMTXCollisionsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMTXCollisionsInterfaceNum"),
    (0, "AC-PM-System-MIB", "acPMTXCollisionsInterval"),
)
if mibBuilder.loadTexts:
    acPMTXCollisionsEntry.setStatus("current")


class _AcPMTXCollisionsInterfaceNum_Type(Unsigned32):
    """Custom type acPMTXCollisionsInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcPMTXCollisionsInterfaceNum_Type.__name__ = "Unsigned32"
_AcPMTXCollisionsInterfaceNum_Object = MibTableColumn
acPMTXCollisionsInterfaceNum = _AcPMTXCollisionsInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10, 1, 1),
    _AcPMTXCollisionsInterfaceNum_Type()
)
acPMTXCollisionsInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTXCollisionsInterfaceNum.setStatus("current")


class _AcPMTXCollisionsInterval_Type(Unsigned32):
    """Custom type acPMTXCollisionsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMTXCollisionsInterval_Type.__name__ = "Unsigned32"
_AcPMTXCollisionsInterval_Object = MibTableColumn
acPMTXCollisionsInterval = _AcPMTXCollisionsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10, 1, 2),
    _AcPMTXCollisionsInterval_Type()
)
acPMTXCollisionsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTXCollisionsInterval.setStatus("current")
_AcPMTXCollisionsVal_Type = Gauge32
_AcPMTXCollisionsVal_Object = MibTableColumn
acPMTXCollisionsVal = _AcPMTXCollisionsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10, 1, 3),
    _AcPMTXCollisionsVal_Type()
)
acPMTXCollisionsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXCollisionsVal.setStatus("current")


class _AcPMTXCollisionsAverage_Type(Integer32):
    """Custom type acPMTXCollisionsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXCollisionsAverage_Type.__name__ = "Integer32"
_AcPMTXCollisionsAverage_Object = MibTableColumn
acPMTXCollisionsAverage = _AcPMTXCollisionsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10, 1, 4),
    _AcPMTXCollisionsAverage_Type()
)
acPMTXCollisionsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXCollisionsAverage.setStatus("current")


class _AcPMTXCollisionsMax_Type(Integer32):
    """Custom type acPMTXCollisionsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXCollisionsMax_Type.__name__ = "Integer32"
_AcPMTXCollisionsMax_Object = MibTableColumn
acPMTXCollisionsMax = _AcPMTXCollisionsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10, 1, 5),
    _AcPMTXCollisionsMax_Type()
)
acPMTXCollisionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXCollisionsMax.setStatus("current")


class _AcPMTXCollisionsMin_Type(Integer32):
    """Custom type acPMTXCollisionsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXCollisionsMin_Type.__name__ = "Integer32"
_AcPMTXCollisionsMin_Object = MibTableColumn
acPMTXCollisionsMin = _AcPMTXCollisionsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10, 1, 6),
    _AcPMTXCollisionsMin_Type()
)
acPMTXCollisionsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXCollisionsMin.setStatus("current")


class _AcPMTXCollisionsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMTXCollisionsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXCollisionsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMTXCollisionsTimeBelowLowThreshold_Object = MibTableColumn
acPMTXCollisionsTimeBelowLowThreshold = _AcPMTXCollisionsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10, 1, 7),
    _AcPMTXCollisionsTimeBelowLowThreshold_Type()
)
acPMTXCollisionsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXCollisionsTimeBelowLowThreshold.setStatus("current")


class _AcPMTXCollisionsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMTXCollisionsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXCollisionsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMTXCollisionsTimeBetweenThresholds_Object = MibTableColumn
acPMTXCollisionsTimeBetweenThresholds = _AcPMTXCollisionsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10, 1, 8),
    _AcPMTXCollisionsTimeBetweenThresholds_Type()
)
acPMTXCollisionsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXCollisionsTimeBetweenThresholds.setStatus("current")


class _AcPMTXCollisionsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMTXCollisionsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXCollisionsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMTXCollisionsTimeAboveHighThreshold_Object = MibTableColumn
acPMTXCollisionsTimeAboveHighThreshold = _AcPMTXCollisionsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10, 1, 9),
    _AcPMTXCollisionsTimeAboveHighThreshold_Type()
)
acPMTXCollisionsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXCollisionsTimeAboveHighThreshold.setStatus("current")


class _AcPMTXCollisionsFullDayAverage_Type(Integer32):
    """Custom type acPMTXCollisionsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXCollisionsFullDayAverage_Type.__name__ = "Integer32"
_AcPMTXCollisionsFullDayAverage_Object = MibTableColumn
acPMTXCollisionsFullDayAverage = _AcPMTXCollisionsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 10, 1, 10),
    _AcPMTXCollisionsFullDayAverage_Type()
)
acPMTXCollisionsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXCollisionsFullDayAverage.setStatus("current")
_AcPMTXLatePacketsTable_Object = MibTable
acPMTXLatePacketsTable = _AcPMTXLatePacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11)
)
if mibBuilder.loadTexts:
    acPMTXLatePacketsTable.setStatus("current")
_AcPMTXLatePacketsEntry_Object = MibTableRow
acPMTXLatePacketsEntry = _AcPMTXLatePacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11, 1)
)
acPMTXLatePacketsEntry.setIndexNames(
    (0, "AC-PM-System-MIB", "acPMTXLatePacketsInterfaceNum"),
    (0, "AC-PM-System-MIB", "acPMTXLatePacketsInterval"),
)
if mibBuilder.loadTexts:
    acPMTXLatePacketsEntry.setStatus("current")


class _AcPMTXLatePacketsInterfaceNum_Type(Unsigned32):
    """Custom type acPMTXLatePacketsInterfaceNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcPMTXLatePacketsInterfaceNum_Type.__name__ = "Unsigned32"
_AcPMTXLatePacketsInterfaceNum_Object = MibTableColumn
acPMTXLatePacketsInterfaceNum = _AcPMTXLatePacketsInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11, 1, 1),
    _AcPMTXLatePacketsInterfaceNum_Type()
)
acPMTXLatePacketsInterfaceNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTXLatePacketsInterfaceNum.setStatus("current")


class _AcPMTXLatePacketsInterval_Type(Unsigned32):
    """Custom type acPMTXLatePacketsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMTXLatePacketsInterval_Type.__name__ = "Unsigned32"
_AcPMTXLatePacketsInterval_Object = MibTableColumn
acPMTXLatePacketsInterval = _AcPMTXLatePacketsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11, 1, 2),
    _AcPMTXLatePacketsInterval_Type()
)
acPMTXLatePacketsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMTXLatePacketsInterval.setStatus("current")
_AcPMTXLatePacketsVal_Type = Gauge32
_AcPMTXLatePacketsVal_Object = MibTableColumn
acPMTXLatePacketsVal = _AcPMTXLatePacketsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11, 1, 3),
    _AcPMTXLatePacketsVal_Type()
)
acPMTXLatePacketsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXLatePacketsVal.setStatus("current")


class _AcPMTXLatePacketsAverage_Type(Integer32):
    """Custom type acPMTXLatePacketsAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXLatePacketsAverage_Type.__name__ = "Integer32"
_AcPMTXLatePacketsAverage_Object = MibTableColumn
acPMTXLatePacketsAverage = _AcPMTXLatePacketsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11, 1, 4),
    _AcPMTXLatePacketsAverage_Type()
)
acPMTXLatePacketsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXLatePacketsAverage.setStatus("current")


class _AcPMTXLatePacketsMax_Type(Integer32):
    """Custom type acPMTXLatePacketsMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXLatePacketsMax_Type.__name__ = "Integer32"
_AcPMTXLatePacketsMax_Object = MibTableColumn
acPMTXLatePacketsMax = _AcPMTXLatePacketsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11, 1, 5),
    _AcPMTXLatePacketsMax_Type()
)
acPMTXLatePacketsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXLatePacketsMax.setStatus("current")


class _AcPMTXLatePacketsMin_Type(Integer32):
    """Custom type acPMTXLatePacketsMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXLatePacketsMin_Type.__name__ = "Integer32"
_AcPMTXLatePacketsMin_Object = MibTableColumn
acPMTXLatePacketsMin = _AcPMTXLatePacketsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11, 1, 6),
    _AcPMTXLatePacketsMin_Type()
)
acPMTXLatePacketsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXLatePacketsMin.setStatus("current")


class _AcPMTXLatePacketsTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMTXLatePacketsTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXLatePacketsTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMTXLatePacketsTimeBelowLowThreshold_Object = MibTableColumn
acPMTXLatePacketsTimeBelowLowThreshold = _AcPMTXLatePacketsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11, 1, 7),
    _AcPMTXLatePacketsTimeBelowLowThreshold_Type()
)
acPMTXLatePacketsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXLatePacketsTimeBelowLowThreshold.setStatus("current")


class _AcPMTXLatePacketsTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMTXLatePacketsTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXLatePacketsTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMTXLatePacketsTimeBetweenThresholds_Object = MibTableColumn
acPMTXLatePacketsTimeBetweenThresholds = _AcPMTXLatePacketsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11, 1, 8),
    _AcPMTXLatePacketsTimeBetweenThresholds_Type()
)
acPMTXLatePacketsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXLatePacketsTimeBetweenThresholds.setStatus("current")


class _AcPMTXLatePacketsTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMTXLatePacketsTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMTXLatePacketsTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMTXLatePacketsTimeAboveHighThreshold_Object = MibTableColumn
acPMTXLatePacketsTimeAboveHighThreshold = _AcPMTXLatePacketsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11, 1, 9),
    _AcPMTXLatePacketsTimeAboveHighThreshold_Type()
)
acPMTXLatePacketsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXLatePacketsTimeAboveHighThreshold.setStatus("current")


class _AcPMTXLatePacketsFullDayAverage_Type(Integer32):
    """Custom type acPMTXLatePacketsFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMTXLatePacketsFullDayAverage_Type.__name__ = "Integer32"
_AcPMTXLatePacketsFullDayAverage_Object = MibTableColumn
acPMTXLatePacketsFullDayAverage = _AcPMTXLatePacketsFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 11, 2, 101, 11, 1, 10),
    _AcPMTXLatePacketsFullDayAverage_Type()
)
acPMTXLatePacketsFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMTXLatePacketsFullDayAverage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-PM-System-MIB",
    **{"acPMSystem": acPMSystem,
       "acPMSystemConfiguration": acPMSystemConfiguration,
       "acPMSystemConfigurationPeriodLength": acPMSystemConfigurationPeriodLength,
       "acPMSystemConfigurationResetTotalCounters": acPMSystemConfigurationResetTotalCounters,
       "acPMNetConnectionAttributes": acPMNetConnectionAttributes,
       "acPMNetConnectionAttributesStateHighThreshold": acPMNetConnectionAttributesStateHighThreshold,
       "acPMNetConnectionAttributesStateLowThreshold": acPMNetConnectionAttributesStateLowThreshold,
       "acPMNetAttributes": acPMNetAttributes,
       "acPMNetAttributesUnknownUDPPortCounterHighThreshold": acPMNetAttributesUnknownUDPPortCounterHighThreshold,
       "acPMNetAttributesUnknownUDPPortCounterLowThreshold": acPMNetAttributesUnknownUDPPortCounterLowThreshold,
       "acPMNetUtilsAttributes": acPMNetUtilsAttributes,
       "acPMNetUtilsAttributesKBytesHighThreshold": acPMNetUtilsAttributesKBytesHighThreshold,
       "acPMNetUtilsAttributesKBytesLowThreshold": acPMNetUtilsAttributesKBytesLowThreshold,
       "acPMNetUtilsAttributesPacketsHighThreshold": acPMNetUtilsAttributesPacketsHighThreshold,
       "acPMNetUtilsAttributesPacketsLowThreshold": acPMNetUtilsAttributesPacketsLowThreshold,
       "acPMNetUtilsAttributesDiscardedPacketsHighThreshold": acPMNetUtilsAttributesDiscardedPacketsHighThreshold,
       "acPMNetUtilsAttributesDiscardedPacketsLowThreshold": acPMNetUtilsAttributesDiscardedPacketsLowThreshold,
       "acPMNetworkAttributes": acPMNetworkAttributes,
       "acPMNetworkAttributesDhcpResponseTimeHighThreshold": acPMNetworkAttributesDhcpResponseTimeHighThreshold,
       "acPMNetworkAttributesDhcpResponseTimeLowThreshold": acPMNetworkAttributesDhcpResponseTimeLowThreshold,
       "acPMCongestionAttributes": acPMCongestionAttributes,
       "acPMCongestionAttributesHighThreshold": acPMCongestionAttributesHighThreshold,
       "acPMCongestionAttributesLowThreshold": acPMCongestionAttributesLowThreshold,
       "acPMNFSAttributes": acPMNFSAttributes,
       "acPMNFSAttributesRoundTripTimeMsHighThreshold": acPMNFSAttributesRoundTripTimeMsHighThreshold,
       "acPMNFSAttributesRoundTripTimeMsLowThreshold": acPMNFSAttributesRoundTripTimeMsLowThreshold,
       "acPMNFSAttributesRetriesHighThreshold": acPMNFSAttributesRetriesHighThreshold,
       "acPMNFSAttributesRetriesLowThreshold": acPMNFSAttributesRetriesLowThreshold,
       "acPMNFSAttributesAbortDueToMaxRetriesExceededHighThreshold": acPMNFSAttributesAbortDueToMaxRetriesExceededHighThreshold,
       "acPMNFSAttributesAbortDueToMaxRetriesExceededLowThreshold": acPMNFSAttributesAbortDueToMaxRetriesExceededLowThreshold,
       "acPMNFSAttributesDelayedResponsesHighThreshold": acPMNFSAttributesDelayedResponsesHighThreshold,
       "acPMNFSAttributesDelayedResponsesLowThreshold": acPMNFSAttributesDelayedResponsesLowThreshold,
       "acPMNFSAttributesBytesDroppedOnRecordHighThreshold": acPMNFSAttributesBytesDroppedOnRecordHighThreshold,
       "acPMNFSAttributesBytesDroppedOnRecordLowThreshold": acPMNFSAttributesBytesDroppedOnRecordLowThreshold,
       "acPMMSBGAttributes": acPMMSBGAttributes,
       "acPMMSBGAttributesRXGoodOctetsHighThreshold": acPMMSBGAttributesRXGoodOctetsHighThreshold,
       "acPMMSBGAttributesRXGoodOctetsLowThreshold": acPMMSBGAttributesRXGoodOctetsLowThreshold,
       "acPMMSBGAttributesRXBadOctetsHighThreshold": acPMMSBGAttributesRXBadOctetsHighThreshold,
       "acPMMSBGAttributesRXBadOctetsLowThreshold": acPMMSBGAttributesRXBadOctetsLowThreshold,
       "acPMMSBGAttributesRXUndersizePacketsHighThreshold": acPMMSBGAttributesRXUndersizePacketsHighThreshold,
       "acPMMSBGAttributesRXUndersizePacketsLowThreshold": acPMMSBGAttributesRXUndersizePacketsLowThreshold,
       "acPMMSBGAttributesRXOversizePacketsHighThreshold": acPMMSBGAttributesRXOversizePacketsHighThreshold,
       "acPMMSBGAttributesRXOversizePacketsLowThreshold": acPMMSBGAttributesRXOversizePacketsLowThreshold,
       "acPMMSBGAttributesRXMacErrorsHighThreshold": acPMMSBGAttributesRXMacErrorsHighThreshold,
       "acPMMSBGAttributesRXMacErrorsLowThreshold": acPMMSBGAttributesRXMacErrorsLowThreshold,
       "acPMMSBGAttributesRXFCSErroredPacketsHighThreshold": acPMMSBGAttributesRXFCSErroredPacketsHighThreshold,
       "acPMMSBGAttributesRXFCSErroredPacketsLowThreshold": acPMMSBGAttributesRXFCSErroredPacketsLowThreshold,
       "acPMMSBGAttributesRXDiscardPacketsHighThreshold": acPMMSBGAttributesRXDiscardPacketsHighThreshold,
       "acPMMSBGAttributesRXDiscardPacketsLowThreshold": acPMMSBGAttributesRXDiscardPacketsLowThreshold,
       "acPMMSBGAttributesTXOctetsHighThreshold": acPMMSBGAttributesTXOctetsHighThreshold,
       "acPMMSBGAttributesTXOctetsLowThreshold": acPMMSBGAttributesTXOctetsLowThreshold,
       "acPMMSBGAttributesTXPacketsHighThreshold": acPMMSBGAttributesTXPacketsHighThreshold,
       "acPMMSBGAttributesTXPacketsLowThreshold": acPMMSBGAttributesTXPacketsLowThreshold,
       "acPMMSBGAttributesTXCollisionsHighThreshold": acPMMSBGAttributesTXCollisionsHighThreshold,
       "acPMMSBGAttributesTXCollisionsLowThreshold": acPMMSBGAttributesTXCollisionsLowThreshold,
       "acPMMSBGAttributesTXLatePacketsHighThreshold": acPMMSBGAttributesTXLatePacketsHighThreshold,
       "acPMMSBGAttributesTXLatePacketsLowThreshold": acPMMSBGAttributesTXLatePacketsLowThreshold,
       "acPMSystemData": acPMSystemData,
       "acPMSystemDataAcPMSystemTimeFromStartOfInterval": acPMSystemDataAcPMSystemTimeFromStartOfInterval,
       "acPMNetConnectionStateTable": acPMNetConnectionStateTable,
       "acPMNetConnectionStateEntry": acPMNetConnectionStateEntry,
       "acPMNetConnectionStateInterval": acPMNetConnectionStateInterval,
       "acPMNetConnectionStateChanges": acPMNetConnectionStateChanges,
       "acPMNetConnectionStateActiveTime": acPMNetConnectionStateActiveTime,
       "acPMNetUnknownUDPPortCounterTable": acPMNetUnknownUDPPortCounterTable,
       "acPMNetUnknownUDPPortCounterEntry": acPMNetUnknownUDPPortCounterEntry,
       "acPMNetUnknownUDPPortCounterInterval": acPMNetUnknownUDPPortCounterInterval,
       "acPMNetUnknownUDPPortCounterVal": acPMNetUnknownUDPPortCounterVal,
       "acPMSystemNetUtils": acPMSystemNetUtils,
       "acPMNetUtilKBytesTable": acPMNetUtilKBytesTable,
       "acPMNetUtilKBytesEntry": acPMNetUtilKBytesEntry,
       "acPMNetUtilKBytesDirection": acPMNetUtilKBytesDirection,
       "acPMNetUtilKBytesInterval": acPMNetUtilKBytesInterval,
       "acPMNetUtilKBytesVal": acPMNetUtilKBytesVal,
       "acPMNetUtilKBytesAverage": acPMNetUtilKBytesAverage,
       "acPMNetUtilKBytesMax": acPMNetUtilKBytesMax,
       "acPMNetUtilKBytesMin": acPMNetUtilKBytesMin,
       "acPMNetUtilKBytesVolume": acPMNetUtilKBytesVolume,
       "acPMNetUtilKBytesTimeBelowLowThreshold": acPMNetUtilKBytesTimeBelowLowThreshold,
       "acPMNetUtilKBytesTimeBetweenThresholds": acPMNetUtilKBytesTimeBetweenThresholds,
       "acPMNetUtilKBytesTimeAboveHighThreshold": acPMNetUtilKBytesTimeAboveHighThreshold,
       "acPMNetUtilKBytesFullDayAverage": acPMNetUtilKBytesFullDayAverage,
       "acPMNetUtilKBytesTotal": acPMNetUtilKBytesTotal,
       "acPMNetUtilPacketsTable": acPMNetUtilPacketsTable,
       "acPMNetUtilPacketsEntry": acPMNetUtilPacketsEntry,
       "acPMNetUtilPacketsDirection": acPMNetUtilPacketsDirection,
       "acPMNetUtilPacketsInterval": acPMNetUtilPacketsInterval,
       "acPMNetUtilPacketsVal": acPMNetUtilPacketsVal,
       "acPMNetUtilPacketsAverage": acPMNetUtilPacketsAverage,
       "acPMNetUtilPacketsMax": acPMNetUtilPacketsMax,
       "acPMNetUtilPacketsMin": acPMNetUtilPacketsMin,
       "acPMNetUtilPacketsVolume": acPMNetUtilPacketsVolume,
       "acPMNetUtilPacketsTimeBelowLowThreshold": acPMNetUtilPacketsTimeBelowLowThreshold,
       "acPMNetUtilPacketsTimeBetweenThresholds": acPMNetUtilPacketsTimeBetweenThresholds,
       "acPMNetUtilPacketsTimeAboveHighThreshold": acPMNetUtilPacketsTimeAboveHighThreshold,
       "acPMNetUtilPacketsFullDayAverage": acPMNetUtilPacketsFullDayAverage,
       "acPMNetUtilPacketsTotal": acPMNetUtilPacketsTotal,
       "acPMNetUtilDiscardedPacketsTable": acPMNetUtilDiscardedPacketsTable,
       "acPMNetUtilDiscardedPacketsEntry": acPMNetUtilDiscardedPacketsEntry,
       "acPMNetUtilDiscardedPacketsInterval": acPMNetUtilDiscardedPacketsInterval,
       "acPMNetUtilDiscardedPacketsVal": acPMNetUtilDiscardedPacketsVal,
       "acPMNetUtilDiscardedPacketsTotal": acPMNetUtilDiscardedPacketsTotal,
       "acPMSystemNetwork": acPMSystemNetwork,
       "acPMDhcpResponseTimeTable": acPMDhcpResponseTimeTable,
       "acPMDhcpResponseTimeEntry": acPMDhcpResponseTimeEntry,
       "acPMDhcpResponseTimeInterval": acPMDhcpResponseTimeInterval,
       "acPMDhcpResponseTimeVal": acPMDhcpResponseTimeVal,
       "acPMDhcpResponseTimeAverage": acPMDhcpResponseTimeAverage,
       "acPMDhcpResponseTimeMax": acPMDhcpResponseTimeMax,
       "acPMDhcpResponseTimeMin": acPMDhcpResponseTimeMin,
       "acPMDhcpResponseTimeVolume": acPMDhcpResponseTimeVolume,
       "acPMDhcpResponseTimeTimeBelowLowThreshold": acPMDhcpResponseTimeTimeBelowLowThreshold,
       "acPMDhcpResponseTimeTimeBetweenThresholds": acPMDhcpResponseTimeTimeBetweenThresholds,
       "acPMDhcpResponseTimeTimeAboveHighThreshold": acPMDhcpResponseTimeTimeAboveHighThreshold,
       "acPMDhcpResponseTimeFullDayAverage": acPMDhcpResponseTimeFullDayAverage,
       "acPMDhcpRequestTable": acPMDhcpRequestTable,
       "acPMDhcpRequestEntry": acPMDhcpRequestEntry,
       "acPMDhcpRequestInterval": acPMDhcpRequestInterval,
       "acPMDhcpRequestVal": acPMDhcpRequestVal,
       "acPMDhcpRequestTotal": acPMDhcpRequestTotal,
       "acPMStunQueryTable": acPMStunQueryTable,
       "acPMStunQueryEntry": acPMStunQueryEntry,
       "acPMStunQueryInterval": acPMStunQueryInterval,
       "acPMStunQueryVal": acPMStunQueryVal,
       "acPMStunDiscoveryTable": acPMStunDiscoveryTable,
       "acPMStunDiscoveryEntry": acPMStunDiscoveryEntry,
       "acPMStunDiscoveryInterval": acPMStunDiscoveryInterval,
       "acPMStunDiscoveryVal": acPMStunDiscoveryVal,
       "acPMStunRetransmissionTable": acPMStunRetransmissionTable,
       "acPMStunRetransmissionEntry": acPMStunRetransmissionEntry,
       "acPMStunRetransmissionInterval": acPMStunRetransmissionInterval,
       "acPMStunRetransmissionVal": acPMStunRetransmissionVal,
       "acPMSystemSctp": acPMSystemSctp,
       "acPMSctpRcvBytesLastSecondTable": acPMSctpRcvBytesLastSecondTable,
       "acPMSctpRcvBytesLastSecondEntry": acPMSctpRcvBytesLastSecondEntry,
       "acPMSctpRcvBytesLastSecondInterval": acPMSctpRcvBytesLastSecondInterval,
       "acPMSctpRcvBytesLastSecondVal": acPMSctpRcvBytesLastSecondVal,
       "acPMSctpRcvBytesLastSecondAverage": acPMSctpRcvBytesLastSecondAverage,
       "acPMSctpRcvBytesLastSecondMax": acPMSctpRcvBytesLastSecondMax,
       "acPMSctpRcvBytesLastSecondMin": acPMSctpRcvBytesLastSecondMin,
       "acPMSctpRcvBytesLastSecondFullDayAverage": acPMSctpRcvBytesLastSecondFullDayAverage,
       "acPMSctpSentBytesLastSecondTable": acPMSctpSentBytesLastSecondTable,
       "acPMSctpSentBytesLastSecondEntry": acPMSctpSentBytesLastSecondEntry,
       "acPMSctpSentBytesLastSecondInterval": acPMSctpSentBytesLastSecondInterval,
       "acPMSctpSentBytesLastSecondVal": acPMSctpSentBytesLastSecondVal,
       "acPMSctpSentBytesLastSecondAverage": acPMSctpSentBytesLastSecondAverage,
       "acPMSctpSentBytesLastSecondMax": acPMSctpSentBytesLastSecondMax,
       "acPMSctpSentBytesLastSecondMin": acPMSctpSentBytesLastSecondMin,
       "acPMSctpSentBytesLastSecondFullDayAverage": acPMSctpSentBytesLastSecondFullDayAverage,
       "acPMSctpRetransBytesTable": acPMSctpRetransBytesTable,
       "acPMSctpRetransBytesEntry": acPMSctpRetransBytesEntry,
       "acPMSctpRetransBytesInterval": acPMSctpRetransBytesInterval,
       "acPMSctpRetransBytesVal": acPMSctpRetransBytesVal,
       "acPMSctpRetransBytesAverage": acPMSctpRetransBytesAverage,
       "acPMSctpRetransBytesMax": acPMSctpRetransBytesMax,
       "acPMSctpRetransBytesMin": acPMSctpRetransBytesMin,
       "acPMSctpRetransBytesFullDayAverage": acPMSctpRetransBytesFullDayAverage,
       "acPMSctpRetransAttemptsTable": acPMSctpRetransAttemptsTable,
       "acPMSctpRetransAttemptsEntry": acPMSctpRetransAttemptsEntry,
       "acPMSctpRetransAttemptsInterval": acPMSctpRetransAttemptsInterval,
       "acPMSctpRetransAttemptsVal": acPMSctpRetransAttemptsVal,
       "acPMSctpRetransAttemptsAverage": acPMSctpRetransAttemptsAverage,
       "acPMSctpRetransAttemptsMax": acPMSctpRetransAttemptsMax,
       "acPMSctpRetransAttemptsMin": acPMSctpRetransAttemptsMin,
       "acPMSctpRetransAttemptsFullDayAverage": acPMSctpRetransAttemptsFullDayAverage,
       "acPMSystemSecurity": acPMSystemSecurity,
       "acPMIPsecCurrentSAsTable": acPMIPsecCurrentSAsTable,
       "acPMIPsecCurrentSAsEntry": acPMIPsecCurrentSAsEntry,
       "acPMIPsecCurrentSAsInterval": acPMIPsecCurrentSAsInterval,
       "acPMIPsecCurrentSAsVal": acPMIPsecCurrentSAsVal,
       "acPMIPsecCurrentSAsAverage": acPMIPsecCurrentSAsAverage,
       "acPMIPsecCurrentSAsMax": acPMIPsecCurrentSAsMax,
       "acPMIPsecCurrentSAsMin": acPMIPsecCurrentSAsMin,
       "acPMIPsecCurrentSAsFullDayAverage": acPMIPsecCurrentSAsFullDayAverage,
       "acPMIPsecCurrentSAsTotal": acPMIPsecCurrentSAsTotal,
       "acPMSystemMulticast": acPMSystemMulticast,
       "acPMMulticastIPPacketsReceivedTable": acPMMulticastIPPacketsReceivedTable,
       "acPMMulticastIPPacketsReceivedEntry": acPMMulticastIPPacketsReceivedEntry,
       "acPMMulticastIPPacketsReceivedInterval": acPMMulticastIPPacketsReceivedInterval,
       "acPMMulticastIPPacketsReceivedVal": acPMMulticastIPPacketsReceivedVal,
       "acPMMulticastIPPacketsReceivedAverage": acPMMulticastIPPacketsReceivedAverage,
       "acPMMulticastIPPacketsReceivedMax": acPMMulticastIPPacketsReceivedMax,
       "acPMMulticastIPPacketsReceivedMin": acPMMulticastIPPacketsReceivedMin,
       "acPMMulticastIPPacketsReceivedFullDayAverage": acPMMulticastIPPacketsReceivedFullDayAverage,
       "acPMMulticastUDPPacketsReceivedTable": acPMMulticastUDPPacketsReceivedTable,
       "acPMMulticastUDPPacketsReceivedEntry": acPMMulticastUDPPacketsReceivedEntry,
       "acPMMulticastUDPPacketsReceivedInterval": acPMMulticastUDPPacketsReceivedInterval,
       "acPMMulticastUDPPacketsReceivedVal": acPMMulticastUDPPacketsReceivedVal,
       "acPMMulticastUDPPacketsReceivedAverage": acPMMulticastUDPPacketsReceivedAverage,
       "acPMMulticastUDPPacketsReceivedMax": acPMMulticastUDPPacketsReceivedMax,
       "acPMMulticastUDPPacketsReceivedMin": acPMMulticastUDPPacketsReceivedMin,
       "acPMMulticastUDPPacketsReceivedFullDayAverage": acPMMulticastUDPPacketsReceivedFullDayAverage,
       "acPMMulticastUDPPacketsRejectedTable": acPMMulticastUDPPacketsRejectedTable,
       "acPMMulticastUDPPacketsRejectedEntry": acPMMulticastUDPPacketsRejectedEntry,
       "acPMMulticastUDPPacketsRejectedInterval": acPMMulticastUDPPacketsRejectedInterval,
       "acPMMulticastUDPPacketsRejectedVal": acPMMulticastUDPPacketsRejectedVal,
       "acPMMulticastUDPPacketsRejectedAverage": acPMMulticastUDPPacketsRejectedAverage,
       "acPMMulticastUDPPacketsRejectedMax": acPMMulticastUDPPacketsRejectedMax,
       "acPMMulticastUDPPacketsRejectedMin": acPMMulticastUDPPacketsRejectedMin,
       "acPMMulticastUDPPacketsRejectedFullDayAverage": acPMMulticastUDPPacketsRejectedFullDayAverage,
       "acPMMulticastIGMPPacketsReceivedTable": acPMMulticastIGMPPacketsReceivedTable,
       "acPMMulticastIGMPPacketsReceivedEntry": acPMMulticastIGMPPacketsReceivedEntry,
       "acPMMulticastIGMPPacketsReceivedInterval": acPMMulticastIGMPPacketsReceivedInterval,
       "acPMMulticastIGMPPacketsReceivedVal": acPMMulticastIGMPPacketsReceivedVal,
       "acPMMulticastIGMPPacketsReceivedAverage": acPMMulticastIGMPPacketsReceivedAverage,
       "acPMMulticastIGMPPacketsReceivedMax": acPMMulticastIGMPPacketsReceivedMax,
       "acPMMulticastIGMPPacketsReceivedMin": acPMMulticastIGMPPacketsReceivedMin,
       "acPMMulticastIGMPPacketsReceivedFullDayAverage": acPMMulticastIGMPPacketsReceivedFullDayAverage,
       "acPMIGMPGeneralQueryReceivedTable": acPMIGMPGeneralQueryReceivedTable,
       "acPMIGMPGeneralQueryReceivedEntry": acPMIGMPGeneralQueryReceivedEntry,
       "acPMIGMPGeneralQueryReceivedInterval": acPMIGMPGeneralQueryReceivedInterval,
       "acPMIGMPGeneralQueryReceivedVal": acPMIGMPGeneralQueryReceivedVal,
       "acPMIGMPGeneralQueryReceivedAverage": acPMIGMPGeneralQueryReceivedAverage,
       "acPMIGMPGeneralQueryReceivedMax": acPMIGMPGeneralQueryReceivedMax,
       "acPMIGMPGeneralQueryReceivedMin": acPMIGMPGeneralQueryReceivedMin,
       "acPMIGMPGeneralQueryReceivedFullDayAverage": acPMIGMPGeneralQueryReceivedFullDayAverage,
       "acPMIGMPSpecificQueryReceivedTable": acPMIGMPSpecificQueryReceivedTable,
       "acPMIGMPSpecificQueryReceivedEntry": acPMIGMPSpecificQueryReceivedEntry,
       "acPMIGMPSpecificQueryReceivedInterval": acPMIGMPSpecificQueryReceivedInterval,
       "acPMIGMPSpecificQueryReceivedVal": acPMIGMPSpecificQueryReceivedVal,
       "acPMIGMPSpecificQueryReceivedAverage": acPMIGMPSpecificQueryReceivedAverage,
       "acPMIGMPSpecificQueryReceivedMax": acPMIGMPSpecificQueryReceivedMax,
       "acPMIGMPSpecificQueryReceivedMin": acPMIGMPSpecificQueryReceivedMin,
       "acPMIGMPSpecificQueryReceivedFullDayAverage": acPMIGMPSpecificQueryReceivedFullDayAverage,
       "acPMIGMPMembershipReportsSentTable": acPMIGMPMembershipReportsSentTable,
       "acPMIGMPMembershipReportsSentEntry": acPMIGMPMembershipReportsSentEntry,
       "acPMIGMPMembershipReportsSentInterval": acPMIGMPMembershipReportsSentInterval,
       "acPMIGMPMembershipReportsSentVal": acPMIGMPMembershipReportsSentVal,
       "acPMIGMPMembershipReportsSentAverage": acPMIGMPMembershipReportsSentAverage,
       "acPMIGMPMembershipReportsSentMax": acPMIGMPMembershipReportsSentMax,
       "acPMIGMPMembershipReportsSentMin": acPMIGMPMembershipReportsSentMin,
       "acPMIGMPMembershipReportsSentFullDayAverage": acPMIGMPMembershipReportsSentFullDayAverage,
       "acPMIGMPLeaveGroupSentTable": acPMIGMPLeaveGroupSentTable,
       "acPMIGMPLeaveGroupSentEntry": acPMIGMPLeaveGroupSentEntry,
       "acPMIGMPLeaveGroupSentInterval": acPMIGMPLeaveGroupSentInterval,
       "acPMIGMPLeaveGroupSentVal": acPMIGMPLeaveGroupSentVal,
       "acPMIGMPLeaveGroupSentAverage": acPMIGMPLeaveGroupSentAverage,
       "acPMIGMPLeaveGroupSentMax": acPMIGMPLeaveGroupSentMax,
       "acPMIGMPLeaveGroupSentMin": acPMIGMPLeaveGroupSentMin,
       "acPMIGMPLeaveGroupSentFullDayAverage": acPMIGMPLeaveGroupSentFullDayAverage,
       "acPMSystemCongestion": acPMSystemCongestion,
       "acPMCongestionGeneralResourcesTable": acPMCongestionGeneralResourcesTable,
       "acPMCongestionGeneralResourcesEntry": acPMCongestionGeneralResourcesEntry,
       "acPMCongestionGeneralResourcesInterval": acPMCongestionGeneralResourcesInterval,
       "acPMCongestionGeneralResourcesVal": acPMCongestionGeneralResourcesVal,
       "acPMCongestionGeneralResourcesAverage": acPMCongestionGeneralResourcesAverage,
       "acPMCongestionGeneralResourcesMax": acPMCongestionGeneralResourcesMax,
       "acPMCongestionGeneralResourcesMin": acPMCongestionGeneralResourcesMin,
       "acPMCongestionGeneralResourcesFullDayAverage": acPMCongestionGeneralResourcesFullDayAverage,
       "acPMCongestionDSPresourcesTable": acPMCongestionDSPresourcesTable,
       "acPMCongestionDSPresourcesEntry": acPMCongestionDSPresourcesEntry,
       "acPMCongestionDSPresourcesInterval": acPMCongestionDSPresourcesInterval,
       "acPMCongestionDSPresourcesVal": acPMCongestionDSPresourcesVal,
       "acPMCongestionDSPresourcesAverage": acPMCongestionDSPresourcesAverage,
       "acPMCongestionDSPresourcesMax": acPMCongestionDSPresourcesMax,
       "acPMCongestionDSPresourcesMin": acPMCongestionDSPresourcesMin,
       "acPMCongestionDSPresourcesFullDayAverage": acPMCongestionDSPresourcesFullDayAverage,
       "acPMCongestionIPresourcesTable": acPMCongestionIPresourcesTable,
       "acPMCongestionIPresourcesEntry": acPMCongestionIPresourcesEntry,
       "acPMCongestionIPresourcesInterval": acPMCongestionIPresourcesInterval,
       "acPMCongestionIPresourcesVal": acPMCongestionIPresourcesVal,
       "acPMCongestionIPresourcesAverage": acPMCongestionIPresourcesAverage,
       "acPMCongestionIPresourcesMax": acPMCongestionIPresourcesMax,
       "acPMCongestionIPresourcesMin": acPMCongestionIPresourcesMin,
       "acPMCongestionIPresourcesFullDayAverage": acPMCongestionIPresourcesFullDayAverage,
       "acPMCongestionATMresourcesTable": acPMCongestionATMresourcesTable,
       "acPMCongestionATMresourcesEntry": acPMCongestionATMresourcesEntry,
       "acPMCongestionATMresourcesInterval": acPMCongestionATMresourcesInterval,
       "acPMCongestionATMresourcesVal": acPMCongestionATMresourcesVal,
       "acPMCongestionATMresourcesAverage": acPMCongestionATMresourcesAverage,
       "acPMCongestionATMresourcesMax": acPMCongestionATMresourcesMax,
       "acPMCongestionATMresourcesMin": acPMCongestionATMresourcesMin,
       "acPMCongestionATMresourcesFullDayAverage": acPMCongestionATMresourcesFullDayAverage,
       "acPMCongestionConferenceResourcesTable": acPMCongestionConferenceResourcesTable,
       "acPMCongestionConferenceResourcesEntry": acPMCongestionConferenceResourcesEntry,
       "acPMCongestionConferenceResourcesInterval": acPMCongestionConferenceResourcesInterval,
       "acPMCongestionConferenceResourcesVal": acPMCongestionConferenceResourcesVal,
       "acPMCongestionConferenceResourcesAverage": acPMCongestionConferenceResourcesAverage,
       "acPMCongestionConferenceResourcesMax": acPMCongestionConferenceResourcesMax,
       "acPMCongestionConferenceResourcesMin": acPMCongestionConferenceResourcesMin,
       "acPMCongestionConferenceResourcesFullDayAverage": acPMCongestionConferenceResourcesFullDayAverage,
       "acPMSystemNFS": acPMSystemNFS,
       "acPMNFSCurrentRequestsTable": acPMNFSCurrentRequestsTable,
       "acPMNFSCurrentRequestsEntry": acPMNFSCurrentRequestsEntry,
       "acPMNFSCurrentRequestsType": acPMNFSCurrentRequestsType,
       "acPMNFSCurrentRequestsInterval": acPMNFSCurrentRequestsInterval,
       "acPMNFSCurrentRequestsVal": acPMNFSCurrentRequestsVal,
       "acPMNFSCurrentRequestsAverage": acPMNFSCurrentRequestsAverage,
       "acPMNFSCurrentRequestsMax": acPMNFSCurrentRequestsMax,
       "acPMNFSCurrentRequestsMin": acPMNFSCurrentRequestsMin,
       "acPMNFSCurrentRequestsFullDayAverage": acPMNFSCurrentRequestsFullDayAverage,
       "acPMNFSRequestsTable": acPMNFSRequestsTable,
       "acPMNFSRequestsEntry": acPMNFSRequestsEntry,
       "acPMNFSRequestsType": acPMNFSRequestsType,
       "acPMNFSRequestsInterval": acPMNFSRequestsInterval,
       "acPMNFSRequestsVal": acPMNFSRequestsVal,
       "acPMNFSRequestsFullDayAverage": acPMNFSRequestsFullDayAverage,
       "acPMNFSRoundTripTimeMsTable": acPMNFSRoundTripTimeMsTable,
       "acPMNFSRoundTripTimeMsEntry": acPMNFSRoundTripTimeMsEntry,
       "acPMNFSRoundTripTimeMsRfsNumber": acPMNFSRoundTripTimeMsRfsNumber,
       "acPMNFSRoundTripTimeMsInterval": acPMNFSRoundTripTimeMsInterval,
       "acPMNFSRoundTripTimeMsVal": acPMNFSRoundTripTimeMsVal,
       "acPMNFSRoundTripTimeMsAverage": acPMNFSRoundTripTimeMsAverage,
       "acPMNFSRoundTripTimeMsMax": acPMNFSRoundTripTimeMsMax,
       "acPMNFSRoundTripTimeMsMin": acPMNFSRoundTripTimeMsMin,
       "acPMNFSRoundTripTimeMsVolume": acPMNFSRoundTripTimeMsVolume,
       "acPMNFSRoundTripTimeMsTimeBelowLowThreshold": acPMNFSRoundTripTimeMsTimeBelowLowThreshold,
       "acPMNFSRoundTripTimeMsTimeBetweenThresholds": acPMNFSRoundTripTimeMsTimeBetweenThresholds,
       "acPMNFSRoundTripTimeMsTimeAboveHighThreshold": acPMNFSRoundTripTimeMsTimeAboveHighThreshold,
       "acPMNFSRoundTripTimeMsFullDayAverage": acPMNFSRoundTripTimeMsFullDayAverage,
       "acPMNFSRetriesTable": acPMNFSRetriesTable,
       "acPMNFSRetriesEntry": acPMNFSRetriesEntry,
       "acPMNFSRetriesRfsNumber": acPMNFSRetriesRfsNumber,
       "acPMNFSRetriesInterval": acPMNFSRetriesInterval,
       "acPMNFSRetriesVal": acPMNFSRetriesVal,
       "acPMNFSRetriesVolume": acPMNFSRetriesVolume,
       "acPMNFSRetriesTimeBelowLowThreshold": acPMNFSRetriesTimeBelowLowThreshold,
       "acPMNFSRetriesTimeBetweenThresholds": acPMNFSRetriesTimeBetweenThresholds,
       "acPMNFSRetriesTimeAboveHighThreshold": acPMNFSRetriesTimeAboveHighThreshold,
       "acPMNFSRetriesFullDayAverage": acPMNFSRetriesFullDayAverage,
       "acPMNFSAbortDueToMaxRetriesExceededTable": acPMNFSAbortDueToMaxRetriesExceededTable,
       "acPMNFSAbortDueToMaxRetriesExceededEntry": acPMNFSAbortDueToMaxRetriesExceededEntry,
       "acPMNFSAbortDueToMaxRetriesExceededRfsNumber": acPMNFSAbortDueToMaxRetriesExceededRfsNumber,
       "acPMNFSAbortDueToMaxRetriesExceededInterval": acPMNFSAbortDueToMaxRetriesExceededInterval,
       "acPMNFSAbortDueToMaxRetriesExceededVal": acPMNFSAbortDueToMaxRetriesExceededVal,
       "acPMNFSAbortDueToMaxRetriesExceededVolume": acPMNFSAbortDueToMaxRetriesExceededVolume,
       "acPMNFSAbortDueToMaxRetriesExceededTimeBelowLowThreshold": acPMNFSAbortDueToMaxRetriesExceededTimeBelowLowThreshold,
       "acPMNFSAbortDueToMaxRetriesExceededTimeBetweenThresholds": acPMNFSAbortDueToMaxRetriesExceededTimeBetweenThresholds,
       "acPMNFSAbortDueToMaxRetriesExceededTimeAboveHighThreshold": acPMNFSAbortDueToMaxRetriesExceededTimeAboveHighThreshold,
       "acPMNFSAbortDueToMaxRetriesExceededFullDayAverage": acPMNFSAbortDueToMaxRetriesExceededFullDayAverage,
       "acPMNFSDelayedResponsesTable": acPMNFSDelayedResponsesTable,
       "acPMNFSDelayedResponsesEntry": acPMNFSDelayedResponsesEntry,
       "acPMNFSDelayedResponsesRfsNumber": acPMNFSDelayedResponsesRfsNumber,
       "acPMNFSDelayedResponsesInterval": acPMNFSDelayedResponsesInterval,
       "acPMNFSDelayedResponsesVal": acPMNFSDelayedResponsesVal,
       "acPMNFSDelayedResponsesVolume": acPMNFSDelayedResponsesVolume,
       "acPMNFSDelayedResponsesTimeBelowLowThreshold": acPMNFSDelayedResponsesTimeBelowLowThreshold,
       "acPMNFSDelayedResponsesTimeBetweenThresholds": acPMNFSDelayedResponsesTimeBetweenThresholds,
       "acPMNFSDelayedResponsesTimeAboveHighThreshold": acPMNFSDelayedResponsesTimeAboveHighThreshold,
       "acPMNFSDelayedResponsesFullDayAverage": acPMNFSDelayedResponsesFullDayAverage,
       "acPMNFSBytesDroppedOnRecordTable": acPMNFSBytesDroppedOnRecordTable,
       "acPMNFSBytesDroppedOnRecordEntry": acPMNFSBytesDroppedOnRecordEntry,
       "acPMNFSBytesDroppedOnRecordRfsNumber": acPMNFSBytesDroppedOnRecordRfsNumber,
       "acPMNFSBytesDroppedOnRecordInterval": acPMNFSBytesDroppedOnRecordInterval,
       "acPMNFSBytesDroppedOnRecordVal": acPMNFSBytesDroppedOnRecordVal,
       "acPMNFSBytesDroppedOnRecordVolume": acPMNFSBytesDroppedOnRecordVolume,
       "acPMNFSBytesDroppedOnRecordTimeBelowLowThreshold": acPMNFSBytesDroppedOnRecordTimeBelowLowThreshold,
       "acPMNFSBytesDroppedOnRecordTimeBetweenThresholds": acPMNFSBytesDroppedOnRecordTimeBetweenThresholds,
       "acPMNFSBytesDroppedOnRecordTimeAboveHighThreshold": acPMNFSBytesDroppedOnRecordTimeAboveHighThreshold,
       "acPMNFSBytesDroppedOnRecordFullDayAverage": acPMNFSBytesDroppedOnRecordFullDayAverage,
       "acPMNFSLookupCallsTable": acPMNFSLookupCallsTable,
       "acPMNFSLookupCallsEntry": acPMNFSLookupCallsEntry,
       "acPMNFSLookupCallsRfsNumber": acPMNFSLookupCallsRfsNumber,
       "acPMNFSLookupCallsInterval": acPMNFSLookupCallsInterval,
       "acPMNFSLookupCallsVal": acPMNFSLookupCallsVal,
       "acPMNFSLookupCallsVolume": acPMNFSLookupCallsVolume,
       "acPMNFSLookupCallsFullDayAverage": acPMNFSLookupCallsFullDayAverage,
       "acPMNFSCreateCallsTable": acPMNFSCreateCallsTable,
       "acPMNFSCreateCallsEntry": acPMNFSCreateCallsEntry,
       "acPMNFSCreateCallsRfsNumber": acPMNFSCreateCallsRfsNumber,
       "acPMNFSCreateCallsInterval": acPMNFSCreateCallsInterval,
       "acPMNFSCreateCallsVal": acPMNFSCreateCallsVal,
       "acPMNFSCreateCallsVolume": acPMNFSCreateCallsVolume,
       "acPMNFSCreateCallsFullDayAverage": acPMNFSCreateCallsFullDayAverage,
       "acPMNFSReadCallsTable": acPMNFSReadCallsTable,
       "acPMNFSReadCallsEntry": acPMNFSReadCallsEntry,
       "acPMNFSReadCallsRfsNumber": acPMNFSReadCallsRfsNumber,
       "acPMNFSReadCallsInterval": acPMNFSReadCallsInterval,
       "acPMNFSReadCallsVal": acPMNFSReadCallsVal,
       "acPMNFSReadCallsVolume": acPMNFSReadCallsVolume,
       "acPMNFSReadCallsFullDayAverage": acPMNFSReadCallsFullDayAverage,
       "acPMNFSWriteCallsTable": acPMNFSWriteCallsTable,
       "acPMNFSWriteCallsEntry": acPMNFSWriteCallsEntry,
       "acPMNFSWriteCallsRfsNumber": acPMNFSWriteCallsRfsNumber,
       "acPMNFSWriteCallsInterval": acPMNFSWriteCallsInterval,
       "acPMNFSWriteCallsVal": acPMNFSWriteCallsVal,
       "acPMNFSWriteCallsVolume": acPMNFSWriteCallsVolume,
       "acPMNFSWriteCallsFullDayAverage": acPMNFSWriteCallsFullDayAverage,
       "acPMSystemMSBG": acPMSystemMSBG,
       "acPMRXGoodOctetsTable": acPMRXGoodOctetsTable,
       "acPMRXGoodOctetsEntry": acPMRXGoodOctetsEntry,
       "acPMRXGoodOctetsInterfaceNum": acPMRXGoodOctetsInterfaceNum,
       "acPMRXGoodOctetsInterval": acPMRXGoodOctetsInterval,
       "acPMRXGoodOctetsVal": acPMRXGoodOctetsVal,
       "acPMRXGoodOctetsAverage": acPMRXGoodOctetsAverage,
       "acPMRXGoodOctetsMax": acPMRXGoodOctetsMax,
       "acPMRXGoodOctetsMin": acPMRXGoodOctetsMin,
       "acPMRXGoodOctetsTimeBelowLowThreshold": acPMRXGoodOctetsTimeBelowLowThreshold,
       "acPMRXGoodOctetsTimeBetweenThresholds": acPMRXGoodOctetsTimeBetweenThresholds,
       "acPMRXGoodOctetsTimeAboveHighThreshold": acPMRXGoodOctetsTimeAboveHighThreshold,
       "acPMRXGoodOctetsFullDayAverage": acPMRXGoodOctetsFullDayAverage,
       "acPMRXBadOctetsTable": acPMRXBadOctetsTable,
       "acPMRXBadOctetsEntry": acPMRXBadOctetsEntry,
       "acPMRXBadOctetsInterfaceNum": acPMRXBadOctetsInterfaceNum,
       "acPMRXBadOctetsInterval": acPMRXBadOctetsInterval,
       "acPMRXBadOctetsVal": acPMRXBadOctetsVal,
       "acPMRXBadOctetsAverage": acPMRXBadOctetsAverage,
       "acPMRXBadOctetsMax": acPMRXBadOctetsMax,
       "acPMRXBadOctetsMin": acPMRXBadOctetsMin,
       "acPMRXBadOctetsTimeBelowLowThreshold": acPMRXBadOctetsTimeBelowLowThreshold,
       "acPMRXBadOctetsTimeBetweenThresholds": acPMRXBadOctetsTimeBetweenThresholds,
       "acPMRXBadOctetsTimeAboveHighThreshold": acPMRXBadOctetsTimeAboveHighThreshold,
       "acPMRXBadOctetsFullDayAverage": acPMRXBadOctetsFullDayAverage,
       "acPMRXUndersizePacketsTable": acPMRXUndersizePacketsTable,
       "acPMRXUndersizePacketsEntry": acPMRXUndersizePacketsEntry,
       "acPMRXUndersizePacketsInterfaceNum": acPMRXUndersizePacketsInterfaceNum,
       "acPMRXUndersizePacketsInterval": acPMRXUndersizePacketsInterval,
       "acPMRXUndersizePacketsVal": acPMRXUndersizePacketsVal,
       "acPMRXUndersizePacketsAverage": acPMRXUndersizePacketsAverage,
       "acPMRXUndersizePacketsMax": acPMRXUndersizePacketsMax,
       "acPMRXUndersizePacketsMin": acPMRXUndersizePacketsMin,
       "acPMRXUndersizePacketsTimeBelowLowThreshold": acPMRXUndersizePacketsTimeBelowLowThreshold,
       "acPMRXUndersizePacketsTimeBetweenThresholds": acPMRXUndersizePacketsTimeBetweenThresholds,
       "acPMRXUndersizePacketsTimeAboveHighThreshold": acPMRXUndersizePacketsTimeAboveHighThreshold,
       "acPMRXUndersizePacketsFullDayAverage": acPMRXUndersizePacketsFullDayAverage,
       "acPMRXOversizePacketsTable": acPMRXOversizePacketsTable,
       "acPMRXOversizePacketsEntry": acPMRXOversizePacketsEntry,
       "acPMRXOversizePacketsInterfaceNum": acPMRXOversizePacketsInterfaceNum,
       "acPMRXOversizePacketsInterval": acPMRXOversizePacketsInterval,
       "acPMRXOversizePacketsVal": acPMRXOversizePacketsVal,
       "acPMRXOversizePacketsAverage": acPMRXOversizePacketsAverage,
       "acPMRXOversizePacketsMax": acPMRXOversizePacketsMax,
       "acPMRXOversizePacketsMin": acPMRXOversizePacketsMin,
       "acPMRXOversizePacketsTimeBelowLowThreshold": acPMRXOversizePacketsTimeBelowLowThreshold,
       "acPMRXOversizePacketsTimeBetweenThresholds": acPMRXOversizePacketsTimeBetweenThresholds,
       "acPMRXOversizePacketsTimeAboveHighThreshold": acPMRXOversizePacketsTimeAboveHighThreshold,
       "acPMRXOversizePacketsFullDayAverage": acPMRXOversizePacketsFullDayAverage,
       "acPMRXMacErrorsTable": acPMRXMacErrorsTable,
       "acPMRXMacErrorsEntry": acPMRXMacErrorsEntry,
       "acPMRXMacErrorsInterfaceNum": acPMRXMacErrorsInterfaceNum,
       "acPMRXMacErrorsInterval": acPMRXMacErrorsInterval,
       "acPMRXMacErrorsVal": acPMRXMacErrorsVal,
       "acPMRXMacErrorsAverage": acPMRXMacErrorsAverage,
       "acPMRXMacErrorsMax": acPMRXMacErrorsMax,
       "acPMRXMacErrorsMin": acPMRXMacErrorsMin,
       "acPMRXMacErrorsTimeBelowLowThreshold": acPMRXMacErrorsTimeBelowLowThreshold,
       "acPMRXMacErrorsTimeBetweenThresholds": acPMRXMacErrorsTimeBetweenThresholds,
       "acPMRXMacErrorsTimeAboveHighThreshold": acPMRXMacErrorsTimeAboveHighThreshold,
       "acPMRXMacErrorsFullDayAverage": acPMRXMacErrorsFullDayAverage,
       "acPMRXFCSErroredPacketsTable": acPMRXFCSErroredPacketsTable,
       "acPMRXFCSErroredPacketsEntry": acPMRXFCSErroredPacketsEntry,
       "acPMRXFCSErroredPacketsInterfaceNum": acPMRXFCSErroredPacketsInterfaceNum,
       "acPMRXFCSErroredPacketsInterval": acPMRXFCSErroredPacketsInterval,
       "acPMRXFCSErroredPacketsVal": acPMRXFCSErroredPacketsVal,
       "acPMRXFCSErroredPacketsAverage": acPMRXFCSErroredPacketsAverage,
       "acPMRXFCSErroredPacketsMax": acPMRXFCSErroredPacketsMax,
       "acPMRXFCSErroredPacketsMin": acPMRXFCSErroredPacketsMin,
       "acPMRXFCSErroredPacketsTimeBelowLowThreshold": acPMRXFCSErroredPacketsTimeBelowLowThreshold,
       "acPMRXFCSErroredPacketsTimeBetweenThresholds": acPMRXFCSErroredPacketsTimeBetweenThresholds,
       "acPMRXFCSErroredPacketsTimeAboveHighThreshold": acPMRXFCSErroredPacketsTimeAboveHighThreshold,
       "acPMRXFCSErroredPacketsFullDayAverage": acPMRXFCSErroredPacketsFullDayAverage,
       "acPMRXDiscardPacketsTable": acPMRXDiscardPacketsTable,
       "acPMRXDiscardPacketsEntry": acPMRXDiscardPacketsEntry,
       "acPMRXDiscardPacketsInterfaceNum": acPMRXDiscardPacketsInterfaceNum,
       "acPMRXDiscardPacketsInterval": acPMRXDiscardPacketsInterval,
       "acPMRXDiscardPacketsVal": acPMRXDiscardPacketsVal,
       "acPMRXDiscardPacketsAverage": acPMRXDiscardPacketsAverage,
       "acPMRXDiscardPacketsMax": acPMRXDiscardPacketsMax,
       "acPMRXDiscardPacketsMin": acPMRXDiscardPacketsMin,
       "acPMRXDiscardPacketsTimeBelowLowThreshold": acPMRXDiscardPacketsTimeBelowLowThreshold,
       "acPMRXDiscardPacketsTimeBetweenThresholds": acPMRXDiscardPacketsTimeBetweenThresholds,
       "acPMRXDiscardPacketsTimeAboveHighThreshold": acPMRXDiscardPacketsTimeAboveHighThreshold,
       "acPMRXDiscardPacketsFullDayAverage": acPMRXDiscardPacketsFullDayAverage,
       "acPMTXOctetsTable": acPMTXOctetsTable,
       "acPMTXOctetsEntry": acPMTXOctetsEntry,
       "acPMTXOctetsInterfaceNum": acPMTXOctetsInterfaceNum,
       "acPMTXOctetsInterval": acPMTXOctetsInterval,
       "acPMTXOctetsVal": acPMTXOctetsVal,
       "acPMTXOctetsAverage": acPMTXOctetsAverage,
       "acPMTXOctetsMax": acPMTXOctetsMax,
       "acPMTXOctetsMin": acPMTXOctetsMin,
       "acPMTXOctetsTimeBelowLowThreshold": acPMTXOctetsTimeBelowLowThreshold,
       "acPMTXOctetsTimeBetweenThresholds": acPMTXOctetsTimeBetweenThresholds,
       "acPMTXOctetsTimeAboveHighThreshold": acPMTXOctetsTimeAboveHighThreshold,
       "acPMTXOctetsFullDayAverage": acPMTXOctetsFullDayAverage,
       "acPMTXPacketsTable": acPMTXPacketsTable,
       "acPMTXPacketsEntry": acPMTXPacketsEntry,
       "acPMTXPacketsInterfaceNum": acPMTXPacketsInterfaceNum,
       "acPMTXPacketsInterval": acPMTXPacketsInterval,
       "acPMTXPacketsVal": acPMTXPacketsVal,
       "acPMTXPacketsAverage": acPMTXPacketsAverage,
       "acPMTXPacketsMax": acPMTXPacketsMax,
       "acPMTXPacketsMin": acPMTXPacketsMin,
       "acPMTXPacketsTimeBelowLowThreshold": acPMTXPacketsTimeBelowLowThreshold,
       "acPMTXPacketsTimeBetweenThresholds": acPMTXPacketsTimeBetweenThresholds,
       "acPMTXPacketsTimeAboveHighThreshold": acPMTXPacketsTimeAboveHighThreshold,
       "acPMTXPacketsFullDayAverage": acPMTXPacketsFullDayAverage,
       "acPMTXCollisionsTable": acPMTXCollisionsTable,
       "acPMTXCollisionsEntry": acPMTXCollisionsEntry,
       "acPMTXCollisionsInterfaceNum": acPMTXCollisionsInterfaceNum,
       "acPMTXCollisionsInterval": acPMTXCollisionsInterval,
       "acPMTXCollisionsVal": acPMTXCollisionsVal,
       "acPMTXCollisionsAverage": acPMTXCollisionsAverage,
       "acPMTXCollisionsMax": acPMTXCollisionsMax,
       "acPMTXCollisionsMin": acPMTXCollisionsMin,
       "acPMTXCollisionsTimeBelowLowThreshold": acPMTXCollisionsTimeBelowLowThreshold,
       "acPMTXCollisionsTimeBetweenThresholds": acPMTXCollisionsTimeBetweenThresholds,
       "acPMTXCollisionsTimeAboveHighThreshold": acPMTXCollisionsTimeAboveHighThreshold,
       "acPMTXCollisionsFullDayAverage": acPMTXCollisionsFullDayAverage,
       "acPMTXLatePacketsTable": acPMTXLatePacketsTable,
       "acPMTXLatePacketsEntry": acPMTXLatePacketsEntry,
       "acPMTXLatePacketsInterfaceNum": acPMTXLatePacketsInterfaceNum,
       "acPMTXLatePacketsInterval": acPMTXLatePacketsInterval,
       "acPMTXLatePacketsVal": acPMTXLatePacketsVal,
       "acPMTXLatePacketsAverage": acPMTXLatePacketsAverage,
       "acPMTXLatePacketsMax": acPMTXLatePacketsMax,
       "acPMTXLatePacketsMin": acPMTXLatePacketsMin,
       "acPMTXLatePacketsTimeBelowLowThreshold": acPMTXLatePacketsTimeBelowLowThreshold,
       "acPMTXLatePacketsTimeBetweenThresholds": acPMTXLatePacketsTimeBetweenThresholds,
       "acPMTXLatePacketsTimeAboveHighThreshold": acPMTXLatePacketsTimeAboveHighThreshold,
       "acPMTXLatePacketsFullDayAverage": acPMTXLatePacketsFullDayAverage}
)
