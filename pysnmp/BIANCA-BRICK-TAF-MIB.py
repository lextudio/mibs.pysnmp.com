# SNMP MIB module (BIANCA-BRICK-TAF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BIANCA-BRICK-TAF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:47:48 2024
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

(Date,) = mibBuilder.importSymbols(
    "BIANCA-BRICK-PPP-MIB",
    "Date")

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
_IpTafTable_Object = MibTable
ipTafTable = _IpTafTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 17)
)
if mibBuilder.loadTexts:
    ipTafTable.setStatus("mandatory")
_IpTafEntry_Object = MibTableRow
ipTafEntry = _IpTafEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1)
)
ipTafEntry.setIndexNames(
    (0, "BIANCA-BRICK-TAF-MIB", "ipTafIfIndex"),
)
if mibBuilder.loadTexts:
    ipTafEntry.setStatus("mandatory")
_IpTafIfIndex_Type = Integer32
_IpTafIfIndex_Object = MibTableColumn
ipTafIfIndex = _IpTafIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 1),
    _IpTafIfIndex_Type()
)
ipTafIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTafIfIndex.setStatus("mandatory")
_IpTafAddress_Type = IpAddress
_IpTafAddress_Object = MibTableColumn
ipTafAddress = _IpTafAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 2),
    _IpTafAddress_Type()
)
ipTafAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTafAddress.setStatus("mandatory")


class _IpTafState_Type(Integer32):
    """Custom type ipTafState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authenticating", 2),
          ("idle", 1),
          ("xfer", 3))
    )


_IpTafState_Type.__name__ = "Integer32"
_IpTafState_Object = MibTableColumn
ipTafState = _IpTafState_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 3),
    _IpTafState_Type()
)
ipTafState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTafState.setStatus("mandatory")
_IpTafAuthTime_Type = Date
_IpTafAuthTime_Object = MibTableColumn
ipTafAuthTime = _IpTafAuthTime_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 4),
    _IpTafAuthTime_Type()
)
ipTafAuthTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTafAuthTime.setStatus("mandatory")
_IpTafTimeout_Type = Integer32
_IpTafTimeout_Object = MibTableColumn
ipTafTimeout = _IpTafTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 4, 5, 17, 1, 5),
    _IpTafTimeout_Type()
)
ipTafTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTafTimeout.setStatus("mandatory")
_Bintecsec_ObjectIdentity = ObjectIdentity
bintecsec = _Bintecsec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 254)
)
_Taf_ObjectIdentity = ObjectIdentity
taf = _Taf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 272, 254, 9)
)
_TafServerTable_Object = MibTable
tafServerTable = _TafServerTable_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1)
)
if mibBuilder.loadTexts:
    tafServerTable.setStatus("mandatory")
_TafServerEntry_Object = MibTableRow
tafServerEntry = _TafServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1)
)
tafServerEntry.setIndexNames(
    (0, "BIANCA-BRICK-TAF-MIB", "tafServerType"),
)
if mibBuilder.loadTexts:
    tafServerEntry.setStatus("mandatory")


class _TafServerType_Type(Integer32):
    """Custom type tafServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ace", 1),
          ("none", 2))
    )


_TafServerType_Type.__name__ = "Integer32"
_TafServerType_Object = MibTableColumn
tafServerType = _TafServerType_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 1),
    _TafServerType_Type()
)
tafServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerType.setStatus("mandatory")
_TafServerNodeSecret_Type = OctetString
_TafServerNodeSecret_Object = MibTableColumn
tafServerNodeSecret = _TafServerNodeSecret_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 2),
    _TafServerNodeSecret_Type()
)
tafServerNodeSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerNodeSecret.setStatus("mandatory")
_TafServerVersion_Type = Integer32
_TafServerVersion_Object = MibTableColumn
tafServerVersion = _TafServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 3),
    _TafServerVersion_Type()
)
tafServerVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerVersion.setStatus("mandatory")


class _TafServerRetries_Type(Integer32):
    """Custom type tafServerRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_TafServerRetries_Type.__name__ = "Integer32"
_TafServerRetries_Object = MibTableColumn
tafServerRetries = _TafServerRetries_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 4),
    _TafServerRetries_Type()
)
tafServerRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerRetries.setStatus("mandatory")


class _TafServerTimeout_Type(Integer32):
    """Custom type tafServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TafServerTimeout_Type.__name__ = "Integer32"
_TafServerTimeout_Object = MibTableColumn
tafServerTimeout = _TafServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 5),
    _TafServerTimeout_Type()
)
tafServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerTimeout.setStatus("mandatory")


class _TafServerEncryption_Type(Integer32):
    """Custom type tafServerEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("des", 2),
          ("sdi", 1))
    )


_TafServerEncryption_Type.__name__ = "Integer32"
_TafServerEncryption_Object = MibTableColumn
tafServerEncryption = _TafServerEncryption_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 6),
    _TafServerEncryption_Type()
)
tafServerEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerEncryption.setStatus("mandatory")
_TafServerAddress_Type = IpAddress
_TafServerAddress_Object = MibTableColumn
tafServerAddress = _TafServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 7),
    _TafServerAddress_Type()
)
tafServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerAddress.setStatus("mandatory")
_TafServerPort_Type = Integer32
_TafServerPort_Object = MibTableColumn
tafServerPort = _TafServerPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 8),
    _TafServerPort_Type()
)
tafServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerPort.setStatus("mandatory")
_TafServerClientPort_Type = Integer32
_TafServerClientPort_Object = MibTableColumn
tafServerClientPort = _TafServerClientPort_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 9),
    _TafServerClientPort_Type()
)
tafServerClientPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerClientPort.setStatus("mandatory")


class _TafServerPriority_Type(Integer32):
    """Custom type tafServerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TafServerPriority_Type.__name__ = "Integer32"
_TafServerPriority_Object = MibTableColumn
tafServerPriority = _TafServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 10),
    _TafServerPriority_Type()
)
tafServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerPriority.setStatus("mandatory")


class _TafServerState_Type(Integer32):
    """Custom type tafServerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("delete", 3),
          ("disabled", 2))
    )


_TafServerState_Type.__name__ = "Integer32"
_TafServerState_Object = MibTableColumn
tafServerState = _TafServerState_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 11),
    _TafServerState_Type()
)
tafServerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerState.setStatus("mandatory")


class _TafServerCheckInterface_Type(Integer32):
    """Custom type tafServerCheckInterface based on Integer32"""
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


_TafServerCheckInterface_Type.__name__ = "Integer32"
_TafServerCheckInterface_Object = MibTableColumn
tafServerCheckInterface = _TafServerCheckInterface_Object(
    (1, 3, 6, 1, 4, 1, 272, 254, 9, 1, 1, 12),
    _TafServerCheckInterface_Type()
)
tafServerCheckInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tafServerCheckInterface.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BIANCA-BRICK-TAF-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "bintec": bintec,
       "bibo": bibo,
       "biboip": biboip,
       "ipTafTable": ipTafTable,
       "ipTafEntry": ipTafEntry,
       "ipTafIfIndex": ipTafIfIndex,
       "ipTafAddress": ipTafAddress,
       "ipTafState": ipTafState,
       "ipTafAuthTime": ipTafAuthTime,
       "ipTafTimeout": ipTafTimeout,
       "bintecsec": bintecsec,
       "taf": taf,
       "tafServerTable": tafServerTable,
       "tafServerEntry": tafServerEntry,
       "tafServerType": tafServerType,
       "tafServerNodeSecret": tafServerNodeSecret,
       "tafServerVersion": tafServerVersion,
       "tafServerRetries": tafServerRetries,
       "tafServerTimeout": tafServerTimeout,
       "tafServerEncryption": tafServerEncryption,
       "tafServerAddress": tafServerAddress,
       "tafServerPort": tafServerPort,
       "tafServerClientPort": tafServerClientPort,
       "tafServerPriority": tafServerPriority,
       "tafServerState": tafServerState,
       "tafServerCheckInterface": tafServerCheckInterface}
)
