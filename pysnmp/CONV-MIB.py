# SNMP MIB module (CONV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CONV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:02 2024
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

(Alias,
 cxConv) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxConv")

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

_CxConvTable_Object = MibTable
cxConvTable = _CxConvTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 1)
)
if mibBuilder.loadTexts:
    cxConvTable.setStatus("mandatory")
_CxConvEntry_Object = MibTableRow
cxConvEntry = _CxConvEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 1, 1)
)
cxConvEntry.setIndexNames(
    (0, "CONV-MIB", "cxConvPort"),
)
if mibBuilder.loadTexts:
    cxConvEntry.setStatus("mandatory")


class _CxConvPort_Type(Integer32):
    """Custom type cxConvPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CxConvPort_Type.__name__ = "Integer32"
_CxConvPort_Object = MibTableColumn
cxConvPort = _CxConvPort_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 1, 1, 1),
    _CxConvPort_Type()
)
cxConvPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxConvPort.setStatus("mandatory")
_CxConvPortAlias_Type = Alias
_CxConvPortAlias_Object = MibTableColumn
cxConvPortAlias = _CxConvPortAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 1, 1, 2),
    _CxConvPortAlias_Type()
)
cxConvPortAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxConvPortAlias.setStatus("mandatory")


class _CxConvRowStatus_Type(Integer32):
    """Custom type cxConvRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxConvRowStatus_Type.__name__ = "Integer32"
_CxConvRowStatus_Object = MibTableColumn
cxConvRowStatus = _CxConvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 1, 1, 3),
    _CxConvRowStatus_Type()
)
cxConvRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxConvRowStatus.setStatus("mandatory")
_CxConvIfIndex_Type = Integer32
_CxConvIfIndex_Object = MibTableColumn
cxConvIfIndex = _CxConvIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 1, 1, 4),
    _CxConvIfIndex_Type()
)
cxConvIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxConvIfIndex.setStatus("mandatory")


class _CxConvState_Type(Integer32):
    """Custom type cxConvState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_CxConvState_Type.__name__ = "Integer32"
_CxConvState_Object = MibTableColumn
cxConvState = _CxConvState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 1, 1, 5),
    _CxConvState_Type()
)
cxConvState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxConvState.setStatus("mandatory")
_CxConvCompression_Type = Integer32
_CxConvCompression_Object = MibTableColumn
cxConvCompression = _CxConvCompression_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 1, 1, 6),
    _CxConvCompression_Type()
)
cxConvCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxConvCompression.setStatus("mandatory")


class _CxConvCompCompatibility_Type(Integer32):
    """Custom type cxConvCompCompatibility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compatibleACC", 2),
          ("compatibleMemotec", 1))
    )


_CxConvCompCompatibility_Type.__name__ = "Integer32"
_CxConvCompCompatibility_Object = MibTableColumn
cxConvCompCompatibility = _CxConvCompCompatibility_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 1, 1, 7),
    _CxConvCompCompatibility_Type()
)
cxConvCompCompatibility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxConvCompCompatibility.setStatus("mandatory")
_CxFwkCircuitTable_Object = MibTable
cxFwkCircuitTable = _CxFwkCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2)
)
if mibBuilder.loadTexts:
    cxFwkCircuitTable.setStatus("mandatory")
_CxFwkCircuitEntry_Object = MibTableRow
cxFwkCircuitEntry = _CxFwkCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1)
)
cxFwkCircuitEntry.setIndexNames(
    (0, "CONV-MIB", "cxFwkCircuitPort"),
)
if mibBuilder.loadTexts:
    cxFwkCircuitEntry.setStatus("mandatory")
_CxFwkCircuitPort_Type = Integer32
_CxFwkCircuitPort_Object = MibTableColumn
cxFwkCircuitPort = _CxFwkCircuitPort_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 1),
    _CxFwkCircuitPort_Type()
)
cxFwkCircuitPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFwkCircuitPort.setStatus("mandatory")


class _CxFwkCircuitState_Type(Integer32):
    """Custom type cxFwkCircuitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              256)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("idle", 256),
          ("openFailed", 4),
          ("opened", 1),
          ("opening", 3))
    )


_CxFwkCircuitState_Type.__name__ = "Integer32"
_CxFwkCircuitState_Object = MibTableColumn
cxFwkCircuitState = _CxFwkCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 2),
    _CxFwkCircuitState_Type()
)
cxFwkCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFwkCircuitState.setStatus("mandatory")


class _CxFwkCircuitRowStatus_Type(Integer32):
    """Custom type cxFwkCircuitRowStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_CxFwkCircuitRowStatus_Type.__name__ = "Integer32"
_CxFwkCircuitRowStatus_Object = MibTableColumn
cxFwkCircuitRowStatus = _CxFwkCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 3),
    _CxFwkCircuitRowStatus_Type()
)
cxFwkCircuitRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFwkCircuitRowStatus.setStatus("mandatory")


class _CxFwkServiceType_Type(Integer32):
    """Custom type cxFwkServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              256)
        )
    )
    namedValues = NamedValues(
        *(("frameRelay", 1),
          ("notSpecified", 256))
    )


_CxFwkServiceType_Type.__name__ = "Integer32"
_CxFwkServiceType_Object = MibTableColumn
cxFwkServiceType = _CxFwkServiceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 4),
    _CxFwkServiceType_Type()
)
cxFwkServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFwkServiceType.setStatus("mandatory")


class _CxFwkServiceProtocol_Type(Integer32):
    """Custom type cxFwkServiceProtocol based on Integer32"""
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
        *(("char", 4),
          ("cls", 1),
          ("pvc", 2),
          ("svc", 3))
    )


_CxFwkServiceProtocol_Type.__name__ = "Integer32"
_CxFwkServiceProtocol_Object = MibTableColumn
cxFwkServiceProtocol = _CxFwkServiceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 5),
    _CxFwkServiceProtocol_Type()
)
cxFwkServiceProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFwkServiceProtocol.setStatus("mandatory")


class _CxFwkServiceName_Type(OctetString):
    """Custom type cxFwkServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_CxFwkServiceName_Type.__name__ = "OctetString"
_CxFwkServiceName_Object = MibTableColumn
cxFwkServiceName = _CxFwkServiceName_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 6),
    _CxFwkServiceName_Type()
)
cxFwkServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFwkServiceName.setStatus("mandatory")


class _CxFwkDestAddress_Type(OctetString):
    """Custom type cxFwkDestAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_CxFwkDestAddress_Type.__name__ = "OctetString"
_CxFwkDestAddress_Object = MibTableColumn
cxFwkDestAddress = _CxFwkDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 7),
    _CxFwkDestAddress_Type()
)
cxFwkDestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFwkDestAddress.setStatus("mandatory")
_CxFwkDestAlias_Type = Alias
_CxFwkDestAlias_Object = MibTableColumn
cxFwkDestAlias = _CxFwkDestAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 8),
    _CxFwkDestAlias_Type()
)
cxFwkDestAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFwkDestAlias.setStatus("mandatory")


class _CxFwkServiceCircuitMdu_Type(Integer32):
    """Custom type cxFwkServiceCircuitMdu based on Integer32"""
    defaultValue = 1600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_CxFwkServiceCircuitMdu_Type.__name__ = "Integer32"
_CxFwkServiceCircuitMdu_Object = MibTableColumn
cxFwkServiceCircuitMdu = _CxFwkServiceCircuitMdu_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 9),
    _CxFwkServiceCircuitMdu_Type()
)
cxFwkServiceCircuitMdu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFwkServiceCircuitMdu.setStatus("mandatory")


class _CxFwkServiceCost_Type(Integer32):
    """Custom type cxFwkServiceCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_CxFwkServiceCost_Type.__name__ = "Integer32"
_CxFwkServiceCost_Object = MibTableColumn
cxFwkServiceCost = _CxFwkServiceCost_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 10),
    _CxFwkServiceCost_Type()
)
cxFwkServiceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFwkServiceCost.setStatus("mandatory")


class _CxFwkServiceCardId_Type(Integer32):
    """Custom type cxFwkServiceCardId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CxFwkServiceCardId_Type.__name__ = "Integer32"
_CxFwkServiceCardId_Object = MibTableColumn
cxFwkServiceCardId = _CxFwkServiceCardId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 11),
    _CxFwkServiceCardId_Type()
)
cxFwkServiceCardId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFwkServiceCardId.setStatus("mandatory")
_CxFwkServiceSapId_Type = Integer32
_CxFwkServiceSapId_Object = MibTableColumn
cxFwkServiceSapId = _CxFwkServiceSapId_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 12),
    _CxFwkServiceSapId_Type()
)
cxFwkServiceSapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFwkServiceSapId.setStatus("mandatory")


class _CxFwkServiceRouteRef_Type(Integer32):
    """Custom type cxFwkServiceRouteRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CxFwkServiceRouteRef_Type.__name__ = "Integer32"
_CxFwkServiceRouteRef_Object = MibTableColumn
cxFwkServiceRouteRef = _CxFwkServiceRouteRef_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 13),
    _CxFwkServiceRouteRef_Type()
)
cxFwkServiceRouteRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cxFwkServiceRouteRef.setStatus("mandatory")
_CxFwkStatsInternalErrors_Type = Counter32
_CxFwkStatsInternalErrors_Object = MibTableColumn
cxFwkStatsInternalErrors = _CxFwkStatsInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 15),
    _CxFwkStatsInternalErrors_Type()
)
cxFwkStatsInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFwkStatsInternalErrors.setStatus("mandatory")
_CxFwkStatsRegistrationErrors_Type = Counter32
_CxFwkStatsRegistrationErrors_Object = MibTableColumn
cxFwkStatsRegistrationErrors = _CxFwkStatsRegistrationErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 16),
    _CxFwkStatsRegistrationErrors_Type()
)
cxFwkStatsRegistrationErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFwkStatsRegistrationErrors.setStatus("mandatory")
_CxFwkStatsQueryErrors_Type = Counter32
_CxFwkStatsQueryErrors_Object = MibTableColumn
cxFwkStatsQueryErrors = _CxFwkStatsQueryErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 17),
    _CxFwkStatsQueryErrors_Type()
)
cxFwkStatsQueryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFwkStatsQueryErrors.setStatus("mandatory")
_CxFwkStatsOpenErrors_Type = Counter32
_CxFwkStatsOpenErrors_Object = MibTableColumn
cxFwkStatsOpenErrors = _CxFwkStatsOpenErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 18),
    _CxFwkStatsOpenErrors_Type()
)
cxFwkStatsOpenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFwkStatsOpenErrors.setStatus("mandatory")
_CxFwkStatsResets_Type = Counter32
_CxFwkStatsResets_Object = MibTableColumn
cxFwkStatsResets = _CxFwkStatsResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 8, 2, 1, 19),
    _CxFwkStatsResets_Type()
)
cxFwkStatsResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cxFwkStatsResets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONV-MIB",
    **{"cxConvTable": cxConvTable,
       "cxConvEntry": cxConvEntry,
       "cxConvPort": cxConvPort,
       "cxConvPortAlias": cxConvPortAlias,
       "cxConvRowStatus": cxConvRowStatus,
       "cxConvIfIndex": cxConvIfIndex,
       "cxConvState": cxConvState,
       "cxConvCompression": cxConvCompression,
       "cxConvCompCompatibility": cxConvCompCompatibility,
       "cxFwkCircuitTable": cxFwkCircuitTable,
       "cxFwkCircuitEntry": cxFwkCircuitEntry,
       "cxFwkCircuitPort": cxFwkCircuitPort,
       "cxFwkCircuitState": cxFwkCircuitState,
       "cxFwkCircuitRowStatus": cxFwkCircuitRowStatus,
       "cxFwkServiceType": cxFwkServiceType,
       "cxFwkServiceProtocol": cxFwkServiceProtocol,
       "cxFwkServiceName": cxFwkServiceName,
       "cxFwkDestAddress": cxFwkDestAddress,
       "cxFwkDestAlias": cxFwkDestAlias,
       "cxFwkServiceCircuitMdu": cxFwkServiceCircuitMdu,
       "cxFwkServiceCost": cxFwkServiceCost,
       "cxFwkServiceCardId": cxFwkServiceCardId,
       "cxFwkServiceSapId": cxFwkServiceSapId,
       "cxFwkServiceRouteRef": cxFwkServiceRouteRef,
       "cxFwkStatsInternalErrors": cxFwkStatsInternalErrors,
       "cxFwkStatsRegistrationErrors": cxFwkStatsRegistrationErrors,
       "cxFwkStatsQueryErrors": cxFwkStatsQueryErrors,
       "cxFwkStatsOpenErrors": cxFwkStatsOpenErrors,
       "cxFwkStatsResets": cxFwkStatsResets}
)
