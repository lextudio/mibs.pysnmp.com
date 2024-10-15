# SNMP MIB module (SONUS-NODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-NODE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:03 2024
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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(sonusEventClass,
 sonusEventDescription,
 sonusEventLevel,
 sonusPortIndex,
 sonusShelfIndex,
 sonusSlotIndex) = mibBuilder.importSymbols(
    "SONUS-COMMON-MIB",
    "sonusEventClass",
    "sonusEventDescription",
    "sonusEventLevel",
    "sonusPortIndex",
    "sonusShelfIndex",
    "sonusSlotIndex")

(sonusSystemMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusSystemMIBs")

(AdapterTypeID,
 HwTypeID,
 ServerFunctionType,
 ServerTypeID,
 SonusAccessLevel,
 SonusAdminAction,
 SonusAdminState,
 SonusName,
 SonusServiceState,
 SonusSoftwareVersion) = mibBuilder.importSymbols(
    "SONUS-TC",
    "AdapterTypeID",
    "HwTypeID",
    "ServerFunctionType",
    "ServerTypeID",
    "SonusAccessLevel",
    "SonusAdminAction",
    "SonusAdminState",
    "SonusName",
    "SonusServiceState",
    "SonusSoftwareVersion")


# MODULE-IDENTITY

sonusNodeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusNodeMIBObjects_ObjectIdentity = ObjectIdentity
sonusNodeMIBObjects = _SonusNodeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1)
)
_SonusNode_ObjectIdentity = ObjectIdentity
sonusNode = _SonusNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1)
)
_SonusNodeAdmnObjects_ObjectIdentity = ObjectIdentity
sonusNodeAdmnObjects = _SonusNodeAdmnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 1)
)


class _SonusNodeAdmnShelves_Type(Integer32):
    """Custom type sonusNodeAdmnShelves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNodeAdmnShelves_Type.__name__ = "Integer32"
_SonusNodeAdmnShelves_Object = MibScalar
sonusNodeAdmnShelves = _SonusNodeAdmnShelves_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 1, 1),
    _SonusNodeAdmnShelves_Type()
)
sonusNodeAdmnShelves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeAdmnShelves.setStatus("current")
_SonusNodeAdmnTelnetLogin_Type = SonusAdminState
_SonusNodeAdmnTelnetLogin_Object = MibScalar
sonusNodeAdmnTelnetLogin = _SonusNodeAdmnTelnetLogin_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 1, 2),
    _SonusNodeAdmnTelnetLogin_Type()
)
sonusNodeAdmnTelnetLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeAdmnTelnetLogin.setStatus("current")
_SonusNodeStatusObjects_ObjectIdentity = ObjectIdentity
sonusNodeStatusObjects = _SonusNodeStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 2)
)


class _SonusNodeStatShelvesPresent_Type(Integer32):
    """Custom type sonusNodeStatShelvesPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNodeStatShelvesPresent_Type.__name__ = "Integer32"
_SonusNodeStatShelvesPresent_Object = MibScalar
sonusNodeStatShelvesPresent = _SonusNodeStatShelvesPresent_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 2, 1),
    _SonusNodeStatShelvesPresent_Type()
)
sonusNodeStatShelvesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeStatShelvesPresent.setStatus("current")
_SonusNodeStatNextIfIndex_Type = Integer32
_SonusNodeStatNextIfIndex_Object = MibScalar
sonusNodeStatNextIfIndex = _SonusNodeStatNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 2, 2),
    _SonusNodeStatNextIfIndex_Type()
)
sonusNodeStatNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeStatNextIfIndex.setStatus("current")


class _SonusNodeStatMgmtStatus_Type(Integer32):
    """Custom type sonusNodeStatMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manageable", 1),
          ("softwareUpgradeFailed", 3),
          ("softwareUpgradeInProgress", 2))
    )


_SonusNodeStatMgmtStatus_Type.__name__ = "Integer32"
_SonusNodeStatMgmtStatus_Object = MibScalar
sonusNodeStatMgmtStatus = _SonusNodeStatMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 2, 3),
    _SonusNodeStatMgmtStatus_Type()
)
sonusNodeStatMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeStatMgmtStatus.setStatus("current")
_SonusNodeShelfAdmnTable_Object = MibTable
sonusNodeShelfAdmnTable = _SonusNodeShelfAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    sonusNodeShelfAdmnTable.setStatus("current")
_SonusNodeShelfAdmnEntry_Object = MibTableRow
sonusNodeShelfAdmnEntry = _SonusNodeShelfAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 3, 1)
)
sonusNodeShelfAdmnEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusNodeShelfAdmnIndex"),
)
if mibBuilder.loadTexts:
    sonusNodeShelfAdmnEntry.setStatus("current")


class _SonusNodeShelfAdmnIndex_Type(Integer32):
    """Custom type sonusNodeShelfAdmnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNodeShelfAdmnIndex_Type.__name__ = "Integer32"
_SonusNodeShelfAdmnIndex_Object = MibTableColumn
sonusNodeShelfAdmnIndex = _SonusNodeShelfAdmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 3, 1, 1),
    _SonusNodeShelfAdmnIndex_Type()
)
sonusNodeShelfAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfAdmnIndex.setStatus("current")
_SonusNodeShelfAdmnState_Type = SonusAdminState
_SonusNodeShelfAdmnState_Object = MibTableColumn
sonusNodeShelfAdmnState = _SonusNodeShelfAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 3, 1, 2),
    _SonusNodeShelfAdmnState_Type()
)
sonusNodeShelfAdmnState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusNodeShelfAdmnState.setStatus("current")
_SonusNodeShelfAdmnIpaddr1_Type = IpAddress
_SonusNodeShelfAdmnIpaddr1_Object = MibTableColumn
sonusNodeShelfAdmnIpaddr1 = _SonusNodeShelfAdmnIpaddr1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 3, 1, 3),
    _SonusNodeShelfAdmnIpaddr1_Type()
)
sonusNodeShelfAdmnIpaddr1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusNodeShelfAdmnIpaddr1.setStatus("current")
_SonusNodeShelfAdmnIpaddr2_Type = IpAddress
_SonusNodeShelfAdmnIpaddr2_Object = MibTableColumn
sonusNodeShelfAdmnIpaddr2 = _SonusNodeShelfAdmnIpaddr2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 3, 1, 4),
    _SonusNodeShelfAdmnIpaddr2_Type()
)
sonusNodeShelfAdmnIpaddr2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusNodeShelfAdmnIpaddr2.setStatus("current")
_SonusNodeShelfAdmn48VdcAState_Type = SonusAdminState
_SonusNodeShelfAdmn48VdcAState_Object = MibTableColumn
sonusNodeShelfAdmn48VdcAState = _SonusNodeShelfAdmn48VdcAState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 3, 1, 5),
    _SonusNodeShelfAdmn48VdcAState_Type()
)
sonusNodeShelfAdmn48VdcAState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusNodeShelfAdmn48VdcAState.setStatus("current")
_SonusNodeShelfAdmn48VdcBState_Type = SonusAdminState
_SonusNodeShelfAdmn48VdcBState_Object = MibTableColumn
sonusNodeShelfAdmn48VdcBState = _SonusNodeShelfAdmn48VdcBState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 3, 1, 6),
    _SonusNodeShelfAdmn48VdcBState_Type()
)
sonusNodeShelfAdmn48VdcBState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusNodeShelfAdmn48VdcBState.setStatus("current")


class _SonusNodeShelfAdmnStatus_Type(Integer32):
    """Custom type sonusNodeShelfAdmnStatus based on Integer32"""
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
        *(("absent", 1),
          ("accepted", 3),
          ("detected", 2),
          ("shuttingDown", 4))
    )


_SonusNodeShelfAdmnStatus_Type.__name__ = "Integer32"
_SonusNodeShelfAdmnStatus_Object = MibTableColumn
sonusNodeShelfAdmnStatus = _SonusNodeShelfAdmnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 3, 1, 7),
    _SonusNodeShelfAdmnStatus_Type()
)
sonusNodeShelfAdmnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfAdmnStatus.setStatus("current")


class _SonusNodeShelfAdmnRestart_Type(Integer32):
    """Custom type sonusNodeShelfAdmnRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("restart", 2),
          ("shutdown", 3),
          ("unknown", 1))
    )


_SonusNodeShelfAdmnRestart_Type.__name__ = "Integer32"
_SonusNodeShelfAdmnRestart_Object = MibTableColumn
sonusNodeShelfAdmnRestart = _SonusNodeShelfAdmnRestart_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 3, 1, 8),
    _SonusNodeShelfAdmnRestart_Type()
)
sonusNodeShelfAdmnRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusNodeShelfAdmnRestart.setStatus("current")
_SonusNodeShelfAdmnRowStatus_Type = RowStatus
_SonusNodeShelfAdmnRowStatus_Object = MibTableColumn
sonusNodeShelfAdmnRowStatus = _SonusNodeShelfAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 3, 1, 9),
    _SonusNodeShelfAdmnRowStatus_Type()
)
sonusNodeShelfAdmnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sonusNodeShelfAdmnRowStatus.setStatus("current")
_SonusNodeShelfStatTable_Object = MibTable
sonusNodeShelfStatTable = _SonusNodeShelfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    sonusNodeShelfStatTable.setStatus("current")
_SonusNodeShelfStatEntry_Object = MibTableRow
sonusNodeShelfStatEntry = _SonusNodeShelfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1)
)
sonusNodeShelfStatEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusNodeShelfStatIndex"),
)
if mibBuilder.loadTexts:
    sonusNodeShelfStatEntry.setStatus("current")
_SonusNodeShelfStatIndex_Type = Integer32
_SonusNodeShelfStatIndex_Object = MibTableColumn
sonusNodeShelfStatIndex = _SonusNodeShelfStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1, 1),
    _SonusNodeShelfStatIndex_Type()
)
sonusNodeShelfStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfStatIndex.setStatus("current")


class _SonusNodeShelfStatSlots_Type(Integer32):
    """Custom type sonusNodeShelfStatSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusNodeShelfStatSlots_Type.__name__ = "Integer32"
_SonusNodeShelfStatSlots_Object = MibTableColumn
sonusNodeShelfStatSlots = _SonusNodeShelfStatSlots_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1, 2),
    _SonusNodeShelfStatSlots_Type()
)
sonusNodeShelfStatSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfStatSlots.setStatus("current")


class _SonusNodeShelfStatSerialNumber_Type(DisplayString):
    """Custom type sonusNodeShelfStatSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SonusNodeShelfStatSerialNumber_Type.__name__ = "DisplayString"
_SonusNodeShelfStatSerialNumber_Object = MibTableColumn
sonusNodeShelfStatSerialNumber = _SonusNodeShelfStatSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1, 3),
    _SonusNodeShelfStatSerialNumber_Type()
)
sonusNodeShelfStatSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfStatSerialNumber.setStatus("current")


class _SonusNodeShelfStatType_Type(Integer32):
    """Custom type sonusNodeShelfStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1))
    )


_SonusNodeShelfStatType_Type.__name__ = "Integer32"
_SonusNodeShelfStatType_Object = MibTableColumn
sonusNodeShelfStatType = _SonusNodeShelfStatType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1, 4),
    _SonusNodeShelfStatType_Type()
)
sonusNodeShelfStatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfStatType.setStatus("current")


class _SonusNodeShelfStatFan_Type(Integer32):
    """Custom type sonusNodeShelfStatFan based on Integer32"""
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
        *(("controllerFailure", 2),
          ("multipleFailures", 4),
          ("notPresent", 1),
          ("operational", 6),
          ("powerFailure", 5),
          ("singleFailure", 3))
    )


_SonusNodeShelfStatFan_Type.__name__ = "Integer32"
_SonusNodeShelfStatFan_Object = MibTableColumn
sonusNodeShelfStatFan = _SonusNodeShelfStatFan_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1, 5),
    _SonusNodeShelfStatFan_Type()
)
sonusNodeShelfStatFan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfStatFan.setStatus("current")


class _SonusNodeShelfStat48VAStatus_Type(Integer32):
    """Custom type sonusNodeShelfStat48VAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2))
    )


_SonusNodeShelfStat48VAStatus_Type.__name__ = "Integer32"
_SonusNodeShelfStat48VAStatus_Object = MibTableColumn
sonusNodeShelfStat48VAStatus = _SonusNodeShelfStat48VAStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1, 6),
    _SonusNodeShelfStat48VAStatus_Type()
)
sonusNodeShelfStat48VAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfStat48VAStatus.setStatus("current")


class _SonusNodeShelfStat48VBStatus_Type(Integer32):
    """Custom type sonusNodeShelfStat48VBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2))
    )


_SonusNodeShelfStat48VBStatus_Type.__name__ = "Integer32"
_SonusNodeShelfStat48VBStatus_Object = MibTableColumn
sonusNodeShelfStat48VBStatus = _SonusNodeShelfStat48VBStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1, 7),
    _SonusNodeShelfStat48VBStatus_Type()
)
sonusNodeShelfStat48VBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfStat48VBStatus.setStatus("current")
_SonusNodeShelfStatBackplane_Type = HwTypeID
_SonusNodeShelfStatBackplane_Object = MibTableColumn
sonusNodeShelfStatBackplane = _SonusNodeShelfStatBackplane_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1, 8),
    _SonusNodeShelfStatBackplane_Type()
)
sonusNodeShelfStatBackplane.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfStatBackplane.setStatus("current")
_SonusNodeShelfStatBootCount_Type = Integer32
_SonusNodeShelfStatBootCount_Object = MibTableColumn
sonusNodeShelfStatBootCount = _SonusNodeShelfStatBootCount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1, 9),
    _SonusNodeShelfStatBootCount_Type()
)
sonusNodeShelfStatBootCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfStatBootCount.setStatus("current")
_SonusNodeShelfStatTemperature_Type = Integer32
_SonusNodeShelfStatTemperature_Object = MibTableColumn
sonusNodeShelfStatTemperature = _SonusNodeShelfStatTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1, 10),
    _SonusNodeShelfStatTemperature_Type()
)
sonusNodeShelfStatTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfStatTemperature.setStatus("current")


class _SonusNodeShelfStatFanSpeed_Type(Integer32):
    """Custom type sonusNodeShelfStatFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1))
    )


_SonusNodeShelfStatFanSpeed_Type.__name__ = "Integer32"
_SonusNodeShelfStatFanSpeed_Object = MibTableColumn
sonusNodeShelfStatFanSpeed = _SonusNodeShelfStatFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 4, 1, 11),
    _SonusNodeShelfStatFanSpeed_Type()
)
sonusNodeShelfStatFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeShelfStatFanSpeed.setStatus("current")
_SonusNodeSrvrAdmnTable_Object = MibTable
sonusNodeSrvrAdmnTable = _SonusNodeSrvrAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnTable.setStatus("current")
_SonusNodeSrvrAdmnEntry_Object = MibTableRow
sonusNodeSrvrAdmnEntry = _SonusNodeSrvrAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1)
)
sonusNodeSrvrAdmnEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusNodeSrvrAdmnShelfIndex"),
    (0, "SONUS-NODE-MIB", "sonusNodeSrvrAdmnSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnEntry.setStatus("current")


class _SonusNodeSrvrAdmnShelfIndex_Type(Integer32):
    """Custom type sonusNodeSrvrAdmnShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNodeSrvrAdmnShelfIndex_Type.__name__ = "Integer32"
_SonusNodeSrvrAdmnShelfIndex_Object = MibTableColumn
sonusNodeSrvrAdmnShelfIndex = _SonusNodeSrvrAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 1),
    _SonusNodeSrvrAdmnShelfIndex_Type()
)
sonusNodeSrvrAdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnShelfIndex.setStatus("current")


class _SonusNodeSrvrAdmnSlotIndex_Type(Integer32):
    """Custom type sonusNodeSrvrAdmnSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusNodeSrvrAdmnSlotIndex_Type.__name__ = "Integer32"
_SonusNodeSrvrAdmnSlotIndex_Object = MibTableColumn
sonusNodeSrvrAdmnSlotIndex = _SonusNodeSrvrAdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 2),
    _SonusNodeSrvrAdmnSlotIndex_Type()
)
sonusNodeSrvrAdmnSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnSlotIndex.setStatus("current")
_SonusNodeSrvrAdmnHwType_Type = ServerTypeID
_SonusNodeSrvrAdmnHwType_Object = MibTableColumn
sonusNodeSrvrAdmnHwType = _SonusNodeSrvrAdmnHwType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 3),
    _SonusNodeSrvrAdmnHwType_Type()
)
sonusNodeSrvrAdmnHwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnHwType.setStatus("current")


class _SonusNodeSrvrAdmnState_Type(SonusAdminState):
    """Custom type sonusNodeSrvrAdmnState based on SonusAdminState"""


_SonusNodeSrvrAdmnState_Object = MibTableColumn
sonusNodeSrvrAdmnState = _SonusNodeSrvrAdmnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 4),
    _SonusNodeSrvrAdmnState_Type()
)
sonusNodeSrvrAdmnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnState.setStatus("current")


class _SonusNodeSrvrAdmnMode_Type(SonusServiceState):
    """Custom type sonusNodeSrvrAdmnMode based on SonusServiceState"""


_SonusNodeSrvrAdmnMode_Object = MibTableColumn
sonusNodeSrvrAdmnMode = _SonusNodeSrvrAdmnMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 5),
    _SonusNodeSrvrAdmnMode_Type()
)
sonusNodeSrvrAdmnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnMode.setStatus("current")


class _SonusNodeSrvrAdmnAction_Type(SonusAdminAction):
    """Custom type sonusNodeSrvrAdmnAction based on SonusAdminAction"""


_SonusNodeSrvrAdmnAction_Object = MibTableColumn
sonusNodeSrvrAdmnAction = _SonusNodeSrvrAdmnAction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 6),
    _SonusNodeSrvrAdmnAction_Type()
)
sonusNodeSrvrAdmnAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnAction.setStatus("current")


class _SonusNodeSrvrAdmnDryupLimit_Type(Integer32):
    """Custom type sonusNodeSrvrAdmnDryupLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusNodeSrvrAdmnDryupLimit_Type.__name__ = "Integer32"
_SonusNodeSrvrAdmnDryupLimit_Object = MibTableColumn
sonusNodeSrvrAdmnDryupLimit = _SonusNodeSrvrAdmnDryupLimit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 7),
    _SonusNodeSrvrAdmnDryupLimit_Type()
)
sonusNodeSrvrAdmnDryupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnDryupLimit.setStatus("current")


class _SonusNodeSrvrAdmnDumpState_Type(SonusAdminState):
    """Custom type sonusNodeSrvrAdmnDumpState based on SonusAdminState"""


_SonusNodeSrvrAdmnDumpState_Object = MibTableColumn
sonusNodeSrvrAdmnDumpState = _SonusNodeSrvrAdmnDumpState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 8),
    _SonusNodeSrvrAdmnDumpState_Type()
)
sonusNodeSrvrAdmnDumpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnDumpState.setStatus("current")
_SonusNodeSrvrAdmnRowStatus_Type = RowStatus
_SonusNodeSrvrAdmnRowStatus_Object = MibTableColumn
sonusNodeSrvrAdmnRowStatus = _SonusNodeSrvrAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 9),
    _SonusNodeSrvrAdmnRowStatus_Type()
)
sonusNodeSrvrAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnRowStatus.setStatus("current")


class _SonusNodeSrvrAdmnRedundancyRole_Type(Integer32):
    """Custom type sonusNodeSrvrAdmnRedundancyRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("redundant", 2))
    )


_SonusNodeSrvrAdmnRedundancyRole_Type.__name__ = "Integer32"
_SonusNodeSrvrAdmnRedundancyRole_Object = MibTableColumn
sonusNodeSrvrAdmnRedundancyRole = _SonusNodeSrvrAdmnRedundancyRole_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 10),
    _SonusNodeSrvrAdmnRedundancyRole_Type()
)
sonusNodeSrvrAdmnRedundancyRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnRedundancyRole.setStatus("current")
_SonusNodeSrvrAdmnAdapHwType_Type = AdapterTypeID
_SonusNodeSrvrAdmnAdapHwType_Object = MibTableColumn
sonusNodeSrvrAdmnAdapHwType = _SonusNodeSrvrAdmnAdapHwType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 11),
    _SonusNodeSrvrAdmnAdapHwType_Type()
)
sonusNodeSrvrAdmnAdapHwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnAdapHwType.setStatus("current")
_SonusNodeSrvrAdmnSpecialFunction_Type = ServerFunctionType
_SonusNodeSrvrAdmnSpecialFunction_Object = MibTableColumn
sonusNodeSrvrAdmnSpecialFunction = _SonusNodeSrvrAdmnSpecialFunction_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 5, 1, 12),
    _SonusNodeSrvrAdmnSpecialFunction_Type()
)
sonusNodeSrvrAdmnSpecialFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeSrvrAdmnSpecialFunction.setStatus("current")
_SonusNodeSlotTable_Object = MibTable
sonusNodeSlotTable = _SonusNodeSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sonusNodeSlotTable.setStatus("current")
_SonusNodeSlotEntry_Object = MibTableRow
sonusNodeSlotEntry = _SonusNodeSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 6, 1)
)
sonusNodeSlotEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusNodeSlotShelfIndex"),
    (0, "SONUS-NODE-MIB", "sonusNodeSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusNodeSlotEntry.setStatus("current")


class _SonusNodeSlotShelfIndex_Type(Integer32):
    """Custom type sonusNodeSlotShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNodeSlotShelfIndex_Type.__name__ = "Integer32"
_SonusNodeSlotShelfIndex_Object = MibTableColumn
sonusNodeSlotShelfIndex = _SonusNodeSlotShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 6, 1, 1),
    _SonusNodeSlotShelfIndex_Type()
)
sonusNodeSlotShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSlotShelfIndex.setStatus("current")


class _SonusNodeSlotIndex_Type(Integer32):
    """Custom type sonusNodeSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusNodeSlotIndex_Type.__name__ = "Integer32"
_SonusNodeSlotIndex_Object = MibTableColumn
sonusNodeSlotIndex = _SonusNodeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 6, 1, 2),
    _SonusNodeSlotIndex_Type()
)
sonusNodeSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSlotIndex.setStatus("current")


class _SonusNodeSlotState_Type(Integer32):
    """Custom type sonusNodeSlotState based on Integer32"""
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
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("activated", 11),
          ("activating", 10),
          ("boot", 5),
          ("coreDump", 7),
          ("empty", 2),
          ("faulted", 13),
          ("holdOff", 8),
          ("inserted", 3),
          ("loading", 9),
          ("powerFail", 15),
          ("powerOff", 14),
          ("reset", 4),
          ("running", 12),
          ("sonicId", 6),
          ("unknown", 1))
    )


_SonusNodeSlotState_Type.__name__ = "Integer32"
_SonusNodeSlotState_Object = MibTableColumn
sonusNodeSlotState = _SonusNodeSlotState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 6, 1, 3),
    _SonusNodeSlotState_Type()
)
sonusNodeSlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSlotState.setStatus("current")
_SonusNodeSlotHwType_Type = HwTypeID
_SonusNodeSlotHwType_Object = MibTableColumn
sonusNodeSlotHwType = _SonusNodeSlotHwType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 6, 1, 4),
    _SonusNodeSlotHwType_Type()
)
sonusNodeSlotHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSlotHwType.setStatus("current")
_SonusNodeSlotHwTypeRev_Type = Integer32
_SonusNodeSlotHwTypeRev_Object = MibTableColumn
sonusNodeSlotHwTypeRev = _SonusNodeSlotHwTypeRev_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 6, 1, 5),
    _SonusNodeSlotHwTypeRev_Type()
)
sonusNodeSlotHwTypeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSlotHwTypeRev.setStatus("current")


class _SonusNodeSlotPower_Type(Integer32):
    """Custom type sonusNodeSlotPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("powerFault", 2),
          ("powerOK", 3),
          ("unknown", 1))
    )


_SonusNodeSlotPower_Type.__name__ = "Integer32"
_SonusNodeSlotPower_Object = MibTableColumn
sonusNodeSlotPower = _SonusNodeSlotPower_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 6, 1, 6),
    _SonusNodeSlotPower_Type()
)
sonusNodeSlotPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSlotPower.setStatus("current")


class _SonusNodeSlotAdapState_Type(Integer32):
    """Custom type sonusNodeSlotAdapState based on Integer32"""
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
        *(("empty", 2),
          ("faulted", 4),
          ("present", 3),
          ("unknown", 1))
    )


_SonusNodeSlotAdapState_Type.__name__ = "Integer32"
_SonusNodeSlotAdapState_Object = MibTableColumn
sonusNodeSlotAdapState = _SonusNodeSlotAdapState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 6, 1, 7),
    _SonusNodeSlotAdapState_Type()
)
sonusNodeSlotAdapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSlotAdapState.setStatus("current")
_SonusNodeSlotAdapHwType_Type = HwTypeID
_SonusNodeSlotAdapHwType_Object = MibTableColumn
sonusNodeSlotAdapHwType = _SonusNodeSlotAdapHwType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 6, 1, 8),
    _SonusNodeSlotAdapHwType_Type()
)
sonusNodeSlotAdapHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSlotAdapHwType.setStatus("current")
_SonusNodeSrvrStatTable_Object = MibTable
sonusNodeSrvrStatTable = _SonusNodeSrvrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    sonusNodeSrvrStatTable.setStatus("current")
_SonusNodeSrvrStatEntry_Object = MibTableRow
sonusNodeSrvrStatEntry = _SonusNodeSrvrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1)
)
sonusNodeSrvrStatEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusNodeSrvrStatShelfIndex"),
    (0, "SONUS-NODE-MIB", "sonusNodeSrvrStatSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusNodeSrvrStatEntry.setStatus("current")


class _SonusNodeSrvrStatShelfIndex_Type(Integer32):
    """Custom type sonusNodeSrvrStatShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNodeSrvrStatShelfIndex_Type.__name__ = "Integer32"
_SonusNodeSrvrStatShelfIndex_Object = MibTableColumn
sonusNodeSrvrStatShelfIndex = _SonusNodeSrvrStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 1),
    _SonusNodeSrvrStatShelfIndex_Type()
)
sonusNodeSrvrStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatShelfIndex.setStatus("current")


class _SonusNodeSrvrStatSlotIndex_Type(Integer32):
    """Custom type sonusNodeSrvrStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusNodeSrvrStatSlotIndex_Type.__name__ = "Integer32"
_SonusNodeSrvrStatSlotIndex_Object = MibTableColumn
sonusNodeSrvrStatSlotIndex = _SonusNodeSrvrStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 2),
    _SonusNodeSrvrStatSlotIndex_Type()
)
sonusNodeSrvrStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatSlotIndex.setStatus("current")
_SonusNodeSrvrStatMiddVersion_Type = Integer32
_SonusNodeSrvrStatMiddVersion_Object = MibTableColumn
sonusNodeSrvrStatMiddVersion = _SonusNodeSrvrStatMiddVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 3),
    _SonusNodeSrvrStatMiddVersion_Type()
)
sonusNodeSrvrStatMiddVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatMiddVersion.setStatus("current")
_SonusNodeSrvrStatHwType_Type = HwTypeID
_SonusNodeSrvrStatHwType_Object = MibTableColumn
sonusNodeSrvrStatHwType = _SonusNodeSrvrStatHwType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 4),
    _SonusNodeSrvrStatHwType_Type()
)
sonusNodeSrvrStatHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatHwType.setStatus("current")


class _SonusNodeSrvrStatSerialNum_Type(DisplayString):
    """Custom type sonusNodeSrvrStatSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SonusNodeSrvrStatSerialNum_Type.__name__ = "DisplayString"
_SonusNodeSrvrStatSerialNum_Object = MibTableColumn
sonusNodeSrvrStatSerialNum = _SonusNodeSrvrStatSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 5),
    _SonusNodeSrvrStatSerialNum_Type()
)
sonusNodeSrvrStatSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatSerialNum.setStatus("current")


class _SonusNodeSrvrStatPartNum_Type(DisplayString):
    """Custom type sonusNodeSrvrStatPartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SonusNodeSrvrStatPartNum_Type.__name__ = "DisplayString"
_SonusNodeSrvrStatPartNum_Object = MibTableColumn
sonusNodeSrvrStatPartNum = _SonusNodeSrvrStatPartNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 6),
    _SonusNodeSrvrStatPartNum_Type()
)
sonusNodeSrvrStatPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatPartNum.setStatus("current")


class _SonusNodeSrvrStatPartNumRev_Type(DisplayString):
    """Custom type sonusNodeSrvrStatPartNumRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_SonusNodeSrvrStatPartNumRev_Type.__name__ = "DisplayString"
_SonusNodeSrvrStatPartNumRev_Object = MibTableColumn
sonusNodeSrvrStatPartNumRev = _SonusNodeSrvrStatPartNumRev_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 7),
    _SonusNodeSrvrStatPartNumRev_Type()
)
sonusNodeSrvrStatPartNumRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatPartNumRev.setStatus("current")


class _SonusNodeSrvrStatMfgDate_Type(DisplayString):
    """Custom type sonusNodeSrvrStatMfgDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SonusNodeSrvrStatMfgDate_Type.__name__ = "DisplayString"
_SonusNodeSrvrStatMfgDate_Object = MibTableColumn
sonusNodeSrvrStatMfgDate = _SonusNodeSrvrStatMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 8),
    _SonusNodeSrvrStatMfgDate_Type()
)
sonusNodeSrvrStatMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatMfgDate.setStatus("current")


class _SonusNodeSrvrStatFlashVersion_Type(DisplayString):
    """Custom type sonusNodeSrvrStatFlashVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SonusNodeSrvrStatFlashVersion_Type.__name__ = "DisplayString"
_SonusNodeSrvrStatFlashVersion_Object = MibTableColumn
sonusNodeSrvrStatFlashVersion = _SonusNodeSrvrStatFlashVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 9),
    _SonusNodeSrvrStatFlashVersion_Type()
)
sonusNodeSrvrStatFlashVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatFlashVersion.setStatus("current")


class _SonusNodeSrvrStatSwVersion_Type(DisplayString):
    """Custom type sonusNodeSrvrStatSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SonusNodeSrvrStatSwVersion_Type.__name__ = "DisplayString"
_SonusNodeSrvrStatSwVersion_Object = MibTableColumn
sonusNodeSrvrStatSwVersion = _SonusNodeSrvrStatSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 10),
    _SonusNodeSrvrStatSwVersion_Type()
)
sonusNodeSrvrStatSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatSwVersion.setStatus("current")
_SonusNodeSrvrStatBuildNum_Type = Integer32
_SonusNodeSrvrStatBuildNum_Object = MibTableColumn
sonusNodeSrvrStatBuildNum = _SonusNodeSrvrStatBuildNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 11),
    _SonusNodeSrvrStatBuildNum_Type()
)
sonusNodeSrvrStatBuildNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatBuildNum.setStatus("current")


class _SonusNodeSrvrStatMode_Type(Integer32):
    """Custom type sonusNodeSrvrStatMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("standby", 1))
    )


_SonusNodeSrvrStatMode_Type.__name__ = "Integer32"
_SonusNodeSrvrStatMode_Object = MibTableColumn
sonusNodeSrvrStatMode = _SonusNodeSrvrStatMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 12),
    _SonusNodeSrvrStatMode_Type()
)
sonusNodeSrvrStatMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatMode.setStatus("current")
_SonusNodeSrvrStatTemperature_Type = Integer32
_SonusNodeSrvrStatTemperature_Object = MibTableColumn
sonusNodeSrvrStatTemperature = _SonusNodeSrvrStatTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 13),
    _SonusNodeSrvrStatTemperature_Type()
)
sonusNodeSrvrStatTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatTemperature.setStatus("current")
_SonusNodeSrvrStatMemUtilization_Type = Integer32
_SonusNodeSrvrStatMemUtilization_Object = MibTableColumn
sonusNodeSrvrStatMemUtilization = _SonusNodeSrvrStatMemUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 14),
    _SonusNodeSrvrStatMemUtilization_Type()
)
sonusNodeSrvrStatMemUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatMemUtilization.setStatus("current")
_SonusNodeSrvrStatCpuUtilization_Type = Integer32
_SonusNodeSrvrStatCpuUtilization_Object = MibTableColumn
sonusNodeSrvrStatCpuUtilization = _SonusNodeSrvrStatCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 15),
    _SonusNodeSrvrStatCpuUtilization_Type()
)
sonusNodeSrvrStatCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatCpuUtilization.setStatus("current")
_SonusNodeSrvrStatHwTypeRev_Type = Integer32
_SonusNodeSrvrStatHwTypeRev_Object = MibTableColumn
sonusNodeSrvrStatHwTypeRev = _SonusNodeSrvrStatHwTypeRev_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 16),
    _SonusNodeSrvrStatHwTypeRev_Type()
)
sonusNodeSrvrStatHwTypeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatHwTypeRev.setStatus("current")
_SonusNodeSrvrStatSwVersionCode_Type = SonusSoftwareVersion
_SonusNodeSrvrStatSwVersionCode_Object = MibTableColumn
sonusNodeSrvrStatSwVersionCode = _SonusNodeSrvrStatSwVersionCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 17),
    _SonusNodeSrvrStatSwVersionCode_Type()
)
sonusNodeSrvrStatSwVersionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatSwVersionCode.setStatus("current")
_SonusNodeSrvrStatEpldRev_Type = Integer32
_SonusNodeSrvrStatEpldRev_Object = MibTableColumn
sonusNodeSrvrStatEpldRev = _SonusNodeSrvrStatEpldRev_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 18),
    _SonusNodeSrvrStatEpldRev_Type()
)
sonusNodeSrvrStatEpldRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatEpldRev.setStatus("current")


class _SonusNodeSrvrStatHostName_Type(DisplayString):
    """Custom type sonusNodeSrvrStatHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SonusNodeSrvrStatHostName_Type.__name__ = "DisplayString"
_SonusNodeSrvrStatHostName_Object = MibTableColumn
sonusNodeSrvrStatHostName = _SonusNodeSrvrStatHostName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 19),
    _SonusNodeSrvrStatHostName_Type()
)
sonusNodeSrvrStatHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatHostName.setStatus("current")


class _SonusNodeSrvrStatUserName_Type(DisplayString):
    """Custom type sonusNodeSrvrStatUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SonusNodeSrvrStatUserName_Type.__name__ = "DisplayString"
_SonusNodeSrvrStatUserName_Object = MibTableColumn
sonusNodeSrvrStatUserName = _SonusNodeSrvrStatUserName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 20),
    _SonusNodeSrvrStatUserName_Type()
)
sonusNodeSrvrStatUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatUserName.setStatus("current")


class _SonusNodeSrvrStatViewName_Type(DisplayString):
    """Custom type sonusNodeSrvrStatViewName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SonusNodeSrvrStatViewName_Type.__name__ = "DisplayString"
_SonusNodeSrvrStatViewName_Object = MibTableColumn
sonusNodeSrvrStatViewName = _SonusNodeSrvrStatViewName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 21),
    _SonusNodeSrvrStatViewName_Type()
)
sonusNodeSrvrStatViewName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatViewName.setStatus("current")
_SonusNodeSrvrStatTotalMem_Type = Integer32
_SonusNodeSrvrStatTotalMem_Object = MibTableColumn
sonusNodeSrvrStatTotalMem = _SonusNodeSrvrStatTotalMem_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 22),
    _SonusNodeSrvrStatTotalMem_Type()
)
sonusNodeSrvrStatTotalMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatTotalMem.setStatus("current")
_SonusNodeSrvrStatFreeMem_Type = Integer32
_SonusNodeSrvrStatFreeMem_Object = MibTableColumn
sonusNodeSrvrStatFreeMem = _SonusNodeSrvrStatFreeMem_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 23),
    _SonusNodeSrvrStatFreeMem_Type()
)
sonusNodeSrvrStatFreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatFreeMem.setStatus("current")
_SonusNodeSrvrStatTotalSharedMem_Type = Integer32
_SonusNodeSrvrStatTotalSharedMem_Object = MibTableColumn
sonusNodeSrvrStatTotalSharedMem = _SonusNodeSrvrStatTotalSharedMem_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 24),
    _SonusNodeSrvrStatTotalSharedMem_Type()
)
sonusNodeSrvrStatTotalSharedMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatTotalSharedMem.setStatus("current")
_SonusNodeSrvrStatFreeSharedMem_Type = Integer32
_SonusNodeSrvrStatFreeSharedMem_Object = MibTableColumn
sonusNodeSrvrStatFreeSharedMem = _SonusNodeSrvrStatFreeSharedMem_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 7, 1, 25),
    _SonusNodeSrvrStatFreeSharedMem_Type()
)
sonusNodeSrvrStatFreeSharedMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSrvrStatFreeSharedMem.setStatus("current")
_SonusNodeAdapStatTable_Object = MibTable
sonusNodeAdapStatTable = _SonusNodeAdapStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 11)
)
if mibBuilder.loadTexts:
    sonusNodeAdapStatTable.setStatus("current")
_SonusNodeAdapStatEntry_Object = MibTableRow
sonusNodeAdapStatEntry = _SonusNodeAdapStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 11, 1)
)
sonusNodeAdapStatEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusNodeAdapStatShelfIndex"),
    (0, "SONUS-NODE-MIB", "sonusNodeAdapStatSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusNodeAdapStatEntry.setStatus("current")


class _SonusNodeAdapStatShelfIndex_Type(Integer32):
    """Custom type sonusNodeAdapStatShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNodeAdapStatShelfIndex_Type.__name__ = "Integer32"
_SonusNodeAdapStatShelfIndex_Object = MibTableColumn
sonusNodeAdapStatShelfIndex = _SonusNodeAdapStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 11, 1, 1),
    _SonusNodeAdapStatShelfIndex_Type()
)
sonusNodeAdapStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeAdapStatShelfIndex.setStatus("current")


class _SonusNodeAdapStatSlotIndex_Type(Integer32):
    """Custom type sonusNodeAdapStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusNodeAdapStatSlotIndex_Type.__name__ = "Integer32"
_SonusNodeAdapStatSlotIndex_Object = MibTableColumn
sonusNodeAdapStatSlotIndex = _SonusNodeAdapStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 11, 1, 2),
    _SonusNodeAdapStatSlotIndex_Type()
)
sonusNodeAdapStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeAdapStatSlotIndex.setStatus("current")
_SonusNodeAdapStatMiddVersion_Type = Integer32
_SonusNodeAdapStatMiddVersion_Object = MibTableColumn
sonusNodeAdapStatMiddVersion = _SonusNodeAdapStatMiddVersion_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 11, 1, 3),
    _SonusNodeAdapStatMiddVersion_Type()
)
sonusNodeAdapStatMiddVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeAdapStatMiddVersion.setStatus("current")
_SonusNodeAdapStatHwType_Type = HwTypeID
_SonusNodeAdapStatHwType_Object = MibTableColumn
sonusNodeAdapStatHwType = _SonusNodeAdapStatHwType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 11, 1, 4),
    _SonusNodeAdapStatHwType_Type()
)
sonusNodeAdapStatHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeAdapStatHwType.setStatus("current")
_SonusNodeAdapStatHwTypeRev_Type = Integer32
_SonusNodeAdapStatHwTypeRev_Object = MibTableColumn
sonusNodeAdapStatHwTypeRev = _SonusNodeAdapStatHwTypeRev_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 11, 1, 5),
    _SonusNodeAdapStatHwTypeRev_Type()
)
sonusNodeAdapStatHwTypeRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeAdapStatHwTypeRev.setStatus("current")


class _SonusNodeAdapStatSerialNum_Type(DisplayString):
    """Custom type sonusNodeAdapStatSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SonusNodeAdapStatSerialNum_Type.__name__ = "DisplayString"
_SonusNodeAdapStatSerialNum_Object = MibTableColumn
sonusNodeAdapStatSerialNum = _SonusNodeAdapStatSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 11, 1, 6),
    _SonusNodeAdapStatSerialNum_Type()
)
sonusNodeAdapStatSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeAdapStatSerialNum.setStatus("current")


class _SonusNodeAdapStatPartNum_Type(DisplayString):
    """Custom type sonusNodeAdapStatPartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SonusNodeAdapStatPartNum_Type.__name__ = "DisplayString"
_SonusNodeAdapStatPartNum_Object = MibTableColumn
sonusNodeAdapStatPartNum = _SonusNodeAdapStatPartNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 11, 1, 7),
    _SonusNodeAdapStatPartNum_Type()
)
sonusNodeAdapStatPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeAdapStatPartNum.setStatus("current")


class _SonusNodeAdapStatPartNumRev_Type(DisplayString):
    """Custom type sonusNodeAdapStatPartNumRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_SonusNodeAdapStatPartNumRev_Type.__name__ = "DisplayString"
_SonusNodeAdapStatPartNumRev_Object = MibTableColumn
sonusNodeAdapStatPartNumRev = _SonusNodeAdapStatPartNumRev_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 11, 1, 8),
    _SonusNodeAdapStatPartNumRev_Type()
)
sonusNodeAdapStatPartNumRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeAdapStatPartNumRev.setStatus("current")


class _SonusNodeAdapStatMfgDate_Type(DisplayString):
    """Custom type sonusNodeAdapStatMfgDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SonusNodeAdapStatMfgDate_Type.__name__ = "DisplayString"
_SonusNodeAdapStatMfgDate_Object = MibTableColumn
sonusNodeAdapStatMfgDate = _SonusNodeAdapStatMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 11, 1, 9),
    _SonusNodeAdapStatMfgDate_Type()
)
sonusNodeAdapStatMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeAdapStatMfgDate.setStatus("current")
_SonusNodeSlotAdmnTable_Object = MibTable
sonusNodeSlotAdmnTable = _SonusNodeSlotAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    sonusNodeSlotAdmnTable.setStatus("current")
_SonusNodeSlotAdmnEntry_Object = MibTableRow
sonusNodeSlotAdmnEntry = _SonusNodeSlotAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 12, 1)
)
sonusNodeSlotAdmnEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusNodeSlotAdmnShelfIndex"),
    (0, "SONUS-NODE-MIB", "sonusNodeSlotAdmnSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusNodeSlotAdmnEntry.setStatus("current")


class _SonusNodeSlotAdmnShelfIndex_Type(Integer32):
    """Custom type sonusNodeSlotAdmnShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNodeSlotAdmnShelfIndex_Type.__name__ = "Integer32"
_SonusNodeSlotAdmnShelfIndex_Object = MibTableColumn
sonusNodeSlotAdmnShelfIndex = _SonusNodeSlotAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 12, 1, 1),
    _SonusNodeSlotAdmnShelfIndex_Type()
)
sonusNodeSlotAdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSlotAdmnShelfIndex.setStatus("current")


class _SonusNodeSlotAdmnSlotIndex_Type(Integer32):
    """Custom type sonusNodeSlotAdmnSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusNodeSlotAdmnSlotIndex_Type.__name__ = "Integer32"
_SonusNodeSlotAdmnSlotIndex_Object = MibTableColumn
sonusNodeSlotAdmnSlotIndex = _SonusNodeSlotAdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 12, 1, 2),
    _SonusNodeSlotAdmnSlotIndex_Type()
)
sonusNodeSlotAdmnSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNodeSlotAdmnSlotIndex.setStatus("current")


class _SonusNodeSlotAdmnReset_Type(Integer32):
    """Custom type sonusNodeSlotAdmnReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coredump", 3),
          ("reset", 2),
          ("undefined", 1))
    )


_SonusNodeSlotAdmnReset_Type.__name__ = "Integer32"
_SonusNodeSlotAdmnReset_Object = MibTableColumn
sonusNodeSlotAdmnReset = _SonusNodeSlotAdmnReset_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 1, 12, 1, 3),
    _SonusNodeSlotAdmnReset_Type()
)
sonusNodeSlotAdmnReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNodeSlotAdmnReset.setStatus("current")
_SonusNvsConfig_ObjectIdentity = ObjectIdentity
sonusNvsConfig = _SonusNvsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2)
)
_SonusNvsConfigTable_Object = MibTable
sonusNvsConfigTable = _SonusNvsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sonusNvsConfigTable.setStatus("current")
_SonusNvsConfigEntry_Object = MibTableRow
sonusNvsConfigEntry = _SonusNvsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1)
)
sonusNvsConfigEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusBparamShelfIndex"),
)
if mibBuilder.loadTexts:
    sonusNvsConfigEntry.setStatus("current")


class _SonusBparamShelfIndex_Type(Integer32):
    """Custom type sonusBparamShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusBparamShelfIndex_Type.__name__ = "Integer32"
_SonusBparamShelfIndex_Object = MibTableColumn
sonusBparamShelfIndex = _SonusBparamShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 1),
    _SonusBparamShelfIndex_Type()
)
sonusBparamShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusBparamShelfIndex.setStatus("current")
_SonusBparamUnused_Type = Integer32
_SonusBparamUnused_Object = MibTableColumn
sonusBparamUnused = _SonusBparamUnused_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 2),
    _SonusBparamUnused_Type()
)
sonusBparamUnused.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusBparamUnused.setStatus("current")


class _SonusBparamPasswd_Type(DisplayString):
    """Custom type sonusBparamPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusBparamPasswd_Type.__name__ = "DisplayString"
_SonusBparamPasswd_Object = MibTableColumn
sonusBparamPasswd = _SonusBparamPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 3),
    _SonusBparamPasswd_Type()
)
sonusBparamPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamPasswd.setStatus("current")
_SonusBparamIpAddrSlot1Port0_Type = IpAddress
_SonusBparamIpAddrSlot1Port0_Object = MibTableColumn
sonusBparamIpAddrSlot1Port0 = _SonusBparamIpAddrSlot1Port0_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 4),
    _SonusBparamIpAddrSlot1Port0_Type()
)
sonusBparamIpAddrSlot1Port0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpAddrSlot1Port0.setStatus("current")
_SonusBparamIpMaskSlot1Port0_Type = IpAddress
_SonusBparamIpMaskSlot1Port0_Object = MibTableColumn
sonusBparamIpMaskSlot1Port0 = _SonusBparamIpMaskSlot1Port0_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 5),
    _SonusBparamIpMaskSlot1Port0_Type()
)
sonusBparamIpMaskSlot1Port0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpMaskSlot1Port0.setStatus("current")
_SonusBparamIpGatewaySlot1Port0_Type = IpAddress
_SonusBparamIpGatewaySlot1Port0_Object = MibTableColumn
sonusBparamIpGatewaySlot1Port0 = _SonusBparamIpGatewaySlot1Port0_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 6),
    _SonusBparamIpGatewaySlot1Port0_Type()
)
sonusBparamIpGatewaySlot1Port0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpGatewaySlot1Port0.setStatus("current")


class _SonusBparamIfSpeedTypeSlot1Port0_Type(Integer32):
    """Custom type sonusBparamIfSpeedTypeSlot1Port0 based on Integer32"""
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
        *(("autoNegotiate", 1),
          ("fullDuplex10", 4),
          ("fullDuplex100", 2),
          ("halfDuplex10", 5),
          ("halfDuplex100", 3))
    )


_SonusBparamIfSpeedTypeSlot1Port0_Type.__name__ = "Integer32"
_SonusBparamIfSpeedTypeSlot1Port0_Object = MibTableColumn
sonusBparamIfSpeedTypeSlot1Port0 = _SonusBparamIfSpeedTypeSlot1Port0_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 7),
    _SonusBparamIfSpeedTypeSlot1Port0_Type()
)
sonusBparamIfSpeedTypeSlot1Port0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIfSpeedTypeSlot1Port0.setStatus("current")
_SonusBparamIpAddrSlot1Port1_Type = IpAddress
_SonusBparamIpAddrSlot1Port1_Object = MibTableColumn
sonusBparamIpAddrSlot1Port1 = _SonusBparamIpAddrSlot1Port1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 8),
    _SonusBparamIpAddrSlot1Port1_Type()
)
sonusBparamIpAddrSlot1Port1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpAddrSlot1Port1.setStatus("current")
_SonusBparamIpMaskSlot1Port1_Type = IpAddress
_SonusBparamIpMaskSlot1Port1_Object = MibTableColumn
sonusBparamIpMaskSlot1Port1 = _SonusBparamIpMaskSlot1Port1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 9),
    _SonusBparamIpMaskSlot1Port1_Type()
)
sonusBparamIpMaskSlot1Port1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpMaskSlot1Port1.setStatus("current")
_SonusBparamIpGatewaySlot1Port1_Type = IpAddress
_SonusBparamIpGatewaySlot1Port1_Object = MibTableColumn
sonusBparamIpGatewaySlot1Port1 = _SonusBparamIpGatewaySlot1Port1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 10),
    _SonusBparamIpGatewaySlot1Port1_Type()
)
sonusBparamIpGatewaySlot1Port1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpGatewaySlot1Port1.setStatus("current")


class _SonusBparamIfSpeedTypeSlot1Port1_Type(Integer32):
    """Custom type sonusBparamIfSpeedTypeSlot1Port1 based on Integer32"""
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
        *(("autoNegotiate", 1),
          ("fullDuplex10", 4),
          ("fullDuplex100", 2),
          ("halfDuplex10", 5),
          ("halfDuplex100", 3))
    )


_SonusBparamIfSpeedTypeSlot1Port1_Type.__name__ = "Integer32"
_SonusBparamIfSpeedTypeSlot1Port1_Object = MibTableColumn
sonusBparamIfSpeedTypeSlot1Port1 = _SonusBparamIfSpeedTypeSlot1Port1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 11),
    _SonusBparamIfSpeedTypeSlot1Port1_Type()
)
sonusBparamIfSpeedTypeSlot1Port1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIfSpeedTypeSlot1Port1.setStatus("current")
_SonusBparamIpAddrSlot1Port2_Type = IpAddress
_SonusBparamIpAddrSlot1Port2_Object = MibTableColumn
sonusBparamIpAddrSlot1Port2 = _SonusBparamIpAddrSlot1Port2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 12),
    _SonusBparamIpAddrSlot1Port2_Type()
)
sonusBparamIpAddrSlot1Port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpAddrSlot1Port2.setStatus("current")
_SonusBparamIpMaskSlot1Port2_Type = IpAddress
_SonusBparamIpMaskSlot1Port2_Object = MibTableColumn
sonusBparamIpMaskSlot1Port2 = _SonusBparamIpMaskSlot1Port2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 13),
    _SonusBparamIpMaskSlot1Port2_Type()
)
sonusBparamIpMaskSlot1Port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpMaskSlot1Port2.setStatus("current")
_SonusBparamIpGatewaySlot1Port2_Type = IpAddress
_SonusBparamIpGatewaySlot1Port2_Object = MibTableColumn
sonusBparamIpGatewaySlot1Port2 = _SonusBparamIpGatewaySlot1Port2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 14),
    _SonusBparamIpGatewaySlot1Port2_Type()
)
sonusBparamIpGatewaySlot1Port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpGatewaySlot1Port2.setStatus("current")


class _SonusBparamIfSpeedTypeSlot1Port2_Type(Integer32):
    """Custom type sonusBparamIfSpeedTypeSlot1Port2 based on Integer32"""
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
        *(("autoNegotiate", 1),
          ("fullDuplex10", 4),
          ("fullDuplex100", 2),
          ("halfDuplex10", 5),
          ("halfDuplex100", 3))
    )


_SonusBparamIfSpeedTypeSlot1Port2_Type.__name__ = "Integer32"
_SonusBparamIfSpeedTypeSlot1Port2_Object = MibTableColumn
sonusBparamIfSpeedTypeSlot1Port2 = _SonusBparamIfSpeedTypeSlot1Port2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 15),
    _SonusBparamIfSpeedTypeSlot1Port2_Type()
)
sonusBparamIfSpeedTypeSlot1Port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIfSpeedTypeSlot1Port2.setStatus("current")
_SonusBparamIpAddrSlot2Port0_Type = IpAddress
_SonusBparamIpAddrSlot2Port0_Object = MibTableColumn
sonusBparamIpAddrSlot2Port0 = _SonusBparamIpAddrSlot2Port0_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 16),
    _SonusBparamIpAddrSlot2Port0_Type()
)
sonusBparamIpAddrSlot2Port0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpAddrSlot2Port0.setStatus("current")
_SonusBparamIpMaskSlot2Port0_Type = IpAddress
_SonusBparamIpMaskSlot2Port0_Object = MibTableColumn
sonusBparamIpMaskSlot2Port0 = _SonusBparamIpMaskSlot2Port0_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 17),
    _SonusBparamIpMaskSlot2Port0_Type()
)
sonusBparamIpMaskSlot2Port0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpMaskSlot2Port0.setStatus("current")
_SonusBparamIpGatewaySlot2Port0_Type = IpAddress
_SonusBparamIpGatewaySlot2Port0_Object = MibTableColumn
sonusBparamIpGatewaySlot2Port0 = _SonusBparamIpGatewaySlot2Port0_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 18),
    _SonusBparamIpGatewaySlot2Port0_Type()
)
sonusBparamIpGatewaySlot2Port0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpGatewaySlot2Port0.setStatus("current")


class _SonusBparamIfSpeedTypeSlot2Port0_Type(Integer32):
    """Custom type sonusBparamIfSpeedTypeSlot2Port0 based on Integer32"""
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
        *(("autoNegotiate", 1),
          ("fullDuplex10", 4),
          ("fullDuplex100", 2),
          ("halfDuplex10", 5),
          ("halfDuplex100", 3))
    )


_SonusBparamIfSpeedTypeSlot2Port0_Type.__name__ = "Integer32"
_SonusBparamIfSpeedTypeSlot2Port0_Object = MibTableColumn
sonusBparamIfSpeedTypeSlot2Port0 = _SonusBparamIfSpeedTypeSlot2Port0_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 19),
    _SonusBparamIfSpeedTypeSlot2Port0_Type()
)
sonusBparamIfSpeedTypeSlot2Port0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIfSpeedTypeSlot2Port0.setStatus("current")
_SonusBparamIpAddrSlot2Port1_Type = IpAddress
_SonusBparamIpAddrSlot2Port1_Object = MibTableColumn
sonusBparamIpAddrSlot2Port1 = _SonusBparamIpAddrSlot2Port1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 20),
    _SonusBparamIpAddrSlot2Port1_Type()
)
sonusBparamIpAddrSlot2Port1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpAddrSlot2Port1.setStatus("current")
_SonusBparamIpMaskSlot2Port1_Type = IpAddress
_SonusBparamIpMaskSlot2Port1_Object = MibTableColumn
sonusBparamIpMaskSlot2Port1 = _SonusBparamIpMaskSlot2Port1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 21),
    _SonusBparamIpMaskSlot2Port1_Type()
)
sonusBparamIpMaskSlot2Port1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpMaskSlot2Port1.setStatus("current")
_SonusBparamIpGatewaySlot2Port1_Type = IpAddress
_SonusBparamIpGatewaySlot2Port1_Object = MibTableColumn
sonusBparamIpGatewaySlot2Port1 = _SonusBparamIpGatewaySlot2Port1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 22),
    _SonusBparamIpGatewaySlot2Port1_Type()
)
sonusBparamIpGatewaySlot2Port1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpGatewaySlot2Port1.setStatus("current")


class _SonusBparamIfSpeedTypeSlot2Port1_Type(Integer32):
    """Custom type sonusBparamIfSpeedTypeSlot2Port1 based on Integer32"""
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
        *(("autoNegotiate", 1),
          ("fullDuplex10", 4),
          ("fullDuplex100", 2),
          ("halfDuplex10", 5),
          ("halfDuplex100", 3))
    )


_SonusBparamIfSpeedTypeSlot2Port1_Type.__name__ = "Integer32"
_SonusBparamIfSpeedTypeSlot2Port1_Object = MibTableColumn
sonusBparamIfSpeedTypeSlot2Port1 = _SonusBparamIfSpeedTypeSlot2Port1_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 23),
    _SonusBparamIfSpeedTypeSlot2Port1_Type()
)
sonusBparamIfSpeedTypeSlot2Port1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIfSpeedTypeSlot2Port1.setStatus("current")
_SonusBparamIpAddrSlot2Port2_Type = IpAddress
_SonusBparamIpAddrSlot2Port2_Object = MibTableColumn
sonusBparamIpAddrSlot2Port2 = _SonusBparamIpAddrSlot2Port2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 24),
    _SonusBparamIpAddrSlot2Port2_Type()
)
sonusBparamIpAddrSlot2Port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpAddrSlot2Port2.setStatus("current")
_SonusBparamIpMaskSlot2Port2_Type = IpAddress
_SonusBparamIpMaskSlot2Port2_Object = MibTableColumn
sonusBparamIpMaskSlot2Port2 = _SonusBparamIpMaskSlot2Port2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 25),
    _SonusBparamIpMaskSlot2Port2_Type()
)
sonusBparamIpMaskSlot2Port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpMaskSlot2Port2.setStatus("current")
_SonusBparamIpGatewaySlot2Port2_Type = IpAddress
_SonusBparamIpGatewaySlot2Port2_Object = MibTableColumn
sonusBparamIpGatewaySlot2Port2 = _SonusBparamIpGatewaySlot2Port2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 26),
    _SonusBparamIpGatewaySlot2Port2_Type()
)
sonusBparamIpGatewaySlot2Port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIpGatewaySlot2Port2.setStatus("current")


class _SonusBparamIfSpeedTypeSlot2Port2_Type(Integer32):
    """Custom type sonusBparamIfSpeedTypeSlot2Port2 based on Integer32"""
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
        *(("autoNegotiate", 1),
          ("fullDuplex10", 4),
          ("fullDuplex100", 2),
          ("halfDuplex10", 5),
          ("halfDuplex100", 3))
    )


_SonusBparamIfSpeedTypeSlot2Port2_Type.__name__ = "Integer32"
_SonusBparamIfSpeedTypeSlot2Port2_Object = MibTableColumn
sonusBparamIfSpeedTypeSlot2Port2 = _SonusBparamIfSpeedTypeSlot2Port2_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 27),
    _SonusBparamIfSpeedTypeSlot2Port2_Type()
)
sonusBparamIfSpeedTypeSlot2Port2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamIfSpeedTypeSlot2Port2.setStatus("current")


class _SonusBparamBootDelay_Type(Integer32):
    """Custom type sonusBparamBootDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_SonusBparamBootDelay_Type.__name__ = "Integer32"
_SonusBparamBootDelay_Object = MibTableColumn
sonusBparamBootDelay = _SonusBparamBootDelay_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 28),
    _SonusBparamBootDelay_Type()
)
sonusBparamBootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamBootDelay.setStatus("current")
_SonusBparamCoreState_Type = SonusAdminState
_SonusBparamCoreState_Object = MibTableColumn
sonusBparamCoreState = _SonusBparamCoreState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 29),
    _SonusBparamCoreState_Type()
)
sonusBparamCoreState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamCoreState.setStatus("current")


class _SonusBparamCoreLevel_Type(Integer32):
    """Custom type sonusBparamCoreLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("sensitive", 2))
    )


_SonusBparamCoreLevel_Type.__name__ = "Integer32"
_SonusBparamCoreLevel_Object = MibTableColumn
sonusBparamCoreLevel = _SonusBparamCoreLevel_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 30),
    _SonusBparamCoreLevel_Type()
)
sonusBparamCoreLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamCoreLevel.setStatus("current")
_SonusBparamBaudRate_Type = Integer32
_SonusBparamBaudRate_Object = MibTableColumn
sonusBparamBaudRate = _SonusBparamBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 31),
    _SonusBparamBaudRate_Type()
)
sonusBparamBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamBaudRate.setStatus("current")
_SonusBparamNfsPrimary_Type = IpAddress
_SonusBparamNfsPrimary_Object = MibTableColumn
sonusBparamNfsPrimary = _SonusBparamNfsPrimary_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 32),
    _SonusBparamNfsPrimary_Type()
)
sonusBparamNfsPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamNfsPrimary.setStatus("current")
_SonusBparamNfsSecondary_Type = IpAddress
_SonusBparamNfsSecondary_Object = MibTableColumn
sonusBparamNfsSecondary = _SonusBparamNfsSecondary_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 33),
    _SonusBparamNfsSecondary_Type()
)
sonusBparamNfsSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamNfsSecondary.setStatus("current")


class _SonusBparamNfsMountPri_Type(DisplayString):
    """Custom type sonusBparamNfsMountPri based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 31),
    )


_SonusBparamNfsMountPri_Type.__name__ = "DisplayString"
_SonusBparamNfsMountPri_Object = MibTableColumn
sonusBparamNfsMountPri = _SonusBparamNfsMountPri_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 34),
    _SonusBparamNfsMountPri_Type()
)
sonusBparamNfsMountPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamNfsMountPri.setStatus("current")


class _SonusBparamNfsMountSec_Type(DisplayString):
    """Custom type sonusBparamNfsMountSec based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 31),
    )


_SonusBparamNfsMountSec_Type.__name__ = "DisplayString"
_SonusBparamNfsMountSec_Object = MibTableColumn
sonusBparamNfsMountSec = _SonusBparamNfsMountSec_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 35),
    _SonusBparamNfsMountSec_Type()
)
sonusBparamNfsMountSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamNfsMountSec.setStatus("current")


class _SonusBparamNfsPathUpgrade_Type(DisplayString):
    """Custom type sonusBparamNfsPathUpgrade based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SonusBparamNfsPathUpgrade_Type.__name__ = "DisplayString"
_SonusBparamNfsPathUpgrade_Object = MibTableColumn
sonusBparamNfsPathUpgrade = _SonusBparamNfsPathUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 36),
    _SonusBparamNfsPathUpgrade_Type()
)
sonusBparamNfsPathUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamNfsPathUpgrade.setStatus("current")


class _SonusBparamNfsPathLoad_Type(DisplayString):
    """Custom type sonusBparamNfsPathLoad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 31),
    )


_SonusBparamNfsPathLoad_Type.__name__ = "DisplayString"
_SonusBparamNfsPathLoad_Object = MibTableColumn
sonusBparamNfsPathLoad = _SonusBparamNfsPathLoad_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 37),
    _SonusBparamNfsPathLoad_Type()
)
sonusBparamNfsPathLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamNfsPathLoad.setStatus("current")


class _SonusBparamPrimName_Type(DisplayString):
    """Custom type sonusBparamPrimName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SonusBparamPrimName_Type.__name__ = "DisplayString"
_SonusBparamPrimName_Object = MibTableColumn
sonusBparamPrimName = _SonusBparamPrimName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 38),
    _SonusBparamPrimName_Type()
)
sonusBparamPrimName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamPrimName.setStatus("current")


class _SonusBparamSecName_Type(DisplayString):
    """Custom type sonusBparamSecName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SonusBparamSecName_Type.__name__ = "DisplayString"
_SonusBparamSecName_Object = MibTableColumn
sonusBparamSecName = _SonusBparamSecName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 39),
    _SonusBparamSecName_Type()
)
sonusBparamSecName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamSecName.setStatus("current")


class _SonusBparamMasterState_Type(Integer32):
    """Custom type sonusBparamMasterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("slave", 1))
    )


_SonusBparamMasterState_Type.__name__ = "Integer32"
_SonusBparamMasterState_Object = MibTableColumn
sonusBparamMasterState = _SonusBparamMasterState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 40),
    _SonusBparamMasterState_Type()
)
sonusBparamMasterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamMasterState.setStatus("current")


class _SonusBparamParamMode_Type(Integer32):
    """Custom type sonusBparamParamMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("binaryFile", 2),
          ("defaults", 3),
          ("disabled", 1))
    )


_SonusBparamParamMode_Type.__name__ = "Integer32"
_SonusBparamParamMode_Object = MibTableColumn
sonusBparamParamMode = _SonusBparamParamMode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 41),
    _SonusBparamParamMode_Type()
)
sonusBparamParamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamParamMode.setStatus("current")


class _SonusBparamCliScript_Type(DisplayString):
    """Custom type sonusBparamCliScript based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SonusBparamCliScript_Type.__name__ = "DisplayString"
_SonusBparamCliScript_Object = MibTableColumn
sonusBparamCliScript = _SonusBparamCliScript_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 42),
    _SonusBparamCliScript_Type()
)
sonusBparamCliScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamCliScript.setStatus("current")
_SonusBparamUId_Type = Integer32
_SonusBparamUId_Object = MibTableColumn
sonusBparamUId = _SonusBparamUId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 43),
    _SonusBparamUId_Type()
)
sonusBparamUId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamUId.setStatus("current")
_SonusBparamGrpId_Type = Integer32
_SonusBparamGrpId_Object = MibTableColumn
sonusBparamGrpId = _SonusBparamGrpId_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 44),
    _SonusBparamGrpId_Type()
)
sonusBparamGrpId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamGrpId.setStatus("current")


class _SonusBparamCoreDumpLimit_Type(Integer32):
    """Custom type sonusBparamCoreDumpLimit based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SonusBparamCoreDumpLimit_Type.__name__ = "Integer32"
_SonusBparamCoreDumpLimit_Object = MibTableColumn
sonusBparamCoreDumpLimit = _SonusBparamCoreDumpLimit_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 45),
    _SonusBparamCoreDumpLimit_Type()
)
sonusBparamCoreDumpLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamCoreDumpLimit.setStatus("current")


class _SonusBparamNfsPathSoftware_Type(DisplayString):
    """Custom type sonusBparamNfsPathSoftware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SonusBparamNfsPathSoftware_Type.__name__ = "DisplayString"
_SonusBparamNfsPathSoftware_Object = MibTableColumn
sonusBparamNfsPathSoftware = _SonusBparamNfsPathSoftware_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 1, 1, 46),
    _SonusBparamNfsPathSoftware_Type()
)
sonusBparamNfsPathSoftware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusBparamNfsPathSoftware.setStatus("current")
_SonusFlashConfigTable_Object = MibTable
sonusFlashConfigTable = _SonusFlashConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sonusFlashConfigTable.setStatus("current")
_SonusFlashConfigEntry_Object = MibTableRow
sonusFlashConfigEntry = _SonusFlashConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 2, 1)
)
sonusFlashConfigEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusFlashAdmnShelfIndex"),
    (0, "SONUS-NODE-MIB", "sonusFlashAdmnSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusFlashConfigEntry.setStatus("current")


class _SonusFlashAdmnShelfIndex_Type(Integer32):
    """Custom type sonusFlashAdmnShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusFlashAdmnShelfIndex_Type.__name__ = "Integer32"
_SonusFlashAdmnShelfIndex_Object = MibTableColumn
sonusFlashAdmnShelfIndex = _SonusFlashAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 2, 1, 1),
    _SonusFlashAdmnShelfIndex_Type()
)
sonusFlashAdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusFlashAdmnShelfIndex.setStatus("current")


class _SonusFlashAdmnSlotIndex_Type(Integer32):
    """Custom type sonusFlashAdmnSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusFlashAdmnSlotIndex_Type.__name__ = "Integer32"
_SonusFlashAdmnSlotIndex_Object = MibTableColumn
sonusFlashAdmnSlotIndex = _SonusFlashAdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 2, 1, 2),
    _SonusFlashAdmnSlotIndex_Type()
)
sonusFlashAdmnSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusFlashAdmnSlotIndex.setStatus("current")


class _SonusFlashAdmnUpdateButton_Type(Integer32):
    """Custom type sonusFlashAdmnUpdateButton based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("update", 1)
    )


_SonusFlashAdmnUpdateButton_Type.__name__ = "Integer32"
_SonusFlashAdmnUpdateButton_Object = MibTableColumn
sonusFlashAdmnUpdateButton = _SonusFlashAdmnUpdateButton_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 2, 1, 3),
    _SonusFlashAdmnUpdateButton_Type()
)
sonusFlashAdmnUpdateButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusFlashAdmnUpdateButton.setStatus("current")
_SonusFlashStatusTable_Object = MibTable
sonusFlashStatusTable = _SonusFlashStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    sonusFlashStatusTable.setStatus("current")
_SonusFlashStatusEntry_Object = MibTableRow
sonusFlashStatusEntry = _SonusFlashStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 3, 1)
)
sonusFlashStatusEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusFlashStatShelfIndex"),
    (0, "SONUS-NODE-MIB", "sonusFlashStatSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusFlashStatusEntry.setStatus("current")


class _SonusFlashStatShelfIndex_Type(Integer32):
    """Custom type sonusFlashStatShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusFlashStatShelfIndex_Type.__name__ = "Integer32"
_SonusFlashStatShelfIndex_Object = MibTableColumn
sonusFlashStatShelfIndex = _SonusFlashStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 3, 1, 1),
    _SonusFlashStatShelfIndex_Type()
)
sonusFlashStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusFlashStatShelfIndex.setStatus("current")


class _SonusFlashStatSlotIndex_Type(Integer32):
    """Custom type sonusFlashStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SonusFlashStatSlotIndex_Type.__name__ = "Integer32"
_SonusFlashStatSlotIndex_Object = MibTableColumn
sonusFlashStatSlotIndex = _SonusFlashStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 3, 1, 2),
    _SonusFlashStatSlotIndex_Type()
)
sonusFlashStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusFlashStatSlotIndex.setStatus("current")


class _SonusFlashStatState_Type(Integer32):
    """Custom type sonusFlashStatState based on Integer32"""
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
        *(("done", 7),
          ("flashErase", 5),
          ("flashWrite", 6),
          ("idle", 1),
          ("imageComplete", 4),
          ("waitData", 3),
          ("waitReply", 2))
    )


_SonusFlashStatState_Type.__name__ = "Integer32"
_SonusFlashStatState_Object = MibTableColumn
sonusFlashStatState = _SonusFlashStatState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 3, 1, 3),
    _SonusFlashStatState_Type()
)
sonusFlashStatState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusFlashStatState.setStatus("current")


class _SonusFlashStatLastStatus_Type(Integer32):
    """Custom type sonusFlashStatLastStatus based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("badBlkType", 12),
          ("badRequest", 4),
          ("badState", 17),
          ("dataTimeout", 8),
          ("flashChecksum", 15),
          ("flashErase", 13),
          ("flashWrite", 14),
          ("imageChecksum", 11),
          ("inProgress", 3),
          ("managerNack", 6),
          ("memoryResources", 10),
          ("mgrNack", 16),
          ("msgSequence", 9),
          ("noReply", 5),
          ("success", 1),
          ("timerResources", 7),
          ("unknown", 2))
    )


_SonusFlashStatLastStatus_Type.__name__ = "Integer32"
_SonusFlashStatLastStatus_Object = MibTableColumn
sonusFlashStatLastStatus = _SonusFlashStatLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 2, 3, 1, 4),
    _SonusFlashStatLastStatus_Type()
)
sonusFlashStatLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusFlashStatLastStatus.setStatus("current")
_SonusUser_ObjectIdentity = ObjectIdentity
sonusUser = _SonusUser_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3)
)
_SonusUserList_ObjectIdentity = ObjectIdentity
sonusUserList = _SonusUserList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1)
)
_SonusUserListNextIndex_Type = Integer32
_SonusUserListNextIndex_Object = MibScalar
sonusUserListNextIndex = _SonusUserListNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 1),
    _SonusUserListNextIndex_Type()
)
sonusUserListNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUserListNextIndex.setStatus("current")
_SonusUserListTable_Object = MibTable
sonusUserListTable = _SonusUserListTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    sonusUserListTable.setStatus("current")
_SonusUserListEntry_Object = MibTableRow
sonusUserListEntry = _SonusUserListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 2, 1)
)
sonusUserListEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusUserListIndex"),
)
if mibBuilder.loadTexts:
    sonusUserListEntry.setStatus("current")


class _SonusUserListIndex_Type(Integer32):
    """Custom type sonusUserListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusUserListIndex_Type.__name__ = "Integer32"
_SonusUserListIndex_Object = MibTableColumn
sonusUserListIndex = _SonusUserListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 2, 1, 1),
    _SonusUserListIndex_Type()
)
sonusUserListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUserListIndex.setStatus("current")
_SonusUserListState_Type = SonusAdminState
_SonusUserListState_Object = MibTableColumn
sonusUserListState = _SonusUserListState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 2, 1, 2),
    _SonusUserListState_Type()
)
sonusUserListState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserListState.setStatus("current")
_SonusUserListUserName_Type = SonusName
_SonusUserListUserName_Object = MibTableColumn
sonusUserListUserName = _SonusUserListUserName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 2, 1, 3),
    _SonusUserListUserName_Type()
)
sonusUserListUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserListUserName.setStatus("current")


class _SonusUserListProfileName_Type(DisplayString):
    """Custom type sonusUserListProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_SonusUserListProfileName_Type.__name__ = "DisplayString"
_SonusUserListProfileName_Object = MibTableColumn
sonusUserListProfileName = _SonusUserListProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 2, 1, 4),
    _SonusUserListProfileName_Type()
)
sonusUserListProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserListProfileName.setStatus("current")


class _SonusUserListPasswd_Type(DisplayString):
    """Custom type sonusUserListPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_SonusUserListPasswd_Type.__name__ = "DisplayString"
_SonusUserListPasswd_Object = MibTableColumn
sonusUserListPasswd = _SonusUserListPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 2, 1, 5),
    _SonusUserListPasswd_Type()
)
sonusUserListPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserListPasswd.setStatus("current")


class _SonusUserListComment_Type(DisplayString):
    """Custom type sonusUserListComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusUserListComment_Type.__name__ = "DisplayString"
_SonusUserListComment_Object = MibTableColumn
sonusUserListComment = _SonusUserListComment_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 2, 1, 6),
    _SonusUserListComment_Type()
)
sonusUserListComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserListComment.setStatus("current")


class _SonusUserListAccess_Type(Integer32):
    """Custom type sonusUserListAccess based on Integer32"""
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
        *(("admin", 3),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_SonusUserListAccess_Type.__name__ = "Integer32"
_SonusUserListAccess_Object = MibTableColumn
sonusUserListAccess = _SonusUserListAccess_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 2, 1, 7),
    _SonusUserListAccess_Type()
)
sonusUserListAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserListAccess.setStatus("current")
_SonusUserListRowStatus_Type = RowStatus
_SonusUserListRowStatus_Object = MibTableColumn
sonusUserListRowStatus = _SonusUserListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 2, 1, 8),
    _SonusUserListRowStatus_Type()
)
sonusUserListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserListRowStatus.setStatus("current")
_SonusUserListStatusTable_Object = MibTable
sonusUserListStatusTable = _SonusUserListStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    sonusUserListStatusTable.setStatus("current")
_SonusUserListStatusEntry_Object = MibTableRow
sonusUserListStatusEntry = _SonusUserListStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 3, 1)
)
sonusUserListStatusEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusUserListStatusIndex"),
)
if mibBuilder.loadTexts:
    sonusUserListStatusEntry.setStatus("current")


class _SonusUserListStatusIndex_Type(Integer32):
    """Custom type sonusUserListStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusUserListStatusIndex_Type.__name__ = "Integer32"
_SonusUserListStatusIndex_Object = MibTableColumn
sonusUserListStatusIndex = _SonusUserListStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 3, 1, 1),
    _SonusUserListStatusIndex_Type()
)
sonusUserListStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonusUserListStatusIndex.setStatus("current")
_SonusUserListStatusLastConfigChange_Type = DateAndTime
_SonusUserListStatusLastConfigChange_Object = MibTableColumn
sonusUserListStatusLastConfigChange = _SonusUserListStatusLastConfigChange_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 1, 3, 1, 2),
    _SonusUserListStatusLastConfigChange_Type()
)
sonusUserListStatusLastConfigChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUserListStatusLastConfigChange.setStatus("current")
_SonusUserProfile_ObjectIdentity = ObjectIdentity
sonusUserProfile = _SonusUserProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2)
)
_SonusUserProfileNextIndex_Type = Integer32
_SonusUserProfileNextIndex_Object = MibScalar
sonusUserProfileNextIndex = _SonusUserProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 1),
    _SonusUserProfileNextIndex_Type()
)
sonusUserProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUserProfileNextIndex.setStatus("current")
_SonusUserProfileTable_Object = MibTable
sonusUserProfileTable = _SonusUserProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    sonusUserProfileTable.setStatus("current")
_SonusUserProfileEntry_Object = MibTableRow
sonusUserProfileEntry = _SonusUserProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1)
)
sonusUserProfileEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusUserProfileIndex"),
)
if mibBuilder.loadTexts:
    sonusUserProfileEntry.setStatus("current")


class _SonusUserProfileIndex_Type(Integer32):
    """Custom type sonusUserProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusUserProfileIndex_Type.__name__ = "Integer32"
_SonusUserProfileIndex_Object = MibTableColumn
sonusUserProfileIndex = _SonusUserProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1, 1),
    _SonusUserProfileIndex_Type()
)
sonusUserProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUserProfileIndex.setStatus("current")
_SonusUserProfileName_Type = SonusName
_SonusUserProfileName_Object = MibTableColumn
sonusUserProfileName = _SonusUserProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1, 2),
    _SonusUserProfileName_Type()
)
sonusUserProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserProfileName.setStatus("current")
_SonusUserProfileUserState_Type = SonusAdminState
_SonusUserProfileUserState_Object = MibTableColumn
sonusUserProfileUserState = _SonusUserProfileUserState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1, 3),
    _SonusUserProfileUserState_Type()
)
sonusUserProfileUserState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserProfileUserState.setStatus("current")


class _SonusUserProfileUserPasswd_Type(DisplayString):
    """Custom type sonusUserProfileUserPasswd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 16),
    )


_SonusUserProfileUserPasswd_Type.__name__ = "DisplayString"
_SonusUserProfileUserPasswd_Object = MibTableColumn
sonusUserProfileUserPasswd = _SonusUserProfileUserPasswd_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1, 4),
    _SonusUserProfileUserPasswd_Type()
)
sonusUserProfileUserPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserProfileUserPasswd.setStatus("current")


class _SonusUserProfileUserComment_Type(DisplayString):
    """Custom type sonusUserProfileUserComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusUserProfileUserComment_Type.__name__ = "DisplayString"
_SonusUserProfileUserComment_Object = MibTableColumn
sonusUserProfileUserComment = _SonusUserProfileUserComment_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1, 5),
    _SonusUserProfileUserComment_Type()
)
sonusUserProfileUserComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserProfileUserComment.setStatus("current")
_SonusUserProfileUserAccess_Type = SonusAccessLevel
_SonusUserProfileUserAccess_Object = MibTableColumn
sonusUserProfileUserAccess = _SonusUserProfileUserAccess_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1, 6),
    _SonusUserProfileUserAccess_Type()
)
sonusUserProfileUserAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserProfileUserAccess.setStatus("current")
_SonusUserProfileUserCommentState_Type = SonusAdminState
_SonusUserProfileUserCommentState_Object = MibTableColumn
sonusUserProfileUserCommentState = _SonusUserProfileUserCommentState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1, 7),
    _SonusUserProfileUserCommentState_Type()
)
sonusUserProfileUserCommentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserProfileUserCommentState.setStatus("current")
_SonusUserProfileUserPasswdState_Type = SonusAdminState
_SonusUserProfileUserPasswdState_Object = MibTableColumn
sonusUserProfileUserPasswdState = _SonusUserProfileUserPasswdState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1, 8),
    _SonusUserProfileUserPasswdState_Type()
)
sonusUserProfileUserPasswdState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserProfileUserPasswdState.setStatus("current")
_SonusUserProfileUserAccessState_Type = SonusAdminState
_SonusUserProfileUserAccessState_Object = MibTableColumn
sonusUserProfileUserAccessState = _SonusUserProfileUserAccessState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1, 9),
    _SonusUserProfileUserAccessState_Type()
)
sonusUserProfileUserAccessState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserProfileUserAccessState.setStatus("current")
_SonusUserProfileUserStateState_Type = SonusAdminState
_SonusUserProfileUserStateState_Object = MibTableColumn
sonusUserProfileUserStateState = _SonusUserProfileUserStateState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1, 10),
    _SonusUserProfileUserStateState_Type()
)
sonusUserProfileUserStateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserProfileUserStateState.setStatus("current")
_SonusUserProfileRowStatus_Type = RowStatus
_SonusUserProfileRowStatus_Object = MibTableColumn
sonusUserProfileRowStatus = _SonusUserProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 3, 2, 2, 1, 11),
    _SonusUserProfileRowStatus_Type()
)
sonusUserProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusUserProfileRowStatus.setStatus("current")
_SonusSwLoad_ObjectIdentity = ObjectIdentity
sonusSwLoad = _SonusSwLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4)
)
_SonusSwLoadTable_Object = MibTable
sonusSwLoadTable = _SonusSwLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sonusSwLoadTable.setStatus("current")
_SonusSwLoadEntry_Object = MibTableRow
sonusSwLoadEntry = _SonusSwLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 1, 1)
)
sonusSwLoadEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusSwLoadAdmnIndex"),
)
if mibBuilder.loadTexts:
    sonusSwLoadEntry.setStatus("current")


class _SonusSwLoadAdmnIndex_Type(Integer32):
    """Custom type sonusSwLoadAdmnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SonusSwLoadAdmnIndex_Type.__name__ = "Integer32"
_SonusSwLoadAdmnIndex_Object = MibTableColumn
sonusSwLoadAdmnIndex = _SonusSwLoadAdmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 1, 1, 1),
    _SonusSwLoadAdmnIndex_Type()
)
sonusSwLoadAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwLoadAdmnIndex.setStatus("current")


class _SonusSwLoadAdmnImageName_Type(DisplayString):
    """Custom type sonusSwLoadAdmnImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_SonusSwLoadAdmnImageName_Type.__name__ = "DisplayString"
_SonusSwLoadAdmnImageName_Object = MibTableColumn
sonusSwLoadAdmnImageName = _SonusSwLoadAdmnImageName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 1, 1, 2),
    _SonusSwLoadAdmnImageName_Type()
)
sonusSwLoadAdmnImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSwLoadAdmnImageName.setStatus("current")
_SonusSwLoadAdmnHwType_Type = ServerTypeID
_SonusSwLoadAdmnHwType_Object = MibTableColumn
sonusSwLoadAdmnHwType = _SonusSwLoadAdmnHwType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 1, 1, 3),
    _SonusSwLoadAdmnHwType_Type()
)
sonusSwLoadAdmnHwType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSwLoadAdmnHwType.setStatus("current")
_SonusSwLoadAdmnRowStatus_Type = RowStatus
_SonusSwLoadAdmnRowStatus_Object = MibTableColumn
sonusSwLoadAdmnRowStatus = _SonusSwLoadAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 1, 1, 4),
    _SonusSwLoadAdmnRowStatus_Type()
)
sonusSwLoadAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSwLoadAdmnRowStatus.setStatus("current")
_SonusSwLoadSpecTable_Object = MibTable
sonusSwLoadSpecTable = _SonusSwLoadSpecTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sonusSwLoadSpecTable.setStatus("current")
_SonusSwLoadSpecEntry_Object = MibTableRow
sonusSwLoadSpecEntry = _SonusSwLoadSpecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 2, 1)
)
sonusSwLoadSpecEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusSwLoadSpecAdmnShelfIndex"),
    (0, "SONUS-NODE-MIB", "sonusSwLoadSpecAdmnSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusSwLoadSpecEntry.setStatus("current")
_SonusSwLoadSpecAdmnShelfIndex_Type = Integer32
_SonusSwLoadSpecAdmnShelfIndex_Object = MibTableColumn
sonusSwLoadSpecAdmnShelfIndex = _SonusSwLoadSpecAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 2, 1, 1),
    _SonusSwLoadSpecAdmnShelfIndex_Type()
)
sonusSwLoadSpecAdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwLoadSpecAdmnShelfIndex.setStatus("current")
_SonusSwLoadSpecAdmnSlotIndex_Type = Integer32
_SonusSwLoadSpecAdmnSlotIndex_Object = MibTableColumn
sonusSwLoadSpecAdmnSlotIndex = _SonusSwLoadSpecAdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 2, 1, 2),
    _SonusSwLoadSpecAdmnSlotIndex_Type()
)
sonusSwLoadSpecAdmnSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusSwLoadSpecAdmnSlotIndex.setStatus("current")


class _SonusSwLoadSpecAdmnImageName_Type(DisplayString):
    """Custom type sonusSwLoadSpecAdmnImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SonusSwLoadSpecAdmnImageName_Type.__name__ = "DisplayString"
_SonusSwLoadSpecAdmnImageName_Object = MibTableColumn
sonusSwLoadSpecAdmnImageName = _SonusSwLoadSpecAdmnImageName_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 2, 1, 3),
    _SonusSwLoadSpecAdmnImageName_Type()
)
sonusSwLoadSpecAdmnImageName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSwLoadSpecAdmnImageName.setStatus("current")
_SonusSwLoadSpecAdmnRowStatus_Type = RowStatus
_SonusSwLoadSpecAdmnRowStatus_Object = MibTableColumn
sonusSwLoadSpecAdmnRowStatus = _SonusSwLoadSpecAdmnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 4, 2, 1, 4),
    _SonusSwLoadSpecAdmnRowStatus_Type()
)
sonusSwLoadSpecAdmnRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusSwLoadSpecAdmnRowStatus.setStatus("current")
_SonusParam_ObjectIdentity = ObjectIdentity
sonusParam = _SonusParam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5)
)
_SonusParamStatusObjects_ObjectIdentity = ObjectIdentity
sonusParamStatusObjects = _SonusParamStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1)
)
_SonusParamSaveSeqNumber_Type = Integer32
_SonusParamSaveSeqNumber_Object = MibScalar
sonusParamSaveSeqNumber = _SonusParamSaveSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 1),
    _SonusParamSaveSeqNumber_Type()
)
sonusParamSaveSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSaveSeqNumber.setStatus("current")
_SonusParamSaveTimeStart_Type = Integer32
_SonusParamSaveTimeStart_Object = MibScalar
sonusParamSaveTimeStart = _SonusParamSaveTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 2),
    _SonusParamSaveTimeStart_Type()
)
sonusParamSaveTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSaveTimeStart.setStatus("current")
_SonusParamSaveTimeStop_Type = Integer32
_SonusParamSaveTimeStop_Object = MibScalar
sonusParamSaveTimeStop = _SonusParamSaveTimeStop_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 3),
    _SonusParamSaveTimeStop_Type()
)
sonusParamSaveTimeStop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSaveTimeStop.setStatus("current")
_SonusParamSaveDuration_Type = Integer32
_SonusParamSaveDuration_Object = MibScalar
sonusParamSaveDuration = _SonusParamSaveDuration_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 4),
    _SonusParamSaveDuration_Type()
)
sonusParamSaveDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSaveDuration.setStatus("current")
_SonusParamSaveTotalBytes_Type = Integer32
_SonusParamSaveTotalBytes_Object = MibScalar
sonusParamSaveTotalBytes = _SonusParamSaveTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 5),
    _SonusParamSaveTotalBytes_Type()
)
sonusParamSaveTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSaveTotalBytes.setStatus("current")
_SonusParamSaveTotalRecords_Type = Integer32
_SonusParamSaveTotalRecords_Object = MibScalar
sonusParamSaveTotalRecords = _SonusParamSaveTotalRecords_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 6),
    _SonusParamSaveTotalRecords_Type()
)
sonusParamSaveTotalRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSaveTotalRecords.setStatus("current")


class _SonusParamSaveFilename_Type(DisplayString):
    """Custom type sonusParamSaveFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusParamSaveFilename_Type.__name__ = "DisplayString"
_SonusParamSaveFilename_Object = MibScalar
sonusParamSaveFilename = _SonusParamSaveFilename_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 7),
    _SonusParamSaveFilename_Type()
)
sonusParamSaveFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSaveFilename.setStatus("current")


class _SonusParamSaveState_Type(Integer32):
    """Custom type sonusParamSaveState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("collect", 6),
          ("done", 8),
          ("fclose", 7),
          ("fopen", 5),
          ("holdoff", 4),
          ("idle", 1),
          ("lock", 3),
          ("retry", 9),
          ("synchronize", 2))
    )


_SonusParamSaveState_Type.__name__ = "Integer32"
_SonusParamSaveState_Object = MibScalar
sonusParamSaveState = _SonusParamSaveState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 8),
    _SonusParamSaveState_Type()
)
sonusParamSaveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSaveState.setStatus("current")
_SonusParamLoadServer_Type = IpAddress
_SonusParamLoadServer_Object = MibScalar
sonusParamLoadServer = _SonusParamLoadServer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 9),
    _SonusParamLoadServer_Type()
)
sonusParamLoadServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamLoadServer.setStatus("current")


class _SonusParamLoadFileType_Type(Integer32):
    """Custom type sonusParamLoadFileType based on Integer32"""
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
        *(("backup", 2),
          ("none", 4),
          ("primary", 1),
          ("temporary", 3))
    )


_SonusParamLoadFileType_Type.__name__ = "Integer32"
_SonusParamLoadFileType_Object = MibScalar
sonusParamLoadFileType = _SonusParamLoadFileType_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 10),
    _SonusParamLoadFileType_Type()
)
sonusParamLoadFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamLoadFileType.setStatus("current")


class _SonusParamLoadStatus_Type(Integer32):
    """Custom type sonusParamLoadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("defaults", 1),
          ("paramError", 3),
          ("success", 2))
    )


_SonusParamLoadStatus_Type.__name__ = "Integer32"
_SonusParamLoadStatus_Object = MibScalar
sonusParamLoadStatus = _SonusParamLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 11),
    _SonusParamLoadStatus_Type()
)
sonusParamLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamLoadStatus.setStatus("current")
_SonusParamLoadSeqNumber_Type = Integer32
_SonusParamLoadSeqNumber_Object = MibScalar
sonusParamLoadSeqNumber = _SonusParamLoadSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 12),
    _SonusParamLoadSeqNumber_Type()
)
sonusParamLoadSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamLoadSeqNumber.setStatus("current")
_SonusParamLoadTotalRecords_Type = Integer32
_SonusParamLoadTotalRecords_Object = MibScalar
sonusParamLoadTotalRecords = _SonusParamLoadTotalRecords_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 13),
    _SonusParamLoadTotalRecords_Type()
)
sonusParamLoadTotalRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamLoadTotalRecords.setStatus("current")
_SonusParamLoadTotalBytes_Type = Integer32
_SonusParamLoadTotalBytes_Object = MibScalar
sonusParamLoadTotalBytes = _SonusParamLoadTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 14),
    _SonusParamLoadTotalBytes_Type()
)
sonusParamLoadTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamLoadTotalBytes.setStatus("current")
_SonusParamLoadDuration_Type = Integer32
_SonusParamLoadDuration_Object = MibScalar
sonusParamLoadDuration = _SonusParamLoadDuration_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 15),
    _SonusParamLoadDuration_Type()
)
sonusParamLoadDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamLoadDuration.setStatus("current")


class _SonusParamLoadSerialNum_Type(DisplayString):
    """Custom type sonusParamLoadSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_SonusParamLoadSerialNum_Type.__name__ = "DisplayString"
_SonusParamLoadSerialNum_Object = MibScalar
sonusParamLoadSerialNum = _SonusParamLoadSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 16),
    _SonusParamLoadSerialNum_Type()
)
sonusParamLoadSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamLoadSerialNum.setStatus("current")


class _SonusParamSavePrimarySrvrState_Type(Integer32):
    """Custom type sonusParamSavePrimarySrvrState based on Integer32"""
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
        *(("ahead", 6),
          ("behind", 4),
          ("current", 5),
          ("failed", 2),
          ("failing", 3),
          ("unknown", 1))
    )


_SonusParamSavePrimarySrvrState_Type.__name__ = "Integer32"
_SonusParamSavePrimarySrvrState_Object = MibScalar
sonusParamSavePrimarySrvrState = _SonusParamSavePrimarySrvrState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 17),
    _SonusParamSavePrimarySrvrState_Type()
)
sonusParamSavePrimarySrvrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSavePrimarySrvrState.setStatus("current")


class _SonusParamSavePrimarySrvrReason_Type(Integer32):
    """Custom type sonusParamSavePrimarySrvrReason based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("close", 9),
          ("create", 2),
          ("flush", 7),
          ("fopen", 3),
          ("header", 4),
          ("memory", 11),
          ("move", 10),
          ("nfs", 6),
          ("none", 12),
          ("success", 1),
          ("timer", 5),
          ("write", 8))
    )


_SonusParamSavePrimarySrvrReason_Type.__name__ = "Integer32"
_SonusParamSavePrimarySrvrReason_Object = MibScalar
sonusParamSavePrimarySrvrReason = _SonusParamSavePrimarySrvrReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 18),
    _SonusParamSavePrimarySrvrReason_Type()
)
sonusParamSavePrimarySrvrReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSavePrimarySrvrReason.setStatus("current")


class _SonusParamSaveSecondarySrvrState_Type(Integer32):
    """Custom type sonusParamSaveSecondarySrvrState based on Integer32"""
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
        *(("ahead", 6),
          ("behind", 4),
          ("current", 5),
          ("failed", 2),
          ("failing", 3),
          ("unknown", 1))
    )


_SonusParamSaveSecondarySrvrState_Type.__name__ = "Integer32"
_SonusParamSaveSecondarySrvrState_Object = MibScalar
sonusParamSaveSecondarySrvrState = _SonusParamSaveSecondarySrvrState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 19),
    _SonusParamSaveSecondarySrvrState_Type()
)
sonusParamSaveSecondarySrvrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSaveSecondarySrvrState.setStatus("current")


class _SonusParamSaveSecondarySrvrReason_Type(Integer32):
    """Custom type sonusParamSaveSecondarySrvrReason based on Integer32"""
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
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("close", 9),
          ("create", 2),
          ("flush", 7),
          ("fopen", 3),
          ("header", 4),
          ("memory", 11),
          ("move", 10),
          ("nfs", 6),
          ("none", 12),
          ("success", 1),
          ("timer", 5),
          ("write", 8))
    )


_SonusParamSaveSecondarySrvrReason_Type.__name__ = "Integer32"
_SonusParamSaveSecondarySrvrReason_Object = MibScalar
sonusParamSaveSecondarySrvrReason = _SonusParamSaveSecondarySrvrReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 20),
    _SonusParamSaveSecondarySrvrReason_Type()
)
sonusParamSaveSecondarySrvrReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamSaveSecondarySrvrReason.setStatus("current")
_SonusParamLastSaveTime_Type = DateAndTime
_SonusParamLastSaveTime_Object = MibScalar
sonusParamLastSaveTime = _SonusParamLastSaveTime_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 1, 21),
    _SonusParamLastSaveTime_Type()
)
sonusParamLastSaveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusParamLastSaveTime.setStatus("current")
_SonusParamAdminObject_ObjectIdentity = ObjectIdentity
sonusParamAdminObject = _SonusParamAdminObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 2)
)


class _SonusParamAdmnMaxIncrPifs_Type(Integer32):
    """Custom type sonusParamAdmnMaxIncrPifs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_SonusParamAdmnMaxIncrPifs_Type.__name__ = "Integer32"
_SonusParamAdmnMaxIncrPifs_Object = MibScalar
sonusParamAdmnMaxIncrPifs = _SonusParamAdmnMaxIncrPifs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 5, 2, 1),
    _SonusParamAdmnMaxIncrPifs_Type()
)
sonusParamAdmnMaxIncrPifs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusParamAdmnMaxIncrPifs.setStatus("current")
_SonusNfs_ObjectIdentity = ObjectIdentity
sonusNfs = _SonusNfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6)
)
_SonusNfsAdmnTable_Object = MibTable
sonusNfsAdmnTable = _SonusNfsAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    sonusNfsAdmnTable.setStatus("current")
_SonusNfsAdmnEntry_Object = MibTableRow
sonusNfsAdmnEntry = _SonusNfsAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 1, 1)
)
sonusNfsAdmnEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusNfsAdmnShelfIndex"),
    (0, "SONUS-NODE-MIB", "sonusNfsAdmnSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusNfsAdmnEntry.setStatus("current")


class _SonusNfsAdmnShelfIndex_Type(Integer32):
    """Custom type sonusNfsAdmnShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNfsAdmnShelfIndex_Type.__name__ = "Integer32"
_SonusNfsAdmnShelfIndex_Object = MibTableColumn
sonusNfsAdmnShelfIndex = _SonusNfsAdmnShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 1, 1, 1),
    _SonusNfsAdmnShelfIndex_Type()
)
sonusNfsAdmnShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsAdmnShelfIndex.setStatus("current")


class _SonusNfsAdmnSlotIndex_Type(Integer32):
    """Custom type sonusNfsAdmnSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SonusNfsAdmnSlotIndex_Type.__name__ = "Integer32"
_SonusNfsAdmnSlotIndex_Object = MibTableColumn
sonusNfsAdmnSlotIndex = _SonusNfsAdmnSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 1, 1, 2),
    _SonusNfsAdmnSlotIndex_Type()
)
sonusNfsAdmnSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsAdmnSlotIndex.setStatus("current")


class _SonusNfsAdmnMountServer_Type(Integer32):
    """Custom type sonusNfsAdmnMountServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_SonusNfsAdmnMountServer_Type.__name__ = "Integer32"
_SonusNfsAdmnMountServer_Object = MibTableColumn
sonusNfsAdmnMountServer = _SonusNfsAdmnMountServer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 1, 1, 3),
    _SonusNfsAdmnMountServer_Type()
)
sonusNfsAdmnMountServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNfsAdmnMountServer.setStatus("current")


class _SonusNfsAdmnUnmountServer_Type(Integer32):
    """Custom type sonusNfsAdmnUnmountServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("standby", 2))
    )


_SonusNfsAdmnUnmountServer_Type.__name__ = "Integer32"
_SonusNfsAdmnUnmountServer_Object = MibTableColumn
sonusNfsAdmnUnmountServer = _SonusNfsAdmnUnmountServer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 1, 1, 4),
    _SonusNfsAdmnUnmountServer_Type()
)
sonusNfsAdmnUnmountServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNfsAdmnUnmountServer.setStatus("current")


class _SonusNfsAdmnToggleActiveServer_Type(Integer32):
    """Custom type sonusNfsAdmnToggleActiveServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("toggle", 2))
    )


_SonusNfsAdmnToggleActiveServer_Type.__name__ = "Integer32"
_SonusNfsAdmnToggleActiveServer_Object = MibTableColumn
sonusNfsAdmnToggleActiveServer = _SonusNfsAdmnToggleActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 1, 1, 5),
    _SonusNfsAdmnToggleActiveServer_Type()
)
sonusNfsAdmnToggleActiveServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNfsAdmnToggleActiveServer.setStatus("current")


class _SonusNfsAdmnSetWritable_Type(Integer32):
    """Custom type sonusNfsAdmnSetWritable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_SonusNfsAdmnSetWritable_Type.__name__ = "Integer32"
_SonusNfsAdmnSetWritable_Object = MibTableColumn
sonusNfsAdmnSetWritable = _SonusNfsAdmnSetWritable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 1, 1, 6),
    _SonusNfsAdmnSetWritable_Type()
)
sonusNfsAdmnSetWritable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sonusNfsAdmnSetWritable.setStatus("current")
_SonusNfsStatTable_Object = MibTable
sonusNfsStatTable = _SonusNfsStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    sonusNfsStatTable.setStatus("current")
_SonusNfsStatEntry_Object = MibTableRow
sonusNfsStatEntry = _SonusNfsStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1)
)
sonusNfsStatEntry.setIndexNames(
    (0, "SONUS-NODE-MIB", "sonusNfsStatShelfIndex"),
    (0, "SONUS-NODE-MIB", "sonusNfsStatSlotIndex"),
)
if mibBuilder.loadTexts:
    sonusNfsStatEntry.setStatus("current")


class _SonusNfsStatShelfIndex_Type(Integer32):
    """Custom type sonusNfsStatShelfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SonusNfsStatShelfIndex_Type.__name__ = "Integer32"
_SonusNfsStatShelfIndex_Object = MibTableColumn
sonusNfsStatShelfIndex = _SonusNfsStatShelfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 1),
    _SonusNfsStatShelfIndex_Type()
)
sonusNfsStatShelfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatShelfIndex.setStatus("current")


class _SonusNfsStatSlotIndex_Type(Integer32):
    """Custom type sonusNfsStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SonusNfsStatSlotIndex_Type.__name__ = "Integer32"
_SonusNfsStatSlotIndex_Object = MibTableColumn
sonusNfsStatSlotIndex = _SonusNfsStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 2),
    _SonusNfsStatSlotIndex_Type()
)
sonusNfsStatSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatSlotIndex.setStatus("current")


class _SonusNfsStatPrimaryStatus_Type(Integer32):
    """Custom type sonusNfsStatPrimaryStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("failed", 7),
          ("invalid", 8),
          ("mounted", 1),
          ("mounting", 2),
          ("readOnly", 5),
          ("testing", 6),
          ("unmounted", 3),
          ("unmounting", 4))
    )


_SonusNfsStatPrimaryStatus_Type.__name__ = "Integer32"
_SonusNfsStatPrimaryStatus_Object = MibTableColumn
sonusNfsStatPrimaryStatus = _SonusNfsStatPrimaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 7),
    _SonusNfsStatPrimaryStatus_Type()
)
sonusNfsStatPrimaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatPrimaryStatus.setStatus("current")


class _SonusNfsStatSecondaryStatus_Type(Integer32):
    """Custom type sonusNfsStatSecondaryStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("failed", 7),
          ("invalid", 8),
          ("mounted", 1),
          ("mounting", 2),
          ("readOnly", 5),
          ("testing", 6),
          ("unmounted", 3),
          ("unmounting", 4))
    )


_SonusNfsStatSecondaryStatus_Type.__name__ = "Integer32"
_SonusNfsStatSecondaryStatus_Object = MibTableColumn
sonusNfsStatSecondaryStatus = _SonusNfsStatSecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 8),
    _SonusNfsStatSecondaryStatus_Type()
)
sonusNfsStatSecondaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatSecondaryStatus.setStatus("current")


class _SonusNfsStatActiveServer_Type(Integer32):
    """Custom type sonusNfsStatActiveServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_SonusNfsStatActiveServer_Type.__name__ = "Integer32"
_SonusNfsStatActiveServer_Object = MibTableColumn
sonusNfsStatActiveServer = _SonusNfsStatActiveServer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 9),
    _SonusNfsStatActiveServer_Type()
)
sonusNfsStatActiveServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatActiveServer.setStatus("current")


class _SonusNfsStatStandbyServer_Type(Integer32):
    """Custom type sonusNfsStatStandbyServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_SonusNfsStatStandbyServer_Type.__name__ = "Integer32"
_SonusNfsStatStandbyServer_Object = MibTableColumn
sonusNfsStatStandbyServer = _SonusNfsStatStandbyServer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 10),
    _SonusNfsStatStandbyServer_Type()
)
sonusNfsStatStandbyServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatStandbyServer.setStatus("current")
_SonusNfsStatPrimaryIP_Type = IpAddress
_SonusNfsStatPrimaryIP_Object = MibTableColumn
sonusNfsStatPrimaryIP = _SonusNfsStatPrimaryIP_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 11),
    _SonusNfsStatPrimaryIP_Type()
)
sonusNfsStatPrimaryIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatPrimaryIP.setStatus("current")
_SonusNfsStatSecondaryIP_Type = IpAddress
_SonusNfsStatSecondaryIP_Object = MibTableColumn
sonusNfsStatSecondaryIP = _SonusNfsStatSecondaryIP_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 12),
    _SonusNfsStatSecondaryIP_Type()
)
sonusNfsStatSecondaryIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatSecondaryIP.setStatus("current")


class _SonusNfsStatPrimaryMount_Type(DisplayString):
    """Custom type sonusNfsStatPrimaryMount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_SonusNfsStatPrimaryMount_Type.__name__ = "DisplayString"
_SonusNfsStatPrimaryMount_Object = MibTableColumn
sonusNfsStatPrimaryMount = _SonusNfsStatPrimaryMount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 13),
    _SonusNfsStatPrimaryMount_Type()
)
sonusNfsStatPrimaryMount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatPrimaryMount.setStatus("current")


class _SonusNfsStatSecondaryMount_Type(DisplayString):
    """Custom type sonusNfsStatSecondaryMount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_SonusNfsStatSecondaryMount_Type.__name__ = "DisplayString"
_SonusNfsStatSecondaryMount_Object = MibTableColumn
sonusNfsStatSecondaryMount = _SonusNfsStatSecondaryMount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 14),
    _SonusNfsStatSecondaryMount_Type()
)
sonusNfsStatSecondaryMount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatSecondaryMount.setStatus("current")


class _SonusNfsStatPrimaryLastError_Type(Integer32):
    """Custom type sonusNfsStatPrimaryLastError based on Integer32"""
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
        *(("badVolumeStructure", 2),
          ("nfsTimeout", 8),
          ("noAccess", 10),
          ("none", 1),
          ("other", 11),
          ("quotaExceeded", 6),
          ("rpcCanNotSend", 9),
          ("serverHardError", 5),
          ("staleNfsHandle", 7),
          ("tooManyFiles", 3),
          ("volumeFull", 4))
    )


_SonusNfsStatPrimaryLastError_Type.__name__ = "Integer32"
_SonusNfsStatPrimaryLastError_Object = MibTableColumn
sonusNfsStatPrimaryLastError = _SonusNfsStatPrimaryLastError_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 15),
    _SonusNfsStatPrimaryLastError_Type()
)
sonusNfsStatPrimaryLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatPrimaryLastError.setStatus("current")


class _SonusNfsStatSecondaryLastError_Type(Integer32):
    """Custom type sonusNfsStatSecondaryLastError based on Integer32"""
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
        *(("badVolumeStructure", 2),
          ("nfsTimeout", 8),
          ("noAccess", 10),
          ("none", 1),
          ("other", 11),
          ("quotaExceeded", 6),
          ("rpcCanNotSend", 9),
          ("serverHardError", 5),
          ("staleNfsHandle", 7),
          ("tooManyFiles", 3),
          ("volumeFull", 4))
    )


_SonusNfsStatSecondaryLastError_Type.__name__ = "Integer32"
_SonusNfsStatSecondaryLastError_Object = MibTableColumn
sonusNfsStatSecondaryLastError = _SonusNfsStatSecondaryLastError_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 1, 6, 2, 1, 16),
    _SonusNfsStatSecondaryLastError_Type()
)
sonusNfsStatSecondaryLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsStatSecondaryLastError.setStatus("current")
_SonusNodeMIBNotifications_ObjectIdentity = ObjectIdentity
sonusNodeMIBNotifications = _SonusNodeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2)
)
_SonusNodeMIBNotificationsPrefix_ObjectIdentity = ObjectIdentity
sonusNodeMIBNotificationsPrefix = _SonusNodeMIBNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0)
)
_SonusNodeMIBNotificationsObjects_ObjectIdentity = ObjectIdentity
sonusNodeMIBNotificationsObjects = _SonusNodeMIBNotificationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 1)
)


class _SonusNfsServer_Type(Integer32):
    """Custom type sonusNfsServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_SonusNfsServer_Type.__name__ = "Integer32"
_SonusNfsServer_Object = MibScalar
sonusNfsServer = _SonusNfsServer_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 1, 1),
    _SonusNfsServer_Type()
)
sonusNfsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsServer.setStatus("current")


class _SonusNfsRole_Type(Integer32):
    """Custom type sonusNfsRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_SonusNfsRole_Type.__name__ = "Integer32"
_SonusNfsRole_Object = MibScalar
sonusNfsRole = _SonusNfsRole_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 1, 2),
    _SonusNfsRole_Type()
)
sonusNfsRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsRole.setStatus("current")
_SonusNfsServerIp_Type = IpAddress
_SonusNfsServerIp_Object = MibScalar
sonusNfsServerIp = _SonusNfsServerIp_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 1, 3),
    _SonusNfsServerIp_Type()
)
sonusNfsServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsServerIp.setStatus("current")


class _SonusNfsServerMount_Type(DisplayString):
    """Custom type sonusNfsServerMount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_SonusNfsServerMount_Type.__name__ = "DisplayString"
_SonusNfsServerMount_Object = MibScalar
sonusNfsServerMount = _SonusNfsServerMount_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 1, 4),
    _SonusNfsServerMount_Type()
)
sonusNfsServerMount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsServerMount.setStatus("current")


class _SonusNfsReason_Type(Integer32):
    """Custom type sonusNfsReason based on Integer32"""
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
        *(("adminOperation", 1),
          ("serverFailure", 2),
          ("serverNotWritable", 3),
          ("serverRecovery", 4))
    )


_SonusNfsReason_Type.__name__ = "Integer32"
_SonusNfsReason_Object = MibScalar
sonusNfsReason = _SonusNfsReason_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 1, 5),
    _SonusNfsReason_Type()
)
sonusNfsReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsReason.setStatus("current")


class _SonusNfsErrorCode_Type(Integer32):
    """Custom type sonusNfsErrorCode based on Integer32"""
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
        *(("badVolumeStructure", 2),
          ("nfsTimeout", 8),
          ("noAccess", 10),
          ("none", 1),
          ("other", 11),
          ("quotaExceeded", 6),
          ("rpcCanNotSend", 9),
          ("serverHardError", 5),
          ("staleNfsHandle", 7),
          ("tooManyFiles", 3),
          ("volumeFull", 4))
    )


_SonusNfsErrorCode_Type.__name__ = "Integer32"
_SonusNfsErrorCode_Object = MibScalar
sonusNfsErrorCode = _SonusNfsErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 1, 6),
    _SonusNfsErrorCode_Type()
)
sonusNfsErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusNfsErrorCode.setStatus("current")

# Managed Objects groups


# Notification objects

sonusNodeShelfPowerA48VdcNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 1)
)
sonusNodeShelfPowerA48VdcNormalNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeShelfPowerA48VdcNormalNotification.setStatus(
        "current"
    )

sonusNodeShelfPowerB48VdcNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 2)
)
sonusNodeShelfPowerB48VdcNormalNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeShelfPowerB48VdcNormalNotification.setStatus(
        "current"
    )

sonusNodeShelfPowerA48VdcFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 3)
)
sonusNodeShelfPowerA48VdcFailureNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeShelfPowerA48VdcFailureNotification.setStatus(
        "current"
    )

sonusNodeShelfPowerB48VdcFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 4)
)
sonusNodeShelfPowerB48VdcFailureNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeShelfPowerB48VdcFailureNotification.setStatus(
        "current"
    )

sonusNodeShelfFanTrayFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 5)
)
sonusNodeShelfFanTrayFailureNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeShelfFanTrayFailureNotification.setStatus(
        "current"
    )

sonusNodeShelfFanTrayOperationalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 6)
)
sonusNodeShelfFanTrayOperationalNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeShelfFanTrayOperationalNotification.setStatus(
        "current"
    )

sonusNodeShelfFanTrayRemovedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 7)
)
sonusNodeShelfFanTrayRemovedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeShelfFanTrayRemovedNotification.setStatus(
        "current"
    )

sonusNodeShelfFanTrayPresentNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 8)
)
sonusNodeShelfFanTrayPresentNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeShelfFanTrayPresentNotification.setStatus(
        "current"
    )

sonusNodeShelfIntakeTempWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 9)
)
sonusNodeShelfIntakeTempWarningNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeShelfIntakeTempWarningNotification.setStatus(
        "current"
    )

sonusNodeServerTempWarningNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 10)
)
sonusNodeServerTempWarningNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerTempWarningNotification.setStatus(
        "current"
    )

sonusNodeServerTempFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 11)
)
sonusNodeServerTempFailureNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerTempFailureNotification.setStatus(
        "current"
    )

sonusNodeServerTempNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 12)
)
sonusNodeServerTempNormalNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerTempNormalNotification.setStatus(
        "current"
    )

sonusNodeServerInsertedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 13)
)
sonusNodeServerInsertedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerInsertedNotification.setStatus(
        "current"
    )

sonusNodeServerRemovedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 14)
)
sonusNodeServerRemovedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerRemovedNotification.setStatus(
        "current"
    )

sonusNodeServerResetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 15)
)
sonusNodeServerResetNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerResetNotification.setStatus(
        "current"
    )

sonusNodeServerOperationalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 16)
)
sonusNodeServerOperationalNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerOperationalNotification.setStatus(
        "current"
    )

sonusNodeServerPowerFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 17)
)
sonusNodeServerPowerFailureNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerPowerFailureNotification.setStatus(
        "current"
    )

sonusNodeServerSoftwareFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 18)
)
sonusNodeServerSoftwareFailureNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerSoftwareFailureNotification.setStatus(
        "current"
    )

sonusNodeServerHardwareFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 19)
)
sonusNodeServerHardwareFailureNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerHardwareFailureNotification.setStatus(
        "current"
    )

sonusNodeAdapterInsertedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 20)
)
sonusNodeAdapterInsertedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeAdapterInsertedNotification.setStatus(
        "current"
    )

sonusNodeAdapterRemovedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 21)
)
sonusNodeAdapterRemovedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeAdapterRemovedNotification.setStatus(
        "current"
    )

sonusNodeMtaInsertedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 22)
)
sonusNodeMtaInsertedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeMtaInsertedNotification.setStatus(
        "current"
    )

sonusNodeMtaRemovedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 23)
)
sonusNodeMtaRemovedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeMtaRemovedNotification.setStatus(
        "current"
    )

sonusNodeEthernetActiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 24)
)
sonusNodeEthernetActiveNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeEthernetActiveNotification.setStatus(
        "current"
    )

sonusNodeEthernetInactiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 25)
)
sonusNodeEthernetInactiveNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeEthernetInactiveNotification.setStatus(
        "current"
    )

sonusNodeEthernetDegradedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 26)
)
sonusNodeEthernetDegradedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusPortIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeEthernetDegradedNotification.setStatus(
        "current"
    )

sonusNodeBootNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 27)
)
sonusNodeBootNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeBootNotification.setStatus(
        "current"
    )

sonusNodeSlaveShelfBootNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 28)
)
sonusNodeSlaveShelfBootNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeSlaveShelfBootNotification.setStatus(
        "current"
    )

sonusNodeNfsServerSwitchoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 29)
)
sonusNodeNfsServerSwitchoverNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-NODE-MIB", "sonusNfsServer"),
        ("SONUS-NODE-MIB", "sonusNfsServerIp"),
        ("SONUS-NODE-MIB", "sonusNfsServerMount"),
        ("SONUS-NODE-MIB", "sonusNfsReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeNfsServerSwitchoverNotification.setStatus(
        "current"
    )

sonusNodeNfsServerOutOfServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 30)
)
sonusNodeNfsServerOutOfServiceNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-NODE-MIB", "sonusNfsServer"),
        ("SONUS-NODE-MIB", "sonusNfsServerIp"),
        ("SONUS-NODE-MIB", "sonusNfsServerMount"),
        ("SONUS-NODE-MIB", "sonusNfsReason"),
        ("SONUS-NODE-MIB", "sonusNfsErrorCode"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeNfsServerOutOfServiceNotification.setStatus(
        "current"
    )

sonusNodeNfsServerInServiceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 31)
)
sonusNodeNfsServerInServiceNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-NODE-MIB", "sonusNfsServer"),
        ("SONUS-NODE-MIB", "sonusNfsServerIp"),
        ("SONUS-NODE-MIB", "sonusNfsServerMount"),
        ("SONUS-NODE-MIB", "sonusNfsReason"),
        ("SONUS-NODE-MIB", "sonusNfsRole"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeNfsServerInServiceNotification.setStatus(
        "current"
    )

sonusNodeNfsServerNotWritableNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 32)
)
sonusNodeNfsServerNotWritableNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-NODE-MIB", "sonusNfsServer"),
        ("SONUS-NODE-MIB", "sonusNfsServerIp"),
        ("SONUS-NODE-MIB", "sonusNfsServerMount"),
        ("SONUS-NODE-MIB", "sonusNfsErrorCode"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeNfsServerNotWritableNotification.setStatus(
        "current"
    )

sonusNodeServerDisabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 33)
)
sonusNodeServerDisabledNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerDisabledNotification.setStatus(
        "current"
    )

sonusNodeServerEnabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 34)
)
sonusNodeServerEnabledNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerEnabledNotification.setStatus(
        "current"
    )

sonusNodeServerDeletedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 35)
)
sonusNodeServerDeletedNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeServerDeletedNotification.setStatus(
        "current"
    )

sonusParamBackupLoadNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 36)
)
sonusParamBackupLoadNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusParamBackupLoadNotification.setStatus(
        "current"
    )

sonusParamCorruptionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 37)
)
sonusParamCorruptionNotification.setObjects(
      *(("SONUS-NODE-MIB", "sonusParamLoadFileType"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusParamCorruptionNotification.setStatus(
        "current"
    )

sonusNodeAdapterMissingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 38)
)
sonusNodeAdapterMissingNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeAdapterMissingNotification.setStatus(
        "current"
    )

sonusNodeAdapterFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 39)
)
sonusNodeAdapterFailureNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeAdapterFailureNotification.setStatus(
        "current"
    )

sonusNodeSlotResetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 40)
)
sonusNodeSlotResetNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeSlotResetNotification.setStatus(
        "current"
    )

sonusNodeParamWriteCompleteNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 41)
)
sonusNodeParamWriteCompleteNotification.setObjects(
      *(("SONUS-NODE-MIB", "sonusParamSaveFilename"),
        ("SONUS-NODE-MIB", "sonusParamSaveSeqNumber"),
        ("SONUS-NODE-MIB", "sonusParamLastSaveTime"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeParamWriteCompleteNotification.setStatus(
        "current"
    )

sonusNodeParamWriteErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 42)
)
sonusNodeParamWriteErrorNotification.setObjects(
      *(("SONUS-NODE-MIB", "sonusParamSavePrimarySrvrReason"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeParamWriteErrorNotification.setStatus(
        "current"
    )

sonusNodeBootMnsActiveNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 43)
)
sonusNodeBootMnsActiveNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusSlotIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeBootMnsActiveNotification.setStatus(
        "current"
    )

sonusNodeShelfIntakeTempNormalNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 2879, 2, 1, 1, 2, 0, 44)
)
sonusNodeShelfIntakeTempNormalNotification.setObjects(
      *(("SONUS-COMMON-MIB", "sonusShelfIndex"),
        ("SONUS-COMMON-MIB", "sonusEventDescription"),
        ("SONUS-COMMON-MIB", "sonusEventClass"),
        ("SONUS-COMMON-MIB", "sonusEventLevel"))
)
if mibBuilder.loadTexts:
    sonusNodeShelfIntakeTempNormalNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-NODE-MIB",
    **{"sonusNodeMIB": sonusNodeMIB,
       "sonusNodeMIBObjects": sonusNodeMIBObjects,
       "sonusNode": sonusNode,
       "sonusNodeAdmnObjects": sonusNodeAdmnObjects,
       "sonusNodeAdmnShelves": sonusNodeAdmnShelves,
       "sonusNodeAdmnTelnetLogin": sonusNodeAdmnTelnetLogin,
       "sonusNodeStatusObjects": sonusNodeStatusObjects,
       "sonusNodeStatShelvesPresent": sonusNodeStatShelvesPresent,
       "sonusNodeStatNextIfIndex": sonusNodeStatNextIfIndex,
       "sonusNodeStatMgmtStatus": sonusNodeStatMgmtStatus,
       "sonusNodeShelfAdmnTable": sonusNodeShelfAdmnTable,
       "sonusNodeShelfAdmnEntry": sonusNodeShelfAdmnEntry,
       "sonusNodeShelfAdmnIndex": sonusNodeShelfAdmnIndex,
       "sonusNodeShelfAdmnState": sonusNodeShelfAdmnState,
       "sonusNodeShelfAdmnIpaddr1": sonusNodeShelfAdmnIpaddr1,
       "sonusNodeShelfAdmnIpaddr2": sonusNodeShelfAdmnIpaddr2,
       "sonusNodeShelfAdmn48VdcAState": sonusNodeShelfAdmn48VdcAState,
       "sonusNodeShelfAdmn48VdcBState": sonusNodeShelfAdmn48VdcBState,
       "sonusNodeShelfAdmnStatus": sonusNodeShelfAdmnStatus,
       "sonusNodeShelfAdmnRestart": sonusNodeShelfAdmnRestart,
       "sonusNodeShelfAdmnRowStatus": sonusNodeShelfAdmnRowStatus,
       "sonusNodeShelfStatTable": sonusNodeShelfStatTable,
       "sonusNodeShelfStatEntry": sonusNodeShelfStatEntry,
       "sonusNodeShelfStatIndex": sonusNodeShelfStatIndex,
       "sonusNodeShelfStatSlots": sonusNodeShelfStatSlots,
       "sonusNodeShelfStatSerialNumber": sonusNodeShelfStatSerialNumber,
       "sonusNodeShelfStatType": sonusNodeShelfStatType,
       "sonusNodeShelfStatFan": sonusNodeShelfStatFan,
       "sonusNodeShelfStat48VAStatus": sonusNodeShelfStat48VAStatus,
       "sonusNodeShelfStat48VBStatus": sonusNodeShelfStat48VBStatus,
       "sonusNodeShelfStatBackplane": sonusNodeShelfStatBackplane,
       "sonusNodeShelfStatBootCount": sonusNodeShelfStatBootCount,
       "sonusNodeShelfStatTemperature": sonusNodeShelfStatTemperature,
       "sonusNodeShelfStatFanSpeed": sonusNodeShelfStatFanSpeed,
       "sonusNodeSrvrAdmnTable": sonusNodeSrvrAdmnTable,
       "sonusNodeSrvrAdmnEntry": sonusNodeSrvrAdmnEntry,
       "sonusNodeSrvrAdmnShelfIndex": sonusNodeSrvrAdmnShelfIndex,
       "sonusNodeSrvrAdmnSlotIndex": sonusNodeSrvrAdmnSlotIndex,
       "sonusNodeSrvrAdmnHwType": sonusNodeSrvrAdmnHwType,
       "sonusNodeSrvrAdmnState": sonusNodeSrvrAdmnState,
       "sonusNodeSrvrAdmnMode": sonusNodeSrvrAdmnMode,
       "sonusNodeSrvrAdmnAction": sonusNodeSrvrAdmnAction,
       "sonusNodeSrvrAdmnDryupLimit": sonusNodeSrvrAdmnDryupLimit,
       "sonusNodeSrvrAdmnDumpState": sonusNodeSrvrAdmnDumpState,
       "sonusNodeSrvrAdmnRowStatus": sonusNodeSrvrAdmnRowStatus,
       "sonusNodeSrvrAdmnRedundancyRole": sonusNodeSrvrAdmnRedundancyRole,
       "sonusNodeSrvrAdmnAdapHwType": sonusNodeSrvrAdmnAdapHwType,
       "sonusNodeSrvrAdmnSpecialFunction": sonusNodeSrvrAdmnSpecialFunction,
       "sonusNodeSlotTable": sonusNodeSlotTable,
       "sonusNodeSlotEntry": sonusNodeSlotEntry,
       "sonusNodeSlotShelfIndex": sonusNodeSlotShelfIndex,
       "sonusNodeSlotIndex": sonusNodeSlotIndex,
       "sonusNodeSlotState": sonusNodeSlotState,
       "sonusNodeSlotHwType": sonusNodeSlotHwType,
       "sonusNodeSlotHwTypeRev": sonusNodeSlotHwTypeRev,
       "sonusNodeSlotPower": sonusNodeSlotPower,
       "sonusNodeSlotAdapState": sonusNodeSlotAdapState,
       "sonusNodeSlotAdapHwType": sonusNodeSlotAdapHwType,
       "sonusNodeSrvrStatTable": sonusNodeSrvrStatTable,
       "sonusNodeSrvrStatEntry": sonusNodeSrvrStatEntry,
       "sonusNodeSrvrStatShelfIndex": sonusNodeSrvrStatShelfIndex,
       "sonusNodeSrvrStatSlotIndex": sonusNodeSrvrStatSlotIndex,
       "sonusNodeSrvrStatMiddVersion": sonusNodeSrvrStatMiddVersion,
       "sonusNodeSrvrStatHwType": sonusNodeSrvrStatHwType,
       "sonusNodeSrvrStatSerialNum": sonusNodeSrvrStatSerialNum,
       "sonusNodeSrvrStatPartNum": sonusNodeSrvrStatPartNum,
       "sonusNodeSrvrStatPartNumRev": sonusNodeSrvrStatPartNumRev,
       "sonusNodeSrvrStatMfgDate": sonusNodeSrvrStatMfgDate,
       "sonusNodeSrvrStatFlashVersion": sonusNodeSrvrStatFlashVersion,
       "sonusNodeSrvrStatSwVersion": sonusNodeSrvrStatSwVersion,
       "sonusNodeSrvrStatBuildNum": sonusNodeSrvrStatBuildNum,
       "sonusNodeSrvrStatMode": sonusNodeSrvrStatMode,
       "sonusNodeSrvrStatTemperature": sonusNodeSrvrStatTemperature,
       "sonusNodeSrvrStatMemUtilization": sonusNodeSrvrStatMemUtilization,
       "sonusNodeSrvrStatCpuUtilization": sonusNodeSrvrStatCpuUtilization,
       "sonusNodeSrvrStatHwTypeRev": sonusNodeSrvrStatHwTypeRev,
       "sonusNodeSrvrStatSwVersionCode": sonusNodeSrvrStatSwVersionCode,
       "sonusNodeSrvrStatEpldRev": sonusNodeSrvrStatEpldRev,
       "sonusNodeSrvrStatHostName": sonusNodeSrvrStatHostName,
       "sonusNodeSrvrStatUserName": sonusNodeSrvrStatUserName,
       "sonusNodeSrvrStatViewName": sonusNodeSrvrStatViewName,
       "sonusNodeSrvrStatTotalMem": sonusNodeSrvrStatTotalMem,
       "sonusNodeSrvrStatFreeMem": sonusNodeSrvrStatFreeMem,
       "sonusNodeSrvrStatTotalSharedMem": sonusNodeSrvrStatTotalSharedMem,
       "sonusNodeSrvrStatFreeSharedMem": sonusNodeSrvrStatFreeSharedMem,
       "sonusNodeAdapStatTable": sonusNodeAdapStatTable,
       "sonusNodeAdapStatEntry": sonusNodeAdapStatEntry,
       "sonusNodeAdapStatShelfIndex": sonusNodeAdapStatShelfIndex,
       "sonusNodeAdapStatSlotIndex": sonusNodeAdapStatSlotIndex,
       "sonusNodeAdapStatMiddVersion": sonusNodeAdapStatMiddVersion,
       "sonusNodeAdapStatHwType": sonusNodeAdapStatHwType,
       "sonusNodeAdapStatHwTypeRev": sonusNodeAdapStatHwTypeRev,
       "sonusNodeAdapStatSerialNum": sonusNodeAdapStatSerialNum,
       "sonusNodeAdapStatPartNum": sonusNodeAdapStatPartNum,
       "sonusNodeAdapStatPartNumRev": sonusNodeAdapStatPartNumRev,
       "sonusNodeAdapStatMfgDate": sonusNodeAdapStatMfgDate,
       "sonusNodeSlotAdmnTable": sonusNodeSlotAdmnTable,
       "sonusNodeSlotAdmnEntry": sonusNodeSlotAdmnEntry,
       "sonusNodeSlotAdmnShelfIndex": sonusNodeSlotAdmnShelfIndex,
       "sonusNodeSlotAdmnSlotIndex": sonusNodeSlotAdmnSlotIndex,
       "sonusNodeSlotAdmnReset": sonusNodeSlotAdmnReset,
       "sonusNvsConfig": sonusNvsConfig,
       "sonusNvsConfigTable": sonusNvsConfigTable,
       "sonusNvsConfigEntry": sonusNvsConfigEntry,
       "sonusBparamShelfIndex": sonusBparamShelfIndex,
       "sonusBparamUnused": sonusBparamUnused,
       "sonusBparamPasswd": sonusBparamPasswd,
       "sonusBparamIpAddrSlot1Port0": sonusBparamIpAddrSlot1Port0,
       "sonusBparamIpMaskSlot1Port0": sonusBparamIpMaskSlot1Port0,
       "sonusBparamIpGatewaySlot1Port0": sonusBparamIpGatewaySlot1Port0,
       "sonusBparamIfSpeedTypeSlot1Port0": sonusBparamIfSpeedTypeSlot1Port0,
       "sonusBparamIpAddrSlot1Port1": sonusBparamIpAddrSlot1Port1,
       "sonusBparamIpMaskSlot1Port1": sonusBparamIpMaskSlot1Port1,
       "sonusBparamIpGatewaySlot1Port1": sonusBparamIpGatewaySlot1Port1,
       "sonusBparamIfSpeedTypeSlot1Port1": sonusBparamIfSpeedTypeSlot1Port1,
       "sonusBparamIpAddrSlot1Port2": sonusBparamIpAddrSlot1Port2,
       "sonusBparamIpMaskSlot1Port2": sonusBparamIpMaskSlot1Port2,
       "sonusBparamIpGatewaySlot1Port2": sonusBparamIpGatewaySlot1Port2,
       "sonusBparamIfSpeedTypeSlot1Port2": sonusBparamIfSpeedTypeSlot1Port2,
       "sonusBparamIpAddrSlot2Port0": sonusBparamIpAddrSlot2Port0,
       "sonusBparamIpMaskSlot2Port0": sonusBparamIpMaskSlot2Port0,
       "sonusBparamIpGatewaySlot2Port0": sonusBparamIpGatewaySlot2Port0,
       "sonusBparamIfSpeedTypeSlot2Port0": sonusBparamIfSpeedTypeSlot2Port0,
       "sonusBparamIpAddrSlot2Port1": sonusBparamIpAddrSlot2Port1,
       "sonusBparamIpMaskSlot2Port1": sonusBparamIpMaskSlot2Port1,
       "sonusBparamIpGatewaySlot2Port1": sonusBparamIpGatewaySlot2Port1,
       "sonusBparamIfSpeedTypeSlot2Port1": sonusBparamIfSpeedTypeSlot2Port1,
       "sonusBparamIpAddrSlot2Port2": sonusBparamIpAddrSlot2Port2,
       "sonusBparamIpMaskSlot2Port2": sonusBparamIpMaskSlot2Port2,
       "sonusBparamIpGatewaySlot2Port2": sonusBparamIpGatewaySlot2Port2,
       "sonusBparamIfSpeedTypeSlot2Port2": sonusBparamIfSpeedTypeSlot2Port2,
       "sonusBparamBootDelay": sonusBparamBootDelay,
       "sonusBparamCoreState": sonusBparamCoreState,
       "sonusBparamCoreLevel": sonusBparamCoreLevel,
       "sonusBparamBaudRate": sonusBparamBaudRate,
       "sonusBparamNfsPrimary": sonusBparamNfsPrimary,
       "sonusBparamNfsSecondary": sonusBparamNfsSecondary,
       "sonusBparamNfsMountPri": sonusBparamNfsMountPri,
       "sonusBparamNfsMountSec": sonusBparamNfsMountSec,
       "sonusBparamNfsPathUpgrade": sonusBparamNfsPathUpgrade,
       "sonusBparamNfsPathLoad": sonusBparamNfsPathLoad,
       "sonusBparamPrimName": sonusBparamPrimName,
       "sonusBparamSecName": sonusBparamSecName,
       "sonusBparamMasterState": sonusBparamMasterState,
       "sonusBparamParamMode": sonusBparamParamMode,
       "sonusBparamCliScript": sonusBparamCliScript,
       "sonusBparamUId": sonusBparamUId,
       "sonusBparamGrpId": sonusBparamGrpId,
       "sonusBparamCoreDumpLimit": sonusBparamCoreDumpLimit,
       "sonusBparamNfsPathSoftware": sonusBparamNfsPathSoftware,
       "sonusFlashConfigTable": sonusFlashConfigTable,
       "sonusFlashConfigEntry": sonusFlashConfigEntry,
       "sonusFlashAdmnShelfIndex": sonusFlashAdmnShelfIndex,
       "sonusFlashAdmnSlotIndex": sonusFlashAdmnSlotIndex,
       "sonusFlashAdmnUpdateButton": sonusFlashAdmnUpdateButton,
       "sonusFlashStatusTable": sonusFlashStatusTable,
       "sonusFlashStatusEntry": sonusFlashStatusEntry,
       "sonusFlashStatShelfIndex": sonusFlashStatShelfIndex,
       "sonusFlashStatSlotIndex": sonusFlashStatSlotIndex,
       "sonusFlashStatState": sonusFlashStatState,
       "sonusFlashStatLastStatus": sonusFlashStatLastStatus,
       "sonusUser": sonusUser,
       "sonusUserList": sonusUserList,
       "sonusUserListNextIndex": sonusUserListNextIndex,
       "sonusUserListTable": sonusUserListTable,
       "sonusUserListEntry": sonusUserListEntry,
       "sonusUserListIndex": sonusUserListIndex,
       "sonusUserListState": sonusUserListState,
       "sonusUserListUserName": sonusUserListUserName,
       "sonusUserListProfileName": sonusUserListProfileName,
       "sonusUserListPasswd": sonusUserListPasswd,
       "sonusUserListComment": sonusUserListComment,
       "sonusUserListAccess": sonusUserListAccess,
       "sonusUserListRowStatus": sonusUserListRowStatus,
       "sonusUserListStatusTable": sonusUserListStatusTable,
       "sonusUserListStatusEntry": sonusUserListStatusEntry,
       "sonusUserListStatusIndex": sonusUserListStatusIndex,
       "sonusUserListStatusLastConfigChange": sonusUserListStatusLastConfigChange,
       "sonusUserProfile": sonusUserProfile,
       "sonusUserProfileNextIndex": sonusUserProfileNextIndex,
       "sonusUserProfileTable": sonusUserProfileTable,
       "sonusUserProfileEntry": sonusUserProfileEntry,
       "sonusUserProfileIndex": sonusUserProfileIndex,
       "sonusUserProfileName": sonusUserProfileName,
       "sonusUserProfileUserState": sonusUserProfileUserState,
       "sonusUserProfileUserPasswd": sonusUserProfileUserPasswd,
       "sonusUserProfileUserComment": sonusUserProfileUserComment,
       "sonusUserProfileUserAccess": sonusUserProfileUserAccess,
       "sonusUserProfileUserCommentState": sonusUserProfileUserCommentState,
       "sonusUserProfileUserPasswdState": sonusUserProfileUserPasswdState,
       "sonusUserProfileUserAccessState": sonusUserProfileUserAccessState,
       "sonusUserProfileUserStateState": sonusUserProfileUserStateState,
       "sonusUserProfileRowStatus": sonusUserProfileRowStatus,
       "sonusSwLoad": sonusSwLoad,
       "sonusSwLoadTable": sonusSwLoadTable,
       "sonusSwLoadEntry": sonusSwLoadEntry,
       "sonusSwLoadAdmnIndex": sonusSwLoadAdmnIndex,
       "sonusSwLoadAdmnImageName": sonusSwLoadAdmnImageName,
       "sonusSwLoadAdmnHwType": sonusSwLoadAdmnHwType,
       "sonusSwLoadAdmnRowStatus": sonusSwLoadAdmnRowStatus,
       "sonusSwLoadSpecTable": sonusSwLoadSpecTable,
       "sonusSwLoadSpecEntry": sonusSwLoadSpecEntry,
       "sonusSwLoadSpecAdmnShelfIndex": sonusSwLoadSpecAdmnShelfIndex,
       "sonusSwLoadSpecAdmnSlotIndex": sonusSwLoadSpecAdmnSlotIndex,
       "sonusSwLoadSpecAdmnImageName": sonusSwLoadSpecAdmnImageName,
       "sonusSwLoadSpecAdmnRowStatus": sonusSwLoadSpecAdmnRowStatus,
       "sonusParam": sonusParam,
       "sonusParamStatusObjects": sonusParamStatusObjects,
       "sonusParamSaveSeqNumber": sonusParamSaveSeqNumber,
       "sonusParamSaveTimeStart": sonusParamSaveTimeStart,
       "sonusParamSaveTimeStop": sonusParamSaveTimeStop,
       "sonusParamSaveDuration": sonusParamSaveDuration,
       "sonusParamSaveTotalBytes": sonusParamSaveTotalBytes,
       "sonusParamSaveTotalRecords": sonusParamSaveTotalRecords,
       "sonusParamSaveFilename": sonusParamSaveFilename,
       "sonusParamSaveState": sonusParamSaveState,
       "sonusParamLoadServer": sonusParamLoadServer,
       "sonusParamLoadFileType": sonusParamLoadFileType,
       "sonusParamLoadStatus": sonusParamLoadStatus,
       "sonusParamLoadSeqNumber": sonusParamLoadSeqNumber,
       "sonusParamLoadTotalRecords": sonusParamLoadTotalRecords,
       "sonusParamLoadTotalBytes": sonusParamLoadTotalBytes,
       "sonusParamLoadDuration": sonusParamLoadDuration,
       "sonusParamLoadSerialNum": sonusParamLoadSerialNum,
       "sonusParamSavePrimarySrvrState": sonusParamSavePrimarySrvrState,
       "sonusParamSavePrimarySrvrReason": sonusParamSavePrimarySrvrReason,
       "sonusParamSaveSecondarySrvrState": sonusParamSaveSecondarySrvrState,
       "sonusParamSaveSecondarySrvrReason": sonusParamSaveSecondarySrvrReason,
       "sonusParamLastSaveTime": sonusParamLastSaveTime,
       "sonusParamAdminObject": sonusParamAdminObject,
       "sonusParamAdmnMaxIncrPifs": sonusParamAdmnMaxIncrPifs,
       "sonusNfs": sonusNfs,
       "sonusNfsAdmnTable": sonusNfsAdmnTable,
       "sonusNfsAdmnEntry": sonusNfsAdmnEntry,
       "sonusNfsAdmnShelfIndex": sonusNfsAdmnShelfIndex,
       "sonusNfsAdmnSlotIndex": sonusNfsAdmnSlotIndex,
       "sonusNfsAdmnMountServer": sonusNfsAdmnMountServer,
       "sonusNfsAdmnUnmountServer": sonusNfsAdmnUnmountServer,
       "sonusNfsAdmnToggleActiveServer": sonusNfsAdmnToggleActiveServer,
       "sonusNfsAdmnSetWritable": sonusNfsAdmnSetWritable,
       "sonusNfsStatTable": sonusNfsStatTable,
       "sonusNfsStatEntry": sonusNfsStatEntry,
       "sonusNfsStatShelfIndex": sonusNfsStatShelfIndex,
       "sonusNfsStatSlotIndex": sonusNfsStatSlotIndex,
       "sonusNfsStatPrimaryStatus": sonusNfsStatPrimaryStatus,
       "sonusNfsStatSecondaryStatus": sonusNfsStatSecondaryStatus,
       "sonusNfsStatActiveServer": sonusNfsStatActiveServer,
       "sonusNfsStatStandbyServer": sonusNfsStatStandbyServer,
       "sonusNfsStatPrimaryIP": sonusNfsStatPrimaryIP,
       "sonusNfsStatSecondaryIP": sonusNfsStatSecondaryIP,
       "sonusNfsStatPrimaryMount": sonusNfsStatPrimaryMount,
       "sonusNfsStatSecondaryMount": sonusNfsStatSecondaryMount,
       "sonusNfsStatPrimaryLastError": sonusNfsStatPrimaryLastError,
       "sonusNfsStatSecondaryLastError": sonusNfsStatSecondaryLastError,
       "sonusNodeMIBNotifications": sonusNodeMIBNotifications,
       "sonusNodeMIBNotificationsPrefix": sonusNodeMIBNotificationsPrefix,
       "sonusNodeShelfPowerA48VdcNormalNotification": sonusNodeShelfPowerA48VdcNormalNotification,
       "sonusNodeShelfPowerB48VdcNormalNotification": sonusNodeShelfPowerB48VdcNormalNotification,
       "sonusNodeShelfPowerA48VdcFailureNotification": sonusNodeShelfPowerA48VdcFailureNotification,
       "sonusNodeShelfPowerB48VdcFailureNotification": sonusNodeShelfPowerB48VdcFailureNotification,
       "sonusNodeShelfFanTrayFailureNotification": sonusNodeShelfFanTrayFailureNotification,
       "sonusNodeShelfFanTrayOperationalNotification": sonusNodeShelfFanTrayOperationalNotification,
       "sonusNodeShelfFanTrayRemovedNotification": sonusNodeShelfFanTrayRemovedNotification,
       "sonusNodeShelfFanTrayPresentNotification": sonusNodeShelfFanTrayPresentNotification,
       "sonusNodeShelfIntakeTempWarningNotification": sonusNodeShelfIntakeTempWarningNotification,
       "sonusNodeServerTempWarningNotification": sonusNodeServerTempWarningNotification,
       "sonusNodeServerTempFailureNotification": sonusNodeServerTempFailureNotification,
       "sonusNodeServerTempNormalNotification": sonusNodeServerTempNormalNotification,
       "sonusNodeServerInsertedNotification": sonusNodeServerInsertedNotification,
       "sonusNodeServerRemovedNotification": sonusNodeServerRemovedNotification,
       "sonusNodeServerResetNotification": sonusNodeServerResetNotification,
       "sonusNodeServerOperationalNotification": sonusNodeServerOperationalNotification,
       "sonusNodeServerPowerFailureNotification": sonusNodeServerPowerFailureNotification,
       "sonusNodeServerSoftwareFailureNotification": sonusNodeServerSoftwareFailureNotification,
       "sonusNodeServerHardwareFailureNotification": sonusNodeServerHardwareFailureNotification,
       "sonusNodeAdapterInsertedNotification": sonusNodeAdapterInsertedNotification,
       "sonusNodeAdapterRemovedNotification": sonusNodeAdapterRemovedNotification,
       "sonusNodeMtaInsertedNotification": sonusNodeMtaInsertedNotification,
       "sonusNodeMtaRemovedNotification": sonusNodeMtaRemovedNotification,
       "sonusNodeEthernetActiveNotification": sonusNodeEthernetActiveNotification,
       "sonusNodeEthernetInactiveNotification": sonusNodeEthernetInactiveNotification,
       "sonusNodeEthernetDegradedNotification": sonusNodeEthernetDegradedNotification,
       "sonusNodeBootNotification": sonusNodeBootNotification,
       "sonusNodeSlaveShelfBootNotification": sonusNodeSlaveShelfBootNotification,
       "sonusNodeNfsServerSwitchoverNotification": sonusNodeNfsServerSwitchoverNotification,
       "sonusNodeNfsServerOutOfServiceNotification": sonusNodeNfsServerOutOfServiceNotification,
       "sonusNodeNfsServerInServiceNotification": sonusNodeNfsServerInServiceNotification,
       "sonusNodeNfsServerNotWritableNotification": sonusNodeNfsServerNotWritableNotification,
       "sonusNodeServerDisabledNotification": sonusNodeServerDisabledNotification,
       "sonusNodeServerEnabledNotification": sonusNodeServerEnabledNotification,
       "sonusNodeServerDeletedNotification": sonusNodeServerDeletedNotification,
       "sonusParamBackupLoadNotification": sonusParamBackupLoadNotification,
       "sonusParamCorruptionNotification": sonusParamCorruptionNotification,
       "sonusNodeAdapterMissingNotification": sonusNodeAdapterMissingNotification,
       "sonusNodeAdapterFailureNotification": sonusNodeAdapterFailureNotification,
       "sonusNodeSlotResetNotification": sonusNodeSlotResetNotification,
       "sonusNodeParamWriteCompleteNotification": sonusNodeParamWriteCompleteNotification,
       "sonusNodeParamWriteErrorNotification": sonusNodeParamWriteErrorNotification,
       "sonusNodeBootMnsActiveNotification": sonusNodeBootMnsActiveNotification,
       "sonusNodeShelfIntakeTempNormalNotification": sonusNodeShelfIntakeTempNormalNotification,
       "sonusNodeMIBNotificationsObjects": sonusNodeMIBNotificationsObjects,
       "sonusNfsServer": sonusNfsServer,
       "sonusNfsRole": sonusNfsRole,
       "sonusNfsServerIp": sonusNfsServerIp,
       "sonusNfsServerMount": sonusNfsServerMount,
       "sonusNfsReason": sonusNfsReason,
       "sonusNfsErrorCode": sonusNfsErrorCode}
)
