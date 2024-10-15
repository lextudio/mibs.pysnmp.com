# SNMP MIB module (CISCO-IETF-PIM-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-PIM-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:01:49 2024
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

(cPimCRPEntry,
 cPimIfEntry,
 cPimIfStatus,
 cPimInetMRouteEntry,
 cPimInetMRouteNextHopEntry,
 cPimNbrAddress,
 cPimNbrAddressType,
 cPimNbrEntry,
 cPimNbrIfIndex) = mibBuilder.importSymbols(
    "CISCO-IETF-PIM-MIB",
    "cPimCRPEntry",
    "cPimIfEntry",
    "cPimIfStatus",
    "cPimInetMRouteEntry",
    "cPimInetMRouteNextHopEntry",
    "cPimNbrAddress",
    "cPimNbrAddressType",
    "cPimNbrEntry",
    "cPimNbrIfIndex")

(cpimRPMappingChangeType,) = mibBuilder.importSymbols(
    "CISCO-PIM-MIB",
    "cpimRPMappingChangeType")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(IANAipMRouteProtocol,) = mibBuilder.importSymbols(
    "IANA-RTPROTO-MIB",
    "IANAipMRouteProtocol")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoIetfPimExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 120)
)
ciscoIetfPimExtMIB.setRevisions(
        ("2014-06-12 00:00",
         "2006-08-25 00:00",
         "2005-02-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoIetfPimExtNotifs_ObjectIdentity = ObjectIdentity
ciscoIetfPimExtNotifs = _CiscoIetfPimExtNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 0)
)
_CiscoIetfPimExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIetfPimExtMIBObjects = _CiscoIetfPimExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1)
)
_CiscoPimExt_ObjectIdentity = ObjectIdentity
ciscoPimExt = _CiscoPimExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1)
)
_CpimExtIfTable_Object = MibTable
cpimExtIfTable = _CpimExtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpimExtIfTable.setStatus("current")
_CpimExtIfEntry_Object = MibTableRow
cpimExtIfEntry = _CpimExtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cpimExtIfEntry.setStatus("current")


class _CpimExtIfTrigHelloInterval_Type(Unsigned32):
    """Custom type cpimExtIfTrigHelloInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtIfTrigHelloInterval_Type.__name__ = "Unsigned32"
_CpimExtIfTrigHelloInterval_Object = MibTableColumn
cpimExtIfTrigHelloInterval = _CpimExtIfTrigHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 1),
    _CpimExtIfTrigHelloInterval_Type()
)
cpimExtIfTrigHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfTrigHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    cpimExtIfTrigHelloInterval.setUnits("seconds")


class _CpimExtIfHelloHoldtime_Type(Unsigned32):
    """Custom type cpimExtIfHelloHoldtime based on Unsigned32"""
    defaultValue = 105

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtIfHelloHoldtime_Type.__name__ = "Unsigned32"
_CpimExtIfHelloHoldtime_Object = MibTableColumn
cpimExtIfHelloHoldtime = _CpimExtIfHelloHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 2),
    _CpimExtIfHelloHoldtime_Type()
)
cpimExtIfHelloHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfHelloHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    cpimExtIfHelloHoldtime.setUnits("seconds")


class _CpimExtIfLanPruneDelay_Type(Bits):
    """Custom type cpimExtIfLanPruneDelay based on Bits"""
    defaultBinValue = "01"

    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )

_CpimExtIfLanPruneDelay_Type.__name__ = "Bits"
_CpimExtIfLanPruneDelay_Object = MibTableColumn
cpimExtIfLanPruneDelay = _CpimExtIfLanPruneDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 3),
    _CpimExtIfLanPruneDelay_Type()
)
cpimExtIfLanPruneDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfLanPruneDelay.setStatus("current")


class _CpimExtIfPropagationDelay_Type(Unsigned32):
    """Custom type cpimExtIfPropagationDelay based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CpimExtIfPropagationDelay_Type.__name__ = "Unsigned32"
_CpimExtIfPropagationDelay_Object = MibTableColumn
cpimExtIfPropagationDelay = _CpimExtIfPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 4),
    _CpimExtIfPropagationDelay_Type()
)
cpimExtIfPropagationDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfPropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    cpimExtIfPropagationDelay.setUnits("milliseconds")


class _CpimExtIfOverrideInterval_Type(Unsigned32):
    """Custom type cpimExtIfOverrideInterval based on Unsigned32"""
    defaultValue = 2500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtIfOverrideInterval_Type.__name__ = "Unsigned32"
_CpimExtIfOverrideInterval_Object = MibTableColumn
cpimExtIfOverrideInterval = _CpimExtIfOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 5),
    _CpimExtIfOverrideInterval_Type()
)
cpimExtIfOverrideInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfOverrideInterval.setStatus("current")


class _CpimExtIfGenerationID_Type(Bits):
    """Custom type cpimExtIfGenerationID based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )

_CpimExtIfGenerationID_Type.__name__ = "Bits"
_CpimExtIfGenerationID_Object = MibTableColumn
cpimExtIfGenerationID = _CpimExtIfGenerationID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 6),
    _CpimExtIfGenerationID_Type()
)
cpimExtIfGenerationID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfGenerationID.setStatus("current")


class _CpimExtIfJoinPruneHoldtime_Type(Unsigned32):
    """Custom type cpimExtIfJoinPruneHoldtime based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtIfJoinPruneHoldtime_Type.__name__ = "Unsigned32"
_CpimExtIfJoinPruneHoldtime_Object = MibTableColumn
cpimExtIfJoinPruneHoldtime = _CpimExtIfJoinPruneHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 7),
    _CpimExtIfJoinPruneHoldtime_Type()
)
cpimExtIfJoinPruneHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfJoinPruneHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    cpimExtIfJoinPruneHoldtime.setUnits("seconds")


class _CpimExtIfGraftRetryInterval_Type(Unsigned32):
    """Custom type cpimExtIfGraftRetryInterval based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtIfGraftRetryInterval_Type.__name__ = "Unsigned32"
_CpimExtIfGraftRetryInterval_Object = MibTableColumn
cpimExtIfGraftRetryInterval = _CpimExtIfGraftRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 8),
    _CpimExtIfGraftRetryInterval_Type()
)
cpimExtIfGraftRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfGraftRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cpimExtIfGraftRetryInterval.setUnits("seconds")


class _CpimExtIfMaxGraftRetries_Type(Unsigned32):
    """Custom type cpimExtIfMaxGraftRetries based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpimExtIfMaxGraftRetries_Type.__name__ = "Unsigned32"
_CpimExtIfMaxGraftRetries_Object = MibTableColumn
cpimExtIfMaxGraftRetries = _CpimExtIfMaxGraftRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 9),
    _CpimExtIfMaxGraftRetries_Type()
)
cpimExtIfMaxGraftRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfMaxGraftRetries.setStatus("current")


class _CpimExtIfSRTTLThreshold_Type(Unsigned32):
    """Custom type cpimExtIfSRTTLThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpimExtIfSRTTLThreshold_Type.__name__ = "Unsigned32"
_CpimExtIfSRTTLThreshold_Object = MibTableColumn
cpimExtIfSRTTLThreshold = _CpimExtIfSRTTLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 10),
    _CpimExtIfSRTTLThreshold_Type()
)
cpimExtIfSRTTLThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfSRTTLThreshold.setStatus("current")
_CpimExtIfLanDelayEnabled_Type = TruthValue
_CpimExtIfLanDelayEnabled_Object = MibTableColumn
cpimExtIfLanDelayEnabled = _CpimExtIfLanDelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 11),
    _CpimExtIfLanDelayEnabled_Type()
)
cpimExtIfLanDelayEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtIfLanDelayEnabled.setStatus("current")
_CpimExtIfSRCapable_Type = TruthValue
_CpimExtIfSRCapable_Object = MibTableColumn
cpimExtIfSRCapable = _CpimExtIfSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 12),
    _CpimExtIfSRCapable_Type()
)
cpimExtIfSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtIfSRCapable.setStatus("current")


class _CpimExtIfDRPriority_Type(Unsigned32):
    """Custom type cpimExtIfDRPriority based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpimExtIfDRPriority_Type.__name__ = "Unsigned32"
_CpimExtIfDRPriority_Object = MibTableColumn
cpimExtIfDRPriority = _CpimExtIfDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 13),
    _CpimExtIfDRPriority_Type()
)
cpimExtIfDRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfDRPriority.setStatus("current")
_CpimExtIfBidirCapable_Type = TruthValue
_CpimExtIfBidirCapable_Object = MibTableColumn
cpimExtIfBidirCapable = _CpimExtIfBidirCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 14),
    _CpimExtIfBidirCapable_Type()
)
cpimExtIfBidirCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtIfBidirCapable.setStatus("current")


class _CpimExtIfBSRBorder_Type(TruthValue):
    """Custom type cpimExtIfBSRBorder based on TruthValue"""


_CpimExtIfBSRBorder_Object = MibTableColumn
cpimExtIfBSRBorder = _CpimExtIfBSRBorder_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 1, 1, 15),
    _CpimExtIfBSRBorder_Type()
)
cpimExtIfBSRBorder.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtIfBSRBorder.setStatus("current")
_CpimExtNbrTable_Object = MibTable
cpimExtNbrTable = _CpimExtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cpimExtNbrTable.setStatus("current")
_CpimExtNbrEntry_Object = MibTableRow
cpimExtNbrEntry = _CpimExtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cpimExtNbrEntry.setStatus("current")


class _CpimExtNbrLANPruneDelay_Type(Unsigned32):
    """Custom type cpimExtNbrLANPruneDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtNbrLANPruneDelay_Type.__name__ = "Unsigned32"
_CpimExtNbrLANPruneDelay_Object = MibTableColumn
cpimExtNbrLANPruneDelay = _CpimExtNbrLANPruneDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 2, 1, 1),
    _CpimExtNbrLANPruneDelay_Type()
)
cpimExtNbrLANPruneDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtNbrLANPruneDelay.setStatus("current")


class _CpimExtNbrOverrideInterval_Type(Unsigned32):
    """Custom type cpimExtNbrOverrideInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtNbrOverrideInterval_Type.__name__ = "Unsigned32"
_CpimExtNbrOverrideInterval_Object = MibTableColumn
cpimExtNbrOverrideInterval = _CpimExtNbrOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 2, 1, 2),
    _CpimExtNbrOverrideInterval_Type()
)
cpimExtNbrOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtNbrOverrideInterval.setStatus("current")


class _CpimExtNbrTBit_Type(Bits):
    """Custom type cpimExtNbrTBit based on Bits"""
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )

_CpimExtNbrTBit_Type.__name__ = "Bits"
_CpimExtNbrTBit_Object = MibTableColumn
cpimExtNbrTBit = _CpimExtNbrTBit_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 2, 1, 3),
    _CpimExtNbrTBit_Type()
)
cpimExtNbrTBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtNbrTBit.setStatus("current")
_CpimExtNbrSRCapable_Type = TruthValue
_CpimExtNbrSRCapable_Object = MibTableColumn
cpimExtNbrSRCapable = _CpimExtNbrSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 2, 1, 4),
    _CpimExtNbrSRCapable_Type()
)
cpimExtNbrSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtNbrSRCapable.setStatus("current")
_CpimExtNbrGenId_Type = Unsigned32
_CpimExtNbrGenId_Object = MibTableColumn
cpimExtNbrGenId = _CpimExtNbrGenId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 2, 1, 5),
    _CpimExtNbrGenId_Type()
)
cpimExtNbrGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtNbrGenId.setStatus("current")
_CpimExtNbrBidirCapable_Type = TruthValue
_CpimExtNbrBidirCapable_Object = MibTableColumn
cpimExtNbrBidirCapable = _CpimExtNbrBidirCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 2, 1, 6),
    _CpimExtNbrBidirCapable_Type()
)
cpimExtNbrBidirCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtNbrBidirCapable.setStatus("current")
_CpimExtNbrDRPresent_Type = TruthValue
_CpimExtNbrDRPresent_Object = MibTableColumn
cpimExtNbrDRPresent = _CpimExtNbrDRPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 2, 1, 7),
    _CpimExtNbrDRPresent_Type()
)
cpimExtNbrDRPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtNbrDRPresent.setStatus("current")


class _CpimExtNbrDRPriority_Type(Unsigned32):
    """Custom type cpimExtNbrDRPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtNbrDRPriority_Type.__name__ = "Unsigned32"
_CpimExtNbrDRPriority_Object = MibTableColumn
cpimExtNbrDRPriority = _CpimExtNbrDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 2, 1, 8),
    _CpimExtNbrDRPriority_Type()
)
cpimExtNbrDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtNbrDRPriority.setStatus("current")
_CpimExtNbrSecAddressTable_Object = MibTable
cpimExtNbrSecAddressTable = _CpimExtNbrSecAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cpimExtNbrSecAddressTable.setStatus("current")
_CpimExtNbrSecAddressEntry_Object = MibTableRow
cpimExtNbrSecAddressEntry = _CpimExtNbrSecAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 3, 1)
)
cpimExtNbrSecAddressEntry.setIndexNames(
    (0, "CISCO-IETF-PIM-MIB", "cPimNbrIfIndex"),
    (0, "CISCO-IETF-PIM-MIB", "cPimNbrAddressType"),
    (0, "CISCO-IETF-PIM-MIB", "cPimNbrAddress"),
    (0, "CISCO-IETF-PIM-EXT-MIB", "cpimExtNbrSecAddress"),
)
if mibBuilder.loadTexts:
    cpimExtNbrSecAddressEntry.setStatus("current")


class _CpimExtNbrSecAddress_Type(InetAddress):
    """Custom type cpimExtNbrSecAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CpimExtNbrSecAddress_Type.__name__ = "InetAddress"
_CpimExtNbrSecAddress_Object = MibTableColumn
cpimExtNbrSecAddress = _CpimExtNbrSecAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 3, 1, 1),
    _CpimExtNbrSecAddress_Type()
)
cpimExtNbrSecAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtNbrSecAddress.setStatus("current")
_CpimExtNbrSecMask_Type = InetAddressPrefixLength
_CpimExtNbrSecMask_Object = MibTableColumn
cpimExtNbrSecMask = _CpimExtNbrSecMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 3, 1, 2),
    _CpimExtNbrSecMask_Type()
)
cpimExtNbrSecMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtNbrSecMask.setStatus("current")
_CpimExtMRouteTable_Object = MibTable
cpimExtMRouteTable = _CpimExtMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cpimExtMRouteTable.setStatus("current")
_CpimExtMRouteEntry_Object = MibTableRow
cpimExtMRouteEntry = _CpimExtMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cpimExtMRouteEntry.setStatus("current")


class _CpimExtMRouteRPFNeighbor_Type(InetAddress):
    """Custom type cpimExtMRouteRPFNeighbor based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CpimExtMRouteRPFNeighbor_Type.__name__ = "InetAddress"
_CpimExtMRouteRPFNeighbor_Object = MibTableColumn
cpimExtMRouteRPFNeighbor = _CpimExtMRouteRPFNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 4, 1, 1),
    _CpimExtMRouteRPFNeighbor_Type()
)
cpimExtMRouteRPFNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtMRouteRPFNeighbor.setStatus("current")
_CpimExtMRouteSourceTimer_Type = TimeTicks
_CpimExtMRouteSourceTimer_Object = MibTableColumn
cpimExtMRouteSourceTimer = _CpimExtMRouteSourceTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 4, 1, 2),
    _CpimExtMRouteSourceTimer_Type()
)
cpimExtMRouteSourceTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtMRouteSourceTimer.setStatus("current")


class _CpimExtMRouteOriginatorSRTTL_Type(Unsigned32):
    """Custom type cpimExtMRouteOriginatorSRTTL based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CpimExtMRouteOriginatorSRTTL_Type.__name__ = "Unsigned32"
_CpimExtMRouteOriginatorSRTTL_Object = MibTableColumn
cpimExtMRouteOriginatorSRTTL = _CpimExtMRouteOriginatorSRTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 4, 1, 3),
    _CpimExtMRouteOriginatorSRTTL_Type()
)
cpimExtMRouteOriginatorSRTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtMRouteOriginatorSRTTL.setStatus("current")
_CpimExtMRouteBidirGroup_Type = TruthValue
_CpimExtMRouteBidirGroup_Object = MibTableColumn
cpimExtMRouteBidirGroup = _CpimExtMRouteBidirGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 4, 1, 4),
    _CpimExtMRouteBidirGroup_Type()
)
cpimExtMRouteBidirGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtMRouteBidirGroup.setStatus("current")
_CpimExtMRouteNextHopTable_Object = MibTable
cpimExtMRouteNextHopTable = _CpimExtMRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cpimExtMRouteNextHopTable.setStatus("current")
_CpimExtMRouteNextHopEntry_Object = MibTableRow
cpimExtMRouteNextHopEntry = _CpimExtMRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cpimExtMRouteNextHopEntry.setStatus("current")


class _CpimExtMRouteNextHopAssertWinner_Type(InetAddress):
    """Custom type cpimExtMRouteNextHopAssertWinner based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CpimExtMRouteNextHopAssertWinner_Type.__name__ = "InetAddress"
_CpimExtMRouteNextHopAssertWinner_Object = MibTableColumn
cpimExtMRouteNextHopAssertWinner = _CpimExtMRouteNextHopAssertWinner_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 5, 1, 1),
    _CpimExtMRouteNextHopAssertWinner_Type()
)
cpimExtMRouteNextHopAssertWinner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtMRouteNextHopAssertWinner.setStatus("current")
_CpimExtMRouteNextHopAssertTimer_Type = TimeTicks
_CpimExtMRouteNextHopAssertTimer_Object = MibTableColumn
cpimExtMRouteNextHopAssertTimer = _CpimExtMRouteNextHopAssertTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 5, 1, 2),
    _CpimExtMRouteNextHopAssertTimer_Type()
)
cpimExtMRouteNextHopAssertTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtMRouteNextHopAssertTimer.setStatus("current")


class _CpimExtMRouteNextHopAssertMetric_Type(Unsigned32):
    """Custom type cpimExtMRouteNextHopAssertMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtMRouteNextHopAssertMetric_Type.__name__ = "Unsigned32"
_CpimExtMRouteNextHopAssertMetric_Object = MibTableColumn
cpimExtMRouteNextHopAssertMetric = _CpimExtMRouteNextHopAssertMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 5, 1, 3),
    _CpimExtMRouteNextHopAssertMetric_Type()
)
cpimExtMRouteNextHopAssertMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtMRouteNextHopAssertMetric.setStatus("current")


class _CpimExtMRouteNextHopAsrtMtrcPref_Type(Unsigned32):
    """Custom type cpimExtMRouteNextHopAsrtMtrcPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtMRouteNextHopAsrtMtrcPref_Type.__name__ = "Unsigned32"
_CpimExtMRouteNextHopAsrtMtrcPref_Object = MibTableColumn
cpimExtMRouteNextHopAsrtMtrcPref = _CpimExtMRouteNextHopAsrtMtrcPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 5, 1, 4),
    _CpimExtMRouteNextHopAsrtMtrcPref_Type()
)
cpimExtMRouteNextHopAsrtMtrcPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtMRouteNextHopAsrtMtrcPref.setStatus("current")
_CpimExtMRouteNextHopJoinPruneTmr_Type = TimeTicks
_CpimExtMRouteNextHopJoinPruneTmr_Object = MibTableColumn
cpimExtMRouteNextHopJoinPruneTmr = _CpimExtMRouteNextHopJoinPruneTmr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 5, 1, 5),
    _CpimExtMRouteNextHopJoinPruneTmr_Type()
)
cpimExtMRouteNextHopJoinPruneTmr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtMRouteNextHopJoinPruneTmr.setStatus("current")
_CpimExtBidirDFTable_Object = MibTable
cpimExtBidirDFTable = _CpimExtBidirDFTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cpimExtBidirDFTable.setStatus("current")
_CpimExtBidirDFEntry_Object = MibTableRow
cpimExtBidirDFEntry = _CpimExtBidirDFEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 6, 1)
)
cpimExtBidirDFEntry.setIndexNames(
    (0, "CISCO-IETF-PIM-EXT-MIB", "cpimExtBidirDFRPAddressType"),
    (0, "CISCO-IETF-PIM-EXT-MIB", "cpimExtBidirDFRPAddress"),
    (0, "CISCO-IETF-PIM-EXT-MIB", "cpimExtBidirDFIfIndex"),
)
if mibBuilder.loadTexts:
    cpimExtBidirDFEntry.setStatus("current")
_CpimExtBidirDFIfIndex_Type = InterfaceIndex
_CpimExtBidirDFIfIndex_Object = MibTableColumn
cpimExtBidirDFIfIndex = _CpimExtBidirDFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 6, 1, 1),
    _CpimExtBidirDFIfIndex_Type()
)
cpimExtBidirDFIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpimExtBidirDFIfIndex.setStatus("current")
_CpimExtBidirDFRPAddressType_Type = InetAddressType
_CpimExtBidirDFRPAddressType_Object = MibTableColumn
cpimExtBidirDFRPAddressType = _CpimExtBidirDFRPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 6, 1, 2),
    _CpimExtBidirDFRPAddressType_Type()
)
cpimExtBidirDFRPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpimExtBidirDFRPAddressType.setStatus("current")


class _CpimExtBidirDFRPAddress_Type(InetAddress):
    """Custom type cpimExtBidirDFRPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CpimExtBidirDFRPAddress_Type.__name__ = "InetAddress"
_CpimExtBidirDFRPAddress_Object = MibTableColumn
cpimExtBidirDFRPAddress = _CpimExtBidirDFRPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 6, 1, 3),
    _CpimExtBidirDFRPAddress_Type()
)
cpimExtBidirDFRPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpimExtBidirDFRPAddress.setStatus("current")


class _CpimExtBidirDFWinnerAddress_Type(InetAddress):
    """Custom type cpimExtBidirDFWinnerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CpimExtBidirDFWinnerAddress_Type.__name__ = "InetAddress"
_CpimExtBidirDFWinnerAddress_Object = MibTableColumn
cpimExtBidirDFWinnerAddress = _CpimExtBidirDFWinnerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 6, 1, 4),
    _CpimExtBidirDFWinnerAddress_Type()
)
cpimExtBidirDFWinnerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtBidirDFWinnerAddress.setStatus("current")
_CpimExtBidirDFWinnerUptime_Type = TimeTicks
_CpimExtBidirDFWinnerUptime_Object = MibTableColumn
cpimExtBidirDFWinnerUptime = _CpimExtBidirDFWinnerUptime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 6, 1, 5),
    _CpimExtBidirDFWinnerUptime_Type()
)
cpimExtBidirDFWinnerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtBidirDFWinnerUptime.setStatus("current")


class _CpimExtBidirDFWnrMtrcPref_Type(Unsigned32):
    """Custom type cpimExtBidirDFWnrMtrcPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtBidirDFWnrMtrcPref_Type.__name__ = "Unsigned32"
_CpimExtBidirDFWnrMtrcPref_Object = MibTableColumn
cpimExtBidirDFWnrMtrcPref = _CpimExtBidirDFWnrMtrcPref_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 6, 1, 6),
    _CpimExtBidirDFWnrMtrcPref_Type()
)
cpimExtBidirDFWnrMtrcPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtBidirDFWnrMtrcPref.setStatus("current")


class _CpimExtBidirDFWinnerMetric_Type(Unsigned32):
    """Custom type cpimExtBidirDFWinnerMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtBidirDFWinnerMetric_Type.__name__ = "Unsigned32"
_CpimExtBidirDFWinnerMetric_Object = MibTableColumn
cpimExtBidirDFWinnerMetric = _CpimExtBidirDFWinnerMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 6, 1, 7),
    _CpimExtBidirDFWinnerMetric_Type()
)
cpimExtBidirDFWinnerMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtBidirDFWinnerMetric.setStatus("current")


class _CpimExtBidirDFState_Type(Integer32):
    """Custom type cpimExtBidirDFState based on Integer32"""
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
        *(("dfBackoff", 4),
          ("dfLose", 2),
          ("dfOffer", 1),
          ("dfWinner", 3),
          ("unknown", 0))
    )


_CpimExtBidirDFState_Type.__name__ = "Integer32"
_CpimExtBidirDFState_Object = MibTableColumn
cpimExtBidirDFState = _CpimExtBidirDFState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 6, 1, 8),
    _CpimExtBidirDFState_Type()
)
cpimExtBidirDFState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtBidirDFState.setStatus("current")
_CpimExtBidirDFStateTimer_Type = TimeTicks
_CpimExtBidirDFStateTimer_Object = MibTableColumn
cpimExtBidirDFStateTimer = _CpimExtBidirDFStateTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 6, 1, 9),
    _CpimExtBidirDFStateTimer_Type()
)
cpimExtBidirDFStateTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtBidirDFStateTimer.setStatus("current")
_CpimExtRPSetTable_Object = MibTable
cpimExtRPSetTable = _CpimExtRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cpimExtRPSetTable.setStatus("current")
_CpimExtRPSetEntry_Object = MibTableRow
cpimExtRPSetEntry = _CpimExtRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1)
)
cpimExtRPSetEntry.setIndexNames(
    (0, "CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetComponent"),
    (0, "CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetAddrType"),
    (0, "CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetGroupAddress"),
    (0, "CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetGroupMask"),
    (0, "CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetType"),
    (0, "CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetProtocol"),
    (0, "CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetAddress"),
)
if mibBuilder.loadTexts:
    cpimExtRPSetEntry.setStatus("current")


class _CpimExtRPSetComponent_Type(Unsigned32):
    """Custom type cpimExtRPSetComponent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CpimExtRPSetComponent_Type.__name__ = "Unsigned32"
_CpimExtRPSetComponent_Object = MibTableColumn
cpimExtRPSetComponent = _CpimExtRPSetComponent_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1, 1),
    _CpimExtRPSetComponent_Type()
)
cpimExtRPSetComponent.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpimExtRPSetComponent.setStatus("current")
_CpimExtRPSetAddrType_Type = InetAddressType
_CpimExtRPSetAddrType_Object = MibTableColumn
cpimExtRPSetAddrType = _CpimExtRPSetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1, 2),
    _CpimExtRPSetAddrType_Type()
)
cpimExtRPSetAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpimExtRPSetAddrType.setStatus("current")


class _CpimExtRPSetGroupAddress_Type(InetAddress):
    """Custom type cpimExtRPSetGroupAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CpimExtRPSetGroupAddress_Type.__name__ = "InetAddress"
_CpimExtRPSetGroupAddress_Object = MibTableColumn
cpimExtRPSetGroupAddress = _CpimExtRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1, 3),
    _CpimExtRPSetGroupAddress_Type()
)
cpimExtRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpimExtRPSetGroupAddress.setStatus("current")
_CpimExtRPSetGroupMask_Type = InetAddressPrefixLength
_CpimExtRPSetGroupMask_Object = MibTableColumn
cpimExtRPSetGroupMask = _CpimExtRPSetGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1, 4),
    _CpimExtRPSetGroupMask_Type()
)
cpimExtRPSetGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpimExtRPSetGroupMask.setStatus("current")


class _CpimExtRPSetType_Type(Integer32):
    """Custom type cpimExtRPSetType based on Integer32"""
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
        *(("autorp", 5),
          ("bsr", 3),
          ("embedded", 4),
          ("other", 1),
          ("static", 2))
    )


_CpimExtRPSetType_Type.__name__ = "Integer32"
_CpimExtRPSetType_Object = MibTableColumn
cpimExtRPSetType = _CpimExtRPSetType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1, 5),
    _CpimExtRPSetType_Type()
)
cpimExtRPSetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpimExtRPSetType.setStatus("current")
_CpimExtRPSetProtocol_Type = IANAipMRouteProtocol
_CpimExtRPSetProtocol_Object = MibTableColumn
cpimExtRPSetProtocol = _CpimExtRPSetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1, 6),
    _CpimExtRPSetProtocol_Type()
)
cpimExtRPSetProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpimExtRPSetProtocol.setStatus("current")


class _CpimExtRPSetAddress_Type(InetAddress):
    """Custom type cpimExtRPSetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_CpimExtRPSetAddress_Type.__name__ = "InetAddress"
_CpimExtRPSetAddress_Object = MibTableColumn
cpimExtRPSetAddress = _CpimExtRPSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1, 7),
    _CpimExtRPSetAddress_Type()
)
cpimExtRPSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cpimExtRPSetAddress.setStatus("current")


class _CpimExtRPSetHoldTime_Type(Unsigned32):
    """Custom type cpimExtRPSetHoldTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpimExtRPSetHoldTime_Type.__name__ = "Unsigned32"
_CpimExtRPSetHoldTime_Object = MibTableColumn
cpimExtRPSetHoldTime = _CpimExtRPSetHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1, 8),
    _CpimExtRPSetHoldTime_Type()
)
cpimExtRPSetHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtRPSetHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    cpimExtRPSetHoldTime.setUnits("seconds")


class _CpimExtRPSetExpiryTime_Type(Unsigned32):
    """Custom type cpimExtRPSetExpiryTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpimExtRPSetExpiryTime_Type.__name__ = "Unsigned32"
_CpimExtRPSetExpiryTime_Object = MibTableColumn
cpimExtRPSetExpiryTime = _CpimExtRPSetExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1, 9),
    _CpimExtRPSetExpiryTime_Type()
)
cpimExtRPSetExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtRPSetExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    cpimExtRPSetExpiryTime.setUnits("seconds")


class _CpimExtRPSetPriority_Type(Integer32):
    """Custom type cpimExtRPSetPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CpimExtRPSetPriority_Type.__name__ = "Integer32"
_CpimExtRPSetPriority_Object = MibTableColumn
cpimExtRPSetPriority = _CpimExtRPSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1, 10),
    _CpimExtRPSetPriority_Type()
)
cpimExtRPSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtRPSetPriority.setStatus("current")
_CpimExtRPSetRPActive_Type = TruthValue
_CpimExtRPSetRPActive_Object = MibTableColumn
cpimExtRPSetRPActive = _CpimExtRPSetRPActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 7, 1, 11),
    _CpimExtRPSetRPActive_Type()
)
cpimExtRPSetRPActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpimExtRPSetRPActive.setStatus("current")
_CpimExtCRPTable_Object = MibTable
cpimExtCRPTable = _CpimExtCRPTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cpimExtCRPTable.setStatus("current")
_CpimExtCRPEntry_Object = MibTableRow
cpimExtCRPEntry = _CpimExtCRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cpimExtCRPEntry.setStatus("current")


class _CpimExtCRPBidir_Type(TruthValue):
    """Custom type cpimExtCRPBidir based on TruthValue"""


_CpimExtCRPBidir_Object = MibTableColumn
cpimExtCRPBidir = _CpimExtCRPBidir_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 8, 1, 1),
    _CpimExtCRPBidir_Type()
)
cpimExtCRPBidir.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cpimExtCRPBidir.setStatus("current")


class _CpimExtSourceLifetime_Type(Unsigned32):
    """Custom type cpimExtSourceLifetime based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpimExtSourceLifetime_Type.__name__ = "Unsigned32"
_CpimExtSourceLifetime_Object = MibScalar
cpimExtSourceLifetime = _CpimExtSourceLifetime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 9),
    _CpimExtSourceLifetime_Type()
)
cpimExtSourceLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpimExtSourceLifetime.setStatus("current")
if mibBuilder.loadTexts:
    cpimExtSourceLifetime.setUnits("seconds")


class _CpimExtStateRefreshInterval_Type(Unsigned32):
    """Custom type cpimExtStateRefreshInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CpimExtStateRefreshInterval_Type.__name__ = "Unsigned32"
_CpimExtStateRefreshInterval_Object = MibScalar
cpimExtStateRefreshInterval = _CpimExtStateRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 10),
    _CpimExtStateRefreshInterval_Type()
)
cpimExtStateRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpimExtStateRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    cpimExtStateRefreshInterval.setUnits("seconds")


class _CpimExtStateRefreshLimitInterval_Type(TimeTicks):
    """Custom type cpimExtStateRefreshLimitInterval based on TimeTicks"""
    defaultValue = 0


_CpimExtStateRefreshLimitInterval_Object = MibScalar
cpimExtStateRefreshLimitInterval = _CpimExtStateRefreshLimitInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 11),
    _CpimExtStateRefreshLimitInterval_Type()
)
cpimExtStateRefreshLimitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpimExtStateRefreshLimitInterval.setStatus("current")


class _CpimExtStateRefreshTimeToLive_Type(Unsigned32):
    """Custom type cpimExtStateRefreshTimeToLive based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_CpimExtStateRefreshTimeToLive_Type.__name__ = "Unsigned32"
_CpimExtStateRefreshTimeToLive_Object = MibScalar
cpimExtStateRefreshTimeToLive = _CpimExtStateRefreshTimeToLive_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 12),
    _CpimExtStateRefreshTimeToLive_Type()
)
cpimExtStateRefreshTimeToLive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpimExtStateRefreshTimeToLive.setStatus("current")


class _CpimExtInterfaceStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cpimExtInterfaceStateChangeNotifEnabled based on TruthValue"""


_CpimExtInterfaceStateChangeNotifEnabled_Object = MibScalar
cpimExtInterfaceStateChangeNotifEnabled = _CpimExtInterfaceStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 13),
    _CpimExtInterfaceStateChangeNotifEnabled_Type()
)
cpimExtInterfaceStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpimExtInterfaceStateChangeNotifEnabled.setStatus("current")


class _CpimExtRPMappingChangeNotifEnabled_Type(TruthValue):
    """Custom type cpimExtRPMappingChangeNotifEnabled based on TruthValue"""


_CpimExtRPMappingChangeNotifEnabled_Object = MibScalar
cpimExtRPMappingChangeNotifEnabled = _CpimExtRPMappingChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 1, 1, 14),
    _CpimExtRPMappingChangeNotifEnabled_Type()
)
cpimExtRPMappingChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpimExtRPMappingChangeNotifEnabled.setStatus("current")
_CiscoIetfPimExtMIBConformance_ObjectIdentity = ObjectIdentity
ciscoIetfPimExtMIBConformance = _CiscoIetfPimExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 2)
)
_CiscoIetfPimExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIetfPimExtMIBCompliances = _CiscoIetfPimExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 2, 1)
)
_CiscoIetfPimExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIetfPimExtMIBGroups = _CiscoIetfPimExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 2, 2)
)
cPimIfEntry.registerAugmentions(
    ("CISCO-IETF-PIM-EXT-MIB",
     "cpimExtIfEntry")
)
cpimExtIfEntry.setIndexNames(*cPimIfEntry.getIndexNames())
cPimNbrEntry.registerAugmentions(
    ("CISCO-IETF-PIM-EXT-MIB",
     "cpimExtNbrEntry")
)
cpimExtNbrEntry.setIndexNames(*cPimNbrEntry.getIndexNames())
cPimInetMRouteEntry.registerAugmentions(
    ("CISCO-IETF-PIM-EXT-MIB",
     "cpimExtMRouteEntry")
)
cpimExtMRouteEntry.setIndexNames(*cPimInetMRouteEntry.getIndexNames())
cPimInetMRouteNextHopEntry.registerAugmentions(
    ("CISCO-IETF-PIM-EXT-MIB",
     "cpimExtMRouteNextHopEntry")
)
cpimExtMRouteNextHopEntry.setIndexNames(*cPimInetMRouteNextHopEntry.getIndexNames())
cPimCRPEntry.registerAugmentions(
    ("CISCO-IETF-PIM-EXT-MIB",
     "cpimExtCRPEntry")
)
cpimExtCRPEntry.setIndexNames(*cPimCRPEntry.getIndexNames())

# Managed Objects groups

ciscoIetfPimExtGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 2, 2, 1)
)
ciscoIetfPimExtGeneralGroup.setObjects(
      *(("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfTrigHelloInterval"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfHelloHoldtime"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfLanPruneDelay"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfPropagationDelay"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfOverrideInterval"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfGenerationID"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfJoinPruneHoldtime"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfGraftRetryInterval"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfMaxGraftRetries"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfSRTTLThreshold"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfLanDelayEnabled"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfSRCapable"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfDRPriority"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfBSRBorder"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtMRouteRPFNeighbor"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtMRouteSourceTimer"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtMRouteOriginatorSRTTL"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetHoldTime"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetExpiryTime"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetPriority"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetRPActive"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtSourceLifetime"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtStateRefreshInterval"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtStateRefreshLimitInterval"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtStateRefreshTimeToLive"))
)
if mibBuilder.loadTexts:
    ciscoIetfPimExtGeneralGroup.setStatus("current")

ciscoIetfPimExtNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 2, 2, 2)
)
ciscoIetfPimExtNbrGroup.setObjects(
      *(("CISCO-IETF-PIM-EXT-MIB", "cpimExtNbrLANPruneDelay"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtNbrOverrideInterval"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtNbrTBit"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtNbrSRCapable"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtNbrGenId"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtNbrDRPresent"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtNbrDRPriority"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtNbrSecAddress"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtNbrSecMask"))
)
if mibBuilder.loadTexts:
    ciscoIetfPimExtNbrGroup.setStatus("current")

ciscoIetfPimExtNextHopGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 2, 2, 3)
)
ciscoIetfPimExtNextHopGroup.setObjects(
      *(("CISCO-IETF-PIM-EXT-MIB", "cpimExtMRouteNextHopAssertWinner"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtMRouteNextHopAssertTimer"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtMRouteNextHopAssertMetric"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtMRouteNextHopAsrtMtrcPref"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtMRouteNextHopJoinPruneTmr"))
)
if mibBuilder.loadTexts:
    ciscoIetfPimExtNextHopGroup.setStatus("current")

ciscoIetfPimExtBidirGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 2, 2, 4)
)
ciscoIetfPimExtBidirGroup.setObjects(
      *(("CISCO-IETF-PIM-EXT-MIB", "cpimExtBidirDFWinnerAddress"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtBidirDFWinnerUptime"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtBidirDFWnrMtrcPref"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtBidirDFWinnerMetric"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtBidirDFState"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtBidirDFStateTimer"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtIfBidirCapable"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtNbrBidirCapable"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtMRouteBidirGroup"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtCRPBidir"))
)
if mibBuilder.loadTexts:
    ciscoIetfPimExtBidirGroup.setStatus("current")

ciscoIetfPimExtNotifEnabledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 2, 2, 6)
)
ciscoIetfPimExtNotifEnabledGroup.setObjects(
      *(("CISCO-IETF-PIM-EXT-MIB", "cpimExtInterfaceStateChangeNotifEnabled"),
        ("CISCO-IETF-PIM-EXT-MIB", "cpimExtRPMappingChangeNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoIetfPimExtNotifEnabledGroup.setStatus("current")


# Notification objects

ciscoIetfPimExtInterfaceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 0, 1)
)
ciscoIetfPimExtInterfaceUp.setObjects(
    ("CISCO-IETF-PIM-MIB", "cPimIfStatus")
)
if mibBuilder.loadTexts:
    ciscoIetfPimExtInterfaceUp.setStatus(
        "current"
    )

ciscoIetfPimExtInterfaceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 0, 2)
)
ciscoIetfPimExtInterfaceDown.setObjects(
    ("CISCO-IETF-PIM-MIB", "cPimIfStatus")
)
if mibBuilder.loadTexts:
    ciscoIetfPimExtInterfaceDown.setStatus(
        "current"
    )

ciscoIetfPimExtRPMappingChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 0, 3)
)
ciscoIetfPimExtRPMappingChange.setObjects(
      *(("CISCO-IETF-PIM-EXT-MIB", "cpimExtRPSetHoldTime"),
        ("CISCO-PIM-MIB", "cpimRPMappingChangeType"))
)
if mibBuilder.loadTexts:
    ciscoIetfPimExtRPMappingChange.setStatus(
        "current"
    )


# Notifications groups

ciscoIetfPimExtNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 2, 2, 5)
)
ciscoIetfPimExtNotificationGroup.setObjects(
      *(("CISCO-IETF-PIM-EXT-MIB", "ciscoIetfPimExtInterfaceUp"),
        ("CISCO-IETF-PIM-EXT-MIB", "ciscoIetfPimExtInterfaceDown"),
        ("CISCO-IETF-PIM-EXT-MIB", "ciscoIetfPimExtRPMappingChange"))
)
if mibBuilder.loadTexts:
    ciscoIetfPimExtNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoIetfPimExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIetfPimExtMIBCompliance.setStatus(
        "deprecated"
    )

ciscoIetfPimExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 120, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoIetfPimExtMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-PIM-EXT-MIB",
    **{"ciscoIetfPimExtMIB": ciscoIetfPimExtMIB,
       "ciscoIetfPimExtNotifs": ciscoIetfPimExtNotifs,
       "ciscoIetfPimExtInterfaceUp": ciscoIetfPimExtInterfaceUp,
       "ciscoIetfPimExtInterfaceDown": ciscoIetfPimExtInterfaceDown,
       "ciscoIetfPimExtRPMappingChange": ciscoIetfPimExtRPMappingChange,
       "ciscoIetfPimExtMIBObjects": ciscoIetfPimExtMIBObjects,
       "ciscoPimExt": ciscoPimExt,
       "cpimExtIfTable": cpimExtIfTable,
       "cpimExtIfEntry": cpimExtIfEntry,
       "cpimExtIfTrigHelloInterval": cpimExtIfTrigHelloInterval,
       "cpimExtIfHelloHoldtime": cpimExtIfHelloHoldtime,
       "cpimExtIfLanPruneDelay": cpimExtIfLanPruneDelay,
       "cpimExtIfPropagationDelay": cpimExtIfPropagationDelay,
       "cpimExtIfOverrideInterval": cpimExtIfOverrideInterval,
       "cpimExtIfGenerationID": cpimExtIfGenerationID,
       "cpimExtIfJoinPruneHoldtime": cpimExtIfJoinPruneHoldtime,
       "cpimExtIfGraftRetryInterval": cpimExtIfGraftRetryInterval,
       "cpimExtIfMaxGraftRetries": cpimExtIfMaxGraftRetries,
       "cpimExtIfSRTTLThreshold": cpimExtIfSRTTLThreshold,
       "cpimExtIfLanDelayEnabled": cpimExtIfLanDelayEnabled,
       "cpimExtIfSRCapable": cpimExtIfSRCapable,
       "cpimExtIfDRPriority": cpimExtIfDRPriority,
       "cpimExtIfBidirCapable": cpimExtIfBidirCapable,
       "cpimExtIfBSRBorder": cpimExtIfBSRBorder,
       "cpimExtNbrTable": cpimExtNbrTable,
       "cpimExtNbrEntry": cpimExtNbrEntry,
       "cpimExtNbrLANPruneDelay": cpimExtNbrLANPruneDelay,
       "cpimExtNbrOverrideInterval": cpimExtNbrOverrideInterval,
       "cpimExtNbrTBit": cpimExtNbrTBit,
       "cpimExtNbrSRCapable": cpimExtNbrSRCapable,
       "cpimExtNbrGenId": cpimExtNbrGenId,
       "cpimExtNbrBidirCapable": cpimExtNbrBidirCapable,
       "cpimExtNbrDRPresent": cpimExtNbrDRPresent,
       "cpimExtNbrDRPriority": cpimExtNbrDRPriority,
       "cpimExtNbrSecAddressTable": cpimExtNbrSecAddressTable,
       "cpimExtNbrSecAddressEntry": cpimExtNbrSecAddressEntry,
       "cpimExtNbrSecAddress": cpimExtNbrSecAddress,
       "cpimExtNbrSecMask": cpimExtNbrSecMask,
       "cpimExtMRouteTable": cpimExtMRouteTable,
       "cpimExtMRouteEntry": cpimExtMRouteEntry,
       "cpimExtMRouteRPFNeighbor": cpimExtMRouteRPFNeighbor,
       "cpimExtMRouteSourceTimer": cpimExtMRouteSourceTimer,
       "cpimExtMRouteOriginatorSRTTL": cpimExtMRouteOriginatorSRTTL,
       "cpimExtMRouteBidirGroup": cpimExtMRouteBidirGroup,
       "cpimExtMRouteNextHopTable": cpimExtMRouteNextHopTable,
       "cpimExtMRouteNextHopEntry": cpimExtMRouteNextHopEntry,
       "cpimExtMRouteNextHopAssertWinner": cpimExtMRouteNextHopAssertWinner,
       "cpimExtMRouteNextHopAssertTimer": cpimExtMRouteNextHopAssertTimer,
       "cpimExtMRouteNextHopAssertMetric": cpimExtMRouteNextHopAssertMetric,
       "cpimExtMRouteNextHopAsrtMtrcPref": cpimExtMRouteNextHopAsrtMtrcPref,
       "cpimExtMRouteNextHopJoinPruneTmr": cpimExtMRouteNextHopJoinPruneTmr,
       "cpimExtBidirDFTable": cpimExtBidirDFTable,
       "cpimExtBidirDFEntry": cpimExtBidirDFEntry,
       "cpimExtBidirDFIfIndex": cpimExtBidirDFIfIndex,
       "cpimExtBidirDFRPAddressType": cpimExtBidirDFRPAddressType,
       "cpimExtBidirDFRPAddress": cpimExtBidirDFRPAddress,
       "cpimExtBidirDFWinnerAddress": cpimExtBidirDFWinnerAddress,
       "cpimExtBidirDFWinnerUptime": cpimExtBidirDFWinnerUptime,
       "cpimExtBidirDFWnrMtrcPref": cpimExtBidirDFWnrMtrcPref,
       "cpimExtBidirDFWinnerMetric": cpimExtBidirDFWinnerMetric,
       "cpimExtBidirDFState": cpimExtBidirDFState,
       "cpimExtBidirDFStateTimer": cpimExtBidirDFStateTimer,
       "cpimExtRPSetTable": cpimExtRPSetTable,
       "cpimExtRPSetEntry": cpimExtRPSetEntry,
       "cpimExtRPSetComponent": cpimExtRPSetComponent,
       "cpimExtRPSetAddrType": cpimExtRPSetAddrType,
       "cpimExtRPSetGroupAddress": cpimExtRPSetGroupAddress,
       "cpimExtRPSetGroupMask": cpimExtRPSetGroupMask,
       "cpimExtRPSetType": cpimExtRPSetType,
       "cpimExtRPSetProtocol": cpimExtRPSetProtocol,
       "cpimExtRPSetAddress": cpimExtRPSetAddress,
       "cpimExtRPSetHoldTime": cpimExtRPSetHoldTime,
       "cpimExtRPSetExpiryTime": cpimExtRPSetExpiryTime,
       "cpimExtRPSetPriority": cpimExtRPSetPriority,
       "cpimExtRPSetRPActive": cpimExtRPSetRPActive,
       "cpimExtCRPTable": cpimExtCRPTable,
       "cpimExtCRPEntry": cpimExtCRPEntry,
       "cpimExtCRPBidir": cpimExtCRPBidir,
       "cpimExtSourceLifetime": cpimExtSourceLifetime,
       "cpimExtStateRefreshInterval": cpimExtStateRefreshInterval,
       "cpimExtStateRefreshLimitInterval": cpimExtStateRefreshLimitInterval,
       "cpimExtStateRefreshTimeToLive": cpimExtStateRefreshTimeToLive,
       "cpimExtInterfaceStateChangeNotifEnabled": cpimExtInterfaceStateChangeNotifEnabled,
       "cpimExtRPMappingChangeNotifEnabled": cpimExtRPMappingChangeNotifEnabled,
       "ciscoIetfPimExtMIBConformance": ciscoIetfPimExtMIBConformance,
       "ciscoIetfPimExtMIBCompliances": ciscoIetfPimExtMIBCompliances,
       "ciscoIetfPimExtMIBCompliance": ciscoIetfPimExtMIBCompliance,
       "ciscoIetfPimExtMIBComplianceRev1": ciscoIetfPimExtMIBComplianceRev1,
       "ciscoIetfPimExtMIBGroups": ciscoIetfPimExtMIBGroups,
       "ciscoIetfPimExtGeneralGroup": ciscoIetfPimExtGeneralGroup,
       "ciscoIetfPimExtNbrGroup": ciscoIetfPimExtNbrGroup,
       "ciscoIetfPimExtNextHopGroup": ciscoIetfPimExtNextHopGroup,
       "ciscoIetfPimExtBidirGroup": ciscoIetfPimExtBidirGroup,
       "ciscoIetfPimExtNotificationGroup": ciscoIetfPimExtNotificationGroup,
       "ciscoIetfPimExtNotifEnabledGroup": ciscoIetfPimExtNotifEnabledGroup}
)
