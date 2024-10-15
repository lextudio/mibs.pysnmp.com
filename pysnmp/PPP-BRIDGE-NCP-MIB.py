# SNMP MIB module (PPP-BRIDGE-NCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PPP-BRIDGE-NCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:00 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ppp,) = mibBuilder.importSymbols(
    "PPP-LCP-MIB",
    "ppp")

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

_PppBridge_ObjectIdentity = ObjectIdentity
pppBridge = _PppBridge_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 23, 4)
)
_PppBridgeTable_Object = MibTable
pppBridgeTable = _PppBridgeTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 1)
)
if mibBuilder.loadTexts:
    pppBridgeTable.setStatus("mandatory")
_PppBridgeEntry_Object = MibTableRow
pppBridgeEntry = _PppBridgeEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1)
)
pppBridgeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppBridgeEntry.setStatus("mandatory")


class _PppBridgeOperStatus_Type(Integer32):
    """Custom type pppBridgeOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-opened", 2),
          ("opened", 1))
    )


_PppBridgeOperStatus_Type.__name__ = "Integer32"
_PppBridgeOperStatus_Object = MibTableColumn
pppBridgeOperStatus = _PppBridgeOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 1),
    _PppBridgeOperStatus_Type()
)
pppBridgeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBridgeOperStatus.setStatus("mandatory")


class _PppBridgeLocalToRemoteTinygramCompression_Type(Integer32):
    """Custom type pppBridgeLocalToRemoteTinygramCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_PppBridgeLocalToRemoteTinygramCompression_Type.__name__ = "Integer32"
_PppBridgeLocalToRemoteTinygramCompression_Object = MibTableColumn
pppBridgeLocalToRemoteTinygramCompression = _PppBridgeLocalToRemoteTinygramCompression_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 2),
    _PppBridgeLocalToRemoteTinygramCompression_Type()
)
pppBridgeLocalToRemoteTinygramCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBridgeLocalToRemoteTinygramCompression.setStatus("mandatory")


class _PppBridgeRemoteToLocalTinygramCompression_Type(Integer32):
    """Custom type pppBridgeRemoteToLocalTinygramCompression based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_PppBridgeRemoteToLocalTinygramCompression_Type.__name__ = "Integer32"
_PppBridgeRemoteToLocalTinygramCompression_Object = MibTableColumn
pppBridgeRemoteToLocalTinygramCompression = _PppBridgeRemoteToLocalTinygramCompression_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 3),
    _PppBridgeRemoteToLocalTinygramCompression_Type()
)
pppBridgeRemoteToLocalTinygramCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBridgeRemoteToLocalTinygramCompression.setStatus("mandatory")


class _PppBridgeLocalToRemoteLanId_Type(Integer32):
    """Custom type pppBridgeLocalToRemoteLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_PppBridgeLocalToRemoteLanId_Type.__name__ = "Integer32"
_PppBridgeLocalToRemoteLanId_Object = MibTableColumn
pppBridgeLocalToRemoteLanId = _PppBridgeLocalToRemoteLanId_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 4),
    _PppBridgeLocalToRemoteLanId_Type()
)
pppBridgeLocalToRemoteLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBridgeLocalToRemoteLanId.setStatus("mandatory")


class _PppBridgeRemoteToLocalLanId_Type(Integer32):
    """Custom type pppBridgeRemoteToLocalLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_PppBridgeRemoteToLocalLanId_Type.__name__ = "Integer32"
_PppBridgeRemoteToLocalLanId_Object = MibTableColumn
pppBridgeRemoteToLocalLanId = _PppBridgeRemoteToLocalLanId_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 1, 1, 5),
    _PppBridgeRemoteToLocalLanId_Type()
)
pppBridgeRemoteToLocalLanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBridgeRemoteToLocalLanId.setStatus("mandatory")
_PppBridgeConfigTable_Object = MibTable
pppBridgeConfigTable = _PppBridgeConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 2)
)
if mibBuilder.loadTexts:
    pppBridgeConfigTable.setStatus("mandatory")
_PppBridgeConfigEntry_Object = MibTableRow
pppBridgeConfigEntry = _PppBridgeConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1)
)
pppBridgeConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pppBridgeConfigEntry.setStatus("mandatory")


class _PppBridgeConfigAdminStatus_Type(Integer32):
    """Custom type pppBridgeConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_PppBridgeConfigAdminStatus_Type.__name__ = "Integer32"
_PppBridgeConfigAdminStatus_Object = MibTableColumn
pppBridgeConfigAdminStatus = _PppBridgeConfigAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 1),
    _PppBridgeConfigAdminStatus_Type()
)
pppBridgeConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppBridgeConfigAdminStatus.setStatus("mandatory")


class _PppBridgeConfigTinygram_Type(Integer32):
    """Custom type pppBridgeConfigTinygram based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_PppBridgeConfigTinygram_Type.__name__ = "Integer32"
_PppBridgeConfigTinygram_Object = MibTableColumn
pppBridgeConfigTinygram = _PppBridgeConfigTinygram_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 2),
    _PppBridgeConfigTinygram_Type()
)
pppBridgeConfigTinygram.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppBridgeConfigTinygram.setStatus("mandatory")


class _PppBridgeConfigRingId_Type(Integer32):
    """Custom type pppBridgeConfigRingId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_PppBridgeConfigRingId_Type.__name__ = "Integer32"
_PppBridgeConfigRingId_Object = MibTableColumn
pppBridgeConfigRingId = _PppBridgeConfigRingId_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 3),
    _PppBridgeConfigRingId_Type()
)
pppBridgeConfigRingId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppBridgeConfigRingId.setStatus("mandatory")


class _PppBridgeConfigLineId_Type(Integer32):
    """Custom type pppBridgeConfigLineId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_PppBridgeConfigLineId_Type.__name__ = "Integer32"
_PppBridgeConfigLineId_Object = MibTableColumn
pppBridgeConfigLineId = _PppBridgeConfigLineId_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 4),
    _PppBridgeConfigLineId_Type()
)
pppBridgeConfigLineId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppBridgeConfigLineId.setStatus("mandatory")


class _PppBridgeConfigLanId_Type(Integer32):
    """Custom type pppBridgeConfigLanId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_PppBridgeConfigLanId_Type.__name__ = "Integer32"
_PppBridgeConfigLanId_Object = MibTableColumn
pppBridgeConfigLanId = _PppBridgeConfigLanId_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 2, 1, 5),
    _PppBridgeConfigLanId_Type()
)
pppBridgeConfigLanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppBridgeConfigLanId.setStatus("mandatory")
_PppBridgeMediaTable_Object = MibTable
pppBridgeMediaTable = _PppBridgeMediaTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 3)
)
if mibBuilder.loadTexts:
    pppBridgeMediaTable.setStatus("mandatory")
_PppBridgeMediaEntry_Object = MibTableRow
pppBridgeMediaEntry = _PppBridgeMediaEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1)
)
pppBridgeMediaEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PPP-BRIDGE-NCP-MIB", "pppBridgeMediaMacType"),
)
if mibBuilder.loadTexts:
    pppBridgeMediaEntry.setStatus("mandatory")


class _PppBridgeMediaMacType_Type(Integer32):
    """Custom type pppBridgeMediaMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppBridgeMediaMacType_Type.__name__ = "Integer32"
_PppBridgeMediaMacType_Object = MibTableColumn
pppBridgeMediaMacType = _PppBridgeMediaMacType_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 1),
    _PppBridgeMediaMacType_Type()
)
pppBridgeMediaMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBridgeMediaMacType.setStatus("mandatory")


class _PppBridgeMediaLocalStatus_Type(Integer32):
    """Custom type pppBridgeMediaLocalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("dont-accept", 2))
    )


_PppBridgeMediaLocalStatus_Type.__name__ = "Integer32"
_PppBridgeMediaLocalStatus_Object = MibTableColumn
pppBridgeMediaLocalStatus = _PppBridgeMediaLocalStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 2),
    _PppBridgeMediaLocalStatus_Type()
)
pppBridgeMediaLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBridgeMediaLocalStatus.setStatus("mandatory")


class _PppBridgeMediaRemoteStatus_Type(Integer32):
    """Custom type pppBridgeMediaRemoteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("dont-accept", 2))
    )


_PppBridgeMediaRemoteStatus_Type.__name__ = "Integer32"
_PppBridgeMediaRemoteStatus_Object = MibTableColumn
pppBridgeMediaRemoteStatus = _PppBridgeMediaRemoteStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 3, 1, 3),
    _PppBridgeMediaRemoteStatus_Type()
)
pppBridgeMediaRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppBridgeMediaRemoteStatus.setStatus("mandatory")
_PppBridgeMediaConfigTable_Object = MibTable
pppBridgeMediaConfigTable = _PppBridgeMediaConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 4)
)
if mibBuilder.loadTexts:
    pppBridgeMediaConfigTable.setStatus("mandatory")
_PppBridgeMediaConfigEntry_Object = MibTableRow
pppBridgeMediaConfigEntry = _PppBridgeMediaConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1)
)
pppBridgeMediaConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "PPP-BRIDGE-NCP-MIB", "pppBridgeMediaConfigMacType"),
)
if mibBuilder.loadTexts:
    pppBridgeMediaConfigEntry.setStatus("mandatory")


class _PppBridgeMediaConfigMacType_Type(Integer32):
    """Custom type pppBridgeMediaConfigMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PppBridgeMediaConfigMacType_Type.__name__ = "Integer32"
_PppBridgeMediaConfigMacType_Object = MibTableColumn
pppBridgeMediaConfigMacType = _PppBridgeMediaConfigMacType_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1, 1),
    _PppBridgeMediaConfigMacType_Type()
)
pppBridgeMediaConfigMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppBridgeMediaConfigMacType.setStatus("mandatory")


class _PppBridgeMediaConfigLocalStatus_Type(Integer32):
    """Custom type pppBridgeMediaConfigLocalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("dont-accept", 2))
    )


_PppBridgeMediaConfigLocalStatus_Type.__name__ = "Integer32"
_PppBridgeMediaConfigLocalStatus_Object = MibTableColumn
pppBridgeMediaConfigLocalStatus = _PppBridgeMediaConfigLocalStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 23, 4, 4, 1, 2),
    _PppBridgeMediaConfigLocalStatus_Type()
)
pppBridgeMediaConfigLocalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppBridgeMediaConfigLocalStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PPP-BRIDGE-NCP-MIB",
    **{"pppBridge": pppBridge,
       "pppBridgeTable": pppBridgeTable,
       "pppBridgeEntry": pppBridgeEntry,
       "pppBridgeOperStatus": pppBridgeOperStatus,
       "pppBridgeLocalToRemoteTinygramCompression": pppBridgeLocalToRemoteTinygramCompression,
       "pppBridgeRemoteToLocalTinygramCompression": pppBridgeRemoteToLocalTinygramCompression,
       "pppBridgeLocalToRemoteLanId": pppBridgeLocalToRemoteLanId,
       "pppBridgeRemoteToLocalLanId": pppBridgeRemoteToLocalLanId,
       "pppBridgeConfigTable": pppBridgeConfigTable,
       "pppBridgeConfigEntry": pppBridgeConfigEntry,
       "pppBridgeConfigAdminStatus": pppBridgeConfigAdminStatus,
       "pppBridgeConfigTinygram": pppBridgeConfigTinygram,
       "pppBridgeConfigRingId": pppBridgeConfigRingId,
       "pppBridgeConfigLineId": pppBridgeConfigLineId,
       "pppBridgeConfigLanId": pppBridgeConfigLanId,
       "pppBridgeMediaTable": pppBridgeMediaTable,
       "pppBridgeMediaEntry": pppBridgeMediaEntry,
       "pppBridgeMediaMacType": pppBridgeMediaMacType,
       "pppBridgeMediaLocalStatus": pppBridgeMediaLocalStatus,
       "pppBridgeMediaRemoteStatus": pppBridgeMediaRemoteStatus,
       "pppBridgeMediaConfigTable": pppBridgeMediaConfigTable,
       "pppBridgeMediaConfigEntry": pppBridgeMediaConfigEntry,
       "pppBridgeMediaConfigMacType": pppBridgeMediaConfigMacType,
       "pppBridgeMediaConfigLocalStatus": pppBridgeMediaConfigLocalStatus}
)
