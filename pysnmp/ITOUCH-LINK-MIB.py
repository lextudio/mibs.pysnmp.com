# SNMP MIB module (ITOUCH-LINK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-LINK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:17 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(iTouch,) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "iTouch")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XLink_ObjectIdentity = ObjectIdentity
xLink = _XLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 24)
)
_XLinkBasic_ObjectIdentity = ObjectIdentity
xLinkBasic = _XLinkBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 24, 1)
)
_LinkTable_Object = MibTable
linkTable = _LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 1)
)
if mibBuilder.loadTexts:
    linkTable.setStatus("mandatory")
_LinkEntry_Object = MibTableRow
linkEntry = _LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1)
)
linkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    linkEntry.setStatus("mandatory")
_LinkNoBuffers_Type = Counter32
_LinkNoBuffers_Object = MibTableColumn
linkNoBuffers = _LinkNoBuffers_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 1),
    _LinkNoBuffers_Type()
)
linkNoBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkNoBuffers.setStatus("mandatory")
_LinkDelayExceeded_Type = Counter32
_LinkDelayExceeded_Object = MibTableColumn
linkDelayExceeded = _LinkDelayExceeded_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 2),
    _LinkDelayExceeded_Type()
)
linkDelayExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDelayExceeded.setStatus("mandatory")
_LinkOutputQFull_Type = Counter32
_LinkOutputQFull_Object = MibTableColumn
linkOutputQFull = _LinkOutputQFull_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 3),
    _LinkOutputQFull_Type()
)
linkOutputQFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkOutputQFull.setStatus("mandatory")
_LinkDownTime_Type = Counter32
_LinkDownTime_Object = MibTableColumn
linkDownTime = _LinkDownTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 4),
    _LinkDownTime_Type()
)
linkDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDownTime.setStatus("mandatory")
_LinkDownCount_Type = Counter32
_LinkDownCount_Object = MibTableColumn
linkDownCount = _LinkDownCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 5),
    _LinkDownCount_Type()
)
linkDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDownCount.setStatus("mandatory")
_LinkDownLastStart_Type = TimeTicks
_LinkDownLastStart_Object = MibTableColumn
linkDownLastStart = _LinkDownLastStart_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 6),
    _LinkDownLastStart_Type()
)
linkDownLastStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkDownLastStart.setStatus("mandatory")


class _LinkStatus_Type(Integer32):
    """Custom type linkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              128,
              129,
              130,
              131,
              132,
              133,
              138,
              139,
              140,
              141,
              143,
              145,
              146)
        )
    )
    namedValues = NamedValues(
        *(("badQuality", 146),
          ("disabled", 145),
          ("down", 132),
          ("initWait", 129),
          ("initWaitDsr", 128),
          ("loop", 138),
          ("purgeWait", 131),
          ("purging", 133),
          ("running1", 7),
          ("running2", 130),
          ("speedChange", 143),
          ("testLoop", 141),
          ("testReceive", 140),
          ("testSend", 139))
    )


_LinkStatus_Type.__name__ = "Integer32"
_LinkStatus_Object = MibTableColumn
linkStatus = _LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 7),
    _LinkStatus_Type()
)
linkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatus.setStatus("mandatory")
_LinkLostBuffers_Type = Counter32
_LinkLostBuffers_Object = MibTableColumn
linkLostBuffers = _LinkLostBuffers_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 1, 1, 8),
    _LinkLostBuffers_Type()
)
linkLostBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkLostBuffers.setStatus("mandatory")
_LinkResourceTable_Object = MibTable
linkResourceTable = _LinkResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 2)
)
if mibBuilder.loadTexts:
    linkResourceTable.setStatus("mandatory")
_LinkResourceEntry_Object = MibTableRow
linkResourceEntry = _LinkResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 2, 1)
)
linkResourceEntry.setIndexNames(
    (0, "ITOUCH-LINK-MIB", "linkResourceType"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    linkResourceEntry.setStatus("mandatory")


class _LinkResourceType_Type(Integer32):
    """Custom type linkResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("outputQueue", 2),
          ("utilization", 1))
    )


_LinkResourceType_Type.__name__ = "Integer32"
_LinkResourceType_Object = MibTableColumn
linkResourceType = _LinkResourceType_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 2, 1, 1),
    _LinkResourceType_Type()
)
linkResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkResourceType.setStatus("mandatory")
_LinkResourceCurrent_Type = Gauge32
_LinkResourceCurrent_Object = MibTableColumn
linkResourceCurrent = _LinkResourceCurrent_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 2, 1, 2),
    _LinkResourceCurrent_Type()
)
linkResourceCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkResourceCurrent.setStatus("mandatory")
_LinkResourceHigh_Type = Gauge32
_LinkResourceHigh_Object = MibTableColumn
linkResourceHigh = _LinkResourceHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 2, 1, 3),
    _LinkResourceHigh_Type()
)
linkResourceHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkResourceHigh.setStatus("mandatory")
_LinkResourceAverage_Type = Gauge32
_LinkResourceAverage_Object = MibTableColumn
linkResourceAverage = _LinkResourceAverage_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 1, 2, 1, 4),
    _LinkResourceAverage_Type()
)
linkResourceAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkResourceAverage.setStatus("mandatory")
_XWan_ObjectIdentity = ObjectIdentity
xWan = _XWan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 24, 3)
)
_WanTable_Object = MibTable
wanTable = _WanTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 3, 1)
)
if mibBuilder.loadTexts:
    wanTable.setStatus("mandatory")
_WanEntry_Object = MibTableRow
wanEntry = _WanEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1)
)
wanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wanEntry.setStatus("mandatory")


class _WanProtocol_Type(Integer32):
    """Custom type wanProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("fr", 3),
          ("fransi", 6),
          ("frdceansi", 8),
          ("frdcelmi", 7),
          ("frlmi", 5),
          ("ppp", 4),
          ("x25", 9),
          ("xcp", 2))
    )


_WanProtocol_Type.__name__ = "Integer32"
_WanProtocol_Object = MibTableColumn
wanProtocol = _WanProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 1),
    _WanProtocol_Type()
)
wanProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanProtocol.setStatus("mandatory")


class _WanCompressionAdminStatus_Type(Integer32):
    """Custom type wanCompressionAdminStatus based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              256)
        )
    )
    namedValues = NamedValues(
        *(("auto", 256),
          ("compress", 2),
          ("noCompression", 1))
    )


_WanCompressionAdminStatus_Type.__name__ = "Integer32"
_WanCompressionAdminStatus_Object = MibTableColumn
wanCompressionAdminStatus = _WanCompressionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 2),
    _WanCompressionAdminStatus_Type()
)
wanCompressionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanCompressionAdminStatus.setStatus("mandatory")


class _WanMaxForwardDelay_Type(Integer32):
    """Custom type wanMaxForwardDelay based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_WanMaxForwardDelay_Type.__name__ = "Integer32"
_WanMaxForwardDelay_Object = MibTableColumn
wanMaxForwardDelay = _WanMaxForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 3),
    _WanMaxForwardDelay_Type()
)
wanMaxForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanMaxForwardDelay.setStatus("mandatory")


class _WanMaxMultiForwardDelay_Type(Integer32):
    """Custom type wanMaxMultiForwardDelay based on Integer32"""
    defaultValue = 700

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32000),
    )


_WanMaxMultiForwardDelay_Type.__name__ = "Integer32"
_WanMaxMultiForwardDelay_Object = MibTableColumn
wanMaxMultiForwardDelay = _WanMaxMultiForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 4),
    _WanMaxMultiForwardDelay_Type()
)
wanMaxMultiForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanMaxMultiForwardDelay.setStatus("mandatory")


class _WanAdminSpeed_Type(Integer32):
    """Custom type wanAdminSpeed based on Integer32"""
    defaultValue = 0


_WanAdminSpeed_Object = MibTableColumn
wanAdminSpeed = _WanAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 5),
    _WanAdminSpeed_Type()
)
wanAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wanAdminSpeed.setStatus("mandatory")


class _WanCompressionOperStatus_Type(Integer32):
    """Custom type wanCompressionOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compressing", 2),
          ("notCompressing", 1))
    )


_WanCompressionOperStatus_Type.__name__ = "Integer32"
_WanCompressionOperStatus_Object = MibTableColumn
wanCompressionOperStatus = _WanCompressionOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 24, 3, 1, 1, 6),
    _WanCompressionOperStatus_Type()
)
wanCompressionOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanCompressionOperStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-LINK-MIB",
    **{"xLink": xLink,
       "xLinkBasic": xLinkBasic,
       "linkTable": linkTable,
       "linkEntry": linkEntry,
       "linkNoBuffers": linkNoBuffers,
       "linkDelayExceeded": linkDelayExceeded,
       "linkOutputQFull": linkOutputQFull,
       "linkDownTime": linkDownTime,
       "linkDownCount": linkDownCount,
       "linkDownLastStart": linkDownLastStart,
       "linkStatus": linkStatus,
       "linkLostBuffers": linkLostBuffers,
       "linkResourceTable": linkResourceTable,
       "linkResourceEntry": linkResourceEntry,
       "linkResourceType": linkResourceType,
       "linkResourceCurrent": linkResourceCurrent,
       "linkResourceHigh": linkResourceHigh,
       "linkResourceAverage": linkResourceAverage,
       "xWan": xWan,
       "wanTable": wanTable,
       "wanEntry": wanEntry,
       "wanProtocol": wanProtocol,
       "wanCompressionAdminStatus": wanCompressionAdminStatus,
       "wanMaxForwardDelay": wanMaxForwardDelay,
       "wanMaxMultiForwardDelay": wanMaxMultiForwardDelay,
       "wanAdminSpeed": wanAdminSpeed,
       "wanCompressionOperStatus": wanCompressionOperStatus}
)
