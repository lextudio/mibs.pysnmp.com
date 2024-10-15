# SNMP MIB module (HUAWEI-UNIMNG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-UNIMNG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:20 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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

(AutonomousType,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwUnimngMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327)
)
hwUnimngMIB.setRevisions(
        ("2015-07-09 14:07",
         "2015-01-09 14:07",
         "2014-11-18 15:30",
         "2014-10-29 16:57",
         "2014-10-23 15:30",
         "2014-09-11 15:30",
         "2014-08-19 15:30",
         "2014-07-10 12:50",
         "2014-03-03 20:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmStatus(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HwUnimngObjects_ObjectIdentity = ObjectIdentity
hwUnimngObjects = _HwUnimngObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 1)
)


class _HwUniMngEnable_Type(Integer32):
    """Custom type hwUniMngEnable based on Integer32"""
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


_HwUniMngEnable_Type.__name__ = "Integer32"
_HwUniMngEnable_Object = MibScalar
hwUniMngEnable = _HwUniMngEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 1, 1),
    _HwUniMngEnable_Type()
)
hwUniMngEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUniMngEnable.setStatus("current")
_HwAsmngObjects_ObjectIdentity = ObjectIdentity
hwAsmngObjects = _HwAsmngObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2)
)
_HwAsTable_Object = MibTable
hwAsTable = _HwAsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1)
)
if mibBuilder.loadTexts:
    hwAsTable.setStatus("current")
_HwAsEntry_Object = MibTableRow
hwAsEntry = _HwAsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1)
)
hwAsEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwAsIndex"),
)
if mibBuilder.loadTexts:
    hwAsEntry.setStatus("current")


class _HwAsIndex_Type(Integer32):
    """Custom type hwAsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwAsIndex_Type.__name__ = "Integer32"
_HwAsIndex_Object = MibTableColumn
hwAsIndex = _HwAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 1),
    _HwAsIndex_Type()
)
hwAsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIndex.setStatus("current")


class _HwAsHardwareVersion_Type(OctetString):
    """Custom type hwAsHardwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwAsHardwareVersion_Type.__name__ = "OctetString"
_HwAsHardwareVersion_Object = MibTableColumn
hwAsHardwareVersion = _HwAsHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 2),
    _HwAsHardwareVersion_Type()
)
hwAsHardwareVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsHardwareVersion.setStatus("current")
_HwAsIpAddress_Type = IpAddress
_HwAsIpAddress_Object = MibTableColumn
hwAsIpAddress = _HwAsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 3),
    _HwAsIpAddress_Type()
)
hwAsIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsIpAddress.setStatus("current")
_HwAsIpNetMask_Type = IpAddress
_HwAsIpNetMask_Object = MibTableColumn
hwAsIpNetMask = _HwAsIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 4),
    _HwAsIpNetMask_Type()
)
hwAsIpNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsIpNetMask.setStatus("current")
_HwAsAccessUser_Type = Integer32
_HwAsAccessUser_Object = MibTableColumn
hwAsAccessUser = _HwAsAccessUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 5),
    _HwAsAccessUser_Type()
)
hwAsAccessUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsAccessUser.setStatus("current")
_HwAsMac_Type = MacAddress
_HwAsMac_Object = MibTableColumn
hwAsMac = _HwAsMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 6),
    _HwAsMac_Type()
)
hwAsMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsMac.setStatus("current")
_HwAsSn_Type = OctetString
_HwAsSn_Object = MibTableColumn
hwAsSn = _HwAsSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 7),
    _HwAsSn_Type()
)
hwAsSn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsSn.setStatus("current")


class _HwAsSysName_Type(OctetString):
    """Custom type hwAsSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwAsSysName_Type.__name__ = "OctetString"
_HwAsSysName_Object = MibTableColumn
hwAsSysName = _HwAsSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 8),
    _HwAsSysName_Type()
)
hwAsSysName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsSysName.setStatus("current")


class _HwAsRunState_Type(Integer32):
    """Custom type hwAsRunState based on Integer32"""
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
        *(("fault", 3),
          ("idle", 1),
          ("normal", 4),
          ("versionMismatch", 2))
    )


_HwAsRunState_Type.__name__ = "Integer32"
_HwAsRunState_Object = MibTableColumn
hwAsRunState = _HwAsRunState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 9),
    _HwAsRunState_Type()
)
hwAsRunState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsRunState.setStatus("current")


class _HwAsSoftwareVersion_Type(OctetString):
    """Custom type hwAsSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwAsSoftwareVersion_Type.__name__ = "OctetString"
_HwAsSoftwareVersion_Object = MibTableColumn
hwAsSoftwareVersion = _HwAsSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 10),
    _HwAsSoftwareVersion_Type()
)
hwAsSoftwareVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsSoftwareVersion.setStatus("current")


class _HwAsModel_Type(OctetString):
    """Custom type hwAsModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 23),
    )


_HwAsModel_Type.__name__ = "OctetString"
_HwAsModel_Object = MibTableColumn
hwAsModel = _HwAsModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 11),
    _HwAsModel_Type()
)
hwAsModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsModel.setStatus("current")
_HwAsDns_Type = IpAddress
_HwAsDns_Object = MibTableColumn
hwAsDns = _HwAsDns_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 12),
    _HwAsDns_Type()
)
hwAsDns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsDns.setStatus("current")
_HwAsOnlineTime_Type = OctetString
_HwAsOnlineTime_Object = MibTableColumn
hwAsOnlineTime = _HwAsOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 13),
    _HwAsOnlineTime_Type()
)
hwAsOnlineTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsOnlineTime.setStatus("current")
_HwAsCpuUseage_Type = Integer32
_HwAsCpuUseage_Object = MibTableColumn
hwAsCpuUseage = _HwAsCpuUseage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 14),
    _HwAsCpuUseage_Type()
)
hwAsCpuUseage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsCpuUseage.setStatus("current")
_HwAsMemoryUseage_Type = Integer32
_HwAsMemoryUseage_Object = MibTableColumn
hwAsMemoryUseage = _HwAsMemoryUseage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 15),
    _HwAsMemoryUseage_Type()
)
hwAsMemoryUseage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsMemoryUseage.setStatus("current")
_HwAsSysMac_Type = MacAddress
_HwAsSysMac_Object = MibTableColumn
hwAsSysMac = _HwAsSysMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 16),
    _HwAsSysMac_Type()
)
hwAsSysMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsSysMac.setStatus("current")


class _HwAsStackEnable_Type(Integer32):
    """Custom type hwAsStackEnable based on Integer32"""
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


_HwAsStackEnable_Type.__name__ = "Integer32"
_HwAsStackEnable_Object = MibTableColumn
hwAsStackEnable = _HwAsStackEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 17),
    _HwAsStackEnable_Type()
)
hwAsStackEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsStackEnable.setStatus("current")
_HwAsGatewayIp_Type = IpAddress
_HwAsGatewayIp_Object = MibTableColumn
hwAsGatewayIp = _HwAsGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 18),
    _HwAsGatewayIp_Type()
)
hwAsGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsGatewayIp.setStatus("current")
_HwAsVpnInstance_Type = OctetString
_HwAsVpnInstance_Object = MibTableColumn
hwAsVpnInstance = _HwAsVpnInstance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 19),
    _HwAsVpnInstance_Type()
)
hwAsVpnInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsVpnInstance.setStatus("current")
_HwAsRowstatus_Type = RowStatus
_HwAsRowstatus_Object = MibTableColumn
hwAsRowstatus = _HwAsRowstatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 1, 1, 50),
    _HwAsRowstatus_Type()
)
hwAsRowstatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsRowstatus.setStatus("current")
_HwAsIfTable_Object = MibTable
hwAsIfTable = _HwAsIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2)
)
if mibBuilder.loadTexts:
    hwAsIfTable.setStatus("current")
_HwAsIfEntry_Object = MibTableRow
hwAsIfEntry = _HwAsIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2, 1)
)
hwAsIfEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwAsIfIndex"),
)
if mibBuilder.loadTexts:
    hwAsIfEntry.setStatus("current")
_HwAsIfIndex_Type = Integer32
_HwAsIfIndex_Object = MibTableColumn
hwAsIfIndex = _HwAsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2, 1, 1),
    _HwAsIfIndex_Type()
)
hwAsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfIndex.setStatus("current")
_HwAsIfDescr_Type = OctetString
_HwAsIfDescr_Object = MibTableColumn
hwAsIfDescr = _HwAsIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2, 1, 2),
    _HwAsIfDescr_Type()
)
hwAsIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfDescr.setStatus("current")
_HwAsIfType_Type = Integer32
_HwAsIfType_Object = MibTableColumn
hwAsIfType = _HwAsIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2, 1, 3),
    _HwAsIfType_Type()
)
hwAsIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfType.setStatus("current")
_HwAsIfMtu_Type = Integer32
_HwAsIfMtu_Object = MibTableColumn
hwAsIfMtu = _HwAsIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2, 1, 4),
    _HwAsIfMtu_Type()
)
hwAsIfMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAsIfMtu.setStatus("current")
_HwAsIfSpeed_Type = Gauge32
_HwAsIfSpeed_Object = MibTableColumn
hwAsIfSpeed = _HwAsIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2, 1, 5),
    _HwAsIfSpeed_Type()
)
hwAsIfSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfSpeed.setStatus("current")
_HwAsIfPhysAddress_Type = OctetString
_HwAsIfPhysAddress_Object = MibTableColumn
hwAsIfPhysAddress = _HwAsIfPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2, 1, 6),
    _HwAsIfPhysAddress_Type()
)
hwAsIfPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfPhysAddress.setStatus("current")


class _HwAsIfAdminStatus_Type(Integer32):
    """Custom type hwAsIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwAsIfAdminStatus_Type.__name__ = "Integer32"
_HwAsIfAdminStatus_Object = MibTableColumn
hwAsIfAdminStatus = _HwAsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2, 1, 7),
    _HwAsIfAdminStatus_Type()
)
hwAsIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAsIfAdminStatus.setStatus("current")


class _HwAsIfOperStatus_Type(Integer32):
    """Custom type hwAsIfOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwAsIfOperStatus_Type.__name__ = "Integer32"
_HwAsIfOperStatus_Object = MibTableColumn
hwAsIfOperStatus = _HwAsIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2, 1, 8),
    _HwAsIfOperStatus_Type()
)
hwAsIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfOperStatus.setStatus("current")
_HwAsIfInUcastPkts_Type = Counter32
_HwAsIfInUcastPkts_Object = MibTableColumn
hwAsIfInUcastPkts = _HwAsIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2, 1, 9),
    _HwAsIfInUcastPkts_Type()
)
hwAsIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfInUcastPkts.setStatus("current")
_HwAsIfOutUcastPkts_Type = Counter32
_HwAsIfOutUcastPkts_Object = MibTableColumn
hwAsIfOutUcastPkts = _HwAsIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 2, 1, 10),
    _HwAsIfOutUcastPkts_Type()
)
hwAsIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfOutUcastPkts.setStatus("current")
_HwAsIfXTable_Object = MibTable
hwAsIfXTable = _HwAsIfXTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3)
)
if mibBuilder.loadTexts:
    hwAsIfXTable.setStatus("current")
_HwAsIfXEntry_Object = MibTableRow
hwAsIfXEntry = _HwAsIfXEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1)
)
hwAsIfXEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwAsIfIndex"),
)
if mibBuilder.loadTexts:
    hwAsIfXEntry.setStatus("current")
_HwAsIfName_Type = OctetString
_HwAsIfName_Object = MibTableColumn
hwAsIfName = _HwAsIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1, 1),
    _HwAsIfName_Type()
)
hwAsIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfName.setStatus("current")


class _HwAsIfLinkUpDownTrapEnable_Type(Integer32):
    """Custom type hwAsIfLinkUpDownTrapEnable based on Integer32"""
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


_HwAsIfLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_HwAsIfLinkUpDownTrapEnable_Object = MibTableColumn
hwAsIfLinkUpDownTrapEnable = _HwAsIfLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1, 2),
    _HwAsIfLinkUpDownTrapEnable_Type()
)
hwAsIfLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAsIfLinkUpDownTrapEnable.setStatus("current")
_HwAsIfHighSpeed_Type = Integer32
_HwAsIfHighSpeed_Object = MibTableColumn
hwAsIfHighSpeed = _HwAsIfHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1, 3),
    _HwAsIfHighSpeed_Type()
)
hwAsIfHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfHighSpeed.setStatus("current")
_HwAsIfAlias_Type = OctetString
_HwAsIfAlias_Object = MibTableColumn
hwAsIfAlias = _HwAsIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1, 4),
    _HwAsIfAlias_Type()
)
hwAsIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAsIfAlias.setStatus("current")
_HwAsIfAsId_Type = Integer32
_HwAsIfAsId_Object = MibTableColumn
hwAsIfAsId = _HwAsIfAsId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1, 5),
    _HwAsIfAsId_Type()
)
hwAsIfAsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfAsId.setStatus("current")
_HwAsIfHCOutOctets_Type = Counter64
_HwAsIfHCOutOctets_Object = MibTableColumn
hwAsIfHCOutOctets = _HwAsIfHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1, 6),
    _HwAsIfHCOutOctets_Type()
)
hwAsIfHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfHCOutOctets.setStatus("current")
_HwAsIfInMulticastPkts_Type = Counter32
_HwAsIfInMulticastPkts_Object = MibTableColumn
hwAsIfInMulticastPkts = _HwAsIfInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1, 7),
    _HwAsIfInMulticastPkts_Type()
)
hwAsIfInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfInMulticastPkts.setStatus("current")
_HwAsIfInBroadcastPkts_Type = Counter32
_HwAsIfInBroadcastPkts_Object = MibTableColumn
hwAsIfInBroadcastPkts = _HwAsIfInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1, 8),
    _HwAsIfInBroadcastPkts_Type()
)
hwAsIfInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfInBroadcastPkts.setStatus("current")
_HwAsIfOutMulticastPkts_Type = Counter32
_HwAsIfOutMulticastPkts_Object = MibTableColumn
hwAsIfOutMulticastPkts = _HwAsIfOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1, 9),
    _HwAsIfOutMulticastPkts_Type()
)
hwAsIfOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfOutMulticastPkts.setStatus("current")
_HwAsIfOutBroadcastPkts_Type = Counter32
_HwAsIfOutBroadcastPkts_Object = MibTableColumn
hwAsIfOutBroadcastPkts = _HwAsIfOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1, 10),
    _HwAsIfOutBroadcastPkts_Type()
)
hwAsIfOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfOutBroadcastPkts.setStatus("current")
_HwAsIfHCInOctets_Type = Counter64
_HwAsIfHCInOctets_Object = MibTableColumn
hwAsIfHCInOctets = _HwAsIfHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 3, 1, 11),
    _HwAsIfHCInOctets_Type()
)
hwAsIfHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsIfHCInOctets.setStatus("current")
_HwAsSlotTable_Object = MibTable
hwAsSlotTable = _HwAsSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 4)
)
if mibBuilder.loadTexts:
    hwAsSlotTable.setStatus("current")
_HwAsSlotEntry_Object = MibTableRow
hwAsSlotEntry = _HwAsSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 4, 1)
)
hwAsSlotEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwAsIndex"),
    (0, "HUAWEI-UNIMNG-MIB", "hwAsSlotId"),
)
if mibBuilder.loadTexts:
    hwAsSlotEntry.setStatus("current")


class _HwAsSlotId_Type(Integer32):
    """Custom type hwAsSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_HwAsSlotId_Type.__name__ = "Integer32"
_HwAsSlotId_Object = MibTableColumn
hwAsSlotId = _HwAsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 4, 1, 1),
    _HwAsSlotId_Type()
)
hwAsSlotId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAsSlotId.setStatus("current")


class _HwAsSlotState_Type(Integer32):
    """Custom type hwAsSlotState based on Integer32"""
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


_HwAsSlotState_Type.__name__ = "Integer32"
_HwAsSlotState_Object = MibTableColumn
hwAsSlotState = _HwAsSlotState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 4, 1, 2),
    _HwAsSlotState_Type()
)
hwAsSlotState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsSlotState.setStatus("current")
_HwAsSlotRowStatus_Type = RowStatus
_HwAsSlotRowStatus_Object = MibTableColumn
hwAsSlotRowStatus = _HwAsSlotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 4, 1, 20),
    _HwAsSlotRowStatus_Type()
)
hwAsSlotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsSlotRowStatus.setStatus("current")
_HwAsmngGlobalObjects_ObjectIdentity = ObjectIdentity
hwAsmngGlobalObjects = _HwAsmngGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 5)
)


class _HwAsAutoReplaceEnable_Type(Integer32):
    """Custom type hwAsAutoReplaceEnable based on Integer32"""
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


_HwAsAutoReplaceEnable_Type.__name__ = "Integer32"
_HwAsAutoReplaceEnable_Object = MibScalar
hwAsAutoReplaceEnable = _HwAsAutoReplaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 5, 1),
    _HwAsAutoReplaceEnable_Type()
)
hwAsAutoReplaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAsAutoReplaceEnable.setStatus("current")


class _HwAsAuthMode_Type(Integer32):
    """Custom type hwAsAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auth", 1),
          ("noAuth", 2))
    )


_HwAsAuthMode_Type.__name__ = "Integer32"
_HwAsAuthMode_Object = MibScalar
hwAsAuthMode = _HwAsAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 5, 2),
    _HwAsAuthMode_Type()
)
hwAsAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAsAuthMode.setStatus("current")
_HwAsMacWhitelistTable_Object = MibTable
hwAsMacWhitelistTable = _HwAsMacWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 6)
)
if mibBuilder.loadTexts:
    hwAsMacWhitelistTable.setStatus("current")
_HwAsMacWhitelistEntry_Object = MibTableRow
hwAsMacWhitelistEntry = _HwAsMacWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 6, 1)
)
hwAsMacWhitelistEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwAsMacWhitelistMacAddr"),
)
if mibBuilder.loadTexts:
    hwAsMacWhitelistEntry.setStatus("current")
_HwAsMacWhitelistMacAddr_Type = MacAddress
_HwAsMacWhitelistMacAddr_Object = MibTableColumn
hwAsMacWhitelistMacAddr = _HwAsMacWhitelistMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 6, 1, 1),
    _HwAsMacWhitelistMacAddr_Type()
)
hwAsMacWhitelistMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAsMacWhitelistMacAddr.setStatus("current")
_HwAsMacWhitelistRowStatus_Type = RowStatus
_HwAsMacWhitelistRowStatus_Object = MibTableColumn
hwAsMacWhitelistRowStatus = _HwAsMacWhitelistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 6, 1, 2),
    _HwAsMacWhitelistRowStatus_Type()
)
hwAsMacWhitelistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsMacWhitelistRowStatus.setStatus("current")
_HwAsMacBlacklistTable_Object = MibTable
hwAsMacBlacklistTable = _HwAsMacBlacklistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 7)
)
if mibBuilder.loadTexts:
    hwAsMacBlacklistTable.setStatus("current")
_HwAsMacBlacklistEntry_Object = MibTableRow
hwAsMacBlacklistEntry = _HwAsMacBlacklistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 7, 1)
)
hwAsMacBlacklistEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwAsMacBlacklistMacAddr"),
)
if mibBuilder.loadTexts:
    hwAsMacBlacklistEntry.setStatus("current")
_HwAsMacBlacklistMacAddr_Type = MacAddress
_HwAsMacBlacklistMacAddr_Object = MibTableColumn
hwAsMacBlacklistMacAddr = _HwAsMacBlacklistMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 7, 1, 1),
    _HwAsMacBlacklistMacAddr_Type()
)
hwAsMacBlacklistMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAsMacBlacklistMacAddr.setStatus("current")
_HwAsMacBlacklistRowStatus_Type = RowStatus
_HwAsMacBlacklistRowStatus_Object = MibTableColumn
hwAsMacBlacklistRowStatus = _HwAsMacBlacklistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 7, 1, 2),
    _HwAsMacBlacklistRowStatus_Type()
)
hwAsMacBlacklistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwAsMacBlacklistRowStatus.setStatus("current")
_HwAsEntityPhysicalTable_Object = MibTable
hwAsEntityPhysicalTable = _HwAsEntityPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8)
)
if mibBuilder.loadTexts:
    hwAsEntityPhysicalTable.setStatus("current")
_HwAsEntityPhysicalEntry_Object = MibTableRow
hwAsEntityPhysicalEntry = _HwAsEntityPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1)
)
hwAsEntityPhysicalEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwAsIndex"),
    (0, "HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwAsEntityPhysicalEntry.setStatus("current")
_HwAsEntityPhysicalIndex_Type = Integer32
_HwAsEntityPhysicalIndex_Object = MibTableColumn
hwAsEntityPhysicalIndex = _HwAsEntityPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 1),
    _HwAsEntityPhysicalIndex_Type()
)
hwAsEntityPhysicalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalIndex.setStatus("current")
_HwAsEntityPhysicalDescr_Type = OctetString
_HwAsEntityPhysicalDescr_Object = MibTableColumn
hwAsEntityPhysicalDescr = _HwAsEntityPhysicalDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 2),
    _HwAsEntityPhysicalDescr_Type()
)
hwAsEntityPhysicalDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalDescr.setStatus("current")
_HwAsEntityPhysicalVendorType_Type = AutonomousType
_HwAsEntityPhysicalVendorType_Object = MibTableColumn
hwAsEntityPhysicalVendorType = _HwAsEntityPhysicalVendorType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 3),
    _HwAsEntityPhysicalVendorType_Type()
)
hwAsEntityPhysicalVendorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalVendorType.setStatus("current")
_HwAsEntityPhysicalContainedIn_Type = Integer32
_HwAsEntityPhysicalContainedIn_Object = MibTableColumn
hwAsEntityPhysicalContainedIn = _HwAsEntityPhysicalContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 4),
    _HwAsEntityPhysicalContainedIn_Type()
)
hwAsEntityPhysicalContainedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalContainedIn.setStatus("current")


class _HwAsEntityPhysicalClass_Type(Integer32):
    """Custom type hwAsEntityPhysicalClass based on Integer32"""
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
        *(("backplane", 4),
          ("chassis", 3),
          ("container", 5),
          ("fan", 7),
          ("module", 9),
          ("other", 1),
          ("port", 10),
          ("powerSupply", 6),
          ("sensor", 8),
          ("stack", 11),
          ("unknown", 2))
    )


_HwAsEntityPhysicalClass_Type.__name__ = "Integer32"
_HwAsEntityPhysicalClass_Object = MibTableColumn
hwAsEntityPhysicalClass = _HwAsEntityPhysicalClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 5),
    _HwAsEntityPhysicalClass_Type()
)
hwAsEntityPhysicalClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalClass.setStatus("current")
_HwAsEntityPhysicalParentRelPos_Type = Integer32
_HwAsEntityPhysicalParentRelPos_Object = MibTableColumn
hwAsEntityPhysicalParentRelPos = _HwAsEntityPhysicalParentRelPos_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 6),
    _HwAsEntityPhysicalParentRelPos_Type()
)
hwAsEntityPhysicalParentRelPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalParentRelPos.setStatus("current")
_HwAsEntityPhysicalName_Type = OctetString
_HwAsEntityPhysicalName_Object = MibTableColumn
hwAsEntityPhysicalName = _HwAsEntityPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 7),
    _HwAsEntityPhysicalName_Type()
)
hwAsEntityPhysicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalName.setStatus("current")
_HwAsEntityPhysicalHardwareRev_Type = OctetString
_HwAsEntityPhysicalHardwareRev_Object = MibTableColumn
hwAsEntityPhysicalHardwareRev = _HwAsEntityPhysicalHardwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 8),
    _HwAsEntityPhysicalHardwareRev_Type()
)
hwAsEntityPhysicalHardwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalHardwareRev.setStatus("current")
_HwAsEntityPhysicalFirmwareRev_Type = OctetString
_HwAsEntityPhysicalFirmwareRev_Object = MibTableColumn
hwAsEntityPhysicalFirmwareRev = _HwAsEntityPhysicalFirmwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 9),
    _HwAsEntityPhysicalFirmwareRev_Type()
)
hwAsEntityPhysicalFirmwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalFirmwareRev.setStatus("current")
_HwAsEntityPhysicalSoftwareRev_Type = OctetString
_HwAsEntityPhysicalSoftwareRev_Object = MibTableColumn
hwAsEntityPhysicalSoftwareRev = _HwAsEntityPhysicalSoftwareRev_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 10),
    _HwAsEntityPhysicalSoftwareRev_Type()
)
hwAsEntityPhysicalSoftwareRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalSoftwareRev.setStatus("current")
_HwAsEntityPhysicalSerialNum_Type = OctetString
_HwAsEntityPhysicalSerialNum_Object = MibTableColumn
hwAsEntityPhysicalSerialNum = _HwAsEntityPhysicalSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 11),
    _HwAsEntityPhysicalSerialNum_Type()
)
hwAsEntityPhysicalSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalSerialNum.setStatus("current")
_HwAsEntityPhysicalMfgName_Type = OctetString
_HwAsEntityPhysicalMfgName_Object = MibTableColumn
hwAsEntityPhysicalMfgName = _HwAsEntityPhysicalMfgName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 8, 1, 12),
    _HwAsEntityPhysicalMfgName_Type()
)
hwAsEntityPhysicalMfgName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPhysicalMfgName.setStatus("current")
_HwAsEntityStateTable_Object = MibTable
hwAsEntityStateTable = _HwAsEntityStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 9)
)
if mibBuilder.loadTexts:
    hwAsEntityStateTable.setStatus("current")
_HwAsEntityStateEntry_Object = MibTableRow
hwAsEntityStateEntry = _HwAsEntityStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 9, 1)
)
hwAsEntityStateEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwAsIndex"),
    (0, "HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwAsEntityStateEntry.setStatus("current")


class _HwAsEntityAdminStatus_Type(Integer32):
    """Custom type hwAsEntityAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("down", 12),
          ("locked", 2),
          ("loopback", 13),
          ("notSupported", 1),
          ("shuttingDown", 3),
          ("unlocked", 4),
          ("up", 11))
    )


_HwAsEntityAdminStatus_Type.__name__ = "Integer32"
_HwAsEntityAdminStatus_Object = MibTableColumn
hwAsEntityAdminStatus = _HwAsEntityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 9, 1, 1),
    _HwAsEntityAdminStatus_Type()
)
hwAsEntityAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityAdminStatus.setStatus("current")


class _HwAsEntityOperStatus_Type(Integer32):
    """Custom type hwAsEntityOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              11,
              12,
              13,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("connect", 13),
          ("disabled", 2),
          ("down", 12),
          ("enabled", 3),
          ("linkDown", 17),
          ("linkUp", 16),
          ("notSupported", 1),
          ("offline", 4),
          ("protocolUp", 15),
          ("up", 11))
    )


_HwAsEntityOperStatus_Type.__name__ = "Integer32"
_HwAsEntityOperStatus_Object = MibTableColumn
hwAsEntityOperStatus = _HwAsEntityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 9, 1, 2),
    _HwAsEntityOperStatus_Type()
)
hwAsEntityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityOperStatus.setStatus("current")


class _HwAsEntityStandbyStatus_Type(Integer32):
    """Custom type hwAsEntityStandbyStatus based on Integer32"""
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
        *(("coldStandby", 3),
          ("hotStandby", 2),
          ("notSupported", 1),
          ("providingService", 4))
    )


_HwAsEntityStandbyStatus_Type.__name__ = "Integer32"
_HwAsEntityStandbyStatus_Object = MibTableColumn
hwAsEntityStandbyStatus = _HwAsEntityStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 9, 1, 3),
    _HwAsEntityStandbyStatus_Type()
)
hwAsEntityStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityStandbyStatus.setStatus("current")
_HwAsEntityAlarmLight_Type = AlarmStatus
_HwAsEntityAlarmLight_Object = MibTableColumn
hwAsEntityAlarmLight = _HwAsEntityAlarmLight_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 9, 1, 4),
    _HwAsEntityAlarmLight_Type()
)
hwAsEntityAlarmLight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityAlarmLight.setStatus("current")


class _HwAsEntityPortType_Type(Integer32):
    """Custom type hwAsEntityPortType based on Integer32"""
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
        *(("copper", 2),
          ("fiber100", 3),
          ("fiber1000", 4),
          ("fiber10000", 5),
          ("notSupported", 1),
          ("optical", 7),
          ("opticalnotExist", 6))
    )


_HwAsEntityPortType_Type.__name__ = "Integer32"
_HwAsEntityPortType_Object = MibTableColumn
hwAsEntityPortType = _HwAsEntityPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 9, 1, 5),
    _HwAsEntityPortType_Type()
)
hwAsEntityPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntityPortType.setStatus("current")
_HwAsEntityAliasMappingTable_Object = MibTable
hwAsEntityAliasMappingTable = _HwAsEntityAliasMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 10)
)
if mibBuilder.loadTexts:
    hwAsEntityAliasMappingTable.setStatus("current")
_HwAsEntityAliasMappingEntry_Object = MibTableRow
hwAsEntityAliasMappingEntry = _HwAsEntityAliasMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 10, 1)
)
hwAsEntityAliasMappingEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwAsIndex"),
    (0, "HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalIndex"),
    (0, "HUAWEI-UNIMNG-MIB", "hwAsEntryAliasLogicalIndexOrZero"),
)
if mibBuilder.loadTexts:
    hwAsEntityAliasMappingEntry.setStatus("current")
_HwAsEntryAliasLogicalIndexOrZero_Type = Integer32
_HwAsEntryAliasLogicalIndexOrZero_Object = MibTableColumn
hwAsEntryAliasLogicalIndexOrZero = _HwAsEntryAliasLogicalIndexOrZero_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 10, 1, 1),
    _HwAsEntryAliasLogicalIndexOrZero_Type()
)
hwAsEntryAliasLogicalIndexOrZero.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwAsEntryAliasLogicalIndexOrZero.setStatus("current")
_HwAsEntryAliasMappingIdentifier_Type = AutonomousType
_HwAsEntryAliasMappingIdentifier_Object = MibTableColumn
hwAsEntryAliasMappingIdentifier = _HwAsEntryAliasMappingIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 2, 10, 1, 2),
    _HwAsEntryAliasMappingIdentifier_Type()
)
hwAsEntryAliasMappingIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAsEntryAliasMappingIdentifier.setStatus("current")
_HwTopomngObjects_ObjectIdentity = ObjectIdentity
hwTopomngObjects = _HwTopomngObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3)
)


class _HwTopomngExploreTime_Type(Integer32):
    """Custom type hwTopomngExploreTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_HwTopomngExploreTime_Type.__name__ = "Integer32"
_HwTopomngExploreTime_Object = MibScalar
hwTopomngExploreTime = _HwTopomngExploreTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 1),
    _HwTopomngExploreTime_Type()
)
hwTopomngExploreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTopomngExploreTime.setStatus("current")
_HwTopomngLastCollectDuration_Type = Integer32
_HwTopomngLastCollectDuration_Object = MibScalar
hwTopomngLastCollectDuration = _HwTopomngLastCollectDuration_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 2),
    _HwTopomngLastCollectDuration_Type()
)
hwTopomngLastCollectDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTopomngLastCollectDuration.setStatus("current")
_HwTopomngTopoTable_Object = MibTable
hwTopomngTopoTable = _HwTopomngTopoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11)
)
if mibBuilder.loadTexts:
    hwTopomngTopoTable.setStatus("current")
_HwTopomngTopoEntry_Object = MibTableRow
hwTopomngTopoEntry = _HwTopomngTopoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11, 1)
)
hwTopomngTopoEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwTopoLocalHop"),
    (0, "HUAWEI-UNIMNG-MIB", "hwTopoLocalMac"),
    (0, "HUAWEI-UNIMNG-MIB", "hwTopoPeerDeviceIndex"),
)
if mibBuilder.loadTexts:
    hwTopomngTopoEntry.setStatus("current")


class _HwTopoLocalHop_Type(Integer32):
    """Custom type hwTopoLocalHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwTopoLocalHop_Type.__name__ = "Integer32"
_HwTopoLocalHop_Object = MibTableColumn
hwTopoLocalHop = _HwTopoLocalHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11, 1, 1),
    _HwTopoLocalHop_Type()
)
hwTopoLocalHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTopoLocalHop.setStatus("current")
_HwTopoLocalMac_Type = MacAddress
_HwTopoLocalMac_Object = MibTableColumn
hwTopoLocalMac = _HwTopoLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11, 1, 2),
    _HwTopoLocalMac_Type()
)
hwTopoLocalMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTopoLocalMac.setStatus("current")


class _HwTopoPeerDeviceIndex_Type(Integer32):
    """Custom type hwTopoPeerDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwTopoPeerDeviceIndex_Type.__name__ = "Integer32"
_HwTopoPeerDeviceIndex_Object = MibTableColumn
hwTopoPeerDeviceIndex = _HwTopoPeerDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11, 1, 3),
    _HwTopoPeerDeviceIndex_Type()
)
hwTopoPeerDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTopoPeerDeviceIndex.setStatus("current")
_HwTopoPeerMac_Type = MacAddress
_HwTopoPeerMac_Object = MibTableColumn
hwTopoPeerMac = _HwTopoPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11, 1, 4),
    _HwTopoPeerMac_Type()
)
hwTopoPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTopoPeerMac.setStatus("current")


class _HwTopoLocalPortName_Type(OctetString):
    """Custom type hwTopoLocalPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwTopoLocalPortName_Type.__name__ = "OctetString"
_HwTopoLocalPortName_Object = MibTableColumn
hwTopoLocalPortName = _HwTopoLocalPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11, 1, 5),
    _HwTopoLocalPortName_Type()
)
hwTopoLocalPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTopoLocalPortName.setStatus("current")


class _HwTopoPeerPortName_Type(OctetString):
    """Custom type hwTopoPeerPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwTopoPeerPortName_Type.__name__ = "OctetString"
_HwTopoPeerPortName_Object = MibTableColumn
hwTopoPeerPortName = _HwTopoPeerPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11, 1, 6),
    _HwTopoPeerPortName_Type()
)
hwTopoPeerPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTopoPeerPortName.setStatus("current")


class _HwTopoLocalTrunkId_Type(Integer32):
    """Custom type hwTopoLocalTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwTopoLocalTrunkId_Type.__name__ = "Integer32"
_HwTopoLocalTrunkId_Object = MibTableColumn
hwTopoLocalTrunkId = _HwTopoLocalTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11, 1, 7),
    _HwTopoLocalTrunkId_Type()
)
hwTopoLocalTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTopoLocalTrunkId.setStatus("current")


class _HwTopoPeerTrunkId_Type(Integer32):
    """Custom type hwTopoPeerTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwTopoPeerTrunkId_Type.__name__ = "Integer32"
_HwTopoPeerTrunkId_Object = MibTableColumn
hwTopoPeerTrunkId = _HwTopoPeerTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11, 1, 8),
    _HwTopoPeerTrunkId_Type()
)
hwTopoPeerTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTopoPeerTrunkId.setStatus("current")


class _HwTopoLocalRole_Type(Integer32):
    """Custom type hwTopoLocalRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("roleAP", 3),
          ("roleAS", 2),
          ("roleUC", 1))
    )


_HwTopoLocalRole_Type.__name__ = "Integer32"
_HwTopoLocalRole_Object = MibTableColumn
hwTopoLocalRole = _HwTopoLocalRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11, 1, 9),
    _HwTopoLocalRole_Type()
)
hwTopoLocalRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTopoLocalRole.setStatus("current")


class _HwTopoPeerRole_Type(Integer32):
    """Custom type hwTopoPeerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("roleAP", 3),
          ("roleAS", 2),
          ("roleUC", 1))
    )


_HwTopoPeerRole_Type.__name__ = "Integer32"
_HwTopoPeerRole_Object = MibTableColumn
hwTopoPeerRole = _HwTopoPeerRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 3, 11, 1, 10),
    _HwTopoPeerRole_Type()
)
hwTopoPeerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTopoPeerRole.setStatus("current")
_HwMbrmngObjects_ObjectIdentity = ObjectIdentity
hwMbrmngObjects = _HwMbrmngObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 4)
)
_HwMbrMngFabricPortTable_Object = MibTable
hwMbrMngFabricPortTable = _HwMbrMngFabricPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 4, 2)
)
if mibBuilder.loadTexts:
    hwMbrMngFabricPortTable.setStatus("current")
_HwMbrMngFabricPortEntry_Object = MibTableRow
hwMbrMngFabricPortEntry = _HwMbrMngFabricPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 4, 2, 1)
)
hwMbrMngFabricPortEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwMbrMngASId"),
    (0, "HUAWEI-UNIMNG-MIB", "hwMbrMngFabricPortId"),
)
if mibBuilder.loadTexts:
    hwMbrMngFabricPortEntry.setStatus("current")


class _HwMbrMngASId_Type(Integer32):
    """Custom type hwMbrMngASId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMbrMngASId_Type.__name__ = "Integer32"
_HwMbrMngASId_Object = MibTableColumn
hwMbrMngASId = _HwMbrMngASId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 4, 2, 1, 1),
    _HwMbrMngASId_Type()
)
hwMbrMngASId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMbrMngASId.setStatus("current")


class _HwMbrMngFabricPortId_Type(Integer32):
    """Custom type hwMbrMngFabricPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwMbrMngFabricPortId_Type.__name__ = "Integer32"
_HwMbrMngFabricPortId_Object = MibTableColumn
hwMbrMngFabricPortId = _HwMbrMngFabricPortId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 4, 2, 1, 2),
    _HwMbrMngFabricPortId_Type()
)
hwMbrMngFabricPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMbrMngFabricPortId.setStatus("current")


class _HwMbrMngFabricPortMemberIfName_Type(OctetString):
    """Custom type hwMbrMngFabricPortMemberIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwMbrMngFabricPortMemberIfName_Type.__name__ = "OctetString"
_HwMbrMngFabricPortMemberIfName_Object = MibTableColumn
hwMbrMngFabricPortMemberIfName = _HwMbrMngFabricPortMemberIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 4, 2, 1, 3),
    _HwMbrMngFabricPortMemberIfName_Type()
)
hwMbrMngFabricPortMemberIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMbrMngFabricPortMemberIfName.setStatus("current")


class _HwMbrMngFabricPortDirection_Type(Integer32):
    """Custom type hwMbrMngFabricPortDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downDirection", 1),
          ("upDirection", 2))
    )


_HwMbrMngFabricPortDirection_Type.__name__ = "Integer32"
_HwMbrMngFabricPortDirection_Object = MibTableColumn
hwMbrMngFabricPortDirection = _HwMbrMngFabricPortDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 4, 2, 1, 4),
    _HwMbrMngFabricPortDirection_Type()
)
hwMbrMngFabricPortDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMbrMngFabricPortDirection.setStatus("current")


class _HwMbrMngFabricPortIndirectFlag_Type(Integer32):
    """Custom type hwMbrMngFabricPortIndirectFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 2),
          ("indirect", 1))
    )


_HwMbrMngFabricPortIndirectFlag_Type.__name__ = "Integer32"
_HwMbrMngFabricPortIndirectFlag_Object = MibTableColumn
hwMbrMngFabricPortIndirectFlag = _HwMbrMngFabricPortIndirectFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 4, 2, 1, 5),
    _HwMbrMngFabricPortIndirectFlag_Type()
)
hwMbrMngFabricPortIndirectFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMbrMngFabricPortIndirectFlag.setStatus("current")


class _HwMbrMngFabricPortDescription_Type(OctetString):
    """Custom type hwMbrMngFabricPortDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwMbrMngFabricPortDescription_Type.__name__ = "OctetString"
_HwMbrMngFabricPortDescription_Object = MibTableColumn
hwMbrMngFabricPortDescription = _HwMbrMngFabricPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 4, 2, 1, 6),
    _HwMbrMngFabricPortDescription_Type()
)
hwMbrMngFabricPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMbrMngFabricPortDescription.setStatus("current")
_HwVermngObjects_ObjectIdentity = ObjectIdentity
hwVermngObjects = _HwVermngObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5)
)
_HwVermngGlobalObjects_ObjectIdentity = ObjectIdentity
hwVermngGlobalObjects = _HwVermngGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 1)
)


class _HwVermngFileServerType_Type(Integer32):
    """Custom type hwVermngFileServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("none", 255),
          ("sftp", 2))
    )


_HwVermngFileServerType_Type.__name__ = "Integer32"
_HwVermngFileServerType_Object = MibScalar
hwVermngFileServerType = _HwVermngFileServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 1, 1),
    _HwVermngFileServerType_Type()
)
hwVermngFileServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngFileServerType.setStatus("current")
_HwVermngUpgradeInfoTable_Object = MibTable
hwVermngUpgradeInfoTable = _HwVermngUpgradeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2)
)
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoTable.setStatus("current")
_HwVermngUpgradeInfoEntry_Object = MibTableRow
hwVermngUpgradeInfoEntry = _HwVermngUpgradeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1)
)
hwVermngUpgradeInfoEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsIndex"),
)
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoEntry.setStatus("current")


class _HwVermngUpgradeInfoAsIndex_Type(Integer32):
    """Custom type hwVermngUpgradeInfoAsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwVermngUpgradeInfoAsIndex_Type.__name__ = "Integer32"
_HwVermngUpgradeInfoAsIndex_Object = MibTableColumn
hwVermngUpgradeInfoAsIndex = _HwVermngUpgradeInfoAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 1),
    _HwVermngUpgradeInfoAsIndex_Type()
)
hwVermngUpgradeInfoAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsIndex.setStatus("current")
_HwVermngUpgradeInfoAsName_Type = DisplayString
_HwVermngUpgradeInfoAsName_Object = MibTableColumn
hwVermngUpgradeInfoAsName = _HwVermngUpgradeInfoAsName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 2),
    _HwVermngUpgradeInfoAsName_Type()
)
hwVermngUpgradeInfoAsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsName.setStatus("current")
_HwVermngUpgradeInfoAsSysSoftware_Type = DisplayString
_HwVermngUpgradeInfoAsSysSoftware_Object = MibTableColumn
hwVermngUpgradeInfoAsSysSoftware = _HwVermngUpgradeInfoAsSysSoftware_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 3),
    _HwVermngUpgradeInfoAsSysSoftware_Type()
)
hwVermngUpgradeInfoAsSysSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsSysSoftware.setStatus("current")
_HwVermngUpgradeInfoAsSysSoftwareVer_Type = DisplayString
_HwVermngUpgradeInfoAsSysSoftwareVer_Object = MibTableColumn
hwVermngUpgradeInfoAsSysSoftwareVer = _HwVermngUpgradeInfoAsSysSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 4),
    _HwVermngUpgradeInfoAsSysSoftwareVer_Type()
)
hwVermngUpgradeInfoAsSysSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsSysSoftwareVer.setStatus("current")
_HwVermngUpgradeInfoAsSysPatch_Type = DisplayString
_HwVermngUpgradeInfoAsSysPatch_Object = MibTableColumn
hwVermngUpgradeInfoAsSysPatch = _HwVermngUpgradeInfoAsSysPatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 5),
    _HwVermngUpgradeInfoAsSysPatch_Type()
)
hwVermngUpgradeInfoAsSysPatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsSysPatch.setStatus("current")
_HwVermngUpgradeInfoAsDownloadSoftware_Type = DisplayString
_HwVermngUpgradeInfoAsDownloadSoftware_Object = MibTableColumn
hwVermngUpgradeInfoAsDownloadSoftware = _HwVermngUpgradeInfoAsDownloadSoftware_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 6),
    _HwVermngUpgradeInfoAsDownloadSoftware_Type()
)
hwVermngUpgradeInfoAsDownloadSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsDownloadSoftware.setStatus("current")
_HwVermngUpgradeInfoAsDownloadSoftwareVer_Type = DisplayString
_HwVermngUpgradeInfoAsDownloadSoftwareVer_Object = MibTableColumn
hwVermngUpgradeInfoAsDownloadSoftwareVer = _HwVermngUpgradeInfoAsDownloadSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 7),
    _HwVermngUpgradeInfoAsDownloadSoftwareVer_Type()
)
hwVermngUpgradeInfoAsDownloadSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsDownloadSoftwareVer.setStatus("current")
_HwVermngUpgradeInfoAsDownloadPatch_Type = DisplayString
_HwVermngUpgradeInfoAsDownloadPatch_Object = MibTableColumn
hwVermngUpgradeInfoAsDownloadPatch = _HwVermngUpgradeInfoAsDownloadPatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 8),
    _HwVermngUpgradeInfoAsDownloadPatch_Type()
)
hwVermngUpgradeInfoAsDownloadPatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsDownloadPatch.setStatus("current")


class _HwVermngUpgradeInfoAsUpgradeState_Type(Integer32):
    """Custom type hwVermngUpgradeInfoAsUpgradeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noUpgrade", 1),
          ("none", 255),
          ("upgrading", 2))
    )


_HwVermngUpgradeInfoAsUpgradeState_Type.__name__ = "Integer32"
_HwVermngUpgradeInfoAsUpgradeState_Object = MibTableColumn
hwVermngUpgradeInfoAsUpgradeState = _HwVermngUpgradeInfoAsUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 9),
    _HwVermngUpgradeInfoAsUpgradeState_Type()
)
hwVermngUpgradeInfoAsUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsUpgradeState.setStatus("current")


class _HwVermngUpgradeInfoAsUpgradeType_Type(Integer32):
    """Custom type hwVermngUpgradeInfoAsUpgradeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("manual", 2),
          ("none", 255),
          ("verSync", 1))
    )


_HwVermngUpgradeInfoAsUpgradeType_Type.__name__ = "Integer32"
_HwVermngUpgradeInfoAsUpgradeType_Object = MibTableColumn
hwVermngUpgradeInfoAsUpgradeType = _HwVermngUpgradeInfoAsUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 10),
    _HwVermngUpgradeInfoAsUpgradeType_Type()
)
hwVermngUpgradeInfoAsUpgradeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsUpgradeType.setStatus("current")


class _HwVermngUpgradeInfoAsFilePhase_Type(Integer32):
    """Custom type hwVermngUpgradeInfoAsFilePhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 255),
          ("patch", 2),
          ("systemSoftware", 1))
    )


_HwVermngUpgradeInfoAsFilePhase_Type.__name__ = "Integer32"
_HwVermngUpgradeInfoAsFilePhase_Object = MibTableColumn
hwVermngUpgradeInfoAsFilePhase = _HwVermngUpgradeInfoAsFilePhase_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 11),
    _HwVermngUpgradeInfoAsFilePhase_Type()
)
hwVermngUpgradeInfoAsFilePhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsFilePhase.setStatus("current")


class _HwVermngUpgradeInfoAsUpgradePhase_Type(Integer32):
    """Custom type hwVermngUpgradeInfoAsUpgradePhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("activateFile", 3),
          ("downloadFile", 1),
          ("none", 255),
          ("reboot", 4),
          ("wait", 2))
    )


_HwVermngUpgradeInfoAsUpgradePhase_Type.__name__ = "Integer32"
_HwVermngUpgradeInfoAsUpgradePhase_Object = MibTableColumn
hwVermngUpgradeInfoAsUpgradePhase = _HwVermngUpgradeInfoAsUpgradePhase_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 12),
    _HwVermngUpgradeInfoAsUpgradePhase_Type()
)
hwVermngUpgradeInfoAsUpgradePhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsUpgradePhase.setStatus("current")


class _HwVermngUpgradeInfoAsUpgradeResult_Type(Integer32):
    """Custom type hwVermngUpgradeInfoAsUpgradeResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("none", 255),
          ("successfully", 1))
    )


_HwVermngUpgradeInfoAsUpgradeResult_Type.__name__ = "Integer32"
_HwVermngUpgradeInfoAsUpgradeResult_Object = MibTableColumn
hwVermngUpgradeInfoAsUpgradeResult = _HwVermngUpgradeInfoAsUpgradeResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 13),
    _HwVermngUpgradeInfoAsUpgradeResult_Type()
)
hwVermngUpgradeInfoAsUpgradeResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsUpgradeResult.setStatus("current")
_HwVermngUpgradeInfoAsErrorCode_Type = Integer32
_HwVermngUpgradeInfoAsErrorCode_Object = MibTableColumn
hwVermngUpgradeInfoAsErrorCode = _HwVermngUpgradeInfoAsErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 14),
    _HwVermngUpgradeInfoAsErrorCode_Type()
)
hwVermngUpgradeInfoAsErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsErrorCode.setStatus("current")
_HwVermngUpgradeInfoAsErrorDescr_Type = DisplayString
_HwVermngUpgradeInfoAsErrorDescr_Object = MibTableColumn
hwVermngUpgradeInfoAsErrorDescr = _HwVermngUpgradeInfoAsErrorDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 2, 1, 15),
    _HwVermngUpgradeInfoAsErrorDescr_Type()
)
hwVermngUpgradeInfoAsErrorDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoAsErrorDescr.setStatus("current")
_HwVermngAsTypeCfgInfoTable_Object = MibTable
hwVermngAsTypeCfgInfoTable = _HwVermngAsTypeCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 3)
)
if mibBuilder.loadTexts:
    hwVermngAsTypeCfgInfoTable.setStatus("current")
_HwVermngAsTypeCfgInfoEntry_Object = MibTableRow
hwVermngAsTypeCfgInfoEntry = _HwVermngAsTypeCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 3, 1)
)
hwVermngAsTypeCfgInfoEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwVermngAsTypeCfgInfoAsTypeIndex"),
)
if mibBuilder.loadTexts:
    hwVermngAsTypeCfgInfoEntry.setStatus("current")


class _HwVermngAsTypeCfgInfoAsTypeIndex_Type(Integer32):
    """Custom type hwVermngAsTypeCfgInfoAsTypeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwVermngAsTypeCfgInfoAsTypeIndex_Type.__name__ = "Integer32"
_HwVermngAsTypeCfgInfoAsTypeIndex_Object = MibTableColumn
hwVermngAsTypeCfgInfoAsTypeIndex = _HwVermngAsTypeCfgInfoAsTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 3, 1, 1),
    _HwVermngAsTypeCfgInfoAsTypeIndex_Type()
)
hwVermngAsTypeCfgInfoAsTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVermngAsTypeCfgInfoAsTypeIndex.setStatus("current")
_HwVermngAsTypeCfgInfoAsTypeName_Type = DisplayString
_HwVermngAsTypeCfgInfoAsTypeName_Object = MibTableColumn
hwVermngAsTypeCfgInfoAsTypeName = _HwVermngAsTypeCfgInfoAsTypeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 3, 1, 2),
    _HwVermngAsTypeCfgInfoAsTypeName_Type()
)
hwVermngAsTypeCfgInfoAsTypeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVermngAsTypeCfgInfoAsTypeName.setStatus("current")
_HwVermngAsTypeCfgInfoSystemSoftware_Type = DisplayString
_HwVermngAsTypeCfgInfoSystemSoftware_Object = MibTableColumn
hwVermngAsTypeCfgInfoSystemSoftware = _HwVermngAsTypeCfgInfoSystemSoftware_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 3, 1, 3),
    _HwVermngAsTypeCfgInfoSystemSoftware_Type()
)
hwVermngAsTypeCfgInfoSystemSoftware.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVermngAsTypeCfgInfoSystemSoftware.setStatus("current")
_HwVermngAsTypeCfgInfoSystemSoftwareVer_Type = DisplayString
_HwVermngAsTypeCfgInfoSystemSoftwareVer_Object = MibTableColumn
hwVermngAsTypeCfgInfoSystemSoftwareVer = _HwVermngAsTypeCfgInfoSystemSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 3, 1, 4),
    _HwVermngAsTypeCfgInfoSystemSoftwareVer_Type()
)
hwVermngAsTypeCfgInfoSystemSoftwareVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVermngAsTypeCfgInfoSystemSoftwareVer.setStatus("current")
_HwVermngAsTypeCfgInfoPatch_Type = DisplayString
_HwVermngAsTypeCfgInfoPatch_Object = MibTableColumn
hwVermngAsTypeCfgInfoPatch = _HwVermngAsTypeCfgInfoPatch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 3, 1, 5),
    _HwVermngAsTypeCfgInfoPatch_Type()
)
hwVermngAsTypeCfgInfoPatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVermngAsTypeCfgInfoPatch.setStatus("current")
_HwVermngAsTypeCfgInfoRowStatus_Type = RowStatus
_HwVermngAsTypeCfgInfoRowStatus_Object = MibTableColumn
hwVermngAsTypeCfgInfoRowStatus = _HwVermngAsTypeCfgInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 5, 3, 1, 50),
    _HwVermngAsTypeCfgInfoRowStatus_Type()
)
hwVermngAsTypeCfgInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVermngAsTypeCfgInfoRowStatus.setStatus("current")
_HwTplmObjects_ObjectIdentity = ObjectIdentity
hwTplmObjects = _HwTplmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6)
)
_HwTplmASGroupTable_Object = MibTable
hwTplmASGroupTable = _HwTplmASGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 11)
)
if mibBuilder.loadTexts:
    hwTplmASGroupTable.setStatus("current")
_HwTplmASGroupEntry_Object = MibTableRow
hwTplmASGroupEntry = _HwTplmASGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 11, 1)
)
hwTplmASGroupEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwTplmASGroupIndex"),
)
if mibBuilder.loadTexts:
    hwTplmASGroupEntry.setStatus("current")


class _HwTplmASGroupIndex_Type(Integer32):
    """Custom type hwTplmASGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwTplmASGroupIndex_Type.__name__ = "Integer32"
_HwTplmASGroupIndex_Object = MibTableColumn
hwTplmASGroupIndex = _HwTplmASGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 11, 1, 1),
    _HwTplmASGroupIndex_Type()
)
hwTplmASGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTplmASGroupIndex.setStatus("current")


class _HwTplmASGroupName_Type(OctetString):
    """Custom type hwTplmASGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwTplmASGroupName_Type.__name__ = "OctetString"
_HwTplmASGroupName_Object = MibTableColumn
hwTplmASGroupName = _HwTplmASGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 11, 1, 2),
    _HwTplmASGroupName_Type()
)
hwTplmASGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmASGroupName.setStatus("current")


class _HwTplmASAdminProfileName_Type(OctetString):
    """Custom type hwTplmASAdminProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwTplmASAdminProfileName_Type.__name__ = "OctetString"
_HwTplmASAdminProfileName_Object = MibTableColumn
hwTplmASAdminProfileName = _HwTplmASAdminProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 11, 1, 3),
    _HwTplmASAdminProfileName_Type()
)
hwTplmASAdminProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmASAdminProfileName.setStatus("current")


class _HwTplmASGroupProfileStatus_Type(Integer32):
    """Custom type hwTplmASGroupProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwTplmASGroupProfileStatus_Type.__name__ = "Integer32"
_HwTplmASGroupProfileStatus_Object = MibTableColumn
hwTplmASGroupProfileStatus = _HwTplmASGroupProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 11, 1, 4),
    _HwTplmASGroupProfileStatus_Type()
)
hwTplmASGroupProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmASGroupProfileStatus.setStatus("current")
_HwTplmASGroupRowStatus_Type = RowStatus
_HwTplmASGroupRowStatus_Object = MibTableColumn
hwTplmASGroupRowStatus = _HwTplmASGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 11, 1, 11),
    _HwTplmASGroupRowStatus_Type()
)
hwTplmASGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmASGroupRowStatus.setStatus("current")
_HwTplmASTable_Object = MibTable
hwTplmASTable = _HwTplmASTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 12)
)
if mibBuilder.loadTexts:
    hwTplmASTable.setStatus("current")
_HwTplmASEntry_Object = MibTableRow
hwTplmASEntry = _HwTplmASEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 12, 1)
)
hwTplmASEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwTplmASId"),
)
if mibBuilder.loadTexts:
    hwTplmASEntry.setStatus("current")


class _HwTplmASId_Type(Integer32):
    """Custom type hwTplmASId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwTplmASId_Type.__name__ = "Integer32"
_HwTplmASId_Object = MibTableColumn
hwTplmASId = _HwTplmASId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 12, 1, 1),
    _HwTplmASId_Type()
)
hwTplmASId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTplmASId.setStatus("current")


class _HwTplmASASGroupName_Type(OctetString):
    """Custom type hwTplmASASGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwTplmASASGroupName_Type.__name__ = "OctetString"
_HwTplmASASGroupName_Object = MibTableColumn
hwTplmASASGroupName = _HwTplmASASGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 12, 1, 2),
    _HwTplmASASGroupName_Type()
)
hwTplmASASGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmASASGroupName.setStatus("current")
_HwTplmASRowStatus_Type = RowStatus
_HwTplmASRowStatus_Object = MibTableColumn
hwTplmASRowStatus = _HwTplmASRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 12, 1, 11),
    _HwTplmASRowStatus_Type()
)
hwTplmASRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmASRowStatus.setStatus("current")
_HwTplmPortGroupTable_Object = MibTable
hwTplmPortGroupTable = _HwTplmPortGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 13)
)
if mibBuilder.loadTexts:
    hwTplmPortGroupTable.setStatus("current")
_HwTplmPortGroupEntry_Object = MibTableRow
hwTplmPortGroupEntry = _HwTplmPortGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 13, 1)
)
hwTplmPortGroupEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwTplmPortGroupIndex"),
)
if mibBuilder.loadTexts:
    hwTplmPortGroupEntry.setStatus("current")


class _HwTplmPortGroupIndex_Type(Integer32):
    """Custom type hwTplmPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 257),
    )


_HwTplmPortGroupIndex_Type.__name__ = "Integer32"
_HwTplmPortGroupIndex_Object = MibTableColumn
hwTplmPortGroupIndex = _HwTplmPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 13, 1, 1),
    _HwTplmPortGroupIndex_Type()
)
hwTplmPortGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTplmPortGroupIndex.setStatus("current")


class _HwTplmPortGroupName_Type(OctetString):
    """Custom type hwTplmPortGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwTplmPortGroupName_Type.__name__ = "OctetString"
_HwTplmPortGroupName_Object = MibTableColumn
hwTplmPortGroupName = _HwTplmPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 13, 1, 2),
    _HwTplmPortGroupName_Type()
)
hwTplmPortGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmPortGroupName.setStatus("current")


class _HwTplmPortGroupType_Type(Integer32):
    """Custom type hwTplmPortGroupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ap", 2),
          ("service", 1))
    )


_HwTplmPortGroupType_Type.__name__ = "Integer32"
_HwTplmPortGroupType_Object = MibTableColumn
hwTplmPortGroupType = _HwTplmPortGroupType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 13, 1, 3),
    _HwTplmPortGroupType_Type()
)
hwTplmPortGroupType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmPortGroupType.setStatus("current")


class _HwTplmPortGroupNetworkBasicProfile_Type(OctetString):
    """Custom type hwTplmPortGroupNetworkBasicProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwTplmPortGroupNetworkBasicProfile_Type.__name__ = "OctetString"
_HwTplmPortGroupNetworkBasicProfile_Object = MibTableColumn
hwTplmPortGroupNetworkBasicProfile = _HwTplmPortGroupNetworkBasicProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 13, 1, 4),
    _HwTplmPortGroupNetworkBasicProfile_Type()
)
hwTplmPortGroupNetworkBasicProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmPortGroupNetworkBasicProfile.setStatus("current")


class _HwTplmPortGroupNetworkEnhancedProfile_Type(OctetString):
    """Custom type hwTplmPortGroupNetworkEnhancedProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwTplmPortGroupNetworkEnhancedProfile_Type.__name__ = "OctetString"
_HwTplmPortGroupNetworkEnhancedProfile_Object = MibTableColumn
hwTplmPortGroupNetworkEnhancedProfile = _HwTplmPortGroupNetworkEnhancedProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 13, 1, 5),
    _HwTplmPortGroupNetworkEnhancedProfile_Type()
)
hwTplmPortGroupNetworkEnhancedProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmPortGroupNetworkEnhancedProfile.setStatus("current")


class _HwTplmPortGroupUserAccessProfile_Type(OctetString):
    """Custom type hwTplmPortGroupUserAccessProfile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwTplmPortGroupUserAccessProfile_Type.__name__ = "OctetString"
_HwTplmPortGroupUserAccessProfile_Object = MibTableColumn
hwTplmPortGroupUserAccessProfile = _HwTplmPortGroupUserAccessProfile_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 13, 1, 6),
    _HwTplmPortGroupUserAccessProfile_Type()
)
hwTplmPortGroupUserAccessProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmPortGroupUserAccessProfile.setStatus("current")


class _HwTplmPortGroupProfileStatus_Type(Integer32):
    """Custom type hwTplmPortGroupProfileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwTplmPortGroupProfileStatus_Type.__name__ = "Integer32"
_HwTplmPortGroupProfileStatus_Object = MibTableColumn
hwTplmPortGroupProfileStatus = _HwTplmPortGroupProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 13, 1, 7),
    _HwTplmPortGroupProfileStatus_Type()
)
hwTplmPortGroupProfileStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmPortGroupProfileStatus.setStatus("current")
_HwTplmPortGroupRowStatus_Type = RowStatus
_HwTplmPortGroupRowStatus_Object = MibTableColumn
hwTplmPortGroupRowStatus = _HwTplmPortGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 13, 1, 11),
    _HwTplmPortGroupRowStatus_Type()
)
hwTplmPortGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmPortGroupRowStatus.setStatus("current")
_HwTplmPortTable_Object = MibTable
hwTplmPortTable = _HwTplmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 14)
)
if mibBuilder.loadTexts:
    hwTplmPortTable.setStatus("current")
_HwTplmPortEntry_Object = MibTableRow
hwTplmPortEntry = _HwTplmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 14, 1)
)
hwTplmPortEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwTplmPortIfIndex"),
)
if mibBuilder.loadTexts:
    hwTplmPortEntry.setStatus("current")
_HwTplmPortIfIndex_Type = Integer32
_HwTplmPortIfIndex_Object = MibTableColumn
hwTplmPortIfIndex = _HwTplmPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 14, 1, 1),
    _HwTplmPortIfIndex_Type()
)
hwTplmPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTplmPortIfIndex.setStatus("current")


class _HwTplmPortPortGroupName_Type(OctetString):
    """Custom type hwTplmPortPortGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwTplmPortPortGroupName_Type.__name__ = "OctetString"
_HwTplmPortPortGroupName_Object = MibTableColumn
hwTplmPortPortGroupName = _HwTplmPortPortGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 14, 1, 2),
    _HwTplmPortPortGroupName_Type()
)
hwTplmPortPortGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmPortPortGroupName.setStatus("current")
_HwTplmPortRowStatus_Type = RowStatus
_HwTplmPortRowStatus_Object = MibTableColumn
hwTplmPortRowStatus = _HwTplmPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 14, 1, 11),
    _HwTplmPortRowStatus_Type()
)
hwTplmPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwTplmPortRowStatus.setStatus("current")
_HwTplmConfigManagement_ObjectIdentity = ObjectIdentity
hwTplmConfigManagement = _HwTplmConfigManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 15)
)


class _HwTplmConfigCommitAll_Type(Integer32):
    """Custom type hwTplmConfigCommitAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("commit", 1)
    )


_HwTplmConfigCommitAll_Type.__name__ = "Integer32"
_HwTplmConfigCommitAll_Object = MibScalar
hwTplmConfigCommitAll = _HwTplmConfigCommitAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 15, 1),
    _HwTplmConfigCommitAll_Type()
)
hwTplmConfigCommitAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTplmConfigCommitAll.setStatus("current")
_HwTplmConfigManagementTable_Object = MibTable
hwTplmConfigManagementTable = _HwTplmConfigManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 15, 2)
)
if mibBuilder.loadTexts:
    hwTplmConfigManagementTable.setStatus("current")
_HwTplmConfigManagementEntry_Object = MibTableRow
hwTplmConfigManagementEntry = _HwTplmConfigManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 15, 2, 1)
)
hwTplmConfigManagementEntry.setIndexNames(
    (0, "HUAWEI-UNIMNG-MIB", "hwTplmConfigManagementASId"),
)
if mibBuilder.loadTexts:
    hwTplmConfigManagementEntry.setStatus("current")


class _HwTplmConfigManagementASId_Type(Integer32):
    """Custom type hwTplmConfigManagementASId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwTplmConfigManagementASId_Type.__name__ = "Integer32"
_HwTplmConfigManagementASId_Object = MibTableColumn
hwTplmConfigManagementASId = _HwTplmConfigManagementASId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 15, 2, 1, 1),
    _HwTplmConfigManagementASId_Type()
)
hwTplmConfigManagementASId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwTplmConfigManagementASId.setStatus("current")


class _HwTplmConfigManagementCommit_Type(Integer32):
    """Custom type hwTplmConfigManagementCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("commit", 1)
    )


_HwTplmConfigManagementCommit_Type.__name__ = "Integer32"
_HwTplmConfigManagementCommit_Object = MibTableColumn
hwTplmConfigManagementCommit = _HwTplmConfigManagementCommit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 6, 15, 2, 1, 2),
    _HwTplmConfigManagementCommit_Type()
)
hwTplmConfigManagementCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwTplmConfigManagementCommit.setStatus("current")
_HwUnimngNotification_ObjectIdentity = ObjectIdentity
hwUnimngNotification = _HwUnimngNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31)
)
_HwTopomngTrap_ObjectIdentity = ObjectIdentity
hwTopomngTrap = _HwTopomngTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1)
)
_HwTopomngTrapObjects_ObjectIdentity = ObjectIdentity
hwTopomngTrapObjects = _HwTopomngTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1, 1)
)
_HwTopomngTrapLocalMac_Type = MacAddress
_HwTopomngTrapLocalMac_Object = MibScalar
hwTopomngTrapLocalMac = _HwTopomngTrapLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1, 1, 1),
    _HwTopomngTrapLocalMac_Type()
)
hwTopomngTrapLocalMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTopomngTrapLocalMac.setStatus("current")


class _HwTopomngTrapLocalPortName_Type(OctetString):
    """Custom type hwTopomngTrapLocalPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwTopomngTrapLocalPortName_Type.__name__ = "OctetString"
_HwTopomngTrapLocalPortName_Object = MibScalar
hwTopomngTrapLocalPortName = _HwTopomngTrapLocalPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1, 1, 2),
    _HwTopomngTrapLocalPortName_Type()
)
hwTopomngTrapLocalPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTopomngTrapLocalPortName.setStatus("current")


class _HwTopomngTrapLocalTrunkId_Type(Integer32):
    """Custom type hwTopomngTrapLocalTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwTopomngTrapLocalTrunkId_Type.__name__ = "Integer32"
_HwTopomngTrapLocalTrunkId_Object = MibScalar
hwTopomngTrapLocalTrunkId = _HwTopomngTrapLocalTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1, 1, 3),
    _HwTopomngTrapLocalTrunkId_Type()
)
hwTopomngTrapLocalTrunkId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTopomngTrapLocalTrunkId.setStatus("current")
_HwTopomngTrapPeerMac_Type = MacAddress
_HwTopomngTrapPeerMac_Object = MibScalar
hwTopomngTrapPeerMac = _HwTopomngTrapPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1, 1, 4),
    _HwTopomngTrapPeerMac_Type()
)
hwTopomngTrapPeerMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTopomngTrapPeerMac.setStatus("current")


class _HwTopomngTrapPeerPortName_Type(OctetString):
    """Custom type hwTopomngTrapPeerPortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwTopomngTrapPeerPortName_Type.__name__ = "OctetString"
_HwTopomngTrapPeerPortName_Object = MibScalar
hwTopomngTrapPeerPortName = _HwTopomngTrapPeerPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1, 1, 5),
    _HwTopomngTrapPeerPortName_Type()
)
hwTopomngTrapPeerPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTopomngTrapPeerPortName.setStatus("current")


class _HwTopomngTrapPeerTrunkId_Type(Integer32):
    """Custom type hwTopomngTrapPeerTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwTopomngTrapPeerTrunkId_Type.__name__ = "Integer32"
_HwTopomngTrapPeerTrunkId_Object = MibScalar
hwTopomngTrapPeerTrunkId = _HwTopomngTrapPeerTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1, 1, 6),
    _HwTopomngTrapPeerTrunkId_Type()
)
hwTopomngTrapPeerTrunkId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTopomngTrapPeerTrunkId.setStatus("current")


class _HwTopomngTrapReason_Type(OctetString):
    """Custom type hwTopomngTrapReason based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwTopomngTrapReason_Type.__name__ = "OctetString"
_HwTopomngTrapReason_Object = MibScalar
hwTopomngTrapReason = _HwTopomngTrapReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1, 1, 7),
    _HwTopomngTrapReason_Type()
)
hwTopomngTrapReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTopomngTrapReason.setStatus("current")
_HwTopomngTraps_ObjectIdentity = ObjectIdentity
hwTopomngTraps = _HwTopomngTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1, 2)
)
_HwAsmngTrap_ObjectIdentity = ObjectIdentity
hwAsmngTrap = _HwAsmngTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2)
)
_HwAsmngTrapObjects_ObjectIdentity = ObjectIdentity
hwAsmngTrapObjects = _HwAsmngTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1)
)
_HwAsmngTrapAsIndex_Type = Integer32
_HwAsmngTrapAsIndex_Object = MibScalar
hwAsmngTrapAsIndex = _HwAsmngTrapAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 1),
    _HwAsmngTrapAsIndex_Type()
)
hwAsmngTrapAsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsIndex.setStatus("current")
_HwAsmngTrapAsModel_Type = OctetString
_HwAsmngTrapAsModel_Object = MibScalar
hwAsmngTrapAsModel = _HwAsmngTrapAsModel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 2),
    _HwAsmngTrapAsModel_Type()
)
hwAsmngTrapAsModel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsModel.setStatus("current")
_HwAsmngTrapAsSysName_Type = OctetString
_HwAsmngTrapAsSysName_Object = MibScalar
hwAsmngTrapAsSysName = _HwAsmngTrapAsSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 3),
    _HwAsmngTrapAsSysName_Type()
)
hwAsmngTrapAsSysName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsSysName.setStatus("current")
_HwAsmngTrapAsMac_Type = MacAddress
_HwAsmngTrapAsMac_Object = MibScalar
hwAsmngTrapAsMac = _HwAsmngTrapAsMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 4),
    _HwAsmngTrapAsMac_Type()
)
hwAsmngTrapAsMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsMac.setStatus("current")
_HwAsmngTrapAsSn_Type = OctetString
_HwAsmngTrapAsSn_Object = MibScalar
hwAsmngTrapAsSn = _HwAsmngTrapAsSn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 5),
    _HwAsmngTrapAsSn_Type()
)
hwAsmngTrapAsSn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsSn.setStatus("current")
_HwAsmngTrapAsIfIndex_Type = Integer32
_HwAsmngTrapAsIfIndex_Object = MibScalar
hwAsmngTrapAsIfIndex = _HwAsmngTrapAsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 6),
    _HwAsmngTrapAsIfIndex_Type()
)
hwAsmngTrapAsIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsIfIndex.setStatus("current")
_HwAsmngTrapAsIfOperStatus_Type = Integer32
_HwAsmngTrapAsIfOperStatus_Object = MibScalar
hwAsmngTrapAsIfOperStatus = _HwAsmngTrapAsIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 7),
    _HwAsmngTrapAsIfOperStatus_Type()
)
hwAsmngTrapAsIfOperStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsIfOperStatus.setStatus("current")
_HwAsmngTrapAsFaultTimes_Type = Integer32
_HwAsmngTrapAsFaultTimes_Object = MibScalar
hwAsmngTrapAsFaultTimes = _HwAsmngTrapAsFaultTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 8),
    _HwAsmngTrapAsFaultTimes_Type()
)
hwAsmngTrapAsFaultTimes.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsFaultTimes.setStatus("current")
_HwAsmngTrapAsIfAdminStatus_Type = Integer32
_HwAsmngTrapAsIfAdminStatus_Object = MibScalar
hwAsmngTrapAsIfAdminStatus = _HwAsmngTrapAsIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 9),
    _HwAsmngTrapAsIfAdminStatus_Type()
)
hwAsmngTrapAsIfAdminStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsIfAdminStatus.setStatus("current")
_HwAsmngTrapAsIfName_Type = OctetString
_HwAsmngTrapAsIfName_Object = MibScalar
hwAsmngTrapAsIfName = _HwAsmngTrapAsIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 10),
    _HwAsmngTrapAsIfName_Type()
)
hwAsmngTrapAsIfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsIfName.setStatus("current")
_HwAsmngTrapAsActualeType_Type = OctetString
_HwAsmngTrapAsActualeType_Object = MibScalar
hwAsmngTrapAsActualeType = _HwAsmngTrapAsActualeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 11),
    _HwAsmngTrapAsActualeType_Type()
)
hwAsmngTrapAsActualeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsActualeType.setStatus("current")
_HwAsmngTrapAsVersion_Type = OctetString
_HwAsmngTrapAsVersion_Object = MibScalar
hwAsmngTrapAsVersion = _HwAsmngTrapAsVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 12),
    _HwAsmngTrapAsVersion_Type()
)
hwAsmngTrapAsVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsVersion.setStatus("current")
_HwAsmngTrapParentVersion_Type = OctetString
_HwAsmngTrapParentVersion_Object = MibScalar
hwAsmngTrapParentVersion = _HwAsmngTrapParentVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 13),
    _HwAsmngTrapParentVersion_Type()
)
hwAsmngTrapParentVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapParentVersion.setStatus("current")
_HwAsmngTrapAddedAsMac_Type = MacAddress
_HwAsmngTrapAddedAsMac_Object = MibScalar
hwAsmngTrapAddedAsMac = _HwAsmngTrapAddedAsMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 14),
    _HwAsmngTrapAddedAsMac_Type()
)
hwAsmngTrapAddedAsMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAddedAsMac.setStatus("current")
_HwAsmngTrapAsSlotId_Type = Integer32
_HwAsmngTrapAsSlotId_Object = MibScalar
hwAsmngTrapAsSlotId = _HwAsmngTrapAsSlotId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 15),
    _HwAsmngTrapAsSlotId_Type()
)
hwAsmngTrapAsSlotId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsSlotId.setStatus("current")
_HwAsmngTrapAddedAsSlotType_Type = OctetString
_HwAsmngTrapAddedAsSlotType_Object = MibScalar
hwAsmngTrapAddedAsSlotType = _HwAsmngTrapAddedAsSlotType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 16),
    _HwAsmngTrapAddedAsSlotType_Type()
)
hwAsmngTrapAddedAsSlotType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAddedAsSlotType.setStatus("current")
_HwAsmngTrapAsPermitNum_Type = Integer32
_HwAsmngTrapAsPermitNum_Object = MibScalar
hwAsmngTrapAsPermitNum = _HwAsmngTrapAsPermitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 17),
    _HwAsmngTrapAsPermitNum_Type()
)
hwAsmngTrapAsPermitNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsPermitNum.setStatus("current")
_HwAsmngTrapAsUnimngMode_Type = Integer32
_HwAsmngTrapAsUnimngMode_Object = MibScalar
hwAsmngTrapAsUnimngMode = _HwAsmngTrapAsUnimngMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 18),
    _HwAsmngTrapAsUnimngMode_Type()
)
hwAsmngTrapAsUnimngMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsUnimngMode.setStatus("current")
_HwAsmngTrapParentUnimngMode_Type = Integer32
_HwAsmngTrapParentUnimngMode_Object = MibScalar
hwAsmngTrapParentUnimngMode = _HwAsmngTrapParentUnimngMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 19),
    _HwAsmngTrapParentUnimngMode_Type()
)
hwAsmngTrapParentUnimngMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapParentUnimngMode.setStatus("current")
_HwAsmngTrapAsIfType_Type = Integer32
_HwAsmngTrapAsIfType_Object = MibScalar
hwAsmngTrapAsIfType = _HwAsmngTrapAsIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 20),
    _HwAsmngTrapAsIfType_Type()
)
hwAsmngTrapAsIfType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsIfType.setStatus("current")
_HwAsmngTrapAsOnlineFailReasonId_Type = Integer32
_HwAsmngTrapAsOnlineFailReasonId_Object = MibScalar
hwAsmngTrapAsOnlineFailReasonId = _HwAsmngTrapAsOnlineFailReasonId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 21),
    _HwAsmngTrapAsOnlineFailReasonId_Type()
)
hwAsmngTrapAsOnlineFailReasonId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsOnlineFailReasonId.setStatus("current")
_HwAsmngTrapAsOnlineFailReasonDesc_Type = OctetString
_HwAsmngTrapAsOnlineFailReasonDesc_Object = MibScalar
hwAsmngTrapAsOnlineFailReasonDesc = _HwAsmngTrapAsOnlineFailReasonDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 1, 22),
    _HwAsmngTrapAsOnlineFailReasonDesc_Type()
)
hwAsmngTrapAsOnlineFailReasonDesc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwAsmngTrapAsOnlineFailReasonDesc.setStatus("current")
_HwAsmngTraps_ObjectIdentity = ObjectIdentity
hwAsmngTraps = _HwAsmngTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2)
)
_HwUniMbrTrap_ObjectIdentity = ObjectIdentity
hwUniMbrTrap = _HwUniMbrTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3)
)
_HwUniMbrTrapObjects_ObjectIdentity = ObjectIdentity
hwUniMbrTrapObjects = _HwUniMbrTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 1)
)
_HwUniMbrLinkStatTrapLocalMac_Type = MacAddress
_HwUniMbrLinkStatTrapLocalMac_Object = MibScalar
hwUniMbrLinkStatTrapLocalMac = _HwUniMbrLinkStatTrapLocalMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 1, 1),
    _HwUniMbrLinkStatTrapLocalMac_Type()
)
hwUniMbrLinkStatTrapLocalMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniMbrLinkStatTrapLocalMac.setStatus("current")
_HwUniMbrLinkStatTrapLocalPortName_Type = OctetString
_HwUniMbrLinkStatTrapLocalPortName_Object = MibScalar
hwUniMbrLinkStatTrapLocalPortName = _HwUniMbrLinkStatTrapLocalPortName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 1, 2),
    _HwUniMbrLinkStatTrapLocalPortName_Type()
)
hwUniMbrLinkStatTrapLocalPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniMbrLinkStatTrapLocalPortName.setStatus("current")


class _HwUniMbrLinkStatTrapChangeType_Type(Integer32):
    """Custom type hwUniMbrLinkStatTrapChangeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down2up", 2),
          ("up2down", 1))
    )


_HwUniMbrLinkStatTrapChangeType_Type.__name__ = "Integer32"
_HwUniMbrLinkStatTrapChangeType_Object = MibScalar
hwUniMbrLinkStatTrapChangeType = _HwUniMbrLinkStatTrapChangeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 1, 3),
    _HwUniMbrLinkStatTrapChangeType_Type()
)
hwUniMbrLinkStatTrapChangeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniMbrLinkStatTrapChangeType.setStatus("current")
_HwUniMbrTrapConnectErrorReason_Type = OctetString
_HwUniMbrTrapConnectErrorReason_Object = MibScalar
hwUniMbrTrapConnectErrorReason = _HwUniMbrTrapConnectErrorReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 1, 4),
    _HwUniMbrTrapConnectErrorReason_Type()
)
hwUniMbrTrapConnectErrorReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniMbrTrapConnectErrorReason.setStatus("current")
_HwUniMbrTrapReceivePktRate_Type = Integer32
_HwUniMbrTrapReceivePktRate_Object = MibScalar
hwUniMbrTrapReceivePktRate = _HwUniMbrTrapReceivePktRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 1, 5),
    _HwUniMbrTrapReceivePktRate_Type()
)
hwUniMbrTrapReceivePktRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniMbrTrapReceivePktRate.setStatus("current")
_HwUniMbrTrapAsIndex_Type = Integer32
_HwUniMbrTrapAsIndex_Object = MibScalar
hwUniMbrTrapAsIndex = _HwUniMbrTrapAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 1, 6),
    _HwUniMbrTrapAsIndex_Type()
)
hwUniMbrTrapAsIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniMbrTrapAsIndex.setStatus("current")
_HwUniMbrTrapAsSysName_Type = OctetString
_HwUniMbrTrapAsSysName_Object = MibScalar
hwUniMbrTrapAsSysName = _HwUniMbrTrapAsSysName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 1, 7),
    _HwUniMbrTrapAsSysName_Type()
)
hwUniMbrTrapAsSysName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniMbrTrapAsSysName.setStatus("current")
_HwUniMbrParaSynFailReason_Type = OctetString
_HwUniMbrParaSynFailReason_Object = MibScalar
hwUniMbrParaSynFailReason = _HwUniMbrParaSynFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 1, 8),
    _HwUniMbrParaSynFailReason_Type()
)
hwUniMbrParaSynFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniMbrParaSynFailReason.setStatus("current")
_HwUniMbrTrapIllegalConfigReason_Type = OctetString
_HwUniMbrTrapIllegalConfigReason_Object = MibScalar
hwUniMbrTrapIllegalConfigReason = _HwUniMbrTrapIllegalConfigReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 1, 9),
    _HwUniMbrTrapIllegalConfigReason_Type()
)
hwUniMbrTrapIllegalConfigReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniMbrTrapIllegalConfigReason.setStatus("current")
_HwUniMbrTraps_ObjectIdentity = ObjectIdentity
hwUniMbrTraps = _HwUniMbrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 2)
)
_HwVermngTrap_ObjectIdentity = ObjectIdentity
hwVermngTrap = _HwVermngTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 4)
)
_HwVermngTrapObjects_ObjectIdentity = ObjectIdentity
hwVermngTrapObjects = _HwVermngTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 4, 1)
)
_HwVermngTraps_ObjectIdentity = ObjectIdentity
hwVermngTraps = _HwVermngTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 4, 2)
)
_HwTplmTrap_ObjectIdentity = ObjectIdentity
hwTplmTrap = _HwTplmTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 5)
)
_HwTplmTrapObjects_ObjectIdentity = ObjectIdentity
hwTplmTrapObjects = _HwTplmTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 5, 1)
)


class _HwTplmTrapASName_Type(OctetString):
    """Custom type hwTplmTrapASName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwTplmTrapASName_Type.__name__ = "OctetString"
_HwTplmTrapASName_Object = MibScalar
hwTplmTrapASName = _HwTplmTrapASName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 5, 1, 1),
    _HwTplmTrapASName_Type()
)
hwTplmTrapASName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTplmTrapASName.setStatus("current")
_HwTplmTrapFailedReason_Type = OctetString
_HwTplmTrapFailedReason_Object = MibScalar
hwTplmTrapFailedReason = _HwTplmTrapFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 5, 1, 2),
    _HwTplmTrapFailedReason_Type()
)
hwTplmTrapFailedReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTplmTrapFailedReason.setStatus("current")
_HwTplmTraps_ObjectIdentity = ObjectIdentity
hwTplmTraps = _HwTplmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 5, 2)
)
_HwUniAsBaseTrap_ObjectIdentity = ObjectIdentity
hwUniAsBaseTrap = _HwUniAsBaseTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6)
)
_HwUniAsBaseTrapObjects_ObjectIdentity = ObjectIdentity
hwUniAsBaseTrapObjects = _HwUniAsBaseTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1)
)
_HwUniAsBaseAsName_Type = DisplayString
_HwUniAsBaseAsName_Object = MibScalar
hwUniAsBaseAsName = _HwUniAsBaseAsName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 1),
    _HwUniAsBaseAsName_Type()
)
hwUniAsBaseAsName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseAsName.setStatus("current")
_HwUniAsBaseAsId_Type = Integer32
_HwUniAsBaseAsId_Object = MibScalar
hwUniAsBaseAsId = _HwUniAsBaseAsId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 2),
    _HwUniAsBaseAsId_Type()
)
hwUniAsBaseAsId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseAsId.setStatus("current")
_HwUniAsBaseEntityPhysicalIndex_Type = Integer32
_HwUniAsBaseEntityPhysicalIndex_Object = MibScalar
hwUniAsBaseEntityPhysicalIndex = _HwUniAsBaseEntityPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 3),
    _HwUniAsBaseEntityPhysicalIndex_Type()
)
hwUniAsBaseEntityPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseEntityPhysicalIndex.setStatus("current")
_HwUniAsBaseTrapSeverity_Type = Integer32
_HwUniAsBaseTrapSeverity_Object = MibScalar
hwUniAsBaseTrapSeverity = _HwUniAsBaseTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 4),
    _HwUniAsBaseTrapSeverity_Type()
)
hwUniAsBaseTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseTrapSeverity.setStatus("current")
_HwUniAsBaseTrapProbableCause_Type = Integer32
_HwUniAsBaseTrapProbableCause_Object = MibScalar
hwUniAsBaseTrapProbableCause = _HwUniAsBaseTrapProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 5),
    _HwUniAsBaseTrapProbableCause_Type()
)
hwUniAsBaseTrapProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseTrapProbableCause.setStatus("current")
_HwUniAsBaseTrapEventType_Type = Integer32
_HwUniAsBaseTrapEventType_Object = MibScalar
hwUniAsBaseTrapEventType = _HwUniAsBaseTrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 6),
    _HwUniAsBaseTrapEventType_Type()
)
hwUniAsBaseTrapEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseTrapEventType.setStatus("current")
_HwUniAsBaseEntPhysicalContainedIn_Type = Integer32
_HwUniAsBaseEntPhysicalContainedIn_Object = MibScalar
hwUniAsBaseEntPhysicalContainedIn = _HwUniAsBaseEntPhysicalContainedIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 7),
    _HwUniAsBaseEntPhysicalContainedIn_Type()
)
hwUniAsBaseEntPhysicalContainedIn.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseEntPhysicalContainedIn.setStatus("current")
_HwUniAsBaseEntPhysicalName_Type = DisplayString
_HwUniAsBaseEntPhysicalName_Object = MibScalar
hwUniAsBaseEntPhysicalName = _HwUniAsBaseEntPhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 8),
    _HwUniAsBaseEntPhysicalName_Type()
)
hwUniAsBaseEntPhysicalName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseEntPhysicalName.setStatus("current")
_HwUniAsBaseRelativeResource_Type = DisplayString
_HwUniAsBaseRelativeResource_Object = MibScalar
hwUniAsBaseRelativeResource = _HwUniAsBaseRelativeResource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 9),
    _HwUniAsBaseRelativeResource_Type()
)
hwUniAsBaseRelativeResource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseRelativeResource.setStatus("current")
_HwUniAsBaseReasonDescription_Type = DisplayString
_HwUniAsBaseReasonDescription_Object = MibScalar
hwUniAsBaseReasonDescription = _HwUniAsBaseReasonDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 10),
    _HwUniAsBaseReasonDescription_Type()
)
hwUniAsBaseReasonDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseReasonDescription.setStatus("current")
_HwUniAsBaseThresholdType_Type = Integer32
_HwUniAsBaseThresholdType_Object = MibScalar
hwUniAsBaseThresholdType = _HwUniAsBaseThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 11),
    _HwUniAsBaseThresholdType_Type()
)
hwUniAsBaseThresholdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseThresholdType.setStatus("current")
_HwUniAsBaseThresholdValue_Type = Integer32
_HwUniAsBaseThresholdValue_Object = MibScalar
hwUniAsBaseThresholdValue = _HwUniAsBaseThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 12),
    _HwUniAsBaseThresholdValue_Type()
)
hwUniAsBaseThresholdValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseThresholdValue.setStatus("current")
_HwUniAsBaseThresholdUnit_Type = Integer32
_HwUniAsBaseThresholdUnit_Object = MibScalar
hwUniAsBaseThresholdUnit = _HwUniAsBaseThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 13),
    _HwUniAsBaseThresholdUnit_Type()
)
hwUniAsBaseThresholdUnit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseThresholdUnit.setStatus("current")
_HwUniAsBaseThresholdHighWarning_Type = Integer32
_HwUniAsBaseThresholdHighWarning_Object = MibScalar
hwUniAsBaseThresholdHighWarning = _HwUniAsBaseThresholdHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 14),
    _HwUniAsBaseThresholdHighWarning_Type()
)
hwUniAsBaseThresholdHighWarning.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseThresholdHighWarning.setStatus("current")
_HwUniAsBaseThresholdHighCritical_Type = Integer32
_HwUniAsBaseThresholdHighCritical_Object = MibScalar
hwUniAsBaseThresholdHighCritical = _HwUniAsBaseThresholdHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 15),
    _HwUniAsBaseThresholdHighCritical_Type()
)
hwUniAsBaseThresholdHighCritical.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseThresholdHighCritical.setStatus("current")
_HwUniAsBaseThresholdLowWarning_Type = Integer32
_HwUniAsBaseThresholdLowWarning_Object = MibScalar
hwUniAsBaseThresholdLowWarning = _HwUniAsBaseThresholdLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 16),
    _HwUniAsBaseThresholdLowWarning_Type()
)
hwUniAsBaseThresholdLowWarning.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseThresholdLowWarning.setStatus("current")
_HwUniAsBaseThresholdLowCritical_Type = Integer32
_HwUniAsBaseThresholdLowCritical_Object = MibScalar
hwUniAsBaseThresholdLowCritical = _HwUniAsBaseThresholdLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 17),
    _HwUniAsBaseThresholdLowCritical_Type()
)
hwUniAsBaseThresholdLowCritical.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseThresholdLowCritical.setStatus("current")
_HwUniAsBaseEntityTrapEntType_Type = Integer32
_HwUniAsBaseEntityTrapEntType_Object = MibScalar
hwUniAsBaseEntityTrapEntType = _HwUniAsBaseEntityTrapEntType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 18),
    _HwUniAsBaseEntityTrapEntType_Type()
)
hwUniAsBaseEntityTrapEntType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseEntityTrapEntType.setStatus("current")
_HwUniAsBaseEntityTrapEntFaultID_Type = Integer32
_HwUniAsBaseEntityTrapEntFaultID_Object = MibScalar
hwUniAsBaseEntityTrapEntFaultID = _HwUniAsBaseEntityTrapEntFaultID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 19),
    _HwUniAsBaseEntityTrapEntFaultID_Type()
)
hwUniAsBaseEntityTrapEntFaultID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseEntityTrapEntFaultID.setStatus("current")
_HwUniAsBaseEntityTrapCommunicateType_Type = Integer32
_HwUniAsBaseEntityTrapCommunicateType_Object = MibScalar
hwUniAsBaseEntityTrapCommunicateType = _HwUniAsBaseEntityTrapCommunicateType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 20),
    _HwUniAsBaseEntityTrapCommunicateType_Type()
)
hwUniAsBaseEntityTrapCommunicateType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseEntityTrapCommunicateType.setStatus("current")
_HwUniAsBaseThresholdEntValue_Type = Integer32
_HwUniAsBaseThresholdEntValue_Object = MibScalar
hwUniAsBaseThresholdEntValue = _HwUniAsBaseThresholdEntValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 21),
    _HwUniAsBaseThresholdEntValue_Type()
)
hwUniAsBaseThresholdEntValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseThresholdEntValue.setStatus("current")
_HwUniAsBaseThresholdEntCurrent_Type = Integer32
_HwUniAsBaseThresholdEntCurrent_Object = MibScalar
hwUniAsBaseThresholdEntCurrent = _HwUniAsBaseThresholdEntCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 22),
    _HwUniAsBaseThresholdEntCurrent_Type()
)
hwUniAsBaseThresholdEntCurrent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseThresholdEntCurrent.setStatus("current")
_HwUniAsBaseEntPhysicalIndex_Type = Integer32
_HwUniAsBaseEntPhysicalIndex_Object = MibScalar
hwUniAsBaseEntPhysicalIndex = _HwUniAsBaseEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 23),
    _HwUniAsBaseEntPhysicalIndex_Type()
)
hwUniAsBaseEntPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseEntPhysicalIndex.setStatus("current")
_HwUniAsBaseThresholdHwBaseThresholdType_Type = Integer32
_HwUniAsBaseThresholdHwBaseThresholdType_Object = MibScalar
hwUniAsBaseThresholdHwBaseThresholdType = _HwUniAsBaseThresholdHwBaseThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 24),
    _HwUniAsBaseThresholdHwBaseThresholdType_Type()
)
hwUniAsBaseThresholdHwBaseThresholdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseThresholdHwBaseThresholdType.setStatus("current")
_HwUniAsBaseThresholdHwBaseThresholdIndex_Type = Integer32
_HwUniAsBaseThresholdHwBaseThresholdIndex_Object = MibScalar
hwUniAsBaseThresholdHwBaseThresholdIndex = _HwUniAsBaseThresholdHwBaseThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 1, 25),
    _HwUniAsBaseThresholdHwBaseThresholdIndex_Type()
)
hwUniAsBaseThresholdHwBaseThresholdIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwUniAsBaseThresholdHwBaseThresholdIndex.setStatus("current")
_HwUniAsBaseTraps_ObjectIdentity = ObjectIdentity
hwUniAsBaseTraps = _HwUniAsBaseTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2)
)
_HwASEnvironmentTrap_ObjectIdentity = ObjectIdentity
hwASEnvironmentTrap = _HwASEnvironmentTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 2)
)
_HwASBoardTrap_ObjectIdentity = ObjectIdentity
hwASBoardTrap = _HwASBoardTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 3)
)
_HwASOpticalTrap_ObjectIdentity = ObjectIdentity
hwASOpticalTrap = _HwASOpticalTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 4)
)
_HwASPowerTrap_ObjectIdentity = ObjectIdentity
hwASPowerTrap = _HwASPowerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 5)
)
_HwASFanTrap_ObjectIdentity = ObjectIdentity
hwASFanTrap = _HwASFanTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 6)
)
_HwASCommunicateTrap_ObjectIdentity = ObjectIdentity
hwASCommunicateTrap = _HwASCommunicateTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 7)
)
_HwASCPUTrap_ObjectIdentity = ObjectIdentity
hwASCPUTrap = _HwASCPUTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 8)
)
_HwASMemoryTrap_ObjectIdentity = ObjectIdentity
hwASMemoryTrap = _HwASMemoryTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 9)
)
_HwASMadTrap_ObjectIdentity = ObjectIdentity
hwASMadTrap = _HwASMadTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 10)
)
_HwUnimngConformance_ObjectIdentity = ObjectIdentity
hwUnimngConformance = _HwUnimngConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50)
)
_HwTopomngCompliances_ObjectIdentity = ObjectIdentity
hwTopomngCompliances = _HwTopomngCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 1)
)
_HwAsmngCompliances_ObjectIdentity = ObjectIdentity
hwAsmngCompliances = _HwAsmngCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2)
)
_HwMbrCompliances_ObjectIdentity = ObjectIdentity
hwMbrCompliances = _HwMbrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 3)
)
_HwVermngCompliances_ObjectIdentity = ObjectIdentity
hwVermngCompliances = _HwVermngCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 4)
)
_HwTplmCompliances_ObjectIdentity = ObjectIdentity
hwTplmCompliances = _HwTplmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 5)
)
_HwUniBaseTrapCompliances_ObjectIdentity = ObjectIdentity
hwUniBaseTrapCompliances = _HwUniBaseTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 6)
)

# Managed Objects groups

hwTopomngObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 1, 1, 1)
)
hwTopomngObjectsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTopomngExploreTime"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngLastCollectDuration"))
)
if mibBuilder.loadTexts:
    hwTopomngObjectsGroup.setStatus("current")

hwTopomngTopoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 1, 1, 2)
)
hwTopomngTopoGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTopoPeerMac"),
        ("HUAWEI-UNIMNG-MIB", "hwTopoLocalPortName"),
        ("HUAWEI-UNIMNG-MIB", "hwTopoPeerPortName"),
        ("HUAWEI-UNIMNG-MIB", "hwTopoLocalTrunkId"),
        ("HUAWEI-UNIMNG-MIB", "hwTopoPeerTrunkId"),
        ("HUAWEI-UNIMNG-MIB", "hwTopoLocalRole"),
        ("HUAWEI-UNIMNG-MIB", "hwTopoPeerRole"))
)
if mibBuilder.loadTexts:
    hwTopomngTopoGroup.setStatus("current")

hwTopomngTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 1, 1, 3)
)
hwTopomngTrapObjectsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTopomngTrapLocalMac"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapLocalPortName"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapLocalTrunkId"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapPeerMac"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapPeerPortName"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapPeerTrunkId"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapReason"))
)
if mibBuilder.loadTexts:
    hwTopomngTrapObjectsGroup.setStatus("current")

hwAsmngObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 1)
)
hwAsmngObjectsGroup.setObjects(
    ("HUAWEI-UNIMNG-MIB", "hwUniMngEnable")
)
if mibBuilder.loadTexts:
    hwAsmngObjectsGroup.setStatus("current")

hwAsmngAsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 2)
)
hwAsmngAsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsHardwareVersion"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIpAddress"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIpNetMask"),
        ("HUAWEI-UNIMNG-MIB", "hwAsAccessUser"),
        ("HUAWEI-UNIMNG-MIB", "hwAsMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsSn"),
        ("HUAWEI-UNIMNG-MIB", "hwAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsRunState"),
        ("HUAWEI-UNIMNG-MIB", "hwAsSoftwareVersion"),
        ("HUAWEI-UNIMNG-MIB", "hwAsDns"),
        ("HUAWEI-UNIMNG-MIB", "hwAsOnlineTime"),
        ("HUAWEI-UNIMNG-MIB", "hwAsCpuUseage"),
        ("HUAWEI-UNIMNG-MIB", "hwAsMemoryUseage"),
        ("HUAWEI-UNIMNG-MIB", "hwAsSysMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsStackEnable"),
        ("HUAWEI-UNIMNG-MIB", "hwAsGatewayIp"),
        ("HUAWEI-UNIMNG-MIB", "hwAsRowstatus"),
        ("HUAWEI-UNIMNG-MIB", "hwAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsVpnInstance"))
)
if mibBuilder.loadTexts:
    hwAsmngAsGroup.setStatus("current")

hwAsmngAsIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 3)
)
hwAsmngAsIfGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsIfDescr"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfType"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfMtu"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfSpeed"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfPhysAddress"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfAdminStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfInUcastPkts"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfOutUcastPkts"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfOperStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfIndex"))
)
if mibBuilder.loadTexts:
    hwAsmngAsIfGroup.setStatus("current")

hwAsmngAsIfXGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 4)
)
hwAsmngAsIfXGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsIfLinkUpDownTrapEnable"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfHighSpeed"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfAlias"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfInUcastPkts"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfOutUcastPkts"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfHCOutOctets"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfInMulticastPkts"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfInBroadcastPkts"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfOutMulticastPkts"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfOutBroadcastPkts"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfHCInOctets"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwAsIfName"))
)
if mibBuilder.loadTexts:
    hwAsmngAsIfXGroup.setStatus("current")

hwAsmngTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 5)
)
hwAsmngTrapObjectsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSn"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfOperStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsFaultTimes"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfAdminStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsActualeType"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsVersion"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapParentVersion"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAddedAsMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSlotId"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAddedAsSlotType"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsPermitNum"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsUnimngMode"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapParentUnimngMode"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfType"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsOnlineFailReasonId"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsOnlineFailReasonDesc"))
)
if mibBuilder.loadTexts:
    hwAsmngTrapObjectsGroup.setStatus("current")

hwAsmngGlobalObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 7)
)
hwAsmngGlobalObjectsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsAutoReplaceEnable"),
        ("HUAWEI-UNIMNG-MIB", "hwAsAuthMode"))
)
if mibBuilder.loadTexts:
    hwAsmngGlobalObjectsGroup.setStatus("current")

hwAsmngMacWhitelistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 8)
)
hwAsmngMacWhitelistGroup.setObjects(
    ("HUAWEI-UNIMNG-MIB", "hwAsMacWhitelistRowStatus")
)
if mibBuilder.loadTexts:
    hwAsmngMacWhitelistGroup.setStatus("current")

hwAsmngMacBlacklistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 9)
)
hwAsmngMacBlacklistGroup.setObjects(
    ("HUAWEI-UNIMNG-MIB", "hwAsMacBlacklistRowStatus")
)
if mibBuilder.loadTexts:
    hwAsmngMacBlacklistGroup.setStatus("current")

hwAsmngEntityPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 10)
)
hwAsmngEntityPhysicalGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalDescr"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalVendorType"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalContainedIn"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalClass"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalParentRelPos"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalHardwareRev"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalFirmwareRev"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalSoftwareRev"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalSerialNum"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityPhysicalMfgName"))
)
if mibBuilder.loadTexts:
    hwAsmngEntityPhysicalGroup.setStatus("current")

hwAsmngEntityStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 11)
)
hwAsmngEntityStateGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsEntityAdminStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityOperStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityStandbyStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityAlarmLight"),
        ("HUAWEI-UNIMNG-MIB", "hwAsEntityPortType"))
)
if mibBuilder.loadTexts:
    hwAsmngEntityStateGroup.setStatus("current")

hwAsmngEntityAliasMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 12)
)
hwAsmngEntityAliasMappingGroup.setObjects(
    ("HUAWEI-UNIMNG-MIB", "hwAsEntryAliasMappingIdentifier")
)
if mibBuilder.loadTexts:
    hwAsmngEntityAliasMappingGroup.setStatus("current")

hwAsmngSlotGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 13)
)
hwAsmngSlotGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsSlotState"),
        ("HUAWEI-UNIMNG-MIB", "hwAsSlotRowStatus"))
)
if mibBuilder.loadTexts:
    hwAsmngSlotGroup.setStatus("current")

hwMbrTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 3, 1, 1)
)
hwMbrTrapObjectsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniMbrLinkStatTrapLocalMac"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrLinkStatTrapLocalPortName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrLinkStatTrapChangeType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapConnectErrorReason"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapReceivePktRate"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrParaSynFailReason"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapIllegalConfigReason"))
)
if mibBuilder.loadTexts:
    hwMbrTrapObjectsGroup.setStatus("current")

hwMbrFabricPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 3, 1, 3)
)
hwMbrFabricPortGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwMbrMngFabricPortMemberIfName"),
        ("HUAWEI-UNIMNG-MIB", "hwMbrMngFabricPortDirection"),
        ("HUAWEI-UNIMNG-MIB", "hwMbrMngFabricPortIndirectFlag"),
        ("HUAWEI-UNIMNG-MIB", "hwMbrMngFabricPortDescription"))
)
if mibBuilder.loadTexts:
    hwMbrFabricPortGroup.setStatus("current")

hwVermngObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 4, 1, 1)
)
hwVermngObjectsGroup.setObjects(
    ("HUAWEI-UNIMNG-MIB", "hwVermngFileServerType")
)
if mibBuilder.loadTexts:
    hwVermngObjectsGroup.setStatus("current")

hwVermngUpgradeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 4, 1, 2)
)
hwVermngUpgradeInfoGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsSysSoftware"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsSysSoftwareVer"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsSysPatch"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsDownloadSoftware"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsDownloadSoftwareVer"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsDownloadPatch"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsUpgradeState"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsUpgradeType"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsFilePhase"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsUpgradePhase"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsUpgradeResult"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsErrorCode"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsErrorDescr"))
)
if mibBuilder.loadTexts:
    hwVermngUpgradeInfoGroup.setStatus("current")

hwVermngAsTypeCfgInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 4, 1, 3)
)
hwVermngAsTypeCfgInfoGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwVermngAsTypeCfgInfoPatch"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngAsTypeCfgInfoSystemSoftwareVer"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngAsTypeCfgInfoRowStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngAsTypeCfgInfoSystemSoftware"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngAsTypeCfgInfoAsTypeName"))
)
if mibBuilder.loadTexts:
    hwVermngAsTypeCfgInfoGroup.setStatus("current")

hwTplmASGroupGoup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 5, 1, 1)
)
hwTplmASGroupGoup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTplmASGroupName"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmASAdminProfileName"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmASGroupProfileStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmASGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwTplmASGroupGoup.setStatus("current")

hwTplmASGoup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 5, 1, 2)
)
hwTplmASGoup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTplmASASGroupName"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmASRowStatus"))
)
if mibBuilder.loadTexts:
    hwTplmASGoup.setStatus("current")

hwTplmPortGroupGoup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 5, 1, 3)
)
hwTplmPortGroupGoup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTplmPortGroupName"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmPortGroupType"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmPortGroupNetworkBasicProfile"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmPortGroupNetworkEnhancedProfile"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmPortGroupUserAccessProfile"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmPortGroupProfileStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmPortGroupRowStatus"))
)
if mibBuilder.loadTexts:
    hwTplmPortGroupGoup.setStatus("current")

hwTplmPortGoup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 5, 1, 4)
)
hwTplmPortGoup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTplmPortPortGroupName"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmPortRowStatus"))
)
if mibBuilder.loadTexts:
    hwTplmPortGoup.setStatus("current")

hwTplmConfigManagementGoup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 5, 1, 5)
)
hwTplmConfigManagementGoup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTplmConfigCommitAll"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmConfigManagementCommit"))
)
if mibBuilder.loadTexts:
    hwTplmConfigManagementGoup.setStatus("current")

hwTplmTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 5, 1, 6)
)
hwTplmTrapObjectsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTplmTrapASName"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmTrapFailedReason"))
)
if mibBuilder.loadTexts:
    hwTplmTrapObjectsGroup.setStatus("current")

hwUniBaseTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 6, 1, 1)
)
hwUniBaseTrapObjectsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseTrapSeverity"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseTrapProbableCause"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseTrapEventType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalContainedIn"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseRelativeResource"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseReasonDescription"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdValue"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdUnit"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdHighWarning"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdHighCritical"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdLowWarning"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdLowCritical"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapCommunicateType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntValue"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntCurrent"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdHwBaseThresholdType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdHwBaseThresholdIndex"))
)
if mibBuilder.loadTexts:
    hwUniBaseTrapObjectsGroup.setStatus("current")


# Notification objects

hwTopomngLinkNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1, 2, 1)
)
hwTopomngLinkNormal.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTopomngTrapLocalMac"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapLocalPortName"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapLocalTrunkId"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapPeerMac"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapPeerPortName"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapPeerTrunkId"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapReason"))
)
if mibBuilder.loadTexts:
    hwTopomngLinkNormal.setStatus(
        "current"
    )

hwTopomngLinkAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 1, 2, 2)
)
hwTopomngLinkAbnormal.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTopomngTrapLocalMac"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapLocalPortName"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapLocalTrunkId"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapPeerMac"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapPeerPortName"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapPeerTrunkId"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngTrapReason"))
)
if mibBuilder.loadTexts:
    hwTopomngLinkAbnormal.setStatus(
        "current"
    )

hwAsFaultNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 1)
)
hwAsFaultNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsFaultTimes"))
)
if mibBuilder.loadTexts:
    hwAsFaultNotify.setStatus(
        "current"
    )

hwAsNormalNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 2)
)
hwAsNormalNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"))
)
if mibBuilder.loadTexts:
    hwAsNormalNotify.setStatus(
        "current"
    )

hwAsAddOffLineNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 3)
)
hwAsAddOffLineNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"))
)
if mibBuilder.loadTexts:
    hwAsAddOffLineNotify.setStatus(
        "current"
    )

hwAsDelOffLineNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 4)
)
hwAsDelOffLineNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"))
)
if mibBuilder.loadTexts:
    hwAsDelOffLineNotify.setStatus(
        "current"
    )

hwAsPortStateChangeToDownNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 5)
)
hwAsPortStateChangeToDownNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfAdminStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfOperStatus"))
)
if mibBuilder.loadTexts:
    hwAsPortStateChangeToDownNotify.setStatus(
        "current"
    )

hwAsPortStateChangeToUpNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 6)
)
hwAsPortStateChangeToUpNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfAdminStatus"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfOperStatus"))
)
if mibBuilder.loadTexts:
    hwAsPortStateChangeToUpNotify.setStatus(
        "current"
    )

hwAsModelNotMatchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 7)
)
hwAsModelNotMatchNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsActualeType"))
)
if mibBuilder.loadTexts:
    hwAsModelNotMatchNotify.setStatus(
        "current"
    )

hwAsVersionNotMatchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 8)
)
hwAsVersionNotMatchNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsVersion"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapParentVersion"))
)
if mibBuilder.loadTexts:
    hwAsVersionNotMatchNotify.setStatus(
        "current"
    )

hwAsNameConflictNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 9)
)
hwAsNameConflictNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAddedAsMac"))
)
if mibBuilder.loadTexts:
    hwAsNameConflictNotify.setStatus(
        "current"
    )

hwAsSlotModelNotMatchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 10)
)
hwAsSlotModelNotMatchNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSlotId"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAddedAsSlotType"))
)
if mibBuilder.loadTexts:
    hwAsSlotModelNotMatchNotify.setStatus(
        "current"
    )

hwAsFullNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 11)
)
hwAsFullNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsPermitNum"))
)
if mibBuilder.loadTexts:
    hwAsFullNotify.setStatus(
        "current"
    )

hwUnimngModeNotMatchNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 12)
)
hwUnimngModeNotMatchNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsUnimngMode"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapParentUnimngMode"))
)
if mibBuilder.loadTexts:
    hwUnimngModeNotMatchNotify.setStatus(
        "current"
    )

hwAsBoardAddNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 13)
)
hwAsBoardAddNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSlotId"))
)
if mibBuilder.loadTexts:
    hwAsBoardAddNotify.setStatus(
        "current"
    )

hwAsBoardDeleteNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 14)
)
hwAsBoardDeleteNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSlotId"))
)
if mibBuilder.loadTexts:
    hwAsBoardDeleteNotify.setStatus(
        "current"
    )

hwAsBoardPlugInNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 15)
)
hwAsBoardPlugInNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSlotId"))
)
if mibBuilder.loadTexts:
    hwAsBoardPlugInNotify.setStatus(
        "current"
    )

hwAsBoardPlugOutNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 16)
)
hwAsBoardPlugOutNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSlotId"))
)
if mibBuilder.loadTexts:
    hwAsBoardPlugOutNotify.setStatus(
        "current"
    )

hwAsInBlacklistNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 17)
)
hwAsInBlacklistNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"))
)
if mibBuilder.loadTexts:
    hwAsInBlacklistNotify.setStatus(
        "current"
    )

hwAsUnconfirmedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 18)
)
hwAsUnconfirmedNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"))
)
if mibBuilder.loadTexts:
    hwAsUnconfirmedNotify.setStatus(
        "current"
    )

hwAsComboPortTypeChangeNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 19)
)
hwAsComboPortTypeChangeNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIfType"))
)
if mibBuilder.loadTexts:
    hwAsComboPortTypeChangeNotify.setStatus(
        "current"
    )

hwAsOnlineFailNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 20)
)
hwAsOnlineFailNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsMac"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsOnlineFailReasonId"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsOnlineFailReasonDesc"))
)
if mibBuilder.loadTexts:
    hwAsOnlineFailNotify.setStatus(
        "current"
    )

hwAsSlotIdInvalidNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 21)
)
hwAsSlotIdInvalidNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsModel"),
        ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSlotId"))
)
if mibBuilder.loadTexts:
    hwAsSlotIdInvalidNotify.setStatus(
        "current"
    )

hwAsSysmacSwitchCfgErrNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 2, 2, 22)
)
hwAsSysmacSwitchCfgErrNotify.setObjects(
    ("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName")
)
if mibBuilder.loadTexts:
    hwAsSysmacSwitchCfgErrNotify.setStatus(
        "current"
    )

hwUniMbrConnectError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 2, 1)
)
hwUniMbrConnectError.setObjects(
    ("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapConnectErrorReason")
)
if mibBuilder.loadTexts:
    hwUniMbrConnectError.setStatus(
        "current"
    )

hwUniMbrASDiscoverAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 2, 2)
)
hwUniMbrASDiscoverAttack.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrLinkStatTrapLocalPortName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapReceivePktRate"))
)
if mibBuilder.loadTexts:
    hwUniMbrASDiscoverAttack.setStatus(
        "current"
    )

hwUniMbrFabricPortMemberDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 2, 3)
)
hwUniMbrFabricPortMemberDelete.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrLinkStatTrapLocalPortName"))
)
if mibBuilder.loadTexts:
    hwUniMbrFabricPortMemberDelete.setStatus(
        "current"
    )

hwUniMbrIllegalFabricConfig = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 3, 2, 4)
)
hwUniMbrIllegalFabricConfig.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapAsIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrTrapIllegalConfigReason"))
)
if mibBuilder.loadTexts:
    hwUniMbrIllegalFabricConfig.setStatus(
        "current"
    )

hwVermngUpgradeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 4, 2, 1)
)
hwVermngUpgradeFail.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsmngTrapAsSysName"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsErrorCode"),
        ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeInfoAsErrorDescr"))
)
if mibBuilder.loadTexts:
    hwVermngUpgradeFail.setStatus(
        "current"
    )

hwTplmCmdExecuteFailedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 5, 2, 1)
)
hwTplmCmdExecuteFailedNotify.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTplmTrapASName"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmTrapFailedReason"))
)
if mibBuilder.loadTexts:
    hwTplmCmdExecuteFailedNotify.setStatus(
        "current"
    )

hwTplmCmdExecuteSuccessfulNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 5, 2, 2)
)
hwTplmCmdExecuteSuccessfulNotify.setObjects(
    ("HUAWEI-UNIMNG-MIB", "hwTplmTrapASName")
)
if mibBuilder.loadTexts:
    hwTplmCmdExecuteSuccessfulNotify.setStatus(
        "current"
    )

hwTplmDirectCmdRecoverFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 5, 2, 3)
)
hwTplmDirectCmdRecoverFail.setObjects(
    ("HUAWEI-UNIMNG-MIB", "hwTplmTrapASName")
)
if mibBuilder.loadTexts:
    hwTplmDirectCmdRecoverFail.setStatus(
        "current"
    )

hwASBrdTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 2, 1)
)
hwASBrdTempAlarm.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntValue"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntCurrent"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASBrdTempAlarm.setStatus(
        "current"
    )

hwASBrdTempResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 2, 2)
)
hwASBrdTempResume.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntValue"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntCurrent"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASBrdTempResume.setStatus(
        "current"
    )

hwASBoardFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 3, 1)
)
hwASBoardFail.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASBoardFail.setStatus(
        "current"
    )

hwASBoardFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 3, 2)
)
hwASBoardFailResume.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASBoardFailResume.setStatus(
        "current"
    )

hwASOpticalInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 4, 1)
)
hwASOpticalInvalid.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASOpticalInvalid.setStatus(
        "current"
    )

hwASOpticalInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 4, 2)
)
hwASOpticalInvalidResume.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASOpticalInvalidResume.setStatus(
        "current"
    )

hwASPowerRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 5, 1)
)
hwASPowerRemove.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASPowerRemove.setStatus(
        "current"
    )

hwASPowerInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 5, 2)
)
hwASPowerInsert.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASPowerInsert.setStatus(
        "current"
    )

hwASPowerInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 5, 3)
)
hwASPowerInvalid.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASPowerInvalid.setStatus(
        "current"
    )

hwASPowerInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 5, 4)
)
hwASPowerInvalidResume.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASPowerInvalidResume.setStatus(
        "current"
    )

hwASFanRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 6, 1)
)
hwASFanRemove.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASFanRemove.setStatus(
        "current"
    )

hwASFanInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 6, 2)
)
hwASFanInsert.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASFanInsert.setStatus(
        "current"
    )

hwASFanInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 6, 3)
)
hwASFanInvalid.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASFanInvalid.setStatus(
        "current"
    )

hwASFanInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 6, 4)
)
hwASFanInvalidResume.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASFanInvalidResume.setStatus(
        "current"
    )

hwASCommunicateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 7, 1)
)
hwASCommunicateError.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapCommunicateType"))
)
if mibBuilder.loadTexts:
    hwASCommunicateError.setStatus(
        "current"
    )

hwASCommunicateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 7, 2)
)
hwASCommunicateResume.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapCommunicateType"))
)
if mibBuilder.loadTexts:
    hwASCommunicateResume.setStatus(
        "current"
    )

hwASCPUUtilizationRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 8, 1)
)
hwASCPUUtilizationRising.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntValue"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntCurrent"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASCPUUtilizationRising.setStatus(
        "current"
    )

hwASCPUUtilizationResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 8, 2)
)
hwASCPUUtilizationResume.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntValue"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntCurrent"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASCPUUtilizationResume.setStatus(
        "current"
    )

hwASMemUtilizationRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 9, 1)
)
hwASMemUtilizationRising.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntValue"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntCurrent"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASMemUtilizationRising.setStatus(
        "current"
    )

hwASMemUtilizationResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 9, 2)
)
hwASMemUtilizationResume.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityPhysicalIndex"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntPhysicalName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdType"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntValue"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseThresholdEntCurrent"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseEntityTrapEntFaultID"))
)
if mibBuilder.loadTexts:
    hwASMemUtilizationResume.setStatus(
        "current"
    )

hwASMadConflictDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 10, 1)
)
hwASMadConflictDetect.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"))
)
if mibBuilder.loadTexts:
    hwASMadConflictDetect.setStatus(
        "current"
    )

hwASMadConflictResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 31, 6, 2, 10, 2)
)
hwASMadConflictResume.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsName"),
        ("HUAWEI-UNIMNG-MIB", "hwUniAsBaseAsId"))
)
if mibBuilder.loadTexts:
    hwASMadConflictResume.setStatus(
        "current"
    )


# Notifications groups

hwTopomngTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 1, 1, 4)
)
hwTopomngTrapsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTopomngLinkNormal"),
        ("HUAWEI-UNIMNG-MIB", "hwTopomngLinkAbnormal"))
)
if mibBuilder.loadTexts:
    hwTopomngTrapsGroup.setStatus(
        "current"
    )

hwAsmngTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1, 6)
)
hwAsmngTrapsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwAsFaultNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsNormalNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsAddOffLineNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsDelOffLineNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsPortStateChangeToDownNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsPortStateChangeToUpNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsModelNotMatchNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsVersionNotMatchNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsNameConflictNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsSlotModelNotMatchNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsFullNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwUnimngModeNotMatchNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsBoardAddNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsBoardDeleteNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsBoardPlugInNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsBoardPlugOutNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsInBlacklistNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsUnconfirmedNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsComboPortTypeChangeNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsOnlineFailNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsSlotIdInvalidNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwAsSysmacSwitchCfgErrNotify"))
)
if mibBuilder.loadTexts:
    hwAsmngTrapsGroup.setStatus(
        "current"
    )

hwMbrTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 3, 1, 2)
)
hwMbrTrapsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwUniMbrConnectError"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrASDiscoverAttack"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrFabricPortMemberDelete"),
        ("HUAWEI-UNIMNG-MIB", "hwUniMbrIllegalFabricConfig"))
)
if mibBuilder.loadTexts:
    hwMbrTrapsGroup.setStatus(
        "current"
    )

hwVermngTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 4, 1, 4)
)
hwVermngTrapsGroup.setObjects(
    ("HUAWEI-UNIMNG-MIB", "hwVermngUpgradeFail")
)
if mibBuilder.loadTexts:
    hwVermngTrapsGroup.setStatus(
        "current"
    )

hwTplmTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 5, 1, 7)
)
hwTplmTrapsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwTplmCmdExecuteFailedNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmCmdExecuteSuccessfulNotify"),
        ("HUAWEI-UNIMNG-MIB", "hwTplmDirectCmdRecoverFail"))
)
if mibBuilder.loadTexts:
    hwTplmTrapsGroup.setStatus(
        "current"
    )

hwUniBaseTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 6, 1, 2)
)
hwUniBaseTrapsGroup.setObjects(
      *(("HUAWEI-UNIMNG-MIB", "hwASBoardFail"),
        ("HUAWEI-UNIMNG-MIB", "hwASBoardFailResume"),
        ("HUAWEI-UNIMNG-MIB", "hwASOpticalInvalid"),
        ("HUAWEI-UNIMNG-MIB", "hwASOpticalInvalidResume"),
        ("HUAWEI-UNIMNG-MIB", "hwASPowerRemove"),
        ("HUAWEI-UNIMNG-MIB", "hwASPowerInsert"),
        ("HUAWEI-UNIMNG-MIB", "hwASPowerInvalid"),
        ("HUAWEI-UNIMNG-MIB", "hwASPowerInvalidResume"),
        ("HUAWEI-UNIMNG-MIB", "hwASFanRemove"),
        ("HUAWEI-UNIMNG-MIB", "hwASFanInsert"),
        ("HUAWEI-UNIMNG-MIB", "hwASFanInvalid"),
        ("HUAWEI-UNIMNG-MIB", "hwASFanInvalidResume"),
        ("HUAWEI-UNIMNG-MIB", "hwASCommunicateError"),
        ("HUAWEI-UNIMNG-MIB", "hwASCommunicateResume"),
        ("HUAWEI-UNIMNG-MIB", "hwASCPUUtilizationRising"),
        ("HUAWEI-UNIMNG-MIB", "hwASCPUUtilizationResume"),
        ("HUAWEI-UNIMNG-MIB", "hwASMemUtilizationRising"),
        ("HUAWEI-UNIMNG-MIB", "hwASMemUtilizationResume"),
        ("HUAWEI-UNIMNG-MIB", "hwASMadConflictDetect"),
        ("HUAWEI-UNIMNG-MIB", "hwASMadConflictResume"),
        ("HUAWEI-UNIMNG-MIB", "hwASBrdTempAlarm"),
        ("HUAWEI-UNIMNG-MIB", "hwASBrdTempResume"))
)
if mibBuilder.loadTexts:
    hwUniBaseTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwTopomngCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 1, 1)
)
if mibBuilder.loadTexts:
    hwTopomngCompliance.setStatus(
        "current"
    )

hwAsmngCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 2, 1)
)
if mibBuilder.loadTexts:
    hwAsmngCompliance.setStatus(
        "current"
    )

hwMbrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 3, 1)
)
if mibBuilder.loadTexts:
    hwMbrCompliance.setStatus(
        "current"
    )

hwVermngCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 4, 1)
)
if mibBuilder.loadTexts:
    hwVermngCompliance.setStatus(
        "current"
    )

hwTplmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 5, 1)
)
if mibBuilder.loadTexts:
    hwTplmCompliance.setStatus(
        "current"
    )

hwUniBaseTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 327, 50, 6, 1)
)
if mibBuilder.loadTexts:
    hwUniBaseTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-UNIMNG-MIB",
    **{"AlarmStatus": AlarmStatus,
       "hwUnimngMIB": hwUnimngMIB,
       "hwUnimngObjects": hwUnimngObjects,
       "hwUniMngEnable": hwUniMngEnable,
       "hwAsmngObjects": hwAsmngObjects,
       "hwAsTable": hwAsTable,
       "hwAsEntry": hwAsEntry,
       "hwAsIndex": hwAsIndex,
       "hwAsHardwareVersion": hwAsHardwareVersion,
       "hwAsIpAddress": hwAsIpAddress,
       "hwAsIpNetMask": hwAsIpNetMask,
       "hwAsAccessUser": hwAsAccessUser,
       "hwAsMac": hwAsMac,
       "hwAsSn": hwAsSn,
       "hwAsSysName": hwAsSysName,
       "hwAsRunState": hwAsRunState,
       "hwAsSoftwareVersion": hwAsSoftwareVersion,
       "hwAsModel": hwAsModel,
       "hwAsDns": hwAsDns,
       "hwAsOnlineTime": hwAsOnlineTime,
       "hwAsCpuUseage": hwAsCpuUseage,
       "hwAsMemoryUseage": hwAsMemoryUseage,
       "hwAsSysMac": hwAsSysMac,
       "hwAsStackEnable": hwAsStackEnable,
       "hwAsGatewayIp": hwAsGatewayIp,
       "hwAsVpnInstance": hwAsVpnInstance,
       "hwAsRowstatus": hwAsRowstatus,
       "hwAsIfTable": hwAsIfTable,
       "hwAsIfEntry": hwAsIfEntry,
       "hwAsIfIndex": hwAsIfIndex,
       "hwAsIfDescr": hwAsIfDescr,
       "hwAsIfType": hwAsIfType,
       "hwAsIfMtu": hwAsIfMtu,
       "hwAsIfSpeed": hwAsIfSpeed,
       "hwAsIfPhysAddress": hwAsIfPhysAddress,
       "hwAsIfAdminStatus": hwAsIfAdminStatus,
       "hwAsIfOperStatus": hwAsIfOperStatus,
       "hwAsIfInUcastPkts": hwAsIfInUcastPkts,
       "hwAsIfOutUcastPkts": hwAsIfOutUcastPkts,
       "hwAsIfXTable": hwAsIfXTable,
       "hwAsIfXEntry": hwAsIfXEntry,
       "hwAsIfName": hwAsIfName,
       "hwAsIfLinkUpDownTrapEnable": hwAsIfLinkUpDownTrapEnable,
       "hwAsIfHighSpeed": hwAsIfHighSpeed,
       "hwAsIfAlias": hwAsIfAlias,
       "hwAsIfAsId": hwAsIfAsId,
       "hwAsIfHCOutOctets": hwAsIfHCOutOctets,
       "hwAsIfInMulticastPkts": hwAsIfInMulticastPkts,
       "hwAsIfInBroadcastPkts": hwAsIfInBroadcastPkts,
       "hwAsIfOutMulticastPkts": hwAsIfOutMulticastPkts,
       "hwAsIfOutBroadcastPkts": hwAsIfOutBroadcastPkts,
       "hwAsIfHCInOctets": hwAsIfHCInOctets,
       "hwAsSlotTable": hwAsSlotTable,
       "hwAsSlotEntry": hwAsSlotEntry,
       "hwAsSlotId": hwAsSlotId,
       "hwAsSlotState": hwAsSlotState,
       "hwAsSlotRowStatus": hwAsSlotRowStatus,
       "hwAsmngGlobalObjects": hwAsmngGlobalObjects,
       "hwAsAutoReplaceEnable": hwAsAutoReplaceEnable,
       "hwAsAuthMode": hwAsAuthMode,
       "hwAsMacWhitelistTable": hwAsMacWhitelistTable,
       "hwAsMacWhitelistEntry": hwAsMacWhitelistEntry,
       "hwAsMacWhitelistMacAddr": hwAsMacWhitelistMacAddr,
       "hwAsMacWhitelistRowStatus": hwAsMacWhitelistRowStatus,
       "hwAsMacBlacklistTable": hwAsMacBlacklistTable,
       "hwAsMacBlacklistEntry": hwAsMacBlacklistEntry,
       "hwAsMacBlacklistMacAddr": hwAsMacBlacklistMacAddr,
       "hwAsMacBlacklistRowStatus": hwAsMacBlacklistRowStatus,
       "hwAsEntityPhysicalTable": hwAsEntityPhysicalTable,
       "hwAsEntityPhysicalEntry": hwAsEntityPhysicalEntry,
       "hwAsEntityPhysicalIndex": hwAsEntityPhysicalIndex,
       "hwAsEntityPhysicalDescr": hwAsEntityPhysicalDescr,
       "hwAsEntityPhysicalVendorType": hwAsEntityPhysicalVendorType,
       "hwAsEntityPhysicalContainedIn": hwAsEntityPhysicalContainedIn,
       "hwAsEntityPhysicalClass": hwAsEntityPhysicalClass,
       "hwAsEntityPhysicalParentRelPos": hwAsEntityPhysicalParentRelPos,
       "hwAsEntityPhysicalName": hwAsEntityPhysicalName,
       "hwAsEntityPhysicalHardwareRev": hwAsEntityPhysicalHardwareRev,
       "hwAsEntityPhysicalFirmwareRev": hwAsEntityPhysicalFirmwareRev,
       "hwAsEntityPhysicalSoftwareRev": hwAsEntityPhysicalSoftwareRev,
       "hwAsEntityPhysicalSerialNum": hwAsEntityPhysicalSerialNum,
       "hwAsEntityPhysicalMfgName": hwAsEntityPhysicalMfgName,
       "hwAsEntityStateTable": hwAsEntityStateTable,
       "hwAsEntityStateEntry": hwAsEntityStateEntry,
       "hwAsEntityAdminStatus": hwAsEntityAdminStatus,
       "hwAsEntityOperStatus": hwAsEntityOperStatus,
       "hwAsEntityStandbyStatus": hwAsEntityStandbyStatus,
       "hwAsEntityAlarmLight": hwAsEntityAlarmLight,
       "hwAsEntityPortType": hwAsEntityPortType,
       "hwAsEntityAliasMappingTable": hwAsEntityAliasMappingTable,
       "hwAsEntityAliasMappingEntry": hwAsEntityAliasMappingEntry,
       "hwAsEntryAliasLogicalIndexOrZero": hwAsEntryAliasLogicalIndexOrZero,
       "hwAsEntryAliasMappingIdentifier": hwAsEntryAliasMappingIdentifier,
       "hwTopomngObjects": hwTopomngObjects,
       "hwTopomngExploreTime": hwTopomngExploreTime,
       "hwTopomngLastCollectDuration": hwTopomngLastCollectDuration,
       "hwTopomngTopoTable": hwTopomngTopoTable,
       "hwTopomngTopoEntry": hwTopomngTopoEntry,
       "hwTopoLocalHop": hwTopoLocalHop,
       "hwTopoLocalMac": hwTopoLocalMac,
       "hwTopoPeerDeviceIndex": hwTopoPeerDeviceIndex,
       "hwTopoPeerMac": hwTopoPeerMac,
       "hwTopoLocalPortName": hwTopoLocalPortName,
       "hwTopoPeerPortName": hwTopoPeerPortName,
       "hwTopoLocalTrunkId": hwTopoLocalTrunkId,
       "hwTopoPeerTrunkId": hwTopoPeerTrunkId,
       "hwTopoLocalRole": hwTopoLocalRole,
       "hwTopoPeerRole": hwTopoPeerRole,
       "hwMbrmngObjects": hwMbrmngObjects,
       "hwMbrMngFabricPortTable": hwMbrMngFabricPortTable,
       "hwMbrMngFabricPortEntry": hwMbrMngFabricPortEntry,
       "hwMbrMngASId": hwMbrMngASId,
       "hwMbrMngFabricPortId": hwMbrMngFabricPortId,
       "hwMbrMngFabricPortMemberIfName": hwMbrMngFabricPortMemberIfName,
       "hwMbrMngFabricPortDirection": hwMbrMngFabricPortDirection,
       "hwMbrMngFabricPortIndirectFlag": hwMbrMngFabricPortIndirectFlag,
       "hwMbrMngFabricPortDescription": hwMbrMngFabricPortDescription,
       "hwVermngObjects": hwVermngObjects,
       "hwVermngGlobalObjects": hwVermngGlobalObjects,
       "hwVermngFileServerType": hwVermngFileServerType,
       "hwVermngUpgradeInfoTable": hwVermngUpgradeInfoTable,
       "hwVermngUpgradeInfoEntry": hwVermngUpgradeInfoEntry,
       "hwVermngUpgradeInfoAsIndex": hwVermngUpgradeInfoAsIndex,
       "hwVermngUpgradeInfoAsName": hwVermngUpgradeInfoAsName,
       "hwVermngUpgradeInfoAsSysSoftware": hwVermngUpgradeInfoAsSysSoftware,
       "hwVermngUpgradeInfoAsSysSoftwareVer": hwVermngUpgradeInfoAsSysSoftwareVer,
       "hwVermngUpgradeInfoAsSysPatch": hwVermngUpgradeInfoAsSysPatch,
       "hwVermngUpgradeInfoAsDownloadSoftware": hwVermngUpgradeInfoAsDownloadSoftware,
       "hwVermngUpgradeInfoAsDownloadSoftwareVer": hwVermngUpgradeInfoAsDownloadSoftwareVer,
       "hwVermngUpgradeInfoAsDownloadPatch": hwVermngUpgradeInfoAsDownloadPatch,
       "hwVermngUpgradeInfoAsUpgradeState": hwVermngUpgradeInfoAsUpgradeState,
       "hwVermngUpgradeInfoAsUpgradeType": hwVermngUpgradeInfoAsUpgradeType,
       "hwVermngUpgradeInfoAsFilePhase": hwVermngUpgradeInfoAsFilePhase,
       "hwVermngUpgradeInfoAsUpgradePhase": hwVermngUpgradeInfoAsUpgradePhase,
       "hwVermngUpgradeInfoAsUpgradeResult": hwVermngUpgradeInfoAsUpgradeResult,
       "hwVermngUpgradeInfoAsErrorCode": hwVermngUpgradeInfoAsErrorCode,
       "hwVermngUpgradeInfoAsErrorDescr": hwVermngUpgradeInfoAsErrorDescr,
       "hwVermngAsTypeCfgInfoTable": hwVermngAsTypeCfgInfoTable,
       "hwVermngAsTypeCfgInfoEntry": hwVermngAsTypeCfgInfoEntry,
       "hwVermngAsTypeCfgInfoAsTypeIndex": hwVermngAsTypeCfgInfoAsTypeIndex,
       "hwVermngAsTypeCfgInfoAsTypeName": hwVermngAsTypeCfgInfoAsTypeName,
       "hwVermngAsTypeCfgInfoSystemSoftware": hwVermngAsTypeCfgInfoSystemSoftware,
       "hwVermngAsTypeCfgInfoSystemSoftwareVer": hwVermngAsTypeCfgInfoSystemSoftwareVer,
       "hwVermngAsTypeCfgInfoPatch": hwVermngAsTypeCfgInfoPatch,
       "hwVermngAsTypeCfgInfoRowStatus": hwVermngAsTypeCfgInfoRowStatus,
       "hwTplmObjects": hwTplmObjects,
       "hwTplmASGroupTable": hwTplmASGroupTable,
       "hwTplmASGroupEntry": hwTplmASGroupEntry,
       "hwTplmASGroupIndex": hwTplmASGroupIndex,
       "hwTplmASGroupName": hwTplmASGroupName,
       "hwTplmASAdminProfileName": hwTplmASAdminProfileName,
       "hwTplmASGroupProfileStatus": hwTplmASGroupProfileStatus,
       "hwTplmASGroupRowStatus": hwTplmASGroupRowStatus,
       "hwTplmASTable": hwTplmASTable,
       "hwTplmASEntry": hwTplmASEntry,
       "hwTplmASId": hwTplmASId,
       "hwTplmASASGroupName": hwTplmASASGroupName,
       "hwTplmASRowStatus": hwTplmASRowStatus,
       "hwTplmPortGroupTable": hwTplmPortGroupTable,
       "hwTplmPortGroupEntry": hwTplmPortGroupEntry,
       "hwTplmPortGroupIndex": hwTplmPortGroupIndex,
       "hwTplmPortGroupName": hwTplmPortGroupName,
       "hwTplmPortGroupType": hwTplmPortGroupType,
       "hwTplmPortGroupNetworkBasicProfile": hwTplmPortGroupNetworkBasicProfile,
       "hwTplmPortGroupNetworkEnhancedProfile": hwTplmPortGroupNetworkEnhancedProfile,
       "hwTplmPortGroupUserAccessProfile": hwTplmPortGroupUserAccessProfile,
       "hwTplmPortGroupProfileStatus": hwTplmPortGroupProfileStatus,
       "hwTplmPortGroupRowStatus": hwTplmPortGroupRowStatus,
       "hwTplmPortTable": hwTplmPortTable,
       "hwTplmPortEntry": hwTplmPortEntry,
       "hwTplmPortIfIndex": hwTplmPortIfIndex,
       "hwTplmPortPortGroupName": hwTplmPortPortGroupName,
       "hwTplmPortRowStatus": hwTplmPortRowStatus,
       "hwTplmConfigManagement": hwTplmConfigManagement,
       "hwTplmConfigCommitAll": hwTplmConfigCommitAll,
       "hwTplmConfigManagementTable": hwTplmConfigManagementTable,
       "hwTplmConfigManagementEntry": hwTplmConfigManagementEntry,
       "hwTplmConfigManagementASId": hwTplmConfigManagementASId,
       "hwTplmConfigManagementCommit": hwTplmConfigManagementCommit,
       "hwUnimngNotification": hwUnimngNotification,
       "hwTopomngTrap": hwTopomngTrap,
       "hwTopomngTrapObjects": hwTopomngTrapObjects,
       "hwTopomngTrapLocalMac": hwTopomngTrapLocalMac,
       "hwTopomngTrapLocalPortName": hwTopomngTrapLocalPortName,
       "hwTopomngTrapLocalTrunkId": hwTopomngTrapLocalTrunkId,
       "hwTopomngTrapPeerMac": hwTopomngTrapPeerMac,
       "hwTopomngTrapPeerPortName": hwTopomngTrapPeerPortName,
       "hwTopomngTrapPeerTrunkId": hwTopomngTrapPeerTrunkId,
       "hwTopomngTrapReason": hwTopomngTrapReason,
       "hwTopomngTraps": hwTopomngTraps,
       "hwTopomngLinkNormal": hwTopomngLinkNormal,
       "hwTopomngLinkAbnormal": hwTopomngLinkAbnormal,
       "hwAsmngTrap": hwAsmngTrap,
       "hwAsmngTrapObjects": hwAsmngTrapObjects,
       "hwAsmngTrapAsIndex": hwAsmngTrapAsIndex,
       "hwAsmngTrapAsModel": hwAsmngTrapAsModel,
       "hwAsmngTrapAsSysName": hwAsmngTrapAsSysName,
       "hwAsmngTrapAsMac": hwAsmngTrapAsMac,
       "hwAsmngTrapAsSn": hwAsmngTrapAsSn,
       "hwAsmngTrapAsIfIndex": hwAsmngTrapAsIfIndex,
       "hwAsmngTrapAsIfOperStatus": hwAsmngTrapAsIfOperStatus,
       "hwAsmngTrapAsFaultTimes": hwAsmngTrapAsFaultTimes,
       "hwAsmngTrapAsIfAdminStatus": hwAsmngTrapAsIfAdminStatus,
       "hwAsmngTrapAsIfName": hwAsmngTrapAsIfName,
       "hwAsmngTrapAsActualeType": hwAsmngTrapAsActualeType,
       "hwAsmngTrapAsVersion": hwAsmngTrapAsVersion,
       "hwAsmngTrapParentVersion": hwAsmngTrapParentVersion,
       "hwAsmngTrapAddedAsMac": hwAsmngTrapAddedAsMac,
       "hwAsmngTrapAsSlotId": hwAsmngTrapAsSlotId,
       "hwAsmngTrapAddedAsSlotType": hwAsmngTrapAddedAsSlotType,
       "hwAsmngTrapAsPermitNum": hwAsmngTrapAsPermitNum,
       "hwAsmngTrapAsUnimngMode": hwAsmngTrapAsUnimngMode,
       "hwAsmngTrapParentUnimngMode": hwAsmngTrapParentUnimngMode,
       "hwAsmngTrapAsIfType": hwAsmngTrapAsIfType,
       "hwAsmngTrapAsOnlineFailReasonId": hwAsmngTrapAsOnlineFailReasonId,
       "hwAsmngTrapAsOnlineFailReasonDesc": hwAsmngTrapAsOnlineFailReasonDesc,
       "hwAsmngTraps": hwAsmngTraps,
       "hwAsFaultNotify": hwAsFaultNotify,
       "hwAsNormalNotify": hwAsNormalNotify,
       "hwAsAddOffLineNotify": hwAsAddOffLineNotify,
       "hwAsDelOffLineNotify": hwAsDelOffLineNotify,
       "hwAsPortStateChangeToDownNotify": hwAsPortStateChangeToDownNotify,
       "hwAsPortStateChangeToUpNotify": hwAsPortStateChangeToUpNotify,
       "hwAsModelNotMatchNotify": hwAsModelNotMatchNotify,
       "hwAsVersionNotMatchNotify": hwAsVersionNotMatchNotify,
       "hwAsNameConflictNotify": hwAsNameConflictNotify,
       "hwAsSlotModelNotMatchNotify": hwAsSlotModelNotMatchNotify,
       "hwAsFullNotify": hwAsFullNotify,
       "hwUnimngModeNotMatchNotify": hwUnimngModeNotMatchNotify,
       "hwAsBoardAddNotify": hwAsBoardAddNotify,
       "hwAsBoardDeleteNotify": hwAsBoardDeleteNotify,
       "hwAsBoardPlugInNotify": hwAsBoardPlugInNotify,
       "hwAsBoardPlugOutNotify": hwAsBoardPlugOutNotify,
       "hwAsInBlacklistNotify": hwAsInBlacklistNotify,
       "hwAsUnconfirmedNotify": hwAsUnconfirmedNotify,
       "hwAsComboPortTypeChangeNotify": hwAsComboPortTypeChangeNotify,
       "hwAsOnlineFailNotify": hwAsOnlineFailNotify,
       "hwAsSlotIdInvalidNotify": hwAsSlotIdInvalidNotify,
       "hwAsSysmacSwitchCfgErrNotify": hwAsSysmacSwitchCfgErrNotify,
       "hwUniMbrTrap": hwUniMbrTrap,
       "hwUniMbrTrapObjects": hwUniMbrTrapObjects,
       "hwUniMbrLinkStatTrapLocalMac": hwUniMbrLinkStatTrapLocalMac,
       "hwUniMbrLinkStatTrapLocalPortName": hwUniMbrLinkStatTrapLocalPortName,
       "hwUniMbrLinkStatTrapChangeType": hwUniMbrLinkStatTrapChangeType,
       "hwUniMbrTrapConnectErrorReason": hwUniMbrTrapConnectErrorReason,
       "hwUniMbrTrapReceivePktRate": hwUniMbrTrapReceivePktRate,
       "hwUniMbrTrapAsIndex": hwUniMbrTrapAsIndex,
       "hwUniMbrTrapAsSysName": hwUniMbrTrapAsSysName,
       "hwUniMbrParaSynFailReason": hwUniMbrParaSynFailReason,
       "hwUniMbrTrapIllegalConfigReason": hwUniMbrTrapIllegalConfigReason,
       "hwUniMbrTraps": hwUniMbrTraps,
       "hwUniMbrConnectError": hwUniMbrConnectError,
       "hwUniMbrASDiscoverAttack": hwUniMbrASDiscoverAttack,
       "hwUniMbrFabricPortMemberDelete": hwUniMbrFabricPortMemberDelete,
       "hwUniMbrIllegalFabricConfig": hwUniMbrIllegalFabricConfig,
       "hwVermngTrap": hwVermngTrap,
       "hwVermngTrapObjects": hwVermngTrapObjects,
       "hwVermngTraps": hwVermngTraps,
       "hwVermngUpgradeFail": hwVermngUpgradeFail,
       "hwTplmTrap": hwTplmTrap,
       "hwTplmTrapObjects": hwTplmTrapObjects,
       "hwTplmTrapASName": hwTplmTrapASName,
       "hwTplmTrapFailedReason": hwTplmTrapFailedReason,
       "hwTplmTraps": hwTplmTraps,
       "hwTplmCmdExecuteFailedNotify": hwTplmCmdExecuteFailedNotify,
       "hwTplmCmdExecuteSuccessfulNotify": hwTplmCmdExecuteSuccessfulNotify,
       "hwTplmDirectCmdRecoverFail": hwTplmDirectCmdRecoverFail,
       "hwUniAsBaseTrap": hwUniAsBaseTrap,
       "hwUniAsBaseTrapObjects": hwUniAsBaseTrapObjects,
       "hwUniAsBaseAsName": hwUniAsBaseAsName,
       "hwUniAsBaseAsId": hwUniAsBaseAsId,
       "hwUniAsBaseEntityPhysicalIndex": hwUniAsBaseEntityPhysicalIndex,
       "hwUniAsBaseTrapSeverity": hwUniAsBaseTrapSeverity,
       "hwUniAsBaseTrapProbableCause": hwUniAsBaseTrapProbableCause,
       "hwUniAsBaseTrapEventType": hwUniAsBaseTrapEventType,
       "hwUniAsBaseEntPhysicalContainedIn": hwUniAsBaseEntPhysicalContainedIn,
       "hwUniAsBaseEntPhysicalName": hwUniAsBaseEntPhysicalName,
       "hwUniAsBaseRelativeResource": hwUniAsBaseRelativeResource,
       "hwUniAsBaseReasonDescription": hwUniAsBaseReasonDescription,
       "hwUniAsBaseThresholdType": hwUniAsBaseThresholdType,
       "hwUniAsBaseThresholdValue": hwUniAsBaseThresholdValue,
       "hwUniAsBaseThresholdUnit": hwUniAsBaseThresholdUnit,
       "hwUniAsBaseThresholdHighWarning": hwUniAsBaseThresholdHighWarning,
       "hwUniAsBaseThresholdHighCritical": hwUniAsBaseThresholdHighCritical,
       "hwUniAsBaseThresholdLowWarning": hwUniAsBaseThresholdLowWarning,
       "hwUniAsBaseThresholdLowCritical": hwUniAsBaseThresholdLowCritical,
       "hwUniAsBaseEntityTrapEntType": hwUniAsBaseEntityTrapEntType,
       "hwUniAsBaseEntityTrapEntFaultID": hwUniAsBaseEntityTrapEntFaultID,
       "hwUniAsBaseEntityTrapCommunicateType": hwUniAsBaseEntityTrapCommunicateType,
       "hwUniAsBaseThresholdEntValue": hwUniAsBaseThresholdEntValue,
       "hwUniAsBaseThresholdEntCurrent": hwUniAsBaseThresholdEntCurrent,
       "hwUniAsBaseEntPhysicalIndex": hwUniAsBaseEntPhysicalIndex,
       "hwUniAsBaseThresholdHwBaseThresholdType": hwUniAsBaseThresholdHwBaseThresholdType,
       "hwUniAsBaseThresholdHwBaseThresholdIndex": hwUniAsBaseThresholdHwBaseThresholdIndex,
       "hwUniAsBaseTraps": hwUniAsBaseTraps,
       "hwASEnvironmentTrap": hwASEnvironmentTrap,
       "hwASBrdTempAlarm": hwASBrdTempAlarm,
       "hwASBrdTempResume": hwASBrdTempResume,
       "hwASBoardTrap": hwASBoardTrap,
       "hwASBoardFail": hwASBoardFail,
       "hwASBoardFailResume": hwASBoardFailResume,
       "hwASOpticalTrap": hwASOpticalTrap,
       "hwASOpticalInvalid": hwASOpticalInvalid,
       "hwASOpticalInvalidResume": hwASOpticalInvalidResume,
       "hwASPowerTrap": hwASPowerTrap,
       "hwASPowerRemove": hwASPowerRemove,
       "hwASPowerInsert": hwASPowerInsert,
       "hwASPowerInvalid": hwASPowerInvalid,
       "hwASPowerInvalidResume": hwASPowerInvalidResume,
       "hwASFanTrap": hwASFanTrap,
       "hwASFanRemove": hwASFanRemove,
       "hwASFanInsert": hwASFanInsert,
       "hwASFanInvalid": hwASFanInvalid,
       "hwASFanInvalidResume": hwASFanInvalidResume,
       "hwASCommunicateTrap": hwASCommunicateTrap,
       "hwASCommunicateError": hwASCommunicateError,
       "hwASCommunicateResume": hwASCommunicateResume,
       "hwASCPUTrap": hwASCPUTrap,
       "hwASCPUUtilizationRising": hwASCPUUtilizationRising,
       "hwASCPUUtilizationResume": hwASCPUUtilizationResume,
       "hwASMemoryTrap": hwASMemoryTrap,
       "hwASMemUtilizationRising": hwASMemUtilizationRising,
       "hwASMemUtilizationResume": hwASMemUtilizationResume,
       "hwASMadTrap": hwASMadTrap,
       "hwASMadConflictDetect": hwASMadConflictDetect,
       "hwASMadConflictResume": hwASMadConflictResume,
       "hwUnimngConformance": hwUnimngConformance,
       "hwTopomngCompliances": hwTopomngCompliances,
       "hwTopomngCompliance": hwTopomngCompliance,
       "hwTopomngObjectsGroup": hwTopomngObjectsGroup,
       "hwTopomngTopoGroup": hwTopomngTopoGroup,
       "hwTopomngTrapObjectsGroup": hwTopomngTrapObjectsGroup,
       "hwTopomngTrapsGroup": hwTopomngTrapsGroup,
       "hwAsmngCompliances": hwAsmngCompliances,
       "hwAsmngCompliance": hwAsmngCompliance,
       "hwAsmngObjectsGroup": hwAsmngObjectsGroup,
       "hwAsmngAsGroup": hwAsmngAsGroup,
       "hwAsmngAsIfGroup": hwAsmngAsIfGroup,
       "hwAsmngAsIfXGroup": hwAsmngAsIfXGroup,
       "hwAsmngTrapObjectsGroup": hwAsmngTrapObjectsGroup,
       "hwAsmngTrapsGroup": hwAsmngTrapsGroup,
       "hwAsmngGlobalObjectsGroup": hwAsmngGlobalObjectsGroup,
       "hwAsmngMacWhitelistGroup": hwAsmngMacWhitelistGroup,
       "hwAsmngMacBlacklistGroup": hwAsmngMacBlacklistGroup,
       "hwAsmngEntityPhysicalGroup": hwAsmngEntityPhysicalGroup,
       "hwAsmngEntityStateGroup": hwAsmngEntityStateGroup,
       "hwAsmngEntityAliasMappingGroup": hwAsmngEntityAliasMappingGroup,
       "hwAsmngSlotGroup": hwAsmngSlotGroup,
       "hwMbrCompliances": hwMbrCompliances,
       "hwMbrCompliance": hwMbrCompliance,
       "hwMbrTrapObjectsGroup": hwMbrTrapObjectsGroup,
       "hwMbrTrapsGroup": hwMbrTrapsGroup,
       "hwMbrFabricPortGroup": hwMbrFabricPortGroup,
       "hwVermngCompliances": hwVermngCompliances,
       "hwVermngCompliance": hwVermngCompliance,
       "hwVermngObjectsGroup": hwVermngObjectsGroup,
       "hwVermngUpgradeInfoGroup": hwVermngUpgradeInfoGroup,
       "hwVermngAsTypeCfgInfoGroup": hwVermngAsTypeCfgInfoGroup,
       "hwVermngTrapsGroup": hwVermngTrapsGroup,
       "hwTplmCompliances": hwTplmCompliances,
       "hwTplmCompliance": hwTplmCompliance,
       "hwTplmASGroupGoup": hwTplmASGroupGoup,
       "hwTplmASGoup": hwTplmASGoup,
       "hwTplmPortGroupGoup": hwTplmPortGroupGoup,
       "hwTplmPortGoup": hwTplmPortGoup,
       "hwTplmConfigManagementGoup": hwTplmConfigManagementGoup,
       "hwTplmTrapObjectsGroup": hwTplmTrapObjectsGroup,
       "hwTplmTrapsGroup": hwTplmTrapsGroup,
       "hwUniBaseTrapCompliances": hwUniBaseTrapCompliances,
       "hwUniBaseTrapCompliance": hwUniBaseTrapCompliance,
       "hwUniBaseTrapObjectsGroup": hwUniBaseTrapObjectsGroup,
       "hwUniBaseTrapsGroup": hwUniBaseTrapsGroup}
)
