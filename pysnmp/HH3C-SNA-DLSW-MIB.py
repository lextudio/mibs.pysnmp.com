# SNMP MIB module (HH3C-SNA-DLSW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-SNA-DLSW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:54 2024
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cdlsw = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37)
)


# Types definitions



class CreateLineFlag(Integer32):
    """Custom type CreateLineFlag based on Integer32"""
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





class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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



# MIB Managed Objects in the order of their OIDs

_Hh3cdlswNode_ObjectIdentity = ObjectIdentity
hh3cdlswNode = _Hh3cdlswNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1)
)


class _Hh3cdlswNodeVersion_Type(OctetString):
    """Custom type hh3cdlswNodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hh3cdlswNodeVersion_Type.__name__ = "OctetString"
_Hh3cdlswNodeVersion_Object = MibScalar
hh3cdlswNodeVersion = _Hh3cdlswNodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 1),
    _Hh3cdlswNodeVersion_Type()
)
hh3cdlswNodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswNodeVersion.setStatus("current")


class _Hh3cdlswNodeVendorID_Type(OctetString):
    """Custom type hh3cdlswNodeVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Hh3cdlswNodeVendorID_Type.__name__ = "OctetString"
_Hh3cdlswNodeVendorID_Object = MibScalar
hh3cdlswNodeVendorID = _Hh3cdlswNodeVendorID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 2),
    _Hh3cdlswNodeVendorID_Type()
)
hh3cdlswNodeVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswNodeVendorID.setStatus("current")
_Hh3cdlswNodeVersionString_Type = DisplayString
_Hh3cdlswNodeVersionString_Object = MibScalar
hh3cdlswNodeVersionString = _Hh3cdlswNodeVersionString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 3),
    _Hh3cdlswNodeVersionString_Type()
)
hh3cdlswNodeVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswNodeVersionString.setStatus("current")


class _Hh3cdlswNodeStdPacingSupport_Type(Integer32):
    """Custom type hh3cdlswNodeStdPacingSupport based on Integer32"""
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


_Hh3cdlswNodeStdPacingSupport_Type.__name__ = "Integer32"
_Hh3cdlswNodeStdPacingSupport_Object = MibScalar
hh3cdlswNodeStdPacingSupport = _Hh3cdlswNodeStdPacingSupport_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 4),
    _Hh3cdlswNodeStdPacingSupport_Type()
)
hh3cdlswNodeStdPacingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswNodeStdPacingSupport.setStatus("current")


class _Hh3cdlswNodeStatus_Type(Integer32):
    """Custom type hh3cdlswNodeStatus based on Integer32"""
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


_Hh3cdlswNodeStatus_Type.__name__ = "Integer32"
_Hh3cdlswNodeStatus_Object = MibScalar
hh3cdlswNodeStatus = _Hh3cdlswNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 5),
    _Hh3cdlswNodeStatus_Type()
)
hh3cdlswNodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodeStatus.setStatus("current")


class _Hh3cdlswNodeVirtualSegmentLFSize_Type(LFSize):
    """Custom type hh3cdlswNodeVirtualSegmentLFSize based on LFSize"""


_Hh3cdlswNodeVirtualSegmentLFSize_Object = MibScalar
hh3cdlswNodeVirtualSegmentLFSize = _Hh3cdlswNodeVirtualSegmentLFSize_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 6),
    _Hh3cdlswNodeVirtualSegmentLFSize_Type()
)
hh3cdlswNodeVirtualSegmentLFSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodeVirtualSegmentLFSize.setStatus("current")
_Hh3cdlswNodeLocalAddr_Type = IpAddress
_Hh3cdlswNodeLocalAddr_Object = MibScalar
hh3cdlswNodeLocalAddr = _Hh3cdlswNodeLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 7),
    _Hh3cdlswNodeLocalAddr_Type()
)
hh3cdlswNodeLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodeLocalAddr.setStatus("current")


class _Hh3cdlswNodePriority_Type(Integer32):
    """Custom type hh3cdlswNodePriority based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cdlswNodePriority_Type.__name__ = "Integer32"
_Hh3cdlswNodePriority_Object = MibScalar
hh3cdlswNodePriority = _Hh3cdlswNodePriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 8),
    _Hh3cdlswNodePriority_Type()
)
hh3cdlswNodePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodePriority.setStatus("current")


class _Hh3cdlswNodeInitWindow_Type(Integer32):
    """Custom type hh3cdlswNodeInitWindow based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cdlswNodeInitWindow_Type.__name__ = "Integer32"
_Hh3cdlswNodeInitWindow_Object = MibScalar
hh3cdlswNodeInitWindow = _Hh3cdlswNodeInitWindow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 9),
    _Hh3cdlswNodeInitWindow_Type()
)
hh3cdlswNodeInitWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodeInitWindow.setStatus("current")


class _Hh3cdlswNodeKeepAlive_Type(Integer32):
    """Custom type hh3cdlswNodeKeepAlive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cdlswNodeKeepAlive_Type.__name__ = "Integer32"
_Hh3cdlswNodeKeepAlive_Object = MibScalar
hh3cdlswNodeKeepAlive = _Hh3cdlswNodeKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 10),
    _Hh3cdlswNodeKeepAlive_Type()
)
hh3cdlswNodeKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodeKeepAlive.setStatus("current")


class _Hh3cdlswNodeMaxWindow_Type(Integer32):
    """Custom type hh3cdlswNodeMaxWindow based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
        ValueRangeConstraint(65535, 65535),
    )


_Hh3cdlswNodeMaxWindow_Type.__name__ = "Integer32"
_Hh3cdlswNodeMaxWindow_Object = MibScalar
hh3cdlswNodeMaxWindow = _Hh3cdlswNodeMaxWindow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 11),
    _Hh3cdlswNodeMaxWindow_Type()
)
hh3cdlswNodeMaxWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodeMaxWindow.setStatus("current")


class _Hh3cdlswNodePermitDynamic_Type(Integer32):
    """Custom type hh3cdlswNodePermitDynamic based on Integer32"""
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
        *(("forbid-dynamic", 2),
          ("permit-dynamic", 1),
          ("unknown", 65535))
    )


_Hh3cdlswNodePermitDynamic_Type.__name__ = "Integer32"
_Hh3cdlswNodePermitDynamic_Object = MibScalar
hh3cdlswNodePermitDynamic = _Hh3cdlswNodePermitDynamic_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 12),
    _Hh3cdlswNodePermitDynamic_Type()
)
hh3cdlswNodePermitDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodePermitDynamic.setStatus("current")


class _Hh3cdlswNodeConnTimeout_Type(Integer32):
    """Custom type hh3cdlswNodeConnTimeout based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cdlswNodeConnTimeout_Type.__name__ = "Integer32"
_Hh3cdlswNodeConnTimeout_Object = MibScalar
hh3cdlswNodeConnTimeout = _Hh3cdlswNodeConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 13),
    _Hh3cdlswNodeConnTimeout_Type()
)
hh3cdlswNodeConnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodeConnTimeout.setStatus("current")


class _Hh3cdlswNodeLocalPendTimeout_Type(Integer32):
    """Custom type hh3cdlswNodeLocalPendTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cdlswNodeLocalPendTimeout_Type.__name__ = "Integer32"
_Hh3cdlswNodeLocalPendTimeout_Object = MibScalar
hh3cdlswNodeLocalPendTimeout = _Hh3cdlswNodeLocalPendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 14),
    _Hh3cdlswNodeLocalPendTimeout_Type()
)
hh3cdlswNodeLocalPendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodeLocalPendTimeout.setStatus("current")


class _Hh3cdlswNodeRemotePendTimeout_Type(Integer32):
    """Custom type hh3cdlswNodeRemotePendTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cdlswNodeRemotePendTimeout_Type.__name__ = "Integer32"
_Hh3cdlswNodeRemotePendTimeout_Object = MibScalar
hh3cdlswNodeRemotePendTimeout = _Hh3cdlswNodeRemotePendTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 15),
    _Hh3cdlswNodeRemotePendTimeout_Type()
)
hh3cdlswNodeRemotePendTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodeRemotePendTimeout.setStatus("current")


class _Hh3cdlswNodeSnaCacheTimeout_Type(Integer32):
    """Custom type hh3cdlswNodeSnaCacheTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cdlswNodeSnaCacheTimeout_Type.__name__ = "Integer32"
_Hh3cdlswNodeSnaCacheTimeout_Object = MibScalar
hh3cdlswNodeSnaCacheTimeout = _Hh3cdlswNodeSnaCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 16),
    _Hh3cdlswNodeSnaCacheTimeout_Type()
)
hh3cdlswNodeSnaCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswNodeSnaCacheTimeout.setStatus("current")
_Hh3cdlswTrapControl_ObjectIdentity = ObjectIdentity
hh3cdlswTrapControl = _Hh3cdlswTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 20)
)


class _Hh3cdlswTrapCntlState_Type(Integer32):
    """Custom type hh3cdlswTrapCntlState based on Integer32"""
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


_Hh3cdlswTrapCntlState_Type.__name__ = "Integer32"
_Hh3cdlswTrapCntlState_Object = MibScalar
hh3cdlswTrapCntlState = _Hh3cdlswTrapCntlState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 1, 20, 1),
    _Hh3cdlswTrapCntlState_Type()
)
hh3cdlswTrapCntlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswTrapCntlState.setStatus("current")
_Hh3cdlswTConn_ObjectIdentity = ObjectIdentity
hh3cdlswTConn = _Hh3cdlswTConn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2)
)
_Hh3cdlswRemotePeerTable_Object = MibTable
hh3cdlswRemotePeerTable = _Hh3cdlswRemotePeerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerTable.setStatus("current")
_Hh3cdlswRemotePeerEntry_Object = MibTableRow
hh3cdlswRemotePeerEntry = _Hh3cdlswRemotePeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1)
)
hh3cdlswRemotePeerEntry.setIndexNames(
    (0, "HH3C-SNA-DLSW-MIB", "hh3cdlswRemotePeerAddr"),
)
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerEntry.setStatus("current")
_Hh3cdlswRemotePeerAddr_Type = IpAddress
_Hh3cdlswRemotePeerAddr_Object = MibTableColumn
hh3cdlswRemotePeerAddr = _Hh3cdlswRemotePeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 1),
    _Hh3cdlswRemotePeerAddr_Type()
)
hh3cdlswRemotePeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerAddr.setStatus("current")


class _Hh3cdlswRemotePeerVersion_Type(OctetString):
    """Custom type hh3cdlswRemotePeerVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hh3cdlswRemotePeerVersion_Type.__name__ = "OctetString"
_Hh3cdlswRemotePeerVersion_Object = MibTableColumn
hh3cdlswRemotePeerVersion = _Hh3cdlswRemotePeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 2),
    _Hh3cdlswRemotePeerVersion_Type()
)
hh3cdlswRemotePeerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerVersion.setStatus("current")


class _Hh3cdlswRemotePeerVendorID_Type(OctetString):
    """Custom type hh3cdlswRemotePeerVendorID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Hh3cdlswRemotePeerVendorID_Type.__name__ = "OctetString"
_Hh3cdlswRemotePeerVendorID_Object = MibTableColumn
hh3cdlswRemotePeerVendorID = _Hh3cdlswRemotePeerVendorID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 3),
    _Hh3cdlswRemotePeerVendorID_Type()
)
hh3cdlswRemotePeerVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerVendorID.setStatus("current")
_Hh3cdlswRemotePeerPaceWindInit_Type = Integer32
_Hh3cdlswRemotePeerPaceWindInit_Object = MibTableColumn
hh3cdlswRemotePeerPaceWindInit = _Hh3cdlswRemotePeerPaceWindInit_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 4),
    _Hh3cdlswRemotePeerPaceWindInit_Type()
)
hh3cdlswRemotePeerPaceWindInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerPaceWindInit.setStatus("current")
_Hh3cdlswRemotePeerVersionString_Type = DisplayString
_Hh3cdlswRemotePeerVersionString_Object = MibTableColumn
hh3cdlswRemotePeerVersionString = _Hh3cdlswRemotePeerVersionString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 5),
    _Hh3cdlswRemotePeerVersionString_Type()
)
hh3cdlswRemotePeerVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerVersionString.setStatus("current")


class _Hh3cdlswRemotePeerIsConfig_Type(Integer32):
    """Custom type hh3cdlswRemotePeerIsConfig based on Integer32"""
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


_Hh3cdlswRemotePeerIsConfig_Type.__name__ = "Integer32"
_Hh3cdlswRemotePeerIsConfig_Object = MibTableColumn
hh3cdlswRemotePeerIsConfig = _Hh3cdlswRemotePeerIsConfig_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 6),
    _Hh3cdlswRemotePeerIsConfig_Type()
)
hh3cdlswRemotePeerIsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerIsConfig.setStatus("current")


class _Hh3cdlswRemotePeerCost_Type(Integer32):
    """Custom type hh3cdlswRemotePeerCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Hh3cdlswRemotePeerCost_Type.__name__ = "Integer32"
_Hh3cdlswRemotePeerCost_Object = MibTableColumn
hh3cdlswRemotePeerCost = _Hh3cdlswRemotePeerCost_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 7),
    _Hh3cdlswRemotePeerCost_Type()
)
hh3cdlswRemotePeerCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerCost.setStatus("current")


class _Hh3cdlswRemotePeerKeepAlive_Type(Integer32):
    """Custom type hh3cdlswRemotePeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdlswRemotePeerKeepAlive_Type.__name__ = "Integer32"
_Hh3cdlswRemotePeerKeepAlive_Object = MibTableColumn
hh3cdlswRemotePeerKeepAlive = _Hh3cdlswRemotePeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 8),
    _Hh3cdlswRemotePeerKeepAlive_Type()
)
hh3cdlswRemotePeerKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerKeepAlive.setStatus("current")
_Hh3cdlswRemotePeerLf_Type = LFSize
_Hh3cdlswRemotePeerLf_Object = MibTableColumn
hh3cdlswRemotePeerLf = _Hh3cdlswRemotePeerLf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 9),
    _Hh3cdlswRemotePeerLf_Type()
)
hh3cdlswRemotePeerLf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerLf.setStatus("current")


class _Hh3cdlswRemotePeerTcpQueneMax_Type(Integer32):
    """Custom type hh3cdlswRemotePeerTcpQueneMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 2000),
    )


_Hh3cdlswRemotePeerTcpQueneMax_Type.__name__ = "Integer32"
_Hh3cdlswRemotePeerTcpQueneMax_Object = MibTableColumn
hh3cdlswRemotePeerTcpQueneMax = _Hh3cdlswRemotePeerTcpQueneMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 10),
    _Hh3cdlswRemotePeerTcpQueneMax_Type()
)
hh3cdlswRemotePeerTcpQueneMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerTcpQueneMax.setStatus("current")


class _Hh3cdlswRemotePeerHaveBackup_Type(Integer32):
    """Custom type hh3cdlswRemotePeerHaveBackup based on Integer32"""
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


_Hh3cdlswRemotePeerHaveBackup_Type.__name__ = "Integer32"
_Hh3cdlswRemotePeerHaveBackup_Object = MibTableColumn
hh3cdlswRemotePeerHaveBackup = _Hh3cdlswRemotePeerHaveBackup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 11),
    _Hh3cdlswRemotePeerHaveBackup_Type()
)
hh3cdlswRemotePeerHaveBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerHaveBackup.setStatus("current")


class _Hh3cdlswRemotePeerIsBackup_Type(Integer32):
    """Custom type hh3cdlswRemotePeerIsBackup based on Integer32"""
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


_Hh3cdlswRemotePeerIsBackup_Type.__name__ = "Integer32"
_Hh3cdlswRemotePeerIsBackup_Object = MibTableColumn
hh3cdlswRemotePeerIsBackup = _Hh3cdlswRemotePeerIsBackup_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 12),
    _Hh3cdlswRemotePeerIsBackup_Type()
)
hh3cdlswRemotePeerIsBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerIsBackup.setStatus("current")
_Hh3cdlswRemotePeerBackupAddr_Type = IpAddress
_Hh3cdlswRemotePeerBackupAddr_Object = MibTableColumn
hh3cdlswRemotePeerBackupAddr = _Hh3cdlswRemotePeerBackupAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 13),
    _Hh3cdlswRemotePeerBackupAddr_Type()
)
hh3cdlswRemotePeerBackupAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerBackupAddr.setStatus("current")


class _Hh3cdlswRemotePeerLinger_Type(Integer32):
    """Custom type hh3cdlswRemotePeerLinger based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_Hh3cdlswRemotePeerLinger_Type.__name__ = "Integer32"
_Hh3cdlswRemotePeerLinger_Object = MibTableColumn
hh3cdlswRemotePeerLinger = _Hh3cdlswRemotePeerLinger_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 14),
    _Hh3cdlswRemotePeerLinger_Type()
)
hh3cdlswRemotePeerLinger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerLinger.setStatus("current")


class _Hh3cdlswRemotePeerLinkState_Type(Integer32):
    """Custom type hh3cdlswRemotePeerLinkState based on Integer32"""
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


_Hh3cdlswRemotePeerLinkState_Type.__name__ = "Integer32"
_Hh3cdlswRemotePeerLinkState_Object = MibTableColumn
hh3cdlswRemotePeerLinkState = _Hh3cdlswRemotePeerLinkState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 15),
    _Hh3cdlswRemotePeerLinkState_Type()
)
hh3cdlswRemotePeerLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerLinkState.setStatus("current")
_Hh3cdlswRemotePeerRecvPacks_Type = Counter32
_Hh3cdlswRemotePeerRecvPacks_Object = MibTableColumn
hh3cdlswRemotePeerRecvPacks = _Hh3cdlswRemotePeerRecvPacks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 16),
    _Hh3cdlswRemotePeerRecvPacks_Type()
)
hh3cdlswRemotePeerRecvPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerRecvPacks.setStatus("current")
_Hh3cdlswRemotePeerSendPacks_Type = Counter32
_Hh3cdlswRemotePeerSendPacks_Object = MibTableColumn
hh3cdlswRemotePeerSendPacks = _Hh3cdlswRemotePeerSendPacks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 17),
    _Hh3cdlswRemotePeerSendPacks_Type()
)
hh3cdlswRemotePeerSendPacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerSendPacks.setStatus("current")
_Hh3cdlswRemotePeerDrops_Type = Counter32
_Hh3cdlswRemotePeerDrops_Object = MibTableColumn
hh3cdlswRemotePeerDrops = _Hh3cdlswRemotePeerDrops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 18),
    _Hh3cdlswRemotePeerDrops_Type()
)
hh3cdlswRemotePeerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerDrops.setStatus("current")
_Hh3cdlswRemotePeerUptime_Type = Counter32
_Hh3cdlswRemotePeerUptime_Object = MibTableColumn
hh3cdlswRemotePeerUptime = _Hh3cdlswRemotePeerUptime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 19),
    _Hh3cdlswRemotePeerUptime_Type()
)
hh3cdlswRemotePeerUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerUptime.setStatus("current")
_Hh3cdlswRemotePeerEntryStatus_Type = EntryStatus
_Hh3cdlswRemotePeerEntryStatus_Object = MibTableColumn
hh3cdlswRemotePeerEntryStatus = _Hh3cdlswRemotePeerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 2, 1, 1, 20),
    _Hh3cdlswRemotePeerEntryStatus_Type()
)
hh3cdlswRemotePeerEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswRemotePeerEntryStatus.setStatus("current")
_Hh3cdlswBridgeGroup_ObjectIdentity = ObjectIdentity
hh3cdlswBridgeGroup = _Hh3cdlswBridgeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 3)
)
_Hh3cdlswBridgeTable_Object = MibTable
hh3cdlswBridgeTable = _Hh3cdlswBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cdlswBridgeTable.setStatus("current")
_Hh3cdlswBridgeEntry_Object = MibTableRow
hh3cdlswBridgeEntry = _Hh3cdlswBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 1, 1)
)
hh3cdlswBridgeEntry.setIndexNames(
    (0, "HH3C-SNA-DLSW-MIB", "hh3cdlswBridgeNum"),
)
if mibBuilder.loadTexts:
    hh3cdlswBridgeEntry.setStatus("current")


class _Hh3cdlswBridgeNum_Type(Integer32):
    """Custom type hh3cdlswBridgeNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Hh3cdlswBridgeNum_Type.__name__ = "Integer32"
_Hh3cdlswBridgeNum_Object = MibTableColumn
hh3cdlswBridgeNum = _Hh3cdlswBridgeNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 1, 1, 1),
    _Hh3cdlswBridgeNum_Type()
)
hh3cdlswBridgeNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswBridgeNum.setStatus("current")
_Hh3cdlswBridgeStatus_Type = CreateLineFlag
_Hh3cdlswBridgeStatus_Object = MibTableColumn
hh3cdlswBridgeStatus = _Hh3cdlswBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 1, 1, 2),
    _Hh3cdlswBridgeStatus_Type()
)
hh3cdlswBridgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswBridgeStatus.setStatus("current")
_Hh3cdlswBridgeIfTable_Object = MibTable
hh3cdlswBridgeIfTable = _Hh3cdlswBridgeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cdlswBridgeIfTable.setStatus("current")
_Hh3cdlswBridgeIfEntry_Object = MibTableRow
hh3cdlswBridgeIfEntry = _Hh3cdlswBridgeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 2, 1)
)
hh3cdlswBridgeIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cdlswBridgeIfEntry.setStatus("current")


class _Hh3cdlswBridgeIfBriGru_Type(Integer32):
    """Custom type hh3cdlswBridgeIfBriGru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_Hh3cdlswBridgeIfBriGru_Type.__name__ = "Integer32"
_Hh3cdlswBridgeIfBriGru_Object = MibTableColumn
hh3cdlswBridgeIfBriGru = _Hh3cdlswBridgeIfBriGru_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 2, 1, 1),
    _Hh3cdlswBridgeIfBriGru_Type()
)
hh3cdlswBridgeIfBriGru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswBridgeIfBriGru.setStatus("current")
_Hh3cdlswBridgeIfName_Type = DisplayString
_Hh3cdlswBridgeIfName_Object = MibTableColumn
hh3cdlswBridgeIfName = _Hh3cdlswBridgeIfName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 2, 1, 2),
    _Hh3cdlswBridgeIfName_Type()
)
hh3cdlswBridgeIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswBridgeIfName.setStatus("current")
_Hh3cdlswBridgeIfStatus_Type = EntryStatus
_Hh3cdlswBridgeIfStatus_Object = MibTableColumn
hh3cdlswBridgeIfStatus = _Hh3cdlswBridgeIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 3, 2, 1, 3),
    _Hh3cdlswBridgeIfStatus_Type()
)
hh3cdlswBridgeIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswBridgeIfStatus.setStatus("current")
_Hh3cdlswLocDirectory_ObjectIdentity = ObjectIdentity
hh3cdlswLocDirectory = _Hh3cdlswLocDirectory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 4)
)
_Hh3cdlswLocMacTable_Object = MibTable
hh3cdlswLocMacTable = _Hh3cdlswLocMacTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cdlswLocMacTable.setStatus("current")
_Hh3cdlswLocMacEntry_Object = MibTableRow
hh3cdlswLocMacEntry = _Hh3cdlswLocMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1, 1)
)
hh3cdlswLocMacEntry.setIndexNames(
    (0, "HH3C-SNA-DLSW-MIB", "hh3cdlswLocMacHashIndex"),
    (0, "HH3C-SNA-DLSW-MIB", "hh3cdlswLocMacHashIndexSeqNum"),
)
if mibBuilder.loadTexts:
    hh3cdlswLocMacEntry.setStatus("current")
_Hh3cdlswLocMacHashIndex_Type = Integer32
_Hh3cdlswLocMacHashIndex_Object = MibTableColumn
hh3cdlswLocMacHashIndex = _Hh3cdlswLocMacHashIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1, 1, 1),
    _Hh3cdlswLocMacHashIndex_Type()
)
hh3cdlswLocMacHashIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswLocMacHashIndex.setStatus("current")
_Hh3cdlswLocMacHashIndexSeqNum_Type = Integer32
_Hh3cdlswLocMacHashIndexSeqNum_Object = MibTableColumn
hh3cdlswLocMacHashIndexSeqNum = _Hh3cdlswLocMacHashIndexSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1, 1, 2),
    _Hh3cdlswLocMacHashIndexSeqNum_Type()
)
hh3cdlswLocMacHashIndexSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswLocMacHashIndexSeqNum.setStatus("current")
_Hh3cdlswLocMacMac_Type = MacAddressNC
_Hh3cdlswLocMacMac_Object = MibTableColumn
hh3cdlswLocMacMac = _Hh3cdlswLocMacMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1, 1, 3),
    _Hh3cdlswLocMacMac_Type()
)
hh3cdlswLocMacMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswLocMacMac.setStatus("current")
_Hh3cdlswLocMacLocalInterfaceName_Type = DisplayString
_Hh3cdlswLocMacLocalInterfaceName_Object = MibTableColumn
hh3cdlswLocMacLocalInterfaceName = _Hh3cdlswLocMacLocalInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 4, 1, 1, 4),
    _Hh3cdlswLocMacLocalInterfaceName_Type()
)
hh3cdlswLocMacLocalInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswLocMacLocalInterfaceName.setStatus("current")
_Hh3cdlswCircuit_ObjectIdentity = ObjectIdentity
hh3cdlswCircuit = _Hh3cdlswCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5)
)
_Hh3cdlswCircuitTable_Object = MibTable
hh3cdlswCircuitTable = _Hh3cdlswCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1)
)
if mibBuilder.loadTexts:
    hh3cdlswCircuitTable.setStatus("current")
_Hh3cdlswCircuitEntry_Object = MibTableRow
hh3cdlswCircuitEntry = _Hh3cdlswCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1)
)
hh3cdlswCircuitEntry.setIndexNames(
    (0, "HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS1CircuitId"),
)
if mibBuilder.loadTexts:
    hh3cdlswCircuitEntry.setStatus("current")
_Hh3cdlswCircuitS1CircuitId_Type = Integer32
_Hh3cdlswCircuitS1CircuitId_Object = MibTableColumn
hh3cdlswCircuitS1CircuitId = _Hh3cdlswCircuitS1CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 1),
    _Hh3cdlswCircuitS1CircuitId_Type()
)
hh3cdlswCircuitS1CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitS1CircuitId.setStatus("current")
_Hh3cdlswCircuitS1Mac_Type = MacAddressNC
_Hh3cdlswCircuitS1Mac_Object = MibTableColumn
hh3cdlswCircuitS1Mac = _Hh3cdlswCircuitS1Mac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 2),
    _Hh3cdlswCircuitS1Mac_Type()
)
hh3cdlswCircuitS1Mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitS1Mac.setStatus("current")


class _Hh3cdlswCircuitS1Sap_Type(OctetString):
    """Custom type hh3cdlswCircuitS1Sap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Hh3cdlswCircuitS1Sap_Type.__name__ = "OctetString"
_Hh3cdlswCircuitS1Sap_Object = MibTableColumn
hh3cdlswCircuitS1Sap = _Hh3cdlswCircuitS1Sap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 3),
    _Hh3cdlswCircuitS1Sap_Type()
)
hh3cdlswCircuitS1Sap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitS1Sap.setStatus("current")
_Hh3cdlswCircuitS2Mac_Type = MacAddressNC
_Hh3cdlswCircuitS2Mac_Object = MibTableColumn
hh3cdlswCircuitS2Mac = _Hh3cdlswCircuitS2Mac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 4),
    _Hh3cdlswCircuitS2Mac_Type()
)
hh3cdlswCircuitS2Mac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitS2Mac.setStatus("current")


class _Hh3cdlswCircuitS2Sap_Type(OctetString):
    """Custom type hh3cdlswCircuitS2Sap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Hh3cdlswCircuitS2Sap_Type.__name__ = "OctetString"
_Hh3cdlswCircuitS2Sap_Object = MibTableColumn
hh3cdlswCircuitS2Sap = _Hh3cdlswCircuitS2Sap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 5),
    _Hh3cdlswCircuitS2Sap_Type()
)
hh3cdlswCircuitS2Sap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitS2Sap.setStatus("current")


class _Hh3cdlswCircuitS1IfIndex_Type(Integer32):
    """Custom type hh3cdlswCircuitS1IfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cdlswCircuitS1IfIndex_Type.__name__ = "Integer32"
_Hh3cdlswCircuitS1IfIndex_Object = MibTableColumn
hh3cdlswCircuitS1IfIndex = _Hh3cdlswCircuitS1IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 6),
    _Hh3cdlswCircuitS1IfIndex_Type()
)
hh3cdlswCircuitS1IfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitS1IfIndex.setStatus("current")
_Hh3cdlswCircuitS1Ifname_Type = DisplayString
_Hh3cdlswCircuitS1Ifname_Object = MibTableColumn
hh3cdlswCircuitS1Ifname = _Hh3cdlswCircuitS1Ifname_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 7),
    _Hh3cdlswCircuitS1Ifname_Type()
)
hh3cdlswCircuitS1Ifname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitS1Ifname.setStatus("current")
_Hh3cdlswCircuitS1DlcType_Type = DlcType
_Hh3cdlswCircuitS1DlcType_Object = MibTableColumn
hh3cdlswCircuitS1DlcType = _Hh3cdlswCircuitS1DlcType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 8),
    _Hh3cdlswCircuitS1DlcType_Type()
)
hh3cdlswCircuitS1DlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitS1DlcType.setStatus("current")
_Hh3cdlswCircuitS2TAddress_Type = IpAddress
_Hh3cdlswCircuitS2TAddress_Object = MibTableColumn
hh3cdlswCircuitS2TAddress = _Hh3cdlswCircuitS2TAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 9),
    _Hh3cdlswCircuitS2TAddress_Type()
)
hh3cdlswCircuitS2TAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitS2TAddress.setStatus("current")
_Hh3cdlswCircuitS2CircuitId_Type = Integer32
_Hh3cdlswCircuitS2CircuitId_Object = MibTableColumn
hh3cdlswCircuitS2CircuitId = _Hh3cdlswCircuitS2CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 10),
    _Hh3cdlswCircuitS2CircuitId_Type()
)
hh3cdlswCircuitS2CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitS2CircuitId.setStatus("current")


class _Hh3cdlswCircuitOrigin_Type(Integer32):
    """Custom type hh3cdlswCircuitOrigin based on Integer32"""
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


_Hh3cdlswCircuitOrigin_Type.__name__ = "Integer32"
_Hh3cdlswCircuitOrigin_Object = MibTableColumn
hh3cdlswCircuitOrigin = _Hh3cdlswCircuitOrigin_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 11),
    _Hh3cdlswCircuitOrigin_Type()
)
hh3cdlswCircuitOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitOrigin.setStatus("current")
_Hh3cdlswCircuitEntryTime_Type = TimeTicks
_Hh3cdlswCircuitEntryTime_Object = MibTableColumn
hh3cdlswCircuitEntryTime = _Hh3cdlswCircuitEntryTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 12),
    _Hh3cdlswCircuitEntryTime_Type()
)
hh3cdlswCircuitEntryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitEntryTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdlswCircuitEntryTime.setUnits("hundredths of a second")
_Hh3cdlswCircuitStateTime_Type = TimeTicks
_Hh3cdlswCircuitStateTime_Object = MibTableColumn
hh3cdlswCircuitStateTime = _Hh3cdlswCircuitStateTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 13),
    _Hh3cdlswCircuitStateTime_Type()
)
hh3cdlswCircuitStateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitStateTime.setStatus("current")
if mibBuilder.loadTexts:
    hh3cdlswCircuitStateTime.setUnits("hundredths of a second")


class _Hh3cdlswCircuitState_Type(Integer32):
    """Custom type hh3cdlswCircuitState based on Integer32"""
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


_Hh3cdlswCircuitState_Type.__name__ = "Integer32"
_Hh3cdlswCircuitState_Object = MibTableColumn
hh3cdlswCircuitState = _Hh3cdlswCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 14),
    _Hh3cdlswCircuitState_Type()
)
hh3cdlswCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitState.setStatus("current")


class _Hh3cdlswCircuitFCSendGrantedUnits_Type(Integer32):
    """Custom type hh3cdlswCircuitFCSendGrantedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cdlswCircuitFCSendGrantedUnits_Type.__name__ = "Integer32"
_Hh3cdlswCircuitFCSendGrantedUnits_Object = MibTableColumn
hh3cdlswCircuitFCSendGrantedUnits = _Hh3cdlswCircuitFCSendGrantedUnits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 15),
    _Hh3cdlswCircuitFCSendGrantedUnits_Type()
)
hh3cdlswCircuitFCSendGrantedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitFCSendGrantedUnits.setStatus("current")


class _Hh3cdlswCircuitFCSendCurrentWndw_Type(Integer32):
    """Custom type hh3cdlswCircuitFCSendCurrentWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cdlswCircuitFCSendCurrentWndw_Type.__name__ = "Integer32"
_Hh3cdlswCircuitFCSendCurrentWndw_Object = MibTableColumn
hh3cdlswCircuitFCSendCurrentWndw = _Hh3cdlswCircuitFCSendCurrentWndw_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 16),
    _Hh3cdlswCircuitFCSendCurrentWndw_Type()
)
hh3cdlswCircuitFCSendCurrentWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitFCSendCurrentWndw.setStatus("current")


class _Hh3cdlswCircuitFCRecvGrantedUnits_Type(Integer32):
    """Custom type hh3cdlswCircuitFCRecvGrantedUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cdlswCircuitFCRecvGrantedUnits_Type.__name__ = "Integer32"
_Hh3cdlswCircuitFCRecvGrantedUnits_Object = MibTableColumn
hh3cdlswCircuitFCRecvGrantedUnits = _Hh3cdlswCircuitFCRecvGrantedUnits_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 17),
    _Hh3cdlswCircuitFCRecvGrantedUnits_Type()
)
hh3cdlswCircuitFCRecvGrantedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitFCRecvGrantedUnits.setStatus("current")


class _Hh3cdlswCircuitFCRecvCurrentWndw_Type(Integer32):
    """Custom type hh3cdlswCircuitFCRecvCurrentWndw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cdlswCircuitFCRecvCurrentWndw_Type.__name__ = "Integer32"
_Hh3cdlswCircuitFCRecvCurrentWndw_Object = MibTableColumn
hh3cdlswCircuitFCRecvCurrentWndw = _Hh3cdlswCircuitFCRecvCurrentWndw_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 5, 1, 1, 18),
    _Hh3cdlswCircuitFCRecvCurrentWndw_Type()
)
hh3cdlswCircuitFCRecvCurrentWndw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswCircuitFCRecvCurrentWndw.setStatus("current")
_Hh3cdlswSdlc_ObjectIdentity = ObjectIdentity
hh3cdlswSdlc = _Hh3cdlswSdlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6)
)
_Hh3cdlswSdlcPortTable_Object = MibTable
hh3cdlswSdlcPortTable = _Hh3cdlswSdlcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortTable.setStatus("current")
_Hh3cdlswSdlcPortEntry_Object = MibTableRow
hh3cdlswSdlcPortEntry = _Hh3cdlswSdlcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1)
)
hh3cdlswSdlcPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortEntry.setStatus("current")
_Hh3cdlswSdlcPortSerialName_Type = DisplayString
_Hh3cdlswSdlcPortSerialName_Object = MibTableColumn
hh3cdlswSdlcPortSerialName = _Hh3cdlswSdlcPortSerialName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 1),
    _Hh3cdlswSdlcPortSerialName_Type()
)
hh3cdlswSdlcPortSerialName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortSerialName.setStatus("current")


class _Hh3cdlswSdlcPortEncap_Type(Integer32):
    """Custom type hh3cdlswSdlcPortEncap based on Integer32"""
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


_Hh3cdlswSdlcPortEncap_Type.__name__ = "Integer32"
_Hh3cdlswSdlcPortEncap_Object = MibTableColumn
hh3cdlswSdlcPortEncap = _Hh3cdlswSdlcPortEncap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 2),
    _Hh3cdlswSdlcPortEncap_Type()
)
hh3cdlswSdlcPortEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortEncap.setStatus("current")


class _Hh3cdlswSdlcPortRole_Type(Integer32):
    """Custom type hh3cdlswSdlcPortRole based on Integer32"""
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


_Hh3cdlswSdlcPortRole_Type.__name__ = "Integer32"
_Hh3cdlswSdlcPortRole_Object = MibTableColumn
hh3cdlswSdlcPortRole = _Hh3cdlswSdlcPortRole_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 3),
    _Hh3cdlswSdlcPortRole_Type()
)
hh3cdlswSdlcPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortRole.setStatus("current")
_Hh3cdlswSdlcPortVmac_Type = MacAddressNC
_Hh3cdlswSdlcPortVmac_Object = MibTableColumn
hh3cdlswSdlcPortVmac = _Hh3cdlswSdlcPortVmac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 4),
    _Hh3cdlswSdlcPortVmac_Type()
)
hh3cdlswSdlcPortVmac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortVmac.setStatus("current")


class _Hh3cdlswSdlcPortHoldq_Type(Integer32):
    """Custom type hh3cdlswSdlcPortHoldq based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 255),
    )


_Hh3cdlswSdlcPortHoldq_Type.__name__ = "Integer32"
_Hh3cdlswSdlcPortHoldq_Object = MibTableColumn
hh3cdlswSdlcPortHoldq = _Hh3cdlswSdlcPortHoldq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 5),
    _Hh3cdlswSdlcPortHoldq_Type()
)
hh3cdlswSdlcPortHoldq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortHoldq.setStatus("current")


class _Hh3cdlswSdlcPortK_Type(Integer32):
    """Custom type hh3cdlswSdlcPortK based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_Hh3cdlswSdlcPortK_Type.__name__ = "Integer32"
_Hh3cdlswSdlcPortK_Object = MibTableColumn
hh3cdlswSdlcPortK = _Hh3cdlswSdlcPortK_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 6),
    _Hh3cdlswSdlcPortK_Type()
)
hh3cdlswSdlcPortK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortK.setStatus("current")


class _Hh3cdlswSdlcPortModule_Type(Integer32):
    """Custom type hh3cdlswSdlcPortModule based on Integer32"""
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


_Hh3cdlswSdlcPortModule_Type.__name__ = "Integer32"
_Hh3cdlswSdlcPortModule_Object = MibTableColumn
hh3cdlswSdlcPortModule = _Hh3cdlswSdlcPortModule_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 7),
    _Hh3cdlswSdlcPortModule_Type()
)
hh3cdlswSdlcPortModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortModule.setStatus("current")


class _Hh3cdlswSdlcPortN1_Type(Integer32):
    """Custom type hh3cdlswSdlcPortN1 based on Integer32"""
    defaultValue = 265

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 17680),
    )


_Hh3cdlswSdlcPortN1_Type.__name__ = "Integer32"
_Hh3cdlswSdlcPortN1_Object = MibTableColumn
hh3cdlswSdlcPortN1 = _Hh3cdlswSdlcPortN1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 8),
    _Hh3cdlswSdlcPortN1_Type()
)
hh3cdlswSdlcPortN1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortN1.setStatus("current")


class _Hh3cdlswSdlcPortN2_Type(Integer32):
    """Custom type hh3cdlswSdlcPortN2 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cdlswSdlcPortN2_Type.__name__ = "Integer32"
_Hh3cdlswSdlcPortN2_Object = MibTableColumn
hh3cdlswSdlcPortN2 = _Hh3cdlswSdlcPortN2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 9),
    _Hh3cdlswSdlcPortN2_Type()
)
hh3cdlswSdlcPortN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortN2.setStatus("current")


class _Hh3cdlswSdlcPortPollPauseTimer_Type(Integer32):
    """Custom type hh3cdlswSdlcPortPollPauseTimer based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Hh3cdlswSdlcPortPollPauseTimer_Type.__name__ = "Integer32"
_Hh3cdlswSdlcPortPollPauseTimer_Object = MibTableColumn
hh3cdlswSdlcPortPollPauseTimer = _Hh3cdlswSdlcPortPollPauseTimer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 10),
    _Hh3cdlswSdlcPortPollPauseTimer_Type()
)
hh3cdlswSdlcPortPollPauseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortPollPauseTimer.setStatus("current")


class _Hh3cdlswSdlcPortSimultaneousEnable_Type(Integer32):
    """Custom type hh3cdlswSdlcPortSimultaneousEnable based on Integer32"""
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


_Hh3cdlswSdlcPortSimultaneousEnable_Type.__name__ = "Integer32"
_Hh3cdlswSdlcPortSimultaneousEnable_Object = MibTableColumn
hh3cdlswSdlcPortSimultaneousEnable = _Hh3cdlswSdlcPortSimultaneousEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 11),
    _Hh3cdlswSdlcPortSimultaneousEnable_Type()
)
hh3cdlswSdlcPortSimultaneousEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortSimultaneousEnable.setStatus("current")


class _Hh3cdlswSdlcPortT1_Type(Integer32):
    """Custom type hh3cdlswSdlcPortT1 based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdlswSdlcPortT1_Type.__name__ = "Integer32"
_Hh3cdlswSdlcPortT1_Object = MibTableColumn
hh3cdlswSdlcPortT1 = _Hh3cdlswSdlcPortT1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 12),
    _Hh3cdlswSdlcPortT1_Type()
)
hh3cdlswSdlcPortT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortT1.setStatus("current")


class _Hh3cdlswSdlcPortT2_Type(Integer32):
    """Custom type hh3cdlswSdlcPortT2 based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdlswSdlcPortT2_Type.__name__ = "Integer32"
_Hh3cdlswSdlcPortT2_Object = MibTableColumn
hh3cdlswSdlcPortT2 = _Hh3cdlswSdlcPortT2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 1, 1, 13),
    _Hh3cdlswSdlcPortT2_Type()
)
hh3cdlswSdlcPortT2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcPortT2.setStatus("current")
_Hh3cdlswSdlcLsTable_Object = MibTable
hh3cdlswSdlcLsTable = _Hh3cdlswSdlcLsTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2)
)
if mibBuilder.loadTexts:
    hh3cdlswSdlcLsTable.setStatus("current")
_Hh3cdlswSdlcLsEntry_Object = MibTableRow
hh3cdlswSdlcLsEntry = _Hh3cdlswSdlcLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1)
)
hh3cdlswSdlcLsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-SNA-DLSW-MIB", "hh3cdlswSdlcLsAddress"),
)
if mibBuilder.loadTexts:
    hh3cdlswSdlcLsEntry.setStatus("current")


class _Hh3cdlswSdlcLsAddress_Type(Integer32):
    """Custom type hh3cdlswSdlcLsAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Hh3cdlswSdlcLsAddress_Type.__name__ = "Integer32"
_Hh3cdlswSdlcLsAddress_Object = MibTableColumn
hh3cdlswSdlcLsAddress = _Hh3cdlswSdlcLsAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 1),
    _Hh3cdlswSdlcLsAddress_Type()
)
hh3cdlswSdlcLsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cdlswSdlcLsAddress.setStatus("current")


class _Hh3cdlswSdlcLsLocalId_Type(Integer32):
    """Custom type hh3cdlswSdlcLsLocalId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cdlswSdlcLsLocalId_Type.__name__ = "Integer32"
_Hh3cdlswSdlcLsLocalId_Object = MibTableColumn
hh3cdlswSdlcLsLocalId = _Hh3cdlswSdlcLsLocalId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 2),
    _Hh3cdlswSdlcLsLocalId_Type()
)
hh3cdlswSdlcLsLocalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcLsLocalId.setStatus("current")
_Hh3cdlswSdlcLsRemoteMac_Type = MacAddressNC
_Hh3cdlswSdlcLsRemoteMac_Object = MibTableColumn
hh3cdlswSdlcLsRemoteMac = _Hh3cdlswSdlcLsRemoteMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 3),
    _Hh3cdlswSdlcLsRemoteMac_Type()
)
hh3cdlswSdlcLsRemoteMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcLsRemoteMac.setStatus("current")


class _Hh3cdlswSdlcLsSsap_Type(Integer32):
    """Custom type hh3cdlswSdlcLsSsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Hh3cdlswSdlcLsSsap_Type.__name__ = "Integer32"
_Hh3cdlswSdlcLsSsap_Object = MibTableColumn
hh3cdlswSdlcLsSsap = _Hh3cdlswSdlcLsSsap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 4),
    _Hh3cdlswSdlcLsSsap_Type()
)
hh3cdlswSdlcLsSsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcLsSsap.setStatus("current")


class _Hh3cdlswSdlcLsDsap_Type(Integer32):
    """Custom type hh3cdlswSdlcLsDsap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_Hh3cdlswSdlcLsDsap_Type.__name__ = "Integer32"
_Hh3cdlswSdlcLsDsap_Object = MibTableColumn
hh3cdlswSdlcLsDsap = _Hh3cdlswSdlcLsDsap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 5),
    _Hh3cdlswSdlcLsDsap_Type()
)
hh3cdlswSdlcLsDsap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcLsDsap.setStatus("current")
_Hh3cdlswSdlcLsStatus_Type = EntryStatus
_Hh3cdlswSdlcLsStatus_Object = MibTableColumn
hh3cdlswSdlcLsStatus = _Hh3cdlswSdlcLsStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 6, 2, 1, 6),
    _Hh3cdlswSdlcLsStatus_Type()
)
hh3cdlswSdlcLsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswSdlcLsStatus.setStatus("current")
_Hh3cdlswLlc2_ObjectIdentity = ObjectIdentity
hh3cdlswLlc2 = _Hh3cdlswLlc2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7)
)
_Hh3cdlswLlc2PortTable_Object = MibTable
hh3cdlswLlc2PortTable = _Hh3cdlswLlc2PortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1)
)
if mibBuilder.loadTexts:
    hh3cdlswLlc2PortTable.setStatus("current")
_Hh3cdlswLlc2PortEntry_Object = MibTableRow
hh3cdlswLlc2PortEntry = _Hh3cdlswLlc2PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1)
)
hh3cdlswLlc2PortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HH3C-SNA-DLSW-MIB", "hh3cdlswBridgeIfBriGru"),
)
if mibBuilder.loadTexts:
    hh3cdlswLlc2PortEntry.setStatus("current")


class _Hh3cdlswLLC2PortAckDelayTime_Type(Integer32):
    """Custom type hh3cdlswLLC2PortAckDelayTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdlswLLC2PortAckDelayTime_Type.__name__ = "Integer32"
_Hh3cdlswLLC2PortAckDelayTime_Object = MibTableColumn
hh3cdlswLLC2PortAckDelayTime = _Hh3cdlswLLC2PortAckDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 1),
    _Hh3cdlswLLC2PortAckDelayTime_Type()
)
hh3cdlswLLC2PortAckDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswLLC2PortAckDelayTime.setStatus("current")


class _Hh3cdlswLLC2PortAckMax_Type(Integer32):
    """Custom type hh3cdlswLLC2PortAckMax based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Hh3cdlswLLC2PortAckMax_Type.__name__ = "Integer32"
_Hh3cdlswLLC2PortAckMax_Object = MibTableColumn
hh3cdlswLLC2PortAckMax = _Hh3cdlswLLC2PortAckMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 2),
    _Hh3cdlswLLC2PortAckMax_Type()
)
hh3cdlswLLC2PortAckMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswLLC2PortAckMax.setStatus("current")


class _Hh3cdlswLLC2PortLocalWnd_Type(Integer32):
    """Custom type hh3cdlswLLC2PortLocalWnd based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_Hh3cdlswLLC2PortLocalWnd_Type.__name__ = "Integer32"
_Hh3cdlswLLC2PortLocalWnd_Object = MibTableColumn
hh3cdlswLLC2PortLocalWnd = _Hh3cdlswLLC2PortLocalWnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 3),
    _Hh3cdlswLLC2PortLocalWnd_Type()
)
hh3cdlswLLC2PortLocalWnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswLLC2PortLocalWnd.setStatus("current")


class _Hh3cdlswLLC2PortModulus_Type(Integer32):
    """Custom type hh3cdlswLLC2PortModulus based on Integer32"""
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


_Hh3cdlswLLC2PortModulus_Type.__name__ = "Integer32"
_Hh3cdlswLLC2PortModulus_Object = MibTableColumn
hh3cdlswLLC2PortModulus = _Hh3cdlswLLC2PortModulus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 4),
    _Hh3cdlswLLC2PortModulus_Type()
)
hh3cdlswLLC2PortModulus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswLLC2PortModulus.setStatus("current")


class _Hh3cdlswLLC2PortN2_Type(Integer32):
    """Custom type hh3cdlswLLC2PortN2 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cdlswLLC2PortN2_Type.__name__ = "Integer32"
_Hh3cdlswLLC2PortN2_Object = MibTableColumn
hh3cdlswLLC2PortN2 = _Hh3cdlswLLC2PortN2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 5),
    _Hh3cdlswLLC2PortN2_Type()
)
hh3cdlswLLC2PortN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswLLC2PortN2.setStatus("current")


class _Hh3cdlswLLC2PortT1_Type(Integer32):
    """Custom type hh3cdlswLLC2PortT1 based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdlswLLC2PortT1_Type.__name__ = "Integer32"
_Hh3cdlswLLC2PortT1_Object = MibTableColumn
hh3cdlswLLC2PortT1 = _Hh3cdlswLLC2PortT1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 6),
    _Hh3cdlswLLC2PortT1_Type()
)
hh3cdlswLLC2PortT1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswLLC2PortT1.setStatus("current")


class _Hh3cdlswLLC2PortTbusyTime_Type(Integer32):
    """Custom type hh3cdlswLLC2PortTbusyTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdlswLLC2PortTbusyTime_Type.__name__ = "Integer32"
_Hh3cdlswLLC2PortTbusyTime_Object = MibTableColumn
hh3cdlswLLC2PortTbusyTime = _Hh3cdlswLLC2PortTbusyTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 7),
    _Hh3cdlswLLC2PortTbusyTime_Type()
)
hh3cdlswLLC2PortTbusyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswLLC2PortTbusyTime.setStatus("current")


class _Hh3cdlswLLC2PortTpfTime_Type(Integer32):
    """Custom type hh3cdlswLLC2PortTpfTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdlswLLC2PortTpfTime_Type.__name__ = "Integer32"
_Hh3cdlswLLC2PortTpfTime_Object = MibTableColumn
hh3cdlswLLC2PortTpfTime = _Hh3cdlswLLC2PortTpfTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 8),
    _Hh3cdlswLLC2PortTpfTime_Type()
)
hh3cdlswLLC2PortTpfTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswLLC2PortTpfTime.setStatus("current")


class _Hh3cdlswLLC2PortTrejTime_Type(Integer32):
    """Custom type hh3cdlswLLC2PortTrejTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_Hh3cdlswLLC2PortTrejTime_Type.__name__ = "Integer32"
_Hh3cdlswLLC2PortTrejTime_Object = MibTableColumn
hh3cdlswLLC2PortTrejTime = _Hh3cdlswLLC2PortTrejTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 9),
    _Hh3cdlswLLC2PortTrejTime_Type()
)
hh3cdlswLLC2PortTrejTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswLLC2PortTrejTime.setStatus("current")


class _Hh3cdlswLLC2PortTxqMax_Type(Integer32):
    """Custom type hh3cdlswLLC2PortTxqMax based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_Hh3cdlswLLC2PortTxqMax_Type.__name__ = "Integer32"
_Hh3cdlswLLC2PortTxqMax_Object = MibTableColumn
hh3cdlswLLC2PortTxqMax = _Hh3cdlswLLC2PortTxqMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 7, 1, 1, 10),
    _Hh3cdlswLLC2PortTxqMax_Type()
)
hh3cdlswLLC2PortTxqMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cdlswLLC2PortTxqMax.setStatus("current")
_Hh3cdlswTraps_ObjectIdentity = ObjectIdentity
hh3cdlswTraps = _Hh3cdlswTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 8)
)
_Hh3cdlswTrapsV2_ObjectIdentity = ObjectIdentity
hh3cdlswTrapsV2 = _Hh3cdlswTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 8, 0)
)

# Managed Objects groups


# Notification objects

hh3cdlswTrapTConnPartnerReject = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 8, 0, 1)
)
hh3cdlswTrapTConnPartnerReject.setObjects(
    ("HH3C-SNA-DLSW-MIB", "hh3cdlswRemotePeerAddr")
)
if mibBuilder.loadTexts:
    hh3cdlswTrapTConnPartnerReject.setStatus(
        "current"
    )

hh3cdlswTrapTConnChangeState = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 8, 0, 2)
)
hh3cdlswTrapTConnChangeState.setObjects(
      *(("HH3C-SNA-DLSW-MIB", "hh3cdlswRemotePeerAddr"),
        ("HH3C-SNA-DLSW-MIB", "hh3cdlswRemotePeerLinkState"))
)
if mibBuilder.loadTexts:
    hh3cdlswTrapTConnChangeState.setStatus(
        "current"
    )

hh3cdlswTrapCircuitChangeState = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 37, 8, 0, 3)
)
hh3cdlswTrapCircuitChangeState.setObjects(
      *(("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS1CircuitId"),
        ("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitState"),
        ("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS1Mac"),
        ("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS1Sap"),
        ("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS2Mac"),
        ("HH3C-SNA-DLSW-MIB", "hh3cdlswCircuitS2Sap"))
)
if mibBuilder.loadTexts:
    hh3cdlswTrapCircuitChangeState.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SNA-DLSW-MIB",
    **{"MacAddressNC": MacAddressNC,
       "EndStationLocation": EndStationLocation,
       "DlcType": DlcType,
       "LFSize": LFSize,
       "CreateLineFlag": CreateLineFlag,
       "EntryStatus": EntryStatus,
       "hh3cdlsw": hh3cdlsw,
       "hh3cdlswNode": hh3cdlswNode,
       "hh3cdlswNodeVersion": hh3cdlswNodeVersion,
       "hh3cdlswNodeVendorID": hh3cdlswNodeVendorID,
       "hh3cdlswNodeVersionString": hh3cdlswNodeVersionString,
       "hh3cdlswNodeStdPacingSupport": hh3cdlswNodeStdPacingSupport,
       "hh3cdlswNodeStatus": hh3cdlswNodeStatus,
       "hh3cdlswNodeVirtualSegmentLFSize": hh3cdlswNodeVirtualSegmentLFSize,
       "hh3cdlswNodeLocalAddr": hh3cdlswNodeLocalAddr,
       "hh3cdlswNodePriority": hh3cdlswNodePriority,
       "hh3cdlswNodeInitWindow": hh3cdlswNodeInitWindow,
       "hh3cdlswNodeKeepAlive": hh3cdlswNodeKeepAlive,
       "hh3cdlswNodeMaxWindow": hh3cdlswNodeMaxWindow,
       "hh3cdlswNodePermitDynamic": hh3cdlswNodePermitDynamic,
       "hh3cdlswNodeConnTimeout": hh3cdlswNodeConnTimeout,
       "hh3cdlswNodeLocalPendTimeout": hh3cdlswNodeLocalPendTimeout,
       "hh3cdlswNodeRemotePendTimeout": hh3cdlswNodeRemotePendTimeout,
       "hh3cdlswNodeSnaCacheTimeout": hh3cdlswNodeSnaCacheTimeout,
       "hh3cdlswTrapControl": hh3cdlswTrapControl,
       "hh3cdlswTrapCntlState": hh3cdlswTrapCntlState,
       "hh3cdlswTConn": hh3cdlswTConn,
       "hh3cdlswRemotePeerTable": hh3cdlswRemotePeerTable,
       "hh3cdlswRemotePeerEntry": hh3cdlswRemotePeerEntry,
       "hh3cdlswRemotePeerAddr": hh3cdlswRemotePeerAddr,
       "hh3cdlswRemotePeerVersion": hh3cdlswRemotePeerVersion,
       "hh3cdlswRemotePeerVendorID": hh3cdlswRemotePeerVendorID,
       "hh3cdlswRemotePeerPaceWindInit": hh3cdlswRemotePeerPaceWindInit,
       "hh3cdlswRemotePeerVersionString": hh3cdlswRemotePeerVersionString,
       "hh3cdlswRemotePeerIsConfig": hh3cdlswRemotePeerIsConfig,
       "hh3cdlswRemotePeerCost": hh3cdlswRemotePeerCost,
       "hh3cdlswRemotePeerKeepAlive": hh3cdlswRemotePeerKeepAlive,
       "hh3cdlswRemotePeerLf": hh3cdlswRemotePeerLf,
       "hh3cdlswRemotePeerTcpQueneMax": hh3cdlswRemotePeerTcpQueneMax,
       "hh3cdlswRemotePeerHaveBackup": hh3cdlswRemotePeerHaveBackup,
       "hh3cdlswRemotePeerIsBackup": hh3cdlswRemotePeerIsBackup,
       "hh3cdlswRemotePeerBackupAddr": hh3cdlswRemotePeerBackupAddr,
       "hh3cdlswRemotePeerLinger": hh3cdlswRemotePeerLinger,
       "hh3cdlswRemotePeerLinkState": hh3cdlswRemotePeerLinkState,
       "hh3cdlswRemotePeerRecvPacks": hh3cdlswRemotePeerRecvPacks,
       "hh3cdlswRemotePeerSendPacks": hh3cdlswRemotePeerSendPacks,
       "hh3cdlswRemotePeerDrops": hh3cdlswRemotePeerDrops,
       "hh3cdlswRemotePeerUptime": hh3cdlswRemotePeerUptime,
       "hh3cdlswRemotePeerEntryStatus": hh3cdlswRemotePeerEntryStatus,
       "hh3cdlswBridgeGroup": hh3cdlswBridgeGroup,
       "hh3cdlswBridgeTable": hh3cdlswBridgeTable,
       "hh3cdlswBridgeEntry": hh3cdlswBridgeEntry,
       "hh3cdlswBridgeNum": hh3cdlswBridgeNum,
       "hh3cdlswBridgeStatus": hh3cdlswBridgeStatus,
       "hh3cdlswBridgeIfTable": hh3cdlswBridgeIfTable,
       "hh3cdlswBridgeIfEntry": hh3cdlswBridgeIfEntry,
       "hh3cdlswBridgeIfBriGru": hh3cdlswBridgeIfBriGru,
       "hh3cdlswBridgeIfName": hh3cdlswBridgeIfName,
       "hh3cdlswBridgeIfStatus": hh3cdlswBridgeIfStatus,
       "hh3cdlswLocDirectory": hh3cdlswLocDirectory,
       "hh3cdlswLocMacTable": hh3cdlswLocMacTable,
       "hh3cdlswLocMacEntry": hh3cdlswLocMacEntry,
       "hh3cdlswLocMacHashIndex": hh3cdlswLocMacHashIndex,
       "hh3cdlswLocMacHashIndexSeqNum": hh3cdlswLocMacHashIndexSeqNum,
       "hh3cdlswLocMacMac": hh3cdlswLocMacMac,
       "hh3cdlswLocMacLocalInterfaceName": hh3cdlswLocMacLocalInterfaceName,
       "hh3cdlswCircuit": hh3cdlswCircuit,
       "hh3cdlswCircuitTable": hh3cdlswCircuitTable,
       "hh3cdlswCircuitEntry": hh3cdlswCircuitEntry,
       "hh3cdlswCircuitS1CircuitId": hh3cdlswCircuitS1CircuitId,
       "hh3cdlswCircuitS1Mac": hh3cdlswCircuitS1Mac,
       "hh3cdlswCircuitS1Sap": hh3cdlswCircuitS1Sap,
       "hh3cdlswCircuitS2Mac": hh3cdlswCircuitS2Mac,
       "hh3cdlswCircuitS2Sap": hh3cdlswCircuitS2Sap,
       "hh3cdlswCircuitS1IfIndex": hh3cdlswCircuitS1IfIndex,
       "hh3cdlswCircuitS1Ifname": hh3cdlswCircuitS1Ifname,
       "hh3cdlswCircuitS1DlcType": hh3cdlswCircuitS1DlcType,
       "hh3cdlswCircuitS2TAddress": hh3cdlswCircuitS2TAddress,
       "hh3cdlswCircuitS2CircuitId": hh3cdlswCircuitS2CircuitId,
       "hh3cdlswCircuitOrigin": hh3cdlswCircuitOrigin,
       "hh3cdlswCircuitEntryTime": hh3cdlswCircuitEntryTime,
       "hh3cdlswCircuitStateTime": hh3cdlswCircuitStateTime,
       "hh3cdlswCircuitState": hh3cdlswCircuitState,
       "hh3cdlswCircuitFCSendGrantedUnits": hh3cdlswCircuitFCSendGrantedUnits,
       "hh3cdlswCircuitFCSendCurrentWndw": hh3cdlswCircuitFCSendCurrentWndw,
       "hh3cdlswCircuitFCRecvGrantedUnits": hh3cdlswCircuitFCRecvGrantedUnits,
       "hh3cdlswCircuitFCRecvCurrentWndw": hh3cdlswCircuitFCRecvCurrentWndw,
       "hh3cdlswSdlc": hh3cdlswSdlc,
       "hh3cdlswSdlcPortTable": hh3cdlswSdlcPortTable,
       "hh3cdlswSdlcPortEntry": hh3cdlswSdlcPortEntry,
       "hh3cdlswSdlcPortSerialName": hh3cdlswSdlcPortSerialName,
       "hh3cdlswSdlcPortEncap": hh3cdlswSdlcPortEncap,
       "hh3cdlswSdlcPortRole": hh3cdlswSdlcPortRole,
       "hh3cdlswSdlcPortVmac": hh3cdlswSdlcPortVmac,
       "hh3cdlswSdlcPortHoldq": hh3cdlswSdlcPortHoldq,
       "hh3cdlswSdlcPortK": hh3cdlswSdlcPortK,
       "hh3cdlswSdlcPortModule": hh3cdlswSdlcPortModule,
       "hh3cdlswSdlcPortN1": hh3cdlswSdlcPortN1,
       "hh3cdlswSdlcPortN2": hh3cdlswSdlcPortN2,
       "hh3cdlswSdlcPortPollPauseTimer": hh3cdlswSdlcPortPollPauseTimer,
       "hh3cdlswSdlcPortSimultaneousEnable": hh3cdlswSdlcPortSimultaneousEnable,
       "hh3cdlswSdlcPortT1": hh3cdlswSdlcPortT1,
       "hh3cdlswSdlcPortT2": hh3cdlswSdlcPortT2,
       "hh3cdlswSdlcLsTable": hh3cdlswSdlcLsTable,
       "hh3cdlswSdlcLsEntry": hh3cdlswSdlcLsEntry,
       "hh3cdlswSdlcLsAddress": hh3cdlswSdlcLsAddress,
       "hh3cdlswSdlcLsLocalId": hh3cdlswSdlcLsLocalId,
       "hh3cdlswSdlcLsRemoteMac": hh3cdlswSdlcLsRemoteMac,
       "hh3cdlswSdlcLsSsap": hh3cdlswSdlcLsSsap,
       "hh3cdlswSdlcLsDsap": hh3cdlswSdlcLsDsap,
       "hh3cdlswSdlcLsStatus": hh3cdlswSdlcLsStatus,
       "hh3cdlswLlc2": hh3cdlswLlc2,
       "hh3cdlswLlc2PortTable": hh3cdlswLlc2PortTable,
       "hh3cdlswLlc2PortEntry": hh3cdlswLlc2PortEntry,
       "hh3cdlswLLC2PortAckDelayTime": hh3cdlswLLC2PortAckDelayTime,
       "hh3cdlswLLC2PortAckMax": hh3cdlswLLC2PortAckMax,
       "hh3cdlswLLC2PortLocalWnd": hh3cdlswLLC2PortLocalWnd,
       "hh3cdlswLLC2PortModulus": hh3cdlswLLC2PortModulus,
       "hh3cdlswLLC2PortN2": hh3cdlswLLC2PortN2,
       "hh3cdlswLLC2PortT1": hh3cdlswLLC2PortT1,
       "hh3cdlswLLC2PortTbusyTime": hh3cdlswLLC2PortTbusyTime,
       "hh3cdlswLLC2PortTpfTime": hh3cdlswLLC2PortTpfTime,
       "hh3cdlswLLC2PortTrejTime": hh3cdlswLLC2PortTrejTime,
       "hh3cdlswLLC2PortTxqMax": hh3cdlswLLC2PortTxqMax,
       "hh3cdlswTraps": hh3cdlswTraps,
       "hh3cdlswTrapsV2": hh3cdlswTrapsV2,
       "hh3cdlswTrapTConnPartnerReject": hh3cdlswTrapTConnPartnerReject,
       "hh3cdlswTrapTConnChangeState": hh3cdlswTrapTConnChangeState,
       "hh3cdlswTrapCircuitChangeState": hh3cdlswTrapCircuitChangeState}
)
