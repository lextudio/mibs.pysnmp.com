# SNMP MIB module (ESWITCH-MIB-V3-0) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ESWITCH-MIB-V3-0
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:53 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_DecMIBextension_ObjectIdentity = ObjectIdentity
decMIBextension = _DecMIBextension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_DecHub900_ObjectIdentity = ObjectIdentity
decHub900 = _DecHub900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11)
)
_ESwitch_ObjectIdentity = ObjectIdentity
eSwitch = _ESwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7)
)
_ESwitchIf_ObjectIdentity = ObjectIdentity
eSwitchIf = _ESwitchIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 1)
)
_ESwitchIfTable_Object = MibTable
eSwitchIfTable = _ESwitchIfTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 1, 1)
)
if mibBuilder.loadTexts:
    eSwitchIfTable.setStatus("mandatory")
_ESwitchIfEntry_Object = MibTableRow
eSwitchIfEntry = _ESwitchIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 1, 1, 1)
)
eSwitchIfEntry.setIndexNames(
    (0, "ESWITCH-MIB-V3-0", "eSwitchIfIndex"),
)
if mibBuilder.loadTexts:
    eSwitchIfEntry.setStatus("mandatory")


class _ESwitchIfIndex_Type(Integer32):
    """Custom type eSwitchIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ESwitchIfIndex_Type.__name__ = "Integer32"
_ESwitchIfIndex_Object = MibTableColumn
eSwitchIfIndex = _ESwitchIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 1, 1, 1, 1),
    _ESwitchIfIndex_Type()
)
eSwitchIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchIfIndex.setStatus("mandatory")


class _ESwitchIfPresent_Type(Integer32):
    """Custom type eSwitchIfPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 2),
          ("present", 1))
    )


_ESwitchIfPresent_Type.__name__ = "Integer32"
_ESwitchIfPresent_Object = MibTableColumn
eSwitchIfPresent = _ESwitchIfPresent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 1, 1, 1, 2),
    _ESwitchIfPresent_Type()
)
eSwitchIfPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchIfPresent.setStatus("mandatory")
_ESwitchPort_ObjectIdentity = ObjectIdentity
eSwitchPort = _ESwitchPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 2)
)
_ESwitchPortTable_Object = MibTable
eSwitchPortTable = _ESwitchPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 2, 1)
)
if mibBuilder.loadTexts:
    eSwitchPortTable.setStatus("mandatory")
_ESwitchPortEntry_Object = MibTableRow
eSwitchPortEntry = _ESwitchPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 2, 1, 1)
)
eSwitchPortEntry.setIndexNames(
    (0, "ESWITCH-MIB-V3-0", "eSwitchPortIndex"),
)
if mibBuilder.loadTexts:
    eSwitchPortEntry.setStatus("mandatory")


class _ESwitchPortIndex_Type(Integer32):
    """Custom type eSwitchPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ESwitchPortIndex_Type.__name__ = "Integer32"
_ESwitchPortIndex_Object = MibTableColumn
eSwitchPortIndex = _ESwitchPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 2, 1, 1, 1),
    _ESwitchPortIndex_Type()
)
eSwitchPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchPortIndex.setStatus("mandatory")


class _ESwitchPortFailed_Type(Integer32):
    """Custom type eSwitchPortFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("not-failed", 3),
          ("unknown", 1))
    )


_ESwitchPortFailed_Type.__name__ = "Integer32"
_ESwitchPortFailed_Object = MibTableColumn
eSwitchPortFailed = _ESwitchPortFailed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 2, 1, 1, 2),
    _ESwitchPortFailed_Type()
)
eSwitchPortFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchPortFailed.setStatus("mandatory")


class _ESwitchPortStatus_Type(Integer32):
    """Custom type eSwitchPortStatus based on Integer32"""
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
        *(("connected", 2),
          ("disconnected", 3),
          ("isolated", 5),
          ("shutdown", 4),
          ("undefined", 1))
    )


_ESwitchPortStatus_Type.__name__ = "Integer32"
_ESwitchPortStatus_Object = MibTableColumn
eSwitchPortStatus = _ESwitchPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 2, 1, 1, 3),
    _ESwitchPortStatus_Type()
)
eSwitchPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchPortStatus.setStatus("mandatory")


class _ESwitchPortShutDownReason_Type(Integer32):
    """Custom type eSwitchPortShutDownReason based on Integer32"""
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
        *(("internal", 5),
          ("mgmt", 3),
          ("none", 1),
          ("other", 2),
          ("security", 4))
    )


_ESwitchPortShutDownReason_Type.__name__ = "Integer32"
_ESwitchPortShutDownReason_Object = MibTableColumn
eSwitchPortShutDownReason = _ESwitchPortShutDownReason_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 2, 1, 1, 4),
    _ESwitchPortShutDownReason_Type()
)
eSwitchPortShutDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchPortShutDownReason.setStatus("mandatory")


class _ESwitchPortSwitchingMode_Type(Integer32):
    """Custom type eSwitchPortSwitchingMode based on Integer32"""
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
        *(("backbone", 3),
          ("manual", 4),
          ("standard", 1),
          ("workgroup", 2))
    )


_ESwitchPortSwitchingMode_Type.__name__ = "Integer32"
_ESwitchPortSwitchingMode_Object = MibTableColumn
eSwitchPortSwitchingMode = _ESwitchPortSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 2, 1, 1, 5),
    _ESwitchPortSwitchingMode_Type()
)
eSwitchPortSwitchingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchPortSwitchingMode.setStatus("mandatory")
_ESwitchFdb_ObjectIdentity = ObjectIdentity
eSwitchFdb = _ESwitchFdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 3)
)
_ESwitchAddrFdb_ObjectIdentity = ObjectIdentity
eSwitchAddrFdb = _ESwitchAddrFdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 3, 1)
)
_ESwitchAddrFdbMaxEntries_Type = Integer32
_ESwitchAddrFdbMaxEntries_Object = MibScalar
eSwitchAddrFdbMaxEntries = _ESwitchAddrFdbMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 3, 1, 1),
    _ESwitchAddrFdbMaxEntries_Type()
)
eSwitchAddrFdbMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchAddrFdbMaxEntries.setStatus("mandatory")
_ESwitchAddrFdbMaxStaticEntries_Type = Integer32
_ESwitchAddrFdbMaxStaticEntries_Object = MibScalar
eSwitchAddrFdbMaxStaticEntries = _ESwitchAddrFdbMaxStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 3, 1, 2),
    _ESwitchAddrFdbMaxStaticEntries_Type()
)
eSwitchAddrFdbMaxStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchAddrFdbMaxStaticEntries.setStatus("mandatory")
_ESwitchAddrFdbMaxNVStaticEntries_Type = Integer32
_ESwitchAddrFdbMaxNVStaticEntries_Object = MibScalar
eSwitchAddrFdbMaxNVStaticEntries = _ESwitchAddrFdbMaxNVStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 3, 1, 3),
    _ESwitchAddrFdbMaxNVStaticEntries_Type()
)
eSwitchAddrFdbMaxNVStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchAddrFdbMaxNVStaticEntries.setStatus("mandatory")
_ESwitchAddrFdbDynamicEntries_Type = Integer32
_ESwitchAddrFdbDynamicEntries_Object = MibScalar
eSwitchAddrFdbDynamicEntries = _ESwitchAddrFdbDynamicEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 3, 1, 4),
    _ESwitchAddrFdbDynamicEntries_Type()
)
eSwitchAddrFdbDynamicEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchAddrFdbDynamicEntries.setStatus("mandatory")
_ESwitchAddrFdbStaticEntries_Type = Integer32
_ESwitchAddrFdbStaticEntries_Object = MibScalar
eSwitchAddrFdbStaticEntries = _ESwitchAddrFdbStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 3, 1, 5),
    _ESwitchAddrFdbStaticEntries_Type()
)
eSwitchAddrFdbStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchAddrFdbStaticEntries.setStatus("mandatory")
_ESwitchAddrFdbNVStaticEntries_Type = Integer32
_ESwitchAddrFdbNVStaticEntries_Object = MibScalar
eSwitchAddrFdbNVStaticEntries = _ESwitchAddrFdbNVStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 3, 1, 6),
    _ESwitchAddrFdbNVStaticEntries_Type()
)
eSwitchAddrFdbNVStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchAddrFdbNVStaticEntries.setStatus("mandatory")


class _ESwitchAddrFdbPurgeStaticEntries_Type(Integer32):
    """Custom type eSwitchAddrFdbPurgeStaticEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("purge", 1)
    )


_ESwitchAddrFdbPurgeStaticEntries_Type.__name__ = "Integer32"
_ESwitchAddrFdbPurgeStaticEntries_Object = MibScalar
eSwitchAddrFdbPurgeStaticEntries = _ESwitchAddrFdbPurgeStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 3, 1, 7),
    _ESwitchAddrFdbPurgeStaticEntries_Type()
)
eSwitchAddrFdbPurgeStaticEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchAddrFdbPurgeStaticEntries.setStatus("mandatory")
_ESwitchStorm_ObjectIdentity = ObjectIdentity
eSwitchStorm = _ESwitchStorm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4)
)


class _ESwitchStormFrameTypeRegulated_Type(Integer32):
    """Custom type eSwitchStormFrameTypeRegulated based on Integer32"""
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
        *(("broadcast", 2),
          ("broadcastAndMulticast", 4),
          ("multicast", 3),
          ("none", 1))
    )


_ESwitchStormFrameTypeRegulated_Type.__name__ = "Integer32"
_ESwitchStormFrameTypeRegulated_Object = MibScalar
eSwitchStormFrameTypeRegulated = _ESwitchStormFrameTypeRegulated_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 1),
    _ESwitchStormFrameTypeRegulated_Type()
)
eSwitchStormFrameTypeRegulated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchStormFrameTypeRegulated.setStatus("mandatory")


class _ESwitchStormPollingInterval_Type(Integer32):
    """Custom type eSwitchStormPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 360000),
    )


_ESwitchStormPollingInterval_Type.__name__ = "Integer32"
_ESwitchStormPollingInterval_Object = MibScalar
eSwitchStormPollingInterval = _ESwitchStormPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 2),
    _ESwitchStormPollingInterval_Type()
)
eSwitchStormPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchStormPollingInterval.setStatus("mandatory")
_ESwitchStormRateLimit_Type = Integer32
_ESwitchStormRateLimit_Object = MibScalar
eSwitchStormRateLimit = _ESwitchStormRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 3),
    _ESwitchStormRateLimit_Type()
)
eSwitchStormRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchStormRateLimit.setStatus("mandatory")


class _ESwitchStormControlAction_Type(Integer32):
    """Custom type eSwitchStormControlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frame-suppression", 1),
          ("port-isolation", 2))
    )


_ESwitchStormControlAction_Type.__name__ = "Integer32"
_ESwitchStormControlAction_Object = MibScalar
eSwitchStormControlAction = _ESwitchStormControlAction_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 4),
    _ESwitchStormControlAction_Type()
)
eSwitchStormControlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchStormControlAction.setStatus("mandatory")


class _ESwitchStormResumptionPolicy_Type(Integer32):
    """Custom type eSwitchStormResumptionPolicy based on Integer32"""
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
        *(("auto-interval", 2),
          ("continue-control", 1),
          ("rate-limit", 3),
          ("responsive-rate-limit", 4))
    )


_ESwitchStormResumptionPolicy_Type.__name__ = "Integer32"
_ESwitchStormResumptionPolicy_Object = MibScalar
eSwitchStormResumptionPolicy = _ESwitchStormResumptionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 5),
    _ESwitchStormResumptionPolicy_Type()
)
eSwitchStormResumptionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchStormResumptionPolicy.setStatus("mandatory")
_ESwitchStormAutoInterval_Type = Integer32
_ESwitchStormAutoInterval_Object = MibScalar
eSwitchStormAutoInterval = _ESwitchStormAutoInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 6),
    _ESwitchStormAutoInterval_Type()
)
eSwitchStormAutoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchStormAutoInterval.setStatus("mandatory")
_ESwitchStormFramesLost_Type = Counter32
_ESwitchStormFramesLost_Object = MibScalar
eSwitchStormFramesLost = _ESwitchStormFramesLost_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 7),
    _ESwitchStormFramesLost_Type()
)
eSwitchStormFramesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchStormFramesLost.setStatus("mandatory")
_ESwitchStormActionsInitiated_Type = Counter32
_ESwitchStormActionsInitiated_Object = MibScalar
eSwitchStormActionsInitiated = _ESwitchStormActionsInitiated_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 8),
    _ESwitchStormActionsInitiated_Type()
)
eSwitchStormActionsInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchStormActionsInitiated.setStatus("mandatory")
_ESwitchStormPortTable_Object = MibTable
eSwitchStormPortTable = _ESwitchStormPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 9)
)
if mibBuilder.loadTexts:
    eSwitchStormPortTable.setStatus("mandatory")
_ESwitchStormPortEntry_Object = MibTableRow
eSwitchStormPortEntry = _ESwitchStormPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 9, 1)
)
eSwitchStormPortEntry.setIndexNames(
    (0, "ESWITCH-MIB-V3-0", "eSwitchStormPortIndex"),
)
if mibBuilder.loadTexts:
    eSwitchStormPortEntry.setStatus("mandatory")


class _ESwitchStormPortIndex_Type(Integer32):
    """Custom type eSwitchStormPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ESwitchStormPortIndex_Type.__name__ = "Integer32"
_ESwitchStormPortIndex_Object = MibTableColumn
eSwitchStormPortIndex = _ESwitchStormPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 9, 1, 1),
    _ESwitchStormPortIndex_Type()
)
eSwitchStormPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchStormPortIndex.setStatus("mandatory")


class _ESwitchStormPortControlStatus_Type(Integer32):
    """Custom type eSwitchStormPortControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 1))
    )


_ESwitchStormPortControlStatus_Type.__name__ = "Integer32"
_ESwitchStormPortControlStatus_Object = MibTableColumn
eSwitchStormPortControlStatus = _ESwitchStormPortControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 9, 1, 2),
    _ESwitchStormPortControlStatus_Type()
)
eSwitchStormPortControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchStormPortControlStatus.setStatus("mandatory")
_ESwitchStormPortFramesLost_Type = Counter32
_ESwitchStormPortFramesLost_Object = MibTableColumn
eSwitchStormPortFramesLost = _ESwitchStormPortFramesLost_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 9, 1, 3),
    _ESwitchStormPortFramesLost_Type()
)
eSwitchStormPortFramesLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchStormPortFramesLost.setStatus("mandatory")
_ESwitchStormPortActionsInitiated_Type = Counter32
_ESwitchStormPortActionsInitiated_Object = MibTableColumn
eSwitchStormPortActionsInitiated = _ESwitchStormPortActionsInitiated_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 4, 9, 1, 4),
    _ESwitchStormPortActionsInitiated_Type()
)
eSwitchStormPortActionsInitiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchStormPortActionsInitiated.setStatus("mandatory")
_ESwitchSecurity_ObjectIdentity = ObjectIdentity
eSwitchSecurity = _ESwitchSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5)
)
_ESwitchSecurityViolationsDetected_Type = Integer32
_ESwitchSecurityViolationsDetected_Object = MibScalar
eSwitchSecurityViolationsDetected = _ESwitchSecurityViolationsDetected_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 1),
    _ESwitchSecurityViolationsDetected_Type()
)
eSwitchSecurityViolationsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchSecurityViolationsDetected.setStatus("mandatory")
_ESwitchSecurityPortTable_Object = MibTable
eSwitchSecurityPortTable = _ESwitchSecurityPortTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 2)
)
if mibBuilder.loadTexts:
    eSwitchSecurityPortTable.setStatus("mandatory")
_ESwitchSecurityPortEntry_Object = MibTableRow
eSwitchSecurityPortEntry = _ESwitchSecurityPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 2, 1)
)
eSwitchSecurityPortEntry.setIndexNames(
    (0, "ESWITCH-MIB-V3-0", "eSwitchSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    eSwitchSecurityPortEntry.setStatus("mandatory")


class _ESwitchSecurityPortIndex_Type(Integer32):
    """Custom type eSwitchSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ESwitchSecurityPortIndex_Type.__name__ = "Integer32"
_ESwitchSecurityPortIndex_Object = MibTableColumn
eSwitchSecurityPortIndex = _ESwitchSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 2, 1, 1),
    _ESwitchSecurityPortIndex_Type()
)
eSwitchSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchSecurityPortIndex.setStatus("mandatory")


class _ESwitchSecurityPortMode_Type(Integer32):
    """Custom type eSwitchSecurityPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-authorize", 3),
          ("manual-authorize", 2),
          ("none", 1))
    )


_ESwitchSecurityPortMode_Type.__name__ = "Integer32"
_ESwitchSecurityPortMode_Object = MibTableColumn
eSwitchSecurityPortMode = _ESwitchSecurityPortMode_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 2, 1, 2),
    _ESwitchSecurityPortMode_Type()
)
eSwitchSecurityPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchSecurityPortMode.setStatus("mandatory")
_ESwitchSecurityPortViolationsDetected_Type = Integer32
_ESwitchSecurityPortViolationsDetected_Object = MibTableColumn
eSwitchSecurityPortViolationsDetected = _ESwitchSecurityPortViolationsDetected_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 2, 1, 3),
    _ESwitchSecurityPortViolationsDetected_Type()
)
eSwitchSecurityPortViolationsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchSecurityPortViolationsDetected.setStatus("mandatory")


class _ESwitchSecurityPortViolationResponse_Type(Integer32):
    """Custom type eSwitchSecurityPortViolationResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("filter-and-log", 2),
          ("shutdown-and-log", 3))
    )


_ESwitchSecurityPortViolationResponse_Type.__name__ = "Integer32"
_ESwitchSecurityPortViolationResponse_Object = MibTableColumn
eSwitchSecurityPortViolationResponse = _ESwitchSecurityPortViolationResponse_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 2, 1, 4),
    _ESwitchSecurityPortViolationResponse_Type()
)
eSwitchSecurityPortViolationResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchSecurityPortViolationResponse.setStatus("mandatory")
_ESwitchSecurityPortMaxAuthAddr_Type = Integer32
_ESwitchSecurityPortMaxAuthAddr_Object = MibTableColumn
eSwitchSecurityPortMaxAuthAddr = _ESwitchSecurityPortMaxAuthAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 2, 1, 5),
    _ESwitchSecurityPortMaxAuthAddr_Type()
)
eSwitchSecurityPortMaxAuthAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchSecurityPortMaxAuthAddr.setStatus("mandatory")
_ESwitchSecurityPortMaxAutoAuthAddr_Type = Integer32
_ESwitchSecurityPortMaxAutoAuthAddr_Object = MibTableColumn
eSwitchSecurityPortMaxAutoAuthAddr = _ESwitchSecurityPortMaxAutoAuthAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 2, 1, 6),
    _ESwitchSecurityPortMaxAutoAuthAddr_Type()
)
eSwitchSecurityPortMaxAutoAuthAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchSecurityPortMaxAutoAuthAddr.setStatus("mandatory")
_ESwitchSecurityPortCurrAuthAddr_Type = Integer32
_ESwitchSecurityPortCurrAuthAddr_Object = MibTableColumn
eSwitchSecurityPortCurrAuthAddr = _ESwitchSecurityPortCurrAuthAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 2, 1, 7),
    _ESwitchSecurityPortCurrAuthAddr_Type()
)
eSwitchSecurityPortCurrAuthAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchSecurityPortCurrAuthAddr.setStatus("mandatory")


class _ESwitchSecurityPortPurgeAuthAddr_Type(Integer32):
    """Custom type eSwitchSecurityPortPurgeAuthAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("trigger", 1)
    )


_ESwitchSecurityPortPurgeAuthAddr_Type.__name__ = "Integer32"
_ESwitchSecurityPortPurgeAuthAddr_Object = MibTableColumn
eSwitchSecurityPortPurgeAuthAddr = _ESwitchSecurityPortPurgeAuthAddr_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 2, 1, 8),
    _ESwitchSecurityPortPurgeAuthAddr_Type()
)
eSwitchSecurityPortPurgeAuthAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchSecurityPortPurgeAuthAddr.setStatus("mandatory")
_ESwitchSecurityAuthTable_Object = MibTable
eSwitchSecurityAuthTable = _ESwitchSecurityAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 3)
)
if mibBuilder.loadTexts:
    eSwitchSecurityAuthTable.setStatus("mandatory")
_ESwitchSecurityAuthEntry_Object = MibTableRow
eSwitchSecurityAuthEntry = _ESwitchSecurityAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 3, 1)
)
eSwitchSecurityAuthEntry.setIndexNames(
    (0, "ESWITCH-MIB-V3-0", "eSwitchSecurityAuthPort"),
    (0, "ESWITCH-MIB-V3-0", "eSwitchSecurityAuthAddress"),
)
if mibBuilder.loadTexts:
    eSwitchSecurityAuthEntry.setStatus("mandatory")


class _ESwitchSecurityAuthPort_Type(Integer32):
    """Custom type eSwitchSecurityAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ESwitchSecurityAuthPort_Type.__name__ = "Integer32"
_ESwitchSecurityAuthPort_Object = MibTableColumn
eSwitchSecurityAuthPort = _ESwitchSecurityAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 3, 1, 1),
    _ESwitchSecurityAuthPort_Type()
)
eSwitchSecurityAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchSecurityAuthPort.setStatus("mandatory")


class _ESwitchSecurityAuthAddress_Type(OctetString):
    """Custom type eSwitchSecurityAuthAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ESwitchSecurityAuthAddress_Type.__name__ = "OctetString"
_ESwitchSecurityAuthAddress_Object = MibTableColumn
eSwitchSecurityAuthAddress = _ESwitchSecurityAuthAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 3, 1, 2),
    _ESwitchSecurityAuthAddress_Type()
)
eSwitchSecurityAuthAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchSecurityAuthAddress.setStatus("mandatory")


class _ESwitchSecurityAuthStatus_Type(Integer32):
    """Custom type eSwitchSecurityAuthStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("invalid", 1))
    )


_ESwitchSecurityAuthStatus_Type.__name__ = "Integer32"
_ESwitchSecurityAuthStatus_Object = MibTableColumn
eSwitchSecurityAuthStatus = _ESwitchSecurityAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 3, 1, 3),
    _ESwitchSecurityAuthStatus_Type()
)
eSwitchSecurityAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSwitchSecurityAuthStatus.setStatus("mandatory")
_ESwitchSecurityLog_ObjectIdentity = ObjectIdentity
eSwitchSecurityLog = _ESwitchSecurityLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 4)
)
_ESwitchSecurityLogMaxEntries_Type = Integer32
_ESwitchSecurityLogMaxEntries_Object = MibScalar
eSwitchSecurityLogMaxEntries = _ESwitchSecurityLogMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 4, 1),
    _ESwitchSecurityLogMaxEntries_Type()
)
eSwitchSecurityLogMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchSecurityLogMaxEntries.setStatus("mandatory")
_ESwitchSecurityLogTable_Object = MibTable
eSwitchSecurityLogTable = _ESwitchSecurityLogTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 4, 2)
)
if mibBuilder.loadTexts:
    eSwitchSecurityLogTable.setStatus("mandatory")
_ESwitchSecurityLogEntry_Object = MibTableRow
eSwitchSecurityLogEntry = _ESwitchSecurityLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 4, 2, 1)
)
eSwitchSecurityLogEntry.setIndexNames(
    (0, "ESWITCH-MIB-V3-0", "eSwitchSecurityLogIndex"),
)
if mibBuilder.loadTexts:
    eSwitchSecurityLogEntry.setStatus("mandatory")


class _ESwitchSecurityLogIndex_Type(Integer32):
    """Custom type eSwitchSecurityLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ESwitchSecurityLogIndex_Type.__name__ = "Integer32"
_ESwitchSecurityLogIndex_Object = MibTableColumn
eSwitchSecurityLogIndex = _ESwitchSecurityLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 4, 2, 1, 1),
    _ESwitchSecurityLogIndex_Type()
)
eSwitchSecurityLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchSecurityLogIndex.setStatus("mandatory")
_ESwitchSecurityLogPort_Type = Integer32
_ESwitchSecurityLogPort_Object = MibTableColumn
eSwitchSecurityLogPort = _ESwitchSecurityLogPort_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 4, 2, 1, 2),
    _ESwitchSecurityLogPort_Type()
)
eSwitchSecurityLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchSecurityLogPort.setStatus("mandatory")


class _ESwitchSecurityLogAddress_Type(OctetString):
    """Custom type eSwitchSecurityLogAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_ESwitchSecurityLogAddress_Type.__name__ = "OctetString"
_ESwitchSecurityLogAddress_Object = MibTableColumn
eSwitchSecurityLogAddress = _ESwitchSecurityLogAddress_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 4, 2, 1, 3),
    _ESwitchSecurityLogAddress_Type()
)
eSwitchSecurityLogAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchSecurityLogAddress.setStatus("mandatory")


class _ESwitchSecurityLogResetNumber_Type(Integer32):
    """Custom type eSwitchSecurityLogResetNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ESwitchSecurityLogResetNumber_Type.__name__ = "Integer32"
_ESwitchSecurityLogResetNumber_Object = MibTableColumn
eSwitchSecurityLogResetNumber = _ESwitchSecurityLogResetNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 4, 2, 1, 4),
    _ESwitchSecurityLogResetNumber_Type()
)
eSwitchSecurityLogResetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchSecurityLogResetNumber.setStatus("mandatory")
_ESwitchSecurityLogTime_Type = TimeTicks
_ESwitchSecurityLogTime_Object = MibTableColumn
eSwitchSecurityLogTime = _ESwitchSecurityLogTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 7, 5, 4, 2, 1, 5),
    _ESwitchSecurityLogTime_Type()
)
eSwitchSecurityLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSwitchSecurityLogTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ESWITCH-MIB-V3-0",
    **{"dec": dec,
       "ema": ema,
       "decMIBextension": decMIBextension,
       "decHub900": decHub900,
       "eSwitch": eSwitch,
       "eSwitchIf": eSwitchIf,
       "eSwitchIfTable": eSwitchIfTable,
       "eSwitchIfEntry": eSwitchIfEntry,
       "eSwitchIfIndex": eSwitchIfIndex,
       "eSwitchIfPresent": eSwitchIfPresent,
       "eSwitchPort": eSwitchPort,
       "eSwitchPortTable": eSwitchPortTable,
       "eSwitchPortEntry": eSwitchPortEntry,
       "eSwitchPortIndex": eSwitchPortIndex,
       "eSwitchPortFailed": eSwitchPortFailed,
       "eSwitchPortStatus": eSwitchPortStatus,
       "eSwitchPortShutDownReason": eSwitchPortShutDownReason,
       "eSwitchPortSwitchingMode": eSwitchPortSwitchingMode,
       "eSwitchFdb": eSwitchFdb,
       "eSwitchAddrFdb": eSwitchAddrFdb,
       "eSwitchAddrFdbMaxEntries": eSwitchAddrFdbMaxEntries,
       "eSwitchAddrFdbMaxStaticEntries": eSwitchAddrFdbMaxStaticEntries,
       "eSwitchAddrFdbMaxNVStaticEntries": eSwitchAddrFdbMaxNVStaticEntries,
       "eSwitchAddrFdbDynamicEntries": eSwitchAddrFdbDynamicEntries,
       "eSwitchAddrFdbStaticEntries": eSwitchAddrFdbStaticEntries,
       "eSwitchAddrFdbNVStaticEntries": eSwitchAddrFdbNVStaticEntries,
       "eSwitchAddrFdbPurgeStaticEntries": eSwitchAddrFdbPurgeStaticEntries,
       "eSwitchStorm": eSwitchStorm,
       "eSwitchStormFrameTypeRegulated": eSwitchStormFrameTypeRegulated,
       "eSwitchStormPollingInterval": eSwitchStormPollingInterval,
       "eSwitchStormRateLimit": eSwitchStormRateLimit,
       "eSwitchStormControlAction": eSwitchStormControlAction,
       "eSwitchStormResumptionPolicy": eSwitchStormResumptionPolicy,
       "eSwitchStormAutoInterval": eSwitchStormAutoInterval,
       "eSwitchStormFramesLost": eSwitchStormFramesLost,
       "eSwitchStormActionsInitiated": eSwitchStormActionsInitiated,
       "eSwitchStormPortTable": eSwitchStormPortTable,
       "eSwitchStormPortEntry": eSwitchStormPortEntry,
       "eSwitchStormPortIndex": eSwitchStormPortIndex,
       "eSwitchStormPortControlStatus": eSwitchStormPortControlStatus,
       "eSwitchStormPortFramesLost": eSwitchStormPortFramesLost,
       "eSwitchStormPortActionsInitiated": eSwitchStormPortActionsInitiated,
       "eSwitchSecurity": eSwitchSecurity,
       "eSwitchSecurityViolationsDetected": eSwitchSecurityViolationsDetected,
       "eSwitchSecurityPortTable": eSwitchSecurityPortTable,
       "eSwitchSecurityPortEntry": eSwitchSecurityPortEntry,
       "eSwitchSecurityPortIndex": eSwitchSecurityPortIndex,
       "eSwitchSecurityPortMode": eSwitchSecurityPortMode,
       "eSwitchSecurityPortViolationsDetected": eSwitchSecurityPortViolationsDetected,
       "eSwitchSecurityPortViolationResponse": eSwitchSecurityPortViolationResponse,
       "eSwitchSecurityPortMaxAuthAddr": eSwitchSecurityPortMaxAuthAddr,
       "eSwitchSecurityPortMaxAutoAuthAddr": eSwitchSecurityPortMaxAutoAuthAddr,
       "eSwitchSecurityPortCurrAuthAddr": eSwitchSecurityPortCurrAuthAddr,
       "eSwitchSecurityPortPurgeAuthAddr": eSwitchSecurityPortPurgeAuthAddr,
       "eSwitchSecurityAuthTable": eSwitchSecurityAuthTable,
       "eSwitchSecurityAuthEntry": eSwitchSecurityAuthEntry,
       "eSwitchSecurityAuthPort": eSwitchSecurityAuthPort,
       "eSwitchSecurityAuthAddress": eSwitchSecurityAuthAddress,
       "eSwitchSecurityAuthStatus": eSwitchSecurityAuthStatus,
       "eSwitchSecurityLog": eSwitchSecurityLog,
       "eSwitchSecurityLogMaxEntries": eSwitchSecurityLogMaxEntries,
       "eSwitchSecurityLogTable": eSwitchSecurityLogTable,
       "eSwitchSecurityLogEntry": eSwitchSecurityLogEntry,
       "eSwitchSecurityLogIndex": eSwitchSecurityLogIndex,
       "eSwitchSecurityLogPort": eSwitchSecurityLogPort,
       "eSwitchSecurityLogAddress": eSwitchSecurityLogAddress,
       "eSwitchSecurityLogResetNumber": eSwitchSecurityLogResetNumber,
       "eSwitchSecurityLogTime": eSwitchSecurityLogTime}
)
