# SNMP MIB module (BIANCA-BRICK-TACACSP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-TACACSP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:47 2024
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
_Bintecsec_ObjectIdentity = ObjectIdentity
bintecsec = _Bintecsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 254)
)
_Tacacsp_ObjectIdentity = ObjectIdentity
tacacsp = _Tacacsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 254, 13)
)
_TacacspServerTable_Object = MibTable
tacacspServerTable = _TacacspServerTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1)
)
if mibBuilder.loadTexts:
    tacacspServerTable.setStatus("mandatory")
_TacacspServerEntry_Object = MibTableRow
tacacspServerEntry = _TacacspServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1)
)
tacacspServerEntry.setIndexNames(
    (0, "BIANCA-BRICK-TACACSP-MIB", "tacacspSrvPriority"),
)
if mibBuilder.loadTexts:
    tacacspServerEntry.setStatus("mandatory")


class _TacacspSrvPriority_Type(Integer32):
    """Custom type tacacspSrvPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_TacacspSrvPriority_Type.__name__ = "Integer32"
_TacacspSrvPriority_Object = MibTableColumn
tacacspSrvPriority = _TacacspSrvPriority_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 1),
    _TacacspSrvPriority_Type()
)
tacacspSrvPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvPriority.setStatus("mandatory")
_TacacspSrvAddress_Type = IpAddress
_TacacspSrvAddress_Object = MibTableColumn
tacacspSrvAddress = _TacacspSrvAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 2),
    _TacacspSrvAddress_Type()
)
tacacspSrvAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvAddress.setStatus("mandatory")


class _TacacspSrvTcpPort_Type(Integer32):
    """Custom type tacacspSrvTcpPort based on Integer32"""
    defaultValue = 49


_TacacspSrvTcpPort_Object = MibTableColumn
tacacspSrvTcpPort = _TacacspSrvTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 3),
    _TacacspSrvTcpPort_Type()
)
tacacspSrvTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacacspSrvTcpPort.setStatus("mandatory")
_TacacspSrvSecret_Type = DisplayString
_TacacspSrvSecret_Object = MibTableColumn
tacacspSrvSecret = _TacacspSrvSecret_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 4),
    _TacacspSrvSecret_Type()
)
tacacspSrvSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvSecret.setStatus("mandatory")


class _TacacspSrvTimeout_Type(Integer32):
    """Custom type tacacspSrvTimeout based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_TacacspSrvTimeout_Type.__name__ = "Integer32"
_TacacspSrvTimeout_Object = MibTableColumn
tacacspSrvTimeout = _TacacspSrvTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 5),
    _TacacspSrvTimeout_Type()
)
tacacspSrvTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvTimeout.setStatus("mandatory")


class _TacacspSrvAdminStatus_Type(Integer32):
    """Custom type tacacspSrvAdminStatus based on Integer32"""
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
          ("down", 2),
          ("up", 1))
    )


_TacacspSrvAdminStatus_Type.__name__ = "Integer32"
_TacacspSrvAdminStatus_Object = MibTableColumn
tacacspSrvAdminStatus = _TacacspSrvAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 7),
    _TacacspSrvAdminStatus_Type()
)
tacacspSrvAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvAdminStatus.setStatus("mandatory")


class _TacacspSrvOperStatus_Type(Integer32):
    """Custom type tacacspSrvOperStatus based on Integer32"""
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
        *(("blocked", 2),
          ("down", 3),
          ("up", 1))
    )


_TacacspSrvOperStatus_Type.__name__ = "Integer32"
_TacacspSrvOperStatus_Object = MibTableColumn
tacacspSrvOperStatus = _TacacspSrvOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 8),
    _TacacspSrvOperStatus_Type()
)
tacacspSrvOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacacspSrvOperStatus.setStatus("mandatory")


class _TacacspSrvPolicy_Type(Integer32):
    """Custom type tacacspSrvPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authoritative", 1),
          ("non-authoritative", 2))
    )


_TacacspSrvPolicy_Type.__name__ = "Integer32"
_TacacspSrvPolicy_Object = MibTableColumn
tacacspSrvPolicy = _TacacspSrvPolicy_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 9),
    _TacacspSrvPolicy_Type()
)
tacacspSrvPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvPolicy.setStatus("mandatory")


class _TacacspSrvEncrMode_Type(Integer32):
    """Custom type tacacspSrvEncrMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleartext", 2),
          ("encrypt", 1))
    )


_TacacspSrvEncrMode_Type.__name__ = "Integer32"
_TacacspSrvEncrMode_Object = MibTableColumn
tacacspSrvEncrMode = _TacacspSrvEncrMode_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 10),
    _TacacspSrvEncrMode_Type()
)
tacacspSrvEncrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvEncrMode.setStatus("mandatory")


class _TacacspSrvMultiSession_Type(Integer32):
    """Custom type tacacspSrvMultiSession based on Integer32"""
    defaultValue = 2

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


_TacacspSrvMultiSession_Type.__name__ = "Integer32"
_TacacspSrvMultiSession_Object = MibTableColumn
tacacspSrvMultiSession = _TacacspSrvMultiSession_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 11),
    _TacacspSrvMultiSession_Type()
)
tacacspSrvMultiSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvMultiSession.setStatus("mandatory")


class _TacacspSrvPppAuth_Type(Integer32):
    """Custom type tacacspSrvPppAuth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TacacspSrvPppAuth_Type.__name__ = "Integer32"
_TacacspSrvPppAuth_Object = MibTableColumn
tacacspSrvPppAuth = _TacacspSrvPppAuth_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 13),
    _TacacspSrvPppAuth_Type()
)
tacacspSrvPppAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvPppAuth.setStatus("mandatory")


class _TacacspSrvLoginAuth_Type(Integer32):
    """Custom type tacacspSrvLoginAuth based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TacacspSrvLoginAuth_Type.__name__ = "Integer32"
_TacacspSrvLoginAuth_Object = MibTableColumn
tacacspSrvLoginAuth = _TacacspSrvLoginAuth_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 14),
    _TacacspSrvLoginAuth_Type()
)
tacacspSrvLoginAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvLoginAuth.setStatus("mandatory")


class _TacacspSrvAccounting_Type(Integer32):
    """Custom type tacacspSrvAccounting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_TacacspSrvAccounting_Type.__name__ = "Integer32"
_TacacspSrvAccounting_Object = MibTableColumn
tacacspSrvAccounting = _TacacspSrvAccounting_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 15),
    _TacacspSrvAccounting_Type()
)
tacacspSrvAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvAccounting.setStatus("mandatory")


class _TacacspSrvBlockTimeout_Type(Integer32):
    """Custom type tacacspSrvBlockTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_TacacspSrvBlockTimeout_Type.__name__ = "Integer32"
_TacacspSrvBlockTimeout_Object = MibTableColumn
tacacspSrvBlockTimeout = _TacacspSrvBlockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 16),
    _TacacspSrvBlockTimeout_Type()
)
tacacspSrvBlockTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvBlockTimeout.setStatus("mandatory")


class _TacacspSrvAuthentNoResp_Type(Integer32):
    """Custom type tacacspSrvAuthentNoResp based on Integer32"""
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
        *(("connection-bydefault", 1),
          ("connection-bylocalloginpwd", 2),
          ("connection-forbidden", 3))
    )


_TacacspSrvAuthentNoResp_Type.__name__ = "Integer32"
_TacacspSrvAuthentNoResp_Object = MibTableColumn
tacacspSrvAuthentNoResp = _TacacspSrvAuthentNoResp_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 17),
    _TacacspSrvAuthentNoResp_Type()
)
tacacspSrvAuthentNoResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvAuthentNoResp.setStatus("mandatory")


class _TacacspSrvAuthentNegResp_Type(Integer32):
    """Custom type tacacspSrvAuthentNegResp based on Integer32"""
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
        *(("connection-bydefault", 1),
          ("connection-bylocalloginpwd", 2),
          ("connection-forbidden", 3))
    )


_TacacspSrvAuthentNegResp_Type.__name__ = "Integer32"
_TacacspSrvAuthentNegResp_Object = MibTableColumn
tacacspSrvAuthentNegResp = _TacacspSrvAuthentNegResp_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 18),
    _TacacspSrvAuthentNegResp_Type()
)
tacacspSrvAuthentNegResp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvAuthentNegResp.setStatus("mandatory")


class _TacacspSrvPrivLvlOnLogin_Type(Integer32):
    """Custom type tacacspSrvPrivLvlOnLogin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_TacacspSrvPrivLvlOnLogin_Type.__name__ = "Integer32"
_TacacspSrvPrivLvlOnLogin_Object = MibTableColumn
tacacspSrvPrivLvlOnLogin = _TacacspSrvPrivLvlOnLogin_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 13, 1, 1, 19),
    _TacacspSrvPrivLvlOnLogin_Type()
)
tacacspSrvPrivLvlOnLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacspSrvPrivLvlOnLogin.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-TACACSP-MIB",
    **{"bintec": bintec,
       "bintecsec": bintecsec,
       "tacacsp": tacacsp,
       "tacacspServerTable": tacacspServerTable,
       "tacacspServerEntry": tacacspServerEntry,
       "tacacspSrvPriority": tacacspSrvPriority,
       "tacacspSrvAddress": tacacspSrvAddress,
       "tacacspSrvTcpPort": tacacspSrvTcpPort,
       "tacacspSrvSecret": tacacspSrvSecret,
       "tacacspSrvTimeout": tacacspSrvTimeout,
       "tacacspSrvAdminStatus": tacacspSrvAdminStatus,
       "tacacspSrvOperStatus": tacacspSrvOperStatus,
       "tacacspSrvPolicy": tacacspSrvPolicy,
       "tacacspSrvEncrMode": tacacspSrvEncrMode,
       "tacacspSrvMultiSession": tacacspSrvMultiSession,
       "tacacspSrvPppAuth": tacacspSrvPppAuth,
       "tacacspSrvLoginAuth": tacacspSrvLoginAuth,
       "tacacspSrvAccounting": tacacspSrvAccounting,
       "tacacspSrvBlockTimeout": tacacspSrvBlockTimeout,
       "tacacspSrvAuthentNoResp": tacacspSrvAuthentNoResp,
       "tacacspSrvAuthentNegResp": tacacspSrvAuthentNegResp,
       "tacacspSrvPrivLvlOnLogin": tacacspSrvPrivLvlOnLogin}
)
