# SNMP MIB module (HP-ICF-PIM) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-PIM
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:57 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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

(ipMRouteEntry,
 ipMRouteGroup,
 ipMRouteSource) = mibBuilder.importSymbols(
    "IPMROUTE-STD-MIB",
    "ipMRouteEntry",
    "ipMRouteGroup",
    "ipMRouteSource")

(pimComponentEntry,
 pimInterfaceEntry,
 pimInterfaceIfIndex,
 pimNeighborEntry,
 pimRPSetComponent,
 pimRPSetEntry) = mibBuilder.importSymbols(
    "PIM-MIB",
    "pimComponentEntry",
    "pimInterfaceEntry",
    "pimInterfaceIfIndex",
    "pimNeighborEntry",
    "pimRPSetComponent",
    "pimRPSetEntry")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfPimMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20)
)
hpicfPimMIB.setRevisions(
        ("2012-04-12 00:00",
         "2010-10-04 00:00",
         "2010-09-01 00:00",
         "2005-08-04 16:19",
         "2004-06-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfPimObjects_ObjectIdentity = ObjectIdentity
hpicfPimObjects = _HpicfPimObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1)
)
_HpicfPimTraps_ObjectIdentity = ObjectIdentity
hpicfPimTraps = _HpicfPimTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 0)
)
_HpicfPim_ObjectIdentity = ObjectIdentity
hpicfPim = _HpicfPim_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1)
)


class _HpicfPimAdminStatus_Type(Integer32):
    """Custom type hpicfPimAdminStatus based on Integer32"""
    defaultValue = 2

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


_HpicfPimAdminStatus_Type.__name__ = "Integer32"
_HpicfPimAdminStatus_Object = MibScalar
hpicfPimAdminStatus = _HpicfPimAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 1),
    _HpicfPimAdminStatus_Type()
)
hpicfPimAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPimAdminStatus.setStatus("current")


class _HpicfPimStateRefreshInterval_Type(Integer32):
    """Custom type hpicfPimStateRefreshInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_HpicfPimStateRefreshInterval_Type.__name__ = "Integer32"
_HpicfPimStateRefreshInterval_Object = MibScalar
hpicfPimStateRefreshInterval = _HpicfPimStateRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 2),
    _HpicfPimStateRefreshInterval_Type()
)
hpicfPimStateRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPimStateRefreshInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPimStateRefreshInterval.setUnits("seconds")


class _HpicfPimSPTThreshold_Type(Integer32):
    """Custom type hpicfPimSPTThreshold based on Integer32"""
    defaultValue = -1


_HpicfPimSPTThreshold_Object = MibScalar
hpicfPimSPTThreshold = _HpicfPimSPTThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 3),
    _HpicfPimSPTThreshold_Type()
)
hpicfPimSPTThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPimSPTThreshold.setStatus("current")


class _HpicfPimTrapControl_Type(Bits):
    """Custom type hpicfPimTrapControl based on Bits"""
    namedValues = NamedValues(
        *(("hardMrtFull", 1),
          ("neighborLoss", 0),
          ("softMrtFull", 2))
    )

_HpicfPimTrapControl_Type.__name__ = "Bits"
_HpicfPimTrapControl_Object = MibScalar
hpicfPimTrapControl = _HpicfPimTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 4),
    _HpicfPimTrapControl_Type()
)
hpicfPimTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPimTrapControl.setStatus("current")
_HpicfPimStaticRPSetTable_Object = MibTable
hpicfPimStaticRPSetTable = _HpicfPimStaticRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfPimStaticRPSetTable.setStatus("current")
_HpicfPimStaticRPSetEntry_Object = MibTableRow
hpicfPimStaticRPSetEntry = _HpicfPimStaticRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 5, 1)
)
hpicfPimStaticRPSetEntry.setIndexNames(
    (0, "PIM-MIB", "pimRPSetComponent"),
    (0, "HP-ICF-PIM", "hpicfPimStaticRPSetGroupAddress"),
    (0, "HP-ICF-PIM", "hpicfPimStaticRPSetGroupMask"),
    (0, "HP-ICF-PIM", "hpicfPimStaticRPSetAddress"),
)
if mibBuilder.loadTexts:
    hpicfPimStaticRPSetEntry.setStatus("current")
_HpicfPimStaticRPSetGroupAddress_Type = IpAddress
_HpicfPimStaticRPSetGroupAddress_Object = MibTableColumn
hpicfPimStaticRPSetGroupAddress = _HpicfPimStaticRPSetGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 5, 1, 1),
    _HpicfPimStaticRPSetGroupAddress_Type()
)
hpicfPimStaticRPSetGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimStaticRPSetGroupAddress.setStatus("current")
_HpicfPimStaticRPSetGroupMask_Type = IpAddress
_HpicfPimStaticRPSetGroupMask_Object = MibTableColumn
hpicfPimStaticRPSetGroupMask = _HpicfPimStaticRPSetGroupMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 5, 1, 2),
    _HpicfPimStaticRPSetGroupMask_Type()
)
hpicfPimStaticRPSetGroupMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimStaticRPSetGroupMask.setStatus("current")
_HpicfPimStaticRPSetAddress_Type = IpAddress
_HpicfPimStaticRPSetAddress_Object = MibTableColumn
hpicfPimStaticRPSetAddress = _HpicfPimStaticRPSetAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 5, 1, 3),
    _HpicfPimStaticRPSetAddress_Type()
)
hpicfPimStaticRPSetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimStaticRPSetAddress.setStatus("current")


class _HpicfPimStaticRPSetOverride_Type(TruthValue):
    """Custom type hpicfPimStaticRPSetOverride based on TruthValue"""


_HpicfPimStaticRPSetOverride_Object = MibTableColumn
hpicfPimStaticRPSetOverride = _HpicfPimStaticRPSetOverride_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 5, 1, 4),
    _HpicfPimStaticRPSetOverride_Type()
)
hpicfPimStaticRPSetOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimStaticRPSetOverride.setStatus("current")
_HpicfPimStaticRPSetRowStatus_Type = RowStatus
_HpicfPimStaticRPSetRowStatus_Object = MibTableColumn
hpicfPimStaticRPSetRowStatus = _HpicfPimStaticRPSetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 5, 1, 5),
    _HpicfPimStaticRPSetRowStatus_Type()
)
hpicfPimStaticRPSetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimStaticRPSetRowStatus.setStatus("current")
_HpicfPimIfTable_Object = MibTable
hpicfPimIfTable = _HpicfPimIfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfPimIfTable.setStatus("current")
_HpicfPimIfEntry_Object = MibTableRow
hpicfPimIfEntry = _HpicfPimIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hpicfPimIfEntry.setStatus("current")
_HpicfPimIfAddress_Type = IpAddress
_HpicfPimIfAddress_Object = MibTableColumn
hpicfPimIfAddress = _HpicfPimIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 1),
    _HpicfPimIfAddress_Type()
)
hpicfPimIfAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfAddress.setStatus("current")


class _HpicfPimIfTrigHelloInterval_Type(Integer32):
    """Custom type hpicfPimIfTrigHelloInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_HpicfPimIfTrigHelloInterval_Type.__name__ = "Integer32"
_HpicfPimIfTrigHelloInterval_Object = MibTableColumn
hpicfPimIfTrigHelloInterval = _HpicfPimIfTrigHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 2),
    _HpicfPimIfTrigHelloInterval_Type()
)
hpicfPimIfTrigHelloInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfTrigHelloInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPimIfTrigHelloInterval.setUnits("seconds")


class _HpicfPimIfHelloHoldtime_Type(Integer32):
    """Custom type hpicfPimIfHelloHoldtime based on Integer32"""
    defaultValue = 105

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 1050),
    )


_HpicfPimIfHelloHoldtime_Type.__name__ = "Integer32"
_HpicfPimIfHelloHoldtime_Object = MibTableColumn
hpicfPimIfHelloHoldtime = _HpicfPimIfHelloHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 3),
    _HpicfPimIfHelloHoldtime_Type()
)
hpicfPimIfHelloHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfHelloHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPimIfHelloHoldtime.setUnits("seconds")


class _HpicfPimIfLanPruneDelay_Type(TruthValue):
    """Custom type hpicfPimIfLanPruneDelay based on TruthValue"""


_HpicfPimIfLanPruneDelay_Object = MibTableColumn
hpicfPimIfLanPruneDelay = _HpicfPimIfLanPruneDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 4),
    _HpicfPimIfLanPruneDelay_Type()
)
hpicfPimIfLanPruneDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfLanPruneDelay.setStatus("current")


class _HpicfPimIfPropagationDelay_Type(Integer32):
    """Custom type hpicfPimIfPropagationDelay based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(250, 2000),
    )


_HpicfPimIfPropagationDelay_Type.__name__ = "Integer32"
_HpicfPimIfPropagationDelay_Object = MibTableColumn
hpicfPimIfPropagationDelay = _HpicfPimIfPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 5),
    _HpicfPimIfPropagationDelay_Type()
)
hpicfPimIfPropagationDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfPropagationDelay.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPimIfPropagationDelay.setUnits("milliseconds")


class _HpicfPimIfOverrideInterval_Type(Integer32):
    """Custom type hpicfPimIfOverrideInterval based on Integer32"""
    defaultValue = 2500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 6000),
    )


_HpicfPimIfOverrideInterval_Type.__name__ = "Integer32"
_HpicfPimIfOverrideInterval_Object = MibTableColumn
hpicfPimIfOverrideInterval = _HpicfPimIfOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 6),
    _HpicfPimIfOverrideInterval_Type()
)
hpicfPimIfOverrideInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfOverrideInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPimIfOverrideInterval.setUnits("milliseconds")


class _HpicfPimIfGenerationID_Type(TruthValue):
    """Custom type hpicfPimIfGenerationID based on TruthValue"""


_HpicfPimIfGenerationID_Object = MibTableColumn
hpicfPimIfGenerationID = _HpicfPimIfGenerationID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 7),
    _HpicfPimIfGenerationID_Type()
)
hpicfPimIfGenerationID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfGenerationID.setStatus("current")


class _HpicfPimIfJoinPruneHoldtime_Type(Unsigned32):
    """Custom type hpicfPimIfJoinPruneHoldtime based on Unsigned32"""
    defaultValue = 210


_HpicfPimIfJoinPruneHoldtime_Object = MibTableColumn
hpicfPimIfJoinPruneHoldtime = _HpicfPimIfJoinPruneHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 8),
    _HpicfPimIfJoinPruneHoldtime_Type()
)
hpicfPimIfJoinPruneHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfJoinPruneHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPimIfJoinPruneHoldtime.setUnits("seconds")


class _HpicfPimIfGraftRetryInterval_Type(Integer32):
    """Custom type hpicfPimIfGraftRetryInterval based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpicfPimIfGraftRetryInterval_Type.__name__ = "Integer32"
_HpicfPimIfGraftRetryInterval_Object = MibTableColumn
hpicfPimIfGraftRetryInterval = _HpicfPimIfGraftRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 9),
    _HpicfPimIfGraftRetryInterval_Type()
)
hpicfPimIfGraftRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfGraftRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPimIfGraftRetryInterval.setUnits("seconds")


class _HpicfPimIfMaxGraftRetries_Type(Integer32):
    """Custom type hpicfPimIfMaxGraftRetries based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HpicfPimIfMaxGraftRetries_Type.__name__ = "Integer32"
_HpicfPimIfMaxGraftRetries_Object = MibTableColumn
hpicfPimIfMaxGraftRetries = _HpicfPimIfMaxGraftRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 10),
    _HpicfPimIfMaxGraftRetries_Type()
)
hpicfPimIfMaxGraftRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfMaxGraftRetries.setStatus("current")


class _HpicfPimIfSRTTLThreshold_Type(Unsigned32):
    """Custom type hpicfPimIfSRTTLThreshold based on Unsigned32"""
    defaultValue = 0


_HpicfPimIfSRTTLThreshold_Object = MibTableColumn
hpicfPimIfSRTTLThreshold = _HpicfPimIfSRTTLThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 11),
    _HpicfPimIfSRTTLThreshold_Type()
)
hpicfPimIfSRTTLThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfSRTTLThreshold.setStatus("current")
_HpicfPimIfLanDelayEnabled_Type = TruthValue
_HpicfPimIfLanDelayEnabled_Object = MibTableColumn
hpicfPimIfLanDelayEnabled = _HpicfPimIfLanDelayEnabled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 12),
    _HpicfPimIfLanDelayEnabled_Type()
)
hpicfPimIfLanDelayEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfLanDelayEnabled.setStatus("current")
_HpicfPimIfSRCapable_Type = TruthValue
_HpicfPimIfSRCapable_Object = MibTableColumn
hpicfPimIfSRCapable = _HpicfPimIfSRCapable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 13),
    _HpicfPimIfSRCapable_Type()
)
hpicfPimIfSRCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfSRCapable.setStatus("current")


class _HpicfPimIfDRPriority_Type(Unsigned32):
    """Custom type hpicfPimIfDRPriority based on Unsigned32"""
    defaultValue = 1


_HpicfPimIfDRPriority_Object = MibTableColumn
hpicfPimIfDRPriority = _HpicfPimIfDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 14),
    _HpicfPimIfDRPriority_Type()
)
hpicfPimIfDRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfDRPriority.setStatus("current")


class _HpicfPimIfNBRTimeout_Type(Integer32):
    """Custom type hpicfPimIfNBRTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 8000),
    )


_HpicfPimIfNBRTimeout_Type.__name__ = "Integer32"
_HpicfPimIfNBRTimeout_Object = MibTableColumn
hpicfPimIfNBRTimeout = _HpicfPimIfNBRTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 15),
    _HpicfPimIfNBRTimeout_Type()
)
hpicfPimIfNBRTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimIfNBRTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPimIfNBRTimeout.setUnits("seconds")
_HpicfPimIfNBRCount_Type = Counter32
_HpicfPimIfNBRCount_Object = MibTableColumn
hpicfPimIfNBRCount = _HpicfPimIfNBRCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 16),
    _HpicfPimIfNBRCount_Type()
)
hpicfPimIfNBRCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfNBRCount.setStatus("current")
_HpicfPimIfNegotiatedPropagationDelay_Type = TimeTicks
_HpicfPimIfNegotiatedPropagationDelay_Object = MibTableColumn
hpicfPimIfNegotiatedPropagationDelay = _HpicfPimIfNegotiatedPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 17),
    _HpicfPimIfNegotiatedPropagationDelay_Type()
)
hpicfPimIfNegotiatedPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfNegotiatedPropagationDelay.setStatus("current")
_HpicfPimIfNegotiatedOverrideInterval_Type = TimeTicks
_HpicfPimIfNegotiatedOverrideInterval_Object = MibTableColumn
hpicfPimIfNegotiatedOverrideInterval = _HpicfPimIfNegotiatedOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 18),
    _HpicfPimIfNegotiatedOverrideInterval_Type()
)
hpicfPimIfNegotiatedOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfNegotiatedOverrideInterval.setStatus("current")
_HpicfPimIfAssertHoldInterval_Type = Counter32
_HpicfPimIfAssertHoldInterval_Object = MibTableColumn
hpicfPimIfAssertHoldInterval = _HpicfPimIfAssertHoldInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 19),
    _HpicfPimIfAssertHoldInterval_Type()
)
hpicfPimIfAssertHoldInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfAssertHoldInterval.setStatus("current")
_HpicfPimIfNumRoutersNotUsingDRPriority_Type = Counter32
_HpicfPimIfNumRoutersNotUsingDRPriority_Object = MibTableColumn
hpicfPimIfNumRoutersNotUsingDRPriority = _HpicfPimIfNumRoutersNotUsingDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 20),
    _HpicfPimIfNumRoutersNotUsingDRPriority_Type()
)
hpicfPimIfNumRoutersNotUsingDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfNumRoutersNotUsingDRPriority.setStatus("current")
_HpicfPimIfNumRoutersNotUsingLanDelay_Type = Counter32
_HpicfPimIfNumRoutersNotUsingLanDelay_Object = MibTableColumn
hpicfPimIfNumRoutersNotUsingLanDelay = _HpicfPimIfNumRoutersNotUsingLanDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 6, 1, 21),
    _HpicfPimIfNumRoutersNotUsingLanDelay_Type()
)
hpicfPimIfNumRoutersNotUsingLanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfNumRoutersNotUsingLanDelay.setStatus("current")
_HpicfPimComponentTable_Object = MibTable
hpicfPimComponentTable = _HpicfPimComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfPimComponentTable.setStatus("current")
_HpicfPimComponentEntry_Object = MibTableRow
hpicfPimComponentEntry = _HpicfPimComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpicfPimComponentEntry.setStatus("current")


class _HpicfPimComponentCBSRAdminStatus_Type(Integer32):
    """Custom type hpicfPimComponentCBSRAdminStatus based on Integer32"""
    defaultValue = 2

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


_HpicfPimComponentCBSRAdminStatus_Type.__name__ = "Integer32"
_HpicfPimComponentCBSRAdminStatus_Object = MibTableColumn
hpicfPimComponentCBSRAdminStatus = _HpicfPimComponentCBSRAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 1),
    _HpicfPimComponentCBSRAdminStatus_Type()
)
hpicfPimComponentCBSRAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimComponentCBSRAdminStatus.setStatus("current")
_HpicfPimComponentCBSRAddress_Type = IpAddress
_HpicfPimComponentCBSRAddress_Object = MibTableColumn
hpicfPimComponentCBSRAddress = _HpicfPimComponentCBSRAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 2),
    _HpicfPimComponentCBSRAddress_Type()
)
hpicfPimComponentCBSRAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimComponentCBSRAddress.setStatus("current")


class _HpicfPimComponentCBSRPriority_Type(Integer32):
    """Custom type hpicfPimComponentCBSRPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfPimComponentCBSRPriority_Type.__name__ = "Integer32"
_HpicfPimComponentCBSRPriority_Object = MibTableColumn
hpicfPimComponentCBSRPriority = _HpicfPimComponentCBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 3),
    _HpicfPimComponentCBSRPriority_Type()
)
hpicfPimComponentCBSRPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimComponentCBSRPriority.setStatus("current")


class _HpicfPimComponentCBSRHashMaskLength_Type(Integer32):
    """Custom type hpicfPimComponentCBSRHashMaskLength based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HpicfPimComponentCBSRHashMaskLength_Type.__name__ = "Integer32"
_HpicfPimComponentCBSRHashMaskLength_Object = MibTableColumn
hpicfPimComponentCBSRHashMaskLength = _HpicfPimComponentCBSRHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 4),
    _HpicfPimComponentCBSRHashMaskLength_Type()
)
hpicfPimComponentCBSRHashMaskLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimComponentCBSRHashMaskLength.setStatus("current")


class _HpicfPimComponentCBSRMessageInterval_Type(Integer32):
    """Custom type hpicfPimComponentCBSRMessageInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_HpicfPimComponentCBSRMessageInterval_Type.__name__ = "Integer32"
_HpicfPimComponentCBSRMessageInterval_Object = MibTableColumn
hpicfPimComponentCBSRMessageInterval = _HpicfPimComponentCBSRMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 5),
    _HpicfPimComponentCBSRMessageInterval_Type()
)
hpicfPimComponentCBSRMessageInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimComponentCBSRMessageInterval.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPimComponentCBSRMessageInterval.setUnits("seconds")


class _HpicfPimComponentCRPPriority_Type(Integer32):
    """Custom type hpicfPimComponentCRPPriority based on Integer32"""
    defaultValue = 192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfPimComponentCRPPriority_Type.__name__ = "Integer32"
_HpicfPimComponentCRPPriority_Object = MibTableColumn
hpicfPimComponentCRPPriority = _HpicfPimComponentCRPPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 6),
    _HpicfPimComponentCRPPriority_Type()
)
hpicfPimComponentCRPPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimComponentCRPPriority.setStatus("current")
_HpicfPimComponentCRPAdvInterval_Type = Unsigned32
_HpicfPimComponentCRPAdvInterval_Object = MibTableColumn
hpicfPimComponentCRPAdvInterval = _HpicfPimComponentCRPAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 7),
    _HpicfPimComponentCRPAdvInterval_Type()
)
hpicfPimComponentCRPAdvInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimComponentCRPAdvInterval.setStatus("current")
_HpicfPimComponentBSRPriority_Type = Unsigned32
_HpicfPimComponentBSRPriority_Object = MibTableColumn
hpicfPimComponentBSRPriority = _HpicfPimComponentBSRPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 8),
    _HpicfPimComponentBSRPriority_Type()
)
hpicfPimComponentBSRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimComponentBSRPriority.setStatus("current")
_HpicfPimComponentBSRHashMaskLength_Type = Unsigned32
_HpicfPimComponentBSRHashMaskLength_Object = MibTableColumn
hpicfPimComponentBSRHashMaskLength = _HpicfPimComponentBSRHashMaskLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 9),
    _HpicfPimComponentBSRHashMaskLength_Type()
)
hpicfPimComponentBSRHashMaskLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimComponentBSRHashMaskLength.setStatus("current")
_HpicfPimComponentBSRUpTime_Type = TimeTicks
_HpicfPimComponentBSRUpTime_Object = MibTableColumn
hpicfPimComponentBSRUpTime = _HpicfPimComponentBSRUpTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 10),
    _HpicfPimComponentBSRUpTime_Type()
)
hpicfPimComponentBSRUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimComponentBSRUpTime.setStatus("current")
_HpicfPimComponentBSRNextMessage_Type = TimeTicks
_HpicfPimComponentBSRNextMessage_Object = MibTableColumn
hpicfPimComponentBSRNextMessage = _HpicfPimComponentBSRNextMessage_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 11),
    _HpicfPimComponentBSRNextMessage_Type()
)
hpicfPimComponentBSRNextMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimComponentBSRNextMessage.setStatus("current")
_HpicfPimComponentCRPAdvTimer_Type = TimeTicks
_HpicfPimComponentCRPAdvTimer_Object = MibTableColumn
hpicfPimComponentCRPAdvTimer = _HpicfPimComponentCRPAdvTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 7, 1, 12),
    _HpicfPimComponentCRPAdvTimer_Type()
)
hpicfPimComponentCRPAdvTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimComponentCRPAdvTimer.setStatus("current")


class _HpicfPimRemoveConfig_Type(TruthValue):
    """Custom type hpicfPimRemoveConfig based on TruthValue"""


_HpicfPimRemoveConfig_Object = MibScalar
hpicfPimRemoveConfig = _HpicfPimRemoveConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 8),
    _HpicfPimRemoveConfig_Type()
)
hpicfPimRemoveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfPimRemoveConfig.setStatus("current")
_HpicfPimStaticRpfTable_Object = MibTable
hpicfPimStaticRpfTable = _HpicfPimStaticRpfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hpicfPimStaticRpfTable.setStatus("current")
_HpicfPimStaticRpfEntry_Object = MibTableRow
hpicfPimStaticRpfEntry = _HpicfPimStaticRpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9, 1)
)
hpicfPimStaticRpfEntry.setIndexNames(
    (0, "HP-ICF-PIM", "hpicfPimStaticRpfSourceAddressType"),
    (0, "HP-ICF-PIM", "hpicfPimStaticRpfSourceAddress"),
    (0, "HP-ICF-PIM", "hpicfPimStaticRpfSourcePrefixLength"),
    (0, "HP-ICF-PIM", "hpicfPimStaticRpfAddressType"),
    (0, "HP-ICF-PIM", "hpicfPimStaticRpfAddress"),
)
if mibBuilder.loadTexts:
    hpicfPimStaticRpfEntry.setStatus("current")
_HpicfPimStaticRpfSourceAddressType_Type = InetAddressType
_HpicfPimStaticRpfSourceAddressType_Object = MibTableColumn
hpicfPimStaticRpfSourceAddressType = _HpicfPimStaticRpfSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9, 1, 1),
    _HpicfPimStaticRpfSourceAddressType_Type()
)
hpicfPimStaticRpfSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimStaticRpfSourceAddressType.setStatus("current")
_HpicfPimStaticRpfSourceAddress_Type = InetAddress
_HpicfPimStaticRpfSourceAddress_Object = MibTableColumn
hpicfPimStaticRpfSourceAddress = _HpicfPimStaticRpfSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9, 1, 2),
    _HpicfPimStaticRpfSourceAddress_Type()
)
hpicfPimStaticRpfSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimStaticRpfSourceAddress.setStatus("current")
_HpicfPimStaticRpfSourcePrefixLength_Type = InetAddressPrefixLength
_HpicfPimStaticRpfSourcePrefixLength_Object = MibTableColumn
hpicfPimStaticRpfSourcePrefixLength = _HpicfPimStaticRpfSourcePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9, 1, 3),
    _HpicfPimStaticRpfSourcePrefixLength_Type()
)
hpicfPimStaticRpfSourcePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimStaticRpfSourcePrefixLength.setStatus("current")
_HpicfPimStaticRpfAddressType_Type = InetAddressType
_HpicfPimStaticRpfAddressType_Object = MibTableColumn
hpicfPimStaticRpfAddressType = _HpicfPimStaticRpfAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9, 1, 4),
    _HpicfPimStaticRpfAddressType_Type()
)
hpicfPimStaticRpfAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimStaticRpfAddressType.setStatus("current")
_HpicfPimStaticRpfAddress_Type = InetAddress
_HpicfPimStaticRpfAddress_Object = MibTableColumn
hpicfPimStaticRpfAddress = _HpicfPimStaticRpfAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9, 1, 5),
    _HpicfPimStaticRpfAddress_Type()
)
hpicfPimStaticRpfAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimStaticRpfAddress.setStatus("current")
_HpicfPimStaticRpfRowStatus_Type = RowStatus
_HpicfPimStaticRpfRowStatus_Object = MibTableColumn
hpicfPimStaticRpfRowStatus = _HpicfPimStaticRpfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9, 1, 6),
    _HpicfPimStaticRpfRowStatus_Type()
)
hpicfPimStaticRpfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPimStaticRpfRowStatus.setStatus("current")


class _HpicfPimStaticRpfOverrideState_Type(Integer32):
    """Custom type hpicfPimStaticRpfOverrideState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inActive", 2))
    )


_HpicfPimStaticRpfOverrideState_Type.__name__ = "Integer32"
_HpicfPimStaticRpfOverrideState_Object = MibTableColumn
hpicfPimStaticRpfOverrideState = _HpicfPimStaticRpfOverrideState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9, 1, 7),
    _HpicfPimStaticRpfOverrideState_Type()
)
hpicfPimStaticRpfOverrideState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimStaticRpfOverrideState.setStatus("current")
_HpicfPimStaticRpfIfIndex_Type = InterfaceIndex
_HpicfPimStaticRpfIfIndex_Object = MibTableColumn
hpicfPimStaticRpfIfIndex = _HpicfPimStaticRpfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9, 1, 8),
    _HpicfPimStaticRpfIfIndex_Type()
)
hpicfPimStaticRpfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimStaticRpfIfIndex.setStatus("current")
_HpicfPimStaticRpfNeighborAddressType_Type = InetAddressType
_HpicfPimStaticRpfNeighborAddressType_Object = MibTableColumn
hpicfPimStaticRpfNeighborAddressType = _HpicfPimStaticRpfNeighborAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9, 1, 9),
    _HpicfPimStaticRpfNeighborAddressType_Type()
)
hpicfPimStaticRpfNeighborAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimStaticRpfNeighborAddressType.setStatus("current")
_HpicfPimStaticRpfNeighborAddress_Type = InetAddress
_HpicfPimStaticRpfNeighborAddress_Object = MibTableColumn
hpicfPimStaticRpfNeighborAddress = _HpicfPimStaticRpfNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 9, 1, 10),
    _HpicfPimStaticRpfNeighborAddress_Type()
)
hpicfPimStaticRpfNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimStaticRpfNeighborAddress.setStatus("current")
_HpicfPimNumStaticRpfEntries_Type = Counter32
_HpicfPimNumStaticRpfEntries_Object = MibScalar
hpicfPimNumStaticRpfEntries = _HpicfPimNumStaticRpfEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 10),
    _HpicfPimNumStaticRpfEntries_Type()
)
hpicfPimNumStaticRpfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimNumStaticRpfEntries.setStatus("current")
_HpicfPimVersion_Type = Counter32
_HpicfPimVersion_Object = MibScalar
hpicfPimVersion = _HpicfPimVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 11),
    _HpicfPimVersion_Type()
)
hpicfPimVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimVersion.setStatus("current")
_HpicfPimStarGEntries_Type = Counter32
_HpicfPimStarGEntries_Object = MibScalar
hpicfPimStarGEntries = _HpicfPimStarGEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 12),
    _HpicfPimStarGEntries_Type()
)
hpicfPimStarGEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimStarGEntries.setStatus("current")
_HpicfPimSGEntries_Type = Counter32
_HpicfPimSGEntries_Object = MibScalar
hpicfPimSGEntries = _HpicfPimSGEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 13),
    _HpicfPimSGEntries_Type()
)
hpicfPimSGEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimSGEntries.setStatus("current")
_HpicfPimMRouteTable_Object = MibTable
hpicfPimMRouteTable = _HpicfPimMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14)
)
if mibBuilder.loadTexts:
    hpicfPimMRouteTable.setStatus("current")
_HpicfPimMRouteEntry_Object = MibTableRow
hpicfPimMRouteEntry = _HpicfPimMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1)
)
if mibBuilder.loadTexts:
    hpicfPimMRouteEntry.setStatus("current")
_HpicfPimSendRegStop_Type = TruthValue
_HpicfPimSendRegStop_Object = MibTableColumn
hpicfPimSendRegStop = _HpicfPimSendRegStop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 1),
    _HpicfPimSendRegStop_Type()
)
hpicfPimSendRegStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimSendRegStop.setStatus("current")
_HpicfPimSGSourceIsActive_Type = TruthValue
_HpicfPimSGSourceIsActive_Object = MibTableColumn
hpicfPimSGSourceIsActive = _HpicfPimSGSourceIsActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 2),
    _HpicfPimSGSourceIsActive_Type()
)
hpicfPimSGSourceIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimSGSourceIsActive.setStatus("current")
_HpicfPimOutgoingRegisterIfAvailable_Type = TruthValue
_HpicfPimOutgoingRegisterIfAvailable_Object = MibTableColumn
hpicfPimOutgoingRegisterIfAvailable = _HpicfPimOutgoingRegisterIfAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 3),
    _HpicfPimOutgoingRegisterIfAvailable_Type()
)
hpicfPimOutgoingRegisterIfAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimOutgoingRegisterIfAvailable.setStatus("current")
_HpicfPimEntryAddSuccess_Type = TruthValue
_HpicfPimEntryAddSuccess_Object = MibTableColumn
hpicfPimEntryAddSuccess = _HpicfPimEntryAddSuccess_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 4),
    _HpicfPimEntryAddSuccess_Type()
)
hpicfPimEntryAddSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimEntryAddSuccess.setStatus("current")
_HpicfPimNumOutgoingInterfaces_Type = Counter32
_HpicfPimNumOutgoingInterfaces_Object = MibTableColumn
hpicfPimNumOutgoingInterfaces = _HpicfPimNumOutgoingInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 5),
    _HpicfPimNumOutgoingInterfaces_Type()
)
hpicfPimNumOutgoingInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimNumOutgoingInterfaces.setStatus("current")
_HpicfPimDirectlyConnectedSource_Type = TruthValue
_HpicfPimDirectlyConnectedSource_Object = MibTableColumn
hpicfPimDirectlyConnectedSource = _HpicfPimDirectlyConnectedSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 6),
    _HpicfPimDirectlyConnectedSource_Type()
)
hpicfPimDirectlyConnectedSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimDirectlyConnectedSource.setStatus("current")
_HpicfPimNeighborSearchFailure_Type = TruthValue
_HpicfPimNeighborSearchFailure_Object = MibTableColumn
hpicfPimNeighborSearchFailure = _HpicfPimNeighborSearchFailure_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 7),
    _HpicfPimNeighborSearchFailure_Type()
)
hpicfPimNeighborSearchFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimNeighborSearchFailure.setStatus("current")
_HpicfPimRPTreePruneSent_Type = TruthValue
_HpicfPimRPTreePruneSent_Object = MibTableColumn
hpicfPimRPTreePruneSent = _HpicfPimRPTreePruneSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 8),
    _HpicfPimRPTreePruneSent_Type()
)
hpicfPimRPTreePruneSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimRPTreePruneSent.setStatus("current")
_HpicfPimOnSPTree_Type = TruthValue
_HpicfPimOnSPTree_Object = MibTableColumn
hpicfPimOnSPTree = _HpicfPimOnSPTree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 9),
    _HpicfPimOnSPTree_Type()
)
hpicfPimOnSPTree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimOnSPTree.setStatus("current")
_HpicfPimRPToSPTreeSwitching_Type = TruthValue
_HpicfPimRPToSPTreeSwitching_Object = MibTableColumn
hpicfPimRPToSPTreeSwitching = _HpicfPimRPToSPTreeSwitching_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 10),
    _HpicfPimRPToSPTreeSwitching_Type()
)
hpicfPimRPToSPTreeSwitching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimRPToSPTreeSwitching.setStatus("current")
_HpicfPimWildcardEntry_Type = TruthValue
_HpicfPimWildcardEntry_Object = MibTableColumn
hpicfPimWildcardEntry = _HpicfPimWildcardEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 11),
    _HpicfPimWildcardEntry_Type()
)
hpicfPimWildcardEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimWildcardEntry.setStatus("current")
_HpicfPimRPFPrimeNeighborAddressType_Type = InetAddressType
_HpicfPimRPFPrimeNeighborAddressType_Object = MibTableColumn
hpicfPimRPFPrimeNeighborAddressType = _HpicfPimRPFPrimeNeighborAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 12),
    _HpicfPimRPFPrimeNeighborAddressType_Type()
)
hpicfPimRPFPrimeNeighborAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimRPFPrimeNeighborAddressType.setStatus("current")
_HpicfPimRPFPrimeNeighborAddress_Type = InetAddress
_HpicfPimRPFPrimeNeighborAddress_Object = MibTableColumn
hpicfPimRPFPrimeNeighborAddress = _HpicfPimRPFPrimeNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 13),
    _HpicfPimRPFPrimeNeighborAddress_Type()
)
hpicfPimRPFPrimeNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimRPFPrimeNeighborAddress.setStatus("current")
_HpicfPimNumDownstreams_Type = Counter32
_HpicfPimNumDownstreams_Object = MibTableColumn
hpicfPimNumDownstreams = _HpicfPimNumDownstreams_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 14, 1, 14),
    _HpicfPimNumDownstreams_Type()
)
hpicfPimNumDownstreams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimNumDownstreams.setStatus("current")
_HpicfPimTotalNeighborCount_Type = Counter32
_HpicfPimTotalNeighborCount_Object = MibScalar
hpicfPimTotalNeighborCount = _HpicfPimTotalNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 15),
    _HpicfPimTotalNeighborCount_Type()
)
hpicfPimTotalNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimTotalNeighborCount.setStatus("current")
_HpicfPimNeighborTable_Object = MibTable
hpicfPimNeighborTable = _HpicfPimNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 16)
)
if mibBuilder.loadTexts:
    hpicfPimNeighborTable.setStatus("current")
_HpicfPimNeighborEntry_Object = MibTableRow
hpicfPimNeighborEntry = _HpicfPimNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    hpicfPimNeighborEntry.setStatus("current")
_HpicfPimNeighborDRPriority_Type = Counter32
_HpicfPimNeighborDRPriority_Object = MibTableColumn
hpicfPimNeighborDRPriority = _HpicfPimNeighborDRPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 16, 1, 1),
    _HpicfPimNeighborDRPriority_Type()
)
hpicfPimNeighborDRPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimNeighborDRPriority.setStatus("current")
_HpicfPimNeighborGenerationIDValue_Type = Counter32
_HpicfPimNeighborGenerationIDValue_Object = MibTableColumn
hpicfPimNeighborGenerationIDValue = _HpicfPimNeighborGenerationIDValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 16, 1, 2),
    _HpicfPimNeighborGenerationIDValue_Type()
)
hpicfPimNeighborGenerationIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimNeighborGenerationIDValue.setStatus("current")
_HpicfPimNeighborHoldtime_Type = Counter32
_HpicfPimNeighborHoldtime_Object = MibTableColumn
hpicfPimNeighborHoldtime = _HpicfPimNeighborHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 16, 1, 3),
    _HpicfPimNeighborHoldtime_Type()
)
hpicfPimNeighborHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimNeighborHoldtime.setStatus("current")
_HpicfPimNeighborPropagationDelay_Type = Counter32
_HpicfPimNeighborPropagationDelay_Object = MibTableColumn
hpicfPimNeighborPropagationDelay = _HpicfPimNeighborPropagationDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 16, 1, 4),
    _HpicfPimNeighborPropagationDelay_Type()
)
hpicfPimNeighborPropagationDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimNeighborPropagationDelay.setStatus("current")
_HpicfPimNeighborOverrideInterval_Type = Counter32
_HpicfPimNeighborOverrideInterval_Object = MibTableColumn
hpicfPimNeighborOverrideInterval = _HpicfPimNeighborOverrideInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 16, 1, 5),
    _HpicfPimNeighborOverrideInterval_Type()
)
hpicfPimNeighborOverrideInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimNeighborOverrideInterval.setStatus("current")
_HpicfPimNeighborStateRefreshInterval_Type = Counter32
_HpicfPimNeighborStateRefreshInterval_Object = MibTableColumn
hpicfPimNeighborStateRefreshInterval = _HpicfPimNeighborStateRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 16, 1, 6),
    _HpicfPimNeighborStateRefreshInterval_Type()
)
hpicfPimNeighborStateRefreshInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimNeighborStateRefreshInterval.setStatus("current")
_HpicfPimUcastRouteTable_Object = MibTable
hpicfPimUcastRouteTable = _HpicfPimUcastRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 17)
)
if mibBuilder.loadTexts:
    hpicfPimUcastRouteTable.setStatus("current")
_HpicfPimUcastRouteEntry_Object = MibTableRow
hpicfPimUcastRouteEntry = _HpicfPimUcastRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 17, 1)
)
hpicfPimUcastRouteEntry.setIndexNames(
    (0, "HP-ICF-PIM", "hpicfPimUcastRouteAddressType"),
    (0, "HP-ICF-PIM", "hpicfPimUcastRouteAddress"),
    (0, "HP-ICF-PIM", "hpicfPimUcastRoutePrefix"),
)
if mibBuilder.loadTexts:
    hpicfPimUcastRouteEntry.setStatus("current")
_HpicfPimUcastRouteAddressType_Type = InetAddressType
_HpicfPimUcastRouteAddressType_Object = MibTableColumn
hpicfPimUcastRouteAddressType = _HpicfPimUcastRouteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 17, 1, 1),
    _HpicfPimUcastRouteAddressType_Type()
)
hpicfPimUcastRouteAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimUcastRouteAddressType.setStatus("current")
_HpicfPimUcastRouteAddress_Type = InetAddress
_HpicfPimUcastRouteAddress_Object = MibTableColumn
hpicfPimUcastRouteAddress = _HpicfPimUcastRouteAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 17, 1, 2),
    _HpicfPimUcastRouteAddress_Type()
)
hpicfPimUcastRouteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimUcastRouteAddress.setStatus("current")
_HpicfPimUcastRoutePrefix_Type = Unsigned32
_HpicfPimUcastRoutePrefix_Object = MibTableColumn
hpicfPimUcastRoutePrefix = _HpicfPimUcastRoutePrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 17, 1, 3),
    _HpicfPimUcastRoutePrefix_Type()
)
hpicfPimUcastRoutePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimUcastRoutePrefix.setStatus("current")
_HpicfPimUcastRouteIfIndex_Type = InterfaceIndex
_HpicfPimUcastRouteIfIndex_Object = MibTableColumn
hpicfPimUcastRouteIfIndex = _HpicfPimUcastRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 17, 1, 4),
    _HpicfPimUcastRouteIfIndex_Type()
)
hpicfPimUcastRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimUcastRouteIfIndex.setStatus("current")
_HpicfPimUcastRouteUpstreamNbrType_Type = InetAddressType
_HpicfPimUcastRouteUpstreamNbrType_Object = MibTableColumn
hpicfPimUcastRouteUpstreamNbrType = _HpicfPimUcastRouteUpstreamNbrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 17, 1, 5),
    _HpicfPimUcastRouteUpstreamNbrType_Type()
)
hpicfPimUcastRouteUpstreamNbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimUcastRouteUpstreamNbrType.setStatus("current")
_HpicfPimUcastRouteUpstreamNbr_Type = InetAddress
_HpicfPimUcastRouteUpstreamNbr_Object = MibTableColumn
hpicfPimUcastRouteUpstreamNbr = _HpicfPimUcastRouteUpstreamNbr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 17, 1, 6),
    _HpicfPimUcastRouteUpstreamNbr_Type()
)
hpicfPimUcastRouteUpstreamNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimUcastRouteUpstreamNbr.setStatus("current")
_HpicfPimUcastRouteProtocol_Type = Unsigned32
_HpicfPimUcastRouteProtocol_Object = MibTableColumn
hpicfPimUcastRouteProtocol = _HpicfPimUcastRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 17, 1, 7),
    _HpicfPimUcastRouteProtocol_Type()
)
hpicfPimUcastRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimUcastRouteProtocol.setStatus("current")
_HpicfPimJoinPruneTable_Object = MibTable
hpicfPimJoinPruneTable = _HpicfPimJoinPruneTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 18)
)
if mibBuilder.loadTexts:
    hpicfPimJoinPruneTable.setStatus("current")
_HpicfPimJoinPruneEntry_Object = MibTableRow
hpicfPimJoinPruneEntry = _HpicfPimJoinPruneEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 18, 1)
)
hpicfPimJoinPruneEntry.setIndexNames(
    (0, "HP-ICF-PIM", "hpicfPimJoinPruneInterface"),
    (0, "HP-ICF-PIM", "hpicfPimJoinPruneInterfaceState"),
    (0, "HP-ICF-PIM", "hpicfPimJoinPruneSourceType"),
    (0, "HP-ICF-PIM", "hpicfPimJoinPruneSourceAddress"),
    (0, "HP-ICF-PIM", "hpicfPimJoinPruneGroupType"),
    (0, "HP-ICF-PIM", "hpicfPimJoinPruneGroupAddress"),
)
if mibBuilder.loadTexts:
    hpicfPimJoinPruneEntry.setStatus("current")
_HpicfPimJoinPruneInterface_Type = InterfaceIndex
_HpicfPimJoinPruneInterface_Object = MibTableColumn
hpicfPimJoinPruneInterface = _HpicfPimJoinPruneInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 18, 1, 1),
    _HpicfPimJoinPruneInterface_Type()
)
hpicfPimJoinPruneInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimJoinPruneInterface.setStatus("current")


class _HpicfPimJoinPruneInterfaceState_Type(Integer32):
    """Custom type hpicfPimJoinPruneInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("join", 1),
          ("prune", 2))
    )


_HpicfPimJoinPruneInterfaceState_Type.__name__ = "Integer32"
_HpicfPimJoinPruneInterfaceState_Object = MibTableColumn
hpicfPimJoinPruneInterfaceState = _HpicfPimJoinPruneInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 18, 1, 2),
    _HpicfPimJoinPruneInterfaceState_Type()
)
hpicfPimJoinPruneInterfaceState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimJoinPruneInterfaceState.setStatus("current")
_HpicfPimJoinPruneSourceType_Type = InetAddressType
_HpicfPimJoinPruneSourceType_Object = MibTableColumn
hpicfPimJoinPruneSourceType = _HpicfPimJoinPruneSourceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 18, 1, 3),
    _HpicfPimJoinPruneSourceType_Type()
)
hpicfPimJoinPruneSourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimJoinPruneSourceType.setStatus("current")
_HpicfPimJoinPruneSourceAddress_Type = InetAddress
_HpicfPimJoinPruneSourceAddress_Object = MibTableColumn
hpicfPimJoinPruneSourceAddress = _HpicfPimJoinPruneSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 18, 1, 4),
    _HpicfPimJoinPruneSourceAddress_Type()
)
hpicfPimJoinPruneSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimJoinPruneSourceAddress.setStatus("current")
_HpicfPimJoinPruneGroupType_Type = InetAddressType
_HpicfPimJoinPruneGroupType_Object = MibTableColumn
hpicfPimJoinPruneGroupType = _HpicfPimJoinPruneGroupType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 18, 1, 5),
    _HpicfPimJoinPruneGroupType_Type()
)
hpicfPimJoinPruneGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimJoinPruneGroupType.setStatus("current")
_HpicfPimJoinPruneGroupAddress_Type = InetAddress
_HpicfPimJoinPruneGroupAddress_Object = MibTableColumn
hpicfPimJoinPruneGroupAddress = _HpicfPimJoinPruneGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 18, 1, 6),
    _HpicfPimJoinPruneGroupAddress_Type()
)
hpicfPimJoinPruneGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimJoinPruneGroupAddress.setStatus("current")
_HpicfPimJoinPruneNeighborAddressType_Type = InetAddressType
_HpicfPimJoinPruneNeighborAddressType_Object = MibTableColumn
hpicfPimJoinPruneNeighborAddressType = _HpicfPimJoinPruneNeighborAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 18, 1, 7),
    _HpicfPimJoinPruneNeighborAddressType_Type()
)
hpicfPimJoinPruneNeighborAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimJoinPruneNeighborAddressType.setStatus("current")
_HpicfPimJoinPruneNeighborAddress_Type = InetAddress
_HpicfPimJoinPruneNeighborAddress_Object = MibTableColumn
hpicfPimJoinPruneNeighborAddress = _HpicfPimJoinPruneNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 18, 1, 8),
    _HpicfPimJoinPruneNeighborAddress_Type()
)
hpicfPimJoinPruneNeighborAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimJoinPruneNeighborAddress.setStatus("current")
_HpicfPimJoinPruneExpiryTime_Type = Unsigned32
_HpicfPimJoinPruneExpiryTime_Object = MibTableColumn
hpicfPimJoinPruneExpiryTime = _HpicfPimJoinPruneExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 18, 1, 9),
    _HpicfPimJoinPruneExpiryTime_Type()
)
hpicfPimJoinPruneExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimJoinPruneExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfPimJoinPruneExpiryTime.setUnits("seconds")
_HpicfPimRPSetTable_Object = MibTable
hpicfPimRPSetTable = _HpicfPimRPSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 19)
)
if mibBuilder.loadTexts:
    hpicfPimRPSetTable.setStatus("current")
_HpicfPimRPSetEntry_Object = MibTableRow
hpicfPimRPSetEntry = _HpicfPimRPSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 19, 1)
)
if mibBuilder.loadTexts:
    hpicfPimRPSetEntry.setStatus("current")
_HpicfPimRPSetPriority_Type = Counter32
_HpicfPimRPSetPriority_Object = MibTableColumn
hpicfPimRPSetPriority = _HpicfPimRPSetPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 19, 1, 1),
    _HpicfPimRPSetPriority_Type()
)
hpicfPimRPSetPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimRPSetPriority.setStatus("current")
_HpicfPimRPSetUptime_Type = TimeTicks
_HpicfPimRPSetUptime_Object = MibTableColumn
hpicfPimRPSetUptime = _HpicfPimRPSetUptime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 19, 1, 2),
    _HpicfPimRPSetUptime_Type()
)
hpicfPimRPSetUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimRPSetUptime.setStatus("current")
_HpicfPimIfMessageCounterTable_Object = MibTable
hpicfPimIfMessageCounterTable = _HpicfPimIfMessageCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20)
)
if mibBuilder.loadTexts:
    hpicfPimIfMessageCounterTable.setStatus("current")
_HpicfPimIfMessageCounterEntry_Object = MibTableRow
hpicfPimIfMessageCounterEntry = _HpicfPimIfMessageCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1)
)
hpicfPimIfMessageCounterEntry.setIndexNames(
    (0, "PIM-MIB", "pimInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    hpicfPimIfMessageCounterEntry.setStatus("current")
_HpicfPimIfMsgCountAssertReceive_Type = Counter32
_HpicfPimIfMsgCountAssertReceive_Object = MibTableColumn
hpicfPimIfMsgCountAssertReceive = _HpicfPimIfMsgCountAssertReceive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 1),
    _HpicfPimIfMsgCountAssertReceive_Type()
)
hpicfPimIfMsgCountAssertReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountAssertReceive.setStatus("current")
_HpicfPimIfMsgCountAssertTransmit_Type = Counter32
_HpicfPimIfMsgCountAssertTransmit_Object = MibTableColumn
hpicfPimIfMsgCountAssertTransmit = _HpicfPimIfMsgCountAssertTransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 2),
    _HpicfPimIfMsgCountAssertTransmit_Type()
)
hpicfPimIfMsgCountAssertTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountAssertTransmit.setStatus("current")
_HpicfPimIfMsgCountAssertInvalid_Type = Counter32
_HpicfPimIfMsgCountAssertInvalid_Object = MibTableColumn
hpicfPimIfMsgCountAssertInvalid = _HpicfPimIfMsgCountAssertInvalid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 3),
    _HpicfPimIfMsgCountAssertInvalid_Type()
)
hpicfPimIfMsgCountAssertInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountAssertInvalid.setStatus("current")
_HpicfPimIfMsgCountGraftReceive_Type = Counter32
_HpicfPimIfMsgCountGraftReceive_Object = MibTableColumn
hpicfPimIfMsgCountGraftReceive = _HpicfPimIfMsgCountGraftReceive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 4),
    _HpicfPimIfMsgCountGraftReceive_Type()
)
hpicfPimIfMsgCountGraftReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountGraftReceive.setStatus("current")
_HpicfPimIfMsgCountGraftTransmit_Type = Counter32
_HpicfPimIfMsgCountGraftTransmit_Object = MibTableColumn
hpicfPimIfMsgCountGraftTransmit = _HpicfPimIfMsgCountGraftTransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 5),
    _HpicfPimIfMsgCountGraftTransmit_Type()
)
hpicfPimIfMsgCountGraftTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountGraftTransmit.setStatus("current")
_HpicfPimIfMsgCountGraftInvalid_Type = Counter32
_HpicfPimIfMsgCountGraftInvalid_Object = MibTableColumn
hpicfPimIfMsgCountGraftInvalid = _HpicfPimIfMsgCountGraftInvalid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 6),
    _HpicfPimIfMsgCountGraftInvalid_Type()
)
hpicfPimIfMsgCountGraftInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountGraftInvalid.setStatus("current")
_HpicfPimIfMsgCountGraftAckReceive_Type = Counter32
_HpicfPimIfMsgCountGraftAckReceive_Object = MibTableColumn
hpicfPimIfMsgCountGraftAckReceive = _HpicfPimIfMsgCountGraftAckReceive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 7),
    _HpicfPimIfMsgCountGraftAckReceive_Type()
)
hpicfPimIfMsgCountGraftAckReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountGraftAckReceive.setStatus("current")
_HpicfPimIfMsgCountGraftAckTransmit_Type = Counter32
_HpicfPimIfMsgCountGraftAckTransmit_Object = MibTableColumn
hpicfPimIfMsgCountGraftAckTransmit = _HpicfPimIfMsgCountGraftAckTransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 8),
    _HpicfPimIfMsgCountGraftAckTransmit_Type()
)
hpicfPimIfMsgCountGraftAckTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountGraftAckTransmit.setStatus("current")
_HpicfPimIfMsgCountGraftAckInvalid_Type = Counter32
_HpicfPimIfMsgCountGraftAckInvalid_Object = MibTableColumn
hpicfPimIfMsgCountGraftAckInvalid = _HpicfPimIfMsgCountGraftAckInvalid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 9),
    _HpicfPimIfMsgCountGraftAckInvalid_Type()
)
hpicfPimIfMsgCountGraftAckInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountGraftAckInvalid.setStatus("current")
_HpicfPimIfMsgCountHelloReceive_Type = Counter32
_HpicfPimIfMsgCountHelloReceive_Object = MibTableColumn
hpicfPimIfMsgCountHelloReceive = _HpicfPimIfMsgCountHelloReceive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 10),
    _HpicfPimIfMsgCountHelloReceive_Type()
)
hpicfPimIfMsgCountHelloReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountHelloReceive.setStatus("current")
_HpicfPimIfMsgCountHelloTransmit_Type = Counter32
_HpicfPimIfMsgCountHelloTransmit_Object = MibTableColumn
hpicfPimIfMsgCountHelloTransmit = _HpicfPimIfMsgCountHelloTransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 11),
    _HpicfPimIfMsgCountHelloTransmit_Type()
)
hpicfPimIfMsgCountHelloTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountHelloTransmit.setStatus("current")
_HpicfPimIfMsgCountHelloInvalid_Type = Counter32
_HpicfPimIfMsgCountHelloInvalid_Object = MibTableColumn
hpicfPimIfMsgCountHelloInvalid = _HpicfPimIfMsgCountHelloInvalid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 12),
    _HpicfPimIfMsgCountHelloInvalid_Type()
)
hpicfPimIfMsgCountHelloInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountHelloInvalid.setStatus("current")
_HpicfPimIfMsgCountJPReceive_Type = Counter32
_HpicfPimIfMsgCountJPReceive_Object = MibTableColumn
hpicfPimIfMsgCountJPReceive = _HpicfPimIfMsgCountJPReceive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 13),
    _HpicfPimIfMsgCountJPReceive_Type()
)
hpicfPimIfMsgCountJPReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountJPReceive.setStatus("current")
_HpicfPimIfMsgCountJPTransmit_Type = Counter32
_HpicfPimIfMsgCountJPTransmit_Object = MibTableColumn
hpicfPimIfMsgCountJPTransmit = _HpicfPimIfMsgCountJPTransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 14),
    _HpicfPimIfMsgCountJPTransmit_Type()
)
hpicfPimIfMsgCountJPTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountJPTransmit.setStatus("current")
_HpicfPimIfMsgCountJPInvalid_Type = Counter32
_HpicfPimIfMsgCountJPInvalid_Object = MibTableColumn
hpicfPimIfMsgCountJPInvalid = _HpicfPimIfMsgCountJPInvalid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 15),
    _HpicfPimIfMsgCountJPInvalid_Type()
)
hpicfPimIfMsgCountJPInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountJPInvalid.setStatus("current")
_HpicfPimIfMsgCountSRReceive_Type = Counter32
_HpicfPimIfMsgCountSRReceive_Object = MibTableColumn
hpicfPimIfMsgCountSRReceive = _HpicfPimIfMsgCountSRReceive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 16),
    _HpicfPimIfMsgCountSRReceive_Type()
)
hpicfPimIfMsgCountSRReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountSRReceive.setStatus("current")
_HpicfPimIfMsgCountSRTransmit_Type = Counter32
_HpicfPimIfMsgCountSRTransmit_Object = MibTableColumn
hpicfPimIfMsgCountSRTransmit = _HpicfPimIfMsgCountSRTransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 17),
    _HpicfPimIfMsgCountSRTransmit_Type()
)
hpicfPimIfMsgCountSRTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountSRTransmit.setStatus("current")
_HpicfPimIfMsgCountSRInvalid_Type = Counter32
_HpicfPimIfMsgCountSRInvalid_Object = MibTableColumn
hpicfPimIfMsgCountSRInvalid = _HpicfPimIfMsgCountSRInvalid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 18),
    _HpicfPimIfMsgCountSRInvalid_Type()
)
hpicfPimIfMsgCountSRInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountSRInvalid.setStatus("current")
_HpicfPimIfMsgCountBSRReceive_Type = Counter32
_HpicfPimIfMsgCountBSRReceive_Object = MibTableColumn
hpicfPimIfMsgCountBSRReceive = _HpicfPimIfMsgCountBSRReceive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 19),
    _HpicfPimIfMsgCountBSRReceive_Type()
)
hpicfPimIfMsgCountBSRReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountBSRReceive.setStatus("current")
_HpicfPimIfMsgCountBSRTransmit_Type = Counter32
_HpicfPimIfMsgCountBSRTransmit_Object = MibTableColumn
hpicfPimIfMsgCountBSRTransmit = _HpicfPimIfMsgCountBSRTransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 20),
    _HpicfPimIfMsgCountBSRTransmit_Type()
)
hpicfPimIfMsgCountBSRTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountBSRTransmit.setStatus("current")
_HpicfPimIfMsgCountBSRInvalid_Type = Counter32
_HpicfPimIfMsgCountBSRInvalid_Object = MibTableColumn
hpicfPimIfMsgCountBSRInvalid = _HpicfPimIfMsgCountBSRInvalid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 21),
    _HpicfPimIfMsgCountBSRInvalid_Type()
)
hpicfPimIfMsgCountBSRInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountBSRInvalid.setStatus("current")
_HpicfPimIfMsgCountCRPReceive_Type = Counter32
_HpicfPimIfMsgCountCRPReceive_Object = MibTableColumn
hpicfPimIfMsgCountCRPReceive = _HpicfPimIfMsgCountCRPReceive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 22),
    _HpicfPimIfMsgCountCRPReceive_Type()
)
hpicfPimIfMsgCountCRPReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountCRPReceive.setStatus("current")
_HpicfPimIfMsgCountCRPTransmit_Type = Counter32
_HpicfPimIfMsgCountCRPTransmit_Object = MibTableColumn
hpicfPimIfMsgCountCRPTransmit = _HpicfPimIfMsgCountCRPTransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 23),
    _HpicfPimIfMsgCountCRPTransmit_Type()
)
hpicfPimIfMsgCountCRPTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountCRPTransmit.setStatus("current")
_HpicfPimIfMsgCountCRPInvalid_Type = Counter32
_HpicfPimIfMsgCountCRPInvalid_Object = MibTableColumn
hpicfPimIfMsgCountCRPInvalid = _HpicfPimIfMsgCountCRPInvalid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 20, 1, 24),
    _HpicfPimIfMsgCountCRPInvalid_Type()
)
hpicfPimIfMsgCountCRPInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimIfMsgCountCRPInvalid.setStatus("current")
_HpicfPimUnackGraftsTable_Object = MibTable
hpicfPimUnackGraftsTable = _HpicfPimUnackGraftsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 21)
)
if mibBuilder.loadTexts:
    hpicfPimUnackGraftsTable.setStatus("current")
_HpicfPimUnackGraftsEntry_Object = MibTableRow
hpicfPimUnackGraftsEntry = _HpicfPimUnackGraftsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 21, 1)
)
hpicfPimUnackGraftsEntry.setIndexNames(
    (0, "HP-ICF-PIM", "hpicfPimUnackGraftSourceType"),
    (0, "HP-ICF-PIM", "hpicfPimUnackGraftSource"),
    (0, "HP-ICF-PIM", "hpicfPimUnackGraftGroupType"),
    (0, "HP-ICF-PIM", "hpicfPimUnackGraftGroup"),
)
if mibBuilder.loadTexts:
    hpicfPimUnackGraftsEntry.setStatus("current")
_HpicfPimUnackGraftSourceType_Type = InetAddressType
_HpicfPimUnackGraftSourceType_Object = MibTableColumn
hpicfPimUnackGraftSourceType = _HpicfPimUnackGraftSourceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 21, 1, 1),
    _HpicfPimUnackGraftSourceType_Type()
)
hpicfPimUnackGraftSourceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimUnackGraftSourceType.setStatus("current")
_HpicfPimUnackGraftSource_Type = InetAddress
_HpicfPimUnackGraftSource_Object = MibTableColumn
hpicfPimUnackGraftSource = _HpicfPimUnackGraftSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 21, 1, 2),
    _HpicfPimUnackGraftSource_Type()
)
hpicfPimUnackGraftSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimUnackGraftSource.setStatus("current")
_HpicfPimUnackGraftGroupType_Type = InetAddressType
_HpicfPimUnackGraftGroupType_Object = MibTableColumn
hpicfPimUnackGraftGroupType = _HpicfPimUnackGraftGroupType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 21, 1, 3),
    _HpicfPimUnackGraftGroupType_Type()
)
hpicfPimUnackGraftGroupType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimUnackGraftGroupType.setStatus("current")
_HpicfPimUnackGraftGroup_Type = InetAddress
_HpicfPimUnackGraftGroup_Object = MibTableColumn
hpicfPimUnackGraftGroup = _HpicfPimUnackGraftGroup_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 21, 1, 4),
    _HpicfPimUnackGraftGroup_Type()
)
hpicfPimUnackGraftGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfPimUnackGraftGroup.setStatus("current")
_HpicfPimUnackGraftAge_Type = Counter32
_HpicfPimUnackGraftAge_Object = MibTableColumn
hpicfPimUnackGraftAge = _HpicfPimUnackGraftAge_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 21, 1, 5),
    _HpicfPimUnackGraftAge_Type()
)
hpicfPimUnackGraftAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimUnackGraftAge.setStatus("current")
_HpicfPimUnackGraftRetransIn_Type = Counter32
_HpicfPimUnackGraftRetransIn_Object = MibTableColumn
hpicfPimUnackGraftRetransIn = _HpicfPimUnackGraftRetransIn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 1, 21, 1, 6),
    _HpicfPimUnackGraftRetransIn_Type()
)
hpicfPimUnackGraftRetransIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimUnackGraftRetransIn.setStatus("current")
_HpicfPimScalars_ObjectIdentity = ObjectIdentity
hpicfPimScalars = _HpicfPimScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 2)
)
_HpicfPimMsgCountRegisterReceive_Type = Counter32
_HpicfPimMsgCountRegisterReceive_Object = MibScalar
hpicfPimMsgCountRegisterReceive = _HpicfPimMsgCountRegisterReceive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 2, 1),
    _HpicfPimMsgCountRegisterReceive_Type()
)
hpicfPimMsgCountRegisterReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimMsgCountRegisterReceive.setStatus("current")
_HpicfPimMsgCountRegisterTransmit_Type = Counter32
_HpicfPimMsgCountRegisterTransmit_Object = MibScalar
hpicfPimMsgCountRegisterTransmit = _HpicfPimMsgCountRegisterTransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 2, 2),
    _HpicfPimMsgCountRegisterTransmit_Type()
)
hpicfPimMsgCountRegisterTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimMsgCountRegisterTransmit.setStatus("current")
_HpicfPimMsgCountRegisterInvalid_Type = Counter32
_HpicfPimMsgCountRegisterInvalid_Object = MibScalar
hpicfPimMsgCountRegisterInvalid = _HpicfPimMsgCountRegisterInvalid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 2, 3),
    _HpicfPimMsgCountRegisterInvalid_Type()
)
hpicfPimMsgCountRegisterInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimMsgCountRegisterInvalid.setStatus("current")
_HpicfPimMsgCountRegStopReceive_Type = Counter32
_HpicfPimMsgCountRegStopReceive_Object = MibScalar
hpicfPimMsgCountRegStopReceive = _HpicfPimMsgCountRegStopReceive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 2, 4),
    _HpicfPimMsgCountRegStopReceive_Type()
)
hpicfPimMsgCountRegStopReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimMsgCountRegStopReceive.setStatus("current")
_HpicfPimMsgCountRegStopTransmit_Type = Counter32
_HpicfPimMsgCountRegStopTransmit_Object = MibScalar
hpicfPimMsgCountRegStopTransmit = _HpicfPimMsgCountRegStopTransmit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 2, 5),
    _HpicfPimMsgCountRegStopTransmit_Type()
)
hpicfPimMsgCountRegStopTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimMsgCountRegStopTransmit.setStatus("current")
_HpicfPimMsgCountRegStopInvalid_Type = Counter32
_HpicfPimMsgCountRegStopInvalid_Object = MibScalar
hpicfPimMsgCountRegStopInvalid = _HpicfPimMsgCountRegStopInvalid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 2, 6),
    _HpicfPimMsgCountRegStopInvalid_Type()
)
hpicfPimMsgCountRegStopInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfPimMsgCountRegStopInvalid.setStatus("current")
_HpicfPimConformance_ObjectIdentity = ObjectIdentity
hpicfPimConformance = _HpicfPimConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2)
)
_HpicfPimGroups_ObjectIdentity = ObjectIdentity
hpicfPimGroups = _HpicfPimGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1)
)
_HpicfPimCompliances_ObjectIdentity = ObjectIdentity
hpicfPimCompliances = _HpicfPimCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 2)
)
pimInterfaceEntry.registerAugmentions(
    ("HP-ICF-PIM",
     "hpicfPimIfEntry")
)
hpicfPimIfEntry.setIndexNames(*pimInterfaceEntry.getIndexNames())
pimComponentEntry.registerAugmentions(
    ("HP-ICF-PIM",
     "hpicfPimComponentEntry")
)
hpicfPimComponentEntry.setIndexNames(*pimComponentEntry.getIndexNames())
ipMRouteEntry.registerAugmentions(
    ("HP-ICF-PIM",
     "hpicfPimMRouteEntry")
)
hpicfPimMRouteEntry.setIndexNames(*ipMRouteEntry.getIndexNames())
pimNeighborEntry.registerAugmentions(
    ("HP-ICF-PIM",
     "hpicfPimNeighborEntry")
)
hpicfPimNeighborEntry.setIndexNames(*pimNeighborEntry.getIndexNames())
pimRPSetEntry.registerAugmentions(
    ("HP-ICF-PIM",
     "hpicfPimRPSetEntry")
)
hpicfPimRPSetEntry.setIndexNames(*pimRPSetEntry.getIndexNames())

# Managed Objects groups

hpicfPimBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 2)
)
hpicfPimBaseGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimAdminStatus"),
        ("HP-ICF-PIM", "hpicfPimStateRefreshInterval"),
        ("HP-ICF-PIM", "hpicfPimSPTThreshold"),
        ("HP-ICF-PIM", "hpicfPimTrapControl"),
        ("HP-ICF-PIM", "hpicfPimRemoveConfig"))
)
if mibBuilder.loadTexts:
    hpicfPimBaseGroup.setStatus("current")

hpicfPimStaticRPSetMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 3)
)
hpicfPimStaticRPSetMappingGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimStaticRPSetOverride"),
        ("HP-ICF-PIM", "hpicfPimStaticRPSetRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfPimStaticRPSetMappingGroup.setStatus("current")

hpicfPimSparseIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 4)
)
hpicfPimSparseIfGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimIfAddress"),
        ("HP-ICF-PIM", "hpicfPimIfTrigHelloInterval"),
        ("HP-ICF-PIM", "hpicfPimIfHelloHoldtime"),
        ("HP-ICF-PIM", "hpicfPimIfLanPruneDelay"),
        ("HP-ICF-PIM", "hpicfPimIfPropagationDelay"),
        ("HP-ICF-PIM", "hpicfPimIfOverrideInterval"),
        ("HP-ICF-PIM", "hpicfPimIfGenerationID"),
        ("HP-ICF-PIM", "hpicfPimIfJoinPruneHoldtime"),
        ("HP-ICF-PIM", "hpicfPimIfLanDelayEnabled"),
        ("HP-ICF-PIM", "hpicfPimIfDRPriority"),
        ("HP-ICF-PIM", "hpicfPimIfNBRTimeout"))
)
if mibBuilder.loadTexts:
    hpicfPimSparseIfGroup.setStatus("current")

hpicfPimDenseIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 5)
)
hpicfPimDenseIfGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimIfAddress"),
        ("HP-ICF-PIM", "hpicfPimIfTrigHelloInterval"),
        ("HP-ICF-PIM", "hpicfPimIfHelloHoldtime"),
        ("HP-ICF-PIM", "hpicfPimIfLanPruneDelay"),
        ("HP-ICF-PIM", "hpicfPimIfPropagationDelay"),
        ("HP-ICF-PIM", "hpicfPimIfOverrideInterval"),
        ("HP-ICF-PIM", "hpicfPimIfGenerationID"),
        ("HP-ICF-PIM", "hpicfPimIfJoinPruneHoldtime"),
        ("HP-ICF-PIM", "hpicfPimIfGraftRetryInterval"),
        ("HP-ICF-PIM", "hpicfPimIfMaxGraftRetries"),
        ("HP-ICF-PIM", "hpicfPimIfSRTTLThreshold"),
        ("HP-ICF-PIM", "hpicfPimIfLanDelayEnabled"),
        ("HP-ICF-PIM", "hpicfPimIfSRCapable"),
        ("HP-ICF-PIM", "hpicfPimIfDRPriority"))
)
if mibBuilder.loadTexts:
    hpicfPimDenseIfGroup.setStatus("current")

hpicfPimComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 6)
)
hpicfPimComponentGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimComponentCBSRAdminStatus"),
        ("HP-ICF-PIM", "hpicfPimComponentCBSRAddress"),
        ("HP-ICF-PIM", "hpicfPimComponentCBSRPriority"),
        ("HP-ICF-PIM", "hpicfPimComponentCBSRHashMaskLength"),
        ("HP-ICF-PIM", "hpicfPimComponentCBSRMessageInterval"),
        ("HP-ICF-PIM", "hpicfPimComponentCRPPriority"),
        ("HP-ICF-PIM", "hpicfPimComponentCRPAdvInterval"),
        ("HP-ICF-PIM", "hpicfPimComponentBSRPriority"),
        ("HP-ICF-PIM", "hpicfPimComponentBSRHashMaskLength"),
        ("HP-ICF-PIM", "hpicfPimComponentBSRUpTime"),
        ("HP-ICF-PIM", "hpicfPimComponentBSRNextMessage"))
)
if mibBuilder.loadTexts:
    hpicfPimComponentGroup.setStatus("current")

hpicfPimStaticRpfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 7)
)
hpicfPimStaticRpfGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimStaticRpfOverrideState"),
        ("HP-ICF-PIM", "hpicfPimStaticRpfRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfPimStaticRpfGroup.setStatus("current")

hpicfPimInterfaceExtensionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 8)
)
hpicfPimInterfaceExtensionsGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimVersion"),
        ("HP-ICF-PIM", "hpicfPimIfNBRCount"),
        ("HP-ICF-PIM", "hpicfPimIfNegotiatedPropagationDelay"),
        ("HP-ICF-PIM", "hpicfPimIfNegotiatedOverrideInterval"),
        ("HP-ICF-PIM", "hpicfPimIfAssertHoldInterval"),
        ("HP-ICF-PIM", "hpicfPimIfNumRoutersNotUsingDRPriority"),
        ("HP-ICF-PIM", "hpicfPimIfNumRoutersNotUsingLanDelay"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountGraftReceive"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountGraftTransmit"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountGraftInvalid"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountGraftAckReceive"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountGraftAckTransmit"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountGraftAckInvalid"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountSRReceive"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountSRTransmit"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountSRInvalid"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountBSRReceive"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountBSRTransmit"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountBSRInvalid"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountCRPReceive"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountCRPTransmit"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountCRPInvalid"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountJPReceive"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountJPTransmit"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountJPInvalid"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountAssertReceive"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountAssertTransmit"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountAssertInvalid"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountHelloReceive"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountHelloTransmit"),
        ("HP-ICF-PIM", "hpicfPimIfMsgCountHelloInvalid"))
)
if mibBuilder.loadTexts:
    hpicfPimInterfaceExtensionsGroup.setStatus("current")

hpicfPimStaticRpfExtensionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 9)
)
hpicfPimStaticRpfExtensionsGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimStaticRpfIfIndex"),
        ("HP-ICF-PIM", "hpicfPimStaticRpfNeighborAddressType"),
        ("HP-ICF-PIM", "hpicfPimStaticRpfNeighborAddress"),
        ("HP-ICF-PIM", "hpicfPimNumStaticRpfEntries"))
)
if mibBuilder.loadTexts:
    hpicfPimStaticRpfExtensionsGroup.setStatus("current")

hpicfPimNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 10)
)
hpicfPimNeighborGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimNeighborDRPriority"),
        ("HP-ICF-PIM", "hpicfPimNeighborGenerationIDValue"),
        ("HP-ICF-PIM", "hpicfPimNeighborHoldtime"),
        ("HP-ICF-PIM", "hpicfPimNeighborPropagationDelay"),
        ("HP-ICF-PIM", "hpicfPimNeighborOverrideInterval"),
        ("HP-ICF-PIM", "hpicfPimNeighborStateRefreshInterval"))
)
if mibBuilder.loadTexts:
    hpicfPimNeighborGroup.setStatus("current")

hpicfPimMRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 11)
)
hpicfPimMRouteGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimSendRegStop"),
        ("HP-ICF-PIM", "hpicfPimSGSourceIsActive"),
        ("HP-ICF-PIM", "hpicfPimOutgoingRegisterIfAvailable"),
        ("HP-ICF-PIM", "hpicfPimEntryAddSuccess"),
        ("HP-ICF-PIM", "hpicfPimNumOutgoingInterfaces"),
        ("HP-ICF-PIM", "hpicfPimDirectlyConnectedSource"),
        ("HP-ICF-PIM", "hpicfPimNeighborSearchFailure"),
        ("HP-ICF-PIM", "hpicfPimRPTreePruneSent"),
        ("HP-ICF-PIM", "hpicfPimOnSPTree"),
        ("HP-ICF-PIM", "hpicfPimRPToSPTreeSwitching"),
        ("HP-ICF-PIM", "hpicfPimWildcardEntry"),
        ("HP-ICF-PIM", "hpicfPimRPFPrimeNeighborAddressType"),
        ("HP-ICF-PIM", "hpicfPimRPFPrimeNeighborAddress"),
        ("HP-ICF-PIM", "hpicfPimNumDownstreams"))
)
if mibBuilder.loadTexts:
    hpicfPimMRouteGroup.setStatus("current")

hpicfPimUcastRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 12)
)
hpicfPimUcastRouteGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimUcastRouteIfIndex"),
        ("HP-ICF-PIM", "hpicfPimUcastRouteUpstreamNbrType"),
        ("HP-ICF-PIM", "hpicfPimUcastRouteUpstreamNbr"),
        ("HP-ICF-PIM", "hpicfPimUcastRouteProtocol"))
)
if mibBuilder.loadTexts:
    hpicfPimUcastRouteGroup.setStatus("current")

hpicfPimUnackGraftsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 13)
)
hpicfPimUnackGraftsGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimUnackGraftAge"),
        ("HP-ICF-PIM", "hpicfPimUnackGraftRetransIn"))
)
if mibBuilder.loadTexts:
    hpicfPimUnackGraftsGroup.setStatus("current")

hpicfPimGlobalCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 14)
)
hpicfPimGlobalCounterGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimMsgCountRegisterReceive"),
        ("HP-ICF-PIM", "hpicfPimMsgCountRegisterTransmit"),
        ("HP-ICF-PIM", "hpicfPimMsgCountRegisterInvalid"),
        ("HP-ICF-PIM", "hpicfPimMsgCountRegStopReceive"),
        ("HP-ICF-PIM", "hpicfPimMsgCountRegStopTransmit"),
        ("HP-ICF-PIM", "hpicfPimMsgCountRegStopInvalid"),
        ("HP-ICF-PIM", "hpicfPimStarGEntries"),
        ("HP-ICF-PIM", "hpicfPimSGEntries"),
        ("HP-ICF-PIM", "hpicfPimTotalNeighborCount"))
)
if mibBuilder.loadTexts:
    hpicfPimGlobalCounterGroup.setStatus("current")

hpicfPimRPSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 15)
)
hpicfPimRPSetGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimRPSetPriority"),
        ("HP-ICF-PIM", "hpicfPimRPSetUptime"),
        ("HP-ICF-PIM", "hpicfPimComponentCRPAdvTimer"))
)
if mibBuilder.loadTexts:
    hpicfPimRPSetGroup.setStatus("current")

hpicfPimJoinPruneGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 17)
)
hpicfPimJoinPruneGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimJoinPruneNeighborAddressType"),
        ("HP-ICF-PIM", "hpicfPimJoinPruneNeighborAddress"),
        ("HP-ICF-PIM", "hpicfPimJoinPruneExpiryTime"))
)
if mibBuilder.loadTexts:
    hpicfPimJoinPruneGroup.setStatus("current")


# Notification objects

hpicfPimHardMRTFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 0, 1)
)
if mibBuilder.loadTexts:
    hpicfPimHardMRTFull.setStatus(
        "current"
    )

hpicfPimSoftMRTFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 1, 0, 2)
)
if mibBuilder.loadTexts:
    hpicfPimSoftMRTFull.setStatus(
        "current"
    )


# Notifications groups

hpicfPimNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 1, 1)
)
hpicfPimNotificationGroup.setObjects(
      *(("HP-ICF-PIM", "hpicfPimHardMRTFull"),
        ("HP-ICF-PIM", "hpicfPimSoftMRTFull"))
)
if mibBuilder.loadTexts:
    hpicfPimNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfPimSparseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfPimSparseMIBCompliance.setStatus(
        "current"
    )

hpicfPimDenseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfPimDenseMIBCompliance.setStatus(
        "current"
    )

hpicfPimNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfPimNotificationCompliance.setStatus(
        "current"
    )

hpicfPimUcastRoutingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 2, 4)
)
if mibBuilder.loadTexts:
    hpicfPimUcastRoutingCompliance.setStatus(
        "current"
    )

hpicfPimMcastRoutingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 2, 5)
)
if mibBuilder.loadTexts:
    hpicfPimMcastRoutingCompliance.setStatus(
        "current"
    )

hpicfPimInterfaceInfoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 2, 6)
)
if mibBuilder.loadTexts:
    hpicfPimInterfaceInfoCompliance.setStatus(
        "current"
    )

hpicfPimProtoMessageCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 2, 7)
)
if mibBuilder.loadTexts:
    hpicfPimProtoMessageCompliance.setStatus(
        "current"
    )

hpicfPimGlobalCountersCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 2, 8)
)
if mibBuilder.loadTexts:
    hpicfPimGlobalCountersCompliance.setStatus(
        "current"
    )

hpicfPimRPSetExtensionsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 20, 2, 2, 9)
)
if mibBuilder.loadTexts:
    hpicfPimRPSetExtensionsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-PIM",
    **{"hpicfPimMIB": hpicfPimMIB,
       "hpicfPimObjects": hpicfPimObjects,
       "hpicfPimTraps": hpicfPimTraps,
       "hpicfPimHardMRTFull": hpicfPimHardMRTFull,
       "hpicfPimSoftMRTFull": hpicfPimSoftMRTFull,
       "hpicfPim": hpicfPim,
       "hpicfPimAdminStatus": hpicfPimAdminStatus,
       "hpicfPimStateRefreshInterval": hpicfPimStateRefreshInterval,
       "hpicfPimSPTThreshold": hpicfPimSPTThreshold,
       "hpicfPimTrapControl": hpicfPimTrapControl,
       "hpicfPimStaticRPSetTable": hpicfPimStaticRPSetTable,
       "hpicfPimStaticRPSetEntry": hpicfPimStaticRPSetEntry,
       "hpicfPimStaticRPSetGroupAddress": hpicfPimStaticRPSetGroupAddress,
       "hpicfPimStaticRPSetGroupMask": hpicfPimStaticRPSetGroupMask,
       "hpicfPimStaticRPSetAddress": hpicfPimStaticRPSetAddress,
       "hpicfPimStaticRPSetOverride": hpicfPimStaticRPSetOverride,
       "hpicfPimStaticRPSetRowStatus": hpicfPimStaticRPSetRowStatus,
       "hpicfPimIfTable": hpicfPimIfTable,
       "hpicfPimIfEntry": hpicfPimIfEntry,
       "hpicfPimIfAddress": hpicfPimIfAddress,
       "hpicfPimIfTrigHelloInterval": hpicfPimIfTrigHelloInterval,
       "hpicfPimIfHelloHoldtime": hpicfPimIfHelloHoldtime,
       "hpicfPimIfLanPruneDelay": hpicfPimIfLanPruneDelay,
       "hpicfPimIfPropagationDelay": hpicfPimIfPropagationDelay,
       "hpicfPimIfOverrideInterval": hpicfPimIfOverrideInterval,
       "hpicfPimIfGenerationID": hpicfPimIfGenerationID,
       "hpicfPimIfJoinPruneHoldtime": hpicfPimIfJoinPruneHoldtime,
       "hpicfPimIfGraftRetryInterval": hpicfPimIfGraftRetryInterval,
       "hpicfPimIfMaxGraftRetries": hpicfPimIfMaxGraftRetries,
       "hpicfPimIfSRTTLThreshold": hpicfPimIfSRTTLThreshold,
       "hpicfPimIfLanDelayEnabled": hpicfPimIfLanDelayEnabled,
       "hpicfPimIfSRCapable": hpicfPimIfSRCapable,
       "hpicfPimIfDRPriority": hpicfPimIfDRPriority,
       "hpicfPimIfNBRTimeout": hpicfPimIfNBRTimeout,
       "hpicfPimIfNBRCount": hpicfPimIfNBRCount,
       "hpicfPimIfNegotiatedPropagationDelay": hpicfPimIfNegotiatedPropagationDelay,
       "hpicfPimIfNegotiatedOverrideInterval": hpicfPimIfNegotiatedOverrideInterval,
       "hpicfPimIfAssertHoldInterval": hpicfPimIfAssertHoldInterval,
       "hpicfPimIfNumRoutersNotUsingDRPriority": hpicfPimIfNumRoutersNotUsingDRPriority,
       "hpicfPimIfNumRoutersNotUsingLanDelay": hpicfPimIfNumRoutersNotUsingLanDelay,
       "hpicfPimComponentTable": hpicfPimComponentTable,
       "hpicfPimComponentEntry": hpicfPimComponentEntry,
       "hpicfPimComponentCBSRAdminStatus": hpicfPimComponentCBSRAdminStatus,
       "hpicfPimComponentCBSRAddress": hpicfPimComponentCBSRAddress,
       "hpicfPimComponentCBSRPriority": hpicfPimComponentCBSRPriority,
       "hpicfPimComponentCBSRHashMaskLength": hpicfPimComponentCBSRHashMaskLength,
       "hpicfPimComponentCBSRMessageInterval": hpicfPimComponentCBSRMessageInterval,
       "hpicfPimComponentCRPPriority": hpicfPimComponentCRPPriority,
       "hpicfPimComponentCRPAdvInterval": hpicfPimComponentCRPAdvInterval,
       "hpicfPimComponentBSRPriority": hpicfPimComponentBSRPriority,
       "hpicfPimComponentBSRHashMaskLength": hpicfPimComponentBSRHashMaskLength,
       "hpicfPimComponentBSRUpTime": hpicfPimComponentBSRUpTime,
       "hpicfPimComponentBSRNextMessage": hpicfPimComponentBSRNextMessage,
       "hpicfPimComponentCRPAdvTimer": hpicfPimComponentCRPAdvTimer,
       "hpicfPimRemoveConfig": hpicfPimRemoveConfig,
       "hpicfPimStaticRpfTable": hpicfPimStaticRpfTable,
       "hpicfPimStaticRpfEntry": hpicfPimStaticRpfEntry,
       "hpicfPimStaticRpfSourceAddressType": hpicfPimStaticRpfSourceAddressType,
       "hpicfPimStaticRpfSourceAddress": hpicfPimStaticRpfSourceAddress,
       "hpicfPimStaticRpfSourcePrefixLength": hpicfPimStaticRpfSourcePrefixLength,
       "hpicfPimStaticRpfAddressType": hpicfPimStaticRpfAddressType,
       "hpicfPimStaticRpfAddress": hpicfPimStaticRpfAddress,
       "hpicfPimStaticRpfRowStatus": hpicfPimStaticRpfRowStatus,
       "hpicfPimStaticRpfOverrideState": hpicfPimStaticRpfOverrideState,
       "hpicfPimStaticRpfIfIndex": hpicfPimStaticRpfIfIndex,
       "hpicfPimStaticRpfNeighborAddressType": hpicfPimStaticRpfNeighborAddressType,
       "hpicfPimStaticRpfNeighborAddress": hpicfPimStaticRpfNeighborAddress,
       "hpicfPimNumStaticRpfEntries": hpicfPimNumStaticRpfEntries,
       "hpicfPimVersion": hpicfPimVersion,
       "hpicfPimStarGEntries": hpicfPimStarGEntries,
       "hpicfPimSGEntries": hpicfPimSGEntries,
       "hpicfPimMRouteTable": hpicfPimMRouteTable,
       "hpicfPimMRouteEntry": hpicfPimMRouteEntry,
       "hpicfPimSendRegStop": hpicfPimSendRegStop,
       "hpicfPimSGSourceIsActive": hpicfPimSGSourceIsActive,
       "hpicfPimOutgoingRegisterIfAvailable": hpicfPimOutgoingRegisterIfAvailable,
       "hpicfPimEntryAddSuccess": hpicfPimEntryAddSuccess,
       "hpicfPimNumOutgoingInterfaces": hpicfPimNumOutgoingInterfaces,
       "hpicfPimDirectlyConnectedSource": hpicfPimDirectlyConnectedSource,
       "hpicfPimNeighborSearchFailure": hpicfPimNeighborSearchFailure,
       "hpicfPimRPTreePruneSent": hpicfPimRPTreePruneSent,
       "hpicfPimOnSPTree": hpicfPimOnSPTree,
       "hpicfPimRPToSPTreeSwitching": hpicfPimRPToSPTreeSwitching,
       "hpicfPimWildcardEntry": hpicfPimWildcardEntry,
       "hpicfPimRPFPrimeNeighborAddressType": hpicfPimRPFPrimeNeighborAddressType,
       "hpicfPimRPFPrimeNeighborAddress": hpicfPimRPFPrimeNeighborAddress,
       "hpicfPimNumDownstreams": hpicfPimNumDownstreams,
       "hpicfPimTotalNeighborCount": hpicfPimTotalNeighborCount,
       "hpicfPimNeighborTable": hpicfPimNeighborTable,
       "hpicfPimNeighborEntry": hpicfPimNeighborEntry,
       "hpicfPimNeighborDRPriority": hpicfPimNeighborDRPriority,
       "hpicfPimNeighborGenerationIDValue": hpicfPimNeighborGenerationIDValue,
       "hpicfPimNeighborHoldtime": hpicfPimNeighborHoldtime,
       "hpicfPimNeighborPropagationDelay": hpicfPimNeighborPropagationDelay,
       "hpicfPimNeighborOverrideInterval": hpicfPimNeighborOverrideInterval,
       "hpicfPimNeighborStateRefreshInterval": hpicfPimNeighborStateRefreshInterval,
       "hpicfPimUcastRouteTable": hpicfPimUcastRouteTable,
       "hpicfPimUcastRouteEntry": hpicfPimUcastRouteEntry,
       "hpicfPimUcastRouteAddressType": hpicfPimUcastRouteAddressType,
       "hpicfPimUcastRouteAddress": hpicfPimUcastRouteAddress,
       "hpicfPimUcastRoutePrefix": hpicfPimUcastRoutePrefix,
       "hpicfPimUcastRouteIfIndex": hpicfPimUcastRouteIfIndex,
       "hpicfPimUcastRouteUpstreamNbrType": hpicfPimUcastRouteUpstreamNbrType,
       "hpicfPimUcastRouteUpstreamNbr": hpicfPimUcastRouteUpstreamNbr,
       "hpicfPimUcastRouteProtocol": hpicfPimUcastRouteProtocol,
       "hpicfPimJoinPruneTable": hpicfPimJoinPruneTable,
       "hpicfPimJoinPruneEntry": hpicfPimJoinPruneEntry,
       "hpicfPimJoinPruneInterface": hpicfPimJoinPruneInterface,
       "hpicfPimJoinPruneInterfaceState": hpicfPimJoinPruneInterfaceState,
       "hpicfPimJoinPruneSourceType": hpicfPimJoinPruneSourceType,
       "hpicfPimJoinPruneSourceAddress": hpicfPimJoinPruneSourceAddress,
       "hpicfPimJoinPruneGroupType": hpicfPimJoinPruneGroupType,
       "hpicfPimJoinPruneGroupAddress": hpicfPimJoinPruneGroupAddress,
       "hpicfPimJoinPruneNeighborAddressType": hpicfPimJoinPruneNeighborAddressType,
       "hpicfPimJoinPruneNeighborAddress": hpicfPimJoinPruneNeighborAddress,
       "hpicfPimJoinPruneExpiryTime": hpicfPimJoinPruneExpiryTime,
       "hpicfPimRPSetTable": hpicfPimRPSetTable,
       "hpicfPimRPSetEntry": hpicfPimRPSetEntry,
       "hpicfPimRPSetPriority": hpicfPimRPSetPriority,
       "hpicfPimRPSetUptime": hpicfPimRPSetUptime,
       "hpicfPimIfMessageCounterTable": hpicfPimIfMessageCounterTable,
       "hpicfPimIfMessageCounterEntry": hpicfPimIfMessageCounterEntry,
       "hpicfPimIfMsgCountAssertReceive": hpicfPimIfMsgCountAssertReceive,
       "hpicfPimIfMsgCountAssertTransmit": hpicfPimIfMsgCountAssertTransmit,
       "hpicfPimIfMsgCountAssertInvalid": hpicfPimIfMsgCountAssertInvalid,
       "hpicfPimIfMsgCountGraftReceive": hpicfPimIfMsgCountGraftReceive,
       "hpicfPimIfMsgCountGraftTransmit": hpicfPimIfMsgCountGraftTransmit,
       "hpicfPimIfMsgCountGraftInvalid": hpicfPimIfMsgCountGraftInvalid,
       "hpicfPimIfMsgCountGraftAckReceive": hpicfPimIfMsgCountGraftAckReceive,
       "hpicfPimIfMsgCountGraftAckTransmit": hpicfPimIfMsgCountGraftAckTransmit,
       "hpicfPimIfMsgCountGraftAckInvalid": hpicfPimIfMsgCountGraftAckInvalid,
       "hpicfPimIfMsgCountHelloReceive": hpicfPimIfMsgCountHelloReceive,
       "hpicfPimIfMsgCountHelloTransmit": hpicfPimIfMsgCountHelloTransmit,
       "hpicfPimIfMsgCountHelloInvalid": hpicfPimIfMsgCountHelloInvalid,
       "hpicfPimIfMsgCountJPReceive": hpicfPimIfMsgCountJPReceive,
       "hpicfPimIfMsgCountJPTransmit": hpicfPimIfMsgCountJPTransmit,
       "hpicfPimIfMsgCountJPInvalid": hpicfPimIfMsgCountJPInvalid,
       "hpicfPimIfMsgCountSRReceive": hpicfPimIfMsgCountSRReceive,
       "hpicfPimIfMsgCountSRTransmit": hpicfPimIfMsgCountSRTransmit,
       "hpicfPimIfMsgCountSRInvalid": hpicfPimIfMsgCountSRInvalid,
       "hpicfPimIfMsgCountBSRReceive": hpicfPimIfMsgCountBSRReceive,
       "hpicfPimIfMsgCountBSRTransmit": hpicfPimIfMsgCountBSRTransmit,
       "hpicfPimIfMsgCountBSRInvalid": hpicfPimIfMsgCountBSRInvalid,
       "hpicfPimIfMsgCountCRPReceive": hpicfPimIfMsgCountCRPReceive,
       "hpicfPimIfMsgCountCRPTransmit": hpicfPimIfMsgCountCRPTransmit,
       "hpicfPimIfMsgCountCRPInvalid": hpicfPimIfMsgCountCRPInvalid,
       "hpicfPimUnackGraftsTable": hpicfPimUnackGraftsTable,
       "hpicfPimUnackGraftsEntry": hpicfPimUnackGraftsEntry,
       "hpicfPimUnackGraftSourceType": hpicfPimUnackGraftSourceType,
       "hpicfPimUnackGraftSource": hpicfPimUnackGraftSource,
       "hpicfPimUnackGraftGroupType": hpicfPimUnackGraftGroupType,
       "hpicfPimUnackGraftGroup": hpicfPimUnackGraftGroup,
       "hpicfPimUnackGraftAge": hpicfPimUnackGraftAge,
       "hpicfPimUnackGraftRetransIn": hpicfPimUnackGraftRetransIn,
       "hpicfPimScalars": hpicfPimScalars,
       "hpicfPimMsgCountRegisterReceive": hpicfPimMsgCountRegisterReceive,
       "hpicfPimMsgCountRegisterTransmit": hpicfPimMsgCountRegisterTransmit,
       "hpicfPimMsgCountRegisterInvalid": hpicfPimMsgCountRegisterInvalid,
       "hpicfPimMsgCountRegStopReceive": hpicfPimMsgCountRegStopReceive,
       "hpicfPimMsgCountRegStopTransmit": hpicfPimMsgCountRegStopTransmit,
       "hpicfPimMsgCountRegStopInvalid": hpicfPimMsgCountRegStopInvalid,
       "hpicfPimConformance": hpicfPimConformance,
       "hpicfPimGroups": hpicfPimGroups,
       "hpicfPimNotificationGroup": hpicfPimNotificationGroup,
       "hpicfPimBaseGroup": hpicfPimBaseGroup,
       "hpicfPimStaticRPSetMappingGroup": hpicfPimStaticRPSetMappingGroup,
       "hpicfPimSparseIfGroup": hpicfPimSparseIfGroup,
       "hpicfPimDenseIfGroup": hpicfPimDenseIfGroup,
       "hpicfPimComponentGroup": hpicfPimComponentGroup,
       "hpicfPimStaticRpfGroup": hpicfPimStaticRpfGroup,
       "hpicfPimInterfaceExtensionsGroup": hpicfPimInterfaceExtensionsGroup,
       "hpicfPimStaticRpfExtensionsGroup": hpicfPimStaticRpfExtensionsGroup,
       "hpicfPimNeighborGroup": hpicfPimNeighborGroup,
       "hpicfPimMRouteGroup": hpicfPimMRouteGroup,
       "hpicfPimUcastRouteGroup": hpicfPimUcastRouteGroup,
       "hpicfPimUnackGraftsGroup": hpicfPimUnackGraftsGroup,
       "hpicfPimGlobalCounterGroup": hpicfPimGlobalCounterGroup,
       "hpicfPimRPSetGroup": hpicfPimRPSetGroup,
       "hpicfPimJoinPruneGroup": hpicfPimJoinPruneGroup,
       "hpicfPimCompliances": hpicfPimCompliances,
       "hpicfPimSparseMIBCompliance": hpicfPimSparseMIBCompliance,
       "hpicfPimDenseMIBCompliance": hpicfPimDenseMIBCompliance,
       "hpicfPimNotificationCompliance": hpicfPimNotificationCompliance,
       "hpicfPimUcastRoutingCompliance": hpicfPimUcastRoutingCompliance,
       "hpicfPimMcastRoutingCompliance": hpicfPimMcastRoutingCompliance,
       "hpicfPimInterfaceInfoCompliance": hpicfPimInterfaceInfoCompliance,
       "hpicfPimProtoMessageCompliance": hpicfPimProtoMessageCompliance,
       "hpicfPimGlobalCountersCompliance": hpicfPimGlobalCountersCompliance,
       "hpicfPimRPSetExtensionsCompliance": hpicfPimRPSetExtensionsCompliance}
)
