# SNMP MIB module (Wellfleet-DLS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-DLS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:02 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfDlsGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDlsGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDls_ObjectIdentity = ObjectIdentity
wfDls = _WfDls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1)
)


class _WfDlsDelete_Type(Integer32):
    """Custom type wfDlsDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsDelete_Type.__name__ = "Integer32"
_WfDlsDelete_Object = MibScalar
wfDlsDelete = _WfDlsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 1),
    _WfDlsDelete_Type()
)
wfDlsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsDelete.setStatus("mandatory")


class _WfDlsDisable_Type(Integer32):
    """Custom type wfDlsDisable based on Integer32"""
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


_WfDlsDisable_Type.__name__ = "Integer32"
_WfDlsDisable_Object = MibScalar
wfDlsDisable = _WfDlsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 2),
    _WfDlsDisable_Type()
)
wfDlsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsDisable.setStatus("mandatory")


class _WfDlsState_Type(Integer32):
    """Custom type wfDlsState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfDlsState_Type.__name__ = "Integer32"
_WfDlsState_Object = MibScalar
wfDlsState = _WfDlsState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 3),
    _WfDlsState_Type()
)
wfDlsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsState.setStatus("mandatory")


class _WfDlsTcpWindowSize_Type(Integer32):
    """Custom type wfDlsTcpWindowSize based on Integer32"""
    defaultValue = 8000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 64000),
    )


_WfDlsTcpWindowSize_Type.__name__ = "Integer32"
_WfDlsTcpWindowSize_Object = MibScalar
wfDlsTcpWindowSize = _WfDlsTcpWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 4),
    _WfDlsTcpWindowSize_Type()
)
wfDlsTcpWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsTcpWindowSize.setStatus("mandatory")
_WfDlsVirtualRing_Type = Integer32
_WfDlsVirtualRing_Object = MibScalar
wfDlsVirtualRing = _WfDlsVirtualRing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 5),
    _WfDlsVirtualRing_Type()
)
wfDlsVirtualRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsVirtualRing.setStatus("mandatory")
_WfDlsInternalLanId_Type = Integer32
_WfDlsInternalLanId_Object = MibScalar
wfDlsInternalLanId = _WfDlsInternalLanId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 6),
    _WfDlsInternalLanId_Type()
)
wfDlsInternalLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInternalLanId.setStatus("mandatory")
_WfDlsBridgeId_Type = Integer32
_WfDlsBridgeId_Object = MibScalar
wfDlsBridgeId = _WfDlsBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 7),
    _WfDlsBridgeId_Type()
)
wfDlsBridgeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsBridgeId.setStatus("mandatory")


class _WfDlsMaxSlotSessions_Type(Integer32):
    """Custom type wfDlsMaxSlotSessions based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_WfDlsMaxSlotSessions_Type.__name__ = "Integer32"
_WfDlsMaxSlotSessions_Object = MibScalar
wfDlsMaxSlotSessions = _WfDlsMaxSlotSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 8),
    _WfDlsMaxSlotSessions_Type()
)
wfDlsMaxSlotSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMaxSlotSessions.setStatus("mandatory")
_WfDlsTotalCircuits_Type = Counter32
_WfDlsTotalCircuits_Object = MibScalar
wfDlsTotalCircuits = _WfDlsTotalCircuits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 9),
    _WfDlsTotalCircuits_Type()
)
wfDlsTotalCircuits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsTotalCircuits.setStatus("mandatory")


class _WfDlsVirtualRingMtu_Type(Integer32):
    """Custom type wfDlsVirtualRingMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_WfDlsVirtualRingMtu_Type.__name__ = "Integer32"
_WfDlsVirtualRingMtu_Object = MibScalar
wfDlsVirtualRingMtu = _WfDlsVirtualRingMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 10),
    _WfDlsVirtualRingMtu_Type()
)
wfDlsVirtualRingMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsVirtualRingMtu.setStatus("mandatory")


class _WfDlsMacAgeTime_Type(Gauge32):
    """Custom type wfDlsMacAgeTime based on Gauge32"""
    defaultValue = 300

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfDlsMacAgeTime_Type.__name__ = "Gauge32"
_WfDlsMacAgeTime_Object = MibScalar
wfDlsMacAgeTime = _WfDlsMacAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 11),
    _WfDlsMacAgeTime_Type()
)
wfDlsMacAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMacAgeTime.setStatus("mandatory")


class _WfDlsNbAgeTime_Type(Gauge32):
    """Custom type wfDlsNbAgeTime based on Gauge32"""
    defaultValue = 300

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 4294967295),
    )


_WfDlsNbAgeTime_Type.__name__ = "Gauge32"
_WfDlsNbAgeTime_Object = MibScalar
wfDlsNbAgeTime = _WfDlsNbAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 12),
    _WfDlsNbAgeTime_Type()
)
wfDlsNbAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsNbAgeTime.setStatus("mandatory")


class _WfDlsUnconfPeerReject_Type(Integer32):
    """Custom type wfDlsUnconfPeerReject based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 1),
          ("rejected", 2))
    )


_WfDlsUnconfPeerReject_Type.__name__ = "Integer32"
_WfDlsUnconfPeerReject_Object = MibScalar
wfDlsUnconfPeerReject = _WfDlsUnconfPeerReject_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 13),
    _WfDlsUnconfPeerReject_Type()
)
wfDlsUnconfPeerReject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsUnconfPeerReject.setStatus("mandatory")


class _WfDlsDebugLevel1_Type(Gauge32):
    """Custom type wfDlsDebugLevel1 based on Gauge32"""
    defaultValue = 4294967295


_WfDlsDebugLevel1_Object = MibScalar
wfDlsDebugLevel1 = _WfDlsDebugLevel1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 14),
    _WfDlsDebugLevel1_Type()
)
wfDlsDebugLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsDebugLevel1.setStatus("mandatory")


class _WfDlsDebugLevel2_Type(Gauge32):
    """Custom type wfDlsDebugLevel2 based on Gauge32"""
    defaultValue = 0


_WfDlsDebugLevel2_Object = MibScalar
wfDlsDebugLevel2 = _WfDlsDebugLevel2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 15),
    _WfDlsDebugLevel2_Type()
)
wfDlsDebugLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsDebugLevel2.setStatus("mandatory")


class _WfDlsWanKeepaliveTime_Type(Integer32):
    """Custom type wfDlsWanKeepaliveTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsWanKeepaliveTime_Type.__name__ = "Integer32"
_WfDlsWanKeepaliveTime_Object = MibScalar
wfDlsWanKeepaliveTime = _WfDlsWanKeepaliveTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 16),
    _WfDlsWanKeepaliveTime_Type()
)
wfDlsWanKeepaliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsWanKeepaliveTime.setStatus("mandatory")


class _WfDlsPPriDisable_Type(Integer32):
    """Custom type wfDlsPPriDisable based on Integer32"""
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


_WfDlsPPriDisable_Type.__name__ = "Integer32"
_WfDlsPPriDisable_Object = MibScalar
wfDlsPPriDisable = _WfDlsPPriDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 17),
    _WfDlsPPriDisable_Type()
)
wfDlsPPriDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPPriDisable.setStatus("mandatory")


class _WfDlsPPriDefaultNumQueues_Type(Integer32):
    """Custom type wfDlsPPriDefaultNumQueues based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfDlsPPriDefaultNumQueues_Type.__name__ = "Integer32"
_WfDlsPPriDefaultNumQueues_Object = MibScalar
wfDlsPPriDefaultNumQueues = _WfDlsPPriDefaultNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 18),
    _WfDlsPPriDefaultNumQueues_Type()
)
wfDlsPPriDefaultNumQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPPriDefaultNumQueues.setStatus("mandatory")
_WfDlsPPriDefaultQBandwidth_Type = OctetString
_WfDlsPPriDefaultQBandwidth_Object = MibScalar
wfDlsPPriDefaultQBandwidth = _WfDlsPPriDefaultQBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 19),
    _WfDlsPPriDefaultQBandwidth_Type()
)
wfDlsPPriDefaultQBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPPriDefaultQBandwidth.setStatus("mandatory")


class _WfDlsPPriUnconfPeerDisable_Type(Integer32):
    """Custom type wfDlsPPriUnconfPeerDisable based on Integer32"""
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


_WfDlsPPriUnconfPeerDisable_Type.__name__ = "Integer32"
_WfDlsPPriUnconfPeerDisable_Object = MibScalar
wfDlsPPriUnconfPeerDisable = _WfDlsPPriUnconfPeerDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 20),
    _WfDlsPPriUnconfPeerDisable_Type()
)
wfDlsPPriUnconfPeerDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPPriUnconfPeerDisable.setStatus("mandatory")


class _WfDlsPPriUnconfPeerMaxQBuf_Type(Integer32):
    """Custom type wfDlsPPriUnconfPeerMaxQBuf based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            50
        )
    )
    namedValues = NamedValues(
        ("default", 50)
    )


_WfDlsPPriUnconfPeerMaxQBuf_Type.__name__ = "Integer32"
_WfDlsPPriUnconfPeerMaxQBuf_Object = MibScalar
wfDlsPPriUnconfPeerMaxQBuf = _WfDlsPPriUnconfPeerMaxQBuf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 21),
    _WfDlsPPriUnconfPeerMaxQBuf_Type()
)
wfDlsPPriUnconfPeerMaxQBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPPriUnconfPeerMaxQBuf.setStatus("mandatory")


class _WfDlsPPriUnconfPeerMaxQSize_Type(Integer32):
    """Custom type wfDlsPPriUnconfPeerMaxQSize based on Integer32"""
    defaultValue = 16000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            16000
        )
    )
    namedValues = NamedValues(
        ("default", 16000)
    )


_WfDlsPPriUnconfPeerMaxQSize_Type.__name__ = "Integer32"
_WfDlsPPriUnconfPeerMaxQSize_Object = MibScalar
wfDlsPPriUnconfPeerMaxQSize = _WfDlsPPriUnconfPeerMaxQSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 22),
    _WfDlsPPriUnconfPeerMaxQSize_Type()
)
wfDlsPPriUnconfPeerMaxQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPPriUnconfPeerMaxQSize.setStatus("mandatory")


class _WfDlsPkgMaxSize_Type(Integer32):
    """Custom type wfDlsPkgMaxSize based on Integer32"""
    defaultValue = 1532

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsPkgMaxSize_Type.__name__ = "Integer32"
_WfDlsPkgMaxSize_Object = MibScalar
wfDlsPkgMaxSize = _WfDlsPkgMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 23),
    _WfDlsPkgMaxSize_Type()
)
wfDlsPkgMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPkgMaxSize.setStatus("mandatory")


class _WfDlsPkgTO_Type(Integer32):
    """Custom type wfDlsPkgTO based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsPkgTO_Type.__name__ = "Integer32"
_WfDlsPkgTO_Object = MibScalar
wfDlsPkgTO = _WfDlsPkgTO_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 24),
    _WfDlsPkgTO_Type()
)
wfDlsPkgTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPkgTO.setStatus("mandatory")


class _WfDlsPkgWinPercent_Type(Integer32):
    """Custom type wfDlsPkgWinPercent based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfDlsPkgWinPercent_Type.__name__ = "Integer32"
_WfDlsPkgWinPercent_Object = MibScalar
wfDlsPkgWinPercent = _WfDlsPkgWinPercent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 25),
    _WfDlsPkgWinPercent_Type()
)
wfDlsPkgWinPercent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPkgWinPercent.setStatus("mandatory")


class _WfDlsMultislotBcasts_Type(Integer32):
    """Custom type wfDlsMultislotBcasts based on Integer32"""
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


_WfDlsMultislotBcasts_Type.__name__ = "Integer32"
_WfDlsMultislotBcasts_Object = MibScalar
wfDlsMultislotBcasts = _WfDlsMultislotBcasts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 26),
    _WfDlsMultislotBcasts_Type()
)
wfDlsMultislotBcasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMultislotBcasts.setStatus("mandatory")


class _WfDlsInitialPacingWindow_Type(Integer32):
    """Custom type wfDlsInitialPacingWindow based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 100),
    )


_WfDlsInitialPacingWindow_Type.__name__ = "Integer32"
_WfDlsInitialPacingWindow_Object = MibScalar
wfDlsInitialPacingWindow = _WfDlsInitialPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 27),
    _WfDlsInitialPacingWindow_Type()
)
wfDlsInitialPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInitialPacingWindow.setStatus("mandatory")


class _WfDlsRfc_Type(Integer32):
    """Custom type wfDlsRfc based on Integer32"""
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
        *(("rfc1434", 1),
          ("rfc1795", 2),
          ("rfc2166", 4),
          ("v20unicast", 3))
    )


_WfDlsRfc_Type.__name__ = "Integer32"
_WfDlsRfc_Object = MibScalar
wfDlsRfc = _WfDlsRfc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 28),
    _WfDlsRfc_Type()
)
wfDlsRfc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsRfc.setStatus("mandatory")


class _WfDlsNetbiosSessionAliveFilter_Type(Integer32):
    """Custom type wfDlsNetbiosSessionAliveFilter based on Integer32"""
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


_WfDlsNetbiosSessionAliveFilter_Type.__name__ = "Integer32"
_WfDlsNetbiosSessionAliveFilter_Object = MibScalar
wfDlsNetbiosSessionAliveFilter = _WfDlsNetbiosSessionAliveFilter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 29),
    _WfDlsNetbiosSessionAliveFilter_Type()
)
wfDlsNetbiosSessionAliveFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsNetbiosSessionAliveFilter.setStatus("mandatory")


class _WfDlsWanKeepaliveRetryTimer_Type(Integer32):
    """Custom type wfDlsWanKeepaliveRetryTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_WfDlsWanKeepaliveRetryTimer_Type.__name__ = "Integer32"
_WfDlsWanKeepaliveRetryTimer_Object = MibScalar
wfDlsWanKeepaliveRetryTimer = _WfDlsWanKeepaliveRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 30),
    _WfDlsWanKeepaliveRetryTimer_Type()
)
wfDlsWanKeepaliveRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsWanKeepaliveRetryTimer.setStatus("mandatory")


class _WfDlsWanKeepaliveRetries_Type(Integer32):
    """Custom type wfDlsWanKeepaliveRetries based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_WfDlsWanKeepaliveRetries_Type.__name__ = "Integer32"
_WfDlsWanKeepaliveRetries_Object = MibScalar
wfDlsWanKeepaliveRetries = _WfDlsWanKeepaliveRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 31),
    _WfDlsWanKeepaliveRetries_Type()
)
wfDlsWanKeepaliveRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsWanKeepaliveRetries.setStatus("mandatory")


class _WfDlsSnaFallbackAttempts_Type(Integer32):
    """Custom type wfDlsSnaFallbackAttempts based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsSnaFallbackAttempts_Type.__name__ = "Integer32"
_WfDlsSnaFallbackAttempts_Object = MibScalar
wfDlsSnaFallbackAttempts = _WfDlsSnaFallbackAttempts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 32),
    _WfDlsSnaFallbackAttempts_Type()
)
wfDlsSnaFallbackAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsSnaFallbackAttempts.setStatus("mandatory")


class _WfDlsNetbiosFallbackTime_Type(Integer32):
    """Custom type wfDlsNetbiosFallbackTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsNetbiosFallbackTime_Type.__name__ = "Integer32"
_WfDlsNetbiosFallbackTime_Object = MibScalar
wfDlsNetbiosFallbackTime = _WfDlsNetbiosFallbackTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 33),
    _WfDlsNetbiosFallbackTime_Type()
)
wfDlsNetbiosFallbackTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsNetbiosFallbackTime.setStatus("mandatory")


class _WfDlsTcpInactTime_Type(Integer32):
    """Custom type wfDlsTcpInactTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsTcpInactTime_Type.__name__ = "Integer32"
_WfDlsTcpInactTime_Object = MibScalar
wfDlsTcpInactTime = _WfDlsTcpInactTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 34),
    _WfDlsTcpInactTime_Type()
)
wfDlsTcpInactTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsTcpInactTime.setStatus("mandatory")


class _WfDlsTcpInactMethod_Type(Integer32):
    """Custom type wfDlsTcpInactMethod based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("circuits", 2),
          ("data", 3),
          ("never", 1))
    )


_WfDlsTcpInactMethod_Type.__name__ = "Integer32"
_WfDlsTcpInactMethod_Object = MibScalar
wfDlsTcpInactMethod = _WfDlsTcpInactMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 35),
    _WfDlsTcpInactMethod_Type()
)
wfDlsTcpInactMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsTcpInactMethod.setStatus("mandatory")


class _WfDlsMslotDLCBcasts_Type(Integer32):
    """Custom type wfDlsMslotDLCBcasts based on Integer32"""
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


_WfDlsMslotDLCBcasts_Type.__name__ = "Integer32"
_WfDlsMslotDLCBcasts_Object = MibScalar
wfDlsMslotDLCBcasts = _WfDlsMslotDLCBcasts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 36),
    _WfDlsMslotDLCBcasts_Type()
)
wfDlsMslotDLCBcasts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMslotDLCBcasts.setStatus("mandatory")


class _WfDlsRsvpSupport_Type(Integer32):
    """Custom type wfDlsRsvpSupport based on Integer32"""
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


_WfDlsRsvpSupport_Type.__name__ = "Integer32"
_WfDlsRsvpSupport_Object = MibScalar
wfDlsRsvpSupport = _WfDlsRsvpSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 37),
    _WfDlsRsvpSupport_Type()
)
wfDlsRsvpSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsRsvpSupport.setStatus("mandatory")


class _WfDlsOutBandwidth_Type(Integer32):
    """Custom type wfDlsOutBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsOutBandwidth_Type.__name__ = "Integer32"
_WfDlsOutBandwidth_Object = MibScalar
wfDlsOutBandwidth = _WfDlsOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 38),
    _WfDlsOutBandwidth_Type()
)
wfDlsOutBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsOutBandwidth.setStatus("mandatory")


class _WfDlsOutBurstSize_Type(Integer32):
    """Custom type wfDlsOutBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsOutBurstSize_Type.__name__ = "Integer32"
_WfDlsOutBurstSize_Object = MibScalar
wfDlsOutBurstSize = _WfDlsOutBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 39),
    _WfDlsOutBurstSize_Type()
)
wfDlsOutBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsOutBurstSize.setStatus("mandatory")


class _WfDlsInBandwidth_Type(Integer32):
    """Custom type wfDlsInBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsInBandwidth_Type.__name__ = "Integer32"
_WfDlsInBandwidth_Object = MibScalar
wfDlsInBandwidth = _WfDlsInBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 40),
    _WfDlsInBandwidth_Type()
)
wfDlsInBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInBandwidth.setStatus("mandatory")


class _WfDlsInBurstSize_Type(Integer32):
    """Custom type wfDlsInBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsInBurstSize_Type.__name__ = "Integer32"
_WfDlsInBurstSize_Object = MibScalar
wfDlsInBurstSize = _WfDlsInBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 41),
    _WfDlsInBurstSize_Type()
)
wfDlsInBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInBurstSize.setStatus("mandatory")


class _WfDlsNonPeakOutBandwidth_Type(Integer32):
    """Custom type wfDlsNonPeakOutBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsNonPeakOutBandwidth_Type.__name__ = "Integer32"
_WfDlsNonPeakOutBandwidth_Object = MibScalar
wfDlsNonPeakOutBandwidth = _WfDlsNonPeakOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 42),
    _WfDlsNonPeakOutBandwidth_Type()
)
wfDlsNonPeakOutBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsNonPeakOutBandwidth.setStatus("mandatory")


class _WfDlsNonPeakOutBurstSize_Type(Integer32):
    """Custom type wfDlsNonPeakOutBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsNonPeakOutBurstSize_Type.__name__ = "Integer32"
_WfDlsNonPeakOutBurstSize_Object = MibScalar
wfDlsNonPeakOutBurstSize = _WfDlsNonPeakOutBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 43),
    _WfDlsNonPeakOutBurstSize_Type()
)
wfDlsNonPeakOutBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsNonPeakOutBurstSize.setStatus("mandatory")


class _WfDlsNonPeakInBandwidth_Type(Integer32):
    """Custom type wfDlsNonPeakInBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsNonPeakInBandwidth_Type.__name__ = "Integer32"
_WfDlsNonPeakInBandwidth_Object = MibScalar
wfDlsNonPeakInBandwidth = _WfDlsNonPeakInBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 44),
    _WfDlsNonPeakInBandwidth_Type()
)
wfDlsNonPeakInBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsNonPeakInBandwidth.setStatus("mandatory")


class _WfDlsNonPeakInBurstSize_Type(Integer32):
    """Custom type wfDlsNonPeakInBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsNonPeakInBurstSize_Type.__name__ = "Integer32"
_WfDlsNonPeakInBurstSize_Object = MibScalar
wfDlsNonPeakInBurstSize = _WfDlsNonPeakInBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 45),
    _WfDlsNonPeakInBurstSize_Type()
)
wfDlsNonPeakInBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsNonPeakInBurstSize.setStatus("mandatory")


class _WfDlsNonPeakStartTime_Type(Integer32):
    """Custom type wfDlsNonPeakStartTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2400),
    )


_WfDlsNonPeakStartTime_Type.__name__ = "Integer32"
_WfDlsNonPeakStartTime_Object = MibScalar
wfDlsNonPeakStartTime = _WfDlsNonPeakStartTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 46),
    _WfDlsNonPeakStartTime_Type()
)
wfDlsNonPeakStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsNonPeakStartTime.setStatus("mandatory")


class _WfDlsNonPeakEndTime_Type(Integer32):
    """Custom type wfDlsNonPeakEndTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2400),
    )


_WfDlsNonPeakEndTime_Type.__name__ = "Integer32"
_WfDlsNonPeakEndTime_Object = MibScalar
wfDlsNonPeakEndTime = _WfDlsNonPeakEndTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 47),
    _WfDlsNonPeakEndTime_Type()
)
wfDlsNonPeakEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsNonPeakEndTime.setStatus("mandatory")
_WfDlsNonPeakStartDays_Type = Counter32
_WfDlsNonPeakStartDays_Object = MibScalar
wfDlsNonPeakStartDays = _WfDlsNonPeakStartDays_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 48),
    _WfDlsNonPeakStartDays_Type()
)
wfDlsNonPeakStartDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsNonPeakStartDays.setStatus("mandatory")


class _WfDlsMultislotCacheUpdate_Type(Integer32):
    """Custom type wfDlsMultislotCacheUpdate based on Integer32"""
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


_WfDlsMultislotCacheUpdate_Type.__name__ = "Integer32"
_WfDlsMultislotCacheUpdate_Object = MibScalar
wfDlsMultislotCacheUpdate = _WfDlsMultislotCacheUpdate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 49),
    _WfDlsMultislotCacheUpdate_Type()
)
wfDlsMultislotCacheUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMultislotCacheUpdate.setStatus("mandatory")


class _WfDlsMacAddrTranslation_Type(Integer32):
    """Custom type wfDlsMacAddrTranslation based on Integer32"""
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


_WfDlsMacAddrTranslation_Type.__name__ = "Integer32"
_WfDlsMacAddrTranslation_Object = MibScalar
wfDlsMacAddrTranslation = _WfDlsMacAddrTranslation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 50),
    _WfDlsMacAddrTranslation_Type()
)
wfDlsMacAddrTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMacAddrTranslation.setStatus("mandatory")


class _WfDlsBan2Support_Type(Integer32):
    """Custom type wfDlsBan2Support based on Integer32"""
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


_WfDlsBan2Support_Type.__name__ = "Integer32"
_WfDlsBan2Support_Object = MibScalar
wfDlsBan2Support = _WfDlsBan2Support_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 51),
    _WfDlsBan2Support_Type()
)
wfDlsBan2Support.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsBan2Support.setStatus("mandatory")


class _WfDlsVirtualRingBridgeCheck_Type(Integer32):
    """Custom type wfDlsVirtualRingBridgeCheck based on Integer32"""
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


_WfDlsVirtualRingBridgeCheck_Type.__name__ = "Integer32"
_WfDlsVirtualRingBridgeCheck_Object = MibScalar
wfDlsVirtualRingBridgeCheck = _WfDlsVirtualRingBridgeCheck_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 52),
    _WfDlsVirtualRingBridgeCheck_Type()
)
wfDlsVirtualRingBridgeCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsVirtualRingBridgeCheck.setStatus("mandatory")


class _WfDlsAcceptBadVendorSpecificCapex_Type(Integer32):
    """Custom type wfDlsAcceptBadVendorSpecificCapex based on Integer32"""
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


_WfDlsAcceptBadVendorSpecificCapex_Type.__name__ = "Integer32"
_WfDlsAcceptBadVendorSpecificCapex_Object = MibScalar
wfDlsAcceptBadVendorSpecificCapex = _WfDlsAcceptBadVendorSpecificCapex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 53),
    _WfDlsAcceptBadVendorSpecificCapex_Type()
)
wfDlsAcceptBadVendorSpecificCapex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsAcceptBadVendorSpecificCapex.setStatus("mandatory")


class _WfDlsDiagSwitch_Type(Integer32):
    """Custom type wfDlsDiagSwitch based on Integer32"""
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


_WfDlsDiagSwitch_Type.__name__ = "Integer32"
_WfDlsDiagSwitch_Object = MibScalar
wfDlsDiagSwitch = _WfDlsDiagSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 54),
    _WfDlsDiagSwitch_Type()
)
wfDlsDiagSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsDiagSwitch.setStatus("mandatory")


class _WfDlsAllowSpecAddrNbDatagram_Type(Integer32):
    """Custom type wfDlsAllowSpecAddrNbDatagram based on Integer32"""
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


_WfDlsAllowSpecAddrNbDatagram_Type.__name__ = "Integer32"
_WfDlsAllowSpecAddrNbDatagram_Object = MibScalar
wfDlsAllowSpecAddrNbDatagram = _WfDlsAllowSpecAddrNbDatagram_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 1, 55),
    _WfDlsAllowSpecAddrNbDatagram_Type()
)
wfDlsAllowSpecAddrNbDatagram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsAllowSpecAddrNbDatagram.setStatus("mandatory")
_WfDlsInterfaceTable_Object = MibTable
wfDlsInterfaceTable = _WfDlsInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2)
)
if mibBuilder.loadTexts:
    wfDlsInterfaceTable.setStatus("mandatory")
_WfDlsInterfaceEntry_Object = MibTableRow
wfDlsInterfaceEntry = _WfDlsInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1)
)
wfDlsInterfaceEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfDlsInterfaceEntry.setStatus("mandatory")


class _WfDlsInterfaceDelete_Type(Integer32):
    """Custom type wfDlsInterfaceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsInterfaceDelete_Type.__name__ = "Integer32"
_WfDlsInterfaceDelete_Object = MibTableColumn
wfDlsInterfaceDelete = _WfDlsInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 1),
    _WfDlsInterfaceDelete_Type()
)
wfDlsInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInterfaceDelete.setStatus("mandatory")


class _WfDlsInterfaceDisable_Type(Integer32):
    """Custom type wfDlsInterfaceDisable based on Integer32"""
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


_WfDlsInterfaceDisable_Type.__name__ = "Integer32"
_WfDlsInterfaceDisable_Object = MibTableColumn
wfDlsInterfaceDisable = _WfDlsInterfaceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 2),
    _WfDlsInterfaceDisable_Type()
)
wfDlsInterfaceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInterfaceDisable.setStatus("mandatory")


class _WfDlsInterfaceState_Type(Integer32):
    """Custom type wfDlsInterfaceState based on Integer32"""
    defaultValue = 2

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfDlsInterfaceState_Type.__name__ = "Integer32"
_WfDlsInterfaceState_Object = MibTableColumn
wfDlsInterfaceState = _WfDlsInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 3),
    _WfDlsInterfaceState_Type()
)
wfDlsInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsInterfaceState.setStatus("mandatory")
_WfDlsInterfaceCircuit_Type = Integer32
_WfDlsInterfaceCircuit_Object = MibTableColumn
wfDlsInterfaceCircuit = _WfDlsInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 4),
    _WfDlsInterfaceCircuit_Type()
)
wfDlsInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsInterfaceCircuit.setStatus("mandatory")


class _WfDlsInterfaceBridgeId_Type(Integer32):
    """Custom type wfDlsInterfaceBridgeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WfDlsInterfaceBridgeId_Type.__name__ = "Integer32"
_WfDlsInterfaceBridgeId_Object = MibTableColumn
wfDlsInterfaceBridgeId = _WfDlsInterfaceBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 5),
    _WfDlsInterfaceBridgeId_Type()
)
wfDlsInterfaceBridgeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInterfaceBridgeId.setStatus("mandatory")


class _WfDlsInterfaceLanId_Type(Integer32):
    """Custom type wfDlsInterfaceLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WfDlsInterfaceLanId_Type.__name__ = "Integer32"
_WfDlsInterfaceLanId_Object = MibTableColumn
wfDlsInterfaceLanId = _WfDlsInterfaceLanId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 6),
    _WfDlsInterfaceLanId_Type()
)
wfDlsInterfaceLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInterfaceLanId.setStatus("mandatory")


class _WfDlsInterfaceDlcType_Type(Integer32):
    """Custom type wfDlsInterfaceDlcType based on Integer32"""
    defaultValue = 2

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
        *(("encaps", 4),
          ("fr", 5),
          ("srb", 2),
          ("sync", 1),
          ("tb", 3),
          ("token", 6))
    )


_WfDlsInterfaceDlcType_Type.__name__ = "Integer32"
_WfDlsInterfaceDlcType_Object = MibTableColumn
wfDlsInterfaceDlcType = _WfDlsInterfaceDlcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 7),
    _WfDlsInterfaceDlcType_Type()
)
wfDlsInterfaceDlcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInterfaceDlcType.setStatus("mandatory")


class _WfDlsInterfaceSdlcMode_Type(Integer32):
    """Custom type wfDlsInterfaceSdlcMode based on Integer32"""
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
        *(("mp", 3),
          ("negot", 4),
          ("pp", 2),
          ("primary", 1))
    )


_WfDlsInterfaceSdlcMode_Type.__name__ = "Integer32"
_WfDlsInterfaceSdlcMode_Object = MibTableColumn
wfDlsInterfaceSdlcMode = _WfDlsInterfaceSdlcMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 8),
    _WfDlsInterfaceSdlcMode_Type()
)
wfDlsInterfaceSdlcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInterfaceSdlcMode.setStatus("mandatory")


class _WfDlsInterfaceNbBcastDgramReduce_Type(Integer32):
    """Custom type wfDlsInterfaceNbBcastDgramReduce based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfDlsInterfaceNbBcastDgramReduce_Type.__name__ = "Integer32"
_WfDlsInterfaceNbBcastDgramReduce_Object = MibTableColumn
wfDlsInterfaceNbBcastDgramReduce = _WfDlsInterfaceNbBcastDgramReduce_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 9),
    _WfDlsInterfaceNbBcastDgramReduce_Type()
)
wfDlsInterfaceNbBcastDgramReduce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInterfaceNbBcastDgramReduce.setStatus("mandatory")


class _WfDlsInterfaceExplorerType_Type(Integer32):
    """Custom type wfDlsInterfaceExplorerType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("are", 2),
          ("ste", 1))
    )


_WfDlsInterfaceExplorerType_Type.__name__ = "Integer32"
_WfDlsInterfaceExplorerType_Object = MibTableColumn
wfDlsInterfaceExplorerType = _WfDlsInterfaceExplorerType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 10),
    _WfDlsInterfaceExplorerType_Type()
)
wfDlsInterfaceExplorerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInterfaceExplorerType.setStatus("mandatory")


class _WfDlsInterfaceNbBcastDgramCache_Type(Integer32):
    """Custom type wfDlsInterfaceNbBcastDgramCache based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 3),
          ("forward", 2),
          ("off", 1))
    )


_WfDlsInterfaceNbBcastDgramCache_Type.__name__ = "Integer32"
_WfDlsInterfaceNbBcastDgramCache_Object = MibTableColumn
wfDlsInterfaceNbBcastDgramCache = _WfDlsInterfaceNbBcastDgramCache_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 11),
    _WfDlsInterfaceNbBcastDgramCache_Type()
)
wfDlsInterfaceNbBcastDgramCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInterfaceNbBcastDgramCache.setStatus("mandatory")


class _WfDlsInterfaceClrCallEnable_Type(Integer32):
    """Custom type wfDlsInterfaceClrCallEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfDlsInterfaceClrCallEnable_Type.__name__ = "Integer32"
_WfDlsInterfaceClrCallEnable_Object = MibTableColumn
wfDlsInterfaceClrCallEnable = _WfDlsInterfaceClrCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 2, 1, 12),
    _WfDlsInterfaceClrCallEnable_Type()
)
wfDlsInterfaceClrCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsInterfaceClrCallEnable.setStatus("mandatory")
_WfDlsSlotTable_Object = MibTable
wfDlsSlotTable = _WfDlsSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3)
)
if mibBuilder.loadTexts:
    wfDlsSlotTable.setStatus("mandatory")
_WfDlsSlotEntry_Object = MibTableRow
wfDlsSlotEntry = _WfDlsSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1)
)
wfDlsSlotEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsSlotNumber"),
)
if mibBuilder.loadTexts:
    wfDlsSlotEntry.setStatus("mandatory")


class _WfDlsSlotDelete_Type(Integer32):
    """Custom type wfDlsSlotDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsSlotDelete_Type.__name__ = "Integer32"
_WfDlsSlotDelete_Object = MibTableColumn
wfDlsSlotDelete = _WfDlsSlotDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 1),
    _WfDlsSlotDelete_Type()
)
wfDlsSlotDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsSlotDelete.setStatus("mandatory")
_WfDlsSlotNumber_Type = Integer32
_WfDlsSlotNumber_Object = MibTableColumn
wfDlsSlotNumber = _WfDlsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 2),
    _WfDlsSlotNumber_Type()
)
wfDlsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsSlotNumber.setStatus("mandatory")
_WfDlsSlotIpAddr_Type = IpAddress
_WfDlsSlotIpAddr_Object = MibTableColumn
wfDlsSlotIpAddr = _WfDlsSlotIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 3),
    _WfDlsSlotIpAddr_Type()
)
wfDlsSlotIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsSlotIpAddr.setStatus("mandatory")
_WfDlsCurrentMemory_Type = Integer32
_WfDlsCurrentMemory_Object = MibTableColumn
wfDlsCurrentMemory = _WfDlsCurrentMemory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 4),
    _WfDlsCurrentMemory_Type()
)
wfDlsCurrentMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsCurrentMemory.setStatus("mandatory")


class _WfDlsMaxAllowedMemory_Type(Gauge32):
    """Custom type wfDlsMaxAllowedMemory based on Gauge32"""
    defaultValue = 4294967295


_WfDlsMaxAllowedMemory_Object = MibTableColumn
wfDlsMaxAllowedMemory = _WfDlsMaxAllowedMemory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 5),
    _WfDlsMaxAllowedMemory_Type()
)
wfDlsMaxAllowedMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMaxAllowedMemory.setStatus("mandatory")
_WfDlsHiWaterMark_Type = Integer32
_WfDlsHiWaterMark_Object = MibTableColumn
wfDlsHiWaterMark = _WfDlsHiWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 6),
    _WfDlsHiWaterMark_Type()
)
wfDlsHiWaterMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsHiWaterMark.setStatus("mandatory")


class _WfDlsSlotGenDestination_Type(Integer32):
    """Custom type wfDlsSlotGenDestination based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WfDlsSlotGenDestination_Type.__name__ = "Integer32"
_WfDlsSlotGenDestination_Object = MibTableColumn
wfDlsSlotGenDestination = _WfDlsSlotGenDestination_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 7),
    _WfDlsSlotGenDestination_Type()
)
wfDlsSlotGenDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsSlotGenDestination.setStatus("mandatory")


class _WfDlsSlotGenSessions_Type(Integer32):
    """Custom type wfDlsSlotGenSessions based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WfDlsSlotGenSessions_Type.__name__ = "Integer32"
_WfDlsSlotGenSessions_Object = MibTableColumn
wfDlsSlotGenSessions = _WfDlsSlotGenSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 8),
    _WfDlsSlotGenSessions_Type()
)
wfDlsSlotGenSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsSlotGenSessions.setStatus("mandatory")


class _WfDlsSlotGenUpperMAC_Type(Integer32):
    """Custom type wfDlsSlotGenUpperMAC based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147418112),
    )


_WfDlsSlotGenUpperMAC_Type.__name__ = "Integer32"
_WfDlsSlotGenUpperMAC_Object = MibTableColumn
wfDlsSlotGenUpperMAC = _WfDlsSlotGenUpperMAC_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 9),
    _WfDlsSlotGenUpperMAC_Type()
)
wfDlsSlotGenUpperMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsSlotGenUpperMAC.setStatus("mandatory")


class _WfDlsSlotCurrentSessions_Type(Integer32):
    """Custom type wfDlsSlotCurrentSessions based on Integer32"""
    defaultValue = 0


_WfDlsSlotCurrentSessions_Object = MibTableColumn
wfDlsSlotCurrentSessions = _WfDlsSlotCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 10),
    _WfDlsSlotCurrentSessions_Type()
)
wfDlsSlotCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsSlotCurrentSessions.setStatus("mandatory")


class _WfDlsSlotHiWaterSessions_Type(Integer32):
    """Custom type wfDlsSlotHiWaterSessions based on Integer32"""
    defaultValue = 0


_WfDlsSlotHiWaterSessions_Object = MibTableColumn
wfDlsSlotHiWaterSessions = _WfDlsSlotHiWaterSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 11),
    _WfDlsSlotHiWaterSessions_Type()
)
wfDlsSlotHiWaterSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsSlotHiWaterSessions.setStatus("mandatory")


class _WfDlsSlotHiWaterReset_Type(Integer32):
    """Custom type wfDlsSlotHiWaterReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_WfDlsSlotHiWaterReset_Type.__name__ = "Integer32"
_WfDlsSlotHiWaterReset_Object = MibTableColumn
wfDlsSlotHiWaterReset = _WfDlsSlotHiWaterReset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 3, 1, 12),
    _WfDlsSlotHiWaterReset_Type()
)
wfDlsSlotHiWaterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsSlotHiWaterReset.setStatus("mandatory")
_WfDlsSapTable_Object = MibTable
wfDlsSapTable = _WfDlsSapTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 4)
)
if mibBuilder.loadTexts:
    wfDlsSapTable.setStatus("mandatory")
_WfDlsSapEntry_Object = MibTableRow
wfDlsSapEntry = _WfDlsSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 4, 1)
)
wfDlsSapEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsSapAddr"),
)
if mibBuilder.loadTexts:
    wfDlsSapEntry.setStatus("mandatory")


class _WfDlsSapDelete_Type(Integer32):
    """Custom type wfDlsSapDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsSapDelete_Type.__name__ = "Integer32"
_WfDlsSapDelete_Object = MibTableColumn
wfDlsSapDelete = _WfDlsSapDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 4, 1, 1),
    _WfDlsSapDelete_Type()
)
wfDlsSapDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsSapDelete.setStatus("mandatory")
_WfDlsSapAddr_Type = Integer32
_WfDlsSapAddr_Object = MibTableColumn
wfDlsSapAddr = _WfDlsSapAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 4, 1, 2),
    _WfDlsSapAddr_Type()
)
wfDlsSapAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsSapAddr.setStatus("mandatory")


class _WfDlsSapCredit_Type(Integer32):
    """Custom type wfDlsSapCredit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 200),
    )


_WfDlsSapCredit_Type.__name__ = "Integer32"
_WfDlsSapCredit_Object = MibTableColumn
wfDlsSapCredit = _WfDlsSapCredit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 4, 1, 3),
    _WfDlsSapCredit_Type()
)
wfDlsSapCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsSapCredit.setStatus("mandatory")
_WfDlsPeerTable_Object = MibTable
wfDlsPeerTable = _WfDlsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5)
)
if mibBuilder.loadTexts:
    wfDlsPeerTable.setStatus("mandatory")
_WfDlsPeerEntry_Object = MibTableRow
wfDlsPeerEntry = _WfDlsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1)
)
wfDlsPeerEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsPeerIpAddr"),
)
if mibBuilder.loadTexts:
    wfDlsPeerEntry.setStatus("mandatory")


class _WfDlsPeerDelete_Type(Integer32):
    """Custom type wfDlsPeerDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsPeerDelete_Type.__name__ = "Integer32"
_WfDlsPeerDelete_Object = MibTableColumn
wfDlsPeerDelete = _WfDlsPeerDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 1),
    _WfDlsPeerDelete_Type()
)
wfDlsPeerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerDelete.setStatus("mandatory")


class _WfDlsPeerState_Type(Integer32):
    """Custom type wfDlsPeerState based on Integer32"""
    defaultValue = 3

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
        *(("backup", 2),
          ("connect", 1),
          ("invalid", 4),
          ("notconn", 3))
    )


_WfDlsPeerState_Type.__name__ = "Integer32"
_WfDlsPeerState_Object = MibTableColumn
wfDlsPeerState = _WfDlsPeerState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 2),
    _WfDlsPeerState_Type()
)
wfDlsPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsPeerState.setStatus("mandatory")
_WfDlsPeerIpAddr_Type = IpAddress
_WfDlsPeerIpAddr_Object = MibTableColumn
wfDlsPeerIpAddr = _WfDlsPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 3),
    _WfDlsPeerIpAddr_Type()
)
wfDlsPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsPeerIpAddr.setStatus("mandatory")


class _WfDlsPeerDefinedBy_Type(Integer32):
    """Custom type wfDlsPeerDefinedBy based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 1),
          ("learned", 2))
    )


_WfDlsPeerDefinedBy_Type.__name__ = "Integer32"
_WfDlsPeerDefinedBy_Object = MibTableColumn
wfDlsPeerDefinedBy = _WfDlsPeerDefinedBy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 4),
    _WfDlsPeerDefinedBy_Type()
)
wfDlsPeerDefinedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsPeerDefinedBy.setStatus("mandatory")


class _WfDlsPeerPPriDisable_Type(Integer32):
    """Custom type wfDlsPeerPPriDisable based on Integer32"""
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


_WfDlsPeerPPriDisable_Type.__name__ = "Integer32"
_WfDlsPeerPPriDisable_Object = MibTableColumn
wfDlsPeerPPriDisable = _WfDlsPeerPPriDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 5),
    _WfDlsPeerPPriDisable_Type()
)
wfDlsPeerPPriDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerPPriDisable.setStatus("mandatory")


class _WfDlsPeerPPriMaxQBuf_Type(Integer32):
    """Custom type wfDlsPeerPPriMaxQBuf based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            50
        )
    )
    namedValues = NamedValues(
        ("default", 50)
    )


_WfDlsPeerPPriMaxQBuf_Type.__name__ = "Integer32"
_WfDlsPeerPPriMaxQBuf_Object = MibTableColumn
wfDlsPeerPPriMaxQBuf = _WfDlsPeerPPriMaxQBuf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 6),
    _WfDlsPeerPPriMaxQBuf_Type()
)
wfDlsPeerPPriMaxQBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerPPriMaxQBuf.setStatus("mandatory")


class _WfDlsPeerPPriMaxQSize_Type(Integer32):
    """Custom type wfDlsPeerPPriMaxQSize based on Integer32"""
    defaultValue = 16000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            16000
        )
    )
    namedValues = NamedValues(
        ("default", 16000)
    )


_WfDlsPeerPPriMaxQSize_Type.__name__ = "Integer32"
_WfDlsPeerPPriMaxQSize_Object = MibTableColumn
wfDlsPeerPPriMaxQSize = _WfDlsPeerPPriMaxQSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 7),
    _WfDlsPeerPPriMaxQSize_Type()
)
wfDlsPeerPPriMaxQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerPPriMaxQSize.setStatus("mandatory")
_WfDlsPeerPPriClearStats_Type = Integer32
_WfDlsPeerPPriClearStats_Object = MibTableColumn
wfDlsPeerPPriClearStats = _WfDlsPeerPPriClearStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 8),
    _WfDlsPeerPPriClearStats_Type()
)
wfDlsPeerPPriClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerPPriClearStats.setStatus("mandatory")


class _WfDlsPeerType_Type(Integer32):
    """Custom type wfDlsPeerType based on Integer32"""
    defaultValue = 6

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
        *(("local", 3),
          ("rfc1434", 2),
          ("rfc1795", 1),
          ("rfc2166", 5),
          ("unknown", 6),
          ("v20unicast", 4))
    )


_WfDlsPeerType_Type.__name__ = "Integer32"
_WfDlsPeerType_Object = MibTableColumn
wfDlsPeerType = _WfDlsPeerType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 9),
    _WfDlsPeerType_Type()
)
wfDlsPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsPeerType.setStatus("mandatory")


class _WfDlsPeerTransportType_Type(Integer32):
    """Custom type wfDlsPeerTransportType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2),
          ("unknown", 3))
    )


_WfDlsPeerTransportType_Type.__name__ = "Integer32"
_WfDlsPeerTransportType_Object = MibTableColumn
wfDlsPeerTransportType = _WfDlsPeerTransportType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 10),
    _WfDlsPeerTransportType_Type()
)
wfDlsPeerTransportType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerTransportType.setStatus("mandatory")


class _WfDlsPeerBackupConfig_Type(Integer32):
    """Custom type wfDlsPeerBackupConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_WfDlsPeerBackupConfig_Type.__name__ = "Integer32"
_WfDlsPeerBackupConfig_Object = MibTableColumn
wfDlsPeerBackupConfig = _WfDlsPeerBackupConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 11),
    _WfDlsPeerBackupConfig_Type()
)
wfDlsPeerBackupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerBackupConfig.setStatus("mandatory")
_WfDlsPeerBackupIpAddr_Type = IpAddress
_WfDlsPeerBackupIpAddr_Object = MibTableColumn
wfDlsPeerBackupIpAddr = _WfDlsPeerBackupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 12),
    _WfDlsPeerBackupIpAddr_Type()
)
wfDlsPeerBackupIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerBackupIpAddr.setStatus("mandatory")


class _WfDlsPeerBackupMaxUpTime_Type(Integer32):
    """Custom type wfDlsPeerBackupMaxUpTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_WfDlsPeerBackupMaxUpTime_Type.__name__ = "Integer32"
_WfDlsPeerBackupMaxUpTime_Object = MibTableColumn
wfDlsPeerBackupMaxUpTime = _WfDlsPeerBackupMaxUpTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 13),
    _WfDlsPeerBackupMaxUpTime_Type()
)
wfDlsPeerBackupMaxUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerBackupMaxUpTime.setStatus("mandatory")


class _WfDlsPeerBackupHoldDownTime_Type(Integer32):
    """Custom type wfDlsPeerBackupHoldDownTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsPeerBackupHoldDownTime_Type.__name__ = "Integer32"
_WfDlsPeerBackupHoldDownTime_Object = MibTableColumn
wfDlsPeerBackupHoldDownTime = _WfDlsPeerBackupHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 14),
    _WfDlsPeerBackupHoldDownTime_Type()
)
wfDlsPeerBackupHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerBackupHoldDownTime.setStatus("mandatory")


class _WfDlsPeerBackupStartTime_Type(Integer32):
    """Custom type wfDlsPeerBackupStartTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2400),
    )


_WfDlsPeerBackupStartTime_Type.__name__ = "Integer32"
_WfDlsPeerBackupStartTime_Object = MibTableColumn
wfDlsPeerBackupStartTime = _WfDlsPeerBackupStartTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 15),
    _WfDlsPeerBackupStartTime_Type()
)
wfDlsPeerBackupStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerBackupStartTime.setStatus("mandatory")


class _WfDlsPeerBackupEndTime_Type(Integer32):
    """Custom type wfDlsPeerBackupEndTime based on Integer32"""
    defaultValue = 2400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2400),
    )


_WfDlsPeerBackupEndTime_Type.__name__ = "Integer32"
_WfDlsPeerBackupEndTime_Object = MibTableColumn
wfDlsPeerBackupEndTime = _WfDlsPeerBackupEndTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 16),
    _WfDlsPeerBackupEndTime_Type()
)
wfDlsPeerBackupEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerBackupEndTime.setStatus("mandatory")


class _WfDlsPeerInteroperability_Type(Integer32):
    """Custom type wfDlsPeerInteroperability based on Integer32"""
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


_WfDlsPeerInteroperability_Type.__name__ = "Integer32"
_WfDlsPeerInteroperability_Object = MibTableColumn
wfDlsPeerInteroperability = _WfDlsPeerInteroperability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 17),
    _WfDlsPeerInteroperability_Type()
)
wfDlsPeerInteroperability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerInteroperability.setStatus("mandatory")


class _WfDlsPeerBackupType_Type(Integer32):
    """Custom type wfDlsPeerBackupType based on Integer32"""
    defaultValue = 3

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
        *(("multicast", 1),
          ("tcp1795", 5),
          ("v20tcp", 4),
          ("v20udp", 2),
          ("v20unknown", 3))
    )


_WfDlsPeerBackupType_Type.__name__ = "Integer32"
_WfDlsPeerBackupType_Object = MibTableColumn
wfDlsPeerBackupType = _WfDlsPeerBackupType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 18),
    _WfDlsPeerBackupType_Type()
)
wfDlsPeerBackupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerBackupType.setStatus("mandatory")


class _WfDlsPeerRsvpMode_Type(Integer32):
    """Custom type wfDlsPeerRsvpMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRsvpForPeer", 2),
          ("useGlobalCfgParams", 3),
          ("usePeerCfgParams", 1))
    )


_WfDlsPeerRsvpMode_Type.__name__ = "Integer32"
_WfDlsPeerRsvpMode_Object = MibTableColumn
wfDlsPeerRsvpMode = _WfDlsPeerRsvpMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 19),
    _WfDlsPeerRsvpMode_Type()
)
wfDlsPeerRsvpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerRsvpMode.setStatus("mandatory")
_WfDlsPeerRsvpSlots_Type = Counter32
_WfDlsPeerRsvpSlots_Object = MibTableColumn
wfDlsPeerRsvpSlots = _WfDlsPeerRsvpSlots_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 20),
    _WfDlsPeerRsvpSlots_Type()
)
wfDlsPeerRsvpSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerRsvpSlots.setStatus("mandatory")


class _WfDlsPeerOutBandwidth_Type(Integer32):
    """Custom type wfDlsPeerOutBandwidth based on Integer32"""
    defaultValue = 0


_WfDlsPeerOutBandwidth_Object = MibTableColumn
wfDlsPeerOutBandwidth = _WfDlsPeerOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 21),
    _WfDlsPeerOutBandwidth_Type()
)
wfDlsPeerOutBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerOutBandwidth.setStatus("mandatory")


class _WfDlsPeerOutBurstSize_Type(Integer32):
    """Custom type wfDlsPeerOutBurstSize based on Integer32"""
    defaultValue = 0


_WfDlsPeerOutBurstSize_Object = MibTableColumn
wfDlsPeerOutBurstSize = _WfDlsPeerOutBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 22),
    _WfDlsPeerOutBurstSize_Type()
)
wfDlsPeerOutBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerOutBurstSize.setStatus("mandatory")


class _WfDlsPeerInBandwidth_Type(Integer32):
    """Custom type wfDlsPeerInBandwidth based on Integer32"""
    defaultValue = 0


_WfDlsPeerInBandwidth_Object = MibTableColumn
wfDlsPeerInBandwidth = _WfDlsPeerInBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 23),
    _WfDlsPeerInBandwidth_Type()
)
wfDlsPeerInBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerInBandwidth.setStatus("mandatory")


class _WfDlsPeerInBurstSize_Type(Integer32):
    """Custom type wfDlsPeerInBurstSize based on Integer32"""
    defaultValue = 0


_WfDlsPeerInBurstSize_Object = MibTableColumn
wfDlsPeerInBurstSize = _WfDlsPeerInBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 24),
    _WfDlsPeerInBurstSize_Type()
)
wfDlsPeerInBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerInBurstSize.setStatus("mandatory")


class _WfDlsPeerNonPeakOutBandwidth_Type(Integer32):
    """Custom type wfDlsPeerNonPeakOutBandwidth based on Integer32"""
    defaultValue = 0


_WfDlsPeerNonPeakOutBandwidth_Object = MibTableColumn
wfDlsPeerNonPeakOutBandwidth = _WfDlsPeerNonPeakOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 25),
    _WfDlsPeerNonPeakOutBandwidth_Type()
)
wfDlsPeerNonPeakOutBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerNonPeakOutBandwidth.setStatus("mandatory")


class _WfDlsPeerNonPeakOutBurstSize_Type(Integer32):
    """Custom type wfDlsPeerNonPeakOutBurstSize based on Integer32"""
    defaultValue = 0


_WfDlsPeerNonPeakOutBurstSize_Object = MibTableColumn
wfDlsPeerNonPeakOutBurstSize = _WfDlsPeerNonPeakOutBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 26),
    _WfDlsPeerNonPeakOutBurstSize_Type()
)
wfDlsPeerNonPeakOutBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerNonPeakOutBurstSize.setStatus("mandatory")


class _WfDlsPeerNonPeakInBandwidth_Type(Integer32):
    """Custom type wfDlsPeerNonPeakInBandwidth based on Integer32"""
    defaultValue = 0


_WfDlsPeerNonPeakInBandwidth_Object = MibTableColumn
wfDlsPeerNonPeakInBandwidth = _WfDlsPeerNonPeakInBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 27),
    _WfDlsPeerNonPeakInBandwidth_Type()
)
wfDlsPeerNonPeakInBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerNonPeakInBandwidth.setStatus("mandatory")


class _WfDlsPeerNonPeakInBurstSize_Type(Integer32):
    """Custom type wfDlsPeerNonPeakInBurstSize based on Integer32"""
    defaultValue = 0


_WfDlsPeerNonPeakInBurstSize_Object = MibTableColumn
wfDlsPeerNonPeakInBurstSize = _WfDlsPeerNonPeakInBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 28),
    _WfDlsPeerNonPeakInBurstSize_Type()
)
wfDlsPeerNonPeakInBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerNonPeakInBurstSize.setStatus("mandatory")


class _WfDlsPeerNonPeakStartTime_Type(Integer32):
    """Custom type wfDlsPeerNonPeakStartTime based on Integer32"""
    defaultValue = 0


_WfDlsPeerNonPeakStartTime_Object = MibTableColumn
wfDlsPeerNonPeakStartTime = _WfDlsPeerNonPeakStartTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 29),
    _WfDlsPeerNonPeakStartTime_Type()
)
wfDlsPeerNonPeakStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerNonPeakStartTime.setStatus("mandatory")


class _WfDlsPeerNonPeakEndTime_Type(Integer32):
    """Custom type wfDlsPeerNonPeakEndTime based on Integer32"""
    defaultValue = 0


_WfDlsPeerNonPeakEndTime_Object = MibTableColumn
wfDlsPeerNonPeakEndTime = _WfDlsPeerNonPeakEndTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 30),
    _WfDlsPeerNonPeakEndTime_Type()
)
wfDlsPeerNonPeakEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerNonPeakEndTime.setStatus("mandatory")
_WfDlsPeerNonPeakStartDays_Type = Counter32
_WfDlsPeerNonPeakStartDays_Object = MibTableColumn
wfDlsPeerNonPeakStartDays = _WfDlsPeerNonPeakStartDays_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 31),
    _WfDlsPeerNonPeakStartDays_Type()
)
wfDlsPeerNonPeakStartDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerNonPeakStartDays.setStatus("mandatory")


class _WfDlsPeerBackupOutBandwidth_Type(Integer32):
    """Custom type wfDlsPeerBackupOutBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsPeerBackupOutBandwidth_Type.__name__ = "Integer32"
_WfDlsPeerBackupOutBandwidth_Object = MibTableColumn
wfDlsPeerBackupOutBandwidth = _WfDlsPeerBackupOutBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 32),
    _WfDlsPeerBackupOutBandwidth_Type()
)
wfDlsPeerBackupOutBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerBackupOutBandwidth.setStatus("mandatory")


class _WfDlsPeerBackupOutBurstSize_Type(Integer32):
    """Custom type wfDlsPeerBackupOutBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsPeerBackupOutBurstSize_Type.__name__ = "Integer32"
_WfDlsPeerBackupOutBurstSize_Object = MibTableColumn
wfDlsPeerBackupOutBurstSize = _WfDlsPeerBackupOutBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 33),
    _WfDlsPeerBackupOutBurstSize_Type()
)
wfDlsPeerBackupOutBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerBackupOutBurstSize.setStatus("mandatory")


class _WfDlsPeerBackupInBandwidth_Type(Integer32):
    """Custom type wfDlsPeerBackupInBandwidth based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsPeerBackupInBandwidth_Type.__name__ = "Integer32"
_WfDlsPeerBackupInBandwidth_Object = MibTableColumn
wfDlsPeerBackupInBandwidth = _WfDlsPeerBackupInBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 34),
    _WfDlsPeerBackupInBandwidth_Type()
)
wfDlsPeerBackupInBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerBackupInBandwidth.setStatus("mandatory")


class _WfDlsPeerBackupInBurstSize_Type(Integer32):
    """Custom type wfDlsPeerBackupInBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsPeerBackupInBurstSize_Type.__name__ = "Integer32"
_WfDlsPeerBackupInBurstSize_Object = MibTableColumn
wfDlsPeerBackupInBurstSize = _WfDlsPeerBackupInBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 5, 1, 35),
    _WfDlsPeerBackupInBurstSize_Type()
)
wfDlsPeerBackupInBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsPeerBackupInBurstSize.setStatus("mandatory")
_WfDlsConnectionTable_Object = MibTable
wfDlsConnectionTable = _WfDlsConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6)
)
if mibBuilder.loadTexts:
    wfDlsConnectionTable.setStatus("mandatory")
_WfDlsConnectionEntry_Object = MibTableRow
wfDlsConnectionEntry = _WfDlsConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1)
)
wfDlsConnectionEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsConnectionCct"),
    (0, "Wellfleet-DLS-MIB", "wfDlsConnectionDstMac"),
    (0, "Wellfleet-DLS-MIB", "wfDlsConnectionSrcMac"),
    (0, "Wellfleet-DLS-MIB", "wfDlsConnectionSaps"),
)
if mibBuilder.loadTexts:
    wfDlsConnectionEntry.setStatus("mandatory")
_WfDlsConnectionCct_Type = Integer32
_WfDlsConnectionCct_Object = MibTableColumn
wfDlsConnectionCct = _WfDlsConnectionCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 1),
    _WfDlsConnectionCct_Type()
)
wfDlsConnectionCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionCct.setStatus("mandatory")


class _WfDlsConnectionDstMac_Type(OctetString):
    """Custom type wfDlsConnectionDstMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfDlsConnectionDstMac_Type.__name__ = "OctetString"
_WfDlsConnectionDstMac_Object = MibTableColumn
wfDlsConnectionDstMac = _WfDlsConnectionDstMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 2),
    _WfDlsConnectionDstMac_Type()
)
wfDlsConnectionDstMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionDstMac.setStatus("mandatory")


class _WfDlsConnectionSrcMac_Type(OctetString):
    """Custom type wfDlsConnectionSrcMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfDlsConnectionSrcMac_Type.__name__ = "OctetString"
_WfDlsConnectionSrcMac_Object = MibTableColumn
wfDlsConnectionSrcMac = _WfDlsConnectionSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 3),
    _WfDlsConnectionSrcMac_Type()
)
wfDlsConnectionSrcMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionSrcMac.setStatus("mandatory")


class _WfDlsConnectionSaps_Type(OctetString):
    """Custom type wfDlsConnectionSaps based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WfDlsConnectionSaps_Type.__name__ = "OctetString"
_WfDlsConnectionSaps_Object = MibTableColumn
wfDlsConnectionSaps = _WfDlsConnectionSaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 4),
    _WfDlsConnectionSaps_Type()
)
wfDlsConnectionSaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionSaps.setStatus("mandatory")


class _WfDlsConnectionState_Type(Integer32):
    """Custom type wfDlsConnectionState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccestab", 2),
          ("connect", 1),
          ("notconn", 3))
    )


_WfDlsConnectionState_Type.__name__ = "Integer32"
_WfDlsConnectionState_Object = MibTableColumn
wfDlsConnectionState = _WfDlsConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 5),
    _WfDlsConnectionState_Type()
)
wfDlsConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionState.setStatus("mandatory")
_WfDlsConnectionRemoteIpAddr_Type = IpAddress
_WfDlsConnectionRemoteIpAddr_Object = MibTableColumn
wfDlsConnectionRemoteIpAddr = _WfDlsConnectionRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 6),
    _WfDlsConnectionRemoteIpAddr_Type()
)
wfDlsConnectionRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionRemoteIpAddr.setStatus("mandatory")
_WfDlsConnectionRemoteRxPort_Type = Integer32
_WfDlsConnectionRemoteRxPort_Object = MibTableColumn
wfDlsConnectionRemoteRxPort = _WfDlsConnectionRemoteRxPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 7),
    _WfDlsConnectionRemoteRxPort_Type()
)
wfDlsConnectionRemoteRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionRemoteRxPort.setStatus("mandatory")
_WfDlsConnectionLocalIpAddr_Type = IpAddress
_WfDlsConnectionLocalIpAddr_Object = MibTableColumn
wfDlsConnectionLocalIpAddr = _WfDlsConnectionLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 8),
    _WfDlsConnectionLocalIpAddr_Type()
)
wfDlsConnectionLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionLocalIpAddr.setStatus("mandatory")
_WfDlsConnectionLocalTxPort_Type = Integer32
_WfDlsConnectionLocalTxPort_Object = MibTableColumn
wfDlsConnectionLocalTxPort = _WfDlsConnectionLocalTxPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 9),
    _WfDlsConnectionLocalTxPort_Type()
)
wfDlsConnectionLocalTxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionLocalTxPort.setStatus("mandatory")
_WfDlsConnectionTxIFrames_Type = Counter32
_WfDlsConnectionTxIFrames_Object = MibTableColumn
wfDlsConnectionTxIFrames = _WfDlsConnectionTxIFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 10),
    _WfDlsConnectionTxIFrames_Type()
)
wfDlsConnectionTxIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionTxIFrames.setStatus("mandatory")
_WfDlsConnectionRxIFrames_Type = Counter32
_WfDlsConnectionRxIFrames_Object = MibTableColumn
wfDlsConnectionRxIFrames = _WfDlsConnectionRxIFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 11),
    _WfDlsConnectionRxIFrames_Type()
)
wfDlsConnectionRxIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionRxIFrames.setStatus("mandatory")
_WfDlsConnectionTxRnrs_Type = Counter32
_WfDlsConnectionTxRnrs_Object = MibTableColumn
wfDlsConnectionTxRnrs = _WfDlsConnectionTxRnrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 12),
    _WfDlsConnectionTxRnrs_Type()
)
wfDlsConnectionTxRnrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionTxRnrs.setStatus("mandatory")
_WfDlsConnectionRxRnrs_Type = Counter32
_WfDlsConnectionRxRnrs_Object = MibTableColumn
wfDlsConnectionRxRnrs = _WfDlsConnectionRxRnrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 13),
    _WfDlsConnectionRxRnrs_Type()
)
wfDlsConnectionRxRnrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionRxRnrs.setStatus("mandatory")
_WfDlsConnectionLocalBlockNum_Type = DisplayString
_WfDlsConnectionLocalBlockNum_Object = MibTableColumn
wfDlsConnectionLocalBlockNum = _WfDlsConnectionLocalBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 14),
    _WfDlsConnectionLocalBlockNum_Type()
)
wfDlsConnectionLocalBlockNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionLocalBlockNum.setStatus("mandatory")
_WfDlsConnectionLocalIdNum_Type = DisplayString
_WfDlsConnectionLocalIdNum_Object = MibTableColumn
wfDlsConnectionLocalIdNum = _WfDlsConnectionLocalIdNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 15),
    _WfDlsConnectionLocalIdNum_Type()
)
wfDlsConnectionLocalIdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionLocalIdNum.setStatus("mandatory")
_WfDlsConnectionLocalCpName_Type = DisplayString
_WfDlsConnectionLocalCpName_Object = MibTableColumn
wfDlsConnectionLocalCpName = _WfDlsConnectionLocalCpName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 16),
    _WfDlsConnectionLocalCpName_Type()
)
wfDlsConnectionLocalCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionLocalCpName.setStatus("mandatory")
_WfDlsConnectionRif_Type = OctetString
_WfDlsConnectionRif_Object = MibTableColumn
wfDlsConnectionRif = _WfDlsConnectionRif_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 17),
    _WfDlsConnectionRif_Type()
)
wfDlsConnectionRif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionRif.setStatus("mandatory")
_WfDlsConnectionRemoteBlockNum_Type = DisplayString
_WfDlsConnectionRemoteBlockNum_Object = MibTableColumn
wfDlsConnectionRemoteBlockNum = _WfDlsConnectionRemoteBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 18),
    _WfDlsConnectionRemoteBlockNum_Type()
)
wfDlsConnectionRemoteBlockNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionRemoteBlockNum.setStatus("mandatory")
_WfDlsConnectionRemoteIdNum_Type = DisplayString
_WfDlsConnectionRemoteIdNum_Object = MibTableColumn
wfDlsConnectionRemoteIdNum = _WfDlsConnectionRemoteIdNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 19),
    _WfDlsConnectionRemoteIdNum_Type()
)
wfDlsConnectionRemoteIdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionRemoteIdNum.setStatus("mandatory")
_WfDlsConnectionRemoteCpName_Type = DisplayString
_WfDlsConnectionRemoteCpName_Object = MibTableColumn
wfDlsConnectionRemoteCpName = _WfDlsConnectionRemoteCpName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 20),
    _WfDlsConnectionRemoteCpName_Type()
)
wfDlsConnectionRemoteCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionRemoteCpName.setStatus("mandatory")


class _WfDlsConnectionLocalDLCorr_Type(OctetString):
    """Custom type wfDlsConnectionLocalDLCorr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfDlsConnectionLocalDLCorr_Type.__name__ = "OctetString"
_WfDlsConnectionLocalDLCorr_Object = MibTableColumn
wfDlsConnectionLocalDLCorr = _WfDlsConnectionLocalDLCorr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 21),
    _WfDlsConnectionLocalDLCorr_Type()
)
wfDlsConnectionLocalDLCorr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionLocalDLCorr.setStatus("mandatory")


class _WfDlsConnectionKilled_Type(Integer32):
    """Custom type wfDlsConnectionKilled based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alive", 1),
          ("dead", 2))
    )


_WfDlsConnectionKilled_Type.__name__ = "Integer32"
_WfDlsConnectionKilled_Object = MibTableColumn
wfDlsConnectionKilled = _WfDlsConnectionKilled_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 22),
    _WfDlsConnectionKilled_Type()
)
wfDlsConnectionKilled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsConnectionKilled.setStatus("mandatory")


class _WfDlsConnectionRemoteDLCorr_Type(OctetString):
    """Custom type wfDlsConnectionRemoteDLCorr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_WfDlsConnectionRemoteDLCorr_Type.__name__ = "OctetString"
_WfDlsConnectionRemoteDLCorr_Object = MibTableColumn
wfDlsConnectionRemoteDLCorr = _WfDlsConnectionRemoteDLCorr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 6, 1, 23),
    _WfDlsConnectionRemoteDLCorr_Type()
)
wfDlsConnectionRemoteDLCorr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsConnectionRemoteDLCorr.setStatus("mandatory")
_WfDlsNbTable_Object = MibTable
wfDlsNbTable = _WfDlsNbTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 7)
)
if mibBuilder.loadTexts:
    wfDlsNbTable.setStatus("mandatory")
_WfDlsNbEntry_Object = MibTableRow
wfDlsNbEntry = _WfDlsNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 7, 1)
)
wfDlsNbEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsNbName"),
)
if mibBuilder.loadTexts:
    wfDlsNbEntry.setStatus("mandatory")


class _WfDlsNbName_Type(OctetString):
    """Custom type wfDlsNbName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_WfDlsNbName_Type.__name__ = "OctetString"
_WfDlsNbName_Object = MibTableColumn
wfDlsNbName = _WfDlsNbName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 7, 1, 1),
    _WfDlsNbName_Type()
)
wfDlsNbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsNbName.setStatus("mandatory")
_WfDlsNbPeerIpAddr_Type = IpAddress
_WfDlsNbPeerIpAddr_Object = MibTableColumn
wfDlsNbPeerIpAddr = _WfDlsNbPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 7, 1, 2),
    _WfDlsNbPeerIpAddr_Type()
)
wfDlsNbPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsNbPeerIpAddr.setStatus("mandatory")
_WfDlsNbCapablePeerIpAddr_Type = IpAddress
_WfDlsNbCapablePeerIpAddr_Object = MibTableColumn
wfDlsNbCapablePeerIpAddr = _WfDlsNbCapablePeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 7, 1, 3),
    _WfDlsNbCapablePeerIpAddr_Type()
)
wfDlsNbCapablePeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsNbCapablePeerIpAddr.setStatus("mandatory")
_WfDlsNbQueries_Type = Counter32
_WfDlsNbQueries_Object = MibTableColumn
wfDlsNbQueries = _WfDlsNbQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 7, 1, 4),
    _WfDlsNbQueries_Type()
)
wfDlsNbQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsNbQueries.setStatus("mandatory")
_WfDlsMacTable_Object = MibTable
wfDlsMacTable = _WfDlsMacTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 8)
)
if mibBuilder.loadTexts:
    wfDlsMacTable.setStatus("mandatory")
_WfDlsMacEntry_Object = MibTableRow
wfDlsMacEntry = _WfDlsMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 8, 1)
)
wfDlsMacEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsMacAddr"),
)
if mibBuilder.loadTexts:
    wfDlsMacEntry.setStatus("mandatory")


class _WfDlsMacAddr_Type(OctetString):
    """Custom type wfDlsMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfDlsMacAddr_Type.__name__ = "OctetString"
_WfDlsMacAddr_Object = MibTableColumn
wfDlsMacAddr = _WfDlsMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 8, 1, 1),
    _WfDlsMacAddr_Type()
)
wfDlsMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsMacAddr.setStatus("mandatory")
_WfDlsMacPeerIpAddr_Type = IpAddress
_WfDlsMacPeerIpAddr_Object = MibTableColumn
wfDlsMacPeerIpAddr = _WfDlsMacPeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 8, 1, 2),
    _WfDlsMacPeerIpAddr_Type()
)
wfDlsMacPeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsMacPeerIpAddr.setStatus("mandatory")
_WfDlsMacCapablePeerIpAddr_Type = IpAddress
_WfDlsMacCapablePeerIpAddr_Object = MibTableColumn
wfDlsMacCapablePeerIpAddr = _WfDlsMacCapablePeerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 8, 1, 3),
    _WfDlsMacCapablePeerIpAddr_Type()
)
wfDlsMacCapablePeerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsMacCapablePeerIpAddr.setStatus("mandatory")
_WfDlsMacQueries_Type = Counter32
_WfDlsMacQueries_Object = MibTableColumn
wfDlsMacQueries = _WfDlsMacQueries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 8, 1, 4),
    _WfDlsMacQueries_Type()
)
wfDlsMacQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsMacQueries.setStatus("mandatory")
_WfDlsTrafficFilterTable_Object = MibTable
wfDlsTrafficFilterTable = _WfDlsTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9)
)
if mibBuilder.loadTexts:
    wfDlsTrafficFilterTable.setStatus("mandatory")
_WfDlsTrafficFilterEntry_Object = MibTableRow
wfDlsTrafficFilterEntry = _WfDlsTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9, 1)
)
wfDlsTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsTrafficFilterCircuit"),
    (0, "Wellfleet-DLS-MIB", "wfDlsTrafficFilterRuleNumber"),
    (0, "Wellfleet-DLS-MIB", "wfDlsTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfDlsTrafficFilterEntry.setStatus("mandatory")


class _WfDlsTrafficFilterCreate_Type(Integer32):
    """Custom type wfDlsTrafficFilterCreate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsTrafficFilterCreate_Type.__name__ = "Integer32"
_WfDlsTrafficFilterCreate_Object = MibTableColumn
wfDlsTrafficFilterCreate = _WfDlsTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9, 1, 1),
    _WfDlsTrafficFilterCreate_Type()
)
wfDlsTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsTrafficFilterCreate.setStatus("mandatory")


class _WfDlsTrafficFilterEnable_Type(Integer32):
    """Custom type wfDlsTrafficFilterEnable based on Integer32"""
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


_WfDlsTrafficFilterEnable_Type.__name__ = "Integer32"
_WfDlsTrafficFilterEnable_Object = MibTableColumn
wfDlsTrafficFilterEnable = _WfDlsTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9, 1, 2),
    _WfDlsTrafficFilterEnable_Type()
)
wfDlsTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsTrafficFilterEnable.setStatus("mandatory")


class _WfDlsTrafficFilterStatus_Type(Integer32):
    """Custom type wfDlsTrafficFilterStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfDlsTrafficFilterStatus_Type.__name__ = "Integer32"
_WfDlsTrafficFilterStatus_Object = MibTableColumn
wfDlsTrafficFilterStatus = _WfDlsTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9, 1, 3),
    _WfDlsTrafficFilterStatus_Type()
)
wfDlsTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsTrafficFilterStatus.setStatus("mandatory")
_WfDlsTrafficFilterCounter_Type = Counter32
_WfDlsTrafficFilterCounter_Object = MibTableColumn
wfDlsTrafficFilterCounter = _WfDlsTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9, 1, 4),
    _WfDlsTrafficFilterCounter_Type()
)
wfDlsTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsTrafficFilterCounter.setStatus("mandatory")
_WfDlsTrafficFilterDefinition_Type = OctetString
_WfDlsTrafficFilterDefinition_Object = MibTableColumn
wfDlsTrafficFilterDefinition = _WfDlsTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9, 1, 5),
    _WfDlsTrafficFilterDefinition_Type()
)
wfDlsTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsTrafficFilterDefinition.setStatus("mandatory")
_WfDlsTrafficFilterReserved_Type = Integer32
_WfDlsTrafficFilterReserved_Object = MibTableColumn
wfDlsTrafficFilterReserved = _WfDlsTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9, 1, 6),
    _WfDlsTrafficFilterReserved_Type()
)
wfDlsTrafficFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsTrafficFilterReserved.setStatus("mandatory")
_WfDlsTrafficFilterCircuit_Type = Integer32
_WfDlsTrafficFilterCircuit_Object = MibTableColumn
wfDlsTrafficFilterCircuit = _WfDlsTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9, 1, 7),
    _WfDlsTrafficFilterCircuit_Type()
)
wfDlsTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsTrafficFilterCircuit.setStatus("mandatory")
_WfDlsTrafficFilterRuleNumber_Type = Integer32
_WfDlsTrafficFilterRuleNumber_Object = MibTableColumn
wfDlsTrafficFilterRuleNumber = _WfDlsTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9, 1, 8),
    _WfDlsTrafficFilterRuleNumber_Type()
)
wfDlsTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsTrafficFilterRuleNumber.setStatus("mandatory")
_WfDlsTrafficFilterFragment_Type = Integer32
_WfDlsTrafficFilterFragment_Object = MibTableColumn
wfDlsTrafficFilterFragment = _WfDlsTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9, 1, 9),
    _WfDlsTrafficFilterFragment_Type()
)
wfDlsTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsTrafficFilterFragment.setStatus("mandatory")
_WfDlsTrafficFilterName_Type = DisplayString
_WfDlsTrafficFilterName_Object = MibTableColumn
wfDlsTrafficFilterName = _WfDlsTrafficFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 9, 1, 10),
    _WfDlsTrafficFilterName_Type()
)
wfDlsTrafficFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsTrafficFilterName.setStatus("mandatory")
_WfDlsDefaultMacTable_Object = MibTable
wfDlsDefaultMacTable = _WfDlsDefaultMacTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 10)
)
if mibBuilder.loadTexts:
    wfDlsDefaultMacTable.setStatus("mandatory")
_WfDlsDefaultMacEntry_Object = MibTableRow
wfDlsDefaultMacEntry = _WfDlsDefaultMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 10, 1)
)
wfDlsDefaultMacEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsDefaultMacAddr"),
)
if mibBuilder.loadTexts:
    wfDlsDefaultMacEntry.setStatus("mandatory")


class _WfDlsDefaultMacDelete_Type(Integer32):
    """Custom type wfDlsDefaultMacDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsDefaultMacDelete_Type.__name__ = "Integer32"
_WfDlsDefaultMacDelete_Object = MibTableColumn
wfDlsDefaultMacDelete = _WfDlsDefaultMacDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 10, 1, 1),
    _WfDlsDefaultMacDelete_Type()
)
wfDlsDefaultMacDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsDefaultMacDelete.setStatus("mandatory")


class _WfDlsDefaultMacAddr_Type(OctetString):
    """Custom type wfDlsDefaultMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfDlsDefaultMacAddr_Type.__name__ = "OctetString"
_WfDlsDefaultMacAddr_Object = MibTableColumn
wfDlsDefaultMacAddr = _WfDlsDefaultMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 10, 1, 2),
    _WfDlsDefaultMacAddr_Type()
)
wfDlsDefaultMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsDefaultMacAddr.setStatus("mandatory")
_WfDlsDefaultMacPeerIp_Type = IpAddress
_WfDlsDefaultMacPeerIp_Object = MibTableColumn
wfDlsDefaultMacPeerIp = _WfDlsDefaultMacPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 10, 1, 3),
    _WfDlsDefaultMacPeerIp_Type()
)
wfDlsDefaultMacPeerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsDefaultMacPeerIp.setStatus("mandatory")
_WfDlsDefaultNbTable_Object = MibTable
wfDlsDefaultNbTable = _WfDlsDefaultNbTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 11)
)
if mibBuilder.loadTexts:
    wfDlsDefaultNbTable.setStatus("mandatory")
_WfDlsDefaultNbEntry_Object = MibTableRow
wfDlsDefaultNbEntry = _WfDlsDefaultNbEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 11, 1)
)
wfDlsDefaultNbEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsDefaultNbName"),
)
if mibBuilder.loadTexts:
    wfDlsDefaultNbEntry.setStatus("mandatory")


class _WfDlsDefaultNbDelete_Type(Integer32):
    """Custom type wfDlsDefaultNbDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsDefaultNbDelete_Type.__name__ = "Integer32"
_WfDlsDefaultNbDelete_Object = MibTableColumn
wfDlsDefaultNbDelete = _WfDlsDefaultNbDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 11, 1, 1),
    _WfDlsDefaultNbDelete_Type()
)
wfDlsDefaultNbDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsDefaultNbDelete.setStatus("mandatory")


class _WfDlsDefaultNbName_Type(OctetString):
    """Custom type wfDlsDefaultNbName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_WfDlsDefaultNbName_Type.__name__ = "OctetString"
_WfDlsDefaultNbName_Object = MibTableColumn
wfDlsDefaultNbName = _WfDlsDefaultNbName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 11, 1, 2),
    _WfDlsDefaultNbName_Type()
)
wfDlsDefaultNbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsDefaultNbName.setStatus("mandatory")
_WfDlsDefaultNbPeerIp_Type = IpAddress
_WfDlsDefaultNbPeerIp_Object = MibTableColumn
wfDlsDefaultNbPeerIp = _WfDlsDefaultNbPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 11, 1, 3),
    _WfDlsDefaultNbPeerIp_Type()
)
wfDlsDefaultNbPeerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsDefaultNbPeerIp.setStatus("mandatory")
_WfDlsLocalDeviceTable_Object = MibTable
wfDlsLocalDeviceTable = _WfDlsLocalDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12)
)
if mibBuilder.loadTexts:
    wfDlsLocalDeviceTable.setStatus("mandatory")
_WfDlsLocalDeviceEntry_Object = MibTableRow
wfDlsLocalDeviceEntry = _WfDlsLocalDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1)
)
wfDlsLocalDeviceEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsLocalDeviceCct"),
    (0, "Wellfleet-DLS-MIB", "wfDlsLocalDeviceAddr"),
)
if mibBuilder.loadTexts:
    wfDlsLocalDeviceEntry.setStatus("mandatory")


class _WfDlsLocalDeviceDelete_Type(Integer32):
    """Custom type wfDlsLocalDeviceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsLocalDeviceDelete_Type.__name__ = "Integer32"
_WfDlsLocalDeviceDelete_Object = MibTableColumn
wfDlsLocalDeviceDelete = _WfDlsLocalDeviceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 1),
    _WfDlsLocalDeviceDelete_Type()
)
wfDlsLocalDeviceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceDelete.setStatus("mandatory")


class _WfDlsLocalDeviceDisable_Type(Integer32):
    """Custom type wfDlsLocalDeviceDisable based on Integer32"""
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


_WfDlsLocalDeviceDisable_Type.__name__ = "Integer32"
_WfDlsLocalDeviceDisable_Object = MibTableColumn
wfDlsLocalDeviceDisable = _WfDlsLocalDeviceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 2),
    _WfDlsLocalDeviceDisable_Type()
)
wfDlsLocalDeviceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceDisable.setStatus("mandatory")


class _WfDlsLocalDeviceState_Type(Integer32):
    """Custom type wfDlsLocalDeviceState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfDlsLocalDeviceState_Type.__name__ = "Integer32"
_WfDlsLocalDeviceState_Object = MibTableColumn
wfDlsLocalDeviceState = _WfDlsLocalDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 3),
    _WfDlsLocalDeviceState_Type()
)
wfDlsLocalDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceState.setStatus("mandatory")
_WfDlsLocalDeviceCct_Type = Integer32
_WfDlsLocalDeviceCct_Object = MibTableColumn
wfDlsLocalDeviceCct = _WfDlsLocalDeviceCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 4),
    _WfDlsLocalDeviceCct_Type()
)
wfDlsLocalDeviceCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceCct.setStatus("mandatory")
_WfDlsLocalDeviceAddr_Type = Integer32
_WfDlsLocalDeviceAddr_Object = MibTableColumn
wfDlsLocalDeviceAddr = _WfDlsLocalDeviceAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 5),
    _WfDlsLocalDeviceAddr_Type()
)
wfDlsLocalDeviceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceAddr.setStatus("mandatory")
_WfDlsLocalDeviceSourceMac_Type = OctetString
_WfDlsLocalDeviceSourceMac_Object = MibTableColumn
wfDlsLocalDeviceSourceMac = _WfDlsLocalDeviceSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 6),
    _WfDlsLocalDeviceSourceMac_Type()
)
wfDlsLocalDeviceSourceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceSourceMac.setStatus("mandatory")


class _WfDlsLocalDeviceSourceSap_Type(Integer32):
    """Custom type wfDlsLocalDeviceSourceSap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_WfDlsLocalDeviceSourceSap_Type.__name__ = "Integer32"
_WfDlsLocalDeviceSourceSap_Object = MibTableColumn
wfDlsLocalDeviceSourceSap = _WfDlsLocalDeviceSourceSap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 7),
    _WfDlsLocalDeviceSourceSap_Type()
)
wfDlsLocalDeviceSourceSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceSourceSap.setStatus("mandatory")
_WfDlsLocalDeviceDestMac_Type = OctetString
_WfDlsLocalDeviceDestMac_Object = MibTableColumn
wfDlsLocalDeviceDestMac = _WfDlsLocalDeviceDestMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 8),
    _WfDlsLocalDeviceDestMac_Type()
)
wfDlsLocalDeviceDestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceDestMac.setStatus("mandatory")


class _WfDlsLocalDeviceDestSap_Type(Integer32):
    """Custom type wfDlsLocalDeviceDestSap based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_WfDlsLocalDeviceDestSap_Type.__name__ = "Integer32"
_WfDlsLocalDeviceDestSap_Object = MibTableColumn
wfDlsLocalDeviceDestSap = _WfDlsLocalDeviceDestSap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 9),
    _WfDlsLocalDeviceDestSap_Type()
)
wfDlsLocalDeviceDestSap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceDestSap.setStatus("mandatory")
_WfDlsLocalDeviceXidValue_Type = OctetString
_WfDlsLocalDeviceXidValue_Object = MibTableColumn
wfDlsLocalDeviceXidValue = _WfDlsLocalDeviceXidValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 10),
    _WfDlsLocalDeviceXidValue_Type()
)
wfDlsLocalDeviceXidValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceXidValue.setStatus("mandatory")


class _WfDlsLocalDeviceCanureachTimer_Type(Integer32):
    """Custom type wfDlsLocalDeviceCanureachTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WfDlsLocalDeviceCanureachTimer_Type.__name__ = "Integer32"
_WfDlsLocalDeviceCanureachTimer_Object = MibTableColumn
wfDlsLocalDeviceCanureachTimer = _WfDlsLocalDeviceCanureachTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 11),
    _WfDlsLocalDeviceCanureachTimer_Type()
)
wfDlsLocalDeviceCanureachTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceCanureachTimer.setStatus("mandatory")


class _WfDlsLocalDeviceCanureachRetries_Type(Gauge32):
    """Custom type wfDlsLocalDeviceCanureachRetries based on Gauge32"""
    defaultValue = 10

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfDlsLocalDeviceCanureachRetries_Type.__name__ = "Gauge32"
_WfDlsLocalDeviceCanureachRetries_Object = MibTableColumn
wfDlsLocalDeviceCanureachRetries = _WfDlsLocalDeviceCanureachRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 12),
    _WfDlsLocalDeviceCanureachRetries_Type()
)
wfDlsLocalDeviceCanureachRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceCanureachRetries.setStatus("mandatory")


class _WfDlsLocalDeviceLSTimer_Type(Integer32):
    """Custom type wfDlsLocalDeviceLSTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_WfDlsLocalDeviceLSTimer_Type.__name__ = "Integer32"
_WfDlsLocalDeviceLSTimer_Object = MibTableColumn
wfDlsLocalDeviceLSTimer = _WfDlsLocalDeviceLSTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 13),
    _WfDlsLocalDeviceLSTimer_Type()
)
wfDlsLocalDeviceLSTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceLSTimer.setStatus("mandatory")


class _WfDlsLocalDeviceLSRetries_Type(Gauge32):
    """Custom type wfDlsLocalDeviceLSRetries based on Gauge32"""
    defaultValue = 10

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfDlsLocalDeviceLSRetries_Type.__name__ = "Gauge32"
_WfDlsLocalDeviceLSRetries_Object = MibTableColumn
wfDlsLocalDeviceLSRetries = _WfDlsLocalDeviceLSRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 14),
    _WfDlsLocalDeviceLSRetries_Type()
)
wfDlsLocalDeviceLSRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceLSRetries.setStatus("mandatory")


class _WfDlsLocalDeviceRcvCredit_Type(Integer32):
    """Custom type wfDlsLocalDeviceRcvCredit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_WfDlsLocalDeviceRcvCredit_Type.__name__ = "Integer32"
_WfDlsLocalDeviceRcvCredit_Object = MibTableColumn
wfDlsLocalDeviceRcvCredit = _WfDlsLocalDeviceRcvCredit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 15),
    _WfDlsLocalDeviceRcvCredit_Type()
)
wfDlsLocalDeviceRcvCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceRcvCredit.setStatus("mandatory")


class _WfDlsLocalDeviceTxCredit_Type(Integer32):
    """Custom type wfDlsLocalDeviceTxCredit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_WfDlsLocalDeviceTxCredit_Type.__name__ = "Integer32"
_WfDlsLocalDeviceTxCredit_Object = MibTableColumn
wfDlsLocalDeviceTxCredit = _WfDlsLocalDeviceTxCredit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 16),
    _WfDlsLocalDeviceTxCredit_Type()
)
wfDlsLocalDeviceTxCredit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceTxCredit.setStatus("mandatory")


class _WfDlsLocalDeviceCurTimer2_Type(Integer32):
    """Custom type wfDlsLocalDeviceCurTimer2 based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsLocalDeviceCurTimer2_Type.__name__ = "Integer32"
_WfDlsLocalDeviceCurTimer2_Object = MibTableColumn
wfDlsLocalDeviceCurTimer2 = _WfDlsLocalDeviceCurTimer2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 17),
    _WfDlsLocalDeviceCurTimer2_Type()
)
wfDlsLocalDeviceCurTimer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceCurTimer2.setStatus("mandatory")


class _WfDlsLocalDeviceCurRetries2_Type(Gauge32):
    """Custom type wfDlsLocalDeviceCurRetries2 based on Gauge32"""
    defaultValue = 4294967295

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfDlsLocalDeviceCurRetries2_Type.__name__ = "Gauge32"
_WfDlsLocalDeviceCurRetries2_Object = MibTableColumn
wfDlsLocalDeviceCurRetries2 = _WfDlsLocalDeviceCurRetries2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 18),
    _WfDlsLocalDeviceCurRetries2_Type()
)
wfDlsLocalDeviceCurRetries2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceCurRetries2.setStatus("mandatory")


class _WfDlsLocalDeviceEnableXidPassthru_Type(Integer32):
    """Custom type wfDlsLocalDeviceEnableXidPassthru based on Integer32"""
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


_WfDlsLocalDeviceEnableXidPassthru_Type.__name__ = "Integer32"
_WfDlsLocalDeviceEnableXidPassthru_Object = MibTableColumn
wfDlsLocalDeviceEnableXidPassthru = _WfDlsLocalDeviceEnableXidPassthru_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 19),
    _WfDlsLocalDeviceEnableXidPassthru_Type()
)
wfDlsLocalDeviceEnableXidPassthru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceEnableXidPassthru.setStatus("mandatory")


class _WfDlsLocalDeviceActivationSequence_Type(Integer32):
    """Custom type wfDlsLocalDeviceActivationSequence based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("localdevicefirst", 1),
          ("peerfirst", 2))
    )


_WfDlsLocalDeviceActivationSequence_Type.__name__ = "Integer32"
_WfDlsLocalDeviceActivationSequence_Object = MibTableColumn
wfDlsLocalDeviceActivationSequence = _WfDlsLocalDeviceActivationSequence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 12, 1, 20),
    _WfDlsLocalDeviceActivationSequence_Type()
)
wfDlsLocalDeviceActivationSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalDeviceActivationSequence.setStatus("mandatory")
_WfDlsLocalCircuitTable_Object = MibTable
wfDlsLocalCircuitTable = _WfDlsLocalCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 13)
)
if mibBuilder.loadTexts:
    wfDlsLocalCircuitTable.setStatus("mandatory")
_WfDlsLocalCircuitEntry_Object = MibTableRow
wfDlsLocalCircuitEntry = _WfDlsLocalCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 13, 1)
)
wfDlsLocalCircuitEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsLocalCircuitCct"),
)
if mibBuilder.loadTexts:
    wfDlsLocalCircuitEntry.setStatus("mandatory")


class _WfDlsLocalCircuitDelete_Type(Integer32):
    """Custom type wfDlsLocalCircuitDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsLocalCircuitDelete_Type.__name__ = "Integer32"
_WfDlsLocalCircuitDelete_Object = MibTableColumn
wfDlsLocalCircuitDelete = _WfDlsLocalCircuitDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 13, 1, 1),
    _WfDlsLocalCircuitDelete_Type()
)
wfDlsLocalCircuitDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalCircuitDelete.setStatus("mandatory")


class _WfDlsLocalCircuitDisable_Type(Integer32):
    """Custom type wfDlsLocalCircuitDisable based on Integer32"""
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


_WfDlsLocalCircuitDisable_Type.__name__ = "Integer32"
_WfDlsLocalCircuitDisable_Object = MibTableColumn
wfDlsLocalCircuitDisable = _WfDlsLocalCircuitDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 13, 1, 2),
    _WfDlsLocalCircuitDisable_Type()
)
wfDlsLocalCircuitDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalCircuitDisable.setStatus("mandatory")


class _WfDlsLocalCircuitState_Type(Integer32):
    """Custom type wfDlsLocalCircuitState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfDlsLocalCircuitState_Type.__name__ = "Integer32"
_WfDlsLocalCircuitState_Object = MibTableColumn
wfDlsLocalCircuitState = _WfDlsLocalCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 13, 1, 3),
    _WfDlsLocalCircuitState_Type()
)
wfDlsLocalCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsLocalCircuitState.setStatus("mandatory")
_WfDlsLocalCircuitCct_Type = Integer32
_WfDlsLocalCircuitCct_Object = MibTableColumn
wfDlsLocalCircuitCct = _WfDlsLocalCircuitCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 13, 1, 4),
    _WfDlsLocalCircuitCct_Type()
)
wfDlsLocalCircuitCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalCircuitCct.setStatus("mandatory")
_WfDlsLocalCircuitClientCount_Type = Integer32
_WfDlsLocalCircuitClientCount_Object = MibTableColumn
wfDlsLocalCircuitClientCount = _WfDlsLocalCircuitClientCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 13, 1, 5),
    _WfDlsLocalCircuitClientCount_Type()
)
wfDlsLocalCircuitClientCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsLocalCircuitClientCount.setStatus("mandatory")
_WfDlsLocalCircuitFrameCount_Type = Integer32
_WfDlsLocalCircuitFrameCount_Object = MibTableColumn
wfDlsLocalCircuitFrameCount = _WfDlsLocalCircuitFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 13, 1, 6),
    _WfDlsLocalCircuitFrameCount_Type()
)
wfDlsLocalCircuitFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsLocalCircuitFrameCount.setStatus("mandatory")
_WfDlsLocalCircuitSlot_Type = Integer32
_WfDlsLocalCircuitSlot_Object = MibTableColumn
wfDlsLocalCircuitSlot = _WfDlsLocalCircuitSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 13, 1, 7),
    _WfDlsLocalCircuitSlot_Type()
)
wfDlsLocalCircuitSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalCircuitSlot.setStatus("mandatory")
_WfDlsLocalCctDefaultMac_Type = OctetString
_WfDlsLocalCctDefaultMac_Object = MibTableColumn
wfDlsLocalCctDefaultMac = _WfDlsLocalCctDefaultMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 13, 1, 8),
    _WfDlsLocalCctDefaultMac_Type()
)
wfDlsLocalCctDefaultMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsLocalCctDefaultMac.setStatus("mandatory")
_WfDlsGenToolTable_Object = MibTable
wfDlsGenToolTable = _WfDlsGenToolTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14)
)
if mibBuilder.loadTexts:
    wfDlsGenToolTable.setStatus("mandatory")
_WfDlsGenToolEntry_Object = MibTableRow
wfDlsGenToolEntry = _WfDlsGenToolEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1)
)
wfDlsGenToolEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsSlotNumber"),
)
if mibBuilder.loadTexts:
    wfDlsGenToolEntry.setStatus("mandatory")


class _WfDlsGenDelete_Type(Integer32):
    """Custom type wfDlsGenDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsGenDelete_Type.__name__ = "Integer32"
_WfDlsGenDelete_Object = MibTableColumn
wfDlsGenDelete = _WfDlsGenDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1, 1),
    _WfDlsGenDelete_Type()
)
wfDlsGenDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsGenDelete.setStatus("mandatory")


class _WfDlsGenDisable_Type(Integer32):
    """Custom type wfDlsGenDisable based on Integer32"""
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


_WfDlsGenDisable_Type.__name__ = "Integer32"
_WfDlsGenDisable_Object = MibTableColumn
wfDlsGenDisable = _WfDlsGenDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1, 2),
    _WfDlsGenDisable_Type()
)
wfDlsGenDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsGenDisable.setStatus("mandatory")


class _WfDlsGenDefaultSessions_Type(Integer32):
    """Custom type wfDlsGenDefaultSessions based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 10000),
    )


_WfDlsGenDefaultSessions_Type.__name__ = "Integer32"
_WfDlsGenDefaultSessions_Object = MibTableColumn
wfDlsGenDefaultSessions = _WfDlsGenDefaultSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1, 3),
    _WfDlsGenDefaultSessions_Type()
)
wfDlsGenDefaultSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsGenDefaultSessions.setStatus("mandatory")


class _WfDlsGenStartupTime_Type(Integer32):
    """Custom type wfDlsGenStartupTime based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 100000),
    )


_WfDlsGenStartupTime_Type.__name__ = "Integer32"
_WfDlsGenStartupTime_Object = MibTableColumn
wfDlsGenStartupTime = _WfDlsGenStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1, 4),
    _WfDlsGenStartupTime_Type()
)
wfDlsGenStartupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsGenStartupTime.setStatus("mandatory")


class _WfDlsGenIFramePerSec_Type(Integer32):
    """Custom type wfDlsGenIFramePerSec based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WfDlsGenIFramePerSec_Type.__name__ = "Integer32"
_WfDlsGenIFramePerSec_Object = MibTableColumn
wfDlsGenIFramePerSec = _WfDlsGenIFramePerSec_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1, 5),
    _WfDlsGenIFramePerSec_Type()
)
wfDlsGenIFramePerSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsGenIFramePerSec.setStatus("mandatory")


class _WfDlsGenMacAddrOffset_Type(Integer32):
    """Custom type wfDlsGenMacAddrOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_WfDlsGenMacAddrOffset_Type.__name__ = "Integer32"
_WfDlsGenMacAddrOffset_Object = MibTableColumn
wfDlsGenMacAddrOffset = _WfDlsGenMacAddrOffset_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1, 6),
    _WfDlsGenMacAddrOffset_Type()
)
wfDlsGenMacAddrOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsGenMacAddrOffset.setStatus("mandatory")


class _WfDlsGenVariableDstMAC_Type(Integer32):
    """Custom type wfDlsGenVariableDstMAC based on Integer32"""
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


_WfDlsGenVariableDstMAC_Type.__name__ = "Integer32"
_WfDlsGenVariableDstMAC_Object = MibTableColumn
wfDlsGenVariableDstMAC = _WfDlsGenVariableDstMAC_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1, 7),
    _WfDlsGenVariableDstMAC_Type()
)
wfDlsGenVariableDstMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsGenVariableDstMAC.setStatus("mandatory")


class _WfDlsGenDefaultUpperMAC_Type(Integer32):
    """Custom type wfDlsGenDefaultUpperMAC based on Integer32"""
    defaultValue = 1079705600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147418112),
    )


_WfDlsGenDefaultUpperMAC_Type.__name__ = "Integer32"
_WfDlsGenDefaultUpperMAC_Object = MibTableColumn
wfDlsGenDefaultUpperMAC = _WfDlsGenDefaultUpperMAC_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1, 8),
    _WfDlsGenDefaultUpperMAC_Type()
)
wfDlsGenDefaultUpperMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsGenDefaultUpperMAC.setStatus("mandatory")


class _WfDlsGenDataLength_Type(Integer32):
    """Custom type wfDlsGenDataLength based on Integer32"""
    defaultValue = 250

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2052),
    )


_WfDlsGenDataLength_Type.__name__ = "Integer32"
_WfDlsGenDataLength_Object = MibTableColumn
wfDlsGenDataLength = _WfDlsGenDataLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1, 9),
    _WfDlsGenDataLength_Type()
)
wfDlsGenDataLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsGenDataLength.setStatus("mandatory")


class _WfDlsGenNumSapPerMac_Type(Integer32):
    """Custom type wfDlsGenNumSapPerMac based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfDlsGenNumSapPerMac_Type.__name__ = "Integer32"
_WfDlsGenNumSapPerMac_Object = MibTableColumn
wfDlsGenNumSapPerMac = _WfDlsGenNumSapPerMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1, 10),
    _WfDlsGenNumSapPerMac_Type()
)
wfDlsGenNumSapPerMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsGenNumSapPerMac.setStatus("mandatory")


class _WfDlsGenSapIncrement_Type(Integer32):
    """Custom type wfDlsGenSapIncrement based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfDlsGenSapIncrement_Type.__name__ = "Integer32"
_WfDlsGenSapIncrement_Object = MibTableColumn
wfDlsGenSapIncrement = _WfDlsGenSapIncrement_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 14, 1, 11),
    _WfDlsGenSapIncrement_Type()
)
wfDlsGenSapIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsGenSapIncrement.setStatus("mandatory")
_WfDlsMcastIpTable_Object = MibTable
wfDlsMcastIpTable = _WfDlsMcastIpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15)
)
if mibBuilder.loadTexts:
    wfDlsMcastIpTable.setStatus("mandatory")
_WfDlsMcastIpEntry_Object = MibTableRow
wfDlsMcastIpEntry = _WfDlsMcastIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1)
)
wfDlsMcastIpEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsMcastIpAddr"),
)
if mibBuilder.loadTexts:
    wfDlsMcastIpEntry.setStatus("mandatory")


class _WfDlsMcastIpDelete_Type(Integer32):
    """Custom type wfDlsMcastIpDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsMcastIpDelete_Type.__name__ = "Integer32"
_WfDlsMcastIpDelete_Object = MibTableColumn
wfDlsMcastIpDelete = _WfDlsMcastIpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1, 1),
    _WfDlsMcastIpDelete_Type()
)
wfDlsMcastIpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMcastIpDelete.setStatus("mandatory")


class _WfDlsMcastIpState_Type(Integer32):
    """Custom type wfDlsMcastIpState based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("notpresent", 3))
    )


_WfDlsMcastIpState_Type.__name__ = "Integer32"
_WfDlsMcastIpState_Object = MibTableColumn
wfDlsMcastIpState = _WfDlsMcastIpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1, 2),
    _WfDlsMcastIpState_Type()
)
wfDlsMcastIpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsMcastIpState.setStatus("mandatory")
_WfDlsMcastIpAddr_Type = IpAddress
_WfDlsMcastIpAddr_Object = MibTableColumn
wfDlsMcastIpAddr = _WfDlsMcastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1, 3),
    _WfDlsMcastIpAddr_Type()
)
wfDlsMcastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsMcastIpAddr.setStatus("mandatory")


class _WfDlsMcastIpSlots_Type(Gauge32):
    """Custom type wfDlsMcastIpSlots based on Gauge32"""
    defaultValue = 4294705152

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfDlsMcastIpSlots_Type.__name__ = "Gauge32"
_WfDlsMcastIpSlots_Object = MibTableColumn
wfDlsMcastIpSlots = _WfDlsMcastIpSlots_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1, 4),
    _WfDlsMcastIpSlots_Type()
)
wfDlsMcastIpSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMcastIpSlots.setStatus("mandatory")


class _WfDlsMcastIpBackupConfig_Type(Integer32):
    """Custom type wfDlsMcastIpBackupConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_WfDlsMcastIpBackupConfig_Type.__name__ = "Integer32"
_WfDlsMcastIpBackupConfig_Object = MibTableColumn
wfDlsMcastIpBackupConfig = _WfDlsMcastIpBackupConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1, 5),
    _WfDlsMcastIpBackupConfig_Type()
)
wfDlsMcastIpBackupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMcastIpBackupConfig.setStatus("mandatory")
_WfDlsMcastIpBackupIpAddr_Type = IpAddress
_WfDlsMcastIpBackupIpAddr_Object = MibTableColumn
wfDlsMcastIpBackupIpAddr = _WfDlsMcastIpBackupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1, 6),
    _WfDlsMcastIpBackupIpAddr_Type()
)
wfDlsMcastIpBackupIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMcastIpBackupIpAddr.setStatus("mandatory")


class _WfDlsMcastIpBackupMaxUpTime_Type(Integer32):
    """Custom type wfDlsMcastIpBackupMaxUpTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999),
    )


_WfDlsMcastIpBackupMaxUpTime_Type.__name__ = "Integer32"
_WfDlsMcastIpBackupMaxUpTime_Object = MibTableColumn
wfDlsMcastIpBackupMaxUpTime = _WfDlsMcastIpBackupMaxUpTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1, 7),
    _WfDlsMcastIpBackupMaxUpTime_Type()
)
wfDlsMcastIpBackupMaxUpTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMcastIpBackupMaxUpTime.setStatus("mandatory")


class _WfDlsMcastIpBackupHoldDownTime_Type(Integer32):
    """Custom type wfDlsMcastIpBackupHoldDownTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfDlsMcastIpBackupHoldDownTime_Type.__name__ = "Integer32"
_WfDlsMcastIpBackupHoldDownTime_Object = MibTableColumn
wfDlsMcastIpBackupHoldDownTime = _WfDlsMcastIpBackupHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1, 8),
    _WfDlsMcastIpBackupHoldDownTime_Type()
)
wfDlsMcastIpBackupHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMcastIpBackupHoldDownTime.setStatus("mandatory")


class _WfDlsMcastIpBackupStartTime_Type(Integer32):
    """Custom type wfDlsMcastIpBackupStartTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2400),
    )


_WfDlsMcastIpBackupStartTime_Type.__name__ = "Integer32"
_WfDlsMcastIpBackupStartTime_Object = MibTableColumn
wfDlsMcastIpBackupStartTime = _WfDlsMcastIpBackupStartTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1, 9),
    _WfDlsMcastIpBackupStartTime_Type()
)
wfDlsMcastIpBackupStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMcastIpBackupStartTime.setStatus("mandatory")


class _WfDlsMcastIpBackupEndTime_Type(Integer32):
    """Custom type wfDlsMcastIpBackupEndTime based on Integer32"""
    defaultValue = 2400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2400),
    )


_WfDlsMcastIpBackupEndTime_Type.__name__ = "Integer32"
_WfDlsMcastIpBackupEndTime_Object = MibTableColumn
wfDlsMcastIpBackupEndTime = _WfDlsMcastIpBackupEndTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1, 10),
    _WfDlsMcastIpBackupEndTime_Type()
)
wfDlsMcastIpBackupEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMcastIpBackupEndTime.setStatus("mandatory")


class _WfDlsMcastIpBackupType_Type(Integer32):
    """Custom type wfDlsMcastIpBackupType based on Integer32"""
    defaultValue = 3

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
        *(("multicast", 1),
          ("tcp1795", 5),
          ("v20tcp", 4),
          ("v20udp", 2),
          ("v20unknown", 3))
    )


_WfDlsMcastIpBackupType_Type.__name__ = "Integer32"
_WfDlsMcastIpBackupType_Object = MibTableColumn
wfDlsMcastIpBackupType = _WfDlsMcastIpBackupType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 15, 1, 11),
    _WfDlsMcastIpBackupType_Type()
)
wfDlsMcastIpBackupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsMcastIpBackupType.setStatus("mandatory")
_WfDlsTranslateMacTable_Object = MibTable
wfDlsTranslateMacTable = _WfDlsTranslateMacTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 16)
)
if mibBuilder.loadTexts:
    wfDlsTranslateMacTable.setStatus("mandatory")
_WfDlsTranslateMacEntry_Object = MibTableRow
wfDlsTranslateMacEntry = _WfDlsTranslateMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 16, 1)
)
wfDlsTranslateMacEntry.setIndexNames(
    (0, "Wellfleet-DLS-MIB", "wfDlsOriginDestMacAddr"),
)
if mibBuilder.loadTexts:
    wfDlsTranslateMacEntry.setStatus("mandatory")


class _WfDlsTranslateMacDelete_Type(Integer32):
    """Custom type wfDlsTranslateMacDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDlsTranslateMacDelete_Type.__name__ = "Integer32"
_WfDlsTranslateMacDelete_Object = MibTableColumn
wfDlsTranslateMacDelete = _WfDlsTranslateMacDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 16, 1, 1),
    _WfDlsTranslateMacDelete_Type()
)
wfDlsTranslateMacDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsTranslateMacDelete.setStatus("mandatory")


class _WfDlsOriginDestMacAddr_Type(OctetString):
    """Custom type wfDlsOriginDestMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfDlsOriginDestMacAddr_Type.__name__ = "OctetString"
_WfDlsOriginDestMacAddr_Object = MibTableColumn
wfDlsOriginDestMacAddr = _WfDlsOriginDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 16, 1, 2),
    _WfDlsOriginDestMacAddr_Type()
)
wfDlsOriginDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDlsOriginDestMacAddr.setStatus("mandatory")


class _WfDlsTranslateDestMacAddr_Type(OctetString):
    """Custom type wfDlsTranslateDestMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WfDlsTranslateDestMacAddr_Type.__name__ = "OctetString"
_WfDlsTranslateDestMacAddr_Object = MibTableColumn
wfDlsTranslateDestMacAddr = _WfDlsTranslateDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 5, 16, 1, 3),
    _WfDlsTranslateDestMacAddr_Type()
)
wfDlsTranslateDestMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDlsTranslateDestMacAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-DLS-MIB",
    **{"wfDls": wfDls,
       "wfDlsDelete": wfDlsDelete,
       "wfDlsDisable": wfDlsDisable,
       "wfDlsState": wfDlsState,
       "wfDlsTcpWindowSize": wfDlsTcpWindowSize,
       "wfDlsVirtualRing": wfDlsVirtualRing,
       "wfDlsInternalLanId": wfDlsInternalLanId,
       "wfDlsBridgeId": wfDlsBridgeId,
       "wfDlsMaxSlotSessions": wfDlsMaxSlotSessions,
       "wfDlsTotalCircuits": wfDlsTotalCircuits,
       "wfDlsVirtualRingMtu": wfDlsVirtualRingMtu,
       "wfDlsMacAgeTime": wfDlsMacAgeTime,
       "wfDlsNbAgeTime": wfDlsNbAgeTime,
       "wfDlsUnconfPeerReject": wfDlsUnconfPeerReject,
       "wfDlsDebugLevel1": wfDlsDebugLevel1,
       "wfDlsDebugLevel2": wfDlsDebugLevel2,
       "wfDlsWanKeepaliveTime": wfDlsWanKeepaliveTime,
       "wfDlsPPriDisable": wfDlsPPriDisable,
       "wfDlsPPriDefaultNumQueues": wfDlsPPriDefaultNumQueues,
       "wfDlsPPriDefaultQBandwidth": wfDlsPPriDefaultQBandwidth,
       "wfDlsPPriUnconfPeerDisable": wfDlsPPriUnconfPeerDisable,
       "wfDlsPPriUnconfPeerMaxQBuf": wfDlsPPriUnconfPeerMaxQBuf,
       "wfDlsPPriUnconfPeerMaxQSize": wfDlsPPriUnconfPeerMaxQSize,
       "wfDlsPkgMaxSize": wfDlsPkgMaxSize,
       "wfDlsPkgTO": wfDlsPkgTO,
       "wfDlsPkgWinPercent": wfDlsPkgWinPercent,
       "wfDlsMultislotBcasts": wfDlsMultislotBcasts,
       "wfDlsInitialPacingWindow": wfDlsInitialPacingWindow,
       "wfDlsRfc": wfDlsRfc,
       "wfDlsNetbiosSessionAliveFilter": wfDlsNetbiosSessionAliveFilter,
       "wfDlsWanKeepaliveRetryTimer": wfDlsWanKeepaliveRetryTimer,
       "wfDlsWanKeepaliveRetries": wfDlsWanKeepaliveRetries,
       "wfDlsSnaFallbackAttempts": wfDlsSnaFallbackAttempts,
       "wfDlsNetbiosFallbackTime": wfDlsNetbiosFallbackTime,
       "wfDlsTcpInactTime": wfDlsTcpInactTime,
       "wfDlsTcpInactMethod": wfDlsTcpInactMethod,
       "wfDlsMslotDLCBcasts": wfDlsMslotDLCBcasts,
       "wfDlsRsvpSupport": wfDlsRsvpSupport,
       "wfDlsOutBandwidth": wfDlsOutBandwidth,
       "wfDlsOutBurstSize": wfDlsOutBurstSize,
       "wfDlsInBandwidth": wfDlsInBandwidth,
       "wfDlsInBurstSize": wfDlsInBurstSize,
       "wfDlsNonPeakOutBandwidth": wfDlsNonPeakOutBandwidth,
       "wfDlsNonPeakOutBurstSize": wfDlsNonPeakOutBurstSize,
       "wfDlsNonPeakInBandwidth": wfDlsNonPeakInBandwidth,
       "wfDlsNonPeakInBurstSize": wfDlsNonPeakInBurstSize,
       "wfDlsNonPeakStartTime": wfDlsNonPeakStartTime,
       "wfDlsNonPeakEndTime": wfDlsNonPeakEndTime,
       "wfDlsNonPeakStartDays": wfDlsNonPeakStartDays,
       "wfDlsMultislotCacheUpdate": wfDlsMultislotCacheUpdate,
       "wfDlsMacAddrTranslation": wfDlsMacAddrTranslation,
       "wfDlsBan2Support": wfDlsBan2Support,
       "wfDlsVirtualRingBridgeCheck": wfDlsVirtualRingBridgeCheck,
       "wfDlsAcceptBadVendorSpecificCapex": wfDlsAcceptBadVendorSpecificCapex,
       "wfDlsDiagSwitch": wfDlsDiagSwitch,
       "wfDlsAllowSpecAddrNbDatagram": wfDlsAllowSpecAddrNbDatagram,
       "wfDlsInterfaceTable": wfDlsInterfaceTable,
       "wfDlsInterfaceEntry": wfDlsInterfaceEntry,
       "wfDlsInterfaceDelete": wfDlsInterfaceDelete,
       "wfDlsInterfaceDisable": wfDlsInterfaceDisable,
       "wfDlsInterfaceState": wfDlsInterfaceState,
       "wfDlsInterfaceCircuit": wfDlsInterfaceCircuit,
       "wfDlsInterfaceBridgeId": wfDlsInterfaceBridgeId,
       "wfDlsInterfaceLanId": wfDlsInterfaceLanId,
       "wfDlsInterfaceDlcType": wfDlsInterfaceDlcType,
       "wfDlsInterfaceSdlcMode": wfDlsInterfaceSdlcMode,
       "wfDlsInterfaceNbBcastDgramReduce": wfDlsInterfaceNbBcastDgramReduce,
       "wfDlsInterfaceExplorerType": wfDlsInterfaceExplorerType,
       "wfDlsInterfaceNbBcastDgramCache": wfDlsInterfaceNbBcastDgramCache,
       "wfDlsInterfaceClrCallEnable": wfDlsInterfaceClrCallEnable,
       "wfDlsSlotTable": wfDlsSlotTable,
       "wfDlsSlotEntry": wfDlsSlotEntry,
       "wfDlsSlotDelete": wfDlsSlotDelete,
       "wfDlsSlotNumber": wfDlsSlotNumber,
       "wfDlsSlotIpAddr": wfDlsSlotIpAddr,
       "wfDlsCurrentMemory": wfDlsCurrentMemory,
       "wfDlsMaxAllowedMemory": wfDlsMaxAllowedMemory,
       "wfDlsHiWaterMark": wfDlsHiWaterMark,
       "wfDlsSlotGenDestination": wfDlsSlotGenDestination,
       "wfDlsSlotGenSessions": wfDlsSlotGenSessions,
       "wfDlsSlotGenUpperMAC": wfDlsSlotGenUpperMAC,
       "wfDlsSlotCurrentSessions": wfDlsSlotCurrentSessions,
       "wfDlsSlotHiWaterSessions": wfDlsSlotHiWaterSessions,
       "wfDlsSlotHiWaterReset": wfDlsSlotHiWaterReset,
       "wfDlsSapTable": wfDlsSapTable,
       "wfDlsSapEntry": wfDlsSapEntry,
       "wfDlsSapDelete": wfDlsSapDelete,
       "wfDlsSapAddr": wfDlsSapAddr,
       "wfDlsSapCredit": wfDlsSapCredit,
       "wfDlsPeerTable": wfDlsPeerTable,
       "wfDlsPeerEntry": wfDlsPeerEntry,
       "wfDlsPeerDelete": wfDlsPeerDelete,
       "wfDlsPeerState": wfDlsPeerState,
       "wfDlsPeerIpAddr": wfDlsPeerIpAddr,
       "wfDlsPeerDefinedBy": wfDlsPeerDefinedBy,
       "wfDlsPeerPPriDisable": wfDlsPeerPPriDisable,
       "wfDlsPeerPPriMaxQBuf": wfDlsPeerPPriMaxQBuf,
       "wfDlsPeerPPriMaxQSize": wfDlsPeerPPriMaxQSize,
       "wfDlsPeerPPriClearStats": wfDlsPeerPPriClearStats,
       "wfDlsPeerType": wfDlsPeerType,
       "wfDlsPeerTransportType": wfDlsPeerTransportType,
       "wfDlsPeerBackupConfig": wfDlsPeerBackupConfig,
       "wfDlsPeerBackupIpAddr": wfDlsPeerBackupIpAddr,
       "wfDlsPeerBackupMaxUpTime": wfDlsPeerBackupMaxUpTime,
       "wfDlsPeerBackupHoldDownTime": wfDlsPeerBackupHoldDownTime,
       "wfDlsPeerBackupStartTime": wfDlsPeerBackupStartTime,
       "wfDlsPeerBackupEndTime": wfDlsPeerBackupEndTime,
       "wfDlsPeerInteroperability": wfDlsPeerInteroperability,
       "wfDlsPeerBackupType": wfDlsPeerBackupType,
       "wfDlsPeerRsvpMode": wfDlsPeerRsvpMode,
       "wfDlsPeerRsvpSlots": wfDlsPeerRsvpSlots,
       "wfDlsPeerOutBandwidth": wfDlsPeerOutBandwidth,
       "wfDlsPeerOutBurstSize": wfDlsPeerOutBurstSize,
       "wfDlsPeerInBandwidth": wfDlsPeerInBandwidth,
       "wfDlsPeerInBurstSize": wfDlsPeerInBurstSize,
       "wfDlsPeerNonPeakOutBandwidth": wfDlsPeerNonPeakOutBandwidth,
       "wfDlsPeerNonPeakOutBurstSize": wfDlsPeerNonPeakOutBurstSize,
       "wfDlsPeerNonPeakInBandwidth": wfDlsPeerNonPeakInBandwidth,
       "wfDlsPeerNonPeakInBurstSize": wfDlsPeerNonPeakInBurstSize,
       "wfDlsPeerNonPeakStartTime": wfDlsPeerNonPeakStartTime,
       "wfDlsPeerNonPeakEndTime": wfDlsPeerNonPeakEndTime,
       "wfDlsPeerNonPeakStartDays": wfDlsPeerNonPeakStartDays,
       "wfDlsPeerBackupOutBandwidth": wfDlsPeerBackupOutBandwidth,
       "wfDlsPeerBackupOutBurstSize": wfDlsPeerBackupOutBurstSize,
       "wfDlsPeerBackupInBandwidth": wfDlsPeerBackupInBandwidth,
       "wfDlsPeerBackupInBurstSize": wfDlsPeerBackupInBurstSize,
       "wfDlsConnectionTable": wfDlsConnectionTable,
       "wfDlsConnectionEntry": wfDlsConnectionEntry,
       "wfDlsConnectionCct": wfDlsConnectionCct,
       "wfDlsConnectionDstMac": wfDlsConnectionDstMac,
       "wfDlsConnectionSrcMac": wfDlsConnectionSrcMac,
       "wfDlsConnectionSaps": wfDlsConnectionSaps,
       "wfDlsConnectionState": wfDlsConnectionState,
       "wfDlsConnectionRemoteIpAddr": wfDlsConnectionRemoteIpAddr,
       "wfDlsConnectionRemoteRxPort": wfDlsConnectionRemoteRxPort,
       "wfDlsConnectionLocalIpAddr": wfDlsConnectionLocalIpAddr,
       "wfDlsConnectionLocalTxPort": wfDlsConnectionLocalTxPort,
       "wfDlsConnectionTxIFrames": wfDlsConnectionTxIFrames,
       "wfDlsConnectionRxIFrames": wfDlsConnectionRxIFrames,
       "wfDlsConnectionTxRnrs": wfDlsConnectionTxRnrs,
       "wfDlsConnectionRxRnrs": wfDlsConnectionRxRnrs,
       "wfDlsConnectionLocalBlockNum": wfDlsConnectionLocalBlockNum,
       "wfDlsConnectionLocalIdNum": wfDlsConnectionLocalIdNum,
       "wfDlsConnectionLocalCpName": wfDlsConnectionLocalCpName,
       "wfDlsConnectionRif": wfDlsConnectionRif,
       "wfDlsConnectionRemoteBlockNum": wfDlsConnectionRemoteBlockNum,
       "wfDlsConnectionRemoteIdNum": wfDlsConnectionRemoteIdNum,
       "wfDlsConnectionRemoteCpName": wfDlsConnectionRemoteCpName,
       "wfDlsConnectionLocalDLCorr": wfDlsConnectionLocalDLCorr,
       "wfDlsConnectionKilled": wfDlsConnectionKilled,
       "wfDlsConnectionRemoteDLCorr": wfDlsConnectionRemoteDLCorr,
       "wfDlsNbTable": wfDlsNbTable,
       "wfDlsNbEntry": wfDlsNbEntry,
       "wfDlsNbName": wfDlsNbName,
       "wfDlsNbPeerIpAddr": wfDlsNbPeerIpAddr,
       "wfDlsNbCapablePeerIpAddr": wfDlsNbCapablePeerIpAddr,
       "wfDlsNbQueries": wfDlsNbQueries,
       "wfDlsMacTable": wfDlsMacTable,
       "wfDlsMacEntry": wfDlsMacEntry,
       "wfDlsMacAddr": wfDlsMacAddr,
       "wfDlsMacPeerIpAddr": wfDlsMacPeerIpAddr,
       "wfDlsMacCapablePeerIpAddr": wfDlsMacCapablePeerIpAddr,
       "wfDlsMacQueries": wfDlsMacQueries,
       "wfDlsTrafficFilterTable": wfDlsTrafficFilterTable,
       "wfDlsTrafficFilterEntry": wfDlsTrafficFilterEntry,
       "wfDlsTrafficFilterCreate": wfDlsTrafficFilterCreate,
       "wfDlsTrafficFilterEnable": wfDlsTrafficFilterEnable,
       "wfDlsTrafficFilterStatus": wfDlsTrafficFilterStatus,
       "wfDlsTrafficFilterCounter": wfDlsTrafficFilterCounter,
       "wfDlsTrafficFilterDefinition": wfDlsTrafficFilterDefinition,
       "wfDlsTrafficFilterReserved": wfDlsTrafficFilterReserved,
       "wfDlsTrafficFilterCircuit": wfDlsTrafficFilterCircuit,
       "wfDlsTrafficFilterRuleNumber": wfDlsTrafficFilterRuleNumber,
       "wfDlsTrafficFilterFragment": wfDlsTrafficFilterFragment,
       "wfDlsTrafficFilterName": wfDlsTrafficFilterName,
       "wfDlsDefaultMacTable": wfDlsDefaultMacTable,
       "wfDlsDefaultMacEntry": wfDlsDefaultMacEntry,
       "wfDlsDefaultMacDelete": wfDlsDefaultMacDelete,
       "wfDlsDefaultMacAddr": wfDlsDefaultMacAddr,
       "wfDlsDefaultMacPeerIp": wfDlsDefaultMacPeerIp,
       "wfDlsDefaultNbTable": wfDlsDefaultNbTable,
       "wfDlsDefaultNbEntry": wfDlsDefaultNbEntry,
       "wfDlsDefaultNbDelete": wfDlsDefaultNbDelete,
       "wfDlsDefaultNbName": wfDlsDefaultNbName,
       "wfDlsDefaultNbPeerIp": wfDlsDefaultNbPeerIp,
       "wfDlsLocalDeviceTable": wfDlsLocalDeviceTable,
       "wfDlsLocalDeviceEntry": wfDlsLocalDeviceEntry,
       "wfDlsLocalDeviceDelete": wfDlsLocalDeviceDelete,
       "wfDlsLocalDeviceDisable": wfDlsLocalDeviceDisable,
       "wfDlsLocalDeviceState": wfDlsLocalDeviceState,
       "wfDlsLocalDeviceCct": wfDlsLocalDeviceCct,
       "wfDlsLocalDeviceAddr": wfDlsLocalDeviceAddr,
       "wfDlsLocalDeviceSourceMac": wfDlsLocalDeviceSourceMac,
       "wfDlsLocalDeviceSourceSap": wfDlsLocalDeviceSourceSap,
       "wfDlsLocalDeviceDestMac": wfDlsLocalDeviceDestMac,
       "wfDlsLocalDeviceDestSap": wfDlsLocalDeviceDestSap,
       "wfDlsLocalDeviceXidValue": wfDlsLocalDeviceXidValue,
       "wfDlsLocalDeviceCanureachTimer": wfDlsLocalDeviceCanureachTimer,
       "wfDlsLocalDeviceCanureachRetries": wfDlsLocalDeviceCanureachRetries,
       "wfDlsLocalDeviceLSTimer": wfDlsLocalDeviceLSTimer,
       "wfDlsLocalDeviceLSRetries": wfDlsLocalDeviceLSRetries,
       "wfDlsLocalDeviceRcvCredit": wfDlsLocalDeviceRcvCredit,
       "wfDlsLocalDeviceTxCredit": wfDlsLocalDeviceTxCredit,
       "wfDlsLocalDeviceCurTimer2": wfDlsLocalDeviceCurTimer2,
       "wfDlsLocalDeviceCurRetries2": wfDlsLocalDeviceCurRetries2,
       "wfDlsLocalDeviceEnableXidPassthru": wfDlsLocalDeviceEnableXidPassthru,
       "wfDlsLocalDeviceActivationSequence": wfDlsLocalDeviceActivationSequence,
       "wfDlsLocalCircuitTable": wfDlsLocalCircuitTable,
       "wfDlsLocalCircuitEntry": wfDlsLocalCircuitEntry,
       "wfDlsLocalCircuitDelete": wfDlsLocalCircuitDelete,
       "wfDlsLocalCircuitDisable": wfDlsLocalCircuitDisable,
       "wfDlsLocalCircuitState": wfDlsLocalCircuitState,
       "wfDlsLocalCircuitCct": wfDlsLocalCircuitCct,
       "wfDlsLocalCircuitClientCount": wfDlsLocalCircuitClientCount,
       "wfDlsLocalCircuitFrameCount": wfDlsLocalCircuitFrameCount,
       "wfDlsLocalCircuitSlot": wfDlsLocalCircuitSlot,
       "wfDlsLocalCctDefaultMac": wfDlsLocalCctDefaultMac,
       "wfDlsGenToolTable": wfDlsGenToolTable,
       "wfDlsGenToolEntry": wfDlsGenToolEntry,
       "wfDlsGenDelete": wfDlsGenDelete,
       "wfDlsGenDisable": wfDlsGenDisable,
       "wfDlsGenDefaultSessions": wfDlsGenDefaultSessions,
       "wfDlsGenStartupTime": wfDlsGenStartupTime,
       "wfDlsGenIFramePerSec": wfDlsGenIFramePerSec,
       "wfDlsGenMacAddrOffset": wfDlsGenMacAddrOffset,
       "wfDlsGenVariableDstMAC": wfDlsGenVariableDstMAC,
       "wfDlsGenDefaultUpperMAC": wfDlsGenDefaultUpperMAC,
       "wfDlsGenDataLength": wfDlsGenDataLength,
       "wfDlsGenNumSapPerMac": wfDlsGenNumSapPerMac,
       "wfDlsGenSapIncrement": wfDlsGenSapIncrement,
       "wfDlsMcastIpTable": wfDlsMcastIpTable,
       "wfDlsMcastIpEntry": wfDlsMcastIpEntry,
       "wfDlsMcastIpDelete": wfDlsMcastIpDelete,
       "wfDlsMcastIpState": wfDlsMcastIpState,
       "wfDlsMcastIpAddr": wfDlsMcastIpAddr,
       "wfDlsMcastIpSlots": wfDlsMcastIpSlots,
       "wfDlsMcastIpBackupConfig": wfDlsMcastIpBackupConfig,
       "wfDlsMcastIpBackupIpAddr": wfDlsMcastIpBackupIpAddr,
       "wfDlsMcastIpBackupMaxUpTime": wfDlsMcastIpBackupMaxUpTime,
       "wfDlsMcastIpBackupHoldDownTime": wfDlsMcastIpBackupHoldDownTime,
       "wfDlsMcastIpBackupStartTime": wfDlsMcastIpBackupStartTime,
       "wfDlsMcastIpBackupEndTime": wfDlsMcastIpBackupEndTime,
       "wfDlsMcastIpBackupType": wfDlsMcastIpBackupType,
       "wfDlsTranslateMacTable": wfDlsTranslateMacTable,
       "wfDlsTranslateMacEntry": wfDlsTranslateMacEntry,
       "wfDlsTranslateMacDelete": wfDlsTranslateMacDelete,
       "wfDlsOriginDestMacAddr": wfDlsOriginDestMacAddr,
       "wfDlsTranslateDestMacAddr": wfDlsTranslateDestMacAddr}
)
