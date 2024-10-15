# SNMP MIB module (HH3C-POS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-POS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:30 2024
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

(hh3cmlsr,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cmlsr")

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

hh3cpos = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8)
)
hh3cpos.setRevisions(
        ("2004-10-12 00:00",
         "2004-07-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cposAppTable_Object = MibTable
hh3cposAppTable = _Hh3cposAppTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1)
)
if mibBuilder.loadTexts:
    hh3cposAppTable.setStatus("current")
_Hh3cposAppEntry_Object = MibTableRow
hh3cposAppEntry = _Hh3cposAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1)
)
hh3cposAppEntry.setIndexNames(
    (0, "HH3C-POS-MIB", "hh3cposAppId"),
)
if mibBuilder.loadTexts:
    hh3cposAppEntry.setStatus("current")


class _Hh3cposAppId_Type(Integer32):
    """Custom type hh3cposAppId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Hh3cposAppId_Type.__name__ = "Integer32"
_Hh3cposAppId_Object = MibTableColumn
hh3cposAppId = _Hh3cposAppId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 1),
    _Hh3cposAppId_Type()
)
hh3cposAppId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposAppId.setStatus("current")


class _Hh3cposAppConnectMode_Type(Integer32):
    """Custom type hh3cposAppConnectMode based on Integer32"""
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


_Hh3cposAppConnectMode_Type.__name__ = "Integer32"
_Hh3cposAppConnectMode_Object = MibTableColumn
hh3cposAppConnectMode = _Hh3cposAppConnectMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 2),
    _Hh3cposAppConnectMode_Type()
)
hh3cposAppConnectMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposAppConnectMode.setStatus("current")


class _Hh3cposAppState_Type(Integer32):
    """Custom type hh3cposAppState based on Integer32"""
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


_Hh3cposAppState_Type.__name__ = "Integer32"
_Hh3cposAppState_Object = MibTableColumn
hh3cposAppState = _Hh3cposAppState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 3),
    _Hh3cposAppState_Type()
)
hh3cposAppState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposAppState.setStatus("current")


class _Hh3cposAppIfIndex_Type(Integer32):
    """Custom type hh3cposAppIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cposAppIfIndex_Type.__name__ = "Integer32"
_Hh3cposAppIfIndex_Object = MibTableColumn
hh3cposAppIfIndex = _Hh3cposAppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 4),
    _Hh3cposAppIfIndex_Type()
)
hh3cposAppIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposAppIfIndex.setStatus("current")
_Hh3cposAppHostIP_Type = IpAddress
_Hh3cposAppHostIP_Object = MibTableColumn
hh3cposAppHostIP = _Hh3cposAppHostIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 5),
    _Hh3cposAppHostIP_Type()
)
hh3cposAppHostIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposAppHostIP.setStatus("current")


class _Hh3cposAppPort_Type(Integer32):
    """Custom type hh3cposAppPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cposAppPort_Type.__name__ = "Integer32"
_Hh3cposAppPort_Object = MibTableColumn
hh3cposAppPort = _Hh3cposAppPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 6),
    _Hh3cposAppPort_Type()
)
hh3cposAppPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposAppPort.setStatus("current")
_Hh3cposAppSourceIp_Type = IpAddress
_Hh3cposAppSourceIp_Object = MibTableColumn
hh3cposAppSourceIp = _Hh3cposAppSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 7),
    _Hh3cposAppSourceIp_Type()
)
hh3cposAppSourceIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposAppSourceIp.setStatus("current")


class _Hh3cposAppRecvPacCounter_Type(Counter32):
    """Custom type hh3cposAppRecvPacCounter based on Counter32"""
    defaultValue = 0


_Hh3cposAppRecvPacCounter_Object = MibTableColumn
hh3cposAppRecvPacCounter = _Hh3cposAppRecvPacCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 8),
    _Hh3cposAppRecvPacCounter_Type()
)
hh3cposAppRecvPacCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposAppRecvPacCounter.setStatus("current")


class _Hh3cposAppErrPacCounter_Type(Counter32):
    """Custom type hh3cposAppErrPacCounter based on Counter32"""
    defaultValue = 0


_Hh3cposAppErrPacCounter_Object = MibTableColumn
hh3cposAppErrPacCounter = _Hh3cposAppErrPacCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 9),
    _Hh3cposAppErrPacCounter_Type()
)
hh3cposAppErrPacCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposAppErrPacCounter.setStatus("current")


class _Hh3cposAppDistrErrCounter_Type(Counter32):
    """Custom type hh3cposAppDistrErrCounter based on Counter32"""
    defaultValue = 0


_Hh3cposAppDistrErrCounter_Object = MibTableColumn
hh3cposAppDistrErrCounter = _Hh3cposAppDistrErrCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 10),
    _Hh3cposAppDistrErrCounter_Type()
)
hh3cposAppDistrErrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposAppDistrErrCounter.setStatus("current")


class _Hh3cposAppBuffedCounter_Type(Counter32):
    """Custom type hh3cposAppBuffedCounter based on Counter32"""
    defaultValue = 0


_Hh3cposAppBuffedCounter_Object = MibTableColumn
hh3cposAppBuffedCounter = _Hh3cposAppBuffedCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 11),
    _Hh3cposAppBuffedCounter_Type()
)
hh3cposAppBuffedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposAppBuffedCounter.setStatus("current")


class _Hh3cposAppDiscardedCounter_Type(Counter32):
    """Custom type hh3cposAppDiscardedCounter based on Counter32"""
    defaultValue = 0


_Hh3cposAppDiscardedCounter_Object = MibTableColumn
hh3cposAppDiscardedCounter = _Hh3cposAppDiscardedCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 12),
    _Hh3cposAppDiscardedCounter_Type()
)
hh3cposAppDiscardedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposAppDiscardedCounter.setStatus("current")


class _Hh3cposAppDebug_Type(Integer32):
    """Custom type hh3cposAppDebug based on Integer32"""
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


_Hh3cposAppDebug_Type.__name__ = "Integer32"
_Hh3cposAppDebug_Object = MibTableColumn
hh3cposAppDebug = _Hh3cposAppDebug_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 13),
    _Hh3cposAppDebug_Type()
)
hh3cposAppDebug.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposAppDebug.setStatus("current")
_Hh3cposAppRowStatus_Type = RowStatus
_Hh3cposAppRowStatus_Object = MibTableColumn
hh3cposAppRowStatus = _Hh3cposAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 14),
    _Hh3cposAppRowStatus_Type()
)
hh3cposAppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposAppRowStatus.setStatus("current")


class _Hh3cposAppX121Addr_Type(OctetString):
    """Custom type hh3cposAppX121Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_Hh3cposAppX121Addr_Type.__name__ = "OctetString"
_Hh3cposAppX121Addr_Object = MibTableColumn
hh3cposAppX121Addr = _Hh3cposAppX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 1, 1, 15),
    _Hh3cposAppX121Addr_Type()
)
hh3cposAppX121Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposAppX121Addr.setStatus("current")
_Hh3cposInterTable_Object = MibTable
hh3cposInterTable = _Hh3cposInterTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2)
)
if mibBuilder.loadTexts:
    hh3cposInterTable.setStatus("current")
_Hh3cposInterEntry_Object = MibTableRow
hh3cposInterEntry = _Hh3cposInterEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1)
)
hh3cposInterEntry.setIndexNames(
    (0, "HH3C-POS-MIB", "hh3cposPosId"),
)
if mibBuilder.loadTexts:
    hh3cposInterEntry.setStatus("current")


class _Hh3cposPosId_Type(Integer32):
    """Custom type hh3cposPosId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cposPosId_Type.__name__ = "Integer32"
_Hh3cposPosId_Object = MibTableColumn
hh3cposPosId = _Hh3cposPosId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 1),
    _Hh3cposPosId_Type()
)
hh3cposPosId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposPosId.setStatus("current")


class _Hh3cposPosIfIndex_Type(Integer32):
    """Custom type hh3cposPosIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cposPosIfIndex_Type.__name__ = "Integer32"
_Hh3cposPosIfIndex_Object = MibTableColumn
hh3cposPosIfIndex = _Hh3cposPosIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 2),
    _Hh3cposPosIfIndex_Type()
)
hh3cposPosIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposPosIfIndex.setStatus("current")


class _Hh3cposPosConnectState_Type(Integer32):
    """Custom type hh3cposPosConnectState based on Integer32"""
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


_Hh3cposPosConnectState_Type.__name__ = "Integer32"
_Hh3cposPosConnectState_Object = MibTableColumn
hh3cposPosConnectState = _Hh3cposPosConnectState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 3),
    _Hh3cposPosConnectState_Type()
)
hh3cposPosConnectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposPosConnectState.setStatus("current")


class _Hh3cposPosRecvPacCounter_Type(Counter32):
    """Custom type hh3cposPosRecvPacCounter based on Counter32"""
    defaultValue = 0


_Hh3cposPosRecvPacCounter_Object = MibTableColumn
hh3cposPosRecvPacCounter = _Hh3cposPosRecvPacCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 4),
    _Hh3cposPosRecvPacCounter_Type()
)
hh3cposPosRecvPacCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposPosRecvPacCounter.setStatus("current")


class _Hh3cposPosErrPacCounter_Type(Counter32):
    """Custom type hh3cposPosErrPacCounter based on Counter32"""
    defaultValue = 0


_Hh3cposPosErrPacCounter_Object = MibTableColumn
hh3cposPosErrPacCounter = _Hh3cposPosErrPacCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 5),
    _Hh3cposPosErrPacCounter_Type()
)
hh3cposPosErrPacCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposPosErrPacCounter.setStatus("current")


class _Hh3cposPosMapErrCounter_Type(Counter32):
    """Custom type hh3cposPosMapErrCounter based on Counter32"""
    defaultValue = 0


_Hh3cposPosMapErrCounter_Object = MibTableColumn
hh3cposPosMapErrCounter = _Hh3cposPosMapErrCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 6),
    _Hh3cposPosMapErrCounter_Type()
)
hh3cposPosMapErrCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposPosMapErrCounter.setStatus("current")


class _Hh3cposPosBuffedCounter_Type(Counter32):
    """Custom type hh3cposPosBuffedCounter based on Counter32"""
    defaultValue = 0


_Hh3cposPosBuffedCounter_Object = MibTableColumn
hh3cposPosBuffedCounter = _Hh3cposPosBuffedCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 7),
    _Hh3cposPosBuffedCounter_Type()
)
hh3cposPosBuffedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposPosBuffedCounter.setStatus("current")


class _Hh3cposPosDiscardedCounter_Type(Counter32):
    """Custom type hh3cposPosDiscardedCounter based on Counter32"""
    defaultValue = 0


_Hh3cposPosDiscardedCounter_Object = MibTableColumn
hh3cposPosDiscardedCounter = _Hh3cposPosDiscardedCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 8),
    _Hh3cposPosDiscardedCounter_Type()
)
hh3cposPosDiscardedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposPosDiscardedCounter.setStatus("current")


class _Hh3cposPosInterDebug_Type(Integer32):
    """Custom type hh3cposPosInterDebug based on Integer32"""
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


_Hh3cposPosInterDebug_Type.__name__ = "Integer32"
_Hh3cposPosInterDebug_Object = MibTableColumn
hh3cposPosInterDebug = _Hh3cposPosInterDebug_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 9),
    _Hh3cposPosInterDebug_Type()
)
hh3cposPosInterDebug.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposPosInterDebug.setStatus("current")
_Hh3cposPosInterRowStatus_Type = RowStatus
_Hh3cposPosInterRowStatus_Object = MibTableColumn
hh3cposPosInterRowStatus = _Hh3cposPosInterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 10),
    _Hh3cposPosInterRowStatus_Type()
)
hh3cposPosInterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposPosInterRowStatus.setStatus("current")


class _Hh3cposPosInterType_Type(Integer32):
    """Custom type hh3cposPosInterType based on Integer32"""
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


_Hh3cposPosInterType_Type.__name__ = "Integer32"
_Hh3cposPosInterType_Object = MibTableColumn
hh3cposPosInterType = _Hh3cposPosInterType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 2, 1, 11),
    _Hh3cposPosInterType_Type()
)
hh3cposPosInterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposPosInterType.setStatus("current")
_Hh3cposMapTable_Object = MibTable
hh3cposMapTable = _Hh3cposMapTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 3)
)
if mibBuilder.loadTexts:
    hh3cposMapTable.setStatus("current")
_Hh3cposMapEntry_Object = MibTableRow
hh3cposMapEntry = _Hh3cposMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 3, 1)
)
hh3cposMapEntry.setIndexNames(
    (0, "HH3C-POS-MIB", "hh3cposMapDes"),
)
if mibBuilder.loadTexts:
    hh3cposMapEntry.setStatus("current")


class _Hh3cposMapDes_Type(Integer32):
    """Custom type hh3cposMapDes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_Hh3cposMapDes_Type.__name__ = "Integer32"
_Hh3cposMapDes_Object = MibTableColumn
hh3cposMapDes = _Hh3cposMapDes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 3, 1, 1),
    _Hh3cposMapDes_Type()
)
hh3cposMapDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposMapDes.setStatus("current")


class _Hh3cposMapAppNumber_Type(Integer32):
    """Custom type hh3cposMapAppNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Hh3cposMapAppNumber_Type.__name__ = "Integer32"
_Hh3cposMapAppNumber_Object = MibTableColumn
hh3cposMapAppNumber = _Hh3cposMapAppNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 3, 1, 2),
    _Hh3cposMapAppNumber_Type()
)
hh3cposMapAppNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposMapAppNumber.setStatus("current")
_Hh3cposMapRowStatus_Type = RowStatus
_Hh3cposMapRowStatus_Object = MibTableColumn
hh3cposMapRowStatus = _Hh3cposMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 3, 1, 3),
    _Hh3cposMapRowStatus_Type()
)
hh3cposMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposMapRowStatus.setStatus("current")
_Hh3cposAsyAppTable_Object = MibTable
hh3cposAsyAppTable = _Hh3cposAsyAppTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 4)
)
if mibBuilder.loadTexts:
    hh3cposAsyAppTable.setStatus("current")
_Hh3cposAsyAppEntry_Object = MibTableRow
hh3cposAsyAppEntry = _Hh3cposAsyAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 4, 1)
)
hh3cposAsyAppEntry.setIndexNames(
    (0, "HH3C-POS-MIB", "hh3cposAsyAppIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cposAsyAppEntry.setStatus("current")


class _Hh3cposAsyAppIfIndex_Type(Integer32):
    """Custom type hh3cposAsyAppIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cposAsyAppIfIndex_Type.__name__ = "Integer32"
_Hh3cposAsyAppIfIndex_Object = MibTableColumn
hh3cposAsyAppIfIndex = _Hh3cposAsyAppIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 4, 1, 1),
    _Hh3cposAsyAppIfIndex_Type()
)
hh3cposAsyAppIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposAsyAppIfIndex.setStatus("current")
_Hh3cposAsyAppRowStatus_Type = RowStatus
_Hh3cposAsyAppRowStatus_Object = MibTableColumn
hh3cposAsyAppRowStatus = _Hh3cposAsyAppRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 4, 1, 2),
    _Hh3cposAsyAppRowStatus_Type()
)
hh3cposAsyAppRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposAsyAppRowStatus.setStatus("current")
_Hh3cposFCMTable_Object = MibTable
hh3cposFCMTable = _Hh3cposFCMTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 5)
)
if mibBuilder.loadTexts:
    hh3cposFCMTable.setStatus("current")
_Hh3cposFCMEntry_Object = MibTableRow
hh3cposFCMEntry = _Hh3cposFCMEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 5, 1)
)
hh3cposFCMEntry.setIndexNames(
    (0, "HH3C-POS-MIB", "hh3cposFCMIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cposFCMEntry.setStatus("current")


class _Hh3cposFCMIfIndex_Type(Integer32):
    """Custom type hh3cposFCMIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cposFCMIfIndex_Type.__name__ = "Integer32"
_Hh3cposFCMIfIndex_Object = MibTableColumn
hh3cposFCMIfIndex = _Hh3cposFCMIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 5, 1, 1),
    _Hh3cposFCMIfIndex_Type()
)
hh3cposFCMIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposFCMIfIndex.setStatus("current")


class _Hh3cposFCMTimeoutCounter_Type(Counter32):
    """Custom type hh3cposFCMTimeoutCounter based on Counter32"""
    defaultValue = 0


_Hh3cposFCMTimeoutCounter_Object = MibTableColumn
hh3cposFCMTimeoutCounter = _Hh3cposFCMTimeoutCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 5, 1, 3),
    _Hh3cposFCMTimeoutCounter_Type()
)
hh3cposFCMTimeoutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposFCMTimeoutCounter.setStatus("current")


class _Hh3cposFCMConnectFailCounter_Type(Counter32):
    """Custom type hh3cposFCMConnectFailCounter based on Counter32"""
    defaultValue = 0


_Hh3cposFCMConnectFailCounter_Object = MibTableColumn
hh3cposFCMConnectFailCounter = _Hh3cposFCMConnectFailCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 5, 1, 4),
    _Hh3cposFCMConnectFailCounter_Type()
)
hh3cposFCMConnectFailCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposFCMConnectFailCounter.setStatus("current")


class _Hh3cposAppSum_Type(Integer32):
    """Custom type hh3cposAppSum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Hh3cposAppSum_Type.__name__ = "Integer32"
_Hh3cposAppSum_Object = MibScalar
hh3cposAppSum = _Hh3cposAppSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 6),
    _Hh3cposAppSum_Type()
)
hh3cposAppSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposAppSum.setStatus("current")


class _Hh3cposInterSum_Type(Integer32):
    """Custom type hh3cposInterSum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_Hh3cposInterSum_Type.__name__ = "Integer32"
_Hh3cposInterSum_Object = MibScalar
hh3cposInterSum = _Hh3cposInterSum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 7),
    _Hh3cposInterSum_Type()
)
hh3cposInterSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cposInterSum.setStatus("current")


class _Hh3cposEnable_Type(Integer32):
    """Custom type hh3cposEnable based on Integer32"""
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


_Hh3cposEnable_Type.__name__ = "Integer32"
_Hh3cposEnable_Object = MibScalar
hh3cposEnable = _Hh3cposEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 8),
    _Hh3cposEnable_Type()
)
hh3cposEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposEnable.setStatus("current")


class _Hh3cposAppDebugAll_Type(Integer32):
    """Custom type hh3cposAppDebugAll based on Integer32"""
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


_Hh3cposAppDebugAll_Type.__name__ = "Integer32"
_Hh3cposAppDebugAll_Object = MibScalar
hh3cposAppDebugAll = _Hh3cposAppDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 9),
    _Hh3cposAppDebugAll_Type()
)
hh3cposAppDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposAppDebugAll.setStatus("current")


class _Hh3cposPosDebugAll_Type(Integer32):
    """Custom type hh3cposPosDebugAll based on Integer32"""
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


_Hh3cposPosDebugAll_Type.__name__ = "Integer32"
_Hh3cposPosDebugAll_Object = MibScalar
hh3cposPosDebugAll = _Hh3cposPosDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 10),
    _Hh3cposPosDebugAll_Type()
)
hh3cposPosDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposPosDebugAll.setStatus("current")


class _Hh3cposClearPacCounter_Type(Integer32):
    """Custom type hh3cposClearPacCounter based on Integer32"""
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


_Hh3cposClearPacCounter_Type.__name__ = "Integer32"
_Hh3cposClearPacCounter_Object = MibScalar
hh3cposClearPacCounter = _Hh3cposClearPacCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 11),
    _Hh3cposClearPacCounter_Type()
)
hh3cposClearPacCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposClearPacCounter.setStatus("current")


class _Hh3cposClearFCMCounter_Type(Integer32):
    """Custom type hh3cposClearFCMCounter based on Integer32"""
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


_Hh3cposClearFCMCounter_Type.__name__ = "Integer32"
_Hh3cposClearFCMCounter_Object = MibScalar
hh3cposClearFCMCounter = _Hh3cposClearFCMCounter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 12),
    _Hh3cposClearFCMCounter_Type()
)
hh3cposClearFCMCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposClearFCMCounter.setStatus("current")


class _Hh3cposEnableTrap_Type(Integer32):
    """Custom type hh3cposEnableTrap based on Integer32"""
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


_Hh3cposEnableTrap_Type.__name__ = "Integer32"
_Hh3cposEnableTrap_Object = MibScalar
hh3cposEnableTrap = _Hh3cposEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 13),
    _Hh3cposEnableTrap_Type()
)
hh3cposEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposEnableTrap.setStatus("current")


class _Hh3cposFCMAnswerTime_Type(Integer32):
    """Custom type hh3cposFCMAnswerTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 2000),
    )


_Hh3cposFCMAnswerTime_Type.__name__ = "Integer32"
_Hh3cposFCMAnswerTime_Object = MibScalar
hh3cposFCMAnswerTime = _Hh3cposFCMAnswerTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 14),
    _Hh3cposFCMAnswerTime_Type()
)
hh3cposFCMAnswerTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposFCMAnswerTime.setStatus("current")


class _Hh3cposFCMTradeTime_Type(Integer32):
    """Custom type hh3cposFCMTradeTime based on Integer32"""
    defaultValue = 60000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30000, 1200000),
    )


_Hh3cposFCMTradeTime_Type.__name__ = "Integer32"
_Hh3cposFCMTradeTime_Object = MibScalar
hh3cposFCMTradeTime = _Hh3cposFCMTradeTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 15),
    _Hh3cposFCMTradeTime_Type()
)
hh3cposFCMTradeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposFCMTradeTime.setStatus("current")


class _Hh3cposFCMPacketInterval_Type(Integer32):
    """Custom type hh3cposFCMPacketInterval based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3500, 10000),
    )


_Hh3cposFCMPacketInterval_Type.__name__ = "Integer32"
_Hh3cposFCMPacketInterval_Object = MibScalar
hh3cposFCMPacketInterval = _Hh3cposFCMPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 16),
    _Hh3cposFCMPacketInterval_Type()
)
hh3cposFCMPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposFCMPacketInterval.setStatus("current")
_Hh3cposTrap_ObjectIdentity = ObjectIdentity
hh3cposTrap = _Hh3cposTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17)
)


class _Hh3cposPadWaitTime_Type(Integer32):
    """Custom type hh3cposPadWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_Hh3cposPadWaitTime_Type.__name__ = "Integer32"
_Hh3cposPadWaitTime_Object = MibScalar
hh3cposPadWaitTime = _Hh3cposPadWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 18),
    _Hh3cposPadWaitTime_Type()
)
hh3cposPadWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposPadWaitTime.setStatus("current")


class _Hh3cposPadIdleTimeout_Type(Integer32):
    """Custom type hh3cposPadIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_Hh3cposPadIdleTimeout_Type.__name__ = "Integer32"
_Hh3cposPadIdleTimeout_Object = MibScalar
hh3cposPadIdleTimeout = _Hh3cposPadIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 19),
    _Hh3cposPadIdleTimeout_Type()
)
hh3cposPadIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposPadIdleTimeout.setStatus("current")


class _Hh3cposPadPacType_Type(Integer32):
    """Custom type hh3cposPadPacType based on Integer32"""
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


_Hh3cposPadPacType_Type.__name__ = "Integer32"
_Hh3cposPadPacType_Object = MibScalar
hh3cposPadPacType = _Hh3cposPadPacType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 20),
    _Hh3cposPadPacType_Type()
)
hh3cposPadPacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposPadPacType.setStatus("current")


class _Hh3cposPadCheckSChar_Type(Integer32):
    """Custom type hh3cposPadCheckSChar based on Integer32"""
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


_Hh3cposPadCheckSChar_Type.__name__ = "Integer32"
_Hh3cposPadCheckSChar_Object = MibScalar
hh3cposPadCheckSChar = _Hh3cposPadCheckSChar_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 21),
    _Hh3cposPadCheckSChar_Type()
)
hh3cposPadCheckSChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cposPadCheckSChar.setStatus("current")
_Hh3cposPadTable_Object = MibTable
hh3cposPadTable = _Hh3cposPadTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 22)
)
if mibBuilder.loadTexts:
    hh3cposPadTable.setStatus("current")
_Hh3cposPadEntry_Object = MibTableRow
hh3cposPadEntry = _Hh3cposPadEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 22, 1)
)
hh3cposPadEntry.setIndexNames(
    (0, "HH3C-POS-MIB", "hh3cposPadIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cposPadEntry.setStatus("current")


class _Hh3cposPadIfIndex_Type(Integer32):
    """Custom type hh3cposPadIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cposPadIfIndex_Type.__name__ = "Integer32"
_Hh3cposPadIfIndex_Object = MibTableColumn
hh3cposPadIfIndex = _Hh3cposPadIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 22, 1, 1),
    _Hh3cposPadIfIndex_Type()
)
hh3cposPadIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cposPadIfIndex.setStatus("current")
_Hh3cposPadRowStatus_Type = RowStatus
_Hh3cposPadRowStatus_Object = MibTableColumn
hh3cposPadRowStatus = _Hh3cposPadRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 22, 1, 2),
    _Hh3cposPadRowStatus_Type()
)
hh3cposPadRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cposPadRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cposAppNotReadyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 1)
)
hh3cposAppNotReadyTrap.setObjects(
    ("HH3C-POS-MIB", "hh3cposAppId")
)
if mibBuilder.loadTexts:
    hh3cposAppNotReadyTrap.setStatus(
        "current"
    )

hh3cposAppConnectFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 2)
)
hh3cposAppConnectFailTrap.setObjects(
    ("HH3C-POS-MIB", "hh3cposAppId")
)
if mibBuilder.loadTexts:
    hh3cposAppConnectFailTrap.setStatus(
        "current"
    )

hh3cposAppStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 3)
)
hh3cposAppStateChangeTrap.setObjects(
      *(("HH3C-POS-MIB", "hh3cposAppId"),
        ("HH3C-POS-MIB", "hh3cposAppState"))
)
if mibBuilder.loadTexts:
    hh3cposAppStateChangeTrap.setStatus(
        "current"
    )

hh3cposAppNotConfigedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 4)
)
hh3cposAppNotConfigedTrap.setObjects(
    ("HH3C-POS-MIB", "hh3cposAppId")
)
if mibBuilder.loadTexts:
    hh3cposAppNotConfigedTrap.setStatus(
        "current"
    )

hh3cposAppBuffOverFlowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 5)
)
hh3cposAppBuffOverFlowTrap.setObjects(
    ("HH3C-POS-MIB", "hh3cposAppId")
)
if mibBuilder.loadTexts:
    hh3cposAppBuffOverFlowTrap.setStatus(
        "current"
    )

hh3cposAppDebugOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 6)
)
hh3cposAppDebugOpenTrap.setObjects(
    ("HH3C-POS-MIB", "hh3cposAppId")
)
if mibBuilder.loadTexts:
    hh3cposAppDebugOpenTrap.setStatus(
        "current"
    )

hh3cposAppDebugAllOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 7)
)
if mibBuilder.loadTexts:
    hh3cposAppDebugAllOpenTrap.setStatus(
        "current"
    )

hh3cposInterBuffOverFlowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 8)
)
if mibBuilder.loadTexts:
    hh3cposInterBuffOverFlowTrap.setStatus(
        "current"
    )

hh3cposInterStateChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 9)
)
hh3cposInterStateChangeTrap.setObjects(
      *(("HH3C-POS-MIB", "hh3cposPosId"),
        ("HH3C-POS-MIB", "hh3cposPosConnectState"))
)
if mibBuilder.loadTexts:
    hh3cposInterStateChangeTrap.setStatus(
        "current"
    )

hh3cposInterDebugOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 10)
)
hh3cposInterDebugOpenTrap.setObjects(
    ("HH3C-POS-MIB", "hh3cposPosId")
)
if mibBuilder.loadTexts:
    hh3cposInterDebugOpenTrap.setStatus(
        "current"
    )

hh3cposInterDebugAllOpenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 11)
)
if mibBuilder.loadTexts:
    hh3cposInterDebugAllOpenTrap.setStatus(
        "current"
    )

hh3cposFCMTimeoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 12)
)
hh3cposFCMTimeoutTrap.setObjects(
    ("HH3C-POS-MIB", "hh3cposFCMIfIndex")
)
if mibBuilder.loadTexts:
    hh3cposFCMTimeoutTrap.setStatus(
        "current"
    )

hh3cposFCMConnectFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 13)
)
hh3cposFCMConnectFailTrap.setObjects(
    ("HH3C-POS-MIB", "hh3cposFCMIfIndex")
)
if mibBuilder.loadTexts:
    hh3cposFCMConnectFailTrap.setStatus(
        "current"
    )

hh3cposClearPacketCounter = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 14)
)
if mibBuilder.loadTexts:
    hh3cposClearPacketCounter.setStatus(
        "current"
    )

hh3cposClearFcmCounter = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 36, 8, 17, 15)
)
if mibBuilder.loadTexts:
    hh3cposClearFcmCounter.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-POS-MIB",
    **{"hh3cpos": hh3cpos,
       "hh3cposAppTable": hh3cposAppTable,
       "hh3cposAppEntry": hh3cposAppEntry,
       "hh3cposAppId": hh3cposAppId,
       "hh3cposAppConnectMode": hh3cposAppConnectMode,
       "hh3cposAppState": hh3cposAppState,
       "hh3cposAppIfIndex": hh3cposAppIfIndex,
       "hh3cposAppHostIP": hh3cposAppHostIP,
       "hh3cposAppPort": hh3cposAppPort,
       "hh3cposAppSourceIp": hh3cposAppSourceIp,
       "hh3cposAppRecvPacCounter": hh3cposAppRecvPacCounter,
       "hh3cposAppErrPacCounter": hh3cposAppErrPacCounter,
       "hh3cposAppDistrErrCounter": hh3cposAppDistrErrCounter,
       "hh3cposAppBuffedCounter": hh3cposAppBuffedCounter,
       "hh3cposAppDiscardedCounter": hh3cposAppDiscardedCounter,
       "hh3cposAppDebug": hh3cposAppDebug,
       "hh3cposAppRowStatus": hh3cposAppRowStatus,
       "hh3cposAppX121Addr": hh3cposAppX121Addr,
       "hh3cposInterTable": hh3cposInterTable,
       "hh3cposInterEntry": hh3cposInterEntry,
       "hh3cposPosId": hh3cposPosId,
       "hh3cposPosIfIndex": hh3cposPosIfIndex,
       "hh3cposPosConnectState": hh3cposPosConnectState,
       "hh3cposPosRecvPacCounter": hh3cposPosRecvPacCounter,
       "hh3cposPosErrPacCounter": hh3cposPosErrPacCounter,
       "hh3cposPosMapErrCounter": hh3cposPosMapErrCounter,
       "hh3cposPosBuffedCounter": hh3cposPosBuffedCounter,
       "hh3cposPosDiscardedCounter": hh3cposPosDiscardedCounter,
       "hh3cposPosInterDebug": hh3cposPosInterDebug,
       "hh3cposPosInterRowStatus": hh3cposPosInterRowStatus,
       "hh3cposPosInterType": hh3cposPosInterType,
       "hh3cposMapTable": hh3cposMapTable,
       "hh3cposMapEntry": hh3cposMapEntry,
       "hh3cposMapDes": hh3cposMapDes,
       "hh3cposMapAppNumber": hh3cposMapAppNumber,
       "hh3cposMapRowStatus": hh3cposMapRowStatus,
       "hh3cposAsyAppTable": hh3cposAsyAppTable,
       "hh3cposAsyAppEntry": hh3cposAsyAppEntry,
       "hh3cposAsyAppIfIndex": hh3cposAsyAppIfIndex,
       "hh3cposAsyAppRowStatus": hh3cposAsyAppRowStatus,
       "hh3cposFCMTable": hh3cposFCMTable,
       "hh3cposFCMEntry": hh3cposFCMEntry,
       "hh3cposFCMIfIndex": hh3cposFCMIfIndex,
       "hh3cposFCMTimeoutCounter": hh3cposFCMTimeoutCounter,
       "hh3cposFCMConnectFailCounter": hh3cposFCMConnectFailCounter,
       "hh3cposAppSum": hh3cposAppSum,
       "hh3cposInterSum": hh3cposInterSum,
       "hh3cposEnable": hh3cposEnable,
       "hh3cposAppDebugAll": hh3cposAppDebugAll,
       "hh3cposPosDebugAll": hh3cposPosDebugAll,
       "hh3cposClearPacCounter": hh3cposClearPacCounter,
       "hh3cposClearFCMCounter": hh3cposClearFCMCounter,
       "hh3cposEnableTrap": hh3cposEnableTrap,
       "hh3cposFCMAnswerTime": hh3cposFCMAnswerTime,
       "hh3cposFCMTradeTime": hh3cposFCMTradeTime,
       "hh3cposFCMPacketInterval": hh3cposFCMPacketInterval,
       "hh3cposTrap": hh3cposTrap,
       "hh3cposAppNotReadyTrap": hh3cposAppNotReadyTrap,
       "hh3cposAppConnectFailTrap": hh3cposAppConnectFailTrap,
       "hh3cposAppStateChangeTrap": hh3cposAppStateChangeTrap,
       "hh3cposAppNotConfigedTrap": hh3cposAppNotConfigedTrap,
       "hh3cposAppBuffOverFlowTrap": hh3cposAppBuffOverFlowTrap,
       "hh3cposAppDebugOpenTrap": hh3cposAppDebugOpenTrap,
       "hh3cposAppDebugAllOpenTrap": hh3cposAppDebugAllOpenTrap,
       "hh3cposInterBuffOverFlowTrap": hh3cposInterBuffOverFlowTrap,
       "hh3cposInterStateChangeTrap": hh3cposInterStateChangeTrap,
       "hh3cposInterDebugOpenTrap": hh3cposInterDebugOpenTrap,
       "hh3cposInterDebugAllOpenTrap": hh3cposInterDebugAllOpenTrap,
       "hh3cposFCMTimeoutTrap": hh3cposFCMTimeoutTrap,
       "hh3cposFCMConnectFailTrap": hh3cposFCMConnectFailTrap,
       "hh3cposClearPacketCounter": hh3cposClearPacketCounter,
       "hh3cposClearFcmCounter": hh3cposClearFcmCounter,
       "hh3cposPadWaitTime": hh3cposPadWaitTime,
       "hh3cposPadIdleTimeout": hh3cposPadIdleTimeout,
       "hh3cposPadPacType": hh3cposPadPacType,
       "hh3cposPadCheckSChar": hh3cposPadCheckSChar,
       "hh3cposPadTable": hh3cposPadTable,
       "hh3cposPadEntry": hh3cposPadEntry,
       "hh3cposPadIfIndex": hh3cposPadIfIndex,
       "hh3cposPadRowStatus": hh3cposPadRowStatus}
)
