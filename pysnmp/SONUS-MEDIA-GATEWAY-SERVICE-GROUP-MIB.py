# SNMP MIB module (SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:02 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusSignallingMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusSignallingMIBs")

(SonusBoolean,
 SonusName,
 SonusNameReference) = mibBuilder.importSymbols(
    "SONUS-TC",
    "SonusBoolean",
    "SonusName",
    "SonusNameReference")


# MODULE-IDENTITY

sonusMediaGatewayServiceGroupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusMediaGatewayServiceGroupMIBObjects_ObjectIdentity = ObjectIdentity
sonusMediaGatewayServiceGroupMIBObjects = _SonusMediaGatewayServiceGroupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1)
)
_SonusMgsgServiceGrp_ObjectIdentity = ObjectIdentity
sonusMgsgServiceGrp = _SonusMgsgServiceGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1)
)
_SonusMgsgServiceGrpNextIndex_Type = Integer32
_SonusMgsgServiceGrpNextIndex_Object = MibScalar
sonusMgsgServiceGrpNextIndex = _SonusMgsgServiceGrpNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 1),
    _SonusMgsgServiceGrpNextIndex_Type()
)
sonusMgsgServiceGrpNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpNextIndex.setStatus("current")
_SonusMgsgServiceGrpTable_Object = MibTable
sonusMgsgServiceGrpTable = _SonusMgsgServiceGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpTable.setStatus("current")
_SonusMgsgServiceGrpEntry_Object = MibTableRow
sonusMgsgServiceGrpEntry = _SonusMgsgServiceGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1)
)
sonusMgsgServiceGrpEntry.setIndexNames(
    (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgServiceGrpListIndex"),
)
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpEntry.setStatus("current")
_SonusMgsgServiceGrpListIndex_Type = Integer32
_SonusMgsgServiceGrpListIndex_Object = MibTableColumn
sonusMgsgServiceGrpListIndex = _SonusMgsgServiceGrpListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 1),
    _SonusMgsgServiceGrpListIndex_Type()
)
sonusMgsgServiceGrpListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpListIndex.setStatus("current")
_SonusMgsgServiceGrpName_Type = SonusName
_SonusMgsgServiceGrpName_Object = MibTableColumn
sonusMgsgServiceGrpName = _SonusMgsgServiceGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 2),
    _SonusMgsgServiceGrpName_Type()
)
sonusMgsgServiceGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpName.setStatus("current")


class _SonusMgsgServiceGrpAdminState_Type(Integer32):
    """Custom type sonusMgsgServiceGrpAdminState based on Integer32"""
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


_SonusMgsgServiceGrpAdminState_Type.__name__ = "Integer32"
_SonusMgsgServiceGrpAdminState_Object = MibTableColumn
sonusMgsgServiceGrpAdminState = _SonusMgsgServiceGrpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 3),
    _SonusMgsgServiceGrpAdminState_Type()
)
sonusMgsgServiceGrpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpAdminState.setStatus("current")
_SonusMgsgServiceGrpControllerName_Type = SonusNameReference
_SonusMgsgServiceGrpControllerName_Object = MibTableColumn
sonusMgsgServiceGrpControllerName = _SonusMgsgServiceGrpControllerName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 4),
    _SonusMgsgServiceGrpControllerName_Type()
)
sonusMgsgServiceGrpControllerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpControllerName.setStatus("current")


class _SonusMgsgServiceGrpType_Type(Integer32):
    """Custom type sonusMgsgServiceGrpType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipdc", 1),
          ("mgcp", 2))
    )


_SonusMgsgServiceGrpType_Type.__name__ = "Integer32"
_SonusMgsgServiceGrpType_Object = MibTableColumn
sonusMgsgServiceGrpType = _SonusMgsgServiceGrpType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 5),
    _SonusMgsgServiceGrpType_Type()
)
sonusMgsgServiceGrpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpType.setStatus("current")


class _SonusMgsgServiceGrpMode_Type(Integer32):
    """Custom type sonusMgsgServiceGrpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2))
    )


_SonusMgsgServiceGrpMode_Type.__name__ = "Integer32"
_SonusMgsgServiceGrpMode_Object = MibTableColumn
sonusMgsgServiceGrpMode = _SonusMgsgServiceGrpMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 6),
    _SonusMgsgServiceGrpMode_Type()
)
sonusMgsgServiceGrpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpMode.setStatus("current")


class _SonusMgsgServiceGrpAction_Type(Integer32):
    """Custom type sonusMgsgServiceGrpAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dryup", 1),
          ("force", 2))
    )


_SonusMgsgServiceGrpAction_Type.__name__ = "Integer32"
_SonusMgsgServiceGrpAction_Object = MibTableColumn
sonusMgsgServiceGrpAction = _SonusMgsgServiceGrpAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 7),
    _SonusMgsgServiceGrpAction_Type()
)
sonusMgsgServiceGrpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpAction.setStatus("current")


class _SonusMgsgServiceGrpTimeout_Type(Integer32):
    """Custom type sonusMgsgServiceGrpTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SonusMgsgServiceGrpTimeout_Type.__name__ = "Integer32"
_SonusMgsgServiceGrpTimeout_Object = MibTableColumn
sonusMgsgServiceGrpTimeout = _SonusMgsgServiceGrpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 8),
    _SonusMgsgServiceGrpTimeout_Type()
)
sonusMgsgServiceGrpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpTimeout.setStatus("current")
_SonusMgsgServiceGrpRowStatus_Type = RowStatus
_SonusMgsgServiceGrpRowStatus_Object = MibTableColumn
sonusMgsgServiceGrpRowStatus = _SonusMgsgServiceGrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 1, 2, 1, 9),
    _SonusMgsgServiceGrpRowStatus_Type()
)
sonusMgsgServiceGrpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpRowStatus.setStatus("current")
_SonusMgsgServiceGrpStatTable_Object = MibTable
sonusMgsgServiceGrpStatTable = _SonusMgsgServiceGrpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpStatTable.setStatus("current")
_SonusMgsgServiceGrpStatEntry_Object = MibTableRow
sonusMgsgServiceGrpStatEntry = _SonusMgsgServiceGrpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 2, 1)
)
sonusMgsgServiceGrpStatEntry.setIndexNames(
    (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgServiceGrpStatListIndex"),
)
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpStatEntry.setStatus("current")
_SonusMgsgServiceGrpStatListIndex_Type = Integer32
_SonusMgsgServiceGrpStatListIndex_Object = MibTableColumn
sonusMgsgServiceGrpStatListIndex = _SonusMgsgServiceGrpStatListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 2, 1, 1),
    _SonusMgsgServiceGrpStatListIndex_Type()
)
sonusMgsgServiceGrpStatListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpStatListIndex.setStatus("current")
_SonusMgsgServiceGrpStatName_Type = SonusNameReference
_SonusMgsgServiceGrpStatName_Object = MibTableColumn
sonusMgsgServiceGrpStatName = _SonusMgsgServiceGrpStatName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 2, 1, 2),
    _SonusMgsgServiceGrpStatName_Type()
)
sonusMgsgServiceGrpStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpStatName.setStatus("current")


class _SonusMgsgServiceGrpStatStatus_Type(Integer32):
    """Custom type sonusMgsgServiceGrpStatStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("blocked", 3),
          ("unavailable", 2))
    )


_SonusMgsgServiceGrpStatStatus_Type.__name__ = "Integer32"
_SonusMgsgServiceGrpStatStatus_Object = MibTableColumn
sonusMgsgServiceGrpStatStatus = _SonusMgsgServiceGrpStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 2, 1, 3),
    _SonusMgsgServiceGrpStatStatus_Type()
)
sonusMgsgServiceGrpStatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgServiceGrpStatStatus.setStatus("current")
_SonusMgsgCktTable_Object = MibTable
sonusMgsgCktTable = _SonusMgsgCktTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3)
)
if mibBuilder.loadTexts:
    sonusMgsgCktTable.setStatus("current")
_SonusMgsgCktEntry_Object = MibTableRow
sonusMgsgCktEntry = _SonusMgsgCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1)
)
sonusMgsgCktEntry.setIndexNames(
    (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktShelfIndex"),
    (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktSlotIndex"),
    (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktDs1Index"),
    (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktDs0Index"),
)
if mibBuilder.loadTexts:
    sonusMgsgCktEntry.setStatus("current")


class _SonusMgsgCktShelfIndex_Type(Integer32):
    """Custom type sonusMgsgCktShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusMgsgCktShelfIndex_Type.__name__ = "Integer32"
_SonusMgsgCktShelfIndex_Object = MibTableColumn
sonusMgsgCktShelfIndex = _SonusMgsgCktShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 1),
    _SonusMgsgCktShelfIndex_Type()
)
sonusMgsgCktShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktShelfIndex.setStatus("current")


class _SonusMgsgCktSlotIndex_Type(Integer32):
    """Custom type sonusMgsgCktSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusMgsgCktSlotIndex_Type.__name__ = "Integer32"
_SonusMgsgCktSlotIndex_Object = MibTableColumn
sonusMgsgCktSlotIndex = _SonusMgsgCktSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 2),
    _SonusMgsgCktSlotIndex_Type()
)
sonusMgsgCktSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktSlotIndex.setStatus("current")


class _SonusMgsgCktDs1Index_Type(Integer32):
    """Custom type sonusMgsgCktDs1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_SonusMgsgCktDs1Index_Type.__name__ = "Integer32"
_SonusMgsgCktDs1Index_Object = MibTableColumn
sonusMgsgCktDs1Index = _SonusMgsgCktDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 3),
    _SonusMgsgCktDs1Index_Type()
)
sonusMgsgCktDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktDs1Index.setStatus("current")


class _SonusMgsgCktDs0Index_Type(Integer32):
    """Custom type sonusMgsgCktDs0Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusMgsgCktDs0Index_Type.__name__ = "Integer32"
_SonusMgsgCktDs0Index_Object = MibTableColumn
sonusMgsgCktDs0Index = _SonusMgsgCktDs0Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 4),
    _SonusMgsgCktDs0Index_Type()
)
sonusMgsgCktDs0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktDs0Index.setStatus("current")
_SonusMgsgCktSrvGrpName_Type = SonusNameReference
_SonusMgsgCktSrvGrpName_Object = MibTableColumn
sonusMgsgCktSrvGrpName = _SonusMgsgCktSrvGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 5),
    _SonusMgsgCktSrvGrpName_Type()
)
sonusMgsgCktSrvGrpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgCktSrvGrpName.setStatus("current")


class _SonusMgsgCktMode_Type(Integer32):
    """Custom type sonusMgsgCktMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 1),
          ("unblocked", 2))
    )


_SonusMgsgCktMode_Type.__name__ = "Integer32"
_SonusMgsgCktMode_Object = MibTableColumn
sonusMgsgCktMode = _SonusMgsgCktMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 6),
    _SonusMgsgCktMode_Type()
)
sonusMgsgCktMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgCktMode.setStatus("current")


class _SonusMgsgCktAction_Type(Integer32):
    """Custom type sonusMgsgCktAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dryup", 1),
          ("force", 2))
    )


_SonusMgsgCktAction_Type.__name__ = "Integer32"
_SonusMgsgCktAction_Object = MibTableColumn
sonusMgsgCktAction = _SonusMgsgCktAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 7),
    _SonusMgsgCktAction_Type()
)
sonusMgsgCktAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgCktAction.setStatus("current")


class _SonusMgsgCktTimeout_Type(Integer32):
    """Custom type sonusMgsgCktTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SonusMgsgCktTimeout_Type.__name__ = "Integer32"
_SonusMgsgCktTimeout_Object = MibTableColumn
sonusMgsgCktTimeout = _SonusMgsgCktTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 8),
    _SonusMgsgCktTimeout_Type()
)
sonusMgsgCktTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgCktTimeout.setStatus("current")


class _SonusMgsgCktAdminState_Type(Integer32):
    """Custom type sonusMgsgCktAdminState based on Integer32"""
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


_SonusMgsgCktAdminState_Type.__name__ = "Integer32"
_SonusMgsgCktAdminState_Object = MibTableColumn
sonusMgsgCktAdminState = _SonusMgsgCktAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 9),
    _SonusMgsgCktAdminState_Type()
)
sonusMgsgCktAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgCktAdminState.setStatus("current")
_SonusMgsgCktProfileName_Type = SonusNameReference
_SonusMgsgCktProfileName_Object = MibTableColumn
sonusMgsgCktProfileName = _SonusMgsgCktProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 10),
    _SonusMgsgCktProfileName_Type()
)
sonusMgsgCktProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgCktProfileName.setStatus("current")


class _SonusMgsgCktType_Type(Integer32):
    """Custom type sonusMgsgCktType based on Integer32"""
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
        *(("data", 1),
          ("dchan-ntwk", 3),
          ("dchan-user", 2))
    )


_SonusMgsgCktType_Type.__name__ = "Integer32"
_SonusMgsgCktType_Object = MibTableColumn
sonusMgsgCktType = _SonusMgsgCktType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 11),
    _SonusMgsgCktType_Type()
)
sonusMgsgCktType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgCktType.setStatus("current")


class _SonusMgsgCktDchanSwitchType_Type(Integer32):
    """Custom type sonusMgsgCktDchanSwitchType based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("dms", 4),
          ("itu", 7),
          ("kdd", 5),
          ("net5", 8),
          ("ni2", 1),
          ("ntt", 6),
          ("sw1tr6", 9),
          ("sw4ess", 2),
          ("sw5esscust", 3),
          ("ts014", 10),
          ("vn", 11))
    )


_SonusMgsgCktDchanSwitchType_Type.__name__ = "Integer32"
_SonusMgsgCktDchanSwitchType_Object = MibTableColumn
sonusMgsgCktDchanSwitchType = _SonusMgsgCktDchanSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 12),
    _SonusMgsgCktDchanSwitchType_Type()
)
sonusMgsgCktDchanSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgCktDchanSwitchType.setStatus("current")
_SonusMgsgCktRowStatus_Type = RowStatus
_SonusMgsgCktRowStatus_Object = MibTableColumn
sonusMgsgCktRowStatus = _SonusMgsgCktRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 3, 1, 13),
    _SonusMgsgCktRowStatus_Type()
)
sonusMgsgCktRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusMgsgCktRowStatus.setStatus("current")
_SonusMgsgCktStatTable_Object = MibTable
sonusMgsgCktStatTable = _SonusMgsgCktStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4)
)
if mibBuilder.loadTexts:
    sonusMgsgCktStatTable.setStatus("current")
_SonusMgsgCktStatEntry_Object = MibTableRow
sonusMgsgCktStatEntry = _SonusMgsgCktStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1)
)
sonusMgsgCktStatEntry.setIndexNames(
    (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktStatShelfIndex"),
    (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktStatSlotIndex"),
    (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktStatDs1Index"),
    (0, "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB", "sonusMgsgCktStatDs0Index"),
)
if mibBuilder.loadTexts:
    sonusMgsgCktStatEntry.setStatus("current")
_SonusMgsgCktStatShelfIndex_Type = Integer32
_SonusMgsgCktStatShelfIndex_Object = MibTableColumn
sonusMgsgCktStatShelfIndex = _SonusMgsgCktStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 1),
    _SonusMgsgCktStatShelfIndex_Type()
)
sonusMgsgCktStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktStatShelfIndex.setStatus("current")
_SonusMgsgCktStatSlotIndex_Type = Integer32
_SonusMgsgCktStatSlotIndex_Object = MibTableColumn
sonusMgsgCktStatSlotIndex = _SonusMgsgCktStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 2),
    _SonusMgsgCktStatSlotIndex_Type()
)
sonusMgsgCktStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktStatSlotIndex.setStatus("current")
_SonusMgsgCktStatDs1Index_Type = Integer32
_SonusMgsgCktStatDs1Index_Object = MibTableColumn
sonusMgsgCktStatDs1Index = _SonusMgsgCktStatDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 3),
    _SonusMgsgCktStatDs1Index_Type()
)
sonusMgsgCktStatDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktStatDs1Index.setStatus("current")
_SonusMgsgCktStatDs0Index_Type = Integer32
_SonusMgsgCktStatDs0Index_Object = MibTableColumn
sonusMgsgCktStatDs0Index = _SonusMgsgCktStatDs0Index_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 4),
    _SonusMgsgCktStatDs0Index_Type()
)
sonusMgsgCktStatDs0Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktStatDs0Index.setStatus("current")
_SonusMgsgCktStatSrvGrpName_Type = SonusNameReference
_SonusMgsgCktStatSrvGrpName_Object = MibTableColumn
sonusMgsgCktStatSrvGrpName = _SonusMgsgCktStatSrvGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 5),
    _SonusMgsgCktStatSrvGrpName_Type()
)
sonusMgsgCktStatSrvGrpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktStatSrvGrpName.setStatus("current")


class _SonusMgsgCktStatMgcState_Type(Integer32):
    """Custom type sonusMgsgCktStatMgcState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 4),
          ("connected", 8),
          ("disabled", 9),
          ("dualToneLoop", 10),
          ("idle", 6),
          ("inUse", 7),
          ("loopback", 5),
          ("maintenance", 3),
          ("notPresent", 1),
          ("outOfService", 2))
    )


_SonusMgsgCktStatMgcState_Type.__name__ = "Integer32"
_SonusMgsgCktStatMgcState_Object = MibTableColumn
sonusMgsgCktStatMgcState = _SonusMgsgCktStatMgcState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 6),
    _SonusMgsgCktStatMgcState_Type()
)
sonusMgsgCktStatMgcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktStatMgcState.setStatus("current")


class _SonusMgsgCktStatLocalHwState_Type(Integer32):
    """Custom type sonusMgsgCktStatLocalHwState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("unavailable", 2))
    )


_SonusMgsgCktStatLocalHwState_Type.__name__ = "Integer32"
_SonusMgsgCktStatLocalHwState_Object = MibTableColumn
sonusMgsgCktStatLocalHwState = _SonusMgsgCktStatLocalHwState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 7),
    _SonusMgsgCktStatLocalHwState_Type()
)
sonusMgsgCktStatLocalHwState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktStatLocalHwState.setStatus("current")
_SonusMgsgCktStatDryupInProgress_Type = SonusBoolean
_SonusMgsgCktStatDryupInProgress_Object = MibTableColumn
sonusMgsgCktStatDryupInProgress = _SonusMgsgCktStatDryupInProgress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 1, 4, 1, 8),
    _SonusMgsgCktStatDryupInProgress_Type()
)
sonusMgsgCktStatDryupInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusMgsgCktStatDryupInProgress.setStatus("current")
_SonusMediaGatewayServiceGroupMIBNotifications_ObjectIdentity = ObjectIdentity
sonusMediaGatewayServiceGroupMIBNotifications = _SonusMediaGatewayServiceGroupMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 2)
)
_SonusMediaGatewayServiceGroupMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusMediaGatewayServiceGroupMIBNotificationsPrefix = _SonusMediaGatewayServiceGroupMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 2, 0)
)
_SonusMediaGatewayServiceGroupMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusMediaGatewayServiceGroupMIBNotificationsObjects = _SonusMediaGatewayServiceGroupMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 6, 3, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-MEDIA-GATEWAY-SERVICE-GROUP-MIB",
    **{"sonusMediaGatewayServiceGroupMIB": sonusMediaGatewayServiceGroupMIB,
       "sonusMediaGatewayServiceGroupMIBObjects": sonusMediaGatewayServiceGroupMIBObjects,
       "sonusMgsgServiceGrp": sonusMgsgServiceGrp,
       "sonusMgsgServiceGrpNextIndex": sonusMgsgServiceGrpNextIndex,
       "sonusMgsgServiceGrpTable": sonusMgsgServiceGrpTable,
       "sonusMgsgServiceGrpEntry": sonusMgsgServiceGrpEntry,
       "sonusMgsgServiceGrpListIndex": sonusMgsgServiceGrpListIndex,
       "sonusMgsgServiceGrpName": sonusMgsgServiceGrpName,
       "sonusMgsgServiceGrpAdminState": sonusMgsgServiceGrpAdminState,
       "sonusMgsgServiceGrpControllerName": sonusMgsgServiceGrpControllerName,
       "sonusMgsgServiceGrpType": sonusMgsgServiceGrpType,
       "sonusMgsgServiceGrpMode": sonusMgsgServiceGrpMode,
       "sonusMgsgServiceGrpAction": sonusMgsgServiceGrpAction,
       "sonusMgsgServiceGrpTimeout": sonusMgsgServiceGrpTimeout,
       "sonusMgsgServiceGrpRowStatus": sonusMgsgServiceGrpRowStatus,
       "sonusMgsgServiceGrpStatTable": sonusMgsgServiceGrpStatTable,
       "sonusMgsgServiceGrpStatEntry": sonusMgsgServiceGrpStatEntry,
       "sonusMgsgServiceGrpStatListIndex": sonusMgsgServiceGrpStatListIndex,
       "sonusMgsgServiceGrpStatName": sonusMgsgServiceGrpStatName,
       "sonusMgsgServiceGrpStatStatus": sonusMgsgServiceGrpStatStatus,
       "sonusMgsgCktTable": sonusMgsgCktTable,
       "sonusMgsgCktEntry": sonusMgsgCktEntry,
       "sonusMgsgCktShelfIndex": sonusMgsgCktShelfIndex,
       "sonusMgsgCktSlotIndex": sonusMgsgCktSlotIndex,
       "sonusMgsgCktDs1Index": sonusMgsgCktDs1Index,
       "sonusMgsgCktDs0Index": sonusMgsgCktDs0Index,
       "sonusMgsgCktSrvGrpName": sonusMgsgCktSrvGrpName,
       "sonusMgsgCktMode": sonusMgsgCktMode,
       "sonusMgsgCktAction": sonusMgsgCktAction,
       "sonusMgsgCktTimeout": sonusMgsgCktTimeout,
       "sonusMgsgCktAdminState": sonusMgsgCktAdminState,
       "sonusMgsgCktProfileName": sonusMgsgCktProfileName,
       "sonusMgsgCktType": sonusMgsgCktType,
       "sonusMgsgCktDchanSwitchType": sonusMgsgCktDchanSwitchType,
       "sonusMgsgCktRowStatus": sonusMgsgCktRowStatus,
       "sonusMgsgCktStatTable": sonusMgsgCktStatTable,
       "sonusMgsgCktStatEntry": sonusMgsgCktStatEntry,
       "sonusMgsgCktStatShelfIndex": sonusMgsgCktStatShelfIndex,
       "sonusMgsgCktStatSlotIndex": sonusMgsgCktStatSlotIndex,
       "sonusMgsgCktStatDs1Index": sonusMgsgCktStatDs1Index,
       "sonusMgsgCktStatDs0Index": sonusMgsgCktStatDs0Index,
       "sonusMgsgCktStatSrvGrpName": sonusMgsgCktStatSrvGrpName,
       "sonusMgsgCktStatMgcState": sonusMgsgCktStatMgcState,
       "sonusMgsgCktStatLocalHwState": sonusMgsgCktStatLocalHwState,
       "sonusMgsgCktStatDryupInProgress": sonusMgsgCktStatDryupInProgress,
       "sonusMediaGatewayServiceGroupMIBNotifications": sonusMediaGatewayServiceGroupMIBNotifications,
       "sonusMediaGatewayServiceGroupMIBNotificationsPrefix": sonusMediaGatewayServiceGroupMIBNotificationsPrefix,
       "sonusMediaGatewayServiceGroupMIBNotificationsObjects": sonusMediaGatewayServiceGroupMIBNotificationsObjects}
)
