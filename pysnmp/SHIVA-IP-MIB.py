# SNMP MIB module (SHIVA-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SHIVA-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:51:26 2024
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

(tIP,) = mibBuilder.importSymbols(
    "SHIVA-MIB",
    "tIP")

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



class _TARPClearCache_Type(Integer32):
    """Custom type tARPClearCache based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TARPClearCache_Type.__name__ = "Integer32"
_TARPClearCache_Object = MibScalar
tARPClearCache = _TARPClearCache_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 1),
    _TARPClearCache_Type()
)
tARPClearCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tARPClearCache.setStatus("mandatory")


class _TIPClearRedirects_Type(Integer32):
    """Custom type tIPClearRedirects based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TIPClearRedirects_Type.__name__ = "Integer32"
_TIPClearRedirects_Object = MibScalar
tIPClearRedirects = _TIPClearRedirects_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 2),
    _TIPClearRedirects_Type()
)
tIPClearRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tIPClearRedirects.setStatus("mandatory")


class _TUDPChecksums_Type(Integer32):
    """Custom type tUDPChecksums based on Integer32"""
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


_TUDPChecksums_Type.__name__ = "Integer32"
_TUDPChecksums_Object = MibScalar
tUDPChecksums = _TUDPChecksums_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 3),
    _TUDPChecksums_Type()
)
tUDPChecksums.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tUDPChecksums.setStatus("mandatory")


class _TIPBroadCastFill_Type(Integer32):
    """Custom type tIPBroadCastFill based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ones", 1),
          ("zeroes", 2))
    )


_TIPBroadCastFill_Type.__name__ = "Integer32"
_TIPBroadCastFill_Object = MibScalar
tIPBroadCastFill = _TIPBroadCastFill_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 4),
    _TIPBroadCastFill_Type()
)
tIPBroadCastFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tIPBroadCastFill.setStatus("mandatory")
_TTimeServerTable_Object = MibTable
tTimeServerTable = _TTimeServerTable_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 5)
)
if mibBuilder.loadTexts:
    tTimeServerTable.setStatus("mandatory")
_TTimeServerEntry_Object = MibTableRow
tTimeServerEntry = _TTimeServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 5, 1)
)
tTimeServerEntry.setIndexNames(
    (0, "SHIVA-IP-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    tTimeServerEntry.setStatus("mandatory")
_TTimeServerAddress_Type = IpAddress
_TTimeServerAddress_Object = MibTableColumn
tTimeServerAddress = _TTimeServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 5, 1, 1),
    _TTimeServerAddress_Type()
)
tTimeServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tTimeServerAddress.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 5, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_TNameServerTable_Object = MibTable
tNameServerTable = _TNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 6)
)
if mibBuilder.loadTexts:
    tNameServerTable.setStatus("mandatory")
_TNameServerEntry_Object = MibTableRow
tNameServerEntry = _TNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 6, 1)
)
tNameServerEntry.setIndexNames(
    (0, "SHIVA-IP-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    tNameServerEntry.setStatus("mandatory")
_TNameServerAddress_Type = IpAddress
_TNameServerAddress_Object = MibTableColumn
tNameServerAddress = _TNameServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 6, 1, 1),
    _TNameServerAddress_Type()
)
tNameServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tNameServerAddress.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 6, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_TBootServerAddress_Type = IpAddress
_TBootServerAddress_Object = MibScalar
tBootServerAddress = _TBootServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 7),
    _TBootServerAddress_Type()
)
tBootServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tBootServerAddress.setStatus("mandatory")
_TSerialIpAddressTable_Object = MibTable
tSerialIpAddressTable = _TSerialIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 8)
)
if mibBuilder.loadTexts:
    tSerialIpAddressTable.setStatus("mandatory")
_TSerialIpAddressEntry_Object = MibTableRow
tSerialIpAddressEntry = _TSerialIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 8, 1)
)
tSerialIpAddressEntry.setIndexNames(
    (0, "SHIVA-IP-MIB", "tSerialIpAddressIndex"),
)
if mibBuilder.loadTexts:
    tSerialIpAddressEntry.setStatus("mandatory")
_TSerialIpAddressIndex_Type = Integer32
_TSerialIpAddressIndex_Object = MibTableColumn
tSerialIpAddressIndex = _TSerialIpAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 8, 1, 1),
    _TSerialIpAddressIndex_Type()
)
tSerialIpAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tSerialIpAddressIndex.setStatus("mandatory")
_TSerialIpAddressLocalDefaultAddress_Type = IpAddress
_TSerialIpAddressLocalDefaultAddress_Object = MibTableColumn
tSerialIpAddressLocalDefaultAddress = _TSerialIpAddressLocalDefaultAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 8, 1, 2),
    _TSerialIpAddressLocalDefaultAddress_Type()
)
tSerialIpAddressLocalDefaultAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSerialIpAddressLocalDefaultAddress.setStatus("mandatory")
_TSerialIpAddressRemoteDefaultAddress_Type = IpAddress
_TSerialIpAddressRemoteDefaultAddress_Object = MibTableColumn
tSerialIpAddressRemoteDefaultAddress = _TSerialIpAddressRemoteDefaultAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 8, 1, 3),
    _TSerialIpAddressRemoteDefaultAddress_Type()
)
tSerialIpAddressRemoteDefaultAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSerialIpAddressRemoteDefaultAddress.setStatus("deprecated")
_TSerialIpAddressLocalAddress_Type = IpAddress
_TSerialIpAddressLocalAddress_Object = MibTableColumn
tSerialIpAddressLocalAddress = _TSerialIpAddressLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 8, 1, 4),
    _TSerialIpAddressLocalAddress_Type()
)
tSerialIpAddressLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSerialIpAddressLocalAddress.setStatus("deprecated")
_TSerialIpAddressRemoteAddress_Type = IpAddress
_TSerialIpAddressRemoteAddress_Object = MibTableColumn
tSerialIpAddressRemoteAddress = _TSerialIpAddressRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 8, 1, 5),
    _TSerialIpAddressRemoteAddress_Type()
)
tSerialIpAddressRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tSerialIpAddressRemoteAddress.setStatus("mandatory")


class _TAcceptAnyClientAddr_Type(Integer32):
    """Custom type tAcceptAnyClientAddr based on Integer32"""
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


_TAcceptAnyClientAddr_Type.__name__ = "Integer32"
_TAcceptAnyClientAddr_Object = MibScalar
tAcceptAnyClientAddr = _TAcceptAnyClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 9),
    _TAcceptAnyClientAddr_Type()
)
tAcceptAnyClientAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tAcceptAnyClientAddr.setStatus("mandatory")
_TNumIpRoutes_Type = Integer32
_TNumIpRoutes_Object = MibScalar
tNumIpRoutes = _TNumIpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 10),
    _TNumIpRoutes_Type()
)
tNumIpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tNumIpRoutes.setStatus("mandatory")


class _TUseConfiguredUserAddr_Type(Integer32):
    """Custom type tUseConfiguredUserAddr based on Integer32"""
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


_TUseConfiguredUserAddr_Type.__name__ = "Integer32"
_TUseConfiguredUserAddr_Object = MibScalar
tUseConfiguredUserAddr = _TUseConfiguredUserAddr_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 11),
    _TUseConfiguredUserAddr_Type()
)
tUseConfiguredUserAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tUseConfiguredUserAddr.setStatus("mandatory")


class _TUseConfiguredPortAddr_Type(Integer32):
    """Custom type tUseConfiguredPortAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("disabled", 2)
    )


_TUseConfiguredPortAddr_Type.__name__ = "Integer32"
_TUseConfiguredPortAddr_Object = MibScalar
tUseConfiguredPortAddr = _TUseConfiguredPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 12),
    _TUseConfiguredPortAddr_Type()
)
tUseConfiguredPortAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tUseConfiguredPortAddr.setStatus("deprecated")


class _TUseDHCPAddr_Type(Integer32):
    """Custom type tUseDHCPAddr based on Integer32"""
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


_TUseDHCPAddr_Type.__name__ = "Integer32"
_TUseDHCPAddr_Object = MibScalar
tUseDHCPAddr = _TUseDHCPAddr_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 13),
    _TUseDHCPAddr_Type()
)
tUseDHCPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tUseDHCPAddr.setStatus("mandatory")
_THomeIPAddr_Type = IpAddress
_THomeIPAddr_Object = MibScalar
tHomeIPAddr = _THomeIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 14),
    _THomeIPAddr_Type()
)
tHomeIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tHomeIPAddr.setStatus("mandatory")


class _TUsePoolAddr_Type(Integer32):
    """Custom type tUsePoolAddr based on Integer32"""
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


_TUsePoolAddr_Type.__name__ = "Integer32"
_TUsePoolAddr_Object = MibScalar
tUsePoolAddr = _TUsePoolAddr_Object(
    (1, 3, 6, 1, 4, 1, 166, 4, 3, 15),
    _TUsePoolAddr_Type()
)
tUsePoolAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tUsePoolAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SHIVA-IP-MIB",
    **{"tARPClearCache": tARPClearCache,
       "tIPClearRedirects": tIPClearRedirects,
       "tUDPChecksums": tUDPChecksums,
       "tIPBroadCastFill": tIPBroadCastFill,
       "tTimeServerTable": tTimeServerTable,
       "tTimeServerEntry": tTimeServerEntry,
       "tTimeServerAddress": tTimeServerAddress,
       "pysmiFakeCol1": pysmiFakeCol1,
       "tNameServerTable": tNameServerTable,
       "tNameServerEntry": tNameServerEntry,
       "tNameServerAddress": tNameServerAddress,
       "pysmiFakeCol2": pysmiFakeCol2,
       "tBootServerAddress": tBootServerAddress,
       "tSerialIpAddressTable": tSerialIpAddressTable,
       "tSerialIpAddressEntry": tSerialIpAddressEntry,
       "tSerialIpAddressIndex": tSerialIpAddressIndex,
       "tSerialIpAddressLocalDefaultAddress": tSerialIpAddressLocalDefaultAddress,
       "tSerialIpAddressRemoteDefaultAddress": tSerialIpAddressRemoteDefaultAddress,
       "tSerialIpAddressLocalAddress": tSerialIpAddressLocalAddress,
       "tSerialIpAddressRemoteAddress": tSerialIpAddressRemoteAddress,
       "tAcceptAnyClientAddr": tAcceptAnyClientAddr,
       "tNumIpRoutes": tNumIpRoutes,
       "tUseConfiguredUserAddr": tUseConfiguredUserAddr,
       "tUseConfiguredPortAddr": tUseConfiguredPortAddr,
       "tUseDHCPAddr": tUseDHCPAddr,
       "tHomeIPAddr": tHomeIPAddr,
       "tUsePoolAddr": tUsePoolAddr}
)
