# SNMP MIB module (XYLAN-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLAN-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:09 2024
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

(xylanNtpArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanNtpArch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XylanNtpConfig_ObjectIdentity = ObjectIdentity
xylanNtpConfig = _XylanNtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1)
)


class _XylanNtpEnable_Type(Integer32):
    """Custom type xylanNtpEnable based on Integer32"""
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


_XylanNtpEnable_Type.__name__ = "Integer32"
_XylanNtpEnable_Object = MibScalar
xylanNtpEnable = _XylanNtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 1),
    _XylanNtpEnable_Type()
)
xylanNtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpEnable.setStatus("mandatory")


class _XylanNtpMonitorEnable_Type(Integer32):
    """Custom type xylanNtpMonitorEnable based on Integer32"""
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


_XylanNtpMonitorEnable_Type.__name__ = "Integer32"
_XylanNtpMonitorEnable_Object = MibScalar
xylanNtpMonitorEnable = _XylanNtpMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 2),
    _XylanNtpMonitorEnable_Type()
)
xylanNtpMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpMonitorEnable.setStatus("mandatory")
_XylanNtpPeerTable_Object = MibTable
xylanNtpPeerTable = _XylanNtpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3)
)
if mibBuilder.loadTexts:
    xylanNtpPeerTable.setStatus("mandatory")
_XylanNtpPeerEntry_Object = MibTableRow
xylanNtpPeerEntry = _XylanNtpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1)
)
xylanNtpPeerEntry.setIndexNames(
    (0, "XYLAN-NTP-MIB", "xylanNtpPeerAddress"),
)
if mibBuilder.loadTexts:
    xylanNtpPeerEntry.setStatus("mandatory")
_XylanNtpPeerAddress_Type = IpAddress
_XylanNtpPeerAddress_Object = MibTableColumn
xylanNtpPeerAddress = _XylanNtpPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 1),
    _XylanNtpPeerAddress_Type()
)
xylanNtpPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerAddress.setStatus("mandatory")


class _XylanNtpPeerType_Type(Integer32):
    """Custom type xylanNtpPeerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("broadcast", 5),
          ("client", 3))
    )


_XylanNtpPeerType_Type.__name__ = "Integer32"
_XylanNtpPeerType_Object = MibTableColumn
xylanNtpPeerType = _XylanNtpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 2),
    _XylanNtpPeerType_Type()
)
xylanNtpPeerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpPeerType.setStatus("mandatory")
_XylanNtpPeerAuth_Type = Integer32
_XylanNtpPeerAuth_Object = MibTableColumn
xylanNtpPeerAuth = _XylanNtpPeerAuth_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 3),
    _XylanNtpPeerAuth_Type()
)
xylanNtpPeerAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpPeerAuth.setStatus("mandatory")
_XylanNtpPeerVersion_Type = Integer32
_XylanNtpPeerVersion_Object = MibTableColumn
xylanNtpPeerVersion = _XylanNtpPeerVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 4),
    _XylanNtpPeerVersion_Type()
)
xylanNtpPeerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpPeerVersion.setStatus("mandatory")
_XylanNtpPeerMinpoll_Type = Integer32
_XylanNtpPeerMinpoll_Object = MibTableColumn
xylanNtpPeerMinpoll = _XylanNtpPeerMinpoll_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 5),
    _XylanNtpPeerMinpoll_Type()
)
xylanNtpPeerMinpoll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpPeerMinpoll.setStatus("mandatory")


class _XylanNtpPeerPrefer_Type(Integer32):
    """Custom type xylanNtpPeerPrefer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-prefer", 2),
          ("prefer", 1))
    )


_XylanNtpPeerPrefer_Type.__name__ = "Integer32"
_XylanNtpPeerPrefer_Object = MibTableColumn
xylanNtpPeerPrefer = _XylanNtpPeerPrefer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 6),
    _XylanNtpPeerPrefer_Type()
)
xylanNtpPeerPrefer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpPeerPrefer.setStatus("mandatory")


class _XylanNtpPeerAdmin_Type(Integer32):
    """Custom type xylanNtpPeerAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanNtpPeerAdmin_Type.__name__ = "Integer32"
_XylanNtpPeerAdmin_Object = MibTableColumn
xylanNtpPeerAdmin = _XylanNtpPeerAdmin_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 7),
    _XylanNtpPeerAdmin_Type()
)
xylanNtpPeerAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpPeerAdmin.setStatus("mandatory")
_XylanNtpPeerName_Type = DisplayString
_XylanNtpPeerName_Object = MibTableColumn
xylanNtpPeerName = _XylanNtpPeerName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 3, 1, 8),
    _XylanNtpPeerName_Type()
)
xylanNtpPeerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpPeerName.setStatus("mandatory")
_XylanNtpAuthDelay_Type = Integer32
_XylanNtpAuthDelay_Object = MibScalar
xylanNtpAuthDelay = _XylanNtpAuthDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 4),
    _XylanNtpAuthDelay_Type()
)
xylanNtpAuthDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpAuthDelay.setStatus("mandatory")
_XylanNtpKeysFile_Type = DisplayString
_XylanNtpKeysFile_Object = MibScalar
xylanNtpKeysFile = _XylanNtpKeysFile_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 5),
    _XylanNtpKeysFile_Type()
)
xylanNtpKeysFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpKeysFile.setStatus("mandatory")
_XylanNtpConfigReqKeyId_Type = Integer32
_XylanNtpConfigReqKeyId_Object = MibScalar
xylanNtpConfigReqKeyId = _XylanNtpConfigReqKeyId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 6),
    _XylanNtpConfigReqKeyId_Type()
)
xylanNtpConfigReqKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpConfigReqKeyId.setStatus("mandatory")
_XylanNtpConfigCtlKeyId_Type = Integer32
_XylanNtpConfigCtlKeyId_Object = MibScalar
xylanNtpConfigCtlKeyId = _XylanNtpConfigCtlKeyId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 7),
    _XylanNtpConfigCtlKeyId_Type()
)
xylanNtpConfigCtlKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpConfigCtlKeyId.setStatus("mandatory")
_XylanNtpConfigCfgKeyId_Type = Integer32
_XylanNtpConfigCfgKeyId_Object = MibScalar
xylanNtpConfigCfgKeyId = _XylanNtpConfigCfgKeyId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 8),
    _XylanNtpConfigCfgKeyId_Type()
)
xylanNtpConfigCfgKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpConfigCfgKeyId.setStatus("mandatory")


class _XylanNtpPrecision_Type(Integer32):
    """Custom type xylanNtpPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, -1),
    )


_XylanNtpPrecision_Type.__name__ = "Integer32"
_XylanNtpPrecision_Object = MibScalar
xylanNtpPrecision = _XylanNtpPrecision_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 1, 9),
    _XylanNtpPrecision_Type()
)
xylanNtpPrecision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpPrecision.setStatus("mandatory")
_XylanNtpInfo_ObjectIdentity = ObjectIdentity
xylanNtpInfo = _XylanNtpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2)
)
_XylanNtpPeerListTable_Object = MibTable
xylanNtpPeerListTable = _XylanNtpPeerListTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1)
)
if mibBuilder.loadTexts:
    xylanNtpPeerListTable.setStatus("mandatory")
_XylanNtpPeerListEntry_Object = MibTableRow
xylanNtpPeerListEntry = _XylanNtpPeerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1)
)
xylanNtpPeerListEntry.setIndexNames(
    (0, "XYLAN-NTP-MIB", "xylanNtpPeerListAddress"),
)
if mibBuilder.loadTexts:
    xylanNtpPeerListEntry.setStatus("mandatory")
_XylanNtpPeerListAddress_Type = IpAddress
_XylanNtpPeerListAddress_Object = MibTableColumn
xylanNtpPeerListAddress = _XylanNtpPeerListAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 1),
    _XylanNtpPeerListAddress_Type()
)
xylanNtpPeerListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerListAddress.setStatus("mandatory")
_XylanNtpPeerListLocal_Type = IpAddress
_XylanNtpPeerListLocal_Object = MibTableColumn
xylanNtpPeerListLocal = _XylanNtpPeerListLocal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 2),
    _XylanNtpPeerListLocal_Type()
)
xylanNtpPeerListLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerListLocal.setStatus("mandatory")
_XylanNtpPeerListStratum_Type = Integer32
_XylanNtpPeerListStratum_Object = MibTableColumn
xylanNtpPeerListStratum = _XylanNtpPeerListStratum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 3),
    _XylanNtpPeerListStratum_Type()
)
xylanNtpPeerListStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerListStratum.setStatus("mandatory")
_XylanNtpPeerListPoll_Type = Integer32
_XylanNtpPeerListPoll_Object = MibTableColumn
xylanNtpPeerListPoll = _XylanNtpPeerListPoll_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 4),
    _XylanNtpPeerListPoll_Type()
)
xylanNtpPeerListPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerListPoll.setStatus("mandatory")
_XylanNtpPeerListReach_Type = Integer32
_XylanNtpPeerListReach_Object = MibTableColumn
xylanNtpPeerListReach = _XylanNtpPeerListReach_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 5),
    _XylanNtpPeerListReach_Type()
)
xylanNtpPeerListReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerListReach.setStatus("mandatory")
_XylanNtpPeerListDelay_Type = DisplayString
_XylanNtpPeerListDelay_Object = MibTableColumn
xylanNtpPeerListDelay = _XylanNtpPeerListDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 6),
    _XylanNtpPeerListDelay_Type()
)
xylanNtpPeerListDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerListDelay.setStatus("mandatory")
_XylanNtpPeerListOffset_Type = DisplayString
_XylanNtpPeerListOffset_Object = MibTableColumn
xylanNtpPeerListOffset = _XylanNtpPeerListOffset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 7),
    _XylanNtpPeerListOffset_Type()
)
xylanNtpPeerListOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerListOffset.setStatus("mandatory")
_XylanNtpPeerListDispersion_Type = DisplayString
_XylanNtpPeerListDispersion_Object = MibTableColumn
xylanNtpPeerListDispersion = _XylanNtpPeerListDispersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 8),
    _XylanNtpPeerListDispersion_Type()
)
xylanNtpPeerListDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerListDispersion.setStatus("mandatory")


class _XylanNtpPeerListSynced_Type(Integer32):
    """Custom type xylanNtpPeerListSynced based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-synchronized", 2),
          ("synchornized", 1))
    )


_XylanNtpPeerListSynced_Type.__name__ = "Integer32"
_XylanNtpPeerListSynced_Object = MibTableColumn
xylanNtpPeerListSynced = _XylanNtpPeerListSynced_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 9),
    _XylanNtpPeerListSynced_Type()
)
xylanNtpPeerListSynced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerListSynced.setStatus("mandatory")
_XylanNtpPeerListName_Type = DisplayString
_XylanNtpPeerListName_Object = MibTableColumn
xylanNtpPeerListName = _XylanNtpPeerListName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 1, 1, 10),
    _XylanNtpPeerListName_Type()
)
xylanNtpPeerListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerListName.setStatus("mandatory")
_XylanNtpLocalInfo_Type = Integer32
_XylanNtpLocalInfo_Object = MibScalar
xylanNtpLocalInfo = _XylanNtpLocalInfo_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2),
    _XylanNtpLocalInfo_Type()
)
xylanNtpLocalInfo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xylanNtpLocalInfo.setStatus("mandatory")
_XylanNtpInfoPeer_Type = IpAddress
_XylanNtpInfoPeer_Object = MibScalar
xylanNtpInfoPeer = _XylanNtpInfoPeer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 1),
    _XylanNtpInfoPeer_Type()
)
xylanNtpInfoPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoPeer.setStatus("mandatory")
_XylanNtpInfoMode_Type = DisplayString
_XylanNtpInfoMode_Object = MibScalar
xylanNtpInfoMode = _XylanNtpInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 2),
    _XylanNtpInfoMode_Type()
)
xylanNtpInfoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoMode.setStatus("mandatory")
_XylanNtpInfoLeapIndicator_Type = Integer32
_XylanNtpInfoLeapIndicator_Object = MibScalar
xylanNtpInfoLeapIndicator = _XylanNtpInfoLeapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 3),
    _XylanNtpInfoLeapIndicator_Type()
)
xylanNtpInfoLeapIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoLeapIndicator.setStatus("mandatory")
_XylanNtpInfoStratum_Type = Integer32
_XylanNtpInfoStratum_Object = MibScalar
xylanNtpInfoStratum = _XylanNtpInfoStratum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 4),
    _XylanNtpInfoStratum_Type()
)
xylanNtpInfoStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoStratum.setStatus("mandatory")


class _XylanNtpInfoPrecision_Type(Integer32):
    """Custom type xylanNtpInfoPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, -4),
    )


_XylanNtpInfoPrecision_Type.__name__ = "Integer32"
_XylanNtpInfoPrecision_Object = MibScalar
xylanNtpInfoPrecision = _XylanNtpInfoPrecision_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 5),
    _XylanNtpInfoPrecision_Type()
)
xylanNtpInfoPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoPrecision.setStatus("mandatory")
_XylanNtpInfoDistance_Type = DisplayString
_XylanNtpInfoDistance_Object = MibScalar
xylanNtpInfoDistance = _XylanNtpInfoDistance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 6),
    _XylanNtpInfoDistance_Type()
)
xylanNtpInfoDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoDistance.setStatus("mandatory")
_XylanNtpInfoDispersion_Type = DisplayString
_XylanNtpInfoDispersion_Object = MibScalar
xylanNtpInfoDispersion = _XylanNtpInfoDispersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 7),
    _XylanNtpInfoDispersion_Type()
)
xylanNtpInfoDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoDispersion.setStatus("mandatory")
_XylanNtpInfoReferenceId_Type = DisplayString
_XylanNtpInfoReferenceId_Object = MibScalar
xylanNtpInfoReferenceId = _XylanNtpInfoReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 8),
    _XylanNtpInfoReferenceId_Type()
)
xylanNtpInfoReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoReferenceId.setStatus("mandatory")
_XylanNtpInfoReferenceTime_Type = DisplayString
_XylanNtpInfoReferenceTime_Object = MibScalar
xylanNtpInfoReferenceTime = _XylanNtpInfoReferenceTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 9),
    _XylanNtpInfoReferenceTime_Type()
)
xylanNtpInfoReferenceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoReferenceTime.setStatus("mandatory")
_XylanNtpInfoFrequency_Type = DisplayString
_XylanNtpInfoFrequency_Object = MibScalar
xylanNtpInfoFrequency = _XylanNtpInfoFrequency_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 10),
    _XylanNtpInfoFrequency_Type()
)
xylanNtpInfoFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoFrequency.setStatus("mandatory")
_XylanNtpInfoStability_Type = DisplayString
_XylanNtpInfoStability_Object = MibScalar
xylanNtpInfoStability = _XylanNtpInfoStability_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 11),
    _XylanNtpInfoStability_Type()
)
xylanNtpInfoStability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoStability.setStatus("mandatory")
_XylanNtpInfoBroadcastDelay_Type = DisplayString
_XylanNtpInfoBroadcastDelay_Object = MibScalar
xylanNtpInfoBroadcastDelay = _XylanNtpInfoBroadcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 12),
    _XylanNtpInfoBroadcastDelay_Type()
)
xylanNtpInfoBroadcastDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoBroadcastDelay.setStatus("mandatory")
_XylanNtpInfoAuthDelay_Type = DisplayString
_XylanNtpInfoAuthDelay_Object = MibScalar
xylanNtpInfoAuthDelay = _XylanNtpInfoAuthDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 2, 13),
    _XylanNtpInfoAuthDelay_Type()
)
xylanNtpInfoAuthDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpInfoAuthDelay.setStatus("mandatory")
_XylanNtpPeerShowTable_Object = MibTable
xylanNtpPeerShowTable = _XylanNtpPeerShowTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3)
)
if mibBuilder.loadTexts:
    xylanNtpPeerShowTable.setStatus("mandatory")
_XylanNtpPeerShowEntry_Object = MibTableRow
xylanNtpPeerShowEntry = _XylanNtpPeerShowEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1)
)
xylanNtpPeerShowEntry.setIndexNames(
    (0, "XYLAN-NTP-MIB", "xylanNtpPeerShowRemote"),
)
if mibBuilder.loadTexts:
    xylanNtpPeerShowEntry.setStatus("mandatory")
_XylanNtpPeerShowRemote_Type = IpAddress
_XylanNtpPeerShowRemote_Object = MibTableColumn
xylanNtpPeerShowRemote = _XylanNtpPeerShowRemote_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 1),
    _XylanNtpPeerShowRemote_Type()
)
xylanNtpPeerShowRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowRemote.setStatus("mandatory")
_XylanNtpPeerShowLocal_Type = IpAddress
_XylanNtpPeerShowLocal_Object = MibTableColumn
xylanNtpPeerShowLocal = _XylanNtpPeerShowLocal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 2),
    _XylanNtpPeerShowLocal_Type()
)
xylanNtpPeerShowLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowLocal.setStatus("mandatory")
_XylanNtpPeerShowHmode_Type = DisplayString
_XylanNtpPeerShowHmode_Object = MibTableColumn
xylanNtpPeerShowHmode = _XylanNtpPeerShowHmode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 3),
    _XylanNtpPeerShowHmode_Type()
)
xylanNtpPeerShowHmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowHmode.setStatus("mandatory")
_XylanNtpPeerShowPmode_Type = DisplayString
_XylanNtpPeerShowPmode_Object = MibTableColumn
xylanNtpPeerShowPmode = _XylanNtpPeerShowPmode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 4),
    _XylanNtpPeerShowPmode_Type()
)
xylanNtpPeerShowPmode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowPmode.setStatus("mandatory")
_XylanNtpPeerShowStratum_Type = Integer32
_XylanNtpPeerShowStratum_Object = MibTableColumn
xylanNtpPeerShowStratum = _XylanNtpPeerShowStratum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 5),
    _XylanNtpPeerShowStratum_Type()
)
xylanNtpPeerShowStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowStratum.setStatus("mandatory")


class _XylanNtpPeerShowPrecision_Type(Integer32):
    """Custom type xylanNtpPeerShowPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, -4),
    )


_XylanNtpPeerShowPrecision_Type.__name__ = "Integer32"
_XylanNtpPeerShowPrecision_Object = MibTableColumn
xylanNtpPeerShowPrecision = _XylanNtpPeerShowPrecision_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 6),
    _XylanNtpPeerShowPrecision_Type()
)
xylanNtpPeerShowPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowPrecision.setStatus("mandatory")
_XylanNtpPeerShowLeapIndicator_Type = Integer32
_XylanNtpPeerShowLeapIndicator_Object = MibTableColumn
xylanNtpPeerShowLeapIndicator = _XylanNtpPeerShowLeapIndicator_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 7),
    _XylanNtpPeerShowLeapIndicator_Type()
)
xylanNtpPeerShowLeapIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowLeapIndicator.setStatus("mandatory")
_XylanNtpPeerShowReferenceId_Type = DisplayString
_XylanNtpPeerShowReferenceId_Object = MibTableColumn
xylanNtpPeerShowReferenceId = _XylanNtpPeerShowReferenceId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 8),
    _XylanNtpPeerShowReferenceId_Type()
)
xylanNtpPeerShowReferenceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowReferenceId.setStatus("mandatory")
_XylanNtpPeerShowRootDistance_Type = DisplayString
_XylanNtpPeerShowRootDistance_Object = MibTableColumn
xylanNtpPeerShowRootDistance = _XylanNtpPeerShowRootDistance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 9),
    _XylanNtpPeerShowRootDistance_Type()
)
xylanNtpPeerShowRootDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowRootDistance.setStatus("mandatory")
_XylanNtpPeerShowRootDispersion_Type = DisplayString
_XylanNtpPeerShowRootDispersion_Object = MibTableColumn
xylanNtpPeerShowRootDispersion = _XylanNtpPeerShowRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 10),
    _XylanNtpPeerShowRootDispersion_Type()
)
xylanNtpPeerShowRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowRootDispersion.setStatus("mandatory")
_XylanNtpPeerShowPpoll_Type = Integer32
_XylanNtpPeerShowPpoll_Object = MibTableColumn
xylanNtpPeerShowPpoll = _XylanNtpPeerShowPpoll_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 11),
    _XylanNtpPeerShowPpoll_Type()
)
xylanNtpPeerShowPpoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowPpoll.setStatus("mandatory")
_XylanNtpPeerShowHpoll_Type = Integer32
_XylanNtpPeerShowHpoll_Object = MibTableColumn
xylanNtpPeerShowHpoll = _XylanNtpPeerShowHpoll_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 12),
    _XylanNtpPeerShowHpoll_Type()
)
xylanNtpPeerShowHpoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowHpoll.setStatus("mandatory")
_XylanNtpPeerShowKeyid_Type = Integer32
_XylanNtpPeerShowKeyid_Object = MibTableColumn
xylanNtpPeerShowKeyid = _XylanNtpPeerShowKeyid_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 13),
    _XylanNtpPeerShowKeyid_Type()
)
xylanNtpPeerShowKeyid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowKeyid.setStatus("mandatory")
_XylanNtpPeerShowVersion_Type = Integer32
_XylanNtpPeerShowVersion_Object = MibTableColumn
xylanNtpPeerShowVersion = _XylanNtpPeerShowVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 14),
    _XylanNtpPeerShowVersion_Type()
)
xylanNtpPeerShowVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowVersion.setStatus("mandatory")
_XylanNtpPeerShowAssociation_Type = Integer32
_XylanNtpPeerShowAssociation_Object = MibTableColumn
xylanNtpPeerShowAssociation = _XylanNtpPeerShowAssociation_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 15),
    _XylanNtpPeerShowAssociation_Type()
)
xylanNtpPeerShowAssociation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowAssociation.setStatus("mandatory")
_XylanNtpPeerShowValid_Type = Integer32
_XylanNtpPeerShowValid_Object = MibTableColumn
xylanNtpPeerShowValid = _XylanNtpPeerShowValid_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 16),
    _XylanNtpPeerShowValid_Type()
)
xylanNtpPeerShowValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowValid.setStatus("mandatory")
_XylanNtpPeerShowReach_Type = Integer32
_XylanNtpPeerShowReach_Object = MibTableColumn
xylanNtpPeerShowReach = _XylanNtpPeerShowReach_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 17),
    _XylanNtpPeerShowReach_Type()
)
xylanNtpPeerShowReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowReach.setStatus("mandatory")
_XylanNtpPeerShowUnreach_Type = Integer32
_XylanNtpPeerShowUnreach_Object = MibTableColumn
xylanNtpPeerShowUnreach = _XylanNtpPeerShowUnreach_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 18),
    _XylanNtpPeerShowUnreach_Type()
)
xylanNtpPeerShowUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowUnreach.setStatus("mandatory")
_XylanNtpPeerShowFlash_Type = Integer32
_XylanNtpPeerShowFlash_Object = MibTableColumn
xylanNtpPeerShowFlash = _XylanNtpPeerShowFlash_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 19),
    _XylanNtpPeerShowFlash_Type()
)
xylanNtpPeerShowFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowFlash.setStatus("mandatory")
_XylanNtpPeerShowBroadcastOffset_Type = DisplayString
_XylanNtpPeerShowBroadcastOffset_Object = MibTableColumn
xylanNtpPeerShowBroadcastOffset = _XylanNtpPeerShowBroadcastOffset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 20),
    _XylanNtpPeerShowBroadcastOffset_Type()
)
xylanNtpPeerShowBroadcastOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowBroadcastOffset.setStatus("mandatory")
_XylanNtpPeerShowTTL_Type = Integer32
_XylanNtpPeerShowTTL_Object = MibTableColumn
xylanNtpPeerShowTTL = _XylanNtpPeerShowTTL_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 21),
    _XylanNtpPeerShowTTL_Type()
)
xylanNtpPeerShowTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowTTL.setStatus("mandatory")
_XylanNtpPeerShowTimer_Type = Integer32
_XylanNtpPeerShowTimer_Object = MibTableColumn
xylanNtpPeerShowTimer = _XylanNtpPeerShowTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 22),
    _XylanNtpPeerShowTimer_Type()
)
xylanNtpPeerShowTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowTimer.setStatus("mandatory")
_XylanNtpPeerShowFlags_Type = Integer32
_XylanNtpPeerShowFlags_Object = MibTableColumn
xylanNtpPeerShowFlags = _XylanNtpPeerShowFlags_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 23),
    _XylanNtpPeerShowFlags_Type()
)
xylanNtpPeerShowFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowFlags.setStatus("mandatory")
_XylanNtpPeerShowReferenceTime_Type = DisplayString
_XylanNtpPeerShowReferenceTime_Object = MibTableColumn
xylanNtpPeerShowReferenceTime = _XylanNtpPeerShowReferenceTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 24),
    _XylanNtpPeerShowReferenceTime_Type()
)
xylanNtpPeerShowReferenceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowReferenceTime.setStatus("mandatory")
_XylanNtpPeerShowOriginateTime_Type = DisplayString
_XylanNtpPeerShowOriginateTime_Object = MibTableColumn
xylanNtpPeerShowOriginateTime = _XylanNtpPeerShowOriginateTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 25),
    _XylanNtpPeerShowOriginateTime_Type()
)
xylanNtpPeerShowOriginateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowOriginateTime.setStatus("mandatory")
_XylanNtpPeerShowReceiveTime_Type = DisplayString
_XylanNtpPeerShowReceiveTime_Object = MibTableColumn
xylanNtpPeerShowReceiveTime = _XylanNtpPeerShowReceiveTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 26),
    _XylanNtpPeerShowReceiveTime_Type()
)
xylanNtpPeerShowReceiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowReceiveTime.setStatus("mandatory")
_XylanNtpPeerShowTransmitTime_Type = DisplayString
_XylanNtpPeerShowTransmitTime_Object = MibTableColumn
xylanNtpPeerShowTransmitTime = _XylanNtpPeerShowTransmitTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 27),
    _XylanNtpPeerShowTransmitTime_Type()
)
xylanNtpPeerShowTransmitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowTransmitTime.setStatus("mandatory")
_XylanNtpPeerShowOffset_Type = DisplayString
_XylanNtpPeerShowOffset_Object = MibTableColumn
xylanNtpPeerShowOffset = _XylanNtpPeerShowOffset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 28),
    _XylanNtpPeerShowOffset_Type()
)
xylanNtpPeerShowOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowOffset.setStatus("mandatory")
_XylanNtpPeerShowDelay_Type = DisplayString
_XylanNtpPeerShowDelay_Object = MibTableColumn
xylanNtpPeerShowDelay = _XylanNtpPeerShowDelay_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 29),
    _XylanNtpPeerShowDelay_Type()
)
xylanNtpPeerShowDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowDelay.setStatus("mandatory")
_XylanNtpPeerShowDispersion_Type = DisplayString
_XylanNtpPeerShowDispersion_Object = MibTableColumn
xylanNtpPeerShowDispersion = _XylanNtpPeerShowDispersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 30),
    _XylanNtpPeerShowDispersion_Type()
)
xylanNtpPeerShowDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowDispersion.setStatus("mandatory")
_XylanNtpPeerShowName_Type = DisplayString
_XylanNtpPeerShowName_Object = MibTableColumn
xylanNtpPeerShowName = _XylanNtpPeerShowName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 2, 3, 1, 31),
    _XylanNtpPeerShowName_Type()
)
xylanNtpPeerShowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpPeerShowName.setStatus("mandatory")
_XylanNtpStats_ObjectIdentity = ObjectIdentity
xylanNtpStats = _XylanNtpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3)
)
_XylanNtpStatsStat_Type = Integer32
_XylanNtpStatsStat_Object = MibScalar
xylanNtpStatsStat = _XylanNtpStatsStat_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1),
    _XylanNtpStatsStat_Type()
)
xylanNtpStatsStat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xylanNtpStatsStat.setStatus("mandatory")
_XylanNtpStatsStatUptime_Type = Counter32
_XylanNtpStatsStatUptime_Object = MibScalar
xylanNtpStatsStatUptime = _XylanNtpStatsStatUptime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 1),
    _XylanNtpStatsStatUptime_Type()
)
xylanNtpStatsStatUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsStatUptime.setStatus("mandatory")
_XylanNtpStatsStatReset_Type = Counter32
_XylanNtpStatsStatReset_Object = MibScalar
xylanNtpStatsStatReset = _XylanNtpStatsStatReset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 2),
    _XylanNtpStatsStatReset_Type()
)
xylanNtpStatsStatReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsStatReset.setStatus("mandatory")
_XylanNtpStatsStatBadStratum_Type = Counter32
_XylanNtpStatsStatBadStratum_Object = MibScalar
xylanNtpStatsStatBadStratum = _XylanNtpStatsStatBadStratum_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 3),
    _XylanNtpStatsStatBadStratum_Type()
)
xylanNtpStatsStatBadStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsStatBadStratum.setStatus("mandatory")
_XylanNtpStatsStatOldVersion_Type = Counter32
_XylanNtpStatsStatOldVersion_Object = MibScalar
xylanNtpStatsStatOldVersion = _XylanNtpStatsStatOldVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 4),
    _XylanNtpStatsStatOldVersion_Type()
)
xylanNtpStatsStatOldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsStatOldVersion.setStatus("mandatory")
_XylanNtpStatsStatNewVersion_Type = Counter32
_XylanNtpStatsStatNewVersion_Object = MibScalar
xylanNtpStatsStatNewVersion = _XylanNtpStatsStatNewVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 5),
    _XylanNtpStatsStatNewVersion_Type()
)
xylanNtpStatsStatNewVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsStatNewVersion.setStatus("mandatory")
_XylanNtpStatsStatUnknownVersion_Type = Counter32
_XylanNtpStatsStatUnknownVersion_Object = MibScalar
xylanNtpStatsStatUnknownVersion = _XylanNtpStatsStatUnknownVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 6),
    _XylanNtpStatsStatUnknownVersion_Type()
)
xylanNtpStatsStatUnknownVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsStatUnknownVersion.setStatus("mandatory")
_XylanNtpStatsStatBadLength_Type = Counter32
_XylanNtpStatsStatBadLength_Object = MibScalar
xylanNtpStatsStatBadLength = _XylanNtpStatsStatBadLength_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 7),
    _XylanNtpStatsStatBadLength_Type()
)
xylanNtpStatsStatBadLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsStatBadLength.setStatus("mandatory")
_XylanNtpStatsStatProcessed_Type = Counter32
_XylanNtpStatsStatProcessed_Object = MibScalar
xylanNtpStatsStatProcessed = _XylanNtpStatsStatProcessed_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 8),
    _XylanNtpStatsStatProcessed_Type()
)
xylanNtpStatsStatProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsStatProcessed.setStatus("mandatory")
_XylanNtpStatsStatBadAuth_Type = Counter32
_XylanNtpStatsStatBadAuth_Object = MibScalar
xylanNtpStatsStatBadAuth = _XylanNtpStatsStatBadAuth_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 9),
    _XylanNtpStatsStatBadAuth_Type()
)
xylanNtpStatsStatBadAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsStatBadAuth.setStatus("mandatory")
_XylanNtpStatsStatLimitRejects_Type = Counter32
_XylanNtpStatsStatLimitRejects_Object = MibScalar
xylanNtpStatsStatLimitRejects = _XylanNtpStatsStatLimitRejects_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 1, 10),
    _XylanNtpStatsStatLimitRejects_Type()
)
xylanNtpStatsStatLimitRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsStatLimitRejects.setStatus("mandatory")
_XylanNtpStatsPeerTable_Object = MibTable
xylanNtpStatsPeerTable = _XylanNtpStatsPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2)
)
if mibBuilder.loadTexts:
    xylanNtpStatsPeerTable.setStatus("mandatory")
_XylanNtpStatsPeerEntry_Object = MibTableRow
xylanNtpStatsPeerEntry = _XylanNtpStatsPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1)
)
xylanNtpStatsPeerEntry.setIndexNames(
    (0, "XYLAN-NTP-MIB", "xylanNtpStatsPeerAddress"),
)
if mibBuilder.loadTexts:
    xylanNtpStatsPeerEntry.setStatus("mandatory")
_XylanNtpStatsPeerAddress_Type = IpAddress
_XylanNtpStatsPeerAddress_Object = MibTableColumn
xylanNtpStatsPeerAddress = _XylanNtpStatsPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 1),
    _XylanNtpStatsPeerAddress_Type()
)
xylanNtpStatsPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerAddress.setStatus("mandatory")
_XylanNtpStatsPeerLocal_Type = IpAddress
_XylanNtpStatsPeerLocal_Object = MibTableColumn
xylanNtpStatsPeerLocal = _XylanNtpStatsPeerLocal_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 2),
    _XylanNtpStatsPeerLocal_Type()
)
xylanNtpStatsPeerLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerLocal.setStatus("mandatory")
_XylanNtpStatsPeerLastRcv_Type = Counter32
_XylanNtpStatsPeerLastRcv_Object = MibTableColumn
xylanNtpStatsPeerLastRcv = _XylanNtpStatsPeerLastRcv_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 3),
    _XylanNtpStatsPeerLastRcv_Type()
)
xylanNtpStatsPeerLastRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerLastRcv.setStatus("mandatory")
_XylanNtpStatsPeerNextSend_Type = Counter32
_XylanNtpStatsPeerNextSend_Object = MibTableColumn
xylanNtpStatsPeerNextSend = _XylanNtpStatsPeerNextSend_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 4),
    _XylanNtpStatsPeerNextSend_Type()
)
xylanNtpStatsPeerNextSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerNextSend.setStatus("mandatory")
_XylanNtpStatsPeerReachChange_Type = Counter32
_XylanNtpStatsPeerReachChange_Object = MibTableColumn
xylanNtpStatsPeerReachChange = _XylanNtpStatsPeerReachChange_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 5),
    _XylanNtpStatsPeerReachChange_Type()
)
xylanNtpStatsPeerReachChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerReachChange.setStatus("mandatory")
_XylanNtpStatsPeerPacketsSent_Type = Counter32
_XylanNtpStatsPeerPacketsSent_Object = MibTableColumn
xylanNtpStatsPeerPacketsSent = _XylanNtpStatsPeerPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 6),
    _XylanNtpStatsPeerPacketsSent_Type()
)
xylanNtpStatsPeerPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerPacketsSent.setStatus("mandatory")
_XylanNtpStatsPeerPacketsRcvd_Type = Counter32
_XylanNtpStatsPeerPacketsRcvd_Object = MibTableColumn
xylanNtpStatsPeerPacketsRcvd = _XylanNtpStatsPeerPacketsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 7),
    _XylanNtpStatsPeerPacketsRcvd_Type()
)
xylanNtpStatsPeerPacketsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerPacketsRcvd.setStatus("mandatory")
_XylanNtpStatsPeerBadAuth_Type = Counter32
_XylanNtpStatsPeerBadAuth_Object = MibTableColumn
xylanNtpStatsPeerBadAuth = _XylanNtpStatsPeerBadAuth_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 8),
    _XylanNtpStatsPeerBadAuth_Type()
)
xylanNtpStatsPeerBadAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerBadAuth.setStatus("mandatory")
_XylanNtpStatsPeerBogusOrigin_Type = Counter32
_XylanNtpStatsPeerBogusOrigin_Object = MibTableColumn
xylanNtpStatsPeerBogusOrigin = _XylanNtpStatsPeerBogusOrigin_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 9),
    _XylanNtpStatsPeerBogusOrigin_Type()
)
xylanNtpStatsPeerBogusOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerBogusOrigin.setStatus("mandatory")
_XylanNtpStatsPeerDuplicate_Type = Counter32
_XylanNtpStatsPeerDuplicate_Object = MibTableColumn
xylanNtpStatsPeerDuplicate = _XylanNtpStatsPeerDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 10),
    _XylanNtpStatsPeerDuplicate_Type()
)
xylanNtpStatsPeerDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerDuplicate.setStatus("mandatory")
_XylanNtpStatsPeerBadDispersion_Type = Counter32
_XylanNtpStatsPeerBadDispersion_Object = MibTableColumn
xylanNtpStatsPeerBadDispersion = _XylanNtpStatsPeerBadDispersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 11),
    _XylanNtpStatsPeerBadDispersion_Type()
)
xylanNtpStatsPeerBadDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerBadDispersion.setStatus("mandatory")
_XylanNtpStatsPeerBadRefTime_Type = Counter32
_XylanNtpStatsPeerBadRefTime_Object = MibTableColumn
xylanNtpStatsPeerBadRefTime = _XylanNtpStatsPeerBadRefTime_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 12),
    _XylanNtpStatsPeerBadRefTime_Type()
)
xylanNtpStatsPeerBadRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerBadRefTime.setStatus("mandatory")
_XylanNtpStatsPeerCandidateOrder_Type = Counter32
_XylanNtpStatsPeerCandidateOrder_Object = MibTableColumn
xylanNtpStatsPeerCandidateOrder = _XylanNtpStatsPeerCandidateOrder_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 13),
    _XylanNtpStatsPeerCandidateOrder_Type()
)
xylanNtpStatsPeerCandidateOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerCandidateOrder.setStatus("mandatory")
_XylanNtpStatsPeerReset_Type = Integer32
_XylanNtpStatsPeerReset_Object = MibTableColumn
xylanNtpStatsPeerReset = _XylanNtpStatsPeerReset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 14),
    _XylanNtpStatsPeerReset_Type()
)
xylanNtpStatsPeerReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerReset.setStatus("mandatory")
_XylanNtpStatsPeerName_Type = DisplayString
_XylanNtpStatsPeerName_Object = MibTableColumn
xylanNtpStatsPeerName = _XylanNtpStatsPeerName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 2, 1, 15),
    _XylanNtpStatsPeerName_Type()
)
xylanNtpStatsPeerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsPeerName.setStatus("mandatory")
_XylanNtpStatsLoop_Type = Integer32
_XylanNtpStatsLoop_Object = MibScalar
xylanNtpStatsLoop = _XylanNtpStatsLoop_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 3),
    _XylanNtpStatsLoop_Type()
)
xylanNtpStatsLoop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xylanNtpStatsLoop.setStatus("mandatory")
_XylanNtpStatsLoopOffset_Type = DisplayString
_XylanNtpStatsLoopOffset_Object = MibScalar
xylanNtpStatsLoopOffset = _XylanNtpStatsLoopOffset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 3, 1),
    _XylanNtpStatsLoopOffset_Type()
)
xylanNtpStatsLoopOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsLoopOffset.setStatus("mandatory")
_XylanNtpStatsLoopFrequency_Type = DisplayString
_XylanNtpStatsLoopFrequency_Object = MibScalar
xylanNtpStatsLoopFrequency = _XylanNtpStatsLoopFrequency_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 3, 2),
    _XylanNtpStatsLoopFrequency_Type()
)
xylanNtpStatsLoopFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsLoopFrequency.setStatus("mandatory")
_XylanNtpStatsLoopPollAdjust_Type = Integer32
_XylanNtpStatsLoopPollAdjust_Object = MibScalar
xylanNtpStatsLoopPollAdjust = _XylanNtpStatsLoopPollAdjust_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 3, 3),
    _XylanNtpStatsLoopPollAdjust_Type()
)
xylanNtpStatsLoopPollAdjust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsLoopPollAdjust.setStatus("mandatory")
_XylanNtpStatsLoopWatchdog_Type = Counter32
_XylanNtpStatsLoopWatchdog_Object = MibScalar
xylanNtpStatsLoopWatchdog = _XylanNtpStatsLoopWatchdog_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 3, 4),
    _XylanNtpStatsLoopWatchdog_Type()
)
xylanNtpStatsLoopWatchdog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsLoopWatchdog.setStatus("mandatory")
_XylanNtpStatsIo_Type = Integer32
_XylanNtpStatsIo_Object = MibScalar
xylanNtpStatsIo = _XylanNtpStatsIo_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4),
    _XylanNtpStatsIo_Type()
)
xylanNtpStatsIo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xylanNtpStatsIo.setStatus("mandatory")
_XylanNtpStatsIoReset_Type = Counter32
_XylanNtpStatsIoReset_Object = MibScalar
xylanNtpStatsIoReset = _XylanNtpStatsIoReset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 1),
    _XylanNtpStatsIoReset_Type()
)
xylanNtpStatsIoReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoReset.setStatus("mandatory")
_XylanNtpStatsIoRcvBuffers_Type = Counter32
_XylanNtpStatsIoRcvBuffers_Object = MibScalar
xylanNtpStatsIoRcvBuffers = _XylanNtpStatsIoRcvBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 2),
    _XylanNtpStatsIoRcvBuffers_Type()
)
xylanNtpStatsIoRcvBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoRcvBuffers.setStatus("mandatory")
_XylanNtpStatsIoFreeRcvBuffers_Type = Counter32
_XylanNtpStatsIoFreeRcvBuffers_Object = MibScalar
xylanNtpStatsIoFreeRcvBuffers = _XylanNtpStatsIoFreeRcvBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 3),
    _XylanNtpStatsIoFreeRcvBuffers_Type()
)
xylanNtpStatsIoFreeRcvBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoFreeRcvBuffers.setStatus("mandatory")
_XylanNtpStatsIoUsedRcvBuffers_Type = Counter32
_XylanNtpStatsIoUsedRcvBuffers_Object = MibScalar
xylanNtpStatsIoUsedRcvBuffers = _XylanNtpStatsIoUsedRcvBuffers_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 4),
    _XylanNtpStatsIoUsedRcvBuffers_Type()
)
xylanNtpStatsIoUsedRcvBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoUsedRcvBuffers.setStatus("mandatory")
_XylanNtpStatsIoRefills_Type = Counter32
_XylanNtpStatsIoRefills_Object = MibScalar
xylanNtpStatsIoRefills = _XylanNtpStatsIoRefills_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 5),
    _XylanNtpStatsIoRefills_Type()
)
xylanNtpStatsIoRefills.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoRefills.setStatus("mandatory")
_XylanNtpStatsIoDroppedPackets_Type = Counter32
_XylanNtpStatsIoDroppedPackets_Object = MibScalar
xylanNtpStatsIoDroppedPackets = _XylanNtpStatsIoDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 6),
    _XylanNtpStatsIoDroppedPackets_Type()
)
xylanNtpStatsIoDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoDroppedPackets.setStatus("mandatory")
_XylanNtpStatsIoIgnoredPackets_Type = Counter32
_XylanNtpStatsIoIgnoredPackets_Object = MibScalar
xylanNtpStatsIoIgnoredPackets = _XylanNtpStatsIoIgnoredPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 7),
    _XylanNtpStatsIoIgnoredPackets_Type()
)
xylanNtpStatsIoIgnoredPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoIgnoredPackets.setStatus("mandatory")
_XylanNtpStatsIoRcvPackets_Type = Counter32
_XylanNtpStatsIoRcvPackets_Object = MibScalar
xylanNtpStatsIoRcvPackets = _XylanNtpStatsIoRcvPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 8),
    _XylanNtpStatsIoRcvPackets_Type()
)
xylanNtpStatsIoRcvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoRcvPackets.setStatus("mandatory")
_XylanNtpStatsIoSentPackets_Type = Counter32
_XylanNtpStatsIoSentPackets_Object = MibScalar
xylanNtpStatsIoSentPackets = _XylanNtpStatsIoSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 9),
    _XylanNtpStatsIoSentPackets_Type()
)
xylanNtpStatsIoSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoSentPackets.setStatus("mandatory")
_XylanNtpStatsIoNotSentPackets_Type = Counter32
_XylanNtpStatsIoNotSentPackets_Object = MibScalar
xylanNtpStatsIoNotSentPackets = _XylanNtpStatsIoNotSentPackets_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 10),
    _XylanNtpStatsIoNotSentPackets_Type()
)
xylanNtpStatsIoNotSentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoNotSentPackets.setStatus("mandatory")
_XylanNtpStatsIoInterrupts_Type = Counter32
_XylanNtpStatsIoInterrupts_Object = MibScalar
xylanNtpStatsIoInterrupts = _XylanNtpStatsIoInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 11),
    _XylanNtpStatsIoInterrupts_Type()
)
xylanNtpStatsIoInterrupts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoInterrupts.setStatus("mandatory")
_XylanNtpStatsIoInterruptsRcv_Type = Counter32
_XylanNtpStatsIoInterruptsRcv_Object = MibScalar
xylanNtpStatsIoInterruptsRcv = _XylanNtpStatsIoInterruptsRcv_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 4, 12),
    _XylanNtpStatsIoInterruptsRcv_Type()
)
xylanNtpStatsIoInterruptsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsIoInterruptsRcv.setStatus("mandatory")
_XylanNtpStatsReset_Type = Integer32
_XylanNtpStatsReset_Object = MibScalar
xylanNtpStatsReset = _XylanNtpStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 5),
    _XylanNtpStatsReset_Type()
)
xylanNtpStatsReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    xylanNtpStatsReset.setStatus("mandatory")
_XylanNtpStatsMonitorTable_Object = MibTable
xylanNtpStatsMonitorTable = _XylanNtpStatsMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6)
)
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorTable.setStatus("mandatory")
_XylanNtpStatsMonitorEntry_Object = MibTableRow
xylanNtpStatsMonitorEntry = _XylanNtpStatsMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1)
)
xylanNtpStatsMonitorEntry.setIndexNames(
    (0, "XYLAN-NTP-MIB", "xylanNtpStatsMonitorIndex"),
)
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorEntry.setStatus("mandatory")
_XylanNtpStatsMonitorIndex_Type = Counter32
_XylanNtpStatsMonitorIndex_Object = MibTableColumn
xylanNtpStatsMonitorIndex = _XylanNtpStatsMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 1),
    _XylanNtpStatsMonitorIndex_Type()
)
xylanNtpStatsMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorIndex.setStatus("mandatory")
_XylanNtpStatsMonitorAddress_Type = IpAddress
_XylanNtpStatsMonitorAddress_Object = MibTableColumn
xylanNtpStatsMonitorAddress = _XylanNtpStatsMonitorAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 2),
    _XylanNtpStatsMonitorAddress_Type()
)
xylanNtpStatsMonitorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorAddress.setStatus("mandatory")
_XylanNtpStatsMonitorPort_Type = Integer32
_XylanNtpStatsMonitorPort_Object = MibTableColumn
xylanNtpStatsMonitorPort = _XylanNtpStatsMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 3),
    _XylanNtpStatsMonitorPort_Type()
)
xylanNtpStatsMonitorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorPort.setStatus("mandatory")
_XylanNtpStatsMonitorLocalAddress_Type = IpAddress
_XylanNtpStatsMonitorLocalAddress_Object = MibTableColumn
xylanNtpStatsMonitorLocalAddress = _XylanNtpStatsMonitorLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 4),
    _XylanNtpStatsMonitorLocalAddress_Type()
)
xylanNtpStatsMonitorLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorLocalAddress.setStatus("mandatory")
_XylanNtpStatsMonitorCount_Type = Counter32
_XylanNtpStatsMonitorCount_Object = MibTableColumn
xylanNtpStatsMonitorCount = _XylanNtpStatsMonitorCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 5),
    _XylanNtpStatsMonitorCount_Type()
)
xylanNtpStatsMonitorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorCount.setStatus("mandatory")
_XylanNtpStatsMonitorMode_Type = DisplayString
_XylanNtpStatsMonitorMode_Object = MibTableColumn
xylanNtpStatsMonitorMode = _XylanNtpStatsMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 6),
    _XylanNtpStatsMonitorMode_Type()
)
xylanNtpStatsMonitorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorMode.setStatus("mandatory")
_XylanNtpStatsMonitorVersion_Type = Integer32
_XylanNtpStatsMonitorVersion_Object = MibTableColumn
xylanNtpStatsMonitorVersion = _XylanNtpStatsMonitorVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 7),
    _XylanNtpStatsMonitorVersion_Type()
)
xylanNtpStatsMonitorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorVersion.setStatus("mandatory")
_XylanNtpStatsMonitorDrop_Type = Counter32
_XylanNtpStatsMonitorDrop_Object = MibTableColumn
xylanNtpStatsMonitorDrop = _XylanNtpStatsMonitorDrop_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 8),
    _XylanNtpStatsMonitorDrop_Type()
)
xylanNtpStatsMonitorDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorDrop.setStatus("mandatory")
_XylanNtpStatsMonitorLast_Type = Counter32
_XylanNtpStatsMonitorLast_Object = MibTableColumn
xylanNtpStatsMonitorLast = _XylanNtpStatsMonitorLast_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 9),
    _XylanNtpStatsMonitorLast_Type()
)
xylanNtpStatsMonitorLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorLast.setStatus("mandatory")
_XylanNtpStatsMonitorFirst_Type = Counter32
_XylanNtpStatsMonitorFirst_Object = MibTableColumn
xylanNtpStatsMonitorFirst = _XylanNtpStatsMonitorFirst_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 10),
    _XylanNtpStatsMonitorFirst_Type()
)
xylanNtpStatsMonitorFirst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorFirst.setStatus("mandatory")
_XylanNtpStatsMonitorName_Type = DisplayString
_XylanNtpStatsMonitorName_Object = MibTableColumn
xylanNtpStatsMonitorName = _XylanNtpStatsMonitorName_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 3, 6, 1, 11),
    _XylanNtpStatsMonitorName_Type()
)
xylanNtpStatsMonitorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpStatsMonitorName.setStatus("mandatory")
_XylanNtpAdmin_ObjectIdentity = ObjectIdentity
xylanNtpAdmin = _XylanNtpAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 4)
)
_XylanNtpAccess_ObjectIdentity = ObjectIdentity
xylanNtpAccess = _XylanNtpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5)
)
_XylanNtpAccessKeyIdTable_Object = MibTable
xylanNtpAccessKeyIdTable = _XylanNtpAccessKeyIdTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 1)
)
if mibBuilder.loadTexts:
    xylanNtpAccessKeyIdTable.setStatus("mandatory")
_XylanNtpAccessKeyIdEntry_Object = MibTableRow
xylanNtpAccessKeyIdEntry = _XylanNtpAccessKeyIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 1, 1)
)
xylanNtpAccessKeyIdEntry.setIndexNames(
    (0, "XYLAN-NTP-MIB", "xylanNtpAccessKeyIdKeyId"),
)
if mibBuilder.loadTexts:
    xylanNtpAccessKeyIdEntry.setStatus("mandatory")
_XylanNtpAccessKeyIdKeyId_Type = Integer32
_XylanNtpAccessKeyIdKeyId_Object = MibTableColumn
xylanNtpAccessKeyIdKeyId = _XylanNtpAccessKeyIdKeyId_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 1, 1, 1),
    _XylanNtpAccessKeyIdKeyId_Type()
)
xylanNtpAccessKeyIdKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpAccessKeyIdKeyId.setStatus("mandatory")


class _XylanNtpAccessKeyIdAdmin_Type(Integer32):
    """Custom type xylanNtpAccessKeyIdAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanNtpAccessKeyIdAdmin_Type.__name__ = "Integer32"
_XylanNtpAccessKeyIdAdmin_Object = MibTableColumn
xylanNtpAccessKeyIdAdmin = _XylanNtpAccessKeyIdAdmin_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 1, 1, 2),
    _XylanNtpAccessKeyIdAdmin_Type()
)
xylanNtpAccessKeyIdAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpAccessKeyIdAdmin.setStatus("mandatory")
_XylanNtpAccessRestrictedTable_Object = MibTable
xylanNtpAccessRestrictedTable = _XylanNtpAccessRestrictedTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2)
)
if mibBuilder.loadTexts:
    xylanNtpAccessRestrictedTable.setStatus("mandatory")
_XylanNtpAccessRestrictedEntry_Object = MibTableRow
xylanNtpAccessRestrictedEntry = _XylanNtpAccessRestrictedEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1)
)
xylanNtpAccessRestrictedEntry.setIndexNames(
    (0, "XYLAN-NTP-MIB", "xylanNtpAccessRestrictedIpAddress"),
    (0, "XYLAN-NTP-MIB", "xylanNtpAccessRestrictedMask"),
)
if mibBuilder.loadTexts:
    xylanNtpAccessRestrictedEntry.setStatus("mandatory")
_XylanNtpAccessRestrictedIpAddress_Type = IpAddress
_XylanNtpAccessRestrictedIpAddress_Object = MibTableColumn
xylanNtpAccessRestrictedIpAddress = _XylanNtpAccessRestrictedIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1, 1),
    _XylanNtpAccessRestrictedIpAddress_Type()
)
xylanNtpAccessRestrictedIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpAccessRestrictedIpAddress.setStatus("mandatory")
_XylanNtpAccessRestrictedMask_Type = IpAddress
_XylanNtpAccessRestrictedMask_Object = MibTableColumn
xylanNtpAccessRestrictedMask = _XylanNtpAccessRestrictedMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1, 2),
    _XylanNtpAccessRestrictedMask_Type()
)
xylanNtpAccessRestrictedMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpAccessRestrictedMask.setStatus("mandatory")
_XylanNtpAccessRestrictedRestrictions_Type = Integer32
_XylanNtpAccessRestrictedRestrictions_Object = MibTableColumn
xylanNtpAccessRestrictedRestrictions = _XylanNtpAccessRestrictedRestrictions_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1, 3),
    _XylanNtpAccessRestrictedRestrictions_Type()
)
xylanNtpAccessRestrictedRestrictions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpAccessRestrictedRestrictions.setStatus("mandatory")
_XylanNtpAccessRestrictedCount_Type = Integer32
_XylanNtpAccessRestrictedCount_Object = MibTableColumn
xylanNtpAccessRestrictedCount = _XylanNtpAccessRestrictedCount_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1, 4),
    _XylanNtpAccessRestrictedCount_Type()
)
xylanNtpAccessRestrictedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xylanNtpAccessRestrictedCount.setStatus("mandatory")


class _XylanNtpAccessRestrictedAdmin_Type(Integer32):
    """Custom type xylanNtpAccessRestrictedAdmin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 2))
    )


_XylanNtpAccessRestrictedAdmin_Type.__name__ = "Integer32"
_XylanNtpAccessRestrictedAdmin_Object = MibTableColumn
xylanNtpAccessRestrictedAdmin = _XylanNtpAccessRestrictedAdmin_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 2, 1, 5),
    _XylanNtpAccessRestrictedAdmin_Type()
)
xylanNtpAccessRestrictedAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xylanNtpAccessRestrictedAdmin.setStatus("mandatory")
_XylanNtpAccessRereadKeyFile_Type = Integer32
_XylanNtpAccessRereadKeyFile_Object = MibScalar
xylanNtpAccessRereadKeyFile = _XylanNtpAccessRereadKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 27, 5, 3),
    _XylanNtpAccessRereadKeyFile_Type()
)
xylanNtpAccessRereadKeyFile.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    xylanNtpAccessRereadKeyFile.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLAN-NTP-MIB",
    **{"xylanNtpConfig": xylanNtpConfig,
       "xylanNtpEnable": xylanNtpEnable,
       "xylanNtpMonitorEnable": xylanNtpMonitorEnable,
       "xylanNtpPeerTable": xylanNtpPeerTable,
       "xylanNtpPeerEntry": xylanNtpPeerEntry,
       "xylanNtpPeerAddress": xylanNtpPeerAddress,
       "xylanNtpPeerType": xylanNtpPeerType,
       "xylanNtpPeerAuth": xylanNtpPeerAuth,
       "xylanNtpPeerVersion": xylanNtpPeerVersion,
       "xylanNtpPeerMinpoll": xylanNtpPeerMinpoll,
       "xylanNtpPeerPrefer": xylanNtpPeerPrefer,
       "xylanNtpPeerAdmin": xylanNtpPeerAdmin,
       "xylanNtpPeerName": xylanNtpPeerName,
       "xylanNtpAuthDelay": xylanNtpAuthDelay,
       "xylanNtpKeysFile": xylanNtpKeysFile,
       "xylanNtpConfigReqKeyId": xylanNtpConfigReqKeyId,
       "xylanNtpConfigCtlKeyId": xylanNtpConfigCtlKeyId,
       "xylanNtpConfigCfgKeyId": xylanNtpConfigCfgKeyId,
       "xylanNtpPrecision": xylanNtpPrecision,
       "xylanNtpInfo": xylanNtpInfo,
       "xylanNtpPeerListTable": xylanNtpPeerListTable,
       "xylanNtpPeerListEntry": xylanNtpPeerListEntry,
       "xylanNtpPeerListAddress": xylanNtpPeerListAddress,
       "xylanNtpPeerListLocal": xylanNtpPeerListLocal,
       "xylanNtpPeerListStratum": xylanNtpPeerListStratum,
       "xylanNtpPeerListPoll": xylanNtpPeerListPoll,
       "xylanNtpPeerListReach": xylanNtpPeerListReach,
       "xylanNtpPeerListDelay": xylanNtpPeerListDelay,
       "xylanNtpPeerListOffset": xylanNtpPeerListOffset,
       "xylanNtpPeerListDispersion": xylanNtpPeerListDispersion,
       "xylanNtpPeerListSynced": xylanNtpPeerListSynced,
       "xylanNtpPeerListName": xylanNtpPeerListName,
       "xylanNtpLocalInfo": xylanNtpLocalInfo,
       "xylanNtpInfoPeer": xylanNtpInfoPeer,
       "xylanNtpInfoMode": xylanNtpInfoMode,
       "xylanNtpInfoLeapIndicator": xylanNtpInfoLeapIndicator,
       "xylanNtpInfoStratum": xylanNtpInfoStratum,
       "xylanNtpInfoPrecision": xylanNtpInfoPrecision,
       "xylanNtpInfoDistance": xylanNtpInfoDistance,
       "xylanNtpInfoDispersion": xylanNtpInfoDispersion,
       "xylanNtpInfoReferenceId": xylanNtpInfoReferenceId,
       "xylanNtpInfoReferenceTime": xylanNtpInfoReferenceTime,
       "xylanNtpInfoFrequency": xylanNtpInfoFrequency,
       "xylanNtpInfoStability": xylanNtpInfoStability,
       "xylanNtpInfoBroadcastDelay": xylanNtpInfoBroadcastDelay,
       "xylanNtpInfoAuthDelay": xylanNtpInfoAuthDelay,
       "xylanNtpPeerShowTable": xylanNtpPeerShowTable,
       "xylanNtpPeerShowEntry": xylanNtpPeerShowEntry,
       "xylanNtpPeerShowRemote": xylanNtpPeerShowRemote,
       "xylanNtpPeerShowLocal": xylanNtpPeerShowLocal,
       "xylanNtpPeerShowHmode": xylanNtpPeerShowHmode,
       "xylanNtpPeerShowPmode": xylanNtpPeerShowPmode,
       "xylanNtpPeerShowStratum": xylanNtpPeerShowStratum,
       "xylanNtpPeerShowPrecision": xylanNtpPeerShowPrecision,
       "xylanNtpPeerShowLeapIndicator": xylanNtpPeerShowLeapIndicator,
       "xylanNtpPeerShowReferenceId": xylanNtpPeerShowReferenceId,
       "xylanNtpPeerShowRootDistance": xylanNtpPeerShowRootDistance,
       "xylanNtpPeerShowRootDispersion": xylanNtpPeerShowRootDispersion,
       "xylanNtpPeerShowPpoll": xylanNtpPeerShowPpoll,
       "xylanNtpPeerShowHpoll": xylanNtpPeerShowHpoll,
       "xylanNtpPeerShowKeyid": xylanNtpPeerShowKeyid,
       "xylanNtpPeerShowVersion": xylanNtpPeerShowVersion,
       "xylanNtpPeerShowAssociation": xylanNtpPeerShowAssociation,
       "xylanNtpPeerShowValid": xylanNtpPeerShowValid,
       "xylanNtpPeerShowReach": xylanNtpPeerShowReach,
       "xylanNtpPeerShowUnreach": xylanNtpPeerShowUnreach,
       "xylanNtpPeerShowFlash": xylanNtpPeerShowFlash,
       "xylanNtpPeerShowBroadcastOffset": xylanNtpPeerShowBroadcastOffset,
       "xylanNtpPeerShowTTL": xylanNtpPeerShowTTL,
       "xylanNtpPeerShowTimer": xylanNtpPeerShowTimer,
       "xylanNtpPeerShowFlags": xylanNtpPeerShowFlags,
       "xylanNtpPeerShowReferenceTime": xylanNtpPeerShowReferenceTime,
       "xylanNtpPeerShowOriginateTime": xylanNtpPeerShowOriginateTime,
       "xylanNtpPeerShowReceiveTime": xylanNtpPeerShowReceiveTime,
       "xylanNtpPeerShowTransmitTime": xylanNtpPeerShowTransmitTime,
       "xylanNtpPeerShowOffset": xylanNtpPeerShowOffset,
       "xylanNtpPeerShowDelay": xylanNtpPeerShowDelay,
       "xylanNtpPeerShowDispersion": xylanNtpPeerShowDispersion,
       "xylanNtpPeerShowName": xylanNtpPeerShowName,
       "xylanNtpStats": xylanNtpStats,
       "xylanNtpStatsStat": xylanNtpStatsStat,
       "xylanNtpStatsStatUptime": xylanNtpStatsStatUptime,
       "xylanNtpStatsStatReset": xylanNtpStatsStatReset,
       "xylanNtpStatsStatBadStratum": xylanNtpStatsStatBadStratum,
       "xylanNtpStatsStatOldVersion": xylanNtpStatsStatOldVersion,
       "xylanNtpStatsStatNewVersion": xylanNtpStatsStatNewVersion,
       "xylanNtpStatsStatUnknownVersion": xylanNtpStatsStatUnknownVersion,
       "xylanNtpStatsStatBadLength": xylanNtpStatsStatBadLength,
       "xylanNtpStatsStatProcessed": xylanNtpStatsStatProcessed,
       "xylanNtpStatsStatBadAuth": xylanNtpStatsStatBadAuth,
       "xylanNtpStatsStatLimitRejects": xylanNtpStatsStatLimitRejects,
       "xylanNtpStatsPeerTable": xylanNtpStatsPeerTable,
       "xylanNtpStatsPeerEntry": xylanNtpStatsPeerEntry,
       "xylanNtpStatsPeerAddress": xylanNtpStatsPeerAddress,
       "xylanNtpStatsPeerLocal": xylanNtpStatsPeerLocal,
       "xylanNtpStatsPeerLastRcv": xylanNtpStatsPeerLastRcv,
       "xylanNtpStatsPeerNextSend": xylanNtpStatsPeerNextSend,
       "xylanNtpStatsPeerReachChange": xylanNtpStatsPeerReachChange,
       "xylanNtpStatsPeerPacketsSent": xylanNtpStatsPeerPacketsSent,
       "xylanNtpStatsPeerPacketsRcvd": xylanNtpStatsPeerPacketsRcvd,
       "xylanNtpStatsPeerBadAuth": xylanNtpStatsPeerBadAuth,
       "xylanNtpStatsPeerBogusOrigin": xylanNtpStatsPeerBogusOrigin,
       "xylanNtpStatsPeerDuplicate": xylanNtpStatsPeerDuplicate,
       "xylanNtpStatsPeerBadDispersion": xylanNtpStatsPeerBadDispersion,
       "xylanNtpStatsPeerBadRefTime": xylanNtpStatsPeerBadRefTime,
       "xylanNtpStatsPeerCandidateOrder": xylanNtpStatsPeerCandidateOrder,
       "xylanNtpStatsPeerReset": xylanNtpStatsPeerReset,
       "xylanNtpStatsPeerName": xylanNtpStatsPeerName,
       "xylanNtpStatsLoop": xylanNtpStatsLoop,
       "xylanNtpStatsLoopOffset": xylanNtpStatsLoopOffset,
       "xylanNtpStatsLoopFrequency": xylanNtpStatsLoopFrequency,
       "xylanNtpStatsLoopPollAdjust": xylanNtpStatsLoopPollAdjust,
       "xylanNtpStatsLoopWatchdog": xylanNtpStatsLoopWatchdog,
       "xylanNtpStatsIo": xylanNtpStatsIo,
       "xylanNtpStatsIoReset": xylanNtpStatsIoReset,
       "xylanNtpStatsIoRcvBuffers": xylanNtpStatsIoRcvBuffers,
       "xylanNtpStatsIoFreeRcvBuffers": xylanNtpStatsIoFreeRcvBuffers,
       "xylanNtpStatsIoUsedRcvBuffers": xylanNtpStatsIoUsedRcvBuffers,
       "xylanNtpStatsIoRefills": xylanNtpStatsIoRefills,
       "xylanNtpStatsIoDroppedPackets": xylanNtpStatsIoDroppedPackets,
       "xylanNtpStatsIoIgnoredPackets": xylanNtpStatsIoIgnoredPackets,
       "xylanNtpStatsIoRcvPackets": xylanNtpStatsIoRcvPackets,
       "xylanNtpStatsIoSentPackets": xylanNtpStatsIoSentPackets,
       "xylanNtpStatsIoNotSentPackets": xylanNtpStatsIoNotSentPackets,
       "xylanNtpStatsIoInterrupts": xylanNtpStatsIoInterrupts,
       "xylanNtpStatsIoInterruptsRcv": xylanNtpStatsIoInterruptsRcv,
       "xylanNtpStatsReset": xylanNtpStatsReset,
       "xylanNtpStatsMonitorTable": xylanNtpStatsMonitorTable,
       "xylanNtpStatsMonitorEntry": xylanNtpStatsMonitorEntry,
       "xylanNtpStatsMonitorIndex": xylanNtpStatsMonitorIndex,
       "xylanNtpStatsMonitorAddress": xylanNtpStatsMonitorAddress,
       "xylanNtpStatsMonitorPort": xylanNtpStatsMonitorPort,
       "xylanNtpStatsMonitorLocalAddress": xylanNtpStatsMonitorLocalAddress,
       "xylanNtpStatsMonitorCount": xylanNtpStatsMonitorCount,
       "xylanNtpStatsMonitorMode": xylanNtpStatsMonitorMode,
       "xylanNtpStatsMonitorVersion": xylanNtpStatsMonitorVersion,
       "xylanNtpStatsMonitorDrop": xylanNtpStatsMonitorDrop,
       "xylanNtpStatsMonitorLast": xylanNtpStatsMonitorLast,
       "xylanNtpStatsMonitorFirst": xylanNtpStatsMonitorFirst,
       "xylanNtpStatsMonitorName": xylanNtpStatsMonitorName,
       "xylanNtpAdmin": xylanNtpAdmin,
       "xylanNtpAccess": xylanNtpAccess,
       "xylanNtpAccessKeyIdTable": xylanNtpAccessKeyIdTable,
       "xylanNtpAccessKeyIdEntry": xylanNtpAccessKeyIdEntry,
       "xylanNtpAccessKeyIdKeyId": xylanNtpAccessKeyIdKeyId,
       "xylanNtpAccessKeyIdAdmin": xylanNtpAccessKeyIdAdmin,
       "xylanNtpAccessRestrictedTable": xylanNtpAccessRestrictedTable,
       "xylanNtpAccessRestrictedEntry": xylanNtpAccessRestrictedEntry,
       "xylanNtpAccessRestrictedIpAddress": xylanNtpAccessRestrictedIpAddress,
       "xylanNtpAccessRestrictedMask": xylanNtpAccessRestrictedMask,
       "xylanNtpAccessRestrictedRestrictions": xylanNtpAccessRestrictedRestrictions,
       "xylanNtpAccessRestrictedCount": xylanNtpAccessRestrictedCount,
       "xylanNtpAccessRestrictedAdmin": xylanNtpAccessRestrictedAdmin,
       "xylanNtpAccessRereadKeyFile": xylanNtpAccessRereadKeyFile}
)
