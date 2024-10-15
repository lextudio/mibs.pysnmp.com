# SNMP MIB module (ZXR10-MSTP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-MSTP
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:00 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(zxr10,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10")


# MODULE-IDENTITY

mstpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127)
)


# Types definitions



class UINT32(Unsigned32):
    """Custom type UINT32 based on Unsigned32"""




class Char(OctetString):
    """Custom type Char based on OctetString"""



# TEXTUAL-CONVENTIONS



class MSTPProtocolType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("mstp", 3),
          ("rstp", 2),
          ("sstp", 1))
    )



class MSTPTransportType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("untransparent", 0))
    )



class MSTPPortEnable(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("portstpunused", 0),
          ("portstpused", 1))
    )



class MSTPLinkType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("p2p", 1),
          ("share", 0))
    )



class MSTPEdgePortEnable(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("edge-disable", 0),
          ("edge-enable", 1))
    )



class MSTPBPDUGuardEnable(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("bpduguarddisable", 0),
          ("bpduguardenable", 1))
    )



class MSTPPacketType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cisco", 1),
          ("hammer", 2),
          ("huawei", 3),
          ("ieee", 0))
    )



class MSTPPortStatus(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("broken", 5),
          ("disabled", 0),
          ("forwarding", 4),
          ("learning", 3),
          ("listening", 2))
    )



class MSTPRootGuardEnable(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rootguarddisable", 0),
          ("rootguardenable", 1))
    )



class MSTPLoopGuardEnable(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loopguarddisable", 0),
          ("loopguardenable", 1))
    )



# MIB Managed Objects in the order of their OIDs

_MstpMibObjects_ObjectIdentity = ObjectIdentity
mstpMibObjects = _MstpMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1)
)
_MstpGlobalPara_ObjectIdentity = ObjectIdentity
mstpGlobalPara = _MstpGlobalPara_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1)
)
_StpProtocolSpecification_Type = MSTPProtocolType
_StpProtocolSpecification_Object = MibScalar
stpProtocolSpecification = _StpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 1),
    _StpProtocolSpecification_Type()
)
stpProtocolSpecification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpProtocolSpecification.setStatus("current")
_StpMaxAge_Type = UINT32
_StpMaxAge_Object = MibScalar
stpMaxAge = _StpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 2),
    _StpMaxAge_Type()
)
stpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpMaxAge.setStatus("current")
_StpHelloTime_Type = UINT32
_StpHelloTime_Object = MibScalar
stpHelloTime = _StpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 3),
    _StpHelloTime_Type()
)
stpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpHelloTime.setStatus("current")
_StpHoldTime_Type = UINT32
_StpHoldTime_Object = MibScalar
stpHoldTime = _StpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 4),
    _StpHoldTime_Type()
)
stpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpHoldTime.setStatus("current")
_StpForwardDelay_Type = UINT32
_StpForwardDelay_Object = MibScalar
stpForwardDelay = _StpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 5),
    _StpForwardDelay_Type()
)
stpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpForwardDelay.setStatus("current")


class _StpBridgeMaxAge_Type(UINT32):
    """Custom type stpBridgeMaxAge based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_StpBridgeMaxAge_Type.__name__ = "UINT32"
_StpBridgeMaxAge_Object = MibScalar
stpBridgeMaxAge = _StpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 6),
    _StpBridgeMaxAge_Type()
)
stpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeMaxAge.setStatus("current")


class _StpBridgeHelloTime_Type(UINT32):
    """Custom type stpBridgeHelloTime based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StpBridgeHelloTime_Type.__name__ = "UINT32"
_StpBridgeHelloTime_Object = MibScalar
stpBridgeHelloTime = _StpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 7),
    _StpBridgeHelloTime_Type()
)
stpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeHelloTime.setStatus("current")


class _StpBridgeForwardDelay_Type(UINT32):
    """Custom type stpBridgeForwardDelay based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_StpBridgeForwardDelay_Type.__name__ = "UINT32"
_StpBridgeForwardDelay_Object = MibScalar
stpBridgeForwardDelay = _StpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 8),
    _StpBridgeForwardDelay_Type()
)
stpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeForwardDelay.setStatus("current")
_StpTransparentEnable_Type = MSTPTransportType
_StpTransparentEnable_Object = MibScalar
stpTransparentEnable = _StpTransparentEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 9),
    _StpTransparentEnable_Type()
)
stpTransparentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpTransparentEnable.setStatus("current")


class _StpRevision_Type(UINT32):
    """Custom type stpRevision based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StpRevision_Type.__name__ = "UINT32"
_StpRevision_Object = MibScalar
stpRevision = _StpRevision_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 10),
    _StpRevision_Type()
)
stpRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpRevision.setStatus("current")


class _StpConfigName_Type(Char):
    """Custom type stpConfigName based on Char"""
    subtypeSpec = Char.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 33),
    )


_StpConfigName_Type.__name__ = "Char"
_StpConfigName_Object = MibScalar
stpConfigName = _StpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 11),
    _StpConfigName_Type()
)
stpConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpConfigName.setStatus("current")


class _StpHmd5Digest_Type(Char):
    """Custom type stpHmd5Digest based on Char"""
    subtypeSpec = Char.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_StpHmd5Digest_Type.__name__ = "Char"
_StpHmd5Digest_Object = MibScalar
stpHmd5Digest = _StpHmd5Digest_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 12),
    _StpHmd5Digest_Type()
)
stpHmd5Digest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpHmd5Digest.setStatus("current")


class _StpHmd5Key_Type(Char):
    """Custom type stpHmd5Key based on Char"""
    subtypeSpec = Char.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_StpHmd5Key_Type.__name__ = "Char"
_StpHmd5Key_Object = MibScalar
stpHmd5Key = _StpHmd5Key_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 1, 13),
    _StpHmd5Key_Type()
)
stpHmd5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpHmd5Key.setStatus("current")
_MstpInstance_ObjectIdentity = ObjectIdentity
mstpInstance = _MstpInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2)
)
_MstpInstanceTable_Object = MibTable
mstpInstanceTable = _MstpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mstpInstanceTable.setStatus("current")
_MstpInstanceEntry_Object = MibTableRow
mstpInstanceEntry = _MstpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1)
)
mstpInstanceEntry.setIndexNames(
    (0, "ZXR10-MSTP", "stpInstanceID"),
)
if mibBuilder.loadTexts:
    mstpInstanceEntry.setStatus("current")


class _StpInstanceID_Type(UINT32):
    """Custom type stpInstanceID based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_StpInstanceID_Type.__name__ = "UINT32"
_StpInstanceID_Object = MibTableColumn
stpInstanceID = _StpInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 1),
    _StpInstanceID_Type()
)
stpInstanceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpInstanceID.setStatus("current")


class _StpBridgePriority_Type(UINT32):
    """Custom type stpBridgePriority based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_StpBridgePriority_Type.__name__ = "UINT32"
_StpBridgePriority_Object = MibTableColumn
stpBridgePriority = _StpBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 2),
    _StpBridgePriority_Type()
)
stpBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgePriority.setStatus("current")
_StpBridgeMac_Type = Char
_StpBridgeMac_Object = MibTableColumn
stpBridgeMac = _StpBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 3),
    _StpBridgeMac_Type()
)
stpBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpBridgeMac.setStatus("current")
_StpInstanceRootPriority_Type = UINT32
_StpInstanceRootPriority_Object = MibTableColumn
stpInstanceRootPriority = _StpInstanceRootPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 4),
    _StpInstanceRootPriority_Type()
)
stpInstanceRootPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInstanceRootPriority.setStatus("current")
_StpInstanceRootMac_Type = Char
_StpInstanceRootMac_Object = MibTableColumn
stpInstanceRootMac = _StpInstanceRootMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 5),
    _StpInstanceRootMac_Type()
)
stpInstanceRootMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpInstanceRootMac.setStatus("current")
_StpRemainHops_Type = UINT32
_StpRemainHops_Object = MibTableColumn
stpRemainHops = _StpRemainHops_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 6),
    _StpRemainHops_Type()
)
stpRemainHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpRemainHops.setStatus("current")


class _StpVlanMaps_Type(Char):
    """Custom type stpVlanMaps based on Char"""
    subtypeSpec = Char.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(100, 100),
    )


_StpVlanMaps_Type.__name__ = "Char"
_StpVlanMaps_Object = MibTableColumn
stpVlanMaps = _StpVlanMaps_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 7),
    _StpVlanMaps_Type()
)
stpVlanMaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpVlanMaps.setStatus("current")
_StpMAXHops_Type = UINT32
_StpMAXHops_Object = MibTableColumn
stpMAXHops = _StpMAXHops_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 8),
    _StpMAXHops_Type()
)
stpMAXHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpMAXHops.setStatus("current")


class _StpBridgeMAXHops_Type(UINT32):
    """Custom type stpBridgeMAXHops based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_StpBridgeMAXHops_Type.__name__ = "UINT32"
_StpBridgeMAXHops_Object = MibTableColumn
stpBridgeMAXHops = _StpBridgeMAXHops_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 9),
    _StpBridgeMAXHops_Type()
)
stpBridgeMAXHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBridgeMAXHops.setStatus("current")
_StpInstanceRowStatus_Type = RowStatus
_StpInstanceRowStatus_Object = MibTableColumn
stpInstanceRowStatus = _StpInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 2, 1, 1, 10),
    _StpInstanceRowStatus_Type()
)
stpInstanceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpInstanceRowStatus.setStatus("current")
_MstpPort_ObjectIdentity = ObjectIdentity
mstpPort = _MstpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3)
)
_MstpPortTable_Object = MibTable
mstpPortTable = _MstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mstpPortTable.setStatus("current")
_MstpPortEntry_Object = MibTableRow
mstpPortEntry = _MstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1)
)
mstpPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mstpPortEntry.setStatus("current")
_StpPortEnable_Type = MSTPPortEnable
_StpPortEnable_Object = MibTableColumn
stpPortEnable = _StpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 1),
    _StpPortEnable_Type()
)
stpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortEnable.setStatus("current")
_StpLinkType_Type = MSTPLinkType
_StpLinkType_Object = MibTableColumn
stpLinkType = _StpLinkType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 2),
    _StpLinkType_Type()
)
stpLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpLinkType.setStatus("current")
_StpEdgedPortEnable_Type = MSTPEdgePortEnable
_StpEdgedPortEnable_Object = MibTableColumn
stpEdgedPortEnable = _StpEdgedPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 3),
    _StpEdgedPortEnable_Type()
)
stpEdgedPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpEdgedPortEnable.setStatus("current")
_StpBPDUGuardEnable_Type = MSTPBPDUGuardEnable
_StpBPDUGuardEnable_Object = MibTableColumn
stpBPDUGuardEnable = _StpBPDUGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 4),
    _StpBPDUGuardEnable_Type()
)
stpBPDUGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpBPDUGuardEnable.setStatus("current")
_StpPacketType_Type = MSTPPacketType
_StpPacketType_Object = MibTableColumn
stpPacketType = _StpPacketType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 5),
    _StpPacketType_Type()
)
stpPacketType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPacketType.setStatus("current")
_StpIfName_Type = Char
_StpIfName_Object = MibTableColumn
stpIfName = _StpIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 3, 1, 1, 6),
    _StpIfName_Type()
)
stpIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpIfName.setStatus("current")
_MstpPortInstance_ObjectIdentity = ObjectIdentity
mstpPortInstance = _MstpPortInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4)
)
_MstpPortInstanceTable_Object = MibTable
mstpPortInstanceTable = _MstpPortInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1)
)
if mibBuilder.loadTexts:
    mstpPortInstanceTable.setStatus("current")
_MstpPortInstanceEntry_Object = MibTableRow
mstpPortInstanceEntry = _MstpPortInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1)
)
mstpPortInstanceEntry.setIndexNames(
    (0, "ZXR10-MSTP", "stpPortInstanceID"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mstpPortInstanceEntry.setStatus("current")
_StpPortInstanceID_Type = UINT32
_StpPortInstanceID_Object = MibTableColumn
stpPortInstanceID = _StpPortInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 1),
    _StpPortInstanceID_Type()
)
stpPortInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortInstanceID.setStatus("current")
_StpPortName_Type = Char
_StpPortName_Object = MibTableColumn
stpPortName = _StpPortName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 2),
    _StpPortName_Type()
)
stpPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortName.setStatus("current")


class _StpPortPriority_Type(UINT32):
    """Custom type stpPortPriority based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_StpPortPriority_Type.__name__ = "UINT32"
_StpPortPriority_Object = MibTableColumn
stpPortPriority = _StpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 3),
    _StpPortPriority_Type()
)
stpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPriority.setStatus("current")


class _StpPortPathCost_Type(UINT32):
    """Custom type stpPortPathCost based on UINT32"""
    subtypeSpec = UINT32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000),
    )


_StpPortPathCost_Type.__name__ = "UINT32"
_StpPortPathCost_Object = MibTableColumn
stpPortPathCost = _StpPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 4),
    _StpPortPathCost_Type()
)
stpPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpPortPathCost.setStatus("current")
_StpPortState_Type = MSTPPortStatus
_StpPortState_Object = MibTableColumn
stpPortState = _StpPortState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 5),
    _StpPortState_Type()
)
stpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortState.setStatus("current")
_StpPortDesignatedCost_Type = UINT32
_StpPortDesignatedCost_Object = MibTableColumn
stpPortDesignatedCost = _StpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 6),
    _StpPortDesignatedCost_Type()
)
stpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedCost.setStatus("current")
_StpPortDesignatedBridgePriority_Type = UINT32
_StpPortDesignatedBridgePriority_Object = MibTableColumn
stpPortDesignatedBridgePriority = _StpPortDesignatedBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 7),
    _StpPortDesignatedBridgePriority_Type()
)
stpPortDesignatedBridgePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedBridgePriority.setStatus("current")
_StpPortDesignatedBridgeMac_Type = Char
_StpPortDesignatedBridgeMac_Object = MibTableColumn
stpPortDesignatedBridgeMac = _StpPortDesignatedBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 8),
    _StpPortDesignatedBridgeMac_Type()
)
stpPortDesignatedBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedBridgeMac.setStatus("current")
_StpPortDesignatedPort_Type = UINT32
_StpPortDesignatedPort_Object = MibTableColumn
stpPortDesignatedPort = _StpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 9),
    _StpPortDesignatedPort_Type()
)
stpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stpPortDesignatedPort.setStatus("current")
_StpRootGuardEnable_Type = MSTPRootGuardEnable
_StpRootGuardEnable_Object = MibTableColumn
stpRootGuardEnable = _StpRootGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 10),
    _StpRootGuardEnable_Type()
)
stpRootGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpRootGuardEnable.setStatus("current")
_StpLoopGuardEnable_Type = MSTPLoopGuardEnable
_StpLoopGuardEnable_Object = MibTableColumn
stpLoopGuardEnable = _StpLoopGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 127, 1, 4, 1, 1, 11),
    _StpLoopGuardEnable_Type()
)
stpLoopGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stpLoopGuardEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-MSTP",
    **{"UINT32": UINT32,
       "Char": Char,
       "MSTPProtocolType": MSTPProtocolType,
       "MSTPTransportType": MSTPTransportType,
       "MSTPPortEnable": MSTPPortEnable,
       "MSTPLinkType": MSTPLinkType,
       "MSTPEdgePortEnable": MSTPEdgePortEnable,
       "MSTPBPDUGuardEnable": MSTPBPDUGuardEnable,
       "MSTPPacketType": MSTPPacketType,
       "MSTPPortStatus": MSTPPortStatus,
       "MSTPRootGuardEnable": MSTPRootGuardEnable,
       "MSTPLoopGuardEnable": MSTPLoopGuardEnable,
       "mstpMIB": mstpMIB,
       "mstpMibObjects": mstpMibObjects,
       "mstpGlobalPara": mstpGlobalPara,
       "stpProtocolSpecification": stpProtocolSpecification,
       "stpMaxAge": stpMaxAge,
       "stpHelloTime": stpHelloTime,
       "stpHoldTime": stpHoldTime,
       "stpForwardDelay": stpForwardDelay,
       "stpBridgeMaxAge": stpBridgeMaxAge,
       "stpBridgeHelloTime": stpBridgeHelloTime,
       "stpBridgeForwardDelay": stpBridgeForwardDelay,
       "stpTransparentEnable": stpTransparentEnable,
       "stpRevision": stpRevision,
       "stpConfigName": stpConfigName,
       "stpHmd5Digest": stpHmd5Digest,
       "stpHmd5Key": stpHmd5Key,
       "mstpInstance": mstpInstance,
       "mstpInstanceTable": mstpInstanceTable,
       "mstpInstanceEntry": mstpInstanceEntry,
       "stpInstanceID": stpInstanceID,
       "stpBridgePriority": stpBridgePriority,
       "stpBridgeMac": stpBridgeMac,
       "stpInstanceRootPriority": stpInstanceRootPriority,
       "stpInstanceRootMac": stpInstanceRootMac,
       "stpRemainHops": stpRemainHops,
       "stpVlanMaps": stpVlanMaps,
       "stpMAXHops": stpMAXHops,
       "stpBridgeMAXHops": stpBridgeMAXHops,
       "stpInstanceRowStatus": stpInstanceRowStatus,
       "mstpPort": mstpPort,
       "mstpPortTable": mstpPortTable,
       "mstpPortEntry": mstpPortEntry,
       "stpPortEnable": stpPortEnable,
       "stpLinkType": stpLinkType,
       "stpEdgedPortEnable": stpEdgedPortEnable,
       "stpBPDUGuardEnable": stpBPDUGuardEnable,
       "stpPacketType": stpPacketType,
       "stpIfName": stpIfName,
       "mstpPortInstance": mstpPortInstance,
       "mstpPortInstanceTable": mstpPortInstanceTable,
       "mstpPortInstanceEntry": mstpPortInstanceEntry,
       "stpPortInstanceID": stpPortInstanceID,
       "stpPortName": stpPortName,
       "stpPortPriority": stpPortPriority,
       "stpPortPathCost": stpPortPathCost,
       "stpPortState": stpPortState,
       "stpPortDesignatedCost": stpPortDesignatedCost,
       "stpPortDesignatedBridgePriority": stpPortDesignatedBridgePriority,
       "stpPortDesignatedBridgeMac": stpPortDesignatedBridgeMac,
       "stpPortDesignatedPort": stpPortDesignatedPort,
       "stpRootGuardEnable": stpRootGuardEnable,
       "stpLoopGuardEnable": stpLoopGuardEnable}
)
