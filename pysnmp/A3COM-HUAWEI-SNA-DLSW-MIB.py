# SNMP MIB module (A3COM-HUAWEI-SNA-DLSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-SNA-DLSW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:04 2024
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

(hwproducts,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "hwproducts")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# MODULE-IDENTITY

dlsw = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MacAddressNC(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )



class EndStationLocation(Integer32, TextualConvention):
    status = "current"
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
        *(("internal", 2),
          ("local", 4),
          ("other", 1),
          ("remote", 3))
    )



class DlcType(Integer32, TextualConvention):
    status = "current"
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
        *(("llc", 3),
          ("na", 2),
          ("other", 1),
          ("qllc", 5),
          ("sdlc", 4))
    )



class LFSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(516,
              1470,
              1500,
              2052,
              4472,
              8144,
              11407,
              11454,
              17800,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("lfs11407", 11407),
          ("lfs11454", 11454),
          ("lfs1470", 1470),
          ("lfs1500", 1500),
          ("lfs17800", 17800),
          ("lfs2052", 2052),
          ("lfs4472", 4472),
          ("lfs516", 516),
          ("lfs8144", 8144),
          ("unknown", 65535))
    )



class CreateLineFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createLine", 1),
          ("deleteLine", 2))
    )



class EntryStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )



# MIB Managed Objects in the order of their OIDs

_DlswNode_ObjectIdentity = ObjectIdentity
dlswNode = _DlswNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1)
)


class _DlswNodeVersion_Type(OctetString):
    """Custom type dlswNodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DlswNodeVersion_Type.__name__ = "OctetString"
_DlswNodeVersion_Object = MibScalar
dlswNodeVersion = _DlswNodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 1),
    _DlswNodeVersion_Type()
)
dlswNodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswNodeVersion.setStatus("current")


class _DlswNodeVendorID_Type(OctetString):
    """Custom type dlswNodeVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DlswNodeVendorID_Type.__name__ = "OctetString"
_DlswNodeVendorID_Object = MibScalar
dlswNodeVendorID = _DlswNodeVendorID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 2),
    _DlswNodeVendorID_Type()
)
dlswNodeVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswNodeVendorID.setStatus("current")
_DlswNodeVersionString_Type = DisplayString
_DlswNodeVersionString_Object = MibScalar
dlswNodeVersionString = _DlswNodeVersionString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 3),
    _DlswNodeVersionString_Type()
)
dlswNodeVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswNodeVersionString.setStatus("current")


class _DlswNodeStdPacingSupport_Type(Integer32):
    """Custom type dlswNodeStdPacingSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("adaptiveRcvWindow", 2),
          ("fixedRcvWindow", 3),
          ("none", 1),
          ("unknown", 65535))
    )


_DlswNodeStdPacingSupport_Type.__name__ = "Integer32"
_DlswNodeStdPacingSupport_Object = MibScalar
dlswNodeStdPacingSupport = _DlswNodeStdPacingSupport_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 4),
    _DlswNodeStdPacingSupport_Type()
)
dlswNodeStdPacingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswNodeStdPacingSupport.setStatus("current")


class _DlswNodeStatus_Type(Integer32):
    """Custom type dlswNodeStatus based on Integer32"""
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


_DlswNodeStatus_Type.__name__ = "Integer32"
_DlswNodeStatus_Object = MibScalar
dlswNodeStatus = _DlswNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 5),
    _DlswNodeStatus_Type()
)
dlswNodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeStatus.setStatus("current")
_DlswNodeUpTime_Type = Integer32
_DlswNodeUpTime_Object = MibScalar
dlswNodeUpTime = _DlswNodeUpTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 6),
    _DlswNodeUpTime_Type()
)
dlswNodeUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswNodeUpTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    dlswNodeUpTime.setUnits("second")


class _DlswNodeVirtualSegmentLFSize_Type(LFSize):
    """Custom type dlswNodeVirtualSegmentLFSize based on LFSize"""


_DlswNodeVirtualSegmentLFSize_Object = MibScalar
dlswNodeVirtualSegmentLFSize = _DlswNodeVirtualSegmentLFSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 7),
    _DlswNodeVirtualSegmentLFSize_Type()
)
dlswNodeVirtualSegmentLFSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeVirtualSegmentLFSize.setStatus("current")
_DlswNodeLocalAddr_Type = IpAddress
_DlswNodeLocalAddr_Object = MibScalar
dlswNodeLocalAddr = _DlswNodeLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 8),
    _DlswNodeLocalAddr_Type()
)
dlswNodeLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeLocalAddr.setStatus("current")


class _DlswNodePriority_Type(Integer32):
    """Custom type dlswNodePriority based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
        ValueRangeConstraint(65535, 65535),
    )


_DlswNodePriority_Type.__name__ = "Integer32"
_DlswNodePriority_Object = MibScalar
dlswNodePriority = _DlswNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 9),
    _DlswNodePriority_Type()
)
dlswNodePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodePriority.setStatus("current")


class _DlswNodeInitWindow_Type(Integer32):
    """Custom type dlswNodeInitWindow based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_DlswNodeInitWindow_Type.__name__ = "Integer32"
_DlswNodeInitWindow_Object = MibScalar
dlswNodeInitWindow = _DlswNodeInitWindow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 10),
    _DlswNodeInitWindow_Type()
)
dlswNodeInitWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeInitWindow.setStatus("current")


class _DlswNodeKeepAlive_Type(Integer32):
    """Custom type dlswNodeKeepAlive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_DlswNodeKeepAlive_Type.__name__ = "Integer32"
_DlswNodeKeepAlive_Object = MibScalar
dlswNodeKeepAlive = _DlswNodeKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 11),
    _DlswNodeKeepAlive_Type()
)
dlswNodeKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeKeepAlive.setStatus("current")


class _DlswNodeMaxWindow_Type(Integer32):
    """Custom type dlswNodeMaxWindow based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_DlswNodeMaxWindow_Type.__name__ = "Integer32"
_DlswNodeMaxWindow_Object = MibScalar
dlswNodeMaxWindow = _DlswNodeMaxWindow_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 12),
    _DlswNodeMaxWindow_Type()
)
dlswNodeMaxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeMaxWindow.setStatus("current")


class _DlswNodePermitDynamic_Type(Integer32):
    """Custom type dlswNodePermitDynamic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("forbidDynamic", 2),
          ("permitDynamic", 1),
          ("unknown", 65535))
    )


_DlswNodePermitDynamic_Type.__name__ = "Integer32"
_DlswNodePermitDynamic_Object = MibScalar
dlswNodePermitDynamic = _DlswNodePermitDynamic_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 13),
    _DlswNodePermitDynamic_Type()
)
dlswNodePermitDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodePermitDynamic.setStatus("current")


class _DlswNodeConnTimeout_Type(Integer32):
    """Custom type dlswNodeConnTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DlswNodeConnTimeout_Type.__name__ = "Integer32"
_DlswNodeConnTimeout_Object = MibScalar
dlswNodeConnTimeout = _DlswNodeConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 14),
    _DlswNodeConnTimeout_Type()
)
dlswNodeConnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeConnTimeout.setStatus("current")


class _DlswNodeLocalPendTimeout_Type(Integer32):
    """Custom type dlswNodeLocalPendTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DlswNodeLocalPendTimeout_Type.__name__ = "Integer32"
_DlswNodeLocalPendTimeout_Object = MibScalar
dlswNodeLocalPendTimeout = _DlswNodeLocalPendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 15),
    _DlswNodeLocalPendTimeout_Type()
)
dlswNodeLocalPendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeLocalPendTimeout.setStatus("current")


class _DlswNodeRemotePendTimeout_Type(Integer32):
    """Custom type dlswNodeRemotePendTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DlswNodeRemotePendTimeout_Type.__name__ = "Integer32"
_DlswNodeRemotePendTimeout_Object = MibScalar
dlswNodeRemotePendTimeout = _DlswNodeRemotePendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 16),
    _DlswNodeRemotePendTimeout_Type()
)
dlswNodeRemotePendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeRemotePendTimeout.setStatus("current")


class _DlswNodeSnaCacheTimeout_Type(Integer32):
    """Custom type dlswNodeSnaCacheTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DlswNodeSnaCacheTimeout_Type.__name__ = "Integer32"
_DlswNodeSnaCacheTimeout_Object = MibScalar
dlswNodeSnaCacheTimeout = _DlswNodeSnaCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 17),
    _DlswNodeSnaCacheTimeout_Type()
)
dlswNodeSnaCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswNodeSnaCacheTimeout.setStatus("current")
_DlswTrapControl_ObjectIdentity = ObjectIdentity
dlswTrapControl = _DlswTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 20)
)


class _DlswTrapCntlState_Type(Integer32):
    """Custom type dlswTrapCntlState based on Integer32"""
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


_DlswTrapCntlState_Type.__name__ = "Integer32"
_DlswTrapCntlState_Object = MibScalar
dlswTrapCntlState = _DlswTrapCntlState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 1, 20, 1),
    _DlswTrapCntlState_Type()
)
dlswTrapCntlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswTrapCntlState.setStatus("current")
_DlswTConn_ObjectIdentity = ObjectIdentity
dlswTConn = _DlswTConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2)
)
_DlswRemotePeerTable_Object = MibTable
dlswRemotePeerTable = _DlswRemotePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1)
)
if mibBuilder.loadTexts:
    dlswRemotePeerTable.setStatus("current")
_DlswRemotePeerEntry_Object = MibTableRow
dlswRemotePeerEntry = _DlswRemotePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1)
)
dlswRemotePeerEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SNA-DLSW-MIB", "dlswRemotePeerAddr"),
)
if mibBuilder.loadTexts:
    dlswRemotePeerEntry.setStatus("current")
_DlswRemotePeerAddr_Type = IpAddress
_DlswRemotePeerAddr_Object = MibTableColumn
dlswRemotePeerAddr = _DlswRemotePeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 1),
    _DlswRemotePeerAddr_Type()
)
dlswRemotePeerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dlswRemotePeerAddr.setStatus("current")


class _DlswRemotePeerVersion_Type(OctetString):
    """Custom type dlswRemotePeerVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DlswRemotePeerVersion_Type.__name__ = "OctetString"
_DlswRemotePeerVersion_Object = MibTableColumn
dlswRemotePeerVersion = _DlswRemotePeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 2),
    _DlswRemotePeerVersion_Type()
)
dlswRemotePeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerVersion.setStatus("current")


class _DlswRemotePeerVendorID_Type(OctetString):
    """Custom type dlswRemotePeerVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_DlswRemotePeerVendorID_Type.__name__ = "OctetString"
_DlswRemotePeerVendorID_Object = MibTableColumn
dlswRemotePeerVendorID = _DlswRemotePeerVendorID_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 3),
    _DlswRemotePeerVendorID_Type()
)
dlswRemotePeerVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerVendorID.setStatus("current")
_DlswRemotePeerPaceWindInit_Type = Integer32
_DlswRemotePeerPaceWindInit_Object = MibTableColumn
dlswRemotePeerPaceWindInit = _DlswRemotePeerPaceWindInit_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 4),
    _DlswRemotePeerPaceWindInit_Type()
)
dlswRemotePeerPaceWindInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerPaceWindInit.setStatus("current")


class _DlswRemotePeerNumOfTcpSessions_Type(Integer32):
    """Custom type dlswRemotePeerNumOfTcpSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DlswRemotePeerNumOfTcpSessions_Type.__name__ = "Integer32"
_DlswRemotePeerNumOfTcpSessions_Object = MibTableColumn
dlswRemotePeerNumOfTcpSessions = _DlswRemotePeerNumOfTcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 5),
    _DlswRemotePeerNumOfTcpSessions_Type()
)
dlswRemotePeerNumOfTcpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerNumOfTcpSessions.setStatus("obsolete")
_DlswRemotePeerVersionString_Type = DisplayString
_DlswRemotePeerVersionString_Object = MibTableColumn
dlswRemotePeerVersionString = _DlswRemotePeerVersionString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 6),
    _DlswRemotePeerVersionString_Type()
)
dlswRemotePeerVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerVersionString.setStatus("current")


class _DlswRemotePeerIsConfig_Type(Integer32):
    """Custom type dlswRemotePeerIsConfig based on Integer32"""
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


_DlswRemotePeerIsConfig_Type.__name__ = "Integer32"
_DlswRemotePeerIsConfig_Object = MibTableColumn
dlswRemotePeerIsConfig = _DlswRemotePeerIsConfig_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 7),
    _DlswRemotePeerIsConfig_Type()
)
dlswRemotePeerIsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerIsConfig.setStatus("current")


class _DlswRemotePeerSetStateToConfig_Type(Integer32):
    """Custom type dlswRemotePeerSetStateToConfig based on Integer32"""
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


_DlswRemotePeerSetStateToConfig_Type.__name__ = "Integer32"
_DlswRemotePeerSetStateToConfig_Object = MibTableColumn
dlswRemotePeerSetStateToConfig = _DlswRemotePeerSetStateToConfig_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 8),
    _DlswRemotePeerSetStateToConfig_Type()
)
dlswRemotePeerSetStateToConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerSetStateToConfig.setStatus("obsolete")


class _DlswRemotePeerCost_Type(Integer32):
    """Custom type dlswRemotePeerCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_DlswRemotePeerCost_Type.__name__ = "Integer32"
_DlswRemotePeerCost_Object = MibTableColumn
dlswRemotePeerCost = _DlswRemotePeerCost_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 9),
    _DlswRemotePeerCost_Type()
)
dlswRemotePeerCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswRemotePeerCost.setStatus("current")


class _DlswRemotePeerKeepAlive_Type(Integer32):
    """Custom type dlswRemotePeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_DlswRemotePeerKeepAlive_Type.__name__ = "Integer32"
_DlswRemotePeerKeepAlive_Object = MibTableColumn
dlswRemotePeerKeepAlive = _DlswRemotePeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 10),
    _DlswRemotePeerKeepAlive_Type()
)
dlswRemotePeerKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswRemotePeerKeepAlive.setStatus("current")
_DlswRemotePeerLf_Type = LFSize
_DlswRemotePeerLf_Object = MibTableColumn
dlswRemotePeerLf = _DlswRemotePeerLf_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 11),
    _DlswRemotePeerLf_Type()
)
dlswRemotePeerLf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswRemotePeerLf.setStatus("current")


class _DlswRemotePeerTcpQueneMax_Type(Integer32):
    """Custom type dlswRemotePeerTcpQueneMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 2000),
    )


_DlswRemotePeerTcpQueneMax_Type.__name__ = "Integer32"
_DlswRemotePeerTcpQueneMax_Object = MibTableColumn
dlswRemotePeerTcpQueneMax = _DlswRemotePeerTcpQueneMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 12),
    _DlswRemotePeerTcpQueneMax_Type()
)
dlswRemotePeerTcpQueneMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswRemotePeerTcpQueneMax.setStatus("current")


class _DlswRemotePeerHaveBackup_Type(Integer32):
    """Custom type dlswRemotePeerHaveBackup based on Integer32"""
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


_DlswRemotePeerHaveBackup_Type.__name__ = "Integer32"
_DlswRemotePeerHaveBackup_Object = MibTableColumn
dlswRemotePeerHaveBackup = _DlswRemotePeerHaveBackup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 13),
    _DlswRemotePeerHaveBackup_Type()
)
dlswRemotePeerHaveBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerHaveBackup.setStatus("current")


class _DlswRemotePeerIsBackup_Type(Integer32):
    """Custom type dlswRemotePeerIsBackup based on Integer32"""
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


_DlswRemotePeerIsBackup_Type.__name__ = "Integer32"
_DlswRemotePeerIsBackup_Object = MibTableColumn
dlswRemotePeerIsBackup = _DlswRemotePeerIsBackup_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 14),
    _DlswRemotePeerIsBackup_Type()
)
dlswRemotePeerIsBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerIsBackup.setStatus("current")
_DlswRemotePeerBackupAddr_Type = IpAddress
_DlswRemotePeerBackupAddr_Object = MibTableColumn
dlswRemotePeerBackupAddr = _DlswRemotePeerBackupAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 15),
    _DlswRemotePeerBackupAddr_Type()
)
dlswRemotePeerBackupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerBackupAddr.setStatus("current")


class _DlswRemotePeerLinger_Type(Integer32):
    """Custom type dlswRemotePeerLinger based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_DlswRemotePeerLinger_Type.__name__ = "Integer32"
_DlswRemotePeerLinger_Object = MibTableColumn
dlswRemotePeerLinger = _DlswRemotePeerLinger_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 16),
    _DlswRemotePeerLinger_Type()
)
dlswRemotePeerLinger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswRemotePeerLinger.setStatus("current")


class _DlswRemotePeerLinkState_Type(Integer32):
    """Custom type dlswRemotePeerLinkState based on Integer32"""
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
        *(("connected", 3),
          ("connecting", 1),
          ("disconnected", 6),
          ("disconnecting", 5),
          ("initCapExchange", 2),
          ("quiescing", 4))
    )


_DlswRemotePeerLinkState_Type.__name__ = "Integer32"
_DlswRemotePeerLinkState_Object = MibTableColumn
dlswRemotePeerLinkState = _DlswRemotePeerLinkState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 17),
    _DlswRemotePeerLinkState_Type()
)
dlswRemotePeerLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerLinkState.setStatus("current")
_DlswRemotePeerRecvPacks_Type = Counter32
_DlswRemotePeerRecvPacks_Object = MibTableColumn
dlswRemotePeerRecvPacks = _DlswRemotePeerRecvPacks_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 18),
    _DlswRemotePeerRecvPacks_Type()
)
dlswRemotePeerRecvPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerRecvPacks.setStatus("current")
_DlswRemotePeerSendPacks_Type = Counter32
_DlswRemotePeerSendPacks_Object = MibTableColumn
dlswRemotePeerSendPacks = _DlswRemotePeerSendPacks_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 19),
    _DlswRemotePeerSendPacks_Type()
)
dlswRemotePeerSendPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerSendPacks.setStatus("current")
_DlswRemotePeerDrops_Type = Counter32
_DlswRemotePeerDrops_Object = MibTableColumn
dlswRemotePeerDrops = _DlswRemotePeerDrops_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 20),
    _DlswRemotePeerDrops_Type()
)
dlswRemotePeerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerDrops.setStatus("current")
_DlswRemotePeerUptime_Type = Counter32
_DlswRemotePeerUptime_Object = MibTableColumn
dlswRemotePeerUptime = _DlswRemotePeerUptime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 21),
    _DlswRemotePeerUptime_Type()
)
dlswRemotePeerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswRemotePeerUptime.setStatus("current")
_DlswRemotePeerEntryStatus_Type = EntryStatus
_DlswRemotePeerEntryStatus_Object = MibTableColumn
dlswRemotePeerEntryStatus = _DlswRemotePeerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 2, 1, 1, 22),
    _DlswRemotePeerEntryStatus_Type()
)
dlswRemotePeerEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswRemotePeerEntryStatus.setStatus("current")
_DlswBridgeGroup_ObjectIdentity = ObjectIdentity
dlswBridgeGroup = _DlswBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 3)
)
_DlswBridgeTable_Object = MibTable
dlswBridgeTable = _DlswBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 3, 1)
)
if mibBuilder.loadTexts:
    dlswBridgeTable.setStatus("current")
_DlswBridgeEntry_Object = MibTableRow
dlswBridgeEntry = _DlswBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 3, 1, 1)
)
dlswBridgeEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SNA-DLSW-MIB", "dlswBridgeNum"),
)
if mibBuilder.loadTexts:
    dlswBridgeEntry.setStatus("current")


class _DlswBridgeNum_Type(Integer32):
    """Custom type dlswBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_DlswBridgeNum_Type.__name__ = "Integer32"
_DlswBridgeNum_Object = MibTableColumn
dlswBridgeNum = _DlswBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 3, 1, 1, 1),
    _DlswBridgeNum_Type()
)
dlswBridgeNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswBridgeNum.setStatus("current")
_DlswBridgeStatus_Type = CreateLineFlag
_DlswBridgeStatus_Object = MibTableColumn
dlswBridgeStatus = _DlswBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 3, 1, 1, 2),
    _DlswBridgeStatus_Type()
)
dlswBridgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswBridgeStatus.setStatus("current")
_DlswBridgeIfTable_Object = MibTable
dlswBridgeIfTable = _DlswBridgeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 3, 2)
)
if mibBuilder.loadTexts:
    dlswBridgeIfTable.setStatus("current")
_DlswBridgeIfEntry_Object = MibTableRow
dlswBridgeIfEntry = _DlswBridgeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 3, 2, 1)
)
dlswBridgeIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dlswBridgeIfEntry.setStatus("current")


class _DlswBridgeIfBriGru_Type(Integer32):
    """Custom type dlswBridgeIfBriGru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_DlswBridgeIfBriGru_Type.__name__ = "Integer32"
_DlswBridgeIfBriGru_Object = MibTableColumn
dlswBridgeIfBriGru = _DlswBridgeIfBriGru_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 3, 2, 1, 1),
    _DlswBridgeIfBriGru_Type()
)
dlswBridgeIfBriGru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswBridgeIfBriGru.setStatus("current")
_DlswBridgeIfName_Type = DisplayString
_DlswBridgeIfName_Object = MibTableColumn
dlswBridgeIfName = _DlswBridgeIfName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 3, 2, 1, 2),
    _DlswBridgeIfName_Type()
)
dlswBridgeIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswBridgeIfName.setStatus("current")
_DlswBridgeIfStatus_Type = EntryStatus
_DlswBridgeIfStatus_Object = MibTableColumn
dlswBridgeIfStatus = _DlswBridgeIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 3, 2, 1, 3),
    _DlswBridgeIfStatus_Type()
)
dlswBridgeIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswBridgeIfStatus.setStatus("current")
_DlswLocDirectory_ObjectIdentity = ObjectIdentity
dlswLocDirectory = _DlswLocDirectory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 4)
)
_DlswLocMacTable_Object = MibTable
dlswLocMacTable = _DlswLocMacTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 4, 1)
)
if mibBuilder.loadTexts:
    dlswLocMacTable.setStatus("current")
_DlswLocMacEntry_Object = MibTableRow
dlswLocMacEntry = _DlswLocMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 4, 1, 1)
)
dlswLocMacEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SNA-DLSW-MIB", "dlswLocMacHashIndex"),
    (0, "A3COM-HUAWEI-SNA-DLSW-MIB", "dlswLocMacHashIndexSeqNum"),
)
if mibBuilder.loadTexts:
    dlswLocMacEntry.setStatus("current")
_DlswLocMacHashIndex_Type = Integer32
_DlswLocMacHashIndex_Object = MibTableColumn
dlswLocMacHashIndex = _DlswLocMacHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 4, 1, 1, 1),
    _DlswLocMacHashIndex_Type()
)
dlswLocMacHashIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswLocMacHashIndex.setStatus("current")
_DlswLocMacHashIndexSeqNum_Type = Integer32
_DlswLocMacHashIndexSeqNum_Object = MibTableColumn
dlswLocMacHashIndexSeqNum = _DlswLocMacHashIndexSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 4, 1, 1, 2),
    _DlswLocMacHashIndexSeqNum_Type()
)
dlswLocMacHashIndexSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswLocMacHashIndexSeqNum.setStatus("current")
_DlswLocMacMac_Type = MacAddressNC
_DlswLocMacMac_Object = MibTableColumn
dlswLocMacMac = _DlswLocMacMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 4, 1, 1, 3),
    _DlswLocMacMac_Type()
)
dlswLocMacMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswLocMacMac.setStatus("current")
_DlswLocMacLocalInterfaceName_Type = DisplayString
_DlswLocMacLocalInterfaceName_Object = MibTableColumn
dlswLocMacLocalInterfaceName = _DlswLocMacLocalInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 4, 1, 1, 4),
    _DlswLocMacLocalInterfaceName_Type()
)
dlswLocMacLocalInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswLocMacLocalInterfaceName.setStatus("current")
_DlswCircuit_ObjectIdentity = ObjectIdentity
dlswCircuit = _DlswCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5)
)
_DlswCircuitTable_Object = MibTable
dlswCircuitTable = _DlswCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1)
)
if mibBuilder.loadTexts:
    dlswCircuitTable.setStatus("current")
_DlswCircuitEntry_Object = MibTableRow
dlswCircuitEntry = _DlswCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1)
)
dlswCircuitEntry.setIndexNames(
    (0, "A3COM-HUAWEI-SNA-DLSW-MIB", "dlswCircuitS1CircuitId"),
)
if mibBuilder.loadTexts:
    dlswCircuitEntry.setStatus("current")
_DlswCircuitS1CircuitId_Type = Integer32
_DlswCircuitS1CircuitId_Object = MibTableColumn
dlswCircuitS1CircuitId = _DlswCircuitS1CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 1),
    _DlswCircuitS1CircuitId_Type()
)
dlswCircuitS1CircuitId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dlswCircuitS1CircuitId.setStatus("current")
_DlswCircuitS1Mac_Type = MacAddressNC
_DlswCircuitS1Mac_Object = MibTableColumn
dlswCircuitS1Mac = _DlswCircuitS1Mac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 2),
    _DlswCircuitS1Mac_Type()
)
dlswCircuitS1Mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1Mac.setStatus("current")


class _DlswCircuitS1Sap_Type(OctetString):
    """Custom type dlswCircuitS1Sap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DlswCircuitS1Sap_Type.__name__ = "OctetString"
_DlswCircuitS1Sap_Object = MibTableColumn
dlswCircuitS1Sap = _DlswCircuitS1Sap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 3),
    _DlswCircuitS1Sap_Type()
)
dlswCircuitS1Sap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1Sap.setStatus("current")
_DlswCircuitS2Mac_Type = MacAddressNC
_DlswCircuitS2Mac_Object = MibTableColumn
dlswCircuitS2Mac = _DlswCircuitS2Mac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 4),
    _DlswCircuitS2Mac_Type()
)
dlswCircuitS2Mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2Mac.setStatus("current")


class _DlswCircuitS2Sap_Type(OctetString):
    """Custom type dlswCircuitS2Sap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DlswCircuitS2Sap_Type.__name__ = "OctetString"
_DlswCircuitS2Sap_Object = MibTableColumn
dlswCircuitS2Sap = _DlswCircuitS2Sap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 5),
    _DlswCircuitS2Sap_Type()
)
dlswCircuitS2Sap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2Sap.setStatus("current")


class _DlswCircuitS1IfIndex_Type(Integer32):
    """Custom type dlswCircuitS1IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlswCircuitS1IfIndex_Type.__name__ = "Integer32"
_DlswCircuitS1IfIndex_Object = MibTableColumn
dlswCircuitS1IfIndex = _DlswCircuitS1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 6),
    _DlswCircuitS1IfIndex_Type()
)
dlswCircuitS1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1IfIndex.setStatus("current")
_DlswCircuitS1Ifname_Type = DisplayString
_DlswCircuitS1Ifname_Object = MibTableColumn
dlswCircuitS1Ifname = _DlswCircuitS1Ifname_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 7),
    _DlswCircuitS1Ifname_Type()
)
dlswCircuitS1Ifname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1Ifname.setStatus("current")
_DlswCircuitS1DlcType_Type = DlcType
_DlswCircuitS1DlcType_Object = MibTableColumn
dlswCircuitS1DlcType = _DlswCircuitS1DlcType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 8),
    _DlswCircuitS1DlcType_Type()
)
dlswCircuitS1DlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS1DlcType.setStatus("current")
_DlswCircuitS2Location_Type = EndStationLocation
_DlswCircuitS2Location_Object = MibTableColumn
dlswCircuitS2Location = _DlswCircuitS2Location_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 9),
    _DlswCircuitS2Location_Type()
)
dlswCircuitS2Location.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2Location.setStatus("obsolete")
_DlswCircuitS2TAddress_Type = IpAddress
_DlswCircuitS2TAddress_Object = MibTableColumn
dlswCircuitS2TAddress = _DlswCircuitS2TAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 10),
    _DlswCircuitS2TAddress_Type()
)
dlswCircuitS2TAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2TAddress.setStatus("current")
_DlswCircuitS2CircuitId_Type = Integer32
_DlswCircuitS2CircuitId_Object = MibTableColumn
dlswCircuitS2CircuitId = _DlswCircuitS2CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 11),
    _DlswCircuitS2CircuitId_Type()
)
dlswCircuitS2CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitS2CircuitId.setStatus("current")


class _DlswCircuitOrigin_Type(Integer32):
    """Custom type dlswCircuitOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s1", 1),
          ("s2", 2))
    )


_DlswCircuitOrigin_Type.__name__ = "Integer32"
_DlswCircuitOrigin_Object = MibTableColumn
dlswCircuitOrigin = _DlswCircuitOrigin_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 12),
    _DlswCircuitOrigin_Type()
)
dlswCircuitOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitOrigin.setStatus("current")
_DlswCircuitEntryTime_Type = TimeTicks
_DlswCircuitEntryTime_Object = MibTableColumn
dlswCircuitEntryTime = _DlswCircuitEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 13),
    _DlswCircuitEntryTime_Type()
)
dlswCircuitEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitEntryTime.setStatus("current")
if mibBuilder.loadTexts:
    dlswCircuitEntryTime.setUnits("hundredths of a second")
_DlswCircuitStateTime_Type = TimeTicks
_DlswCircuitStateTime_Object = MibTableColumn
dlswCircuitStateTime = _DlswCircuitStateTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 14),
    _DlswCircuitStateTime_Type()
)
dlswCircuitStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitStateTime.setStatus("current")
if mibBuilder.loadTexts:
    dlswCircuitStateTime.setUnits("hundredths of a second")


class _DlswCircuitState_Type(Integer32):
    """Custom type dlswCircuitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("circuitEstablished", 5),
          ("circuitPending", 4),
          ("circuitRestart", 12),
          ("circuitStart", 2),
          ("connectPending", 6),
          ("connected", 8),
          ("contactPending", 7),
          ("disconnectPending", 9),
          ("disconnected", 1),
          ("haltPending", 10),
          ("haltPendingNoack", 11),
          ("resolvePending", 3),
          ("restartPending", 13))
    )


_DlswCircuitState_Type.__name__ = "Integer32"
_DlswCircuitState_Object = MibTableColumn
dlswCircuitState = _DlswCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 15),
    _DlswCircuitState_Type()
)
dlswCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitState.setStatus("current")


class _DlswCircuitPriority_Type(Integer32):
    """Custom type dlswCircuitPriority based on Integer32"""
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
        *(("high", 4),
          ("highest", 5),
          ("low", 2),
          ("medium", 3),
          ("unsupported", 1))
    )


_DlswCircuitPriority_Type.__name__ = "Integer32"
_DlswCircuitPriority_Object = MibTableColumn
dlswCircuitPriority = _DlswCircuitPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 16),
    _DlswCircuitPriority_Type()
)
dlswCircuitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitPriority.setStatus("obsolete")


class _DlswCircuitFCSendGrantedUnits_Type(Integer32):
    """Custom type dlswCircuitFCSendGrantedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCSendGrantedUnits_Type.__name__ = "Integer32"
_DlswCircuitFCSendGrantedUnits_Object = MibTableColumn
dlswCircuitFCSendGrantedUnits = _DlswCircuitFCSendGrantedUnits_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 17),
    _DlswCircuitFCSendGrantedUnits_Type()
)
dlswCircuitFCSendGrantedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCSendGrantedUnits.setStatus("current")


class _DlswCircuitFCSendCurrentWndw_Type(Integer32):
    """Custom type dlswCircuitFCSendCurrentWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCSendCurrentWndw_Type.__name__ = "Integer32"
_DlswCircuitFCSendCurrentWndw_Object = MibTableColumn
dlswCircuitFCSendCurrentWndw = _DlswCircuitFCSendCurrentWndw_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 18),
    _DlswCircuitFCSendCurrentWndw_Type()
)
dlswCircuitFCSendCurrentWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCSendCurrentWndw.setStatus("current")


class _DlswCircuitFCRecvGrantedUnits_Type(Integer32):
    """Custom type dlswCircuitFCRecvGrantedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCRecvGrantedUnits_Type.__name__ = "Integer32"
_DlswCircuitFCRecvGrantedUnits_Object = MibTableColumn
dlswCircuitFCRecvGrantedUnits = _DlswCircuitFCRecvGrantedUnits_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 19),
    _DlswCircuitFCRecvGrantedUnits_Type()
)
dlswCircuitFCRecvGrantedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCRecvGrantedUnits.setStatus("current")


class _DlswCircuitFCRecvCurrentWndw_Type(Integer32):
    """Custom type dlswCircuitFCRecvCurrentWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DlswCircuitFCRecvCurrentWndw_Type.__name__ = "Integer32"
_DlswCircuitFCRecvCurrentWndw_Object = MibTableColumn
dlswCircuitFCRecvCurrentWndw = _DlswCircuitFCRecvCurrentWndw_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 20),
    _DlswCircuitFCRecvCurrentWndw_Type()
)
dlswCircuitFCRecvCurrentWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCRecvCurrentWndw.setStatus("current")
_DlswCircuitFCLargestRecvGranted_Type = Gauge32
_DlswCircuitFCLargestRecvGranted_Object = MibTableColumn
dlswCircuitFCLargestRecvGranted = _DlswCircuitFCLargestRecvGranted_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 21),
    _DlswCircuitFCLargestRecvGranted_Type()
)
dlswCircuitFCLargestRecvGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCLargestRecvGranted.setStatus("obsolete")
_DlswCircuitFCLargestSendGranted_Type = Gauge32
_DlswCircuitFCLargestSendGranted_Object = MibTableColumn
dlswCircuitFCLargestSendGranted = _DlswCircuitFCLargestSendGranted_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 5, 1, 1, 22),
    _DlswCircuitFCLargestSendGranted_Type()
)
dlswCircuitFCLargestSendGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswCircuitFCLargestSendGranted.setStatus("obsolete")
_DlswSdlc_ObjectIdentity = ObjectIdentity
dlswSdlc = _DlswSdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6)
)
_DlswSdlcPortTable_Object = MibTable
dlswSdlcPortTable = _DlswSdlcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1)
)
if mibBuilder.loadTexts:
    dlswSdlcPortTable.setStatus("current")
_DlswSdlcPortEntry_Object = MibTableRow
dlswSdlcPortEntry = _DlswSdlcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1)
)
dlswSdlcPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dlswSdlcPortEntry.setStatus("current")
_DlswSdlcPortSerialName_Type = DisplayString
_DlswSdlcPortSerialName_Object = MibTableColumn
dlswSdlcPortSerialName = _DlswSdlcPortSerialName_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 1),
    _DlswSdlcPortSerialName_Type()
)
dlswSdlcPortSerialName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswSdlcPortSerialName.setStatus("current")


class _DlswSdlcPortEncap_Type(Integer32):
    """Custom type dlswSdlcPortEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("ppp", 2),
          ("sdlc", 1))
    )


_DlswSdlcPortEncap_Type.__name__ = "Integer32"
_DlswSdlcPortEncap_Object = MibTableColumn
dlswSdlcPortEncap = _DlswSdlcPortEncap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 2),
    _DlswSdlcPortEncap_Type()
)
dlswSdlcPortEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswSdlcPortEncap.setStatus("current")


class _DlswSdlcPortRole_Type(Integer32):
    """Custom type dlswSdlcPortRole based on Integer32"""
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
        *(("norole", 3),
          ("primary", 1),
          ("seconday", 2))
    )


_DlswSdlcPortRole_Type.__name__ = "Integer32"
_DlswSdlcPortRole_Object = MibTableColumn
dlswSdlcPortRole = _DlswSdlcPortRole_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 3),
    _DlswSdlcPortRole_Type()
)
dlswSdlcPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortRole.setStatus("current")
_DlswSdlcPortVmac_Type = MacAddressNC
_DlswSdlcPortVmac_Object = MibTableColumn
dlswSdlcPortVmac = _DlswSdlcPortVmac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 4),
    _DlswSdlcPortVmac_Type()
)
dlswSdlcPortVmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortVmac.setStatus("current")


class _DlswSdlcPortHoldq_Type(Integer32):
    """Custom type dlswSdlcPortHoldq based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 255),
    )


_DlswSdlcPortHoldq_Type.__name__ = "Integer32"
_DlswSdlcPortHoldq_Object = MibTableColumn
dlswSdlcPortHoldq = _DlswSdlcPortHoldq_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 5),
    _DlswSdlcPortHoldq_Type()
)
dlswSdlcPortHoldq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortHoldq.setStatus("current")


class _DlswSdlcPortK_Type(Integer32):
    """Custom type dlswSdlcPortK based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_DlswSdlcPortK_Type.__name__ = "Integer32"
_DlswSdlcPortK_Object = MibTableColumn
dlswSdlcPortK = _DlswSdlcPortK_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 6),
    _DlswSdlcPortK_Type()
)
dlswSdlcPortK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortK.setStatus("current")


class _DlswSdlcPortModule_Type(Integer32):
    """Custom type dlswSdlcPortModule based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              128)
        )
    )
    namedValues = NamedValues(
        *(("m128", 128),
          ("m8", 8))
    )


_DlswSdlcPortModule_Type.__name__ = "Integer32"
_DlswSdlcPortModule_Object = MibTableColumn
dlswSdlcPortModule = _DlswSdlcPortModule_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 7),
    _DlswSdlcPortModule_Type()
)
dlswSdlcPortModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortModule.setStatus("current")


class _DlswSdlcPortN1_Type(Integer32):
    """Custom type dlswSdlcPortN1 based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17680),
    )


_DlswSdlcPortN1_Type.__name__ = "Integer32"
_DlswSdlcPortN1_Object = MibTableColumn
dlswSdlcPortN1 = _DlswSdlcPortN1_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 8),
    _DlswSdlcPortN1_Type()
)
dlswSdlcPortN1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortN1.setStatus("current")


class _DlswSdlcPortN2_Type(Integer32):
    """Custom type dlswSdlcPortN2 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DlswSdlcPortN2_Type.__name__ = "Integer32"
_DlswSdlcPortN2_Object = MibTableColumn
dlswSdlcPortN2 = _DlswSdlcPortN2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 9),
    _DlswSdlcPortN2_Type()
)
dlswSdlcPortN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortN2.setStatus("current")


class _DlswSdlcPortPollPauseTimer_Type(Integer32):
    """Custom type dlswSdlcPortPollPauseTimer based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_DlswSdlcPortPollPauseTimer_Type.__name__ = "Integer32"
_DlswSdlcPortPollPauseTimer_Object = MibTableColumn
dlswSdlcPortPollPauseTimer = _DlswSdlcPortPollPauseTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 10),
    _DlswSdlcPortPollPauseTimer_Type()
)
dlswSdlcPortPollPauseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortPollPauseTimer.setStatus("current")


class _DlswSdlcPortSimultaneousEnable_Type(Integer32):
    """Custom type dlswSdlcPortSimultaneousEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disenable", 2),
          ("enable", 1))
    )


_DlswSdlcPortSimultaneousEnable_Type.__name__ = "Integer32"
_DlswSdlcPortSimultaneousEnable_Object = MibTableColumn
dlswSdlcPortSimultaneousEnable = _DlswSdlcPortSimultaneousEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 11),
    _DlswSdlcPortSimultaneousEnable_Type()
)
dlswSdlcPortSimultaneousEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortSimultaneousEnable.setStatus("current")


class _DlswSdlcPortT1_Type(Integer32):
    """Custom type dlswSdlcPortT1 based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_DlswSdlcPortT1_Type.__name__ = "Integer32"
_DlswSdlcPortT1_Object = MibTableColumn
dlswSdlcPortT1 = _DlswSdlcPortT1_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 12),
    _DlswSdlcPortT1_Type()
)
dlswSdlcPortT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortT1.setStatus("current")


class _DlswSdlcPortT2_Type(Integer32):
    """Custom type dlswSdlcPortT2 based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_DlswSdlcPortT2_Type.__name__ = "Integer32"
_DlswSdlcPortT2_Object = MibTableColumn
dlswSdlcPortT2 = _DlswSdlcPortT2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 13),
    _DlswSdlcPortT2_Type()
)
dlswSdlcPortT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortT2.setStatus("current")


class _DlswSdlcPortNrziEncoding_Type(Integer32):
    """Custom type dlswSdlcPortNrziEncoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disenable", 2),
          ("enable", 1))
    )


_DlswSdlcPortNrziEncoding_Type.__name__ = "Integer32"
_DlswSdlcPortNrziEncoding_Object = MibTableColumn
dlswSdlcPortNrziEncoding = _DlswSdlcPortNrziEncoding_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 14),
    _DlswSdlcPortNrziEncoding_Type()
)
dlswSdlcPortNrziEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortNrziEncoding.setStatus("obsolete")


class _DlswSdlcPortIdleMarkEnable_Type(Integer32):
    """Custom type dlswSdlcPortIdleMarkEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disenable", 2),
          ("enable", 1))
    )


_DlswSdlcPortIdleMarkEnable_Type.__name__ = "Integer32"
_DlswSdlcPortIdleMarkEnable_Object = MibTableColumn
dlswSdlcPortIdleMarkEnable = _DlswSdlcPortIdleMarkEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 1, 1, 15),
    _DlswSdlcPortIdleMarkEnable_Type()
)
dlswSdlcPortIdleMarkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcPortIdleMarkEnable.setStatus("obsolete")
_DlswSdlcLsTable_Object = MibTable
dlswSdlcLsTable = _DlswSdlcLsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 2)
)
if mibBuilder.loadTexts:
    dlswSdlcLsTable.setStatus("current")
_DlswSdlcLsEntry_Object = MibTableRow
dlswSdlcLsEntry = _DlswSdlcLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 2, 1)
)
dlswSdlcLsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-SNA-DLSW-MIB", "dlswSdlcLsAddress"),
)
if mibBuilder.loadTexts:
    dlswSdlcLsEntry.setStatus("current")


class _DlswSdlcLsAddress_Type(Integer32):
    """Custom type dlswSdlcLsAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DlswSdlcLsAddress_Type.__name__ = "Integer32"
_DlswSdlcLsAddress_Object = MibTableColumn
dlswSdlcLsAddress = _DlswSdlcLsAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 2, 1, 1),
    _DlswSdlcLsAddress_Type()
)
dlswSdlcLsAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dlswSdlcLsAddress.setStatus("current")


class _DlswSdlcLsLocalId_Type(Integer32):
    """Custom type dlswSdlcLsLocalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DlswSdlcLsLocalId_Type.__name__ = "Integer32"
_DlswSdlcLsLocalId_Object = MibTableColumn
dlswSdlcLsLocalId = _DlswSdlcLsLocalId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 2, 1, 2),
    _DlswSdlcLsLocalId_Type()
)
dlswSdlcLsLocalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcLsLocalId.setStatus("current")
_DlswSdlcLsRemoteMac_Type = MacAddressNC
_DlswSdlcLsRemoteMac_Object = MibTableColumn
dlswSdlcLsRemoteMac = _DlswSdlcLsRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 2, 1, 3),
    _DlswSdlcLsRemoteMac_Type()
)
dlswSdlcLsRemoteMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcLsRemoteMac.setStatus("current")


class _DlswSdlcLsSsap_Type(Integer32):
    """Custom type dlswSdlcLsSsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DlswSdlcLsSsap_Type.__name__ = "Integer32"
_DlswSdlcLsSsap_Object = MibTableColumn
dlswSdlcLsSsap = _DlswSdlcLsSsap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 2, 1, 4),
    _DlswSdlcLsSsap_Type()
)
dlswSdlcLsSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcLsSsap.setStatus("current")


class _DlswSdlcLsDsap_Type(Integer32):
    """Custom type dlswSdlcLsDsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DlswSdlcLsDsap_Type.__name__ = "Integer32"
_DlswSdlcLsDsap_Object = MibTableColumn
dlswSdlcLsDsap = _DlswSdlcLsDsap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 2, 1, 5),
    _DlswSdlcLsDsap_Type()
)
dlswSdlcLsDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcLsDsap.setStatus("current")
_DlswSdlcLsStatus_Type = EntryStatus
_DlswSdlcLsStatus_Object = MibTableColumn
dlswSdlcLsStatus = _DlswSdlcLsStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 6, 2, 1, 6),
    _DlswSdlcLsStatus_Type()
)
dlswSdlcLsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswSdlcLsStatus.setStatus("current")
_DlswLlc2_ObjectIdentity = ObjectIdentity
dlswLlc2 = _DlswLlc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7)
)
_DlswLlc2PortTable_Object = MibTable
dlswLlc2PortTable = _DlswLlc2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1)
)
if mibBuilder.loadTexts:
    dlswLlc2PortTable.setStatus("current")
_DlswLlc2PortEntry_Object = MibTableRow
dlswLlc2PortEntry = _DlswLlc2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1, 1)
)
dlswLlc2PortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-SNA-DLSW-MIB", "dlswBridgeIfBriGru"),
)
if mibBuilder.loadTexts:
    dlswLlc2PortEntry.setStatus("current")


class _DlswLLC2PortAckDelayTime_Type(Integer32):
    """Custom type dlswLLC2PortAckDelayTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_DlswLLC2PortAckDelayTime_Type.__name__ = "Integer32"
_DlswLLC2PortAckDelayTime_Object = MibTableColumn
dlswLLC2PortAckDelayTime = _DlswLLC2PortAckDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1, 1, 1),
    _DlswLLC2PortAckDelayTime_Type()
)
dlswLLC2PortAckDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswLLC2PortAckDelayTime.setStatus("current")


class _DlswLLC2PortAckMax_Type(Integer32):
    """Custom type dlswLLC2PortAckMax based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_DlswLLC2PortAckMax_Type.__name__ = "Integer32"
_DlswLLC2PortAckMax_Object = MibTableColumn
dlswLLC2PortAckMax = _DlswLLC2PortAckMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1, 1, 2),
    _DlswLLC2PortAckMax_Type()
)
dlswLLC2PortAckMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswLLC2PortAckMax.setStatus("current")


class _DlswLLC2PortLocalWnd_Type(Integer32):
    """Custom type dlswLLC2PortLocalWnd based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_DlswLLC2PortLocalWnd_Type.__name__ = "Integer32"
_DlswLLC2PortLocalWnd_Object = MibTableColumn
dlswLLC2PortLocalWnd = _DlswLLC2PortLocalWnd_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1, 1, 3),
    _DlswLLC2PortLocalWnd_Type()
)
dlswLLC2PortLocalWnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswLLC2PortLocalWnd.setStatus("current")


class _DlswLLC2PortModulus_Type(Integer32):
    """Custom type dlswLLC2PortModulus based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(8,
              128)
        )
    )
    namedValues = NamedValues(
        *(("m128", 128),
          ("m8", 8))
    )


_DlswLLC2PortModulus_Type.__name__ = "Integer32"
_DlswLLC2PortModulus_Object = MibTableColumn
dlswLLC2PortModulus = _DlswLLC2PortModulus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1, 1, 4),
    _DlswLLC2PortModulus_Type()
)
dlswLLC2PortModulus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswLLC2PortModulus.setStatus("current")


class _DlswLLC2PortN2_Type(Integer32):
    """Custom type dlswLLC2PortN2 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DlswLLC2PortN2_Type.__name__ = "Integer32"
_DlswLLC2PortN2_Object = MibTableColumn
dlswLLC2PortN2 = _DlswLLC2PortN2_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1, 1, 5),
    _DlswLLC2PortN2_Type()
)
dlswLLC2PortN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswLLC2PortN2.setStatus("current")


class _DlswLLC2PortT1_Type(Integer32):
    """Custom type dlswLLC2PortT1 based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_DlswLLC2PortT1_Type.__name__ = "Integer32"
_DlswLLC2PortT1_Object = MibTableColumn
dlswLLC2PortT1 = _DlswLLC2PortT1_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1, 1, 6),
    _DlswLLC2PortT1_Type()
)
dlswLLC2PortT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswLLC2PortT1.setStatus("current")


class _DlswLLC2PortTbusyTime_Type(Integer32):
    """Custom type dlswLLC2PortTbusyTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_DlswLLC2PortTbusyTime_Type.__name__ = "Integer32"
_DlswLLC2PortTbusyTime_Object = MibTableColumn
dlswLLC2PortTbusyTime = _DlswLLC2PortTbusyTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1, 1, 7),
    _DlswLLC2PortTbusyTime_Type()
)
dlswLLC2PortTbusyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswLLC2PortTbusyTime.setStatus("current")


class _DlswLLC2PortTpfTime_Type(Integer32):
    """Custom type dlswLLC2PortTpfTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_DlswLLC2PortTpfTime_Type.__name__ = "Integer32"
_DlswLLC2PortTpfTime_Object = MibTableColumn
dlswLLC2PortTpfTime = _DlswLLC2PortTpfTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1, 1, 8),
    _DlswLLC2PortTpfTime_Type()
)
dlswLLC2PortTpfTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswLLC2PortTpfTime.setStatus("current")


class _DlswLLC2PortTrejTime_Type(Integer32):
    """Custom type dlswLLC2PortTrejTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_DlswLLC2PortTrejTime_Type.__name__ = "Integer32"
_DlswLLC2PortTrejTime_Object = MibTableColumn
dlswLLC2PortTrejTime = _DlswLLC2PortTrejTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1, 1, 9),
    _DlswLLC2PortTrejTime_Type()
)
dlswLLC2PortTrejTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswLLC2PortTrejTime.setStatus("current")


class _DlswLLC2PortTxqMax_Type(Integer32):
    """Custom type dlswLLC2PortTxqMax based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_DlswLLC2PortTxqMax_Type.__name__ = "Integer32"
_DlswLLC2PortTxqMax_Object = MibTableColumn
dlswLLC2PortTxqMax = _DlswLLC2PortTxqMax_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 7, 1, 1, 10),
    _DlswLLC2PortTxqMax_Type()
)
dlswLLC2PortTxqMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dlswLLC2PortTxqMax.setStatus("current")
_DlswTraps_ObjectIdentity = ObjectIdentity
dlswTraps = _DlswTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 8)
)
_DlswTrapsV2_ObjectIdentity = ObjectIdentity
dlswTrapsV2 = _DlswTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 8, 0)
)

# Managed Objects groups


# Notification objects

dlswTrapTConnPartnerReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 8, 0, 1)
)
dlswTrapTConnPartnerReject.setObjects(
    ("A3COM-HUAWEI-SNA-DLSW-MIB", "dlswRemotePeerAddr")
)
if mibBuilder.loadTexts:
    dlswTrapTConnPartnerReject.setStatus(
        "current"
    )

dlswTrapTConnChangeState = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 8, 0, 2)
)
dlswTrapTConnChangeState.setObjects(
      *(("A3COM-HUAWEI-SNA-DLSW-MIB", "dlswRemotePeerAddr"),
        ("A3COM-HUAWEI-SNA-DLSW-MIB", "dlswRemotePeerLinkState"))
)
if mibBuilder.loadTexts:
    dlswTrapTConnChangeState.setStatus(
        "current"
    )

dlswTrapCircuitChangeState = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 34, 8, 0, 3)
)
dlswTrapCircuitChangeState.setObjects(
      *(("A3COM-HUAWEI-SNA-DLSW-MIB", "dlswCircuitS1CircuitId"),
        ("A3COM-HUAWEI-SNA-DLSW-MIB", "dlswCircuitState"),
        ("A3COM-HUAWEI-SNA-DLSW-MIB", "dlswCircuitS1Mac"),
        ("A3COM-HUAWEI-SNA-DLSW-MIB", "dlswCircuitS1Sap"),
        ("A3COM-HUAWEI-SNA-DLSW-MIB", "dlswCircuitS2Mac"),
        ("A3COM-HUAWEI-SNA-DLSW-MIB", "dlswCircuitS2Sap"))
)
if mibBuilder.loadTexts:
    dlswTrapCircuitChangeState.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-SNA-DLSW-MIB",
    **{"MacAddressNC": MacAddressNC,
       "EndStationLocation": EndStationLocation,
       "DlcType": DlcType,
       "LFSize": LFSize,
       "CreateLineFlag": CreateLineFlag,
       "EntryStatus": EntryStatus,
       "dlsw": dlsw,
       "dlswNode": dlswNode,
       "dlswNodeVersion": dlswNodeVersion,
       "dlswNodeVendorID": dlswNodeVendorID,
       "dlswNodeVersionString": dlswNodeVersionString,
       "dlswNodeStdPacingSupport": dlswNodeStdPacingSupport,
       "dlswNodeStatus": dlswNodeStatus,
       "dlswNodeUpTime": dlswNodeUpTime,
       "dlswNodeVirtualSegmentLFSize": dlswNodeVirtualSegmentLFSize,
       "dlswNodeLocalAddr": dlswNodeLocalAddr,
       "dlswNodePriority": dlswNodePriority,
       "dlswNodeInitWindow": dlswNodeInitWindow,
       "dlswNodeKeepAlive": dlswNodeKeepAlive,
       "dlswNodeMaxWindow": dlswNodeMaxWindow,
       "dlswNodePermitDynamic": dlswNodePermitDynamic,
       "dlswNodeConnTimeout": dlswNodeConnTimeout,
       "dlswNodeLocalPendTimeout": dlswNodeLocalPendTimeout,
       "dlswNodeRemotePendTimeout": dlswNodeRemotePendTimeout,
       "dlswNodeSnaCacheTimeout": dlswNodeSnaCacheTimeout,
       "dlswTrapControl": dlswTrapControl,
       "dlswTrapCntlState": dlswTrapCntlState,
       "dlswTConn": dlswTConn,
       "dlswRemotePeerTable": dlswRemotePeerTable,
       "dlswRemotePeerEntry": dlswRemotePeerEntry,
       "dlswRemotePeerAddr": dlswRemotePeerAddr,
       "dlswRemotePeerVersion": dlswRemotePeerVersion,
       "dlswRemotePeerVendorID": dlswRemotePeerVendorID,
       "dlswRemotePeerPaceWindInit": dlswRemotePeerPaceWindInit,
       "dlswRemotePeerNumOfTcpSessions": dlswRemotePeerNumOfTcpSessions,
       "dlswRemotePeerVersionString": dlswRemotePeerVersionString,
       "dlswRemotePeerIsConfig": dlswRemotePeerIsConfig,
       "dlswRemotePeerSetStateToConfig": dlswRemotePeerSetStateToConfig,
       "dlswRemotePeerCost": dlswRemotePeerCost,
       "dlswRemotePeerKeepAlive": dlswRemotePeerKeepAlive,
       "dlswRemotePeerLf": dlswRemotePeerLf,
       "dlswRemotePeerTcpQueneMax": dlswRemotePeerTcpQueneMax,
       "dlswRemotePeerHaveBackup": dlswRemotePeerHaveBackup,
       "dlswRemotePeerIsBackup": dlswRemotePeerIsBackup,
       "dlswRemotePeerBackupAddr": dlswRemotePeerBackupAddr,
       "dlswRemotePeerLinger": dlswRemotePeerLinger,
       "dlswRemotePeerLinkState": dlswRemotePeerLinkState,
       "dlswRemotePeerRecvPacks": dlswRemotePeerRecvPacks,
       "dlswRemotePeerSendPacks": dlswRemotePeerSendPacks,
       "dlswRemotePeerDrops": dlswRemotePeerDrops,
       "dlswRemotePeerUptime": dlswRemotePeerUptime,
       "dlswRemotePeerEntryStatus": dlswRemotePeerEntryStatus,
       "dlswBridgeGroup": dlswBridgeGroup,
       "dlswBridgeTable": dlswBridgeTable,
       "dlswBridgeEntry": dlswBridgeEntry,
       "dlswBridgeNum": dlswBridgeNum,
       "dlswBridgeStatus": dlswBridgeStatus,
       "dlswBridgeIfTable": dlswBridgeIfTable,
       "dlswBridgeIfEntry": dlswBridgeIfEntry,
       "dlswBridgeIfBriGru": dlswBridgeIfBriGru,
       "dlswBridgeIfName": dlswBridgeIfName,
       "dlswBridgeIfStatus": dlswBridgeIfStatus,
       "dlswLocDirectory": dlswLocDirectory,
       "dlswLocMacTable": dlswLocMacTable,
       "dlswLocMacEntry": dlswLocMacEntry,
       "dlswLocMacHashIndex": dlswLocMacHashIndex,
       "dlswLocMacHashIndexSeqNum": dlswLocMacHashIndexSeqNum,
       "dlswLocMacMac": dlswLocMacMac,
       "dlswLocMacLocalInterfaceName": dlswLocMacLocalInterfaceName,
       "dlswCircuit": dlswCircuit,
       "dlswCircuitTable": dlswCircuitTable,
       "dlswCircuitEntry": dlswCircuitEntry,
       "dlswCircuitS1CircuitId": dlswCircuitS1CircuitId,
       "dlswCircuitS1Mac": dlswCircuitS1Mac,
       "dlswCircuitS1Sap": dlswCircuitS1Sap,
       "dlswCircuitS2Mac": dlswCircuitS2Mac,
       "dlswCircuitS2Sap": dlswCircuitS2Sap,
       "dlswCircuitS1IfIndex": dlswCircuitS1IfIndex,
       "dlswCircuitS1Ifname": dlswCircuitS1Ifname,
       "dlswCircuitS1DlcType": dlswCircuitS1DlcType,
       "dlswCircuitS2Location": dlswCircuitS2Location,
       "dlswCircuitS2TAddress": dlswCircuitS2TAddress,
       "dlswCircuitS2CircuitId": dlswCircuitS2CircuitId,
       "dlswCircuitOrigin": dlswCircuitOrigin,
       "dlswCircuitEntryTime": dlswCircuitEntryTime,
       "dlswCircuitStateTime": dlswCircuitStateTime,
       "dlswCircuitState": dlswCircuitState,
       "dlswCircuitPriority": dlswCircuitPriority,
       "dlswCircuitFCSendGrantedUnits": dlswCircuitFCSendGrantedUnits,
       "dlswCircuitFCSendCurrentWndw": dlswCircuitFCSendCurrentWndw,
       "dlswCircuitFCRecvGrantedUnits": dlswCircuitFCRecvGrantedUnits,
       "dlswCircuitFCRecvCurrentWndw": dlswCircuitFCRecvCurrentWndw,
       "dlswCircuitFCLargestRecvGranted": dlswCircuitFCLargestRecvGranted,
       "dlswCircuitFCLargestSendGranted": dlswCircuitFCLargestSendGranted,
       "dlswSdlc": dlswSdlc,
       "dlswSdlcPortTable": dlswSdlcPortTable,
       "dlswSdlcPortEntry": dlswSdlcPortEntry,
       "dlswSdlcPortSerialName": dlswSdlcPortSerialName,
       "dlswSdlcPortEncap": dlswSdlcPortEncap,
       "dlswSdlcPortRole": dlswSdlcPortRole,
       "dlswSdlcPortVmac": dlswSdlcPortVmac,
       "dlswSdlcPortHoldq": dlswSdlcPortHoldq,
       "dlswSdlcPortK": dlswSdlcPortK,
       "dlswSdlcPortModule": dlswSdlcPortModule,
       "dlswSdlcPortN1": dlswSdlcPortN1,
       "dlswSdlcPortN2": dlswSdlcPortN2,
       "dlswSdlcPortPollPauseTimer": dlswSdlcPortPollPauseTimer,
       "dlswSdlcPortSimultaneousEnable": dlswSdlcPortSimultaneousEnable,
       "dlswSdlcPortT1": dlswSdlcPortT1,
       "dlswSdlcPortT2": dlswSdlcPortT2,
       "dlswSdlcPortNrziEncoding": dlswSdlcPortNrziEncoding,
       "dlswSdlcPortIdleMarkEnable": dlswSdlcPortIdleMarkEnable,
       "dlswSdlcLsTable": dlswSdlcLsTable,
       "dlswSdlcLsEntry": dlswSdlcLsEntry,
       "dlswSdlcLsAddress": dlswSdlcLsAddress,
       "dlswSdlcLsLocalId": dlswSdlcLsLocalId,
       "dlswSdlcLsRemoteMac": dlswSdlcLsRemoteMac,
       "dlswSdlcLsSsap": dlswSdlcLsSsap,
       "dlswSdlcLsDsap": dlswSdlcLsDsap,
       "dlswSdlcLsStatus": dlswSdlcLsStatus,
       "dlswLlc2": dlswLlc2,
       "dlswLlc2PortTable": dlswLlc2PortTable,
       "dlswLlc2PortEntry": dlswLlc2PortEntry,
       "dlswLLC2PortAckDelayTime": dlswLLC2PortAckDelayTime,
       "dlswLLC2PortAckMax": dlswLLC2PortAckMax,
       "dlswLLC2PortLocalWnd": dlswLLC2PortLocalWnd,
       "dlswLLC2PortModulus": dlswLLC2PortModulus,
       "dlswLLC2PortN2": dlswLLC2PortN2,
       "dlswLLC2PortT1": dlswLLC2PortT1,
       "dlswLLC2PortTbusyTime": dlswLLC2PortTbusyTime,
       "dlswLLC2PortTpfTime": dlswLLC2PortTpfTime,
       "dlswLLC2PortTrejTime": dlswLLC2PortTrejTime,
       "dlswLLC2PortTxqMax": dlswLLC2PortTxqMax,
       "dlswTraps": dlswTraps,
       "dlswTrapsV2": dlswTrapsV2,
       "dlswTrapTConnPartnerReject": dlswTrapTConnPartnerReject,
       "dlswTrapTConnChangeState": dlswTrapTConnChangeState,
       "dlswTrapCircuitChangeState": dlswTrapCircuitChangeState}
)
