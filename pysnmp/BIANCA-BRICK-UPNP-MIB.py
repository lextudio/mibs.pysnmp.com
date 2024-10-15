# SNMP MIB module (BIANCA-BRICK-UPNP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-UPNP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:50 2024
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
_Upnp_ObjectIdentity = ObjectIdentity
upnp = _Upnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45)
)
_UpnpGlobals_ObjectIdentity = ObjectIdentity
upnpGlobals = _UpnpGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 10)
)


class _UpnpGlobStatus_Type(Integer32):
    """Custom type upnpGlobStatus based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 30),
          ("enabled", 10),
          ("restricted", 20))
    )


_UpnpGlobStatus_Type.__name__ = "Integer32"
_UpnpGlobStatus_Object = MibScalar
upnpGlobStatus = _UpnpGlobStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 10, 10),
    _UpnpGlobStatus_Type()
)
upnpGlobStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upnpGlobStatus.setStatus("mandatory")


class _UpnpGlobTcpPort_Type(Integer32):
    """Custom type upnpGlobTcpPort based on Integer32"""
    defaultValue = 5678

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UpnpGlobTcpPort_Type.__name__ = "Integer32"
_UpnpGlobTcpPort_Object = MibScalar
upnpGlobTcpPort = _UpnpGlobTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 10, 20),
    _UpnpGlobTcpPort_Type()
)
upnpGlobTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upnpGlobTcpPort.setStatus("mandatory")


class _UpnpGlobSsdpTtl_Type(Integer32):
    """Custom type upnpGlobSsdpTtl based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UpnpGlobSsdpTtl_Type.__name__ = "Integer32"
_UpnpGlobSsdpTtl_Object = MibScalar
upnpGlobSsdpTtl = _UpnpGlobSsdpTtl_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 10, 30),
    _UpnpGlobSsdpTtl_Type()
)
upnpGlobSsdpTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upnpGlobSsdpTtl.setStatus("mandatory")
_IpNatUPnPTable_Object = MibTable
ipNatUPnPTable = _IpNatUPnPTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 20)
)
if mibBuilder.loadTexts:
    ipNatUPnPTable.setStatus("mandatory")
_IpNatUPnPEntry_Object = MibTableRow
ipNatUPnPEntry = _IpNatUPnPEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 20, 10)
)
ipNatUPnPEntry.setIndexNames(
    (0, "BIANCA-BRICK-UPNP-MIB", "ipNatUPnPIfIndex"),
    (0, "BIANCA-BRICK-UPNP-MIB", "ipNatUPnPProtocol"),
    (0, "BIANCA-BRICK-UPNP-MIB", "ipNatUPnPRemoteAddr"),
    (0, "BIANCA-BRICK-UPNP-MIB", "ipNatUPnPExtPort"),
)
if mibBuilder.loadTexts:
    ipNatUPnPEntry.setStatus("mandatory")
_IpNatUPnPIfIndex_Type = Integer32
_IpNatUPnPIfIndex_Object = MibTableColumn
ipNatUPnPIfIndex = _IpNatUPnPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 20, 10, 10),
    _IpNatUPnPIfIndex_Type()
)
ipNatUPnPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatUPnPIfIndex.setStatus("mandatory")


class _IpNatUPnPProtocol_Type(Integer32):
    """Custom type ipNatUPnPProtocol based on Integer32"""
    defaultValue = 6

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


_IpNatUPnPProtocol_Type.__name__ = "Integer32"
_IpNatUPnPProtocol_Object = MibTableColumn
ipNatUPnPProtocol = _IpNatUPnPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 20, 10, 20),
    _IpNatUPnPProtocol_Type()
)
ipNatUPnPProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatUPnPProtocol.setStatus("mandatory")
_IpNatUPnPRemoteAddr_Type = IpAddress
_IpNatUPnPRemoteAddr_Object = MibTableColumn
ipNatUPnPRemoteAddr = _IpNatUPnPRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 20, 10, 30),
    _IpNatUPnPRemoteAddr_Type()
)
ipNatUPnPRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatUPnPRemoteAddr.setStatus("mandatory")


class _IpNatUPnPExtPort_Type(Integer32):
    """Custom type ipNatUPnPExtPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpNatUPnPExtPort_Type.__name__ = "Integer32"
_IpNatUPnPExtPort_Object = MibTableColumn
ipNatUPnPExtPort = _IpNatUPnPExtPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 20, 10, 40),
    _IpNatUPnPExtPort_Type()
)
ipNatUPnPExtPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatUPnPExtPort.setStatus("mandatory")
_IpNatUPnPIntAddr_Type = IpAddress
_IpNatUPnPIntAddr_Object = MibTableColumn
ipNatUPnPIntAddr = _IpNatUPnPIntAddr_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 20, 10, 50),
    _IpNatUPnPIntAddr_Type()
)
ipNatUPnPIntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatUPnPIntAddr.setStatus("mandatory")


class _IpNatUPnPIntPort_Type(Integer32):
    """Custom type ipNatUPnPIntPort based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpNatUPnPIntPort_Type.__name__ = "Integer32"
_IpNatUPnPIntPort_Object = MibTableColumn
ipNatUPnPIntPort = _IpNatUPnPIntPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 20, 10, 60),
    _IpNatUPnPIntPort_Type()
)
ipNatUPnPIntPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatUPnPIntPort.setStatus("mandatory")


class _IpNatUPnPLeaseDuration_Type(Integer32):
    """Custom type ipNatUPnPLeaseDuration based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5184000),
    )


_IpNatUPnPLeaseDuration_Type.__name__ = "Integer32"
_IpNatUPnPLeaseDuration_Object = MibTableColumn
ipNatUPnPLeaseDuration = _IpNatUPnPLeaseDuration_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 20, 10, 70),
    _IpNatUPnPLeaseDuration_Type()
)
ipNatUPnPLeaseDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatUPnPLeaseDuration.setStatus("mandatory")


class _IpNatUPnPStatus_Type(Integer32):
    """Custom type ipNatUPnPStatus based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20,
              30)
        )
    )
    namedValues = NamedValues(
        *(("delete", 10),
          ("disabled", 30),
          ("enabled", 20))
    )


_IpNatUPnPStatus_Type.__name__ = "Integer32"
_IpNatUPnPStatus_Object = MibTableColumn
ipNatUPnPStatus = _IpNatUPnPStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 20, 10, 80),
    _IpNatUPnPStatus_Type()
)
ipNatUPnPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNatUPnPStatus.setStatus("mandatory")


class _IpNatUPnPDescription_Type(DisplayString):
    """Custom type ipNatUPnPDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpNatUPnPDescription_Type.__name__ = "DisplayString"
_IpNatUPnPDescription_Object = MibTableColumn
ipNatUPnPDescription = _IpNatUPnPDescription_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 20, 10, 90),
    _IpNatUPnPDescription_Type()
)
ipNatUPnPDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNatUPnPDescription.setStatus("mandatory")
_UpnpIfTable_Object = MibTable
upnpIfTable = _UpnpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 30)
)
if mibBuilder.loadTexts:
    upnpIfTable.setStatus("mandatory")
_UpnpIfEntry_Object = MibTableRow
upnpIfEntry = _UpnpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 30, 10)
)
upnpIfEntry.setIndexNames(
    (0, "BIANCA-BRICK-UPNP-MIB", "upnpIfIndex"),
)
if mibBuilder.loadTexts:
    upnpIfEntry.setStatus("mandatory")
_UpnpIfIndex_Type = Integer32
_UpnpIfIndex_Object = MibTableColumn
upnpIfIndex = _UpnpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 30, 10, 10),
    _UpnpIfIndex_Type()
)
upnpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upnpIfIndex.setStatus("mandatory")


class _UpnpIfClientRequests_Type(Integer32):
    """Custom type upnpIfClientRequests based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 20),
          ("enabled", 10))
    )


_UpnpIfClientRequests_Type.__name__ = "Integer32"
_UpnpIfClientRequests_Object = MibTableColumn
upnpIfClientRequests = _UpnpIfClientRequests_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 30, 10, 20),
    _UpnpIfClientRequests_Type()
)
upnpIfClientRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upnpIfClientRequests.setStatus("mandatory")


class _UpnpIfUPnPControlled_Type(Integer32):
    """Custom type upnpIfUPnPControlled based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10,
              20)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 20),
          ("enabled", 10))
    )


_UpnpIfUPnPControlled_Type.__name__ = "Integer32"
_UpnpIfUPnPControlled_Object = MibTableColumn
upnpIfUPnPControlled = _UpnpIfUPnPControlled_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 45, 30, 10, 30),
    _UpnpIfUPnPControlled_Type()
)
upnpIfUPnPControlled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upnpIfUPnPControlled.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-UPNP-MIB",
    **{"bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "upnp": upnp,
       "upnpGlobals": upnpGlobals,
       "upnpGlobStatus": upnpGlobStatus,
       "upnpGlobTcpPort": upnpGlobTcpPort,
       "upnpGlobSsdpTtl": upnpGlobSsdpTtl,
       "ipNatUPnPTable": ipNatUPnPTable,
       "ipNatUPnPEntry": ipNatUPnPEntry,
       "ipNatUPnPIfIndex": ipNatUPnPIfIndex,
       "ipNatUPnPProtocol": ipNatUPnPProtocol,
       "ipNatUPnPRemoteAddr": ipNatUPnPRemoteAddr,
       "ipNatUPnPExtPort": ipNatUPnPExtPort,
       "ipNatUPnPIntAddr": ipNatUPnPIntAddr,
       "ipNatUPnPIntPort": ipNatUPnPIntPort,
       "ipNatUPnPLeaseDuration": ipNatUPnPLeaseDuration,
       "ipNatUPnPStatus": ipNatUPnPStatus,
       "ipNatUPnPDescription": ipNatUPnPDescription,
       "upnpIfTable": upnpIfTable,
       "upnpIfEntry": upnpIfEntry,
       "upnpIfIndex": upnpIfIndex,
       "upnpIfClientRequests": upnpIfClientRequests,
       "upnpIfUPnPControlled": upnpIfUPnPControlled}
)
