# SNMP MIB module (Wellfleet-MPLS-LDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-MPLS-LDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:42 2024
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

(wfMplsLdpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfMplsLdpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfMplsLdpSessCfgTable_Object = MibTable
wfMplsLdpSessCfgTable = _WfMplsLdpSessCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1)
)
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgTable.setStatus("mandatory")
_WfMplsLdpSessCfgEntry_Object = MibTableRow
wfMplsLdpSessCfgEntry = _WfMplsLdpSessCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1)
)
wfMplsLdpSessCfgEntry.setIndexNames(
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessCfgSlot"),
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessCfgCircuit"),
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessCfgIndex"),
)
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgEntry.setStatus("mandatory")


class _WfMplsLdpSessCfgCreate_Type(Integer32):
    """Custom type wfMplsLdpSessCfgCreate based on Integer32"""
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


_WfMplsLdpSessCfgCreate_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgCreate_Object = MibTableColumn
wfMplsLdpSessCfgCreate = _WfMplsLdpSessCfgCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 1),
    _WfMplsLdpSessCfgCreate_Type()
)
wfMplsLdpSessCfgCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgCreate.setStatus("mandatory")


class _WfMplsLdpSessCfgEnable_Type(Integer32):
    """Custom type wfMplsLdpSessCfgEnable based on Integer32"""
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


_WfMplsLdpSessCfgEnable_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgEnable_Object = MibTableColumn
wfMplsLdpSessCfgEnable = _WfMplsLdpSessCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 2),
    _WfMplsLdpSessCfgEnable_Type()
)
wfMplsLdpSessCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgEnable.setStatus("mandatory")
_WfMplsLdpSessCfgSlot_Type = Integer32
_WfMplsLdpSessCfgSlot_Object = MibTableColumn
wfMplsLdpSessCfgSlot = _WfMplsLdpSessCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 3),
    _WfMplsLdpSessCfgSlot_Type()
)
wfMplsLdpSessCfgSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgSlot.setStatus("mandatory")
_WfMplsLdpSessCfgIndex_Type = Integer32
_WfMplsLdpSessCfgIndex_Object = MibTableColumn
wfMplsLdpSessCfgIndex = _WfMplsLdpSessCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 4),
    _WfMplsLdpSessCfgIndex_Type()
)
wfMplsLdpSessCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgIndex.setStatus("mandatory")


class _WfMplsLdpSessCfgCircuit_Type(Integer32):
    """Custom type wfMplsLdpSessCfgCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfMplsLdpSessCfgCircuit_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgCircuit_Object = MibTableColumn
wfMplsLdpSessCfgCircuit = _WfMplsLdpSessCfgCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 5),
    _WfMplsLdpSessCfgCircuit_Type()
)
wfMplsLdpSessCfgCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgCircuit.setStatus("mandatory")
_WfMplsLdpSessCfgLocalIpAddress_Type = IpAddress
_WfMplsLdpSessCfgLocalIpAddress_Object = MibTableColumn
wfMplsLdpSessCfgLocalIpAddress = _WfMplsLdpSessCfgLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 6),
    _WfMplsLdpSessCfgLocalIpAddress_Type()
)
wfMplsLdpSessCfgLocalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgLocalIpAddress.setStatus("mandatory")


class _WfMplsLdpSessCfgLocalTcpPort_Type(Integer32):
    """Custom type wfMplsLdpSessCfgLocalTcpPort based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfMplsLdpSessCfgLocalTcpPort_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgLocalTcpPort_Object = MibTableColumn
wfMplsLdpSessCfgLocalTcpPort = _WfMplsLdpSessCfgLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 7),
    _WfMplsLdpSessCfgLocalTcpPort_Type()
)
wfMplsLdpSessCfgLocalTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgLocalTcpPort.setStatus("mandatory")
_WfMplsLdpSessCfgRemoteIpAddress_Type = IpAddress
_WfMplsLdpSessCfgRemoteIpAddress_Object = MibTableColumn
wfMplsLdpSessCfgRemoteIpAddress = _WfMplsLdpSessCfgRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 8),
    _WfMplsLdpSessCfgRemoteIpAddress_Type()
)
wfMplsLdpSessCfgRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgRemoteIpAddress.setStatus("mandatory")


class _WfMplsLdpSessCfgRemoteTcpPort_Type(Integer32):
    """Custom type wfMplsLdpSessCfgRemoteTcpPort based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfMplsLdpSessCfgRemoteTcpPort_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgRemoteTcpPort_Object = MibTableColumn
wfMplsLdpSessCfgRemoteTcpPort = _WfMplsLdpSessCfgRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 9),
    _WfMplsLdpSessCfgRemoteTcpPort_Type()
)
wfMplsLdpSessCfgRemoteTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgRemoteTcpPort.setStatus("mandatory")


class _WfMplsLdpSessCfgRoutesConfigMode_Type(Integer32):
    """Custom type wfMplsLdpSessCfgRoutesConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_WfMplsLdpSessCfgRoutesConfigMode_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgRoutesConfigMode_Object = MibTableColumn
wfMplsLdpSessCfgRoutesConfigMode = _WfMplsLdpSessCfgRoutesConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 10),
    _WfMplsLdpSessCfgRoutesConfigMode_Type()
)
wfMplsLdpSessCfgRoutesConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgRoutesConfigMode.setStatus("mandatory")


class _WfMplsLdpSessCfgHoldTime_Type(Integer32):
    """Custom type wfMplsLdpSessCfgHoldTime based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_WfMplsLdpSessCfgHoldTime_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgHoldTime_Object = MibTableColumn
wfMplsLdpSessCfgHoldTime = _WfMplsLdpSessCfgHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 11),
    _WfMplsLdpSessCfgHoldTime_Type()
)
wfMplsLdpSessCfgHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgHoldTime.setStatus("mandatory")


class _WfMplsLdpSessCfgProto_Type(Integer32):
    """Custom type wfMplsLdpSessCfgProto based on Integer32"""
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
        *(("hybridospf", 3),
          ("hybridrip", 4),
          ("ospf", 1),
          ("rip", 2))
    )


_WfMplsLdpSessCfgProto_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgProto_Object = MibTableColumn
wfMplsLdpSessCfgProto = _WfMplsLdpSessCfgProto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 12),
    _WfMplsLdpSessCfgProto_Type()
)
wfMplsLdpSessCfgProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgProto.setStatus("mandatory")


class _WfMplsLdpSessCfgAggregation_Type(Integer32):
    """Custom type wfMplsLdpSessCfgAggregation based on Integer32"""
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


_WfMplsLdpSessCfgAggregation_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgAggregation_Object = MibTableColumn
wfMplsLdpSessCfgAggregation = _WfMplsLdpSessCfgAggregation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 13),
    _WfMplsLdpSessCfgAggregation_Type()
)
wfMplsLdpSessCfgAggregation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgAggregation.setStatus("mandatory")


class _WfMplsLdpSessCfgDebugLevel_Type(Integer32):
    """Custom type wfMplsLdpSessCfgDebugLevel based on Integer32"""
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
        *(("debug", 4),
          ("one", 1),
          ("three", 3),
          ("two", 2))
    )


_WfMplsLdpSessCfgDebugLevel_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgDebugLevel_Object = MibTableColumn
wfMplsLdpSessCfgDebugLevel = _WfMplsLdpSessCfgDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 14),
    _WfMplsLdpSessCfgDebugLevel_Type()
)
wfMplsLdpSessCfgDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgDebugLevel.setStatus("mandatory")


class _WfMplsLdpSessCfgReqBindRetryTime_Type(Integer32):
    """Custom type wfMplsLdpSessCfgReqBindRetryTime based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_WfMplsLdpSessCfgReqBindRetryTime_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgReqBindRetryTime_Object = MibTableColumn
wfMplsLdpSessCfgReqBindRetryTime = _WfMplsLdpSessCfgReqBindRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 15),
    _WfMplsLdpSessCfgReqBindRetryTime_Type()
)
wfMplsLdpSessCfgReqBindRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgReqBindRetryTime.setStatus("mandatory")


class _WfMplsLdpSessCfgReqBindRetries_Type(Integer32):
    """Custom type wfMplsLdpSessCfgReqBindRetries based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_WfMplsLdpSessCfgReqBindRetries_Type.__name__ = "Integer32"
_WfMplsLdpSessCfgReqBindRetries_Object = MibTableColumn
wfMplsLdpSessCfgReqBindRetries = _WfMplsLdpSessCfgReqBindRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 1, 1, 16),
    _WfMplsLdpSessCfgReqBindRetries_Type()
)
wfMplsLdpSessCfgReqBindRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpSessCfgReqBindRetries.setStatus("mandatory")
_WfMplsLdpSessActualTable_Object = MibTable
wfMplsLdpSessActualTable = _WfMplsLdpSessActualTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2)
)
if mibBuilder.loadTexts:
    wfMplsLdpSessActualTable.setStatus("mandatory")
_WfMplsLdpSessActualEntry_Object = MibTableRow
wfMplsLdpSessActualEntry = _WfMplsLdpSessActualEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1)
)
wfMplsLdpSessActualEntry.setIndexNames(
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessActualCircuit"),
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpSessActualIndex"),
)
if mibBuilder.loadTexts:
    wfMplsLdpSessActualEntry.setStatus("mandatory")
_WfMplsLdpSessActualIndex_Type = Integer32
_WfMplsLdpSessActualIndex_Object = MibTableColumn
wfMplsLdpSessActualIndex = _WfMplsLdpSessActualIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 1),
    _WfMplsLdpSessActualIndex_Type()
)
wfMplsLdpSessActualIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualIndex.setStatus("mandatory")


class _WfMplsLdpSessActualCircuit_Type(Integer32):
    """Custom type wfMplsLdpSessActualCircuit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfMplsLdpSessActualCircuit_Type.__name__ = "Integer32"
_WfMplsLdpSessActualCircuit_Object = MibTableColumn
wfMplsLdpSessActualCircuit = _WfMplsLdpSessActualCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 2),
    _WfMplsLdpSessActualCircuit_Type()
)
wfMplsLdpSessActualCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualCircuit.setStatus("mandatory")


class _WfMplsLdpSessActualState_Type(Integer32):
    """Custom type wfMplsLdpSessActualState based on Integer32"""
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


_WfMplsLdpSessActualState_Type.__name__ = "Integer32"
_WfMplsLdpSessActualState_Object = MibTableColumn
wfMplsLdpSessActualState = _WfMplsLdpSessActualState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 3),
    _WfMplsLdpSessActualState_Type()
)
wfMplsLdpSessActualState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualState.setStatus("mandatory")


class _WfMplsLdpSessActualPeerState_Type(Integer32):
    """Custom type wfMplsLdpSessActualPeerState based on Integer32"""
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
        *(("initialized", 1),
          ("openrec", 3),
          ("opensend", 2),
          ("operational", 4))
    )


_WfMplsLdpSessActualPeerState_Type.__name__ = "Integer32"
_WfMplsLdpSessActualPeerState_Object = MibTableColumn
wfMplsLdpSessActualPeerState = _WfMplsLdpSessActualPeerState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 4),
    _WfMplsLdpSessActualPeerState_Type()
)
wfMplsLdpSessActualPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualPeerState.setStatus("mandatory")
_WfMplsLdpSessActualLocalIpAddress_Type = IpAddress
_WfMplsLdpSessActualLocalIpAddress_Object = MibTableColumn
wfMplsLdpSessActualLocalIpAddress = _WfMplsLdpSessActualLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 5),
    _WfMplsLdpSessActualLocalIpAddress_Type()
)
wfMplsLdpSessActualLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualLocalIpAddress.setStatus("mandatory")


class _WfMplsLdpSessActualLocalTcpPort_Type(Integer32):
    """Custom type wfMplsLdpSessActualLocalTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfMplsLdpSessActualLocalTcpPort_Type.__name__ = "Integer32"
_WfMplsLdpSessActualLocalTcpPort_Object = MibTableColumn
wfMplsLdpSessActualLocalTcpPort = _WfMplsLdpSessActualLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 6),
    _WfMplsLdpSessActualLocalTcpPort_Type()
)
wfMplsLdpSessActualLocalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualLocalTcpPort.setStatus("mandatory")
_WfMplsLdpSessActualRemoteIpAddress_Type = IpAddress
_WfMplsLdpSessActualRemoteIpAddress_Object = MibTableColumn
wfMplsLdpSessActualRemoteIpAddress = _WfMplsLdpSessActualRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 7),
    _WfMplsLdpSessActualRemoteIpAddress_Type()
)
wfMplsLdpSessActualRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualRemoteIpAddress.setStatus("mandatory")


class _WfMplsLdpSessActualRemoteTcpPort_Type(Integer32):
    """Custom type wfMplsLdpSessActualRemoteTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfMplsLdpSessActualRemoteTcpPort_Type.__name__ = "Integer32"
_WfMplsLdpSessActualRemoteTcpPort_Object = MibTableColumn
wfMplsLdpSessActualRemoteTcpPort = _WfMplsLdpSessActualRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 8),
    _WfMplsLdpSessActualRemoteTcpPort_Type()
)
wfMplsLdpSessActualRemoteTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualRemoteTcpPort.setStatus("mandatory")


class _WfMplsLdpSessActualHoldTime_Type(Integer32):
    """Custom type wfMplsLdpSessActualHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_WfMplsLdpSessActualHoldTime_Type.__name__ = "Integer32"
_WfMplsLdpSessActualHoldTime_Object = MibTableColumn
wfMplsLdpSessActualHoldTime = _WfMplsLdpSessActualHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 9),
    _WfMplsLdpSessActualHoldTime_Type()
)
wfMplsLdpSessActualHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualHoldTime.setStatus("mandatory")


class _WfMplsLdpSessActualRoutesConfigMode_Type(Integer32):
    """Custom type wfMplsLdpSessActualRoutesConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_WfMplsLdpSessActualRoutesConfigMode_Type.__name__ = "Integer32"
_WfMplsLdpSessActualRoutesConfigMode_Object = MibTableColumn
wfMplsLdpSessActualRoutesConfigMode = _WfMplsLdpSessActualRoutesConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 10),
    _WfMplsLdpSessActualRoutesConfigMode_Type()
)
wfMplsLdpSessActualRoutesConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualRoutesConfigMode.setStatus("mandatory")


class _WfMplsLdpSessActualTCPConnectionRole_Type(Integer32):
    """Custom type wfMplsLdpSessActualTCPConnectionRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_WfMplsLdpSessActualTCPConnectionRole_Type.__name__ = "Integer32"
_WfMplsLdpSessActualTCPConnectionRole_Object = MibTableColumn
wfMplsLdpSessActualTCPConnectionRole = _WfMplsLdpSessActualTCPConnectionRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 11),
    _WfMplsLdpSessActualTCPConnectionRole_Type()
)
wfMplsLdpSessActualTCPConnectionRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualTCPConnectionRole.setStatus("mandatory")
_WfMplsLdpSessActualSlot_Type = Integer32
_WfMplsLdpSessActualSlot_Object = MibTableColumn
wfMplsLdpSessActualSlot = _WfMplsLdpSessActualSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 2, 1, 12),
    _WfMplsLdpSessActualSlot_Type()
)
wfMplsLdpSessActualSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpSessActualSlot.setStatus("mandatory")
_WfMplsLdpCfgRouteTable_Object = MibTable
wfMplsLdpCfgRouteTable = _WfMplsLdpCfgRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3)
)
if mibBuilder.loadTexts:
    wfMplsLdpCfgRouteTable.setStatus("mandatory")
_WfMplsLdpCfgRouteEntry_Object = MibTableRow
wfMplsLdpCfgRouteEntry = _WfMplsLdpCfgRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1)
)
wfMplsLdpCfgRouteEntry.setIndexNames(
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpCfgRouteCct"),
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpCfgRouteSessId"),
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpCfgRouteIndex"),
)
if mibBuilder.loadTexts:
    wfMplsLdpCfgRouteEntry.setStatus("mandatory")


class _WfMplsLdpCfgRouteCreate_Type(Integer32):
    """Custom type wfMplsLdpCfgRouteCreate based on Integer32"""
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


_WfMplsLdpCfgRouteCreate_Type.__name__ = "Integer32"
_WfMplsLdpCfgRouteCreate_Object = MibTableColumn
wfMplsLdpCfgRouteCreate = _WfMplsLdpCfgRouteCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 1),
    _WfMplsLdpCfgRouteCreate_Type()
)
wfMplsLdpCfgRouteCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpCfgRouteCreate.setStatus("mandatory")


class _WfMplsLdpCfgRouteEnable_Type(Integer32):
    """Custom type wfMplsLdpCfgRouteEnable based on Integer32"""
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


_WfMplsLdpCfgRouteEnable_Type.__name__ = "Integer32"
_WfMplsLdpCfgRouteEnable_Object = MibTableColumn
wfMplsLdpCfgRouteEnable = _WfMplsLdpCfgRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 2),
    _WfMplsLdpCfgRouteEnable_Type()
)
wfMplsLdpCfgRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpCfgRouteEnable.setStatus("mandatory")


class _WfMplsLdpCfgRouteCct_Type(Integer32):
    """Custom type wfMplsLdpCfgRouteCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfMplsLdpCfgRouteCct_Type.__name__ = "Integer32"
_WfMplsLdpCfgRouteCct_Object = MibTableColumn
wfMplsLdpCfgRouteCct = _WfMplsLdpCfgRouteCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 3),
    _WfMplsLdpCfgRouteCct_Type()
)
wfMplsLdpCfgRouteCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpCfgRouteCct.setStatus("mandatory")


class _WfMplsLdpCfgRouteSessId_Type(Integer32):
    """Custom type wfMplsLdpCfgRouteSessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfMplsLdpCfgRouteSessId_Type.__name__ = "Integer32"
_WfMplsLdpCfgRouteSessId_Object = MibTableColumn
wfMplsLdpCfgRouteSessId = _WfMplsLdpCfgRouteSessId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 4),
    _WfMplsLdpCfgRouteSessId_Type()
)
wfMplsLdpCfgRouteSessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpCfgRouteSessId.setStatus("mandatory")
_WfMplsLdpCfgRouteIndex_Type = Integer32
_WfMplsLdpCfgRouteIndex_Object = MibTableColumn
wfMplsLdpCfgRouteIndex = _WfMplsLdpCfgRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 5),
    _WfMplsLdpCfgRouteIndex_Type()
)
wfMplsLdpCfgRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpCfgRouteIndex.setStatus("mandatory")
_WfMplsLdpCfgRouteDestination_Type = IpAddress
_WfMplsLdpCfgRouteDestination_Object = MibTableColumn
wfMplsLdpCfgRouteDestination = _WfMplsLdpCfgRouteDestination_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 6),
    _WfMplsLdpCfgRouteDestination_Type()
)
wfMplsLdpCfgRouteDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpCfgRouteDestination.setStatus("mandatory")
_WfMplsLdpCfgRouteMask_Type = IpAddress
_WfMplsLdpCfgRouteMask_Object = MibTableColumn
wfMplsLdpCfgRouteMask = _WfMplsLdpCfgRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 7),
    _WfMplsLdpCfgRouteMask_Type()
)
wfMplsLdpCfgRouteMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMplsLdpCfgRouteMask.setStatus("mandatory")


class _WfMplsLdpCfgRouteState_Type(Integer32):
    """Custom type wfMplsLdpCfgRouteState based on Integer32"""
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


_WfMplsLdpCfgRouteState_Type.__name__ = "Integer32"
_WfMplsLdpCfgRouteState_Object = MibTableColumn
wfMplsLdpCfgRouteState = _WfMplsLdpCfgRouteState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 3, 1, 8),
    _WfMplsLdpCfgRouteState_Type()
)
wfMplsLdpCfgRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpCfgRouteState.setStatus("mandatory")
_WfMplsLdpLibTable_Object = MibTable
wfMplsLdpLibTable = _WfMplsLdpLibTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4)
)
if mibBuilder.loadTexts:
    wfMplsLdpLibTable.setStatus("mandatory")
_WfMplsLdpLibEntry_Object = MibTableRow
wfMplsLdpLibEntry = _WfMplsLdpLibEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1)
)
wfMplsLdpLibEntry.setIndexNames(
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibCct"),
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibSessId"),
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibDest"),
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibMid"),
    (0, "Wellfleet-MPLS-LDP-MIB", "wfMplsLdpLibIndex"),
)
if mibBuilder.loadTexts:
    wfMplsLdpLibEntry.setStatus("mandatory")


class _WfMplsLdpLibCct_Type(Integer32):
    """Custom type wfMplsLdpLibCct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfMplsLdpLibCct_Type.__name__ = "Integer32"
_WfMplsLdpLibCct_Object = MibTableColumn
wfMplsLdpLibCct = _WfMplsLdpLibCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 1),
    _WfMplsLdpLibCct_Type()
)
wfMplsLdpLibCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpLibCct.setStatus("mandatory")


class _WfMplsLdpLibSessId_Type(Integer32):
    """Custom type wfMplsLdpLibSessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfMplsLdpLibSessId_Type.__name__ = "Integer32"
_WfMplsLdpLibSessId_Object = MibTableColumn
wfMplsLdpLibSessId = _WfMplsLdpLibSessId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 2),
    _WfMplsLdpLibSessId_Type()
)
wfMplsLdpLibSessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpLibSessId.setStatus("mandatory")
_WfMplsLdpLibDest_Type = IpAddress
_WfMplsLdpLibDest_Object = MibTableColumn
wfMplsLdpLibDest = _WfMplsLdpLibDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 3),
    _WfMplsLdpLibDest_Type()
)
wfMplsLdpLibDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpLibDest.setStatus("mandatory")
_WfMplsLdpLibMid_Type = Integer32
_WfMplsLdpLibMid_Object = MibTableColumn
wfMplsLdpLibMid = _WfMplsLdpLibMid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 4),
    _WfMplsLdpLibMid_Type()
)
wfMplsLdpLibMid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpLibMid.setStatus("mandatory")
_WfMplsLdpLibLabel_Type = Integer32
_WfMplsLdpLibLabel_Object = MibTableColumn
wfMplsLdpLibLabel = _WfMplsLdpLibLabel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 5),
    _WfMplsLdpLibLabel_Type()
)
wfMplsLdpLibLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpLibLabel.setStatus("mandatory")


class _WfMplsLdpLibEncaps_Type(Integer32):
    """Custom type wfMplsLdpLibEncaps based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llcsnap", 1),
          ("null", 2))
    )


_WfMplsLdpLibEncaps_Type.__name__ = "Integer32"
_WfMplsLdpLibEncaps_Object = MibTableColumn
wfMplsLdpLibEncaps = _WfMplsLdpLibEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 6),
    _WfMplsLdpLibEncaps_Type()
)
wfMplsLdpLibEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpLibEncaps.setStatus("mandatory")


class _WfMplsLdpLibDirection_Type(Integer32):
    """Custom type wfMplsLdpLibDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("inbound", 1),
          ("outbound", 2))
    )


_WfMplsLdpLibDirection_Type.__name__ = "Integer32"
_WfMplsLdpLibDirection_Object = MibTableColumn
wfMplsLdpLibDirection = _WfMplsLdpLibDirection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 7),
    _WfMplsLdpLibDirection_Type()
)
wfMplsLdpLibDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpLibDirection.setStatus("mandatory")
_WfMplsLdpLibSlot_Type = Integer32
_WfMplsLdpLibSlot_Object = MibTableColumn
wfMplsLdpLibSlot = _WfMplsLdpLibSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 8),
    _WfMplsLdpLibSlot_Type()
)
wfMplsLdpLibSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpLibSlot.setStatus("mandatory")
_WfMplsLdpLibIndex_Type = Integer32
_WfMplsLdpLibIndex_Object = MibTableColumn
wfMplsLdpLibIndex = _WfMplsLdpLibIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 9, 15, 4, 1, 9),
    _WfMplsLdpLibIndex_Type()
)
wfMplsLdpLibIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfMplsLdpLibIndex.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-MPLS-LDP-MIB",
    **{"wfMplsLdpSessCfgTable": wfMplsLdpSessCfgTable,
       "wfMplsLdpSessCfgEntry": wfMplsLdpSessCfgEntry,
       "wfMplsLdpSessCfgCreate": wfMplsLdpSessCfgCreate,
       "wfMplsLdpSessCfgEnable": wfMplsLdpSessCfgEnable,
       "wfMplsLdpSessCfgSlot": wfMplsLdpSessCfgSlot,
       "wfMplsLdpSessCfgIndex": wfMplsLdpSessCfgIndex,
       "wfMplsLdpSessCfgCircuit": wfMplsLdpSessCfgCircuit,
       "wfMplsLdpSessCfgLocalIpAddress": wfMplsLdpSessCfgLocalIpAddress,
       "wfMplsLdpSessCfgLocalTcpPort": wfMplsLdpSessCfgLocalTcpPort,
       "wfMplsLdpSessCfgRemoteIpAddress": wfMplsLdpSessCfgRemoteIpAddress,
       "wfMplsLdpSessCfgRemoteTcpPort": wfMplsLdpSessCfgRemoteTcpPort,
       "wfMplsLdpSessCfgRoutesConfigMode": wfMplsLdpSessCfgRoutesConfigMode,
       "wfMplsLdpSessCfgHoldTime": wfMplsLdpSessCfgHoldTime,
       "wfMplsLdpSessCfgProto": wfMplsLdpSessCfgProto,
       "wfMplsLdpSessCfgAggregation": wfMplsLdpSessCfgAggregation,
       "wfMplsLdpSessCfgDebugLevel": wfMplsLdpSessCfgDebugLevel,
       "wfMplsLdpSessCfgReqBindRetryTime": wfMplsLdpSessCfgReqBindRetryTime,
       "wfMplsLdpSessCfgReqBindRetries": wfMplsLdpSessCfgReqBindRetries,
       "wfMplsLdpSessActualTable": wfMplsLdpSessActualTable,
       "wfMplsLdpSessActualEntry": wfMplsLdpSessActualEntry,
       "wfMplsLdpSessActualIndex": wfMplsLdpSessActualIndex,
       "wfMplsLdpSessActualCircuit": wfMplsLdpSessActualCircuit,
       "wfMplsLdpSessActualState": wfMplsLdpSessActualState,
       "wfMplsLdpSessActualPeerState": wfMplsLdpSessActualPeerState,
       "wfMplsLdpSessActualLocalIpAddress": wfMplsLdpSessActualLocalIpAddress,
       "wfMplsLdpSessActualLocalTcpPort": wfMplsLdpSessActualLocalTcpPort,
       "wfMplsLdpSessActualRemoteIpAddress": wfMplsLdpSessActualRemoteIpAddress,
       "wfMplsLdpSessActualRemoteTcpPort": wfMplsLdpSessActualRemoteTcpPort,
       "wfMplsLdpSessActualHoldTime": wfMplsLdpSessActualHoldTime,
       "wfMplsLdpSessActualRoutesConfigMode": wfMplsLdpSessActualRoutesConfigMode,
       "wfMplsLdpSessActualTCPConnectionRole": wfMplsLdpSessActualTCPConnectionRole,
       "wfMplsLdpSessActualSlot": wfMplsLdpSessActualSlot,
       "wfMplsLdpCfgRouteTable": wfMplsLdpCfgRouteTable,
       "wfMplsLdpCfgRouteEntry": wfMplsLdpCfgRouteEntry,
       "wfMplsLdpCfgRouteCreate": wfMplsLdpCfgRouteCreate,
       "wfMplsLdpCfgRouteEnable": wfMplsLdpCfgRouteEnable,
       "wfMplsLdpCfgRouteCct": wfMplsLdpCfgRouteCct,
       "wfMplsLdpCfgRouteSessId": wfMplsLdpCfgRouteSessId,
       "wfMplsLdpCfgRouteIndex": wfMplsLdpCfgRouteIndex,
       "wfMplsLdpCfgRouteDestination": wfMplsLdpCfgRouteDestination,
       "wfMplsLdpCfgRouteMask": wfMplsLdpCfgRouteMask,
       "wfMplsLdpCfgRouteState": wfMplsLdpCfgRouteState,
       "wfMplsLdpLibTable": wfMplsLdpLibTable,
       "wfMplsLdpLibEntry": wfMplsLdpLibEntry,
       "wfMplsLdpLibCct": wfMplsLdpLibCct,
       "wfMplsLdpLibSessId": wfMplsLdpLibSessId,
       "wfMplsLdpLibDest": wfMplsLdpLibDest,
       "wfMplsLdpLibMid": wfMplsLdpLibMid,
       "wfMplsLdpLibLabel": wfMplsLdpLibLabel,
       "wfMplsLdpLibEncaps": wfMplsLdpLibEncaps,
       "wfMplsLdpLibDirection": wfMplsLdpLibDirection,
       "wfMplsLdpLibSlot": wfMplsLdpLibSlot,
       "wfMplsLdpLibIndex": wfMplsLdpLibIndex}
)
