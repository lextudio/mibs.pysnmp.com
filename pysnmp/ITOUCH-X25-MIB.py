# SNMP MIB module (ITOUCH-X25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-X25-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:24 2024
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

(iTouch,) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "iTouch")

(X121Address,) = mibBuilder.importSymbols(
    "RFC1382-MIB",
    "X121Address")

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

_XX25_ObjectIdentity = ObjectIdentity
xX25 = _XX25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 20)
)
_XX25ChannelTable_Object = MibTable
xX25ChannelTable = _XX25ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 4)
)
if mibBuilder.loadTexts:
    xX25ChannelTable.setStatus("mandatory")
_XX25ChannelEntry_Object = MibTableRow
xX25ChannelEntry = _XX25ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 4, 1)
)
xX25ChannelEntry.setIndexNames(
    (0, "ITOUCH-X25-MIB", "xX25ChannelIndex"),
)
if mibBuilder.loadTexts:
    xX25ChannelEntry.setStatus("mandatory")
_XX25ChannelIndex_Type = Integer32
_XX25ChannelIndex_Object = MibTableColumn
xX25ChannelIndex = _XX25ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 4, 1, 1),
    _XX25ChannelIndex_Type()
)
xX25ChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xX25ChannelIndex.setStatus("mandatory")


class _XX25ChannelLowPVC_Type(Integer32):
    """Custom type xX25ChannelLowPVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_XX25ChannelLowPVC_Type.__name__ = "Integer32"
_XX25ChannelLowPVC_Object = MibTableColumn
xX25ChannelLowPVC = _XX25ChannelLowPVC_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 4, 1, 2),
    _XX25ChannelLowPVC_Type()
)
xX25ChannelLowPVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25ChannelLowPVC.setStatus("mandatory")


class _XX25ChannelHighPVC_Type(Integer32):
    """Custom type xX25ChannelHighPVC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_XX25ChannelHighPVC_Type.__name__ = "Integer32"
_XX25ChannelHighPVC_Object = MibTableColumn
xX25ChannelHighPVC = _XX25ChannelHighPVC_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 4, 1, 3),
    _XX25ChannelHighPVC_Type()
)
xX25ChannelHighPVC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25ChannelHighPVC.setStatus("mandatory")


class _XX25ChannelNetwork_Type(Integer32):
    """Custom type xX25ChannelNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccitt", 1),
          ("ddnStandard", 2))
    )


_XX25ChannelNetwork_Type.__name__ = "Integer32"
_XX25ChannelNetwork_Object = MibTableColumn
xX25ChannelNetwork = _XX25ChannelNetwork_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 4, 1, 4),
    _XX25ChannelNetwork_Type()
)
xX25ChannelNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25ChannelNetwork.setStatus("mandatory")


class _XX25ChannelMaxPrecedence_Type(Integer32):
    """Custom type xX25ChannelMaxPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_XX25ChannelMaxPrecedence_Type.__name__ = "Integer32"
_XX25ChannelMaxPrecedence_Object = MibTableColumn
xX25ChannelMaxPrecedence = _XX25ChannelMaxPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 4, 1, 5),
    _XX25ChannelMaxPrecedence_Type()
)
xX25ChannelMaxPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25ChannelMaxPrecedence.setStatus("mandatory")
_XX25ChannelStdVersion_Type = Integer32
_XX25ChannelStdVersion_Object = MibTableColumn
xX25ChannelStdVersion = _XX25ChannelStdVersion_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 4, 1, 6),
    _XX25ChannelStdVersion_Type()
)
xX25ChannelStdVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25ChannelStdVersion.setStatus("mandatory")
_XX25VcCfgTable_Object = MibTable
xX25VcCfgTable = _XX25VcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6)
)
if mibBuilder.loadTexts:
    xX25VcCfgTable.setStatus("mandatory")
_XX25VcCfgEntry_Object = MibTableRow
xX25VcCfgEntry = _XX25VcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6, 1)
)
xX25VcCfgEntry.setIndexNames(
    (0, "ITOUCH-X25-MIB", "xX25VcCfgIndex"),
)
if mibBuilder.loadTexts:
    xX25VcCfgEntry.setStatus("mandatory")
_XX25VcCfgIndex_Type = Integer32
_XX25VcCfgIndex_Object = MibTableColumn
xX25VcCfgIndex = _XX25VcCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6, 1, 1),
    _XX25VcCfgIndex_Type()
)
xX25VcCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xX25VcCfgIndex.setStatus("mandatory")
_XX25VcCfgPartnerAddr_Type = X121Address
_XX25VcCfgPartnerAddr_Object = MibTableColumn
xX25VcCfgPartnerAddr = _XX25VcCfgPartnerAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6, 1, 2),
    _XX25VcCfgPartnerAddr_Type()
)
xX25VcCfgPartnerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25VcCfgPartnerAddr.setStatus("mandatory")


class _XX25VcCfgInterfaceIndex_Type(Integer32):
    """Custom type xX25VcCfgInterfaceIndex based on Integer32"""
    defaultValue = 0


_XX25VcCfgInterfaceIndex_Object = MibTableColumn
xX25VcCfgInterfaceIndex = _XX25VcCfgInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6, 1, 3),
    _XX25VcCfgInterfaceIndex_Type()
)
xX25VcCfgInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25VcCfgInterfaceIndex.setStatus("mandatory")


class _XX25VcCfgLinkIndex_Type(Integer32):
    """Custom type xX25VcCfgLinkIndex based on Integer32"""
    defaultValue = 0


_XX25VcCfgLinkIndex_Object = MibTableColumn
xX25VcCfgLinkIndex = _XX25VcCfgLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6, 1, 4),
    _XX25VcCfgLinkIndex_Type()
)
xX25VcCfgLinkIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25VcCfgLinkIndex.setStatus("mandatory")


class _XX25VcCfgProtocol_Type(Integer32):
    """Custom type xX25VcCfgProtocol based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 1),
          ("bridged", 2),
          ("decnet", 3),
          ("ip", 4),
          ("ipx", 5),
          ("multiProtocol", 6),
          ("osi", 7))
    )


_XX25VcCfgProtocol_Type.__name__ = "Integer32"
_XX25VcCfgProtocol_Object = MibTableColumn
xX25VcCfgProtocol = _XX25VcCfgProtocol_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6, 1, 5),
    _XX25VcCfgProtocol_Type()
)
xX25VcCfgProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25VcCfgProtocol.setStatus("mandatory")


class _XX25VcCfgEncapsulation_Type(Integer32):
    """Custom type xX25VcCfgEncapsulation based on Integer32"""
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
        *(("dedicated", 2),
          ("null", 1),
          ("snap", 3))
    )


_XX25VcCfgEncapsulation_Type.__name__ = "Integer32"
_XX25VcCfgEncapsulation_Object = MibTableColumn
xX25VcCfgEncapsulation = _XX25VcCfgEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6, 1, 6),
    _XX25VcCfgEncapsulation_Type()
)
xX25VcCfgEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25VcCfgEncapsulation.setStatus("mandatory")


class _XX25VcCfgPvc_Type(Integer32):
    """Custom type xX25VcCfgPvc based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_XX25VcCfgPvc_Type.__name__ = "Integer32"
_XX25VcCfgPvc_Object = MibTableColumn
xX25VcCfgPvc = _XX25VcCfgPvc_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6, 1, 7),
    _XX25VcCfgPvc_Type()
)
xX25VcCfgPvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25VcCfgPvc.setStatus("mandatory")


class _XX25VcCfgPartnerIpAddress_Type(IpAddress):
    """Custom type xX25VcCfgPartnerIpAddress based on IpAddress"""
    defaultValue = 0


_XX25VcCfgPartnerIpAddress_Object = MibTableColumn
xX25VcCfgPartnerIpAddress = _XX25VcCfgPartnerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6, 1, 8),
    _XX25VcCfgPartnerIpAddress_Type()
)
xX25VcCfgPartnerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25VcCfgPartnerIpAddress.setStatus("mandatory")


class _XX25VcCfgClearFacilities_Type(Integer32):
    """Custom type xX25VcCfgClearFacilities based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_XX25VcCfgClearFacilities_Type.__name__ = "Integer32"
_XX25VcCfgClearFacilities_Object = MibTableColumn
xX25VcCfgClearFacilities = _XX25VcCfgClearFacilities_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6, 1, 9),
    _XX25VcCfgClearFacilities_Type()
)
xX25VcCfgClearFacilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25VcCfgClearFacilities.setStatus("mandatory")


class _XX25VcCfgStatus_Type(Integer32):
    """Custom type xX25VcCfgStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_XX25VcCfgStatus_Type.__name__ = "Integer32"
_XX25VcCfgStatus_Object = MibTableColumn
xX25VcCfgStatus = _XX25VcCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 6, 1, 10),
    _XX25VcCfgStatus_Type()
)
xX25VcCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25VcCfgStatus.setStatus("mandatory")
_XX25LinkTable_Object = MibTable
xX25LinkTable = _XX25LinkTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7)
)
if mibBuilder.loadTexts:
    xX25LinkTable.setStatus("mandatory")
_XX25LinkEntry_Object = MibTableRow
xX25LinkEntry = _XX25LinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1)
)
xX25LinkEntry.setIndexNames(
    (0, "ITOUCH-X25-MIB", "xX25LinkIndex"),
)
if mibBuilder.loadTexts:
    xX25LinkEntry.setStatus("mandatory")
_XX25LinkIndex_Type = Integer32
_XX25LinkIndex_Object = MibTableColumn
xX25LinkIndex = _XX25LinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 1),
    _XX25LinkIndex_Type()
)
xX25LinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xX25LinkIndex.setStatus("mandatory")


class _XX25LinkRRDelay_Type(Integer32):
    """Custom type xX25LinkRRDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_XX25LinkRRDelay_Type.__name__ = "Integer32"
_XX25LinkRRDelay_Object = MibTableColumn
xX25LinkRRDelay = _XX25LinkRRDelay_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 2),
    _XX25LinkRRDelay_Type()
)
xX25LinkRRDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkRRDelay.setStatus("mandatory")


class _XX25LinkIdleTimeout_Type(Integer32):
    """Custom type xX25LinkIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_XX25LinkIdleTimeout_Type.__name__ = "Integer32"
_XX25LinkIdleTimeout_Object = MibTableColumn
xX25LinkIdleTimeout = _XX25LinkIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 3),
    _XX25LinkIdleTimeout_Type()
)
xX25LinkIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkIdleTimeout.setStatus("mandatory")


class _XX25LinkHoldDownTimer_Type(Integer32):
    """Custom type xX25LinkHoldDownTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_XX25LinkHoldDownTimer_Type.__name__ = "Integer32"
_XX25LinkHoldDownTimer_Object = MibTableColumn
xX25LinkHoldDownTimer = _XX25LinkHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 4),
    _XX25LinkHoldDownTimer_Type()
)
xX25LinkHoldDownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkHoldDownTimer.setStatus("mandatory")


class _XX25LinkAccUncfgCalls_Type(Integer32):
    """Custom type xX25LinkAccUncfgCalls based on Integer32"""
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


_XX25LinkAccUncfgCalls_Type.__name__ = "Integer32"
_XX25LinkAccUncfgCalls_Object = MibTableColumn
xX25LinkAccUncfgCalls = _XX25LinkAccUncfgCalls_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 5),
    _XX25LinkAccUncfgCalls_Type()
)
xX25LinkAccUncfgCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkAccUncfgCalls.setStatus("mandatory")


class _XX25LinkDefWindSize_Type(Integer32):
    """Custom type xX25LinkDefWindSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_XX25LinkDefWindSize_Type.__name__ = "Integer32"
_XX25LinkDefWindSize_Object = MibTableColumn
xX25LinkDefWindSize = _XX25LinkDefWindSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 6),
    _XX25LinkDefWindSize_Type()
)
xX25LinkDefWindSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkDefWindSize.setStatus("mandatory")


class _XX25LinkMaxWindSize_Type(Integer32):
    """Custom type xX25LinkMaxWindSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_XX25LinkMaxWindSize_Type.__name__ = "Integer32"
_XX25LinkMaxWindSize_Object = MibTableColumn
xX25LinkMaxWindSize = _XX25LinkMaxWindSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 7),
    _XX25LinkMaxWindSize_Type()
)
xX25LinkMaxWindSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkMaxWindSize.setStatus("mandatory")


class _XX25LinkDefPktSize_Type(Integer32):
    """Custom type xX25LinkDefPktSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              64,
              128,
              256,
              512,
              1024,
              2048,
              4096)
        )
    )
    namedValues = NamedValues(
        *(("bytes1024", 1024),
          ("bytes128", 128),
          ("bytes16", 16),
          ("bytes2048", 2048),
          ("bytes256", 256),
          ("bytes32", 32),
          ("bytes4096", 4096),
          ("bytes512", 512),
          ("bytes64", 64))
    )


_XX25LinkDefPktSize_Type.__name__ = "Integer32"
_XX25LinkDefPktSize_Object = MibTableColumn
xX25LinkDefPktSize = _XX25LinkDefPktSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 8),
    _XX25LinkDefPktSize_Type()
)
xX25LinkDefPktSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkDefPktSize.setStatus("mandatory")


class _XX25LinkDefThrptClassIn_Type(Integer32):
    """Custom type xX25LinkDefThrptClassIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(75,
              150,
              300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200,
              48000)
        )
    )
    namedValues = NamedValues(
        *(("bps1200", 1200),
          ("bps150", 150),
          ("bps19200", 19200),
          ("bps2400", 2400),
          ("bps300", 300),
          ("bps4800", 4800),
          ("bps48000", 48000),
          ("bps600", 600),
          ("bps75", 75),
          ("bps9600", 9600))
    )


_XX25LinkDefThrptClassIn_Type.__name__ = "Integer32"
_XX25LinkDefThrptClassIn_Object = MibTableColumn
xX25LinkDefThrptClassIn = _XX25LinkDefThrptClassIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 9),
    _XX25LinkDefThrptClassIn_Type()
)
xX25LinkDefThrptClassIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkDefThrptClassIn.setStatus("mandatory")


class _XX25LinkDefThrptClassOut_Type(Integer32):
    """Custom type xX25LinkDefThrptClassOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(75,
              150,
              300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200,
              48000)
        )
    )
    namedValues = NamedValues(
        *(("bps1200", 1200),
          ("bps150", 150),
          ("bps19200", 19200),
          ("bps2400", 2400),
          ("bps300", 300),
          ("bps4800", 4800),
          ("bps48000", 48000),
          ("bps600", 600),
          ("bps75", 75),
          ("bps9600", 9600))
    )


_XX25LinkDefThrptClassOut_Type.__name__ = "Integer32"
_XX25LinkDefThrptClassOut_Object = MibTableColumn
xX25LinkDefThrptClassOut = _XX25LinkDefThrptClassOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 10),
    _XX25LinkDefThrptClassOut_Type()
)
xX25LinkDefThrptClassOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkDefThrptClassOut.setStatus("mandatory")


class _XX25LinkDefThrptClassInMsk_Type(Integer32):
    """Custom type xX25LinkDefThrptClassInMsk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(75,
              150,
              300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200,
              48000)
        )
    )
    namedValues = NamedValues(
        *(("bps1200", 1200),
          ("bps150", 150),
          ("bps19200", 19200),
          ("bps2400", 2400),
          ("bps300", 300),
          ("bps4800", 4800),
          ("bps48000", 48000),
          ("bps600", 600),
          ("bps75", 75),
          ("bps9600", 9600))
    )


_XX25LinkDefThrptClassInMsk_Type.__name__ = "Integer32"
_XX25LinkDefThrptClassInMsk_Object = MibTableColumn
xX25LinkDefThrptClassInMsk = _XX25LinkDefThrptClassInMsk_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 11),
    _XX25LinkDefThrptClassInMsk_Type()
)
xX25LinkDefThrptClassInMsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkDefThrptClassInMsk.setStatus("deprecated")


class _XX25LinkDefThrptClassOutMsk_Type(Integer32):
    """Custom type xX25LinkDefThrptClassOutMsk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(75,
              150,
              300,
              600,
              1200,
              2400,
              4800,
              9600,
              19200,
              48000)
        )
    )
    namedValues = NamedValues(
        *(("bps1200", 1200),
          ("bps150", 150),
          ("bps19200", 19200),
          ("bps2400", 2400),
          ("bps300", 300),
          ("bps4800", 4800),
          ("bps48000", 48000),
          ("bps600", 600),
          ("bps75", 75),
          ("bps9600", 9600))
    )


_XX25LinkDefThrptClassOutMsk_Type.__name__ = "Integer32"
_XX25LinkDefThrptClassOutMsk_Object = MibTableColumn
xX25LinkDefThrptClassOutMsk = _XX25LinkDefThrptClassOutMsk_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 12),
    _XX25LinkDefThrptClassOutMsk_Type()
)
xX25LinkDefThrptClassOutMsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkDefThrptClassOutMsk.setStatus("deprecated")


class _XX25LinkFlowCtrlNeg_Type(Integer32):
    """Custom type xX25LinkFlowCtrlNeg based on Integer32"""
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


_XX25LinkFlowCtrlNeg_Type.__name__ = "Integer32"
_XX25LinkFlowCtrlNeg_Object = MibTableColumn
xX25LinkFlowCtrlNeg = _XX25LinkFlowCtrlNeg_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 13),
    _XX25LinkFlowCtrlNeg_Type()
)
xX25LinkFlowCtrlNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkFlowCtrlNeg.setStatus("mandatory")


class _XX25LinkThrptClassNeg_Type(Integer32):
    """Custom type xX25LinkThrptClassNeg based on Integer32"""
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


_XX25LinkThrptClassNeg_Type.__name__ = "Integer32"
_XX25LinkThrptClassNeg_Object = MibTableColumn
xX25LinkThrptClassNeg = _XX25LinkThrptClassNeg_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 14),
    _XX25LinkThrptClassNeg_Type()
)
xX25LinkThrptClassNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkThrptClassNeg.setStatus("mandatory")


class _XX25LinkICallBarred_Type(Integer32):
    """Custom type xX25LinkICallBarred based on Integer32"""
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


_XX25LinkICallBarred_Type.__name__ = "Integer32"
_XX25LinkICallBarred_Object = MibTableColumn
xX25LinkICallBarred = _XX25LinkICallBarred_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 15),
    _XX25LinkICallBarred_Type()
)
xX25LinkICallBarred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkICallBarred.setStatus("mandatory")


class _XX25LinkOCallBarred_Type(Integer32):
    """Custom type xX25LinkOCallBarred based on Integer32"""
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


_XX25LinkOCallBarred_Type.__name__ = "Integer32"
_XX25LinkOCallBarred_Object = MibTableColumn
xX25LinkOCallBarred = _XX25LinkOCallBarred_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 16),
    _XX25LinkOCallBarred_Type()
)
xX25LinkOCallBarred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkOCallBarred.setStatus("mandatory")


class _XX25LinkOneOut_Type(Integer32):
    """Custom type xX25LinkOneOut based on Integer32"""
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


_XX25LinkOneOut_Type.__name__ = "Integer32"
_XX25LinkOneOut_Object = MibTableColumn
xX25LinkOneOut = _XX25LinkOneOut_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 17),
    _XX25LinkOneOut_Type()
)
xX25LinkOneOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkOneOut.setStatus("mandatory")


class _XX25LinkOneIn_Type(Integer32):
    """Custom type xX25LinkOneIn based on Integer32"""
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


_XX25LinkOneIn_Type.__name__ = "Integer32"
_XX25LinkOneIn_Object = MibTableColumn
xX25LinkOneIn = _XX25LinkOneIn_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 18),
    _XX25LinkOneIn_Type()
)
xX25LinkOneIn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkOneIn.setStatus("mandatory")


class _XX25LinkRevChargeAcc_Type(Integer32):
    """Custom type xX25LinkRevChargeAcc based on Integer32"""
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


_XX25LinkRevChargeAcc_Type.__name__ = "Integer32"
_XX25LinkRevChargeAcc_Object = MibTableColumn
xX25LinkRevChargeAcc = _XX25LinkRevChargeAcc_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 19),
    _XX25LinkRevChargeAcc_Type()
)
xX25LinkRevChargeAcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkRevChargeAcc.setStatus("mandatory")


class _XX25LinkLocalChargePrevent_Type(Integer32):
    """Custom type xX25LinkLocalChargePrevent based on Integer32"""
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


_XX25LinkLocalChargePrevent_Type.__name__ = "Integer32"
_XX25LinkLocalChargePrevent_Object = MibTableColumn
xX25LinkLocalChargePrevent = _XX25LinkLocalChargePrevent_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 20),
    _XX25LinkLocalChargePrevent_Type()
)
xX25LinkLocalChargePrevent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkLocalChargePrevent.setStatus("mandatory")


class _XX25LinkRpoa_Type(Integer32):
    """Custom type xX25LinkRpoa based on Integer32"""
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


_XX25LinkRpoa_Type.__name__ = "Integer32"
_XX25LinkRpoa_Object = MibTableColumn
xX25LinkRpoa = _XX25LinkRpoa_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 21),
    _XX25LinkRpoa_Type()
)
xX25LinkRpoa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkRpoa.setStatus("mandatory")


class _XX25LinkNui_Type(Integer32):
    """Custom type xX25LinkNui based on Integer32"""
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


_XX25LinkNui_Type.__name__ = "Integer32"
_XX25LinkNui_Object = MibTableColumn
xX25LinkNui = _XX25LinkNui_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 22),
    _XX25LinkNui_Type()
)
xX25LinkNui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkNui.setStatus("mandatory")


class _XX25LinkMaxPacketSize_Type(Integer32):
    """Custom type xX25LinkMaxPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              64,
              128,
              256,
              512,
              1024)
        )
    )
    namedValues = NamedValues(
        *(("bytes1024", 1024),
          ("bytes128", 128),
          ("bytes16", 16),
          ("bytes256", 256),
          ("bytes32", 32),
          ("bytes512", 512),
          ("bytes64", 64))
    )


_XX25LinkMaxPacketSize_Type.__name__ = "Integer32"
_XX25LinkMaxPacketSize_Object = MibTableColumn
xX25LinkMaxPacketSize = _XX25LinkMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 23),
    _XX25LinkMaxPacketSize_Type()
)
xX25LinkMaxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkMaxPacketSize.setStatus("mandatory")


class _XX25LinkInsertCallingAddr_Type(Integer32):
    """Custom type xX25LinkInsertCallingAddr based on Integer32"""
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


_XX25LinkInsertCallingAddr_Type.__name__ = "Integer32"
_XX25LinkInsertCallingAddr_Object = MibTableColumn
xX25LinkInsertCallingAddr = _XX25LinkInsertCallingAddr_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 24),
    _XX25LinkInsertCallingAddr_Type()
)
xX25LinkInsertCallingAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkInsertCallingAddr.setStatus("mandatory")
_XX25LinkDefaultInterface_Type = Integer32
_XX25LinkDefaultInterface_Object = MibTableColumn
xX25LinkDefaultInterface = _XX25LinkDefaultInterface_Object(
    (1, 3, 6, 1, 4, 1, 33, 20, 7, 1, 25),
    _XX25LinkDefaultInterface_Type()
)
xX25LinkDefaultInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xX25LinkDefaultInterface.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-X25-MIB",
    **{"xX25": xX25,
       "xX25ChannelTable": xX25ChannelTable,
       "xX25ChannelEntry": xX25ChannelEntry,
       "xX25ChannelIndex": xX25ChannelIndex,
       "xX25ChannelLowPVC": xX25ChannelLowPVC,
       "xX25ChannelHighPVC": xX25ChannelHighPVC,
       "xX25ChannelNetwork": xX25ChannelNetwork,
       "xX25ChannelMaxPrecedence": xX25ChannelMaxPrecedence,
       "xX25ChannelStdVersion": xX25ChannelStdVersion,
       "xX25VcCfgTable": xX25VcCfgTable,
       "xX25VcCfgEntry": xX25VcCfgEntry,
       "xX25VcCfgIndex": xX25VcCfgIndex,
       "xX25VcCfgPartnerAddr": xX25VcCfgPartnerAddr,
       "xX25VcCfgInterfaceIndex": xX25VcCfgInterfaceIndex,
       "xX25VcCfgLinkIndex": xX25VcCfgLinkIndex,
       "xX25VcCfgProtocol": xX25VcCfgProtocol,
       "xX25VcCfgEncapsulation": xX25VcCfgEncapsulation,
       "xX25VcCfgPvc": xX25VcCfgPvc,
       "xX25VcCfgPartnerIpAddress": xX25VcCfgPartnerIpAddress,
       "xX25VcCfgClearFacilities": xX25VcCfgClearFacilities,
       "xX25VcCfgStatus": xX25VcCfgStatus,
       "xX25LinkTable": xX25LinkTable,
       "xX25LinkEntry": xX25LinkEntry,
       "xX25LinkIndex": xX25LinkIndex,
       "xX25LinkRRDelay": xX25LinkRRDelay,
       "xX25LinkIdleTimeout": xX25LinkIdleTimeout,
       "xX25LinkHoldDownTimer": xX25LinkHoldDownTimer,
       "xX25LinkAccUncfgCalls": xX25LinkAccUncfgCalls,
       "xX25LinkDefWindSize": xX25LinkDefWindSize,
       "xX25LinkMaxWindSize": xX25LinkMaxWindSize,
       "xX25LinkDefPktSize": xX25LinkDefPktSize,
       "xX25LinkDefThrptClassIn": xX25LinkDefThrptClassIn,
       "xX25LinkDefThrptClassOut": xX25LinkDefThrptClassOut,
       "xX25LinkDefThrptClassInMsk": xX25LinkDefThrptClassInMsk,
       "xX25LinkDefThrptClassOutMsk": xX25LinkDefThrptClassOutMsk,
       "xX25LinkFlowCtrlNeg": xX25LinkFlowCtrlNeg,
       "xX25LinkThrptClassNeg": xX25LinkThrptClassNeg,
       "xX25LinkICallBarred": xX25LinkICallBarred,
       "xX25LinkOCallBarred": xX25LinkOCallBarred,
       "xX25LinkOneOut": xX25LinkOneOut,
       "xX25LinkOneIn": xX25LinkOneIn,
       "xX25LinkRevChargeAcc": xX25LinkRevChargeAcc,
       "xX25LinkLocalChargePrevent": xX25LinkLocalChargePrevent,
       "xX25LinkRpoa": xX25LinkRpoa,
       "xX25LinkNui": xX25LinkNui,
       "xX25LinkMaxPacketSize": xX25LinkMaxPacketSize,
       "xX25LinkInsertCallingAddr": xX25LinkInsertCallingAddr,
       "xX25LinkDefaultInterface": xX25LinkDefaultInterface}
)
