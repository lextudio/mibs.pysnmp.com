# SNMP MIB module (BIANCA-BRICK-PROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-PROXY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:43 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Bintec_ObjectIdentity = ObjectIdentity
bintec = _Bintec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272)
)
_Bibo_ObjectIdentity = ObjectIdentity
bibo = _Bibo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4)
)
_Biboip_ObjectIdentity = ObjectIdentity
biboip = _Biboip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5)
)
_IpProxyTable_Object = MibTable
ipProxyTable = _IpProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 50)
)
if mibBuilder.loadTexts:
    ipProxyTable.setStatus("mandatory")
_IpProxyEntry_Object = MibTableRow
ipProxyEntry = _IpProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1)
)
ipProxyEntry.setIndexNames(
    (0, "BIANCA-BRICK-PROXY-MIB", "ipProxyDescr"),
)
if mibBuilder.loadTexts:
    ipProxyEntry.setStatus("mandatory")


class _IpProxyDescr_Type(DisplayString):
    """Custom type ipProxyDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_IpProxyDescr_Type.__name__ = "DisplayString"
_IpProxyDescr_Object = MibTableColumn
ipProxyDescr = _IpProxyDescr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 1),
    _IpProxyDescr_Type()
)
ipProxyDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipProxyDescr.setStatus("mandatory")


class _IpProxyAdminStatus_Type(Integer32):
    """Custom type ipProxyAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("disable", 2),
          ("enable", 1))
    )


_IpProxyAdminStatus_Type.__name__ = "Integer32"
_IpProxyAdminStatus_Object = MibTableColumn
ipProxyAdminStatus = _IpProxyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 2),
    _IpProxyAdminStatus_Type()
)
ipProxyAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipProxyAdminStatus.setStatus("mandatory")


class _IpProxyApplication_Type(Integer32):
    """Custom type ipProxyApplication based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              15)
        )
    )
    namedValues = NamedValues(
        *(("h323tcp", 8),
          ("h323udp", 4),
          ("mgcp", 2),
          ("none", 15),
          ("rtsp", 3),
          ("sip", 1))
    )


_IpProxyApplication_Type.__name__ = "Integer32"
_IpProxyApplication_Object = MibTableColumn
ipProxyApplication = _IpProxyApplication_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 3),
    _IpProxyApplication_Type()
)
ipProxyApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipProxyApplication.setStatus("mandatory")


class _IpProxyProtocol_Type(Integer32):
    """Custom type ipProxyProtocol based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_IpProxyProtocol_Type.__name__ = "Integer32"
_IpProxyProtocol_Object = MibTableColumn
ipProxyProtocol = _IpProxyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 4),
    _IpProxyProtocol_Type()
)
ipProxyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipProxyProtocol.setStatus("mandatory")


class _IpProxyIntPort_Type(Integer32):
    """Custom type ipProxyIntPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpProxyIntPort_Type.__name__ = "Integer32"
_IpProxyIntPort_Object = MibTableColumn
ipProxyIntPort = _IpProxyIntPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 5),
    _IpProxyIntPort_Type()
)
ipProxyIntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipProxyIntPort.setStatus("mandatory")


class _IpProxyExtPort_Type(Integer32):
    """Custom type ipProxyExtPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpProxyExtPort_Type.__name__ = "Integer32"
_IpProxyExtPort_Object = MibTableColumn
ipProxyExtPort = _IpProxyExtPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 6),
    _IpProxyExtPort_Type()
)
ipProxyExtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipProxyExtPort.setStatus("mandatory")
_IpProxyIntAddr_Type = IpAddress
_IpProxyIntAddr_Object = MibTableColumn
ipProxyIntAddr = _IpProxyIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 7),
    _IpProxyIntAddr_Type()
)
ipProxyIntAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipProxyIntAddr.setStatus("mandatory")


class _IpProxyPriority_Type(Integer32):
    """Custom type ipProxyPriority based on Integer32"""
    defaultValue = 1

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
        *(("default", 1),
          ("high", 3),
          ("low", 5),
          ("low-latency", 2),
          ("medium", 4))
    )


_IpProxyPriority_Type.__name__ = "Integer32"
_IpProxyPriority_Object = MibTableColumn
ipProxyPriority = _IpProxyPriority_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 8),
    _IpProxyPriority_Type()
)
ipProxyPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipProxyPriority.setStatus("mandatory")


class _IpProxyTimeout_Type(Integer32):
    """Custom type ipProxyTimeout based on Integer32"""
    defaultValue = 7200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_IpProxyTimeout_Type.__name__ = "Integer32"
_IpProxyTimeout_Object = MibTableColumn
ipProxyTimeout = _IpProxyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 50, 1, 9),
    _IpProxyTimeout_Type()
)
ipProxyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipProxyTimeout.setStatus("mandatory")
_Media_ObjectIdentity = ObjectIdentity
media = _Media_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 50)
)
_MediaConnTable_Object = MibTable
mediaConnTable = _MediaConnTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 1)
)
if mibBuilder.loadTexts:
    mediaConnTable.setStatus("mandatory")
_MediaConnEntry_Object = MibTableRow
mediaConnEntry = _MediaConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1)
)
mediaConnEntry.setIndexNames(
    (0, "BIANCA-BRICK-PROXY-MIB", "mediaConnIndex"),
)
if mibBuilder.loadTexts:
    mediaConnEntry.setStatus("mandatory")


class _MediaConnIndex_Type(Integer32):
    """Custom type mediaConnIndex based on Integer32"""
    defaultValue = 1


_MediaConnIndex_Object = MibTableColumn
mediaConnIndex = _MediaConnIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 1),
    _MediaConnIndex_Type()
)
mediaConnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaConnIndex.setStatus("mandatory")
_MediaConnIntAddr_Type = IpAddress
_MediaConnIntAddr_Object = MibTableColumn
mediaConnIntAddr = _MediaConnIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 2),
    _MediaConnIntAddr_Type()
)
mediaConnIntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaConnIntAddr.setStatus("mandatory")
_MediaConnIntPort_Type = Integer32
_MediaConnIntPort_Object = MibTableColumn
mediaConnIntPort = _MediaConnIntPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 3),
    _MediaConnIntPort_Type()
)
mediaConnIntPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaConnIntPort.setStatus("mandatory")
_MediaConnExtAddr_Type = IpAddress
_MediaConnExtAddr_Object = MibTableColumn
mediaConnExtAddr = _MediaConnExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 4),
    _MediaConnExtAddr_Type()
)
mediaConnExtAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaConnExtAddr.setStatus("mandatory")
_MediaConnExtPort_Type = Integer32
_MediaConnExtPort_Object = MibTableColumn
mediaConnExtPort = _MediaConnExtPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 5),
    _MediaConnExtPort_Type()
)
mediaConnExtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaConnExtPort.setStatus("mandatory")
_MediaConnRemoteAddr_Type = IpAddress
_MediaConnRemoteAddr_Object = MibTableColumn
mediaConnRemoteAddr = _MediaConnRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 6),
    _MediaConnRemoteAddr_Type()
)
mediaConnRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaConnRemoteAddr.setStatus("mandatory")
_MediaConnRemotePort_Type = Integer32
_MediaConnRemotePort_Object = MibTableColumn
mediaConnRemotePort = _MediaConnRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 7),
    _MediaConnRemotePort_Type()
)
mediaConnRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaConnRemotePort.setStatus("mandatory")
_MediaConnAge_Type = TimeTicks
_MediaConnAge_Object = MibTableColumn
mediaConnAge = _MediaConnAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 1, 1, 8),
    _MediaConnAge_Type()
)
mediaConnAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaConnAge.setStatus("mandatory")
_MediaTerminalTable_Object = MibTable
mediaTerminalTable = _MediaTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 2)
)
if mibBuilder.loadTexts:
    mediaTerminalTable.setStatus("mandatory")
_MediaTerminalEntry_Object = MibTableRow
mediaTerminalEntry = _MediaTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1)
)
mediaTerminalEntry.setIndexNames(
    (0, "BIANCA-BRICK-PROXY-MIB", "mediaTerminalIntAddr"),
    (0, "BIANCA-BRICK-PROXY-MIB", "mediaTerminalIntPort"),
)
if mibBuilder.loadTexts:
    mediaTerminalEntry.setStatus("mandatory")
_MediaTerminalIntAddr_Type = IpAddress
_MediaTerminalIntAddr_Object = MibTableColumn
mediaTerminalIntAddr = _MediaTerminalIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 1),
    _MediaTerminalIntAddr_Type()
)
mediaTerminalIntAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaTerminalIntAddr.setStatus("mandatory")


class _MediaTerminalIntPort_Type(Integer32):
    """Custom type mediaTerminalIntPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MediaTerminalIntPort_Type.__name__ = "Integer32"
_MediaTerminalIntPort_Object = MibTableColumn
mediaTerminalIntPort = _MediaTerminalIntPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 2),
    _MediaTerminalIntPort_Type()
)
mediaTerminalIntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaTerminalIntPort.setStatus("mandatory")


class _MediaTerminalExtPort_Type(Integer32):
    """Custom type mediaTerminalExtPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MediaTerminalExtPort_Type.__name__ = "Integer32"
_MediaTerminalExtPort_Object = MibTableColumn
mediaTerminalExtPort = _MediaTerminalExtPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 3),
    _MediaTerminalExtPort_Type()
)
mediaTerminalExtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaTerminalExtPort.setStatus("mandatory")


class _MediaTerminalRemotePort_Type(Integer32):
    """Custom type mediaTerminalRemotePort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MediaTerminalRemotePort_Type.__name__ = "Integer32"
_MediaTerminalRemotePort_Object = MibTableColumn
mediaTerminalRemotePort = _MediaTerminalRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 4),
    _MediaTerminalRemotePort_Type()
)
mediaTerminalRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaTerminalRemotePort.setStatus("mandatory")


class _MediaTerminalLifetime_Type(Integer32):
    """Custom type mediaTerminalLifetime based on Integer32"""
    defaultValue = 0


_MediaTerminalLifetime_Object = MibTableColumn
mediaTerminalLifetime = _MediaTerminalLifetime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 5),
    _MediaTerminalLifetime_Type()
)
mediaTerminalLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaTerminalLifetime.setStatus("mandatory")


class _MediaTerminalAge_Type(Integer32):
    """Custom type mediaTerminalAge based on Integer32"""
    defaultValue = 0


_MediaTerminalAge_Object = MibTableColumn
mediaTerminalAge = _MediaTerminalAge_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 6),
    _MediaTerminalAge_Type()
)
mediaTerminalAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaTerminalAge.setStatus("mandatory")


class _MediaTerminalProto_Type(Integer32):
    """Custom type mediaTerminalProto based on Integer32"""
    defaultValue = 17

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              17)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 6),
          ("udp", 17))
    )


_MediaTerminalProto_Type.__name__ = "Integer32"
_MediaTerminalProto_Object = MibTableColumn
mediaTerminalProto = _MediaTerminalProto_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 7),
    _MediaTerminalProto_Type()
)
mediaTerminalProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaTerminalProto.setStatus("mandatory")


class _MediaTerminalType_Type(Integer32):
    """Custom type mediaTerminalType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              8)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("delete", 8),
          ("server", 2))
    )


_MediaTerminalType_Type.__name__ = "Integer32"
_MediaTerminalType_Object = MibTableColumn
mediaTerminalType = _MediaTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 8),
    _MediaTerminalType_Type()
)
mediaTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mediaTerminalType.setStatus("mandatory")


class _MediaTerminalSessions_Type(Integer32):
    """Custom type mediaTerminalSessions based on Integer32"""
    defaultValue = 0


_MediaTerminalSessions_Object = MibTableColumn
mediaTerminalSessions = _MediaTerminalSessions_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 50, 2, 1, 10),
    _MediaTerminalSessions_Type()
)
mediaTerminalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mediaTerminalSessions.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-PROXY-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "ipProxyTable": ipProxyTable,
       "ipProxyEntry": ipProxyEntry,
       "ipProxyDescr": ipProxyDescr,
       "ipProxyAdminStatus": ipProxyAdminStatus,
       "ipProxyApplication": ipProxyApplication,
       "ipProxyProtocol": ipProxyProtocol,
       "ipProxyIntPort": ipProxyIntPort,
       "ipProxyExtPort": ipProxyExtPort,
       "ipProxyIntAddr": ipProxyIntAddr,
       "ipProxyPriority": ipProxyPriority,
       "ipProxyTimeout": ipProxyTimeout,
       "media": media,
       "mediaConnTable": mediaConnTable,
       "mediaConnEntry": mediaConnEntry,
       "mediaConnIndex": mediaConnIndex,
       "mediaConnIntAddr": mediaConnIntAddr,
       "mediaConnIntPort": mediaConnIntPort,
       "mediaConnExtAddr": mediaConnExtAddr,
       "mediaConnExtPort": mediaConnExtPort,
       "mediaConnRemoteAddr": mediaConnRemoteAddr,
       "mediaConnRemotePort": mediaConnRemotePort,
       "mediaConnAge": mediaConnAge,
       "mediaTerminalTable": mediaTerminalTable,
       "mediaTerminalEntry": mediaTerminalEntry,
       "mediaTerminalIntAddr": mediaTerminalIntAddr,
       "mediaTerminalIntPort": mediaTerminalIntPort,
       "mediaTerminalExtPort": mediaTerminalExtPort,
       "mediaTerminalRemotePort": mediaTerminalRemotePort,
       "mediaTerminalLifetime": mediaTerminalLifetime,
       "mediaTerminalAge": mediaTerminalAge,
       "mediaTerminalProto": mediaTerminalProto,
       "mediaTerminalType": mediaTerminalType,
       "mediaTerminalSessions": mediaTerminalSessions}
)
