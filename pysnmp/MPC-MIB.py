# SNMP MIB module (MPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MPC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:51 2024
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

(AtmAddr,) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmAddr")

(lecIndex,) = mibBuilder.importSymbols(
    "LAN-EMULATION-CLIENT-MIB",
    "lecIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mpoaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1)
)
mpoaMIB.setRevisions(
        ("1998-11-09 00:00",
         "1998-05-22 00:00",
         "1998-02-25 00:00")
)


# Types definitions



class AtmAddr(OctetString):
    """Custom type AtmAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(13, 13),
        ValueSizeConstraint(20, 20),
    )




# TEXTUAL-CONVENTIONS



class LecIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class AtmConfigAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(20, 20),
    )



class InternetworkAddrType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 12),
          ("banyanVines", 14),
          ("bbn1822", 5),
          ("decnetIV", 13),
          ("e163", 7),
          ("e164", 8),
          ("e164WithNsap", 15),
          ("f69", 9),
          ("hdlc", 4),
          ("ieee802", 6),
          ("ipV4", 1),
          ("ipV6", 2),
          ("ipx", 11),
          ("nsap", 3),
          ("other", 0),
          ("x121", 10))
    )



class InternetworkAddr(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )



class MpcIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class MpsIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfMpoa_ObjectIdentity = ObjectIdentity
atmfMpoa = _AtmfMpoa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8)
)
_MpoaMIBObjects_ObjectIdentity = ObjectIdentity
mpoaMIBObjects = _MpoaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1)
)
_MpoaCommonObjects_ObjectIdentity = ObjectIdentity
mpoaCommonObjects = _MpoaCommonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 1)
)
_MpcObjects_ObjectIdentity = ObjectIdentity
mpcObjects = _MpcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2)
)


class _MpcNextIndex_Type(Integer32):
    """Custom type mpcNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MpcNextIndex_Type.__name__ = "Integer32"
_MpcNextIndex_Object = MibScalar
mpcNextIndex = _MpcNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 1),
    _MpcNextIndex_Type()
)
mpcNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpcNextIndex.setStatus("current")
_MpcConfigTable_Object = MibTable
mpcConfigTable = _MpcConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    mpcConfigTable.setStatus("current")
_MpcConfigEntry_Object = MibTableRow
mpcConfigEntry = _MpcConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1)
)
mpcConfigEntry.setIndexNames(
    (0, "MPC-MIB", "mpcIndex"),
)
if mibBuilder.loadTexts:
    mpcConfigEntry.setStatus("current")
_MpcIndex_Type = MpcIndex
_MpcIndex_Object = MibTableColumn
mpcIndex = _MpcIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 1),
    _MpcIndex_Type()
)
mpcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpcIndex.setStatus("current")
_MpcRowStatus_Type = RowStatus
_MpcRowStatus_Object = MibTableColumn
mpcRowStatus = _MpcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 2),
    _MpcRowStatus_Type()
)
mpcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpcRowStatus.setStatus("current")


class _MpcConfigMode_Type(Integer32):
    """Custom type mpcConfigMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_MpcConfigMode_Type.__name__ = "Integer32"
_MpcConfigMode_Object = MibTableColumn
mpcConfigMode = _MpcConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 3),
    _MpcConfigMode_Type()
)
mpcConfigMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpcConfigMode.setStatus("current")
_MpcCtrlAtmAddr_Type = AtmConfigAddr
_MpcCtrlAtmAddr_Object = MibTableColumn
mpcCtrlAtmAddr = _MpcCtrlAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 4),
    _MpcCtrlAtmAddr_Type()
)
mpcCtrlAtmAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpcCtrlAtmAddr.setStatus("current")


class _MpcSCSetupFrameCount_Type(Integer32):
    """Custom type mpcSCSetupFrameCount based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpcSCSetupFrameCount_Type.__name__ = "Integer32"
_MpcSCSetupFrameCount_Object = MibTableColumn
mpcSCSetupFrameCount = _MpcSCSetupFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 5),
    _MpcSCSetupFrameCount_Type()
)
mpcSCSetupFrameCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpcSCSetupFrameCount.setStatus("current")


class _MpcSCSetupFrameTime_Type(Integer32):
    """Custom type mpcSCSetupFrameTime based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_MpcSCSetupFrameTime_Type.__name__ = "Integer32"
_MpcSCSetupFrameTime_Object = MibTableColumn
mpcSCSetupFrameTime = _MpcSCSetupFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 6),
    _MpcSCSetupFrameTime_Type()
)
mpcSCSetupFrameTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpcSCSetupFrameTime.setStatus("current")


class _MpcInitialRetryTime_Type(Integer32):
    """Custom type mpcInitialRetryTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_MpcInitialRetryTime_Type.__name__ = "Integer32"
_MpcInitialRetryTime_Object = MibTableColumn
mpcInitialRetryTime = _MpcInitialRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 7),
    _MpcInitialRetryTime_Type()
)
mpcInitialRetryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpcInitialRetryTime.setStatus("current")


class _MpcRetryTimeMaximum_Type(Integer32):
    """Custom type mpcRetryTimeMaximum based on Integer32"""
    defaultValue = 40

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_MpcRetryTimeMaximum_Type.__name__ = "Integer32"
_MpcRetryTimeMaximum_Object = MibTableColumn
mpcRetryTimeMaximum = _MpcRetryTimeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 8),
    _MpcRetryTimeMaximum_Type()
)
mpcRetryTimeMaximum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpcRetryTimeMaximum.setStatus("current")


class _MpcHoldDownTime_Type(Integer32):
    """Custom type mpcHoldDownTime based on Integer32"""
    defaultValue = 160

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1200),
    )


_MpcHoldDownTime_Type.__name__ = "Integer32"
_MpcHoldDownTime_Object = MibTableColumn
mpcHoldDownTime = _MpcHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 2, 1, 9),
    _MpcHoldDownTime_Type()
)
mpcHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mpcHoldDownTime.setStatus("current")
_MpcActualTable_Object = MibTable
mpcActualTable = _MpcActualTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    mpcActualTable.setStatus("current")
_MpcActualEntry_Object = MibTableRow
mpcActualEntry = _MpcActualEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mpcActualEntry.setStatus("current")


class _MpcActualState_Type(Integer32):
    """Custom type mpcActualState based on Integer32"""
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
        *(("down", 4),
          ("initialState", 2),
          ("unknown", 1),
          ("up", 3))
    )


_MpcActualState_Type.__name__ = "Integer32"
_MpcActualState_Object = MibTableColumn
mpcActualState = _MpcActualState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 1),
    _MpcActualState_Type()
)
mpcActualState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualState.setStatus("current")
_MpcDiscontinuityTime_Type = TimeStamp
_MpcDiscontinuityTime_Object = MibTableColumn
mpcDiscontinuityTime = _MpcDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 2),
    _MpcDiscontinuityTime_Type()
)
mpcDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcDiscontinuityTime.setStatus("current")


class _MpcActualConfigMode_Type(Integer32):
    """Custom type mpcActualConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_MpcActualConfigMode_Type.__name__ = "Integer32"
_MpcActualConfigMode_Object = MibTableColumn
mpcActualConfigMode = _MpcActualConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 3),
    _MpcActualConfigMode_Type()
)
mpcActualConfigMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualConfigMode.setStatus("current")


class _MpcActualSCSetupFrameCount_Type(Integer32):
    """Custom type mpcActualSCSetupFrameCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MpcActualSCSetupFrameCount_Type.__name__ = "Integer32"
_MpcActualSCSetupFrameCount_Object = MibTableColumn
mpcActualSCSetupFrameCount = _MpcActualSCSetupFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 4),
    _MpcActualSCSetupFrameCount_Type()
)
mpcActualSCSetupFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualSCSetupFrameCount.setStatus("current")


class _MpcActualSCSetupFrameTime_Type(Integer32):
    """Custom type mpcActualSCSetupFrameTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_MpcActualSCSetupFrameTime_Type.__name__ = "Integer32"
_MpcActualSCSetupFrameTime_Object = MibTableColumn
mpcActualSCSetupFrameTime = _MpcActualSCSetupFrameTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 5),
    _MpcActualSCSetupFrameTime_Type()
)
mpcActualSCSetupFrameTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualSCSetupFrameTime.setStatus("current")


class _MpcActualInitialRetryTime_Type(Integer32):
    """Custom type mpcActualInitialRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_MpcActualInitialRetryTime_Type.__name__ = "Integer32"
_MpcActualInitialRetryTime_Object = MibTableColumn
mpcActualInitialRetryTime = _MpcActualInitialRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 6),
    _MpcActualInitialRetryTime_Type()
)
mpcActualInitialRetryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualInitialRetryTime.setStatus("current")


class _MpcActualRetryTimeMaximum_Type(Integer32):
    """Custom type mpcActualRetryTimeMaximum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_MpcActualRetryTimeMaximum_Type.__name__ = "Integer32"
_MpcActualRetryTimeMaximum_Object = MibTableColumn
mpcActualRetryTimeMaximum = _MpcActualRetryTimeMaximum_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 7),
    _MpcActualRetryTimeMaximum_Type()
)
mpcActualRetryTimeMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualRetryTimeMaximum.setStatus("current")


class _MpcActualHoldDownTime_Type(Integer32):
    """Custom type mpcActualHoldDownTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1200),
    )


_MpcActualHoldDownTime_Type.__name__ = "Integer32"
_MpcActualHoldDownTime_Object = MibTableColumn
mpcActualHoldDownTime = _MpcActualHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 3, 1, 8),
    _MpcActualHoldDownTime_Type()
)
mpcActualHoldDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcActualHoldDownTime.setStatus("current")
_MpcStatisticsTable_Object = MibTable
mpcStatisticsTable = _MpcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    mpcStatisticsTable.setStatus("current")
_MpcStatisticsEntry_Object = MibTableRow
mpcStatisticsEntry = _MpcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    mpcStatisticsEntry.setStatus("current")
_MpcStatTxMpoaResolveRequests_Type = Counter32
_MpcStatTxMpoaResolveRequests_Object = MibTableColumn
mpcStatTxMpoaResolveRequests = _MpcStatTxMpoaResolveRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 1),
    _MpcStatTxMpoaResolveRequests_Type()
)
mpcStatTxMpoaResolveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaResolveRequests.setStatus("current")
_MpcStatRxMpoaResolveReplyAcks_Type = Counter32
_MpcStatRxMpoaResolveReplyAcks_Object = MibTableColumn
mpcStatRxMpoaResolveReplyAcks = _MpcStatRxMpoaResolveReplyAcks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 2),
    _MpcStatRxMpoaResolveReplyAcks_Type()
)
mpcStatRxMpoaResolveReplyAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyAcks.setStatus("current")
_MpcStatRxMpoaResolveReplyInsufECResources_Type = Counter32
_MpcStatRxMpoaResolveReplyInsufECResources_Object = MibTableColumn
mpcStatRxMpoaResolveReplyInsufECResources = _MpcStatRxMpoaResolveReplyInsufECResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 3),
    _MpcStatRxMpoaResolveReplyInsufECResources_Type()
)
mpcStatRxMpoaResolveReplyInsufECResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyInsufECResources.setStatus("current")
_MpcStatRxMpoaResolveReplyInsufSCResources_Type = Counter32
_MpcStatRxMpoaResolveReplyInsufSCResources_Object = MibTableColumn
mpcStatRxMpoaResolveReplyInsufSCResources = _MpcStatRxMpoaResolveReplyInsufSCResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 4),
    _MpcStatRxMpoaResolveReplyInsufSCResources_Type()
)
mpcStatRxMpoaResolveReplyInsufSCResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyInsufSCResources.setStatus("current")
_MpcStatRxMpoaResolveReplyInsufEitherResources_Type = Counter32
_MpcStatRxMpoaResolveReplyInsufEitherResources_Object = MibTableColumn
mpcStatRxMpoaResolveReplyInsufEitherResources = _MpcStatRxMpoaResolveReplyInsufEitherResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 5),
    _MpcStatRxMpoaResolveReplyInsufEitherResources_Type()
)
mpcStatRxMpoaResolveReplyInsufEitherResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyInsufEitherResources.setStatus("current")
_MpcStatRxMpoaResolveReplyUnsupportedInetProt_Type = Counter32
_MpcStatRxMpoaResolveReplyUnsupportedInetProt_Object = MibTableColumn
mpcStatRxMpoaResolveReplyUnsupportedInetProt = _MpcStatRxMpoaResolveReplyUnsupportedInetProt_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 6),
    _MpcStatRxMpoaResolveReplyUnsupportedInetProt_Type()
)
mpcStatRxMpoaResolveReplyUnsupportedInetProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyUnsupportedInetProt.setStatus("current")
_MpcStatRxMpoaResolveReplyUnsupportedMacEncaps_Type = Counter32
_MpcStatRxMpoaResolveReplyUnsupportedMacEncaps_Object = MibTableColumn
mpcStatRxMpoaResolveReplyUnsupportedMacEncaps = _MpcStatRxMpoaResolveReplyUnsupportedMacEncaps_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 7),
    _MpcStatRxMpoaResolveReplyUnsupportedMacEncaps_Type()
)
mpcStatRxMpoaResolveReplyUnsupportedMacEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyUnsupportedMacEncaps.setStatus("current")
_MpcStatRxMpoaResolveReplyUnspecifiedOther_Type = Counter32
_MpcStatRxMpoaResolveReplyUnspecifiedOther_Object = MibTableColumn
mpcStatRxMpoaResolveReplyUnspecifiedOther = _MpcStatRxMpoaResolveReplyUnspecifiedOther_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 8),
    _MpcStatRxMpoaResolveReplyUnspecifiedOther_Type()
)
mpcStatRxMpoaResolveReplyUnspecifiedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaResolveReplyUnspecifiedOther.setStatus("current")
_MpcStatRxMpoaImpRequests_Type = Counter32
_MpcStatRxMpoaImpRequests_Object = MibTableColumn
mpcStatRxMpoaImpRequests = _MpcStatRxMpoaImpRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 9),
    _MpcStatRxMpoaImpRequests_Type()
)
mpcStatRxMpoaImpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaImpRequests.setStatus("current")
_MpcStatTxMpoaImpReplyAcks_Type = Counter32
_MpcStatTxMpoaImpReplyAcks_Object = MibTableColumn
mpcStatTxMpoaImpReplyAcks = _MpcStatTxMpoaImpReplyAcks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 10),
    _MpcStatTxMpoaImpReplyAcks_Type()
)
mpcStatTxMpoaImpReplyAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyAcks.setStatus("current")
_MpcStatTxMpoaImpReplyInsufECResources_Type = Counter32
_MpcStatTxMpoaImpReplyInsufECResources_Object = MibTableColumn
mpcStatTxMpoaImpReplyInsufECResources = _MpcStatTxMpoaImpReplyInsufECResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 11),
    _MpcStatTxMpoaImpReplyInsufECResources_Type()
)
mpcStatTxMpoaImpReplyInsufECResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyInsufECResources.setStatus("current")
_MpcStatTxMpoaImpReplyInsufSCResources_Type = Counter32
_MpcStatTxMpoaImpReplyInsufSCResources_Object = MibTableColumn
mpcStatTxMpoaImpReplyInsufSCResources = _MpcStatTxMpoaImpReplyInsufSCResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 12),
    _MpcStatTxMpoaImpReplyInsufSCResources_Type()
)
mpcStatTxMpoaImpReplyInsufSCResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyInsufSCResources.setStatus("current")
_MpcStatTxMpoaImpReplyInsufEitherResources_Type = Counter32
_MpcStatTxMpoaImpReplyInsufEitherResources_Object = MibTableColumn
mpcStatTxMpoaImpReplyInsufEitherResources = _MpcStatTxMpoaImpReplyInsufEitherResources_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 13),
    _MpcStatTxMpoaImpReplyInsufEitherResources_Type()
)
mpcStatTxMpoaImpReplyInsufEitherResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyInsufEitherResources.setStatus("current")
_MpcStatTxMpoaImpReplyUnsupportedInetProt_Type = Counter32
_MpcStatTxMpoaImpReplyUnsupportedInetProt_Object = MibTableColumn
mpcStatTxMpoaImpReplyUnsupportedInetProt = _MpcStatTxMpoaImpReplyUnsupportedInetProt_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 14),
    _MpcStatTxMpoaImpReplyUnsupportedInetProt_Type()
)
mpcStatTxMpoaImpReplyUnsupportedInetProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyUnsupportedInetProt.setStatus("current")
_MpcStatTxMpoaImpReplyUnsupportedMacEncaps_Type = Counter32
_MpcStatTxMpoaImpReplyUnsupportedMacEncaps_Object = MibTableColumn
mpcStatTxMpoaImpReplyUnsupportedMacEncaps = _MpcStatTxMpoaImpReplyUnsupportedMacEncaps_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 15),
    _MpcStatTxMpoaImpReplyUnsupportedMacEncaps_Type()
)
mpcStatTxMpoaImpReplyUnsupportedMacEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyUnsupportedMacEncaps.setStatus("current")
_MpcStatTxMpoaImpReplyUnspecifiedOther_Type = Counter32
_MpcStatTxMpoaImpReplyUnspecifiedOther_Object = MibTableColumn
mpcStatTxMpoaImpReplyUnspecifiedOther = _MpcStatTxMpoaImpReplyUnspecifiedOther_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 16),
    _MpcStatTxMpoaImpReplyUnspecifiedOther_Type()
)
mpcStatTxMpoaImpReplyUnspecifiedOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaImpReplyUnspecifiedOther.setStatus("current")
_MpcStatTxMpoaEgressCachePurgeRequests_Type = Counter32
_MpcStatTxMpoaEgressCachePurgeRequests_Object = MibTableColumn
mpcStatTxMpoaEgressCachePurgeRequests = _MpcStatTxMpoaEgressCachePurgeRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 17),
    _MpcStatTxMpoaEgressCachePurgeRequests_Type()
)
mpcStatTxMpoaEgressCachePurgeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaEgressCachePurgeRequests.setStatus("current")
_MpcStatRxMpoaEgressCachePurgeReplies_Type = Counter32
_MpcStatRxMpoaEgressCachePurgeReplies_Object = MibTableColumn
mpcStatRxMpoaEgressCachePurgeReplies = _MpcStatRxMpoaEgressCachePurgeReplies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 18),
    _MpcStatRxMpoaEgressCachePurgeReplies_Type()
)
mpcStatRxMpoaEgressCachePurgeReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaEgressCachePurgeReplies.setStatus("current")
_MpcStatRxMpoaKeepAlives_Type = Counter32
_MpcStatRxMpoaKeepAlives_Object = MibTableColumn
mpcStatRxMpoaKeepAlives = _MpcStatRxMpoaKeepAlives_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 19),
    _MpcStatRxMpoaKeepAlives_Type()
)
mpcStatRxMpoaKeepAlives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaKeepAlives.setStatus("current")
_MpcStatRxMpoaTriggers_Type = Counter32
_MpcStatRxMpoaTriggers_Object = MibTableColumn
mpcStatRxMpoaTriggers = _MpcStatRxMpoaTriggers_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 20),
    _MpcStatRxMpoaTriggers_Type()
)
mpcStatRxMpoaTriggers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaTriggers.setStatus("current")
_MpcStatRxMpoaDataPlanePurges_Type = Counter32
_MpcStatRxMpoaDataPlanePurges_Object = MibTableColumn
mpcStatRxMpoaDataPlanePurges = _MpcStatRxMpoaDataPlanePurges_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 21),
    _MpcStatRxMpoaDataPlanePurges_Type()
)
mpcStatRxMpoaDataPlanePurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxMpoaDataPlanePurges.setStatus("current")
_MpcStatTxMpoaDataPlanePurges_Type = Counter32
_MpcStatTxMpoaDataPlanePurges_Object = MibTableColumn
mpcStatTxMpoaDataPlanePurges = _MpcStatTxMpoaDataPlanePurges_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 22),
    _MpcStatTxMpoaDataPlanePurges_Type()
)
mpcStatTxMpoaDataPlanePurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxMpoaDataPlanePurges.setStatus("current")
_MpcStatRxNhrpPurgeRequests_Type = Counter32
_MpcStatRxNhrpPurgeRequests_Object = MibTableColumn
mpcStatRxNhrpPurgeRequests = _MpcStatRxNhrpPurgeRequests_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 23),
    _MpcStatRxNhrpPurgeRequests_Type()
)
mpcStatRxNhrpPurgeRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxNhrpPurgeRequests.setStatus("current")
_MpcStatTxNhrpPurgeReplies_Type = Counter32
_MpcStatTxNhrpPurgeReplies_Object = MibTableColumn
mpcStatTxNhrpPurgeReplies = _MpcStatTxNhrpPurgeReplies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 24),
    _MpcStatTxNhrpPurgeReplies_Type()
)
mpcStatTxNhrpPurgeReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatTxNhrpPurgeReplies.setStatus("current")
_MpcStatRxErrUnrecognizedExtensions_Type = Counter32
_MpcStatRxErrUnrecognizedExtensions_Object = MibTableColumn
mpcStatRxErrUnrecognizedExtensions = _MpcStatRxErrUnrecognizedExtensions_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 25),
    _MpcStatRxErrUnrecognizedExtensions_Type()
)
mpcStatRxErrUnrecognizedExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrUnrecognizedExtensions.setStatus("current")
_MpcStatRxErrLoopDetecteds_Type = Counter32
_MpcStatRxErrLoopDetecteds_Object = MibTableColumn
mpcStatRxErrLoopDetecteds = _MpcStatRxErrLoopDetecteds_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 26),
    _MpcStatRxErrLoopDetecteds_Type()
)
mpcStatRxErrLoopDetecteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrLoopDetecteds.setStatus("current")
_MpcStatRxErrProtoAddrUnreachables_Type = Counter32
_MpcStatRxErrProtoAddrUnreachables_Object = MibTableColumn
mpcStatRxErrProtoAddrUnreachables = _MpcStatRxErrProtoAddrUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 27),
    _MpcStatRxErrProtoAddrUnreachables_Type()
)
mpcStatRxErrProtoAddrUnreachables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrProtoAddrUnreachables.setStatus("current")
_MpcStatRxErrProtoErrors_Type = Counter32
_MpcStatRxErrProtoErrors_Object = MibTableColumn
mpcStatRxErrProtoErrors = _MpcStatRxErrProtoErrors_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 28),
    _MpcStatRxErrProtoErrors_Type()
)
mpcStatRxErrProtoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrProtoErrors.setStatus("current")
_MpcStatRxErrSduSizeExceededs_Type = Counter32
_MpcStatRxErrSduSizeExceededs_Object = MibTableColumn
mpcStatRxErrSduSizeExceededs = _MpcStatRxErrSduSizeExceededs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 29),
    _MpcStatRxErrSduSizeExceededs_Type()
)
mpcStatRxErrSduSizeExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrSduSizeExceededs.setStatus("current")
_MpcStatRxErrInvalidExtensions_Type = Counter32
_MpcStatRxErrInvalidExtensions_Object = MibTableColumn
mpcStatRxErrInvalidExtensions = _MpcStatRxErrInvalidExtensions_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 30),
    _MpcStatRxErrInvalidExtensions_Type()
)
mpcStatRxErrInvalidExtensions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrInvalidExtensions.setStatus("current")
_MpcStatRxErrInvalidReplies_Type = Counter32
_MpcStatRxErrInvalidReplies_Object = MibTableColumn
mpcStatRxErrInvalidReplies = _MpcStatRxErrInvalidReplies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 31),
    _MpcStatRxErrInvalidReplies_Type()
)
mpcStatRxErrInvalidReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrInvalidReplies.setStatus("current")
_MpcStatRxErrAuthenticationFailures_Type = Counter32
_MpcStatRxErrAuthenticationFailures_Object = MibTableColumn
mpcStatRxErrAuthenticationFailures = _MpcStatRxErrAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 32),
    _MpcStatRxErrAuthenticationFailures_Type()
)
mpcStatRxErrAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrAuthenticationFailures.setStatus("current")
_MpcStatRxErrHopCountExceededs_Type = Counter32
_MpcStatRxErrHopCountExceededs_Object = MibTableColumn
mpcStatRxErrHopCountExceededs = _MpcStatRxErrHopCountExceededs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 5, 1, 33),
    _MpcStatRxErrHopCountExceededs_Type()
)
mpcStatRxErrHopCountExceededs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcStatRxErrHopCountExceededs.setStatus("current")
_MpcMpsTable_Object = MibTable
mpcMpsTable = _MpcMpsTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    mpcMpsTable.setStatus("current")
_MpcMpsEntry_Object = MibTableRow
mpcMpsEntry = _MpcMpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 8, 1)
)
mpcMpsEntry.setIndexNames(
    (0, "MPC-MIB", "mpcMpsIndex"),
)
if mibBuilder.loadTexts:
    mpcMpsEntry.setStatus("current")
_MpcMpsIndex_Type = MpsIndex
_MpcMpsIndex_Object = MibTableColumn
mpcMpsIndex = _MpcMpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 8, 1, 1),
    _MpcMpsIndex_Type()
)
mpcMpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpcMpsIndex.setStatus("current")
_MpcMpsAtmAddr_Type = AtmAddr
_MpcMpsAtmAddr_Object = MibTableColumn
mpcMpsAtmAddr = _MpcMpsAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 8, 1, 2),
    _MpcMpsAtmAddr_Type()
)
mpcMpsAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcMpsAtmAddr.setStatus("current")
_MpcIngressCacheTable_Object = MibTable
mpcIngressCacheTable = _MpcIngressCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12)
)
if mibBuilder.loadTexts:
    mpcIngressCacheTable.setStatus("current")
_MpcIngressCacheEntry_Object = MibTableRow
mpcIngressCacheEntry = _MpcIngressCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1)
)
mpcIngressCacheEntry.setIndexNames(
    (0, "MPC-MIB", "mpcIngressCacheDestInetworkAddrType"),
    (0, "MPC-MIB", "mpcIngressCacheDestAddr"),
    (0, "MPC-MIB", "mpcIndex"),
    (0, "MPC-MIB", "mpcMpsIndex"),
)
if mibBuilder.loadTexts:
    mpcIngressCacheEntry.setStatus("current")
_MpcIngressCacheDestInetworkAddrType_Type = InternetworkAddrType
_MpcIngressCacheDestInetworkAddrType_Object = MibTableColumn
mpcIngressCacheDestInetworkAddrType = _MpcIngressCacheDestInetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 1),
    _MpcIngressCacheDestInetworkAddrType_Type()
)
mpcIngressCacheDestInetworkAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheDestInetworkAddrType.setStatus("current")
_MpcIngressCacheDestAddr_Type = InternetworkAddr
_MpcIngressCacheDestAddr_Object = MibTableColumn
mpcIngressCacheDestAddr = _MpcIngressCacheDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 2),
    _MpcIngressCacheDestAddr_Type()
)
mpcIngressCacheDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheDestAddr.setStatus("current")
_MpcIngressCachePrefixLen_Type = Integer32
_MpcIngressCachePrefixLen_Object = MibTableColumn
mpcIngressCachePrefixLen = _MpcIngressCachePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 3),
    _MpcIngressCachePrefixLen_Type()
)
mpcIngressCachePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCachePrefixLen.setStatus("current")
_MpcIngressCacheDestAtmAddr_Type = AtmAddr
_MpcIngressCacheDestAtmAddr_Object = MibTableColumn
mpcIngressCacheDestAtmAddr = _MpcIngressCacheDestAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 4),
    _MpcIngressCacheDestAtmAddr_Type()
)
mpcIngressCacheDestAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheDestAtmAddr.setStatus("current")
_MpcIngressCacheSrcAtmAddr_Type = AtmAddr
_MpcIngressCacheSrcAtmAddr_Object = MibTableColumn
mpcIngressCacheSrcAtmAddr = _MpcIngressCacheSrcAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 5),
    _MpcIngressCacheSrcAtmAddr_Type()
)
mpcIngressCacheSrcAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheSrcAtmAddr.setStatus("current")


class _MpcIngressCacheEntryState_Type(Integer32):
    """Custom type mpcIngressCacheEntryState based on Integer32"""
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
        *(("active", 3),
          ("doesNotExist", 1),
          ("inactive", 2),
          ("negative", 4))
    )


_MpcIngressCacheEntryState_Type.__name__ = "Integer32"
_MpcIngressCacheEntryState_Object = MibTableColumn
mpcIngressCacheEntryState = _MpcIngressCacheEntryState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 6),
    _MpcIngressCacheEntryState_Type()
)
mpcIngressCacheEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheEntryState.setStatus("current")
_MpcIngressCacheEgressCacheTagValid_Type = TruthValue
_MpcIngressCacheEgressCacheTagValid_Object = MibTableColumn
mpcIngressCacheEgressCacheTagValid = _MpcIngressCacheEgressCacheTagValid_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 7),
    _MpcIngressCacheEgressCacheTagValid_Type()
)
mpcIngressCacheEgressCacheTagValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheEgressCacheTagValid.setStatus("current")
_MpcIngressCacheEgressCacheTag_Type = Integer32
_MpcIngressCacheEgressCacheTag_Object = MibTableColumn
mpcIngressCacheEgressCacheTag = _MpcIngressCacheEgressCacheTag_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 8),
    _MpcIngressCacheEgressCacheTag_Type()
)
mpcIngressCacheEgressCacheTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheEgressCacheTag.setStatus("current")


class _MpcIngressCacheLastNhrpCieCode_Type(Integer32):
    """Custom type mpcIngressCacheLastNhrpCieCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MpcIngressCacheLastNhrpCieCode_Type.__name__ = "Integer32"
_MpcIngressCacheLastNhrpCieCode_Object = MibTableColumn
mpcIngressCacheLastNhrpCieCode = _MpcIngressCacheLastNhrpCieCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 9),
    _MpcIngressCacheLastNhrpCieCode_Type()
)
mpcIngressCacheLastNhrpCieCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheLastNhrpCieCode.setStatus("current")
_MpcIngressCacheSigErrCode_Type = Integer32
_MpcIngressCacheSigErrCode_Object = MibTableColumn
mpcIngressCacheSigErrCode = _MpcIngressCacheSigErrCode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 10),
    _MpcIngressCacheSigErrCode_Type()
)
mpcIngressCacheSigErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheSigErrCode.setStatus("current")
_MpcIngressCacheRetries_Type = Counter32
_MpcIngressCacheRetries_Object = MibTableColumn
mpcIngressCacheRetries = _MpcIngressCacheRetries_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 11),
    _MpcIngressCacheRetries_Type()
)
mpcIngressCacheRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheRetries.setStatus("current")
_MpcIngressCacheTimeUntilNextResolutionRequest_Type = TimeInterval
_MpcIngressCacheTimeUntilNextResolutionRequest_Object = MibTableColumn
mpcIngressCacheTimeUntilNextResolutionRequest = _MpcIngressCacheTimeUntilNextResolutionRequest_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 12),
    _MpcIngressCacheTimeUntilNextResolutionRequest_Type()
)
mpcIngressCacheTimeUntilNextResolutionRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheTimeUntilNextResolutionRequest.setStatus("current")
_MpcIngressCacheHoldingTime_Type = TimeInterval
_MpcIngressCacheHoldingTime_Object = MibTableColumn
mpcIngressCacheHoldingTime = _MpcIngressCacheHoldingTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 13),
    _MpcIngressCacheHoldingTime_Type()
)
mpcIngressCacheHoldingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheHoldingTime.setStatus("current")


class _MpcIngressCacheServiceCategory_Type(Integer32):
    """Custom type mpcIngressCacheServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpcIngressCacheServiceCategory_Type.__name__ = "Integer32"
_MpcIngressCacheServiceCategory_Object = MibTableColumn
mpcIngressCacheServiceCategory = _MpcIngressCacheServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 12, 1, 14),
    _MpcIngressCacheServiceCategory_Type()
)
mpcIngressCacheServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcIngressCacheServiceCategory.setStatus("current")
_MpcEgressCacheTable_Object = MibTable
mpcEgressCacheTable = _MpcEgressCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15)
)
if mibBuilder.loadTexts:
    mpcEgressCacheTable.setStatus("current")
_MpcEgressCacheEntry_Object = MibTableRow
mpcEgressCacheEntry = _MpcEgressCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1)
)
mpcEgressCacheEntry.setIndexNames(
    (0, "MPC-MIB", "mpcEgressCacheId"),
    (0, "MPC-MIB", "mpcIndex"),
    (0, "MPC-MIB", "mpcMpsIndex"),
)
if mibBuilder.loadTexts:
    mpcEgressCacheEntry.setStatus("current")


class _MpcEgressCacheId_Type(Integer32):
    """Custom type mpcEgressCacheId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MpcEgressCacheId_Type.__name__ = "Integer32"
_MpcEgressCacheId_Object = MibTableColumn
mpcEgressCacheId = _MpcEgressCacheId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 1),
    _MpcEgressCacheId_Type()
)
mpcEgressCacheId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheId.setStatus("current")
_MpcEgressCacheInetworkAddrType_Type = InternetworkAddrType
_MpcEgressCacheInetworkAddrType_Object = MibTableColumn
mpcEgressCacheInetworkAddrType = _MpcEgressCacheInetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 2),
    _MpcEgressCacheInetworkAddrType_Type()
)
mpcEgressCacheInetworkAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheInetworkAddrType.setStatus("current")
_MpcEgressCacheIDestAddr_Type = InternetworkAddr
_MpcEgressCacheIDestAddr_Object = MibTableColumn
mpcEgressCacheIDestAddr = _MpcEgressCacheIDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 3),
    _MpcEgressCacheIDestAddr_Type()
)
mpcEgressCacheIDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheIDestAddr.setStatus("current")
_MpcEgressCachePrefixLen_Type = Integer32
_MpcEgressCachePrefixLen_Object = MibTableColumn
mpcEgressCachePrefixLen = _MpcEgressCachePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 4),
    _MpcEgressCachePrefixLen_Type()
)
mpcEgressCachePrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCachePrefixLen.setStatus("current")


class _MpcEgressCacheEntryState_Type(Integer32):
    """Custom type mpcEgressCacheEntryState based on Integer32"""
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
        *(("active", 3),
          ("doesNotExist", 1),
          ("inactive", 2),
          ("negative", 4))
    )


_MpcEgressCacheEntryState_Type.__name__ = "Integer32"
_MpcEgressCacheEntryState_Object = MibTableColumn
mpcEgressCacheEntryState = _MpcEgressCacheEntryState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 5),
    _MpcEgressCacheEntryState_Type()
)
mpcEgressCacheEntryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheEntryState.setStatus("current")
_MpcEgressCacheEgressCacheTagValid_Type = TruthValue
_MpcEgressCacheEgressCacheTagValid_Object = MibTableColumn
mpcEgressCacheEgressCacheTagValid = _MpcEgressCacheEgressCacheTagValid_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 6),
    _MpcEgressCacheEgressCacheTagValid_Type()
)
mpcEgressCacheEgressCacheTagValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheEgressCacheTagValid.setStatus("current")
_MpcEgressCacheEgressCacheTag_Type = Integer32
_MpcEgressCacheEgressCacheTag_Object = MibTableColumn
mpcEgressCacheEgressCacheTag = _MpcEgressCacheEgressCacheTag_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 7),
    _MpcEgressCacheEgressCacheTag_Type()
)
mpcEgressCacheEgressCacheTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheEgressCacheTag.setStatus("current")
_MpcEgressCacheHoldTime_Type = TimeInterval
_MpcEgressCacheHoldTime_Object = MibTableColumn
mpcEgressCacheHoldTime = _MpcEgressCacheHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 8),
    _MpcEgressCacheHoldTime_Type()
)
mpcEgressCacheHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheHoldTime.setStatus("current")


class _MpcEgressCacheDataLinkHeader_Type(OctetString):
    """Custom type mpcEgressCacheDataLinkHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MpcEgressCacheDataLinkHeader_Type.__name__ = "OctetString"
_MpcEgressCacheDataLinkHeader_Object = MibTableColumn
mpcEgressCacheDataLinkHeader = _MpcEgressCacheDataLinkHeader_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 9),
    _MpcEgressCacheDataLinkHeader_Type()
)
mpcEgressCacheDataLinkHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheDataLinkHeader.setStatus("current")
_MpcEgressCacheIngressMpcDataAtmAddr_Type = AtmAddr
_MpcEgressCacheIngressMpcDataAtmAddr_Object = MibTableColumn
mpcEgressCacheIngressMpcDataAtmAddr = _MpcEgressCacheIngressMpcDataAtmAddr_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 10),
    _MpcEgressCacheIngressMpcDataAtmAddr_Type()
)
mpcEgressCacheIngressMpcDataAtmAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheIngressMpcDataAtmAddr.setStatus("current")
_MpcEgressCacheLecIndex_Type = LecIndex
_MpcEgressCacheLecIndex_Object = MibTableColumn
mpcEgressCacheLecIndex = _MpcEgressCacheLecIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 11),
    _MpcEgressCacheLecIndex_Type()
)
mpcEgressCacheLecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheLecIndex.setStatus("current")


class _MpcEgressCacheServiceCategory_Type(Integer32):
    """Custom type mpcEgressCacheServiceCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MpcEgressCacheServiceCategory_Type.__name__ = "Integer32"
_MpcEgressCacheServiceCategory_Object = MibTableColumn
mpcEgressCacheServiceCategory = _MpcEgressCacheServiceCategory_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 15, 1, 12),
    _MpcEgressCacheServiceCategory_Type()
)
mpcEgressCacheServiceCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpcEgressCacheServiceCategory.setStatus("current")
_MpcMpsObjects_ObjectIdentity = ObjectIdentity
mpcMpsObjects = _MpcMpsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 1, 2, 16)
)
_MpoaMIBConformance_ObjectIdentity = ObjectIdentity
mpoaMIBConformance = _MpoaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2)
)
_MpoaMIBGroups_ObjectIdentity = ObjectIdentity
mpoaMIBGroups = _MpoaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 1)
)
_MpoaMIBCompliances_ObjectIdentity = ObjectIdentity
mpoaMIBCompliances = _MpoaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 8, 1, 2, 2)
)
mpcConfigEntry.registerAugmentions(
    ("MPC-MIB",
     "mpcActualEntry")
)
mpcActualEntry.setIndexNames(*mpcConfigEntry.getIndexNames())
mpcConfigEntry.registerAugmentions(
    ("MPC-MIB",
     "mpcStatisticsEntry")
)
mpcStatisticsEntry.setIndexNames(*mpcConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPC-MIB",
    **{"AtmAddr": AtmAddr,
       "LecIndex": LecIndex,
       "AtmConfigAddr": AtmConfigAddr,
       "InternetworkAddrType": InternetworkAddrType,
       "InternetworkAddr": InternetworkAddr,
       "MpcIndex": MpcIndex,
       "MpsIndex": MpsIndex,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfMpoa": atmfMpoa,
       "mpoaMIB": mpoaMIB,
       "mpoaMIBObjects": mpoaMIBObjects,
       "mpoaCommonObjects": mpoaCommonObjects,
       "mpcObjects": mpcObjects,
       "mpcNextIndex": mpcNextIndex,
       "mpcConfigTable": mpcConfigTable,
       "mpcConfigEntry": mpcConfigEntry,
       "mpcIndex": mpcIndex,
       "mpcRowStatus": mpcRowStatus,
       "mpcConfigMode": mpcConfigMode,
       "mpcCtrlAtmAddr": mpcCtrlAtmAddr,
       "mpcSCSetupFrameCount": mpcSCSetupFrameCount,
       "mpcSCSetupFrameTime": mpcSCSetupFrameTime,
       "mpcInitialRetryTime": mpcInitialRetryTime,
       "mpcRetryTimeMaximum": mpcRetryTimeMaximum,
       "mpcHoldDownTime": mpcHoldDownTime,
       "mpcActualTable": mpcActualTable,
       "mpcActualEntry": mpcActualEntry,
       "mpcActualState": mpcActualState,
       "mpcDiscontinuityTime": mpcDiscontinuityTime,
       "mpcActualConfigMode": mpcActualConfigMode,
       "mpcActualSCSetupFrameCount": mpcActualSCSetupFrameCount,
       "mpcActualSCSetupFrameTime": mpcActualSCSetupFrameTime,
       "mpcActualInitialRetryTime": mpcActualInitialRetryTime,
       "mpcActualRetryTimeMaximum": mpcActualRetryTimeMaximum,
       "mpcActualHoldDownTime": mpcActualHoldDownTime,
       "mpcStatisticsTable": mpcStatisticsTable,
       "mpcStatisticsEntry": mpcStatisticsEntry,
       "mpcStatTxMpoaResolveRequests": mpcStatTxMpoaResolveRequests,
       "mpcStatRxMpoaResolveReplyAcks": mpcStatRxMpoaResolveReplyAcks,
       "mpcStatRxMpoaResolveReplyInsufECResources": mpcStatRxMpoaResolveReplyInsufECResources,
       "mpcStatRxMpoaResolveReplyInsufSCResources": mpcStatRxMpoaResolveReplyInsufSCResources,
       "mpcStatRxMpoaResolveReplyInsufEitherResources": mpcStatRxMpoaResolveReplyInsufEitherResources,
       "mpcStatRxMpoaResolveReplyUnsupportedInetProt": mpcStatRxMpoaResolveReplyUnsupportedInetProt,
       "mpcStatRxMpoaResolveReplyUnsupportedMacEncaps": mpcStatRxMpoaResolveReplyUnsupportedMacEncaps,
       "mpcStatRxMpoaResolveReplyUnspecifiedOther": mpcStatRxMpoaResolveReplyUnspecifiedOther,
       "mpcStatRxMpoaImpRequests": mpcStatRxMpoaImpRequests,
       "mpcStatTxMpoaImpReplyAcks": mpcStatTxMpoaImpReplyAcks,
       "mpcStatTxMpoaImpReplyInsufECResources": mpcStatTxMpoaImpReplyInsufECResources,
       "mpcStatTxMpoaImpReplyInsufSCResources": mpcStatTxMpoaImpReplyInsufSCResources,
       "mpcStatTxMpoaImpReplyInsufEitherResources": mpcStatTxMpoaImpReplyInsufEitherResources,
       "mpcStatTxMpoaImpReplyUnsupportedInetProt": mpcStatTxMpoaImpReplyUnsupportedInetProt,
       "mpcStatTxMpoaImpReplyUnsupportedMacEncaps": mpcStatTxMpoaImpReplyUnsupportedMacEncaps,
       "mpcStatTxMpoaImpReplyUnspecifiedOther": mpcStatTxMpoaImpReplyUnspecifiedOther,
       "mpcStatTxMpoaEgressCachePurgeRequests": mpcStatTxMpoaEgressCachePurgeRequests,
       "mpcStatRxMpoaEgressCachePurgeReplies": mpcStatRxMpoaEgressCachePurgeReplies,
       "mpcStatRxMpoaKeepAlives": mpcStatRxMpoaKeepAlives,
       "mpcStatRxMpoaTriggers": mpcStatRxMpoaTriggers,
       "mpcStatRxMpoaDataPlanePurges": mpcStatRxMpoaDataPlanePurges,
       "mpcStatTxMpoaDataPlanePurges": mpcStatTxMpoaDataPlanePurges,
       "mpcStatRxNhrpPurgeRequests": mpcStatRxNhrpPurgeRequests,
       "mpcStatTxNhrpPurgeReplies": mpcStatTxNhrpPurgeReplies,
       "mpcStatRxErrUnrecognizedExtensions": mpcStatRxErrUnrecognizedExtensions,
       "mpcStatRxErrLoopDetecteds": mpcStatRxErrLoopDetecteds,
       "mpcStatRxErrProtoAddrUnreachables": mpcStatRxErrProtoAddrUnreachables,
       "mpcStatRxErrProtoErrors": mpcStatRxErrProtoErrors,
       "mpcStatRxErrSduSizeExceededs": mpcStatRxErrSduSizeExceededs,
       "mpcStatRxErrInvalidExtensions": mpcStatRxErrInvalidExtensions,
       "mpcStatRxErrInvalidReplies": mpcStatRxErrInvalidReplies,
       "mpcStatRxErrAuthenticationFailures": mpcStatRxErrAuthenticationFailures,
       "mpcStatRxErrHopCountExceededs": mpcStatRxErrHopCountExceededs,
       "mpcMpsTable": mpcMpsTable,
       "mpcMpsEntry": mpcMpsEntry,
       "mpcMpsIndex": mpcMpsIndex,
       "mpcMpsAtmAddr": mpcMpsAtmAddr,
       "mpcIngressCacheTable": mpcIngressCacheTable,
       "mpcIngressCacheEntry": mpcIngressCacheEntry,
       "mpcIngressCacheDestInetworkAddrType": mpcIngressCacheDestInetworkAddrType,
       "mpcIngressCacheDestAddr": mpcIngressCacheDestAddr,
       "mpcIngressCachePrefixLen": mpcIngressCachePrefixLen,
       "mpcIngressCacheDestAtmAddr": mpcIngressCacheDestAtmAddr,
       "mpcIngressCacheSrcAtmAddr": mpcIngressCacheSrcAtmAddr,
       "mpcIngressCacheEntryState": mpcIngressCacheEntryState,
       "mpcIngressCacheEgressCacheTagValid": mpcIngressCacheEgressCacheTagValid,
       "mpcIngressCacheEgressCacheTag": mpcIngressCacheEgressCacheTag,
       "mpcIngressCacheLastNhrpCieCode": mpcIngressCacheLastNhrpCieCode,
       "mpcIngressCacheSigErrCode": mpcIngressCacheSigErrCode,
       "mpcIngressCacheRetries": mpcIngressCacheRetries,
       "mpcIngressCacheTimeUntilNextResolutionRequest": mpcIngressCacheTimeUntilNextResolutionRequest,
       "mpcIngressCacheHoldingTime": mpcIngressCacheHoldingTime,
       "mpcIngressCacheServiceCategory": mpcIngressCacheServiceCategory,
       "mpcEgressCacheTable": mpcEgressCacheTable,
       "mpcEgressCacheEntry": mpcEgressCacheEntry,
       "mpcEgressCacheId": mpcEgressCacheId,
       "mpcEgressCacheInetworkAddrType": mpcEgressCacheInetworkAddrType,
       "mpcEgressCacheIDestAddr": mpcEgressCacheIDestAddr,
       "mpcEgressCachePrefixLen": mpcEgressCachePrefixLen,
       "mpcEgressCacheEntryState": mpcEgressCacheEntryState,
       "mpcEgressCacheEgressCacheTagValid": mpcEgressCacheEgressCacheTagValid,
       "mpcEgressCacheEgressCacheTag": mpcEgressCacheEgressCacheTag,
       "mpcEgressCacheHoldTime": mpcEgressCacheHoldTime,
       "mpcEgressCacheDataLinkHeader": mpcEgressCacheDataLinkHeader,
       "mpcEgressCacheIngressMpcDataAtmAddr": mpcEgressCacheIngressMpcDataAtmAddr,
       "mpcEgressCacheLecIndex": mpcEgressCacheLecIndex,
       "mpcEgressCacheServiceCategory": mpcEgressCacheServiceCategory,
       "mpcMpsObjects": mpcMpsObjects,
       "mpoaMIBConformance": mpoaMIBConformance,
       "mpoaMIBGroups": mpoaMIBGroups,
       "mpoaMIBCompliances": mpoaMIBCompliances}
)
