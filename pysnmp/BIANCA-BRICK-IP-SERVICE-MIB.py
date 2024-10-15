# SNMP MIB module (BIANCA-BRICK-IP-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-IP-SERVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:30 2024
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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
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
_Biboipsrv_ObjectIdentity = ObjectIdentity
biboipsrv = _Biboipsrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14)
)
_LocalTcpAllowTable_Object = MibTable
localTcpAllowTable = _LocalTcpAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1)
)
if mibBuilder.loadTexts:
    localTcpAllowTable.setStatus("mandatory")
_LocalTcpAllowEntry_Object = MibTableRow
localTcpAllowEntry = _LocalTcpAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1)
)
localTcpAllowEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "localTcpAllowAddr"),
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "Service"),
)
if mibBuilder.loadTexts:
    localTcpAllowEntry.setStatus("mandatory")


class _LocalTcpAllowAddrMode_Type(Integer32):
    """Custom type localTcpAllowAddrMode based on Integer32"""
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
          ("dont-verify", 1),
          ("verify", 2))
    )


_LocalTcpAllowAddrMode_Type.__name__ = "Integer32"
_LocalTcpAllowAddrMode_Object = MibTableColumn
localTcpAllowAddrMode = _LocalTcpAllowAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 1),
    _LocalTcpAllowAddrMode_Type()
)
localTcpAllowAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowAddrMode.setStatus("mandatory")
_LocalTcpAllowAddr_Type = IpAddress
_LocalTcpAllowAddr_Object = MibTableColumn
localTcpAllowAddr = _LocalTcpAllowAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 2),
    _LocalTcpAllowAddr_Type()
)
localTcpAllowAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowAddr.setStatus("mandatory")
_LocalTcpAllowMask_Type = IpAddress
_LocalTcpAllowMask_Object = MibTableColumn
localTcpAllowMask = _LocalTcpAllowMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 3),
    _LocalTcpAllowMask_Type()
)
localTcpAllowMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowMask.setStatus("mandatory")


class _LocalTcpAllowIfMode_Type(Integer32):
    """Custom type localTcpAllowIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_LocalTcpAllowIfMode_Type.__name__ = "Integer32"
_LocalTcpAllowIfMode_Object = MibTableColumn
localTcpAllowIfMode = _LocalTcpAllowIfMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 4),
    _LocalTcpAllowIfMode_Type()
)
localTcpAllowIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowIfMode.setStatus("mandatory")
_LocalTcpAllowIfIndex_Type = Integer32
_LocalTcpAllowIfIndex_Object = MibTableColumn
localTcpAllowIfIndex = _LocalTcpAllowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 5),
    _LocalTcpAllowIfIndex_Type()
)
localTcpAllowIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowIfIndex.setStatus("mandatory")


class _LocalTcpAllowService_Type(Integer32):
    """Custom type localTcpAllowService based on Integer32"""
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
        *(("capi", 4),
          ("http", 7),
          ("rfc1086", 6),
          ("snmp", 3),
          ("tapi", 5),
          ("telnet", 1),
          ("trace", 2))
    )


_LocalTcpAllowService_Type.__name__ = "Integer32"
_LocalTcpAllowService_Object = MibTableColumn
localTcpAllowService = _LocalTcpAllowService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 1, 1, 6),
    _LocalTcpAllowService_Type()
)
localTcpAllowService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localTcpAllowService.setStatus("mandatory")
_LocalUdpAllowTable_Object = MibTable
localUdpAllowTable = _LocalUdpAllowTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2)
)
if mibBuilder.loadTexts:
    localUdpAllowTable.setStatus("mandatory")
_LocalUdpAllowEntry_Object = MibTableRow
localUdpAllowEntry = _LocalUdpAllowEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1)
)
localUdpAllowEntry.setIndexNames(
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "localUdpAllowAddr"),
    (0, "BIANCA-BRICK-IP-SERVICE-MIB", "Service"),
)
if mibBuilder.loadTexts:
    localUdpAllowEntry.setStatus("mandatory")


class _LocalUdpAllowAddrMode_Type(Integer32):
    """Custom type localUdpAllowAddrMode based on Integer32"""
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
          ("dont-verify", 1),
          ("verify", 2))
    )


_LocalUdpAllowAddrMode_Type.__name__ = "Integer32"
_LocalUdpAllowAddrMode_Object = MibTableColumn
localUdpAllowAddrMode = _LocalUdpAllowAddrMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 1),
    _LocalUdpAllowAddrMode_Type()
)
localUdpAllowAddrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowAddrMode.setStatus("mandatory")
_LocalUdpAllowAddr_Type = IpAddress
_LocalUdpAllowAddr_Object = MibTableColumn
localUdpAllowAddr = _LocalUdpAllowAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 2),
    _LocalUdpAllowAddr_Type()
)
localUdpAllowAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowAddr.setStatus("mandatory")
_LocalUdpAllowMask_Type = IpAddress
_LocalUdpAllowMask_Object = MibTableColumn
localUdpAllowMask = _LocalUdpAllowMask_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 3),
    _LocalUdpAllowMask_Type()
)
localUdpAllowMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowMask.setStatus("mandatory")


class _LocalUdpAllowIfMode_Type(Integer32):
    """Custom type localUdpAllowIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dont-verify", 1),
          ("verify", 2))
    )


_LocalUdpAllowIfMode_Type.__name__ = "Integer32"
_LocalUdpAllowIfMode_Object = MibTableColumn
localUdpAllowIfMode = _LocalUdpAllowIfMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 4),
    _LocalUdpAllowIfMode_Type()
)
localUdpAllowIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowIfMode.setStatus("mandatory")
_LocalUdpAllowIfIndex_Type = Integer32
_LocalUdpAllowIfIndex_Object = MibTableColumn
localUdpAllowIfIndex = _LocalUdpAllowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 5),
    _LocalUdpAllowIfIndex_Type()
)
localUdpAllowIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowIfIndex.setStatus("mandatory")


class _LocalUdpAllowService_Type(Integer32):
    """Custom type localUdpAllowService based on Integer32"""
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
        *(("bootps", 3),
          ("dns", 4),
          ("nbns", 5),
          ("rip", 2),
          ("snmp", 1),
          ("statmon", 6))
    )


_LocalUdpAllowService_Type.__name__ = "Integer32"
_LocalUdpAllowService_Object = MibTableColumn
localUdpAllowService = _LocalUdpAllowService_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 14, 2, 1, 6),
    _LocalUdpAllowService_Type()
)
localUdpAllowService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUdpAllowService.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-IP-SERVICE-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "biboipsrv": biboipsrv,
       "localTcpAllowTable": localTcpAllowTable,
       "localTcpAllowEntry": localTcpAllowEntry,
       "localTcpAllowAddrMode": localTcpAllowAddrMode,
       "localTcpAllowAddr": localTcpAllowAddr,
       "localTcpAllowMask": localTcpAllowMask,
       "localTcpAllowIfMode": localTcpAllowIfMode,
       "localTcpAllowIfIndex": localTcpAllowIfIndex,
       "localTcpAllowService": localTcpAllowService,
       "localUdpAllowTable": localUdpAllowTable,
       "localUdpAllowEntry": localUdpAllowEntry,
       "localUdpAllowAddrMode": localUdpAllowAddrMode,
       "localUdpAllowAddr": localUdpAllowAddr,
       "localUdpAllowMask": localUdpAllowMask,
       "localUdpAllowIfMode": localUdpAllowIfMode,
       "localUdpAllowIfIndex": localUdpAllowIfIndex,
       "localUdpAllowService": localUdpAllowService}
)
