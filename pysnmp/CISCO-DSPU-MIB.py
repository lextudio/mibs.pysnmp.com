# SNMP MIB module (CISCO-DSPU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DSPU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:11 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoDspuMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24)
)
ciscoDspuMIB.setRevisions(
        ("1995-12-18 00:00",
         "1995-08-15 00:00",
         "1995-01-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DspuObjects_ObjectIdentity = ObjectIdentity
dspuObjects = _DspuObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1)
)
_DspuNode_ObjectIdentity = ObjectIdentity
dspuNode = _DspuNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1)
)


class _DspuNodeRsrb_Type(TruthValue):
    """Custom type dspuNodeRsrb based on TruthValue"""


_DspuNodeRsrb_Object = MibScalar
dspuNodeRsrb = _DspuNodeRsrb_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 1),
    _DspuNodeRsrb_Type()
)
dspuNodeRsrb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspuNodeRsrb.setStatus("current")


class _DspuNodeRsrbLocalVirtualRing_Type(Integer32):
    """Custom type dspuNodeRsrbLocalVirtualRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_DspuNodeRsrbLocalVirtualRing_Type.__name__ = "Integer32"
_DspuNodeRsrbLocalVirtualRing_Object = MibScalar
dspuNodeRsrbLocalVirtualRing = _DspuNodeRsrbLocalVirtualRing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 2),
    _DspuNodeRsrbLocalVirtualRing_Type()
)
dspuNodeRsrbLocalVirtualRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspuNodeRsrbLocalVirtualRing.setStatus("current")


class _DspuNodeRsrbBridgeNumber_Type(Integer32):
    """Custom type dspuNodeRsrbBridgeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DspuNodeRsrbBridgeNumber_Type.__name__ = "Integer32"
_DspuNodeRsrbBridgeNumber_Object = MibScalar
dspuNodeRsrbBridgeNumber = _DspuNodeRsrbBridgeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 3),
    _DspuNodeRsrbBridgeNumber_Type()
)
dspuNodeRsrbBridgeNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspuNodeRsrbBridgeNumber.setStatus("current")


class _DspuNodeRsrbTargetVirtualRing_Type(Integer32):
    """Custom type dspuNodeRsrbTargetVirtualRing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_DspuNodeRsrbTargetVirtualRing_Type.__name__ = "Integer32"
_DspuNodeRsrbTargetVirtualRing_Object = MibScalar
dspuNodeRsrbTargetVirtualRing = _DspuNodeRsrbTargetVirtualRing_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 4),
    _DspuNodeRsrbTargetVirtualRing_Type()
)
dspuNodeRsrbTargetVirtualRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspuNodeRsrbTargetVirtualRing.setStatus("current")
_DspuNodeRsrbVirtualMacAddress_Type = MacAddress
_DspuNodeRsrbVirtualMacAddress_Object = MibScalar
dspuNodeRsrbVirtualMacAddress = _DspuNodeRsrbVirtualMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 5),
    _DspuNodeRsrbVirtualMacAddress_Type()
)
dspuNodeRsrbVirtualMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspuNodeRsrbVirtualMacAddress.setStatus("current")


class _DspuNodeDefaultPu_Type(TruthValue):
    """Custom type dspuNodeDefaultPu based on TruthValue"""


_DspuNodeDefaultPu_Object = MibScalar
dspuNodeDefaultPu = _DspuNodeDefaultPu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 6),
    _DspuNodeDefaultPu_Type()
)
dspuNodeDefaultPu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspuNodeDefaultPu.setStatus("current")


class _DspuNodeDefaultPuWindowSize_Type(Integer32):
    """Custom type dspuNodeDefaultPuWindowSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_DspuNodeDefaultPuWindowSize_Type.__name__ = "Integer32"
_DspuNodeDefaultPuWindowSize_Object = MibScalar
dspuNodeDefaultPuWindowSize = _DspuNodeDefaultPuWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 7),
    _DspuNodeDefaultPuWindowSize_Type()
)
dspuNodeDefaultPuWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspuNodeDefaultPuWindowSize.setStatus("current")


class _DspuNodeDefaultPuMaxIframe_Type(Integer32):
    """Custom type dspuNodeDefaultPuMaxIframe based on Integer32"""
    defaultValue = 1472

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 18432),
    )


_DspuNodeDefaultPuMaxIframe_Type.__name__ = "Integer32"
_DspuNodeDefaultPuMaxIframe_Object = MibScalar
dspuNodeDefaultPuMaxIframe = _DspuNodeDefaultPuMaxIframe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 8),
    _DspuNodeDefaultPuMaxIframe_Type()
)
dspuNodeDefaultPuMaxIframe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspuNodeDefaultPuMaxIframe.setStatus("current")


class _DspuNodeActivationWindow_Type(Integer32):
    """Custom type dspuNodeActivationWindow based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DspuNodeActivationWindow_Type.__name__ = "Integer32"
_DspuNodeActivationWindow_Object = MibScalar
dspuNodeActivationWindow = _DspuNodeActivationWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 9),
    _DspuNodeActivationWindow_Type()
)
dspuNodeActivationWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspuNodeActivationWindow.setStatus("current")
_DspuNodeLastConfigChgTime_Type = TimeStamp
_DspuNodeLastConfigChgTime_Object = MibScalar
dspuNodeLastConfigChgTime = _DspuNodeLastConfigChgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 1, 10),
    _DspuNodeLastConfigChgTime_Type()
)
dspuNodeLastConfigChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuNodeLastConfigChgTime.setStatus("current")
_DspuPoolClass_ObjectIdentity = ObjectIdentity
dspuPoolClass = _DspuPoolClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2)
)
_DspuPoolClassTable_Object = MibTable
dspuPoolClassTable = _DspuPoolClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dspuPoolClassTable.setStatus("current")
_DspuPoolClassEntry_Object = MibTableRow
dspuPoolClassEntry = _DspuPoolClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1)
)
dspuPoolClassEntry.setIndexNames(
    (0, "CISCO-DSPU-MIB", "dspuPoolClassIndex"),
)
if mibBuilder.loadTexts:
    dspuPoolClassEntry.setStatus("current")


class _DspuPoolClassIndex_Type(Integer32):
    """Custom type dspuPoolClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DspuPoolClassIndex_Type.__name__ = "Integer32"
_DspuPoolClassIndex_Object = MibTableColumn
dspuPoolClassIndex = _DspuPoolClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1, 1),
    _DspuPoolClassIndex_Type()
)
dspuPoolClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dspuPoolClassIndex.setStatus("current")


class _DspuPoolClassName_Type(DisplayString):
    """Custom type dspuPoolClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DspuPoolClassName_Type.__name__ = "DisplayString"
_DspuPoolClassName_Object = MibTableColumn
dspuPoolClassName = _DspuPoolClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1, 2),
    _DspuPoolClassName_Type()
)
dspuPoolClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspuPoolClassName.setStatus("current")


class _DspuPoolClassInactivityTimeout_Type(Integer32):
    """Custom type dspuPoolClassInactivityTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DspuPoolClassInactivityTimeout_Type.__name__ = "Integer32"
_DspuPoolClassInactivityTimeout_Object = MibTableColumn
dspuPoolClassInactivityTimeout = _DspuPoolClassInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1, 3),
    _DspuPoolClassInactivityTimeout_Type()
)
dspuPoolClassInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dspuPoolClassInactivityTimeout.setStatus("current")
_DspuPoolClassOperUpStreamLuDefs_Type = Integer32
_DspuPoolClassOperUpStreamLuDefs_Object = MibTableColumn
dspuPoolClassOperUpStreamLuDefs = _DspuPoolClassOperUpStreamLuDefs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1, 4),
    _DspuPoolClassOperUpStreamLuDefs_Type()
)
dspuPoolClassOperUpStreamLuDefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPoolClassOperUpStreamLuDefs.setStatus("current")
_DspuPoolClassOperDnStreamLuDefs_Type = Integer32
_DspuPoolClassOperDnStreamLuDefs_Object = MibTableColumn
dspuPoolClassOperDnStreamLuDefs = _DspuPoolClassOperDnStreamLuDefs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 2, 1, 1, 5),
    _DspuPoolClassOperDnStreamLuDefs_Type()
)
dspuPoolClassOperDnStreamLuDefs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPoolClassOperDnStreamLuDefs.setStatus("current")
_DspuPooledLu_ObjectIdentity = ObjectIdentity
dspuPooledLu = _DspuPooledLu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 3)
)
_DspuPooledLuTable_Object = MibTable
dspuPooledLuTable = _DspuPooledLuTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dspuPooledLuTable.setStatus("current")
_DspuPooledLuEntry_Object = MibTableRow
dspuPooledLuEntry = _DspuPooledLuEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 3, 1, 1)
)
dspuPooledLuEntry.setIndexNames(
    (0, "CISCO-DSPU-MIB", "dspuPoolClassIndex"),
    (0, "CISCO-DSPU-MIB", "dspuPuOperIndex"),
    (0, "CISCO-DSPU-MIB", "dspuLuOperLuLocalAddress"),
)
if mibBuilder.loadTexts:
    dspuPooledLuEntry.setStatus("current")
_DspuPooledLuPeerPuIndex_Type = Integer32
_DspuPooledLuPeerPuIndex_Object = MibTableColumn
dspuPooledLuPeerPuIndex = _DspuPooledLuPeerPuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 3, 1, 1, 1),
    _DspuPooledLuPeerPuIndex_Type()
)
dspuPooledLuPeerPuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPooledLuPeerPuIndex.setStatus("current")


class _DspuPooledLuPeerLuLocalAddress_Type(Integer32):
    """Custom type dspuPooledLuPeerLuLocalAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_DspuPooledLuPeerLuLocalAddress_Type.__name__ = "Integer32"
_DspuPooledLuPeerLuLocalAddress_Object = MibTableColumn
dspuPooledLuPeerLuLocalAddress = _DspuPooledLuPeerLuLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 3, 1, 1, 2),
    _DspuPooledLuPeerLuLocalAddress_Type()
)
dspuPooledLuPeerLuLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPooledLuPeerLuLocalAddress.setStatus("current")
_DspuPu_ObjectIdentity = ObjectIdentity
dspuPu = _DspuPu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4)
)
_DspuPuAdminTable_Object = MibTable
dspuPuAdminTable = _DspuPuAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dspuPuAdminTable.setStatus("current")
_DspuPuAdminEntry_Object = MibTableRow
dspuPuAdminEntry = _DspuPuAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1)
)
dspuPuAdminEntry.setIndexNames(
    (0, "CISCO-DSPU-MIB", "dspuPuAdminIndex"),
)
if mibBuilder.loadTexts:
    dspuPuAdminEntry.setStatus("current")


class _DspuPuAdminIndex_Type(Integer32):
    """Custom type dspuPuAdminIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DspuPuAdminIndex_Type.__name__ = "Integer32"
_DspuPuAdminIndex_Object = MibTableColumn
dspuPuAdminIndex = _DspuPuAdminIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 1),
    _DspuPuAdminIndex_Type()
)
dspuPuAdminIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dspuPuAdminIndex.setStatus("current")


class _DspuPuAdminName_Type(DisplayString):
    """Custom type dspuPuAdminName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DspuPuAdminName_Type.__name__ = "DisplayString"
_DspuPuAdminName_Object = MibTableColumn
dspuPuAdminName = _DspuPuAdminName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 2),
    _DspuPuAdminName_Type()
)
dspuPuAdminName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminName.setStatus("current")


class _DspuPuAdminType_Type(Integer32):
    """Custom type dspuPuAdminType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dnstreamPu", 2),
          ("upstreamPu", 1))
    )


_DspuPuAdminType_Type.__name__ = "Integer32"
_DspuPuAdminType_Object = MibTableColumn
dspuPuAdminType = _DspuPuAdminType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 3),
    _DspuPuAdminType_Type()
)
dspuPuAdminType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminType.setStatus("current")
_DspuPuAdminRemoteMacAddress_Type = MacAddress
_DspuPuAdminRemoteMacAddress_Object = MibTableColumn
dspuPuAdminRemoteMacAddress = _DspuPuAdminRemoteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 4),
    _DspuPuAdminRemoteMacAddress_Type()
)
dspuPuAdminRemoteMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminRemoteMacAddress.setStatus("current")


class _DspuPuAdminRemoteSapAddress_Type(Integer32):
    """Custom type dspuPuAdminRemoteSapAddress based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DspuPuAdminRemoteSapAddress_Type.__name__ = "Integer32"
_DspuPuAdminRemoteSapAddress_Object = MibTableColumn
dspuPuAdminRemoteSapAddress = _DspuPuAdminRemoteSapAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 5),
    _DspuPuAdminRemoteSapAddress_Type()
)
dspuPuAdminRemoteSapAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminRemoteSapAddress.setStatus("current")


class _DspuPuAdminLocalSapAddress_Type(Integer32):
    """Custom type dspuPuAdminLocalSapAddress based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DspuPuAdminLocalSapAddress_Type.__name__ = "Integer32"
_DspuPuAdminLocalSapAddress_Object = MibTableColumn
dspuPuAdminLocalSapAddress = _DspuPuAdminLocalSapAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 6),
    _DspuPuAdminLocalSapAddress_Type()
)
dspuPuAdminLocalSapAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminLocalSapAddress.setStatus("current")
_DspuPuAdminXid_Type = Integer32
_DspuPuAdminXid_Object = MibTableColumn
dspuPuAdminXid = _DspuPuAdminXid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 7),
    _DspuPuAdminXid_Type()
)
dspuPuAdminXid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminXid.setStatus("current")


class _DspuPuAdminXidFmt_Type(Integer32):
    """Custom type dspuPuAdminXidFmt based on Integer32"""
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
        *(("format0", 2),
          ("format3", 3),
          ("formatUnknown", 1))
    )


_DspuPuAdminXidFmt_Type.__name__ = "Integer32"
_DspuPuAdminXidFmt_Object = MibTableColumn
dspuPuAdminXidFmt = _DspuPuAdminXidFmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 8),
    _DspuPuAdminXidFmt_Type()
)
dspuPuAdminXidFmt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminXidFmt.setStatus("current")


class _DspuPuAdminWindowSize_Type(Integer32):
    """Custom type dspuPuAdminWindowSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_DspuPuAdminWindowSize_Type.__name__ = "Integer32"
_DspuPuAdminWindowSize_Object = MibTableColumn
dspuPuAdminWindowSize = _DspuPuAdminWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 9),
    _DspuPuAdminWindowSize_Type()
)
dspuPuAdminWindowSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminWindowSize.setStatus("current")


class _DspuPuAdminMaxIframe_Type(Integer32):
    """Custom type dspuPuAdminMaxIframe based on Integer32"""
    defaultValue = 1472

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 18432),
    )


_DspuPuAdminMaxIframe_Type.__name__ = "Integer32"
_DspuPuAdminMaxIframe_Object = MibTableColumn
dspuPuAdminMaxIframe = _DspuPuAdminMaxIframe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 10),
    _DspuPuAdminMaxIframe_Type()
)
dspuPuAdminMaxIframe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminMaxIframe.setStatus("current")


class _DspuPuAdminLinkRetryCount_Type(Integer32):
    """Custom type dspuPuAdminLinkRetryCount based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DspuPuAdminLinkRetryCount_Type.__name__ = "Integer32"
_DspuPuAdminLinkRetryCount_Object = MibTableColumn
dspuPuAdminLinkRetryCount = _DspuPuAdminLinkRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 11),
    _DspuPuAdminLinkRetryCount_Type()
)
dspuPuAdminLinkRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminLinkRetryCount.setStatus("current")


class _DspuPuAdminLinkRetryTimeout_Type(Integer32):
    """Custom type dspuPuAdminLinkRetryTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_DspuPuAdminLinkRetryTimeout_Type.__name__ = "Integer32"
_DspuPuAdminLinkRetryTimeout_Object = MibTableColumn
dspuPuAdminLinkRetryTimeout = _DspuPuAdminLinkRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 12),
    _DspuPuAdminLinkRetryTimeout_Type()
)
dspuPuAdminLinkRetryTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminLinkRetryTimeout.setStatus("current")


class _DspuPuAdminStartPu_Type(TruthValue):
    """Custom type dspuPuAdminStartPu based on TruthValue"""


_DspuPuAdminStartPu_Object = MibTableColumn
dspuPuAdminStartPu = _DspuPuAdminStartPu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 13),
    _DspuPuAdminStartPu_Type()
)
dspuPuAdminStartPu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminStartPu.setStatus("current")


class _DspuPuAdminDlcType_Type(Integer32):
    """Custom type dspuPuAdminDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 5),
          ("fddi", 10),
          ("framerelay", 9),
          ("qllc", 11),
          ("rsrb", 8),
          ("sdlc", 2),
          ("tokenRing", 6),
          ("undefined", 1))
    )


_DspuPuAdminDlcType_Type.__name__ = "Integer32"
_DspuPuAdminDlcType_Object = MibTableColumn
dspuPuAdminDlcType = _DspuPuAdminDlcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 14),
    _DspuPuAdminDlcType_Type()
)
dspuPuAdminDlcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminDlcType.setStatus("current")


class _DspuPuAdminDlcUnit_Type(Integer32):
    """Custom type dspuPuAdminDlcUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DspuPuAdminDlcUnit_Type.__name__ = "Integer32"
_DspuPuAdminDlcUnit_Object = MibTableColumn
dspuPuAdminDlcUnit = _DspuPuAdminDlcUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 15),
    _DspuPuAdminDlcUnit_Type()
)
dspuPuAdminDlcUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminDlcUnit.setStatus("current")


class _DspuPuAdminDlcPort_Type(Integer32):
    """Custom type dspuPuAdminDlcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DspuPuAdminDlcPort_Type.__name__ = "Integer32"
_DspuPuAdminDlcPort_Object = MibTableColumn
dspuPuAdminDlcPort = _DspuPuAdminDlcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 16),
    _DspuPuAdminDlcPort_Type()
)
dspuPuAdminDlcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminDlcPort.setStatus("current")


class _DspuPuAdminFocalPoint_Type(TruthValue):
    """Custom type dspuPuAdminFocalPoint based on TruthValue"""


_DspuPuAdminFocalPoint_Object = MibTableColumn
dspuPuAdminFocalPoint = _DspuPuAdminFocalPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 17),
    _DspuPuAdminFocalPoint_Type()
)
dspuPuAdminFocalPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminFocalPoint.setStatus("current")
_DspuPuAdminRowStatus_Type = RowStatus
_DspuPuAdminRowStatus_Object = MibTableColumn
dspuPuAdminRowStatus = _DspuPuAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 18),
    _DspuPuAdminRowStatus_Type()
)
dspuPuAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminRowStatus.setStatus("current")


class _DspuPuAdminRemoteAddress_Type(DisplayString):
    """Custom type dspuPuAdminRemoteAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DspuPuAdminRemoteAddress_Type.__name__ = "DisplayString"
_DspuPuAdminRemoteAddress_Object = MibTableColumn
dspuPuAdminRemoteAddress = _DspuPuAdminRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 1, 1, 19),
    _DspuPuAdminRemoteAddress_Type()
)
dspuPuAdminRemoteAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuPuAdminRemoteAddress.setStatus("current")
_DspuPuOperTable_Object = MibTable
dspuPuOperTable = _DspuPuOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dspuPuOperTable.setStatus("current")
_DspuPuOperEntry_Object = MibTableRow
dspuPuOperEntry = _DspuPuOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1)
)
dspuPuOperEntry.setIndexNames(
    (0, "CISCO-DSPU-MIB", "dspuPuOperIndex"),
)
if mibBuilder.loadTexts:
    dspuPuOperEntry.setStatus("current")


class _DspuPuOperIndex_Type(Integer32):
    """Custom type dspuPuOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DspuPuOperIndex_Type.__name__ = "Integer32"
_DspuPuOperIndex_Object = MibTableColumn
dspuPuOperIndex = _DspuPuOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 1),
    _DspuPuOperIndex_Type()
)
dspuPuOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dspuPuOperIndex.setStatus("current")


class _DspuPuOperName_Type(DisplayString):
    """Custom type dspuPuOperName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DspuPuOperName_Type.__name__ = "DisplayString"
_DspuPuOperName_Object = MibTableColumn
dspuPuOperName = _DspuPuOperName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 2),
    _DspuPuOperName_Type()
)
dspuPuOperName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperName.setStatus("current")


class _DspuPuOperType_Type(Integer32):
    """Custom type dspuPuOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dnstreamPu", 2),
          ("upstreamPu", 1))
    )


_DspuPuOperType_Type.__name__ = "Integer32"
_DspuPuOperType_Object = MibTableColumn
dspuPuOperType = _DspuPuOperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 3),
    _DspuPuOperType_Type()
)
dspuPuOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperType.setStatus("current")
_DspuPuOperRemoteMacAddress_Type = MacAddress
_DspuPuOperRemoteMacAddress_Object = MibTableColumn
dspuPuOperRemoteMacAddress = _DspuPuOperRemoteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 4),
    _DspuPuOperRemoteMacAddress_Type()
)
dspuPuOperRemoteMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperRemoteMacAddress.setStatus("current")


class _DspuPuOperRemoteSapAddress_Type(Integer32):
    """Custom type dspuPuOperRemoteSapAddress based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DspuPuOperRemoteSapAddress_Type.__name__ = "Integer32"
_DspuPuOperRemoteSapAddress_Object = MibTableColumn
dspuPuOperRemoteSapAddress = _DspuPuOperRemoteSapAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 5),
    _DspuPuOperRemoteSapAddress_Type()
)
dspuPuOperRemoteSapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperRemoteSapAddress.setStatus("current")


class _DspuPuOperLocalSapAddress_Type(Integer32):
    """Custom type dspuPuOperLocalSapAddress based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DspuPuOperLocalSapAddress_Type.__name__ = "Integer32"
_DspuPuOperLocalSapAddress_Object = MibTableColumn
dspuPuOperLocalSapAddress = _DspuPuOperLocalSapAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 6),
    _DspuPuOperLocalSapAddress_Type()
)
dspuPuOperLocalSapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperLocalSapAddress.setStatus("current")
_DspuPuOperXid_Type = Integer32
_DspuPuOperXid_Object = MibTableColumn
dspuPuOperXid = _DspuPuOperXid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 7),
    _DspuPuOperXid_Type()
)
dspuPuOperXid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperXid.setStatus("current")


class _DspuPuOperXidFmt_Type(Integer32):
    """Custom type dspuPuOperXidFmt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("format0", 2),
          ("format3", 3),
          ("formatUnknown", 1))
    )


_DspuPuOperXidFmt_Type.__name__ = "Integer32"
_DspuPuOperXidFmt_Object = MibTableColumn
dspuPuOperXidFmt = _DspuPuOperXidFmt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 8),
    _DspuPuOperXidFmt_Type()
)
dspuPuOperXidFmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperXidFmt.setStatus("current")


class _DspuPuOperWindowSize_Type(Integer32):
    """Custom type dspuPuOperWindowSize based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_DspuPuOperWindowSize_Type.__name__ = "Integer32"
_DspuPuOperWindowSize_Object = MibTableColumn
dspuPuOperWindowSize = _DspuPuOperWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 9),
    _DspuPuOperWindowSize_Type()
)
dspuPuOperWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperWindowSize.setStatus("current")


class _DspuPuOperMaxIframe_Type(Integer32):
    """Custom type dspuPuOperMaxIframe based on Integer32"""
    defaultValue = 1472

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 18432),
    )


_DspuPuOperMaxIframe_Type.__name__ = "Integer32"
_DspuPuOperMaxIframe_Object = MibTableColumn
dspuPuOperMaxIframe = _DspuPuOperMaxIframe_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 10),
    _DspuPuOperMaxIframe_Type()
)
dspuPuOperMaxIframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperMaxIframe.setStatus("current")


class _DspuPuOperLinkRetryCount_Type(Integer32):
    """Custom type dspuPuOperLinkRetryCount based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DspuPuOperLinkRetryCount_Type.__name__ = "Integer32"
_DspuPuOperLinkRetryCount_Object = MibTableColumn
dspuPuOperLinkRetryCount = _DspuPuOperLinkRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 11),
    _DspuPuOperLinkRetryCount_Type()
)
dspuPuOperLinkRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperLinkRetryCount.setStatus("current")


class _DspuPuOperLinkRetryTimeout_Type(Integer32):
    """Custom type dspuPuOperLinkRetryTimeout based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_DspuPuOperLinkRetryTimeout_Type.__name__ = "Integer32"
_DspuPuOperLinkRetryTimeout_Object = MibTableColumn
dspuPuOperLinkRetryTimeout = _DspuPuOperLinkRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 12),
    _DspuPuOperLinkRetryTimeout_Type()
)
dspuPuOperLinkRetryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperLinkRetryTimeout.setStatus("current")


class _DspuPuOperStartPu_Type(TruthValue):
    """Custom type dspuPuOperStartPu based on TruthValue"""


_DspuPuOperStartPu_Object = MibTableColumn
dspuPuOperStartPu = _DspuPuOperStartPu_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 13),
    _DspuPuOperStartPu_Type()
)
dspuPuOperStartPu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperStartPu.setStatus("current")


class _DspuPuOperDlcType_Type(Integer32):
    """Custom type dspuPuOperDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 5),
          ("fddi", 10),
          ("framerelay", 9),
          ("qllc", 11),
          ("rsrb", 8),
          ("sdlc", 2),
          ("tokenRing", 6),
          ("undefined", 1))
    )


_DspuPuOperDlcType_Type.__name__ = "Integer32"
_DspuPuOperDlcType_Object = MibTableColumn
dspuPuOperDlcType = _DspuPuOperDlcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 14),
    _DspuPuOperDlcType_Type()
)
dspuPuOperDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperDlcType.setStatus("current")


class _DspuPuOperDlcUnit_Type(Integer32):
    """Custom type dspuPuOperDlcUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DspuPuOperDlcUnit_Type.__name__ = "Integer32"
_DspuPuOperDlcUnit_Object = MibTableColumn
dspuPuOperDlcUnit = _DspuPuOperDlcUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 15),
    _DspuPuOperDlcUnit_Type()
)
dspuPuOperDlcUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperDlcUnit.setStatus("current")


class _DspuPuOperDlcPort_Type(Integer32):
    """Custom type dspuPuOperDlcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DspuPuOperDlcPort_Type.__name__ = "Integer32"
_DspuPuOperDlcPort_Object = MibTableColumn
dspuPuOperDlcPort = _DspuPuOperDlcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 16),
    _DspuPuOperDlcPort_Type()
)
dspuPuOperDlcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperDlcPort.setStatus("current")


class _DspuPuOperFocalPoint_Type(TruthValue):
    """Custom type dspuPuOperFocalPoint based on TruthValue"""


_DspuPuOperFocalPoint_Object = MibTableColumn
dspuPuOperFocalPoint = _DspuPuOperFocalPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 17),
    _DspuPuOperFocalPoint_Type()
)
dspuPuOperFocalPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperFocalPoint.setStatus("current")


class _DspuPuOperState_Type(Integer32):
    """Custom type dspuPuOperState based on Integer32"""
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


_DspuPuOperState_Type.__name__ = "Integer32"
_DspuPuOperState_Object = MibTableColumn
dspuPuOperState = _DspuPuOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 18),
    _DspuPuOperState_Type()
)
dspuPuOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperState.setStatus("current")


class _DspuPuOperFsmState_Type(Integer32):
    """Custom type dspuPuOperFsmState based on Integer32"""
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("linkConnIn", 7),
          ("linkConnOut", 6),
          ("linkConnected", 8),
          ("linkPendClose", 14),
          ("linkPendConnIn", 3),
          ("linkPendConnOut", 2),
          ("linkPendDisc", 13),
          ("linkPendXid", 4),
          ("linkReset", 1),
          ("linkXidNeg", 5),
          ("puActive", 10),
          ("puBusy", 11),
          ("puPendAct", 9),
          ("puPendInact", 12))
    )


_DspuPuOperFsmState_Type.__name__ = "Integer32"
_DspuPuOperFsmState_Object = MibTableColumn
dspuPuOperFsmState = _DspuPuOperFsmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 19),
    _DspuPuOperFsmState_Type()
)
dspuPuOperFsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperFsmState.setStatus("current")
_DspuPuOperStartTime_Type = TimeStamp
_DspuPuOperStartTime_Object = MibTableColumn
dspuPuOperStartTime = _DspuPuOperStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 20),
    _DspuPuOperStartTime_Type()
)
dspuPuOperStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperStartTime.setStatus("current")
_DspuPuOperLastStateChgTime_Type = TimeStamp
_DspuPuOperLastStateChgTime_Object = MibTableColumn
dspuPuOperLastStateChgTime = _DspuPuOperLastStateChgTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 21),
    _DspuPuOperLastStateChgTime_Type()
)
dspuPuOperLastStateChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperLastStateChgTime.setStatus("current")


class _DspuPuOperRemoteAddress_Type(DisplayString):
    """Custom type dspuPuOperRemoteAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_DspuPuOperRemoteAddress_Type.__name__ = "DisplayString"
_DspuPuOperRemoteAddress_Object = MibTableColumn
dspuPuOperRemoteAddress = _DspuPuOperRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 2, 1, 22),
    _DspuPuOperRemoteAddress_Type()
)
dspuPuOperRemoteAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuOperRemoteAddress.setStatus("current")
_DspuPuStatsTable_Object = MibTable
dspuPuStatsTable = _DspuPuStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dspuPuStatsTable.setStatus("current")
_DspuPuStatsEntry_Object = MibTableRow
dspuPuStatsEntry = _DspuPuStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1)
)
dspuPuStatsEntry.setIndexNames(
    (0, "CISCO-DSPU-MIB", "dspuPuOperIndex"),
)
if mibBuilder.loadTexts:
    dspuPuStatsEntry.setStatus("current")
_DspuPuStatsSentBytes_Type = Counter32
_DspuPuStatsSentBytes_Object = MibTableColumn
dspuPuStatsSentBytes = _DspuPuStatsSentBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 1),
    _DspuPuStatsSentBytes_Type()
)
dspuPuStatsSentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuStatsSentBytes.setStatus("current")
_DspuPuStatsRcvdBytes_Type = Counter32
_DspuPuStatsRcvdBytes_Object = MibTableColumn
dspuPuStatsRcvdBytes = _DspuPuStatsRcvdBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 2),
    _DspuPuStatsRcvdBytes_Type()
)
dspuPuStatsRcvdBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuStatsRcvdBytes.setStatus("current")
_DspuPuStatsSentFrames_Type = Counter32
_DspuPuStatsSentFrames_Object = MibTableColumn
dspuPuStatsSentFrames = _DspuPuStatsSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 3),
    _DspuPuStatsSentFrames_Type()
)
dspuPuStatsSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuStatsSentFrames.setStatus("current")
_DspuPuStatsRcvdFrames_Type = Counter32
_DspuPuStatsRcvdFrames_Object = MibTableColumn
dspuPuStatsRcvdFrames = _DspuPuStatsRcvdFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 4),
    _DspuPuStatsRcvdFrames_Type()
)
dspuPuStatsRcvdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuStatsRcvdFrames.setStatus("current")
_DspuPuStatsSentNegativeRsps_Type = Counter32
_DspuPuStatsSentNegativeRsps_Object = MibTableColumn
dspuPuStatsSentNegativeRsps = _DspuPuStatsSentNegativeRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 5),
    _DspuPuStatsSentNegativeRsps_Type()
)
dspuPuStatsSentNegativeRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuStatsSentNegativeRsps.setStatus("current")
_DspuPuStatsRcvdNegativeRsps_Type = Counter32
_DspuPuStatsRcvdNegativeRsps_Object = MibTableColumn
dspuPuStatsRcvdNegativeRsps = _DspuPuStatsRcvdNegativeRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 6),
    _DspuPuStatsRcvdNegativeRsps_Type()
)
dspuPuStatsRcvdNegativeRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuStatsRcvdNegativeRsps.setStatus("current")
_DspuPuStatsActiveLus_Type = Counter32
_DspuPuStatsActiveLus_Object = MibTableColumn
dspuPuStatsActiveLus = _DspuPuStatsActiveLus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 7),
    _DspuPuStatsActiveLus_Type()
)
dspuPuStatsActiveLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuStatsActiveLus.setStatus("current")
_DspuPuStatsInactiveLus_Type = Counter32
_DspuPuStatsInactiveLus_Object = MibTableColumn
dspuPuStatsInactiveLus = _DspuPuStatsInactiveLus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 8),
    _DspuPuStatsInactiveLus_Type()
)
dspuPuStatsInactiveLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuStatsInactiveLus.setStatus("current")
_DspuPuStatsBindLus_Type = Counter32
_DspuPuStatsBindLus_Object = MibTableColumn
dspuPuStatsBindLus = _DspuPuStatsBindLus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 9),
    _DspuPuStatsBindLus_Type()
)
dspuPuStatsBindLus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuStatsBindLus.setStatus("current")
_DspuPuStatsActivationFailures_Type = Counter32
_DspuPuStatsActivationFailures_Object = MibTableColumn
dspuPuStatsActivationFailures = _DspuPuStatsActivationFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 10),
    _DspuPuStatsActivationFailures_Type()
)
dspuPuStatsActivationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuStatsActivationFailures.setStatus("current")


class _DspuPuStatsLastActivationFailureReason_Type(Integer32):
    """Custom type dspuPuStatsLastActivationFailureReason based on Integer32"""
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
        *(("configurationError", 4),
          ("internalError", 3),
          ("noError", 1),
          ("otherError", 2),
          ("puAlreadyActive", 6),
          ("puNegativeResponse", 5))
    )


_DspuPuStatsLastActivationFailureReason_Type.__name__ = "Integer32"
_DspuPuStatsLastActivationFailureReason_Object = MibTableColumn
dspuPuStatsLastActivationFailureReason = _DspuPuStatsLastActivationFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 3, 1, 11),
    _DspuPuStatsLastActivationFailureReason_Type()
)
dspuPuStatsLastActivationFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuPuStatsLastActivationFailureReason.setStatus("current")
_DspuPuTraps_ObjectIdentity = ObjectIdentity
dspuPuTraps = _DspuPuTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4)
)
_DspuPuTrapsPrefix_ObjectIdentity = ObjectIdentity
dspuPuTrapsPrefix = _DspuPuTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4, 0)
)
_DspuLu_ObjectIdentity = ObjectIdentity
dspuLu = _DspuLu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5)
)
_DspuLuAdminTable_Object = MibTable
dspuLuAdminTable = _DspuLuAdminTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dspuLuAdminTable.setStatus("current")
_DspuLuAdminEntry_Object = MibTableRow
dspuLuAdminEntry = _DspuLuAdminEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1)
)
dspuLuAdminEntry.setIndexNames(
    (0, "CISCO-DSPU-MIB", "dspuPuAdminIndex"),
    (0, "CISCO-DSPU-MIB", "dspuLuAdminLuLocalAddress"),
)
if mibBuilder.loadTexts:
    dspuLuAdminEntry.setStatus("current")


class _DspuLuAdminLuLocalAddress_Type(Integer32):
    """Custom type dspuLuAdminLuLocalAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DspuLuAdminLuLocalAddress_Type.__name__ = "Integer32"
_DspuLuAdminLuLocalAddress_Object = MibTableColumn
dspuLuAdminLuLocalAddress = _DspuLuAdminLuLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 1),
    _DspuLuAdminLuLocalAddress_Type()
)
dspuLuAdminLuLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dspuLuAdminLuLocalAddress.setStatus("current")


class _DspuLuAdminType_Type(Integer32):
    """Custom type dspuLuAdminType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 2),
          ("pooled", 1))
    )


_DspuLuAdminType_Type.__name__ = "Integer32"
_DspuLuAdminType_Object = MibTableColumn
dspuLuAdminType = _DspuLuAdminType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 2),
    _DspuLuAdminType_Type()
)
dspuLuAdminType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuLuAdminType.setStatus("current")


class _DspuLuAdminPoolClassName_Type(DisplayString):
    """Custom type dspuLuAdminPoolClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DspuLuAdminPoolClassName_Type.__name__ = "DisplayString"
_DspuLuAdminPoolClassName_Object = MibTableColumn
dspuLuAdminPoolClassName = _DspuLuAdminPoolClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 3),
    _DspuLuAdminPoolClassName_Type()
)
dspuLuAdminPoolClassName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuLuAdminPoolClassName.setStatus("current")
_DspuLuAdminPeerPuIndex_Type = Integer32
_DspuLuAdminPeerPuIndex_Object = MibTableColumn
dspuLuAdminPeerPuIndex = _DspuLuAdminPeerPuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 4),
    _DspuLuAdminPeerPuIndex_Type()
)
dspuLuAdminPeerPuIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuLuAdminPeerPuIndex.setStatus("current")


class _DspuLuAdminPeerLuLocalAddress_Type(Integer32):
    """Custom type dspuLuAdminPeerLuLocalAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DspuLuAdminPeerLuLocalAddress_Type.__name__ = "Integer32"
_DspuLuAdminPeerLuLocalAddress_Object = MibTableColumn
dspuLuAdminPeerLuLocalAddress = _DspuLuAdminPeerLuLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 5),
    _DspuLuAdminPeerLuLocalAddress_Type()
)
dspuLuAdminPeerLuLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuLuAdminPeerLuLocalAddress.setStatus("current")
_DspuLuAdminRowStatus_Type = RowStatus
_DspuLuAdminRowStatus_Object = MibTableColumn
dspuLuAdminRowStatus = _DspuLuAdminRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 1, 1, 6),
    _DspuLuAdminRowStatus_Type()
)
dspuLuAdminRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuLuAdminRowStatus.setStatus("current")
_DspuLuOperTable_Object = MibTable
dspuLuOperTable = _DspuLuOperTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dspuLuOperTable.setStatus("current")
_DspuLuOperEntry_Object = MibTableRow
dspuLuOperEntry = _DspuLuOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1)
)
dspuLuOperEntry.setIndexNames(
    (0, "CISCO-DSPU-MIB", "dspuPuOperIndex"),
    (0, "CISCO-DSPU-MIB", "dspuLuOperLuLocalAddress"),
)
if mibBuilder.loadTexts:
    dspuLuOperEntry.setStatus("current")


class _DspuLuOperLuLocalAddress_Type(Integer32):
    """Custom type dspuLuOperLuLocalAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DspuLuOperLuLocalAddress_Type.__name__ = "Integer32"
_DspuLuOperLuLocalAddress_Object = MibTableColumn
dspuLuOperLuLocalAddress = _DspuLuOperLuLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 1),
    _DspuLuOperLuLocalAddress_Type()
)
dspuLuOperLuLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dspuLuOperLuLocalAddress.setStatus("current")


class _DspuLuOperType_Type(Integer32):
    """Custom type dspuLuOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 2),
          ("pooled", 1))
    )


_DspuLuOperType_Type.__name__ = "Integer32"
_DspuLuOperType_Object = MibTableColumn
dspuLuOperType = _DspuLuOperType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 2),
    _DspuLuOperType_Type()
)
dspuLuOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuLuOperType.setStatus("current")


class _DspuLuOperPoolClassName_Type(DisplayString):
    """Custom type dspuLuOperPoolClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DspuLuOperPoolClassName_Type.__name__ = "DisplayString"
_DspuLuOperPoolClassName_Object = MibTableColumn
dspuLuOperPoolClassName = _DspuLuOperPoolClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 3),
    _DspuLuOperPoolClassName_Type()
)
dspuLuOperPoolClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuLuOperPoolClassName.setStatus("current")
_DspuLuOperPeerPuIndex_Type = Integer32
_DspuLuOperPeerPuIndex_Object = MibTableColumn
dspuLuOperPeerPuIndex = _DspuLuOperPeerPuIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 4),
    _DspuLuOperPeerPuIndex_Type()
)
dspuLuOperPeerPuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuLuOperPeerPuIndex.setStatus("current")


class _DspuLuOperPeerLuLocalAddress_Type(Integer32):
    """Custom type dspuLuOperPeerLuLocalAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_DspuLuOperPeerLuLocalAddress_Type.__name__ = "Integer32"
_DspuLuOperPeerLuLocalAddress_Object = MibTableColumn
dspuLuOperPeerLuLocalAddress = _DspuLuOperPeerLuLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 5),
    _DspuLuOperPeerLuLocalAddress_Type()
)
dspuLuOperPeerLuLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuLuOperPeerLuLocalAddress.setStatus("current")


class _DspuLuOperState_Type(Integer32):
    """Custom type dspuLuOperState based on Integer32"""
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


_DspuLuOperState_Type.__name__ = "Integer32"
_DspuLuOperState_Object = MibTableColumn
dspuLuOperState = _DspuLuOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 6),
    _DspuLuOperState_Type()
)
dspuLuOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuLuOperState.setStatus("current")


class _DspuLuOperFsmState_Type(Integer32):
    """Custom type dspuLuOperFsmState based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("bothAvail", 7),
          ("dnInactivityPendInact", 11),
          ("dnLuActUnav", 5),
          ("dnLuPendAct", 4),
          ("dnLuPendInact", 8),
          ("dnLuStarted", 2),
          ("luInactivityTimeout", 10),
          ("reset", 1),
          ("upLuActive", 3),
          ("upLuPendAvail", 6),
          ("upLuPendInact", 9))
    )


_DspuLuOperFsmState_Type.__name__ = "Integer32"
_DspuLuOperFsmState_Object = MibTableColumn
dspuLuOperFsmState = _DspuLuOperFsmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 7),
    _DspuLuOperFsmState_Type()
)
dspuLuOperFsmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuLuOperFsmState.setStatus("current")


class _DspuLuOperSessionState_Type(Integer32):
    """Custom type dspuLuOperSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bound", 1),
          ("unbound", 2))
    )


_DspuLuOperSessionState_Type.__name__ = "Integer32"
_DspuLuOperSessionState_Object = MibTableColumn
dspuLuOperSessionState = _DspuLuOperSessionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 8),
    _DspuLuOperSessionState_Type()
)
dspuLuOperSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuLuOperSessionState.setStatus("current")


class _DspuLuOperLastActivationFailureReason_Type(Integer32):
    """Custom type dspuLuOperLastActivationFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("luNegativeResponse", 3),
          ("noError", 1),
          ("otherError", 2))
    )


_DspuLuOperLastActivationFailureReason_Type.__name__ = "Integer32"
_DspuLuOperLastActivationFailureReason_Object = MibTableColumn
dspuLuOperLastActivationFailureReason = _DspuLuOperLastActivationFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 2, 1, 9),
    _DspuLuOperLastActivationFailureReason_Type()
)
dspuLuOperLastActivationFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuLuOperLastActivationFailureReason.setStatus("current")
_DspuLuTraps_ObjectIdentity = ObjectIdentity
dspuLuTraps = _DspuLuTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 3)
)
_DspuLuTrapsPrefix_ObjectIdentity = ObjectIdentity
dspuLuTrapsPrefix = _DspuLuTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 3, 0)
)
_DspuSap_ObjectIdentity = ObjectIdentity
dspuSap = _DspuSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6)
)
_DspuSapTable_Object = MibTable
dspuSapTable = _DspuSapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dspuSapTable.setStatus("current")
_DspuSapEntry_Object = MibTableRow
dspuSapEntry = _DspuSapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1)
)
dspuSapEntry.setIndexNames(
    (0, "CISCO-DSPU-MIB", "dspuSapDlcType"),
    (0, "CISCO-DSPU-MIB", "dspuSapDlcUnit"),
    (0, "CISCO-DSPU-MIB", "dspuSapDlcPort"),
    (0, "CISCO-DSPU-MIB", "dspuSapAddress"),
)
if mibBuilder.loadTexts:
    dspuSapEntry.setStatus("current")


class _DspuSapAddress_Type(Integer32):
    """Custom type dspuSapAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_DspuSapAddress_Type.__name__ = "Integer32"
_DspuSapAddress_Object = MibTableColumn
dspuSapAddress = _DspuSapAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 1),
    _DspuSapAddress_Type()
)
dspuSapAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dspuSapAddress.setStatus("current")


class _DspuSapType_Type(Integer32):
    """Custom type dspuSapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dnstreamSap", 2),
          ("upstreamSap", 1))
    )


_DspuSapType_Type.__name__ = "Integer32"
_DspuSapType_Object = MibTableColumn
dspuSapType = _DspuSapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 2),
    _DspuSapType_Type()
)
dspuSapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuSapType.setStatus("current")


class _DspuSapDlcType_Type(Integer32):
    """Custom type dspuSapDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 5),
          ("fddi", 10),
          ("framerelay", 9),
          ("qllc", 11),
          ("rsrb", 8),
          ("sdlc", 2),
          ("tokenRing", 6),
          ("undefined", 1))
    )


_DspuSapDlcType_Type.__name__ = "Integer32"
_DspuSapDlcType_Object = MibTableColumn
dspuSapDlcType = _DspuSapDlcType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 3),
    _DspuSapDlcType_Type()
)
dspuSapDlcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dspuSapDlcType.setStatus("current")


class _DspuSapDlcUnit_Type(Integer32):
    """Custom type dspuSapDlcUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DspuSapDlcUnit_Type.__name__ = "Integer32"
_DspuSapDlcUnit_Object = MibTableColumn
dspuSapDlcUnit = _DspuSapDlcUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 4),
    _DspuSapDlcUnit_Type()
)
dspuSapDlcUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dspuSapDlcUnit.setStatus("current")


class _DspuSapDlcPort_Type(Integer32):
    """Custom type dspuSapDlcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DspuSapDlcPort_Type.__name__ = "Integer32"
_DspuSapDlcPort_Object = MibTableColumn
dspuSapDlcPort = _DspuSapDlcPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 5),
    _DspuSapDlcPort_Type()
)
dspuSapDlcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dspuSapDlcPort.setStatus("current")


class _DspuSapOperState_Type(Integer32):
    """Custom type dspuSapOperState based on Integer32"""
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
        *(("sapClosed", 1),
          ("sapClosing", 4),
          ("sapOpened", 3),
          ("sapOpening", 2))
    )


_DspuSapOperState_Type.__name__ = "Integer32"
_DspuSapOperState_Object = MibTableColumn
dspuSapOperState = _DspuSapOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 6),
    _DspuSapOperState_Type()
)
dspuSapOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dspuSapOperState.setStatus("current")
_DspuSapRowStatus_Type = RowStatus
_DspuSapRowStatus_Object = MibTableColumn
dspuSapRowStatus = _DspuSapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 1, 1, 7),
    _DspuSapRowStatus_Type()
)
dspuSapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dspuSapRowStatus.setStatus("current")
_DspuSapTraps_ObjectIdentity = ObjectIdentity
dspuSapTraps = _DspuSapTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 2)
)
_CiscoDspuMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDspuMIBConformance = _CiscoDspuMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2)
)
_CiscoDspuMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDspuMIBCompliances = _CiscoDspuMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 1)
)
_CiscoDspuMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDspuMIBGroups = _CiscoDspuMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2)
)

# Managed Objects groups

dspuNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 1)
)
dspuNodeGroup.setObjects(
      *(("CISCO-DSPU-MIB", "dspuNodeRsrb"),
        ("CISCO-DSPU-MIB", "dspuNodeRsrbLocalVirtualRing"),
        ("CISCO-DSPU-MIB", "dspuNodeRsrbBridgeNumber"),
        ("CISCO-DSPU-MIB", "dspuNodeRsrbTargetVirtualRing"),
        ("CISCO-DSPU-MIB", "dspuNodeRsrbVirtualMacAddress"),
        ("CISCO-DSPU-MIB", "dspuNodeDefaultPu"),
        ("CISCO-DSPU-MIB", "dspuNodeDefaultPuWindowSize"),
        ("CISCO-DSPU-MIB", "dspuNodeDefaultPuMaxIframe"),
        ("CISCO-DSPU-MIB", "dspuNodeActivationWindow"),
        ("CISCO-DSPU-MIB", "dspuNodeLastConfigChgTime"))
)
if mibBuilder.loadTexts:
    dspuNodeGroup.setStatus("current")

dspuPoolClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 2)
)
dspuPoolClassGroup.setObjects(
      *(("CISCO-DSPU-MIB", "dspuPoolClassName"),
        ("CISCO-DSPU-MIB", "dspuPoolClassInactivityTimeout"),
        ("CISCO-DSPU-MIB", "dspuPoolClassOperUpStreamLuDefs"),
        ("CISCO-DSPU-MIB", "dspuPoolClassOperDnStreamLuDefs"))
)
if mibBuilder.loadTexts:
    dspuPoolClassGroup.setStatus("current")

dspuPooledLuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 3)
)
dspuPooledLuGroup.setObjects(
      *(("CISCO-DSPU-MIB", "dspuPooledLuPeerPuIndex"),
        ("CISCO-DSPU-MIB", "dspuPooledLuPeerLuLocalAddress"))
)
if mibBuilder.loadTexts:
    dspuPooledLuGroup.setStatus("current")

dspuPuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 4)
)
dspuPuGroup.setObjects(
      *(("CISCO-DSPU-MIB", "dspuPuAdminName"),
        ("CISCO-DSPU-MIB", "dspuPuAdminType"),
        ("CISCO-DSPU-MIB", "dspuPuAdminRemoteMacAddress"),
        ("CISCO-DSPU-MIB", "dspuPuAdminRemoteSapAddress"),
        ("CISCO-DSPU-MIB", "dspuPuAdminLocalSapAddress"),
        ("CISCO-DSPU-MIB", "dspuPuAdminXid"),
        ("CISCO-DSPU-MIB", "dspuPuAdminXidFmt"),
        ("CISCO-DSPU-MIB", "dspuPuAdminWindowSize"),
        ("CISCO-DSPU-MIB", "dspuPuAdminMaxIframe"),
        ("CISCO-DSPU-MIB", "dspuPuAdminLinkRetryCount"),
        ("CISCO-DSPU-MIB", "dspuPuAdminLinkRetryTimeout"),
        ("CISCO-DSPU-MIB", "dspuPuAdminStartPu"),
        ("CISCO-DSPU-MIB", "dspuPuAdminDlcType"),
        ("CISCO-DSPU-MIB", "dspuPuAdminDlcUnit"),
        ("CISCO-DSPU-MIB", "dspuPuAdminDlcPort"),
        ("CISCO-DSPU-MIB", "dspuPuAdminFocalPoint"),
        ("CISCO-DSPU-MIB", "dspuPuAdminRowStatus"),
        ("CISCO-DSPU-MIB", "dspuPuOperName"),
        ("CISCO-DSPU-MIB", "dspuPuOperType"),
        ("CISCO-DSPU-MIB", "dspuPuOperRemoteMacAddress"),
        ("CISCO-DSPU-MIB", "dspuPuOperRemoteSapAddress"),
        ("CISCO-DSPU-MIB", "dspuPuOperLocalSapAddress"),
        ("CISCO-DSPU-MIB", "dspuPuOperXid"),
        ("CISCO-DSPU-MIB", "dspuPuOperXidFmt"),
        ("CISCO-DSPU-MIB", "dspuPuOperWindowSize"),
        ("CISCO-DSPU-MIB", "dspuPuOperMaxIframe"),
        ("CISCO-DSPU-MIB", "dspuPuOperLinkRetryCount"),
        ("CISCO-DSPU-MIB", "dspuPuOperLinkRetryTimeout"),
        ("CISCO-DSPU-MIB", "dspuPuOperStartPu"),
        ("CISCO-DSPU-MIB", "dspuPuOperDlcType"),
        ("CISCO-DSPU-MIB", "dspuPuOperDlcUnit"),
        ("CISCO-DSPU-MIB", "dspuPuOperDlcPort"),
        ("CISCO-DSPU-MIB", "dspuPuOperFocalPoint"),
        ("CISCO-DSPU-MIB", "dspuPuOperState"),
        ("CISCO-DSPU-MIB", "dspuPuOperFsmState"),
        ("CISCO-DSPU-MIB", "dspuPuOperStartTime"),
        ("CISCO-DSPU-MIB", "dspuPuOperLastStateChgTime"),
        ("CISCO-DSPU-MIB", "dspuPuStatsSentBytes"),
        ("CISCO-DSPU-MIB", "dspuPuStatsRcvdBytes"),
        ("CISCO-DSPU-MIB", "dspuPuStatsSentFrames"),
        ("CISCO-DSPU-MIB", "dspuPuStatsRcvdFrames"),
        ("CISCO-DSPU-MIB", "dspuPuStatsSentNegativeRsps"),
        ("CISCO-DSPU-MIB", "dspuPuStatsRcvdNegativeRsps"),
        ("CISCO-DSPU-MIB", "dspuPuStatsActiveLus"),
        ("CISCO-DSPU-MIB", "dspuPuStatsInactiveLus"),
        ("CISCO-DSPU-MIB", "dspuPuStatsBindLus"),
        ("CISCO-DSPU-MIB", "dspuPuStatsActivationFailures"),
        ("CISCO-DSPU-MIB", "dspuPuStatsLastActivationFailureReason"))
)
if mibBuilder.loadTexts:
    dspuPuGroup.setStatus("obsolete")

dspuLuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 5)
)
dspuLuGroup.setObjects(
      *(("CISCO-DSPU-MIB", "dspuLuAdminType"),
        ("CISCO-DSPU-MIB", "dspuLuAdminPoolClassName"),
        ("CISCO-DSPU-MIB", "dspuLuAdminPeerPuIndex"),
        ("CISCO-DSPU-MIB", "dspuLuAdminPeerLuLocalAddress"),
        ("CISCO-DSPU-MIB", "dspuLuAdminRowStatus"),
        ("CISCO-DSPU-MIB", "dspuLuOperType"),
        ("CISCO-DSPU-MIB", "dspuLuOperPoolClassName"),
        ("CISCO-DSPU-MIB", "dspuLuOperPeerPuIndex"),
        ("CISCO-DSPU-MIB", "dspuLuOperPeerLuLocalAddress"),
        ("CISCO-DSPU-MIB", "dspuLuOperState"),
        ("CISCO-DSPU-MIB", "dspuLuOperFsmState"),
        ("CISCO-DSPU-MIB", "dspuLuOperSessionState"))
)
if mibBuilder.loadTexts:
    dspuLuGroup.setStatus("obsolete")

dspuSapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 6)
)
dspuSapGroup.setObjects(
      *(("CISCO-DSPU-MIB", "dspuSapType"),
        ("CISCO-DSPU-MIB", "dspuSapOperState"),
        ("CISCO-DSPU-MIB", "dspuSapRowStatus"))
)
if mibBuilder.loadTexts:
    dspuSapGroup.setStatus("current")

dspuPuGroupV11R01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 7)
)
dspuPuGroupV11R01.setObjects(
      *(("CISCO-DSPU-MIB", "dspuPuAdminName"),
        ("CISCO-DSPU-MIB", "dspuPuAdminType"),
        ("CISCO-DSPU-MIB", "dspuPuAdminRemoteMacAddress"),
        ("CISCO-DSPU-MIB", "dspuPuAdminRemoteSapAddress"),
        ("CISCO-DSPU-MIB", "dspuPuAdminLocalSapAddress"),
        ("CISCO-DSPU-MIB", "dspuPuAdminXid"),
        ("CISCO-DSPU-MIB", "dspuPuAdminXidFmt"),
        ("CISCO-DSPU-MIB", "dspuPuAdminWindowSize"),
        ("CISCO-DSPU-MIB", "dspuPuAdminMaxIframe"),
        ("CISCO-DSPU-MIB", "dspuPuAdminLinkRetryCount"),
        ("CISCO-DSPU-MIB", "dspuPuAdminLinkRetryTimeout"),
        ("CISCO-DSPU-MIB", "dspuPuAdminStartPu"),
        ("CISCO-DSPU-MIB", "dspuPuAdminDlcType"),
        ("CISCO-DSPU-MIB", "dspuPuAdminDlcUnit"),
        ("CISCO-DSPU-MIB", "dspuPuAdminDlcPort"),
        ("CISCO-DSPU-MIB", "dspuPuAdminFocalPoint"),
        ("CISCO-DSPU-MIB", "dspuPuAdminRowStatus"),
        ("CISCO-DSPU-MIB", "dspuPuAdminRemoteAddress"),
        ("CISCO-DSPU-MIB", "dspuPuOperName"),
        ("CISCO-DSPU-MIB", "dspuPuOperType"),
        ("CISCO-DSPU-MIB", "dspuPuOperRemoteMacAddress"),
        ("CISCO-DSPU-MIB", "dspuPuOperRemoteSapAddress"),
        ("CISCO-DSPU-MIB", "dspuPuOperLocalSapAddress"),
        ("CISCO-DSPU-MIB", "dspuPuOperXid"),
        ("CISCO-DSPU-MIB", "dspuPuOperXidFmt"),
        ("CISCO-DSPU-MIB", "dspuPuOperWindowSize"),
        ("CISCO-DSPU-MIB", "dspuPuOperMaxIframe"),
        ("CISCO-DSPU-MIB", "dspuPuOperLinkRetryCount"),
        ("CISCO-DSPU-MIB", "dspuPuOperLinkRetryTimeout"),
        ("CISCO-DSPU-MIB", "dspuPuOperStartPu"),
        ("CISCO-DSPU-MIB", "dspuPuOperDlcType"),
        ("CISCO-DSPU-MIB", "dspuPuOperDlcUnit"),
        ("CISCO-DSPU-MIB", "dspuPuOperDlcPort"),
        ("CISCO-DSPU-MIB", "dspuPuOperFocalPoint"),
        ("CISCO-DSPU-MIB", "dspuPuOperState"),
        ("CISCO-DSPU-MIB", "dspuPuOperFsmState"),
        ("CISCO-DSPU-MIB", "dspuPuOperStartTime"),
        ("CISCO-DSPU-MIB", "dspuPuOperLastStateChgTime"),
        ("CISCO-DSPU-MIB", "dspuPuOperRemoteAddress"),
        ("CISCO-DSPU-MIB", "dspuPuStatsSentBytes"),
        ("CISCO-DSPU-MIB", "dspuPuStatsRcvdBytes"),
        ("CISCO-DSPU-MIB", "dspuPuStatsSentFrames"),
        ("CISCO-DSPU-MIB", "dspuPuStatsRcvdFrames"),
        ("CISCO-DSPU-MIB", "dspuPuStatsSentNegativeRsps"),
        ("CISCO-DSPU-MIB", "dspuPuStatsRcvdNegativeRsps"),
        ("CISCO-DSPU-MIB", "dspuPuStatsActiveLus"),
        ("CISCO-DSPU-MIB", "dspuPuStatsInactiveLus"),
        ("CISCO-DSPU-MIB", "dspuPuStatsBindLus"),
        ("CISCO-DSPU-MIB", "dspuPuStatsActivationFailures"),
        ("CISCO-DSPU-MIB", "dspuPuStatsLastActivationFailureReason"))
)
if mibBuilder.loadTexts:
    dspuPuGroupV11R01.setStatus("current")

dspuLuGroupV11R01 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 2, 8)
)
dspuLuGroupV11R01.setObjects(
      *(("CISCO-DSPU-MIB", "dspuLuAdminType"),
        ("CISCO-DSPU-MIB", "dspuLuAdminPoolClassName"),
        ("CISCO-DSPU-MIB", "dspuLuAdminPeerPuIndex"),
        ("CISCO-DSPU-MIB", "dspuLuAdminPeerLuLocalAddress"),
        ("CISCO-DSPU-MIB", "dspuLuAdminRowStatus"),
        ("CISCO-DSPU-MIB", "dspuLuOperType"),
        ("CISCO-DSPU-MIB", "dspuLuOperPoolClassName"),
        ("CISCO-DSPU-MIB", "dspuLuOperPeerPuIndex"),
        ("CISCO-DSPU-MIB", "dspuLuOperPeerLuLocalAddress"),
        ("CISCO-DSPU-MIB", "dspuLuOperState"),
        ("CISCO-DSPU-MIB", "dspuLuOperFsmState"),
        ("CISCO-DSPU-MIB", "dspuLuOperSessionState"),
        ("CISCO-DSPU-MIB", "dspuLuOperLastActivationFailureReason"))
)
if mibBuilder.loadTexts:
    dspuLuGroupV11R01.setStatus("current")


# Notification objects

newdspuPuStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4, 0, 1)
)
newdspuPuStateChangeTrap.setObjects(
      *(("CISCO-DSPU-MIB", "dspuPuOperName"),
        ("CISCO-DSPU-MIB", "dspuPuOperState"))
)
if mibBuilder.loadTexts:
    newdspuPuStateChangeTrap.setStatus(
        "current"
    )

newdspuPuActivationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4, 0, 2)
)
newdspuPuActivationFailureTrap.setObjects(
      *(("CISCO-DSPU-MIB", "dspuPuOperName"),
        ("CISCO-DSPU-MIB", "dspuPuOperState"),
        ("CISCO-DSPU-MIB", "dspuPuStatsLastActivationFailureReason"))
)
if mibBuilder.loadTexts:
    newdspuPuActivationFailureTrap.setStatus(
        "current"
    )

dspuPuStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4, 1)
)
dspuPuStateChangeTrap.setObjects(
      *(("CISCO-DSPU-MIB", "dspuPuOperName"),
        ("CISCO-DSPU-MIB", "dspuPuOperState"))
)
if mibBuilder.loadTexts:
    dspuPuStateChangeTrap.setStatus(
        "obsolete"
    )

dspuPuActivationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 4, 4, 2)
)
dspuPuActivationFailureTrap.setObjects(
      *(("CISCO-DSPU-MIB", "dspuPuOperName"),
        ("CISCO-DSPU-MIB", "dspuPuOperState"),
        ("CISCO-DSPU-MIB", "dspuPuStatsLastActivationFailureReason"))
)
if mibBuilder.loadTexts:
    dspuPuActivationFailureTrap.setStatus(
        "obsolete"
    )

newdspuLuStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 3, 0, 1)
)
newdspuLuStateChangeTrap.setObjects(
      *(("CISCO-DSPU-MIB", "dspuPuOperName"),
        ("CISCO-DSPU-MIB", "dspuLuOperState"))
)
if mibBuilder.loadTexts:
    newdspuLuStateChangeTrap.setStatus(
        "current"
    )

dspuLuActivationFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 3, 0, 2)
)
dspuLuActivationFailureTrap.setObjects(
      *(("CISCO-DSPU-MIB", "dspuPuOperName"),
        ("CISCO-DSPU-MIB", "dspuLuOperState"),
        ("CISCO-DSPU-MIB", "dspuLuOperLastActivationFailureReason"))
)
if mibBuilder.loadTexts:
    dspuLuActivationFailureTrap.setStatus(
        "current"
    )

dspuLuStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 5, 3, 1)
)
dspuLuStateChangeTrap.setObjects(
      *(("CISCO-DSPU-MIB", "dspuPuOperName"),
        ("CISCO-DSPU-MIB", "dspuLuOperLuLocalAddress"),
        ("CISCO-DSPU-MIB", "dspuLuOperState"))
)
if mibBuilder.loadTexts:
    dspuLuStateChangeTrap.setStatus(
        "obsolete"
    )

dspuSapStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 1, 6, 2, 1)
)
dspuSapStateChangeTrap.setObjects(
      *(("CISCO-DSPU-MIB", "dspuSapDlcType"),
        ("CISCO-DSPU-MIB", "dspuSapDlcUnit"),
        ("CISCO-DSPU-MIB", "dspuSapDlcPort"),
        ("CISCO-DSPU-MIB", "dspuSapAddress"),
        ("CISCO-DSPU-MIB", "dspuSapOperState"))
)
if mibBuilder.loadTexts:
    dspuSapStateChangeTrap.setStatus(
        "obsolete"
    )


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDspuMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDspuMIBCompliance.setStatus(
        "obsolete"
    )

ciscoDspuMIBComplianceV11R01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 24, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoDspuMIBComplianceV11R01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DSPU-MIB",
    **{"ciscoDspuMIB": ciscoDspuMIB,
       "dspuObjects": dspuObjects,
       "dspuNode": dspuNode,
       "dspuNodeRsrb": dspuNodeRsrb,
       "dspuNodeRsrbLocalVirtualRing": dspuNodeRsrbLocalVirtualRing,
       "dspuNodeRsrbBridgeNumber": dspuNodeRsrbBridgeNumber,
       "dspuNodeRsrbTargetVirtualRing": dspuNodeRsrbTargetVirtualRing,
       "dspuNodeRsrbVirtualMacAddress": dspuNodeRsrbVirtualMacAddress,
       "dspuNodeDefaultPu": dspuNodeDefaultPu,
       "dspuNodeDefaultPuWindowSize": dspuNodeDefaultPuWindowSize,
       "dspuNodeDefaultPuMaxIframe": dspuNodeDefaultPuMaxIframe,
       "dspuNodeActivationWindow": dspuNodeActivationWindow,
       "dspuNodeLastConfigChgTime": dspuNodeLastConfigChgTime,
       "dspuPoolClass": dspuPoolClass,
       "dspuPoolClassTable": dspuPoolClassTable,
       "dspuPoolClassEntry": dspuPoolClassEntry,
       "dspuPoolClassIndex": dspuPoolClassIndex,
       "dspuPoolClassName": dspuPoolClassName,
       "dspuPoolClassInactivityTimeout": dspuPoolClassInactivityTimeout,
       "dspuPoolClassOperUpStreamLuDefs": dspuPoolClassOperUpStreamLuDefs,
       "dspuPoolClassOperDnStreamLuDefs": dspuPoolClassOperDnStreamLuDefs,
       "dspuPooledLu": dspuPooledLu,
       "dspuPooledLuTable": dspuPooledLuTable,
       "dspuPooledLuEntry": dspuPooledLuEntry,
       "dspuPooledLuPeerPuIndex": dspuPooledLuPeerPuIndex,
       "dspuPooledLuPeerLuLocalAddress": dspuPooledLuPeerLuLocalAddress,
       "dspuPu": dspuPu,
       "dspuPuAdminTable": dspuPuAdminTable,
       "dspuPuAdminEntry": dspuPuAdminEntry,
       "dspuPuAdminIndex": dspuPuAdminIndex,
       "dspuPuAdminName": dspuPuAdminName,
       "dspuPuAdminType": dspuPuAdminType,
       "dspuPuAdminRemoteMacAddress": dspuPuAdminRemoteMacAddress,
       "dspuPuAdminRemoteSapAddress": dspuPuAdminRemoteSapAddress,
       "dspuPuAdminLocalSapAddress": dspuPuAdminLocalSapAddress,
       "dspuPuAdminXid": dspuPuAdminXid,
       "dspuPuAdminXidFmt": dspuPuAdminXidFmt,
       "dspuPuAdminWindowSize": dspuPuAdminWindowSize,
       "dspuPuAdminMaxIframe": dspuPuAdminMaxIframe,
       "dspuPuAdminLinkRetryCount": dspuPuAdminLinkRetryCount,
       "dspuPuAdminLinkRetryTimeout": dspuPuAdminLinkRetryTimeout,
       "dspuPuAdminStartPu": dspuPuAdminStartPu,
       "dspuPuAdminDlcType": dspuPuAdminDlcType,
       "dspuPuAdminDlcUnit": dspuPuAdminDlcUnit,
       "dspuPuAdminDlcPort": dspuPuAdminDlcPort,
       "dspuPuAdminFocalPoint": dspuPuAdminFocalPoint,
       "dspuPuAdminRowStatus": dspuPuAdminRowStatus,
       "dspuPuAdminRemoteAddress": dspuPuAdminRemoteAddress,
       "dspuPuOperTable": dspuPuOperTable,
       "dspuPuOperEntry": dspuPuOperEntry,
       "dspuPuOperIndex": dspuPuOperIndex,
       "dspuPuOperName": dspuPuOperName,
       "dspuPuOperType": dspuPuOperType,
       "dspuPuOperRemoteMacAddress": dspuPuOperRemoteMacAddress,
       "dspuPuOperRemoteSapAddress": dspuPuOperRemoteSapAddress,
       "dspuPuOperLocalSapAddress": dspuPuOperLocalSapAddress,
       "dspuPuOperXid": dspuPuOperXid,
       "dspuPuOperXidFmt": dspuPuOperXidFmt,
       "dspuPuOperWindowSize": dspuPuOperWindowSize,
       "dspuPuOperMaxIframe": dspuPuOperMaxIframe,
       "dspuPuOperLinkRetryCount": dspuPuOperLinkRetryCount,
       "dspuPuOperLinkRetryTimeout": dspuPuOperLinkRetryTimeout,
       "dspuPuOperStartPu": dspuPuOperStartPu,
       "dspuPuOperDlcType": dspuPuOperDlcType,
       "dspuPuOperDlcUnit": dspuPuOperDlcUnit,
       "dspuPuOperDlcPort": dspuPuOperDlcPort,
       "dspuPuOperFocalPoint": dspuPuOperFocalPoint,
       "dspuPuOperState": dspuPuOperState,
       "dspuPuOperFsmState": dspuPuOperFsmState,
       "dspuPuOperStartTime": dspuPuOperStartTime,
       "dspuPuOperLastStateChgTime": dspuPuOperLastStateChgTime,
       "dspuPuOperRemoteAddress": dspuPuOperRemoteAddress,
       "dspuPuStatsTable": dspuPuStatsTable,
       "dspuPuStatsEntry": dspuPuStatsEntry,
       "dspuPuStatsSentBytes": dspuPuStatsSentBytes,
       "dspuPuStatsRcvdBytes": dspuPuStatsRcvdBytes,
       "dspuPuStatsSentFrames": dspuPuStatsSentFrames,
       "dspuPuStatsRcvdFrames": dspuPuStatsRcvdFrames,
       "dspuPuStatsSentNegativeRsps": dspuPuStatsSentNegativeRsps,
       "dspuPuStatsRcvdNegativeRsps": dspuPuStatsRcvdNegativeRsps,
       "dspuPuStatsActiveLus": dspuPuStatsActiveLus,
       "dspuPuStatsInactiveLus": dspuPuStatsInactiveLus,
       "dspuPuStatsBindLus": dspuPuStatsBindLus,
       "dspuPuStatsActivationFailures": dspuPuStatsActivationFailures,
       "dspuPuStatsLastActivationFailureReason": dspuPuStatsLastActivationFailureReason,
       "dspuPuTraps": dspuPuTraps,
       "dspuPuTrapsPrefix": dspuPuTrapsPrefix,
       "newdspuPuStateChangeTrap": newdspuPuStateChangeTrap,
       "newdspuPuActivationFailureTrap": newdspuPuActivationFailureTrap,
       "dspuPuStateChangeTrap": dspuPuStateChangeTrap,
       "dspuPuActivationFailureTrap": dspuPuActivationFailureTrap,
       "dspuLu": dspuLu,
       "dspuLuAdminTable": dspuLuAdminTable,
       "dspuLuAdminEntry": dspuLuAdminEntry,
       "dspuLuAdminLuLocalAddress": dspuLuAdminLuLocalAddress,
       "dspuLuAdminType": dspuLuAdminType,
       "dspuLuAdminPoolClassName": dspuLuAdminPoolClassName,
       "dspuLuAdminPeerPuIndex": dspuLuAdminPeerPuIndex,
       "dspuLuAdminPeerLuLocalAddress": dspuLuAdminPeerLuLocalAddress,
       "dspuLuAdminRowStatus": dspuLuAdminRowStatus,
       "dspuLuOperTable": dspuLuOperTable,
       "dspuLuOperEntry": dspuLuOperEntry,
       "dspuLuOperLuLocalAddress": dspuLuOperLuLocalAddress,
       "dspuLuOperType": dspuLuOperType,
       "dspuLuOperPoolClassName": dspuLuOperPoolClassName,
       "dspuLuOperPeerPuIndex": dspuLuOperPeerPuIndex,
       "dspuLuOperPeerLuLocalAddress": dspuLuOperPeerLuLocalAddress,
       "dspuLuOperState": dspuLuOperState,
       "dspuLuOperFsmState": dspuLuOperFsmState,
       "dspuLuOperSessionState": dspuLuOperSessionState,
       "dspuLuOperLastActivationFailureReason": dspuLuOperLastActivationFailureReason,
       "dspuLuTraps": dspuLuTraps,
       "dspuLuTrapsPrefix": dspuLuTrapsPrefix,
       "newdspuLuStateChangeTrap": newdspuLuStateChangeTrap,
       "dspuLuActivationFailureTrap": dspuLuActivationFailureTrap,
       "dspuLuStateChangeTrap": dspuLuStateChangeTrap,
       "dspuSap": dspuSap,
       "dspuSapTable": dspuSapTable,
       "dspuSapEntry": dspuSapEntry,
       "dspuSapAddress": dspuSapAddress,
       "dspuSapType": dspuSapType,
       "dspuSapDlcType": dspuSapDlcType,
       "dspuSapDlcUnit": dspuSapDlcUnit,
       "dspuSapDlcPort": dspuSapDlcPort,
       "dspuSapOperState": dspuSapOperState,
       "dspuSapRowStatus": dspuSapRowStatus,
       "dspuSapTraps": dspuSapTraps,
       "dspuSapStateChangeTrap": dspuSapStateChangeTrap,
       "ciscoDspuMIBConformance": ciscoDspuMIBConformance,
       "ciscoDspuMIBCompliances": ciscoDspuMIBCompliances,
       "ciscoDspuMIBCompliance": ciscoDspuMIBCompliance,
       "ciscoDspuMIBComplianceV11R01": ciscoDspuMIBComplianceV11R01,
       "ciscoDspuMIBGroups": ciscoDspuMIBGroups,
       "dspuNodeGroup": dspuNodeGroup,
       "dspuPoolClassGroup": dspuPoolClassGroup,
       "dspuPooledLuGroup": dspuPooledLuGroup,
       "dspuPuGroup": dspuPuGroup,
       "dspuLuGroup": dspuLuGroup,
       "dspuSapGroup": dspuSapGroup,
       "dspuPuGroupV11R01": dspuPuGroupV11R01,
       "dspuLuGroupV11R01": dspuLuGroupV11R01}
)
