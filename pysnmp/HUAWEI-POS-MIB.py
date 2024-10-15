# SNMP MIB module (HUAWEI-POS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-POS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:35 2024
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

(huawei,
 mlsr) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "huawei",
    "mlsr")

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


# MODULE-IDENTITY

pos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8)
)
pos.setRevisions(
        ("2004-10-12 00:00",
         "2004-07-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PosAppTable_Object = MibTable
posAppTable = _PosAppTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1)
)
if mibBuilder.loadTexts:
    posAppTable.setStatus("current")
_PosAppEntry_Object = MibTableRow
posAppEntry = _PosAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1)
)
posAppEntry.setIndexNames(
    (0, "HUAWEI-POS-MIB", "posAppId"),
)
if mibBuilder.loadTexts:
    posAppEntry.setStatus("current")


class _PosAppId_Type(Integer32):
    """Custom type posAppId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PosAppId_Type.__name__ = "Integer32"
_PosAppId_Object = MibTableColumn
posAppId = _PosAppId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 1),
    _PosAppId_Type()
)
posAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posAppId.setStatus("current")


class _PosAppConnectMode_Type(Integer32):
    """Custom type posAppConnectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flow", 2),
          ("pad", 3),
          ("tcp", 1))
    )


_PosAppConnectMode_Type.__name__ = "Integer32"
_PosAppConnectMode_Object = MibTableColumn
posAppConnectMode = _PosAppConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 2),
    _PosAppConnectMode_Type()
)
posAppConnectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posAppConnectMode.setStatus("current")


class _PosAppState_Type(Integer32):
    """Custom type posAppState based on Integer32"""
    defaultValue = 1

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
        *(("down", 2),
          ("kept", 5),
          ("linked", 7),
          ("linking", 6),
          ("noset", 1),
          ("ok", 4),
          ("up", 3))
    )


_PosAppState_Type.__name__ = "Integer32"
_PosAppState_Object = MibTableColumn
posAppState = _PosAppState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 3),
    _PosAppState_Type()
)
posAppState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posAppState.setStatus("current")


class _PosAppIfIndex_Type(Integer32):
    """Custom type posAppIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PosAppIfIndex_Type.__name__ = "Integer32"
_PosAppIfIndex_Object = MibTableColumn
posAppIfIndex = _PosAppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 4),
    _PosAppIfIndex_Type()
)
posAppIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posAppIfIndex.setStatus("current")
_PosAppHostIP_Type = IpAddress
_PosAppHostIP_Object = MibTableColumn
posAppHostIP = _PosAppHostIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 5),
    _PosAppHostIP_Type()
)
posAppHostIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posAppHostIP.setStatus("current")


class _PosAppPort_Type(Integer32):
    """Custom type posAppPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PosAppPort_Type.__name__ = "Integer32"
_PosAppPort_Object = MibTableColumn
posAppPort = _PosAppPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 6),
    _PosAppPort_Type()
)
posAppPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posAppPort.setStatus("current")
_PosAppSourceIp_Type = IpAddress
_PosAppSourceIp_Object = MibTableColumn
posAppSourceIp = _PosAppSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 7),
    _PosAppSourceIp_Type()
)
posAppSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posAppSourceIp.setStatus("current")


class _PosAppRecvPacCounter_Type(Counter32):
    """Custom type posAppRecvPacCounter based on Counter32"""
    defaultValue = 0


_PosAppRecvPacCounter_Object = MibTableColumn
posAppRecvPacCounter = _PosAppRecvPacCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 8),
    _PosAppRecvPacCounter_Type()
)
posAppRecvPacCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posAppRecvPacCounter.setStatus("current")


class _PosAppErrPacCounter_Type(Counter32):
    """Custom type posAppErrPacCounter based on Counter32"""
    defaultValue = 0


_PosAppErrPacCounter_Object = MibTableColumn
posAppErrPacCounter = _PosAppErrPacCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 9),
    _PosAppErrPacCounter_Type()
)
posAppErrPacCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posAppErrPacCounter.setStatus("current")


class _PosAppDistrErrCounter_Type(Counter32):
    """Custom type posAppDistrErrCounter based on Counter32"""
    defaultValue = 0


_PosAppDistrErrCounter_Object = MibTableColumn
posAppDistrErrCounter = _PosAppDistrErrCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 10),
    _PosAppDistrErrCounter_Type()
)
posAppDistrErrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posAppDistrErrCounter.setStatus("current")


class _PosAppBuffedCounter_Type(Counter32):
    """Custom type posAppBuffedCounter based on Counter32"""
    defaultValue = 0


_PosAppBuffedCounter_Object = MibTableColumn
posAppBuffedCounter = _PosAppBuffedCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 11),
    _PosAppBuffedCounter_Type()
)
posAppBuffedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posAppBuffedCounter.setStatus("current")


class _PosAppDiscardedCounter_Type(Counter32):
    """Custom type posAppDiscardedCounter based on Counter32"""
    defaultValue = 0


_PosAppDiscardedCounter_Object = MibTableColumn
posAppDiscardedCounter = _PosAppDiscardedCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 12),
    _PosAppDiscardedCounter_Type()
)
posAppDiscardedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posAppDiscardedCounter.setStatus("current")


class _PosAppDebug_Type(Integer32):
    """Custom type posAppDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("open", 2))
    )


_PosAppDebug_Type.__name__ = "Integer32"
_PosAppDebug_Object = MibTableColumn
posAppDebug = _PosAppDebug_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 13),
    _PosAppDebug_Type()
)
posAppDebug.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posAppDebug.setStatus("current")
_PosAppRowStatus_Type = RowStatus
_PosAppRowStatus_Object = MibTableColumn
posAppRowStatus = _PosAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 14),
    _PosAppRowStatus_Type()
)
posAppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posAppRowStatus.setStatus("current")


class _PosAppX121Addr_Type(OctetString):
    """Custom type posAppX121Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_PosAppX121Addr_Type.__name__ = "OctetString"
_PosAppX121Addr_Object = MibTableColumn
posAppX121Addr = _PosAppX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 1, 1, 15),
    _PosAppX121Addr_Type()
)
posAppX121Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posAppX121Addr.setStatus("current")
_PosInterTable_Object = MibTable
posInterTable = _PosInterTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2)
)
if mibBuilder.loadTexts:
    posInterTable.setStatus("current")
_PosInterEntry_Object = MibTableRow
posInterEntry = _PosInterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1)
)
posInterEntry.setIndexNames(
    (0, "HUAWEI-POS-MIB", "posPosId"),
)
if mibBuilder.loadTexts:
    posInterEntry.setStatus("current")


class _PosPosId_Type(Integer32):
    """Custom type posPosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PosPosId_Type.__name__ = "Integer32"
_PosPosId_Object = MibTableColumn
posPosId = _PosPosId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1, 1),
    _PosPosId_Type()
)
posPosId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posPosId.setStatus("current")


class _PosPosIfIndex_Type(Integer32):
    """Custom type posPosIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PosPosIfIndex_Type.__name__ = "Integer32"
_PosPosIfIndex_Object = MibTableColumn
posPosIfIndex = _PosPosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1, 2),
    _PosPosIfIndex_Type()
)
posPosIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posPosIfIndex.setStatus("current")


class _PosPosConnectState_Type(Integer32):
    """Custom type posPosConnectState based on Integer32"""
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
        *(("down", 2),
          ("noset", 1),
          ("ok", 4),
          ("up", 3))
    )


_PosPosConnectState_Type.__name__ = "Integer32"
_PosPosConnectState_Object = MibTableColumn
posPosConnectState = _PosPosConnectState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1, 3),
    _PosPosConnectState_Type()
)
posPosConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posPosConnectState.setStatus("current")


class _PosPosRecvPacCounter_Type(Counter32):
    """Custom type posPosRecvPacCounter based on Counter32"""
    defaultValue = 0


_PosPosRecvPacCounter_Object = MibTableColumn
posPosRecvPacCounter = _PosPosRecvPacCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1, 4),
    _PosPosRecvPacCounter_Type()
)
posPosRecvPacCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posPosRecvPacCounter.setStatus("current")


class _PosPosErrPacCounter_Type(Counter32):
    """Custom type posPosErrPacCounter based on Counter32"""
    defaultValue = 0


_PosPosErrPacCounter_Object = MibTableColumn
posPosErrPacCounter = _PosPosErrPacCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1, 5),
    _PosPosErrPacCounter_Type()
)
posPosErrPacCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posPosErrPacCounter.setStatus("current")


class _PosPosMapErrCounter_Type(Counter32):
    """Custom type posPosMapErrCounter based on Counter32"""
    defaultValue = 0


_PosPosMapErrCounter_Object = MibTableColumn
posPosMapErrCounter = _PosPosMapErrCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1, 6),
    _PosPosMapErrCounter_Type()
)
posPosMapErrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posPosMapErrCounter.setStatus("current")


class _PosPosBuffedCounter_Type(Counter32):
    """Custom type posPosBuffedCounter based on Counter32"""
    defaultValue = 0


_PosPosBuffedCounter_Object = MibTableColumn
posPosBuffedCounter = _PosPosBuffedCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1, 7),
    _PosPosBuffedCounter_Type()
)
posPosBuffedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posPosBuffedCounter.setStatus("current")


class _PosPosDiscardedCounter_Type(Counter32):
    """Custom type posPosDiscardedCounter based on Counter32"""
    defaultValue = 0


_PosPosDiscardedCounter_Object = MibTableColumn
posPosDiscardedCounter = _PosPosDiscardedCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1, 8),
    _PosPosDiscardedCounter_Type()
)
posPosDiscardedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posPosDiscardedCounter.setStatus("current")


class _PosPosInterDebug_Type(Integer32):
    """Custom type posPosInterDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("open", 2))
    )


_PosPosInterDebug_Type.__name__ = "Integer32"
_PosPosInterDebug_Object = MibTableColumn
posPosInterDebug = _PosPosInterDebug_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1, 9),
    _PosPosInterDebug_Type()
)
posPosInterDebug.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posPosInterDebug.setStatus("current")
_PosPosInterRowStatus_Type = RowStatus
_PosPosInterRowStatus_Object = MibTableColumn
posPosInterRowStatus = _PosPosInterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1, 10),
    _PosPosInterRowStatus_Type()
)
posPosInterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posPosInterRowStatus.setStatus("current")


class _PosPosInterType_Type(Integer32):
    """Custom type posPosInterType based on Integer32"""
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
        *(("asy", 2),
          ("fcm", 1),
          ("pad-client", 3),
          ("pad-server", 4))
    )


_PosPosInterType_Type.__name__ = "Integer32"
_PosPosInterType_Object = MibTableColumn
posPosInterType = _PosPosInterType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 2, 1, 11),
    _PosPosInterType_Type()
)
posPosInterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posPosInterType.setStatus("current")
_PosMapTable_Object = MibTable
posMapTable = _PosMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 3)
)
if mibBuilder.loadTexts:
    posMapTable.setStatus("current")
_PosMapEntry_Object = MibTableRow
posMapEntry = _PosMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 3, 1)
)
posMapEntry.setIndexNames(
    (0, "HUAWEI-POS-MIB", "posMapDes"),
)
if mibBuilder.loadTexts:
    posMapEntry.setStatus("current")


class _PosMapDes_Type(Integer32):
    """Custom type posMapDes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_PosMapDes_Type.__name__ = "Integer32"
_PosMapDes_Object = MibTableColumn
posMapDes = _PosMapDes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 3, 1, 1),
    _PosMapDes_Type()
)
posMapDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posMapDes.setStatus("current")


class _PosMapAppNumber_Type(Integer32):
    """Custom type posMapAppNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_PosMapAppNumber_Type.__name__ = "Integer32"
_PosMapAppNumber_Object = MibTableColumn
posMapAppNumber = _PosMapAppNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 3, 1, 2),
    _PosMapAppNumber_Type()
)
posMapAppNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posMapAppNumber.setStatus("current")
_PosMapRowStatus_Type = RowStatus
_PosMapRowStatus_Object = MibTableColumn
posMapRowStatus = _PosMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 3, 1, 3),
    _PosMapRowStatus_Type()
)
posMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posMapRowStatus.setStatus("current")
_PosAsyAppTable_Object = MibTable
posAsyAppTable = _PosAsyAppTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 4)
)
if mibBuilder.loadTexts:
    posAsyAppTable.setStatus("current")
_PosAsyAppEntry_Object = MibTableRow
posAsyAppEntry = _PosAsyAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 4, 1)
)
posAsyAppEntry.setIndexNames(
    (0, "HUAWEI-POS-MIB", "posAsyAppIfIndex"),
)
if mibBuilder.loadTexts:
    posAsyAppEntry.setStatus("current")


class _PosAsyAppIfIndex_Type(Integer32):
    """Custom type posAsyAppIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PosAsyAppIfIndex_Type.__name__ = "Integer32"
_PosAsyAppIfIndex_Object = MibTableColumn
posAsyAppIfIndex = _PosAsyAppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 4, 1, 1),
    _PosAsyAppIfIndex_Type()
)
posAsyAppIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posAsyAppIfIndex.setStatus("current")
_PosAsyAppRowStatus_Type = RowStatus
_PosAsyAppRowStatus_Object = MibTableColumn
posAsyAppRowStatus = _PosAsyAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 4, 1, 2),
    _PosAsyAppRowStatus_Type()
)
posAsyAppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posAsyAppRowStatus.setStatus("current")
_PosFCMTable_Object = MibTable
posFCMTable = _PosFCMTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 5)
)
if mibBuilder.loadTexts:
    posFCMTable.setStatus("current")
_PosFCMEntry_Object = MibTableRow
posFCMEntry = _PosFCMEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 5, 1)
)
posFCMEntry.setIndexNames(
    (0, "HUAWEI-POS-MIB", "posFCMIfIndex"),
)
if mibBuilder.loadTexts:
    posFCMEntry.setStatus("current")


class _PosFCMIfIndex_Type(Integer32):
    """Custom type posFCMIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PosFCMIfIndex_Type.__name__ = "Integer32"
_PosFCMIfIndex_Object = MibTableColumn
posFCMIfIndex = _PosFCMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 5, 1, 1),
    _PosFCMIfIndex_Type()
)
posFCMIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posFCMIfIndex.setStatus("current")


class _PosFCMTimeoutCounter_Type(Counter32):
    """Custom type posFCMTimeoutCounter based on Counter32"""
    defaultValue = 0


_PosFCMTimeoutCounter_Object = MibTableColumn
posFCMTimeoutCounter = _PosFCMTimeoutCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 5, 1, 3),
    _PosFCMTimeoutCounter_Type()
)
posFCMTimeoutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posFCMTimeoutCounter.setStatus("current")


class _PosFCMConnectFailCounter_Type(Counter32):
    """Custom type posFCMConnectFailCounter based on Counter32"""
    defaultValue = 0


_PosFCMConnectFailCounter_Object = MibTableColumn
posFCMConnectFailCounter = _PosFCMConnectFailCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 5, 1, 4),
    _PosFCMConnectFailCounter_Type()
)
posFCMConnectFailCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posFCMConnectFailCounter.setStatus("current")


class _PosAppSum_Type(Integer32):
    """Custom type posAppSum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_PosAppSum_Type.__name__ = "Integer32"
_PosAppSum_Object = MibScalar
posAppSum = _PosAppSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 6),
    _PosAppSum_Type()
)
posAppSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posAppSum.setStatus("current")


class _PosInterSum_Type(Integer32):
    """Custom type posInterSum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_PosInterSum_Type.__name__ = "Integer32"
_PosInterSum_Object = MibScalar
posInterSum = _PosInterSum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 7),
    _PosInterSum_Type()
)
posInterSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    posInterSum.setStatus("current")


class _PosEnable_Type(Integer32):
    """Custom type posEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PosEnable_Type.__name__ = "Integer32"
_PosEnable_Object = MibScalar
posEnable = _PosEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 8),
    _PosEnable_Type()
)
posEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posEnable.setStatus("current")


class _PosAppDebugAll_Type(Integer32):
    """Custom type posAppDebugAll based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("open", 2))
    )


_PosAppDebugAll_Type.__name__ = "Integer32"
_PosAppDebugAll_Object = MibScalar
posAppDebugAll = _PosAppDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 9),
    _PosAppDebugAll_Type()
)
posAppDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posAppDebugAll.setStatus("current")


class _PosPosDebugAll_Type(Integer32):
    """Custom type posPosDebugAll based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 1),
          ("open", 2))
    )


_PosPosDebugAll_Type.__name__ = "Integer32"
_PosPosDebugAll_Object = MibScalar
posPosDebugAll = _PosPosDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 10),
    _PosPosDebugAll_Type()
)
posPosDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posPosDebugAll.setStatus("current")


class _PosClearPacCounter_Type(Integer32):
    """Custom type posClearPacCounter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("counting", 2))
    )


_PosClearPacCounter_Type.__name__ = "Integer32"
_PosClearPacCounter_Object = MibScalar
posClearPacCounter = _PosClearPacCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 11),
    _PosClearPacCounter_Type()
)
posClearPacCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posClearPacCounter.setStatus("current")


class _PosClearFCMCounter_Type(Integer32):
    """Custom type posClearFCMCounter based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("counting", 2))
    )


_PosClearFCMCounter_Type.__name__ = "Integer32"
_PosClearFCMCounter_Object = MibScalar
posClearFCMCounter = _PosClearFCMCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 12),
    _PosClearFCMCounter_Type()
)
posClearFCMCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posClearFCMCounter.setStatus("current")


class _PosEnableTrap_Type(Integer32):
    """Custom type posEnableTrap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PosEnableTrap_Type.__name__ = "Integer32"
_PosEnableTrap_Object = MibScalar
posEnableTrap = _PosEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 13),
    _PosEnableTrap_Type()
)
posEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posEnableTrap.setStatus("current")


class _PosFCMAnswerTime_Type(Integer32):
    """Custom type posFCMAnswerTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2000),
    )


_PosFCMAnswerTime_Type.__name__ = "Integer32"
_PosFCMAnswerTime_Object = MibScalar
posFCMAnswerTime = _PosFCMAnswerTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 14),
    _PosFCMAnswerTime_Type()
)
posFCMAnswerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posFCMAnswerTime.setStatus("current")


class _PosFCMTradeTime_Type(Integer32):
    """Custom type posFCMTradeTime based on Integer32"""
    defaultValue = 60000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 1200000),
    )


_PosFCMTradeTime_Type.__name__ = "Integer32"
_PosFCMTradeTime_Object = MibScalar
posFCMTradeTime = _PosFCMTradeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 15),
    _PosFCMTradeTime_Type()
)
posFCMTradeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posFCMTradeTime.setStatus("current")


class _PosFCMPacketInterval_Type(Integer32):
    """Custom type posFCMPacketInterval based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3500, 10000),
    )


_PosFCMPacketInterval_Type.__name__ = "Integer32"
_PosFCMPacketInterval_Object = MibScalar
posFCMPacketInterval = _PosFCMPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 16),
    _PosFCMPacketInterval_Type()
)
posFCMPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posFCMPacketInterval.setStatus("current")
_PosTrap_ObjectIdentity = ObjectIdentity
posTrap = _PosTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17)
)


class _PosPadWaitTime_Type(Integer32):
    """Custom type posPadWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_PosPadWaitTime_Type.__name__ = "Integer32"
_PosPadWaitTime_Object = MibScalar
posPadWaitTime = _PosPadWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 18),
    _PosPadWaitTime_Type()
)
posPadWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posPadWaitTime.setStatus("current")


class _PosPadIdleTimeout_Type(Integer32):
    """Custom type posPadIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_PosPadIdleTimeout_Type.__name__ = "Integer32"
_PosPadIdleTimeout_Object = MibScalar
posPadIdleTimeout = _PosPadIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 19),
    _PosPadIdleTimeout_Type()
)
posPadIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posPadIdleTimeout.setStatus("current")


class _PosPadPacType_Type(Integer32):
    """Custom type posPadPacType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("asy", 2),
          ("syn", 1))
    )


_PosPadPacType_Type.__name__ = "Integer32"
_PosPadPacType_Object = MibScalar
posPadPacType = _PosPadPacType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 20),
    _PosPadPacType_Type()
)
posPadPacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posPadPacType.setStatus("current")


class _PosPadCheckSChar_Type(Integer32):
    """Custom type posPadCheckSChar based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PosPadCheckSChar_Type.__name__ = "Integer32"
_PosPadCheckSChar_Object = MibScalar
posPadCheckSChar = _PosPadCheckSChar_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 21),
    _PosPadCheckSChar_Type()
)
posPadCheckSChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    posPadCheckSChar.setStatus("current")
_PosPadTable_Object = MibTable
posPadTable = _PosPadTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 22)
)
if mibBuilder.loadTexts:
    posPadTable.setStatus("current")
_PosPadEntry_Object = MibTableRow
posPadEntry = _PosPadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 22, 1)
)
posPadEntry.setIndexNames(
    (0, "HUAWEI-POS-MIB", "posPadIfIndex"),
)
if mibBuilder.loadTexts:
    posPadEntry.setStatus("current")


class _PosPadIfIndex_Type(Integer32):
    """Custom type posPadIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PosPadIfIndex_Type.__name__ = "Integer32"
_PosPadIfIndex_Object = MibTableColumn
posPadIfIndex = _PosPadIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 22, 1, 1),
    _PosPadIfIndex_Type()
)
posPadIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    posPadIfIndex.setStatus("current")
_PosPadRowStatus_Type = RowStatus
_PosPadRowStatus_Object = MibTableColumn
posPadRowStatus = _PosPadRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 22, 1, 2),
    _PosPadRowStatus_Type()
)
posPadRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    posPadRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

posAppNotReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 1)
)
posAppNotReadyTrap.setObjects(
    ("HUAWEI-POS-MIB", "posAppId")
)
if mibBuilder.loadTexts:
    posAppNotReadyTrap.setStatus(
        "current"
    )

posAppConnectFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 2)
)
posAppConnectFailTrap.setObjects(
    ("HUAWEI-POS-MIB", "posAppId")
)
if mibBuilder.loadTexts:
    posAppConnectFailTrap.setStatus(
        "current"
    )

posAppStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 3)
)
posAppStateChangeTrap.setObjects(
      *(("HUAWEI-POS-MIB", "posAppId"),
        ("HUAWEI-POS-MIB", "posAppState"))
)
if mibBuilder.loadTexts:
    posAppStateChangeTrap.setStatus(
        "current"
    )

posAppNotConfigedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 4)
)
posAppNotConfigedTrap.setObjects(
    ("HUAWEI-POS-MIB", "posAppId")
)
if mibBuilder.loadTexts:
    posAppNotConfigedTrap.setStatus(
        "current"
    )

posAppBuffOverFlowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 5)
)
posAppBuffOverFlowTrap.setObjects(
    ("HUAWEI-POS-MIB", "posAppId")
)
if mibBuilder.loadTexts:
    posAppBuffOverFlowTrap.setStatus(
        "current"
    )

posAppDebugOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 6)
)
posAppDebugOpenTrap.setObjects(
    ("HUAWEI-POS-MIB", "posAppId")
)
if mibBuilder.loadTexts:
    posAppDebugOpenTrap.setStatus(
        "current"
    )

posAppDebugAllOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 7)
)
if mibBuilder.loadTexts:
    posAppDebugAllOpenTrap.setStatus(
        "current"
    )

posInterBuffOverFlowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 8)
)
if mibBuilder.loadTexts:
    posInterBuffOverFlowTrap.setStatus(
        "current"
    )

posInterStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 9)
)
posInterStateChangeTrap.setObjects(
      *(("HUAWEI-POS-MIB", "posPosId"),
        ("HUAWEI-POS-MIB", "posPosConnectState"))
)
if mibBuilder.loadTexts:
    posInterStateChangeTrap.setStatus(
        "current"
    )

posInterDebugOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 10)
)
posInterDebugOpenTrap.setObjects(
    ("HUAWEI-POS-MIB", "posPosId")
)
if mibBuilder.loadTexts:
    posInterDebugOpenTrap.setStatus(
        "current"
    )

posInterDebugAllOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 11)
)
if mibBuilder.loadTexts:
    posInterDebugAllOpenTrap.setStatus(
        "current"
    )

posFCMTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 12)
)
posFCMTimeoutTrap.setObjects(
    ("HUAWEI-POS-MIB", "posFCMIfIndex")
)
if mibBuilder.loadTexts:
    posFCMTimeoutTrap.setStatus(
        "current"
    )

posFCMConnectFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 13)
)
posFCMConnectFailTrap.setObjects(
    ("HUAWEI-POS-MIB", "posFCMIfIndex")
)
if mibBuilder.loadTexts:
    posFCMConnectFailTrap.setStatus(
        "current"
    )

posClearPacketCounter = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 14)
)
if mibBuilder.loadTexts:
    posClearPacketCounter.setStatus(
        "current"
    )

posClearFcmCounter = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 8, 17, 15)
)
if mibBuilder.loadTexts:
    posClearFcmCounter.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-POS-MIB",
    **{"pos": pos,
       "posAppTable": posAppTable,
       "posAppEntry": posAppEntry,
       "posAppId": posAppId,
       "posAppConnectMode": posAppConnectMode,
       "posAppState": posAppState,
       "posAppIfIndex": posAppIfIndex,
       "posAppHostIP": posAppHostIP,
       "posAppPort": posAppPort,
       "posAppSourceIp": posAppSourceIp,
       "posAppRecvPacCounter": posAppRecvPacCounter,
       "posAppErrPacCounter": posAppErrPacCounter,
       "posAppDistrErrCounter": posAppDistrErrCounter,
       "posAppBuffedCounter": posAppBuffedCounter,
       "posAppDiscardedCounter": posAppDiscardedCounter,
       "posAppDebug": posAppDebug,
       "posAppRowStatus": posAppRowStatus,
       "posAppX121Addr": posAppX121Addr,
       "posInterTable": posInterTable,
       "posInterEntry": posInterEntry,
       "posPosId": posPosId,
       "posPosIfIndex": posPosIfIndex,
       "posPosConnectState": posPosConnectState,
       "posPosRecvPacCounter": posPosRecvPacCounter,
       "posPosErrPacCounter": posPosErrPacCounter,
       "posPosMapErrCounter": posPosMapErrCounter,
       "posPosBuffedCounter": posPosBuffedCounter,
       "posPosDiscardedCounter": posPosDiscardedCounter,
       "posPosInterDebug": posPosInterDebug,
       "posPosInterRowStatus": posPosInterRowStatus,
       "posPosInterType": posPosInterType,
       "posMapTable": posMapTable,
       "posMapEntry": posMapEntry,
       "posMapDes": posMapDes,
       "posMapAppNumber": posMapAppNumber,
       "posMapRowStatus": posMapRowStatus,
       "posAsyAppTable": posAsyAppTable,
       "posAsyAppEntry": posAsyAppEntry,
       "posAsyAppIfIndex": posAsyAppIfIndex,
       "posAsyAppRowStatus": posAsyAppRowStatus,
       "posFCMTable": posFCMTable,
       "posFCMEntry": posFCMEntry,
       "posFCMIfIndex": posFCMIfIndex,
       "posFCMTimeoutCounter": posFCMTimeoutCounter,
       "posFCMConnectFailCounter": posFCMConnectFailCounter,
       "posAppSum": posAppSum,
       "posInterSum": posInterSum,
       "posEnable": posEnable,
       "posAppDebugAll": posAppDebugAll,
       "posPosDebugAll": posPosDebugAll,
       "posClearPacCounter": posClearPacCounter,
       "posClearFCMCounter": posClearFCMCounter,
       "posEnableTrap": posEnableTrap,
       "posFCMAnswerTime": posFCMAnswerTime,
       "posFCMTradeTime": posFCMTradeTime,
       "posFCMPacketInterval": posFCMPacketInterval,
       "posTrap": posTrap,
       "posAppNotReadyTrap": posAppNotReadyTrap,
       "posAppConnectFailTrap": posAppConnectFailTrap,
       "posAppStateChangeTrap": posAppStateChangeTrap,
       "posAppNotConfigedTrap": posAppNotConfigedTrap,
       "posAppBuffOverFlowTrap": posAppBuffOverFlowTrap,
       "posAppDebugOpenTrap": posAppDebugOpenTrap,
       "posAppDebugAllOpenTrap": posAppDebugAllOpenTrap,
       "posInterBuffOverFlowTrap": posInterBuffOverFlowTrap,
       "posInterStateChangeTrap": posInterStateChangeTrap,
       "posInterDebugOpenTrap": posInterDebugOpenTrap,
       "posInterDebugAllOpenTrap": posInterDebugAllOpenTrap,
       "posFCMTimeoutTrap": posFCMTimeoutTrap,
       "posFCMConnectFailTrap": posFCMConnectFailTrap,
       "posClearPacketCounter": posClearPacketCounter,
       "posClearFcmCounter": posClearFcmCounter,
       "posPadWaitTime": posPadWaitTime,
       "posPadIdleTimeout": posPadIdleTimeout,
       "posPadPacType": posPadPacType,
       "posPadCheckSChar": posPadCheckSChar,
       "posPadTable": posPadTable,
       "posPadEntry": posPadEntry,
       "posPadIfIndex": posPadIfIndex,
       "posPadRowStatus": posPadRowStatus}
)
