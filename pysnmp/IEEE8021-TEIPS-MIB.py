# SNMP MIB module (IEEE8021-TEIPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IEEE8021-TEIPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:08:44 2024
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

(ieee8021BridgeBaseComponentId,) = mibBuilder.importSymbols(
    "IEEE8021-BRIDGE-MIB",
    "ieee8021BridgeBaseComponentId")

(IEEE8021BridgePortNumber,
 IEEE8021PbbTeTSidId,
 IEEE8021TeipsIpgConfigActiveRequests,
 IEEE8021TeipsIpgConfigAdmin,
 IEEE8021TeipsIpgid,
 ieee802dot1mibs) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber",
    "IEEE8021PbbTeTSidId",
    "IEEE8021TeipsIpgConfigActiveRequests",
    "IEEE8021TeipsIpgConfigAdmin",
    "IEEE8021TeipsIpgid",
    "ieee802dot1mibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ieee8021TeipsMib = ModuleIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24)
)
ieee8021TeipsMib.setRevisions(
        ("2011-08-17 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ieee8021TeipsNotifications_ObjectIdentity = ObjectIdentity
ieee8021TeipsNotifications = _Ieee8021TeipsNotifications_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 0)
)
_Ieee8021TeipsObjects_ObjectIdentity = ObjectIdentity
ieee8021TeipsObjects = _Ieee8021TeipsObjects_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 1)
)
_Ieee8021TeipsIpgTable_Object = MibTable
ieee8021TeipsIpgTable = _Ieee8021TeipsIpgTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021TeipsIpgTable.setStatus("current")
_Ieee8021TeipsIpgEntry_Object = MibTableRow
ieee8021TeipsIpgEntry = _Ieee8021TeipsIpgEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1)
)
ieee8021TeipsIpgEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"),
)
if mibBuilder.loadTexts:
    ieee8021TeipsIpgEntry.setStatus("current")
_Ieee8021TeipsIpgid_Type = IEEE8021TeipsIpgid
_Ieee8021TeipsIpgid_Object = MibTableColumn
ieee8021TeipsIpgid = _Ieee8021TeipsIpgid_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 1),
    _Ieee8021TeipsIpgid_Type()
)
ieee8021TeipsIpgid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgid.setStatus("current")
_Ieee8021TeipsIpgWorkingMA_Type = Unsigned32
_Ieee8021TeipsIpgWorkingMA_Object = MibTableColumn
ieee8021TeipsIpgWorkingMA = _Ieee8021TeipsIpgWorkingMA_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 2),
    _Ieee8021TeipsIpgWorkingMA_Type()
)
ieee8021TeipsIpgWorkingMA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgWorkingMA.setStatus("current")
_Ieee8021TeipsIpgProtectionMA_Type = Unsigned32
_Ieee8021TeipsIpgProtectionMA_Object = MibTableColumn
ieee8021TeipsIpgProtectionMA = _Ieee8021TeipsIpgProtectionMA_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 3),
    _Ieee8021TeipsIpgProtectionMA_Type()
)
ieee8021TeipsIpgProtectionMA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgProtectionMA.setStatus("current")
_Ieee8021TeipsIpgWorkingPortNumber_Type = IEEE8021BridgePortNumber
_Ieee8021TeipsIpgWorkingPortNumber_Object = MibTableColumn
ieee8021TeipsIpgWorkingPortNumber = _Ieee8021TeipsIpgWorkingPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 4),
    _Ieee8021TeipsIpgWorkingPortNumber_Type()
)
ieee8021TeipsIpgWorkingPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgWorkingPortNumber.setStatus("current")
_Ieee8021TeipsIpgProtectionPortNumber_Type = IEEE8021BridgePortNumber
_Ieee8021TeipsIpgProtectionPortNumber_Object = MibTableColumn
ieee8021TeipsIpgProtectionPortNumber = _Ieee8021TeipsIpgProtectionPortNumber_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 5),
    _Ieee8021TeipsIpgProtectionPortNumber_Type()
)
ieee8021TeipsIpgProtectionPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgProtectionPortNumber.setStatus("current")


class _Ieee8021TeipsIpgStorageType_Type(StorageType):
    """Custom type ieee8021TeipsIpgStorageType based on StorageType"""


_Ieee8021TeipsIpgStorageType_Object = MibTableColumn
ieee8021TeipsIpgStorageType = _Ieee8021TeipsIpgStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 6),
    _Ieee8021TeipsIpgStorageType_Type()
)
ieee8021TeipsIpgStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgStorageType.setStatus("current")
_Ieee8021TeipsIpgRowStatus_Type = RowStatus
_Ieee8021TeipsIpgRowStatus_Object = MibTableColumn
ieee8021TeipsIpgRowStatus = _Ieee8021TeipsIpgRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 1, 1, 7),
    _Ieee8021TeipsIpgRowStatus_Type()
)
ieee8021TeipsIpgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgRowStatus.setStatus("current")
_Ieee8021TeipsTesiTable_Object = MibTable
ieee8021TeipsTesiTable = _Ieee8021TeipsTesiTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2)
)
if mibBuilder.loadTexts:
    ieee8021TeipsTesiTable.setStatus("current")
_Ieee8021TeipsTesiEntry_Object = MibTableRow
ieee8021TeipsTesiEntry = _Ieee8021TeipsTesiEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1)
)
ieee8021TeipsTesiEntry.setIndexNames(
    (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"),
    (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiIndex"),
)
if mibBuilder.loadTexts:
    ieee8021TeipsTesiEntry.setStatus("current")


class _Ieee8021TeipsTesiIndex_Type(Unsigned32):
    """Custom type ieee8021TeipsTesiIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Ieee8021TeipsTesiIndex_Type.__name__ = "Unsigned32"
_Ieee8021TeipsTesiIndex_Object = MibTableColumn
ieee8021TeipsTesiIndex = _Ieee8021TeipsTesiIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 1),
    _Ieee8021TeipsTesiIndex_Type()
)
ieee8021TeipsTesiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021TeipsTesiIndex.setStatus("current")
_Ieee8021TeipsTesiId_Type = IEEE8021PbbTeTSidId
_Ieee8021TeipsTesiId_Object = MibTableColumn
ieee8021TeipsTesiId = _Ieee8021TeipsTesiId_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 2),
    _Ieee8021TeipsTesiId_Type()
)
ieee8021TeipsTesiId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsTesiId.setStatus("current")


class _Ieee8021TeipsTesiStorageType_Type(StorageType):
    """Custom type ieee8021TeipsTesiStorageType based on StorageType"""


_Ieee8021TeipsTesiStorageType_Object = MibTableColumn
ieee8021TeipsTesiStorageType = _Ieee8021TeipsTesiStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 3),
    _Ieee8021TeipsTesiStorageType_Type()
)
ieee8021TeipsTesiStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsTesiStorageType.setStatus("current")
_Ieee8021TeipsTesiRowStatus_Type = RowStatus
_Ieee8021TeipsTesiRowStatus_Object = MibTableColumn
ieee8021TeipsTesiRowStatus = _Ieee8021TeipsTesiRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 2, 1, 4),
    _Ieee8021TeipsTesiRowStatus_Type()
)
ieee8021TeipsTesiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsTesiRowStatus.setStatus("current")
_Ieee8021TeipsCandidatePsTable_Object = MibTable
ieee8021TeipsCandidatePsTable = _Ieee8021TeipsCandidatePsTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3)
)
if mibBuilder.loadTexts:
    ieee8021TeipsCandidatePsTable.setStatus("current")
_Ieee8021TeipsCandidatePsEntry_Object = MibTableRow
ieee8021TeipsCandidatePsEntry = _Ieee8021TeipsCandidatePsEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1)
)
ieee8021TeipsCandidatePsEntry.setIndexNames(
    (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"),
    (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsIndex"),
)
if mibBuilder.loadTexts:
    ieee8021TeipsCandidatePsEntry.setStatus("current")


class _Ieee8021TeipsCandidatePsIndex_Type(Unsigned32):
    """Custom type ieee8021TeipsCandidatePsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_Ieee8021TeipsCandidatePsIndex_Type.__name__ = "Unsigned32"
_Ieee8021TeipsCandidatePsIndex_Object = MibTableColumn
ieee8021TeipsCandidatePsIndex = _Ieee8021TeipsCandidatePsIndex_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 1),
    _Ieee8021TeipsCandidatePsIndex_Type()
)
ieee8021TeipsCandidatePsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ieee8021TeipsCandidatePsIndex.setStatus("current")
_Ieee8021TeipsCandidatePsMA_Type = Unsigned32
_Ieee8021TeipsCandidatePsMA_Object = MibTableColumn
ieee8021TeipsCandidatePsMA = _Ieee8021TeipsCandidatePsMA_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 2),
    _Ieee8021TeipsCandidatePsMA_Type()
)
ieee8021TeipsCandidatePsMA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsCandidatePsMA.setStatus("current")
_Ieee8021TeipsCandidatePsPort_Type = IEEE8021BridgePortNumber
_Ieee8021TeipsCandidatePsPort_Object = MibTableColumn
ieee8021TeipsCandidatePsPort = _Ieee8021TeipsCandidatePsPort_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 3),
    _Ieee8021TeipsCandidatePsPort_Type()
)
ieee8021TeipsCandidatePsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsCandidatePsPort.setStatus("current")
_Ieee8021TeipsCandidatePsOper_Type = TruthValue
_Ieee8021TeipsCandidatePsOper_Object = MibTableColumn
ieee8021TeipsCandidatePsOper = _Ieee8021TeipsCandidatePsOper_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 4),
    _Ieee8021TeipsCandidatePsOper_Type()
)
ieee8021TeipsCandidatePsOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsCandidatePsOper.setStatus("current")


class _Ieee8021TeipsCandidatePsStorageType_Type(StorageType):
    """Custom type ieee8021TeipsCandidatePsStorageType based on StorageType"""


_Ieee8021TeipsCandidatePsStorageType_Object = MibTableColumn
ieee8021TeipsCandidatePsStorageType = _Ieee8021TeipsCandidatePsStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 5),
    _Ieee8021TeipsCandidatePsStorageType_Type()
)
ieee8021TeipsCandidatePsStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsCandidatePsStorageType.setStatus("current")
_Ieee8021TeipsCandidatePsRowStatus_Type = RowStatus
_Ieee8021TeipsCandidatePsRowStatus_Object = MibTableColumn
ieee8021TeipsCandidatePsRowStatus = _Ieee8021TeipsCandidatePsRowStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 3, 1, 6),
    _Ieee8021TeipsCandidatePsRowStatus_Type()
)
ieee8021TeipsCandidatePsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsCandidatePsRowStatus.setStatus("current")
_Ieee8021TeipsIpgConfigTable_Object = MibTable
ieee8021TeipsIpgConfigTable = _Ieee8021TeipsIpgConfigTable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4)
)
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigTable.setStatus("current")
_Ieee8021TeipsIpgConfigEntry_Object = MibTableRow
ieee8021TeipsIpgConfigEntry = _Ieee8021TeipsIpgConfigEntry_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1)
)
ieee8021TeipsIpgConfigEntry.setIndexNames(
    (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"),
    (0, "IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgid"),
)
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigEntry.setStatus("current")


class _Ieee8021TeipsIpgConfigState_Type(Integer32):
    """Custom type ieee8021TeipsIpgConfigState based on Integer32"""
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
        *(("protAdmin", 4),
          ("protectionSegment", 2),
          ("waitToRestore", 3),
          ("workingSegment", 1))
    )


_Ieee8021TeipsIpgConfigState_Type.__name__ = "Integer32"
_Ieee8021TeipsIpgConfigState_Object = MibTableColumn
ieee8021TeipsIpgConfigState = _Ieee8021TeipsIpgConfigState_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 1),
    _Ieee8021TeipsIpgConfigState_Type()
)
ieee8021TeipsIpgConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigState.setStatus("current")
_Ieee8021TeipsIpgConfigCommandStatus_Type = IEEE8021TeipsIpgConfigAdmin
_Ieee8021TeipsIpgConfigCommandStatus_Object = MibTableColumn
ieee8021TeipsIpgConfigCommandStatus = _Ieee8021TeipsIpgConfigCommandStatus_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 2),
    _Ieee8021TeipsIpgConfigCommandStatus_Type()
)
ieee8021TeipsIpgConfigCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigCommandStatus.setStatus("current")
_Ieee8021TeipsIpgConfigCommandLast_Type = IEEE8021TeipsIpgConfigAdmin
_Ieee8021TeipsIpgConfigCommandLast_Object = MibTableColumn
ieee8021TeipsIpgConfigCommandLast = _Ieee8021TeipsIpgConfigCommandLast_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 3),
    _Ieee8021TeipsIpgConfigCommandLast_Type()
)
ieee8021TeipsIpgConfigCommandLast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigCommandLast.setStatus("current")


class _Ieee8021TeipsIpgConfigCommandAdmin_Type(IEEE8021TeipsIpgConfigAdmin):
    """Custom type ieee8021TeipsIpgConfigCommandAdmin based on IEEE8021TeipsIpgConfigAdmin"""


_Ieee8021TeipsIpgConfigCommandAdmin_Object = MibTableColumn
ieee8021TeipsIpgConfigCommandAdmin = _Ieee8021TeipsIpgConfigCommandAdmin_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 4),
    _Ieee8021TeipsIpgConfigCommandAdmin_Type()
)
ieee8021TeipsIpgConfigCommandAdmin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigCommandAdmin.setStatus("current")
_Ieee8021TeipsIpgConfigActiveRequests_Type = IEEE8021TeipsIpgConfigActiveRequests
_Ieee8021TeipsIpgConfigActiveRequests_Object = MibTableColumn
ieee8021TeipsIpgConfigActiveRequests = _Ieee8021TeipsIpgConfigActiveRequests_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 5),
    _Ieee8021TeipsIpgConfigActiveRequests_Type()
)
ieee8021TeipsIpgConfigActiveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigActiveRequests.setStatus("current")


class _Ieee8021TeipsIpgConfigWTR_Type(Unsigned32):
    """Custom type ieee8021TeipsIpgConfigWTR based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 12),
    )


_Ieee8021TeipsIpgConfigWTR_Type.__name__ = "Unsigned32"
_Ieee8021TeipsIpgConfigWTR_Object = MibTableColumn
ieee8021TeipsIpgConfigWTR = _Ieee8021TeipsIpgConfigWTR_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 6),
    _Ieee8021TeipsIpgConfigWTR_Type()
)
ieee8021TeipsIpgConfigWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigWTR.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigWTR.setUnits("minutes")


class _Ieee8021TeipsIpgConfigHoldOff_Type(Unsigned32):
    """Custom type ieee8021TeipsIpgConfigHoldOff based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Ieee8021TeipsIpgConfigHoldOff_Type.__name__ = "Unsigned32"
_Ieee8021TeipsIpgConfigHoldOff_Object = MibTableColumn
ieee8021TeipsIpgConfigHoldOff = _Ieee8021TeipsIpgConfigHoldOff_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 7),
    _Ieee8021TeipsIpgConfigHoldOff_Type()
)
ieee8021TeipsIpgConfigHoldOff.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigHoldOff.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigHoldOff.setUnits("deciseconds")


class _Ieee8021TeipsIpgM1ConfigState_Type(Integer32):
    """Custom type ieee8021TeipsIpgM1ConfigState based on Integer32"""
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
        *(("assignNewPs", 4),
          ("psAssigned", 1),
          ("revertToBetterPs", 5),
          ("segmentFailed", 3),
          ("segmentOk", 2))
    )


_Ieee8021TeipsIpgM1ConfigState_Type.__name__ = "Integer32"
_Ieee8021TeipsIpgM1ConfigState_Object = MibTableColumn
ieee8021TeipsIpgM1ConfigState = _Ieee8021TeipsIpgM1ConfigState_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 8),
    _Ieee8021TeipsIpgM1ConfigState_Type()
)
ieee8021TeipsIpgM1ConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgM1ConfigState.setStatus("current")


class _Ieee8021TeipsIpgConfigMWTR_Type(Unsigned32):
    """Custom type ieee8021TeipsIpgConfigMWTR based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 12),
    )


_Ieee8021TeipsIpgConfigMWTR_Type.__name__ = "Unsigned32"
_Ieee8021TeipsIpgConfigMWTR_Object = MibTableColumn
ieee8021TeipsIpgConfigMWTR = _Ieee8021TeipsIpgConfigMWTR_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 9),
    _Ieee8021TeipsIpgConfigMWTR_Type()
)
ieee8021TeipsIpgConfigMWTR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigMWTR.setStatus("current")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigMWTR.setUnits("minutes")


class _Ieee8021TeipsIpgConfigNotifyEnable_Type(TruthValue):
    """Custom type ieee8021TeipsIpgConfigNotifyEnable based on TruthValue"""


_Ieee8021TeipsIpgConfigNotifyEnable_Object = MibTableColumn
ieee8021TeipsIpgConfigNotifyEnable = _Ieee8021TeipsIpgConfigNotifyEnable_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 10),
    _Ieee8021TeipsIpgConfigNotifyEnable_Type()
)
ieee8021TeipsIpgConfigNotifyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigNotifyEnable.setStatus("current")


class _Ieee8021TeipsIpgConfigStorageType_Type(StorageType):
    """Custom type ieee8021TeipsIpgConfigStorageType based on StorageType"""


_Ieee8021TeipsIpgConfigStorageType_Object = MibTableColumn
ieee8021TeipsIpgConfigStorageType = _Ieee8021TeipsIpgConfigStorageType_Object(
    (1, 3, 111, 2, 802, 1, 1, 24, 1, 4, 1, 11),
    _Ieee8021TeipsIpgConfigStorageType_Type()
)
ieee8021TeipsIpgConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigStorageType.setStatus("current")
_Ieee8021TeipsConformance_ObjectIdentity = ObjectIdentity
ieee8021TeipsConformance = _Ieee8021TeipsConformance_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 2)
)
_Ieee8021TeipsCompliances_ObjectIdentity = ObjectIdentity
ieee8021TeipsCompliances = _Ieee8021TeipsCompliances_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1)
)
_Ieee8021TeipsGroups_ObjectIdentity = ObjectIdentity
ieee8021TeipsGroups = _Ieee8021TeipsGroups_ObjectIdentity(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2)
)

# Managed Objects groups

ieee8021TeipsIpgGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 1)
)
ieee8021TeipsIpgGroup.setObjects(
      *(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgWorkingMA"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgProtectionMA"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgWorkingPortNumber"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgProtectionPortNumber"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgStorageType"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsIpgGroup.setStatus("current")

ieee8021TeipsCandidatePsGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 2)
)
ieee8021TeipsCandidatePsGroup.setObjects(
      *(("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsMA"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsPort"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsOper"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsStorageType"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsCandidatePsRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsCandidatePsGroup.setStatus("current")

ieee8021TeipsIpgTesiGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 3)
)
ieee8021TeipsIpgTesiGroup.setObjects(
      *(("IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiId"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiStorageType"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsTesiRowStatus"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsIpgTesiGroup.setStatus("current")

ieee8021TeipsIpgConfigManGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 4)
)
ieee8021TeipsIpgConfigManGroup.setObjects(
      *(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigState"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandStatus"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandLast"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandAdmin"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigActiveRequests"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigNotifyEnable"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigStorageType"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigManGroup.setStatus("current")

ieee8021TeipsIpgConfigOptGroup = ObjectGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 5)
)
ieee8021TeipsIpgConfigOptGroup.setObjects(
      *(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigWTR"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigMWTR"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgM1ConfigState"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigHoldOff"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsIpgConfigOptGroup.setStatus("current")


# Notification objects

ieee8021TeipsIpgAdminFailure = NotificationType(
    (1, 3, 111, 2, 802, 1, 1, 24, 0, 1)
)
ieee8021TeipsIpgAdminFailure.setObjects(
      *(("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigState"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandStatus"),
        ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgConfigCommandLast"))
)
if mibBuilder.loadTexts:
    ieee8021TeipsIpgAdminFailure.setStatus(
        "current"
    )


# Notifications groups

ieee8021TeipsNotificationsGroup = NotificationGroup(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 2, 6)
)
ieee8021TeipsNotificationsGroup.setObjects(
    ("IEEE8021-TEIPS-MIB", "ieee8021TeipsIpgAdminFailure")
)
if mibBuilder.loadTexts:
    ieee8021TeipsNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ieee8021TeipsCompliance = ModuleCompliance(
    (1, 3, 111, 2, 802, 1, 1, 24, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ieee8021TeipsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IEEE8021-TEIPS-MIB",
    **{"ieee8021TeipsMib": ieee8021TeipsMib,
       "ieee8021TeipsNotifications": ieee8021TeipsNotifications,
       "ieee8021TeipsIpgAdminFailure": ieee8021TeipsIpgAdminFailure,
       "ieee8021TeipsObjects": ieee8021TeipsObjects,
       "ieee8021TeipsIpgTable": ieee8021TeipsIpgTable,
       "ieee8021TeipsIpgEntry": ieee8021TeipsIpgEntry,
       "ieee8021TeipsIpgid": ieee8021TeipsIpgid,
       "ieee8021TeipsIpgWorkingMA": ieee8021TeipsIpgWorkingMA,
       "ieee8021TeipsIpgProtectionMA": ieee8021TeipsIpgProtectionMA,
       "ieee8021TeipsIpgWorkingPortNumber": ieee8021TeipsIpgWorkingPortNumber,
       "ieee8021TeipsIpgProtectionPortNumber": ieee8021TeipsIpgProtectionPortNumber,
       "ieee8021TeipsIpgStorageType": ieee8021TeipsIpgStorageType,
       "ieee8021TeipsIpgRowStatus": ieee8021TeipsIpgRowStatus,
       "ieee8021TeipsTesiTable": ieee8021TeipsTesiTable,
       "ieee8021TeipsTesiEntry": ieee8021TeipsTesiEntry,
       "ieee8021TeipsTesiIndex": ieee8021TeipsTesiIndex,
       "ieee8021TeipsTesiId": ieee8021TeipsTesiId,
       "ieee8021TeipsTesiStorageType": ieee8021TeipsTesiStorageType,
       "ieee8021TeipsTesiRowStatus": ieee8021TeipsTesiRowStatus,
       "ieee8021TeipsCandidatePsTable": ieee8021TeipsCandidatePsTable,
       "ieee8021TeipsCandidatePsEntry": ieee8021TeipsCandidatePsEntry,
       "ieee8021TeipsCandidatePsIndex": ieee8021TeipsCandidatePsIndex,
       "ieee8021TeipsCandidatePsMA": ieee8021TeipsCandidatePsMA,
       "ieee8021TeipsCandidatePsPort": ieee8021TeipsCandidatePsPort,
       "ieee8021TeipsCandidatePsOper": ieee8021TeipsCandidatePsOper,
       "ieee8021TeipsCandidatePsStorageType": ieee8021TeipsCandidatePsStorageType,
       "ieee8021TeipsCandidatePsRowStatus": ieee8021TeipsCandidatePsRowStatus,
       "ieee8021TeipsIpgConfigTable": ieee8021TeipsIpgConfigTable,
       "ieee8021TeipsIpgConfigEntry": ieee8021TeipsIpgConfigEntry,
       "ieee8021TeipsIpgConfigState": ieee8021TeipsIpgConfigState,
       "ieee8021TeipsIpgConfigCommandStatus": ieee8021TeipsIpgConfigCommandStatus,
       "ieee8021TeipsIpgConfigCommandLast": ieee8021TeipsIpgConfigCommandLast,
       "ieee8021TeipsIpgConfigCommandAdmin": ieee8021TeipsIpgConfigCommandAdmin,
       "ieee8021TeipsIpgConfigActiveRequests": ieee8021TeipsIpgConfigActiveRequests,
       "ieee8021TeipsIpgConfigWTR": ieee8021TeipsIpgConfigWTR,
       "ieee8021TeipsIpgConfigHoldOff": ieee8021TeipsIpgConfigHoldOff,
       "ieee8021TeipsIpgM1ConfigState": ieee8021TeipsIpgM1ConfigState,
       "ieee8021TeipsIpgConfigMWTR": ieee8021TeipsIpgConfigMWTR,
       "ieee8021TeipsIpgConfigNotifyEnable": ieee8021TeipsIpgConfigNotifyEnable,
       "ieee8021TeipsIpgConfigStorageType": ieee8021TeipsIpgConfigStorageType,
       "ieee8021TeipsConformance": ieee8021TeipsConformance,
       "ieee8021TeipsCompliances": ieee8021TeipsCompliances,
       "ieee8021TeipsCompliance": ieee8021TeipsCompliance,
       "ieee8021TeipsGroups": ieee8021TeipsGroups,
       "ieee8021TeipsIpgGroup": ieee8021TeipsIpgGroup,
       "ieee8021TeipsCandidatePsGroup": ieee8021TeipsCandidatePsGroup,
       "ieee8021TeipsIpgTesiGroup": ieee8021TeipsIpgTesiGroup,
       "ieee8021TeipsIpgConfigManGroup": ieee8021TeipsIpgConfigManGroup,
       "ieee8021TeipsIpgConfigOptGroup": ieee8021TeipsIpgConfigOptGroup,
       "ieee8021TeipsNotificationsGroup": ieee8021TeipsNotificationsGroup}
)
