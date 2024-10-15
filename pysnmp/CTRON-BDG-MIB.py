# SNMP MIB module (CTRON-BDG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-BDG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:33 2024
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

(bridge,
 layerMgmt) = mibBuilder.importSymbols(
    "IRM-OIDS",
    "bridge",
    "layerMgmt")

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

_BridgeRev1_ObjectIdentity = ObjectIdentity
bridgeRev1 = _BridgeRev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1)
)
_Bdgdevice_ObjectIdentity = ObjectIdentity
bdgdevice = _Bdgdevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1)
)


class _BdgdeviceDisableBdg_Type(Integer32):
    """Custom type bdgdeviceDisableBdg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableBridge", 0),
          ("enableBridge", 1))
    )


_BdgdeviceDisableBdg_Type.__name__ = "Integer32"
_BdgdeviceDisableBdg_Object = MibScalar
bdgdeviceDisableBdg = _BdgdeviceDisableBdg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 1),
    _BdgdeviceDisableBdg_Type()
)
bdgdeviceDisableBdg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceDisableBdg.setStatus("mandatory")


class _BdgdeviceRestoreSettings_Type(Integer32):
    """Custom type bdgdeviceRestoreSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("restoreSettings", 0)
    )


_BdgdeviceRestoreSettings_Type.__name__ = "Integer32"
_BdgdeviceRestoreSettings_Object = MibScalar
bdgdeviceRestoreSettings = _BdgdeviceRestoreSettings_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 2),
    _BdgdeviceRestoreSettings_Type()
)
bdgdeviceRestoreSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceRestoreSettings.setStatus("mandatory")
_BdgdeviceBdgName_Type = OctetString
_BdgdeviceBdgName_Object = MibScalar
bdgdeviceBdgName = _BdgdeviceBdgName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 4),
    _BdgdeviceBdgName_Type()
)
bdgdeviceBdgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceBdgName.setStatus("mandatory")
_BdgdeviceNumPorts_Type = Integer32
_BdgdeviceNumPorts_Object = MibScalar
bdgdeviceNumPorts = _BdgdeviceNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 5),
    _BdgdeviceNumPorts_Type()
)
bdgdeviceNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceNumPorts.setStatus("mandatory")
_BdgdeviceType_Type = OctetString
_BdgdeviceType_Object = MibScalar
bdgdeviceType = _BdgdeviceType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 6),
    _BdgdeviceType_Type()
)
bdgdeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceType.setStatus("mandatory")
_BdgdeviceVersion_Type = OctetString
_BdgdeviceVersion_Object = MibScalar
bdgdeviceVersion = _BdgdeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 7),
    _BdgdeviceVersion_Type()
)
bdgdeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceVersion.setStatus("mandatory")
_BdgdeviceLocation_Type = OctetString
_BdgdeviceLocation_Object = MibScalar
bdgdeviceLocation = _BdgdeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 8),
    _BdgdeviceLocation_Type()
)
bdgdeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceLocation.setStatus("mandatory")
_BdgdeviceStatus_Type = OctetString
_BdgdeviceStatus_Object = MibScalar
bdgdeviceStatus = _BdgdeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 9),
    _BdgdeviceStatus_Type()
)
bdgdeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceStatus.setStatus("mandatory")


class _BdgdeviceRestartBdg_Type(Integer32):
    """Custom type bdgdeviceRestartBdg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("restartBridge", 0)
    )


_BdgdeviceRestartBdg_Type.__name__ = "Integer32"
_BdgdeviceRestartBdg_Object = MibScalar
bdgdeviceRestartBdg = _BdgdeviceRestartBdg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 10),
    _BdgdeviceRestartBdg_Type()
)
bdgdeviceRestartBdg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceRestartBdg.setStatus("mandatory")
_BdgdeviceFrFwd_Type = Counter32
_BdgdeviceFrFwd_Object = MibScalar
bdgdeviceFrFwd = _BdgdeviceFrFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 11),
    _BdgdeviceFrFwd_Type()
)
bdgdeviceFrFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceFrFwd.setStatus("mandatory")
_BdgdeviceFrRx_Type = Counter32
_BdgdeviceFrRx_Object = MibScalar
bdgdeviceFrRx = _BdgdeviceFrRx_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 12),
    _BdgdeviceFrRx_Type()
)
bdgdeviceFrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceFrRx.setStatus("mandatory")
_BdgdeviceFrFlt_Type = Counter32
_BdgdeviceFrFlt_Object = MibScalar
bdgdeviceFrFlt = _BdgdeviceFrFlt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 13),
    _BdgdeviceFrFlt_Type()
)
bdgdeviceFrFlt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceFrFlt.setStatus("mandatory")
_BdgdeviceErr_Type = Counter32
_BdgdeviceErr_Object = MibScalar
bdgdeviceErr = _BdgdeviceErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 14),
    _BdgdeviceErr_Type()
)
bdgdeviceErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceErr.setStatus("mandatory")
_BdgdeviceSwitchSetting_Type = OctetString
_BdgdeviceSwitchSetting_Object = MibScalar
bdgdeviceSwitchSetting = _BdgdeviceSwitchSetting_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 15),
    _BdgdeviceSwitchSetting_Type()
)
bdgdeviceSwitchSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceSwitchSetting.setStatus("mandatory")
_BdgdeviceNumRestarts_Type = Counter32
_BdgdeviceNumRestarts_Object = MibScalar
bdgdeviceNumRestarts = _BdgdeviceNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 16),
    _BdgdeviceNumRestarts_Type()
)
bdgdeviceNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceNumRestarts.setStatus("mandatory")


class _BdgdeviceTypeFiltering_Type(Integer32):
    """Custom type bdgdeviceTypeFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("ieee8021", 0),
          ("specialDB", 1))
    )


_BdgdeviceTypeFiltering_Type.__name__ = "Integer32"
_BdgdeviceTypeFiltering_Object = MibScalar
bdgdeviceTypeFiltering = _BdgdeviceTypeFiltering_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 17),
    _BdgdeviceTypeFiltering_Type()
)
bdgdeviceTypeFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceTypeFiltering.setStatus("mandatory")


class _BdgdeviceSTAProtocol_Type(Integer32):
    """Custom type bdgdeviceSTAProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dec", 1),
          ("ieee8021", 0),
          ("none", 2))
    )


_BdgdeviceSTAProtocol_Type.__name__ = "Integer32"
_BdgdeviceSTAProtocol_Object = MibScalar
bdgdeviceSTAProtocol = _BdgdeviceSTAProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 18),
    _BdgdeviceSTAProtocol_Type()
)
bdgdeviceSTAProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceSTAProtocol.setStatus("mandatory")
_BdgdeviceBridgeID_Type = OctetString
_BdgdeviceBridgeID_Object = MibScalar
bdgdeviceBridgeID = _BdgdeviceBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 19),
    _BdgdeviceBridgeID_Type()
)
bdgdeviceBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceBridgeID.setStatus("mandatory")
_BdgdeviceTopChgCnt_Type = Counter32
_BdgdeviceTopChgCnt_Object = MibScalar
bdgdeviceTopChgCnt = _BdgdeviceTopChgCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 20),
    _BdgdeviceTopChgCnt_Type()
)
bdgdeviceTopChgCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceTopChgCnt.setStatus("mandatory")
_BdgdeviceRootCost_Type = Integer32
_BdgdeviceRootCost_Object = MibScalar
bdgdeviceRootCost = _BdgdeviceRootCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 21),
    _BdgdeviceRootCost_Type()
)
bdgdeviceRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceRootCost.setStatus("mandatory")
_BdgdeviceRootPort_Type = Integer32
_BdgdeviceRootPort_Object = MibScalar
bdgdeviceRootPort = _BdgdeviceRootPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 22),
    _BdgdeviceRootPort_Type()
)
bdgdeviceRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceRootPort.setStatus("mandatory")
_BdgdeviceHelloTime_Type = Integer32
_BdgdeviceHelloTime_Object = MibScalar
bdgdeviceHelloTime = _BdgdeviceHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 23),
    _BdgdeviceHelloTime_Type()
)
bdgdeviceHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceHelloTime.setStatus("mandatory")
_BdgdeviceBdgMaxAge_Type = Integer32
_BdgdeviceBdgMaxAge_Object = MibScalar
bdgdeviceBdgMaxAge = _BdgdeviceBdgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 24),
    _BdgdeviceBdgMaxAge_Type()
)
bdgdeviceBdgMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceBdgMaxAge.setStatus("mandatory")
_BdgdeviceBdgFwdDly_Type = Integer32
_BdgdeviceBdgFwdDly_Object = MibScalar
bdgdeviceBdgFwdDly = _BdgdeviceBdgFwdDly_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 25),
    _BdgdeviceBdgFwdDly_Type()
)
bdgdeviceBdgFwdDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceBdgFwdDly.setStatus("mandatory")
_BdgdeviceTimeTopChg_Type = Integer32
_BdgdeviceTimeTopChg_Object = MibScalar
bdgdeviceTimeTopChg = _BdgdeviceTimeTopChg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 26),
    _BdgdeviceTimeTopChg_Type()
)
bdgdeviceTimeTopChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceTimeTopChg.setStatus("mandatory")


class _BdgdeviceTopChg_Type(Integer32):
    """Custom type bdgdeviceTopChg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noTopologyChangeInProgress", 0),
          ("topologyChangeInProgress", 1))
    )


_BdgdeviceTopChg_Type.__name__ = "Integer32"
_BdgdeviceTopChg_Object = MibScalar
bdgdeviceTopChg = _BdgdeviceTopChg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 27),
    _BdgdeviceTopChg_Type()
)
bdgdeviceTopChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceTopChg.setStatus("mandatory")
_BdgdeviceDesigRoot_Type = OctetString
_BdgdeviceDesigRoot_Object = MibScalar
bdgdeviceDesigRoot = _BdgdeviceDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 28),
    _BdgdeviceDesigRoot_Type()
)
bdgdeviceDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceDesigRoot.setStatus("mandatory")
_BdgdeviceMaxAge_Type = Integer32
_BdgdeviceMaxAge_Object = MibScalar
bdgdeviceMaxAge = _BdgdeviceMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 29),
    _BdgdeviceMaxAge_Type()
)
bdgdeviceMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceMaxAge.setStatus("mandatory")
_BdgdeviceHoldTime_Type = Integer32
_BdgdeviceHoldTime_Object = MibScalar
bdgdeviceHoldTime = _BdgdeviceHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 30),
    _BdgdeviceHoldTime_Type()
)
bdgdeviceHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceHoldTime.setStatus("mandatory")
_BdgdeviceFwdDly_Type = Integer32
_BdgdeviceFwdDly_Object = MibScalar
bdgdeviceFwdDly = _BdgdeviceFwdDly_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 31),
    _BdgdeviceFwdDly_Type()
)
bdgdeviceFwdDly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceFwdDly.setStatus("mandatory")
_BdgdeviceBdgHello_Type = Integer32
_BdgdeviceBdgHello_Object = MibScalar
bdgdeviceBdgHello = _BdgdeviceBdgHello_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 32),
    _BdgdeviceBdgHello_Type()
)
bdgdeviceBdgHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceBdgHello.setStatus("mandatory")
_BdgdeviceBdgPriority_Type = Integer32
_BdgdeviceBdgPriority_Object = MibScalar
bdgdeviceBdgPriority = _BdgdeviceBdgPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 33),
    _BdgdeviceBdgPriority_Type()
)
bdgdeviceBdgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceBdgPriority.setStatus("mandatory")


class _BdgdeviceResetCounts_Type(Integer32):
    """Custom type bdgdeviceResetCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("resetCounts", 0)
    )


_BdgdeviceResetCounts_Type.__name__ = "Integer32"
_BdgdeviceResetCounts_Object = MibScalar
bdgdeviceResetCounts = _BdgdeviceResetCounts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 34),
    _BdgdeviceResetCounts_Type()
)
bdgdeviceResetCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgdeviceResetCounts.setStatus("mandatory")
_BdgdeviceUptime_Type = Integer32
_BdgdeviceUptime_Object = MibScalar
bdgdeviceUptime = _BdgdeviceUptime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 35),
    _BdgdeviceUptime_Type()
)
bdgdeviceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceUptime.setStatus("mandatory")
_BdgdeviceTrapType_Type = ObjectIdentifier
_BdgdeviceTrapType_Object = MibScalar
bdgdeviceTrapType = _BdgdeviceTrapType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 1, 36),
    _BdgdeviceTrapType_Type()
)
bdgdeviceTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgdeviceTrapType.setStatus("mandatory")
_BdgPort_ObjectIdentity = ObjectIdentity
bdgPort = _BdgPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2)
)
_BdgPortAddress_Type = OctetString
_BdgPortAddress_Object = MibScalar
bdgPortAddress = _BdgPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 1),
    _BdgPortAddress_Type()
)
bdgPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortAddress.setStatus("mandatory")
_BdgPortName_Type = OctetString
_BdgPortName_Object = MibScalar
bdgPortName = _BdgPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 2),
    _BdgPortName_Type()
)
bdgPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgPortName.setStatus("mandatory")
_BdgPortType_Type = OctetString
_BdgPortType_Object = MibScalar
bdgPortType = _BdgPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 3),
    _BdgPortType_Type()
)
bdgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortType.setStatus("mandatory")
_BdgPortStatus_Type = OctetString
_BdgPortStatus_Object = MibScalar
bdgPortStatus = _BdgPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 4),
    _BdgPortStatus_Type()
)
bdgPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortStatus.setStatus("mandatory")
_BdgPortNetName_Type = OctetString
_BdgPortNetName_Object = MibScalar
bdgPortNetName = _BdgPortNetName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 5),
    _BdgPortNetName_Type()
)
bdgPortNetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgPortNetName.setStatus("mandatory")
_BdgPortFrRx_Type = Counter32
_BdgPortFrRx_Object = MibScalar
bdgPortFrRx = _BdgPortFrRx_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 6),
    _BdgPortFrRx_Type()
)
bdgPortFrRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortFrRx.setStatus("mandatory")
_BdgPortDisInb_Type = Counter32
_BdgPortDisInb_Object = MibScalar
bdgPortDisInb = _BdgPortDisInb_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 7),
    _BdgPortDisInb_Type()
)
bdgPortDisInb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDisInb.setStatus("mandatory")
_BdgPortFwdOutb_Type = Counter32
_BdgPortFwdOutb_Object = MibScalar
bdgPortFwdOutb = _BdgPortFwdOutb_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 8),
    _BdgPortFwdOutb_Type()
)
bdgPortFwdOutb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortFwdOutb.setStatus("mandatory")
_BdgPortDisLOB_Type = Counter32
_BdgPortDisLOB_Object = MibScalar
bdgPortDisLOB = _BdgPortDisLOB_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 9),
    _BdgPortDisLOB_Type()
)
bdgPortDisLOB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDisLOB.setStatus("mandatory")
_BdgPortDisTDE_Type = Counter32
_BdgPortDisTDE_Object = MibScalar
bdgPortDisTDE = _BdgPortDisTDE_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 10),
    _BdgPortDisTDE_Type()
)
bdgPortDisTDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDisTDE.setStatus("mandatory")
_BdgPortDisErr_Type = Counter32
_BdgPortDisErr_Object = MibScalar
bdgPortDisErr = _BdgPortDisErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 11),
    _BdgPortDisErr_Type()
)
bdgPortDisErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDisErr.setStatus("mandatory")
_BdgPortColl_Type = Counter32
_BdgPortColl_Object = MibScalar
bdgPortColl = _BdgPortColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 12),
    _BdgPortColl_Type()
)
bdgPortColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortColl.setStatus("mandatory")
_BdgPortTxAbrt_Type = Counter32
_BdgPortTxAbrt_Object = MibScalar
bdgPortTxAbrt = _BdgPortTxAbrt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 13),
    _BdgPortTxAbrt_Type()
)
bdgPortTxAbrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortTxAbrt.setStatus("mandatory")
_BdgPortOowColl_Type = Counter32
_BdgPortOowColl_Object = MibScalar
bdgPortOowColl = _BdgPortOowColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 14),
    _BdgPortOowColl_Type()
)
bdgPortOowColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortOowColl.setStatus("mandatory")
_BdgPortCRCErr_Type = Counter32
_BdgPortCRCErr_Object = MibScalar
bdgPortCRCErr = _BdgPortCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 15),
    _BdgPortCRCErr_Type()
)
bdgPortCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortCRCErr.setStatus("mandatory")
_BdgPortFrAlErr_Type = Counter32
_BdgPortFrAlErr_Object = MibScalar
bdgPortFrAlErr = _BdgPortFrAlErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 16),
    _BdgPortFrAlErr_Type()
)
bdgPortFrAlErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortFrAlErr.setStatus("mandatory")
_BdgPortPriority_Type = Integer32
_BdgPortPriority_Object = MibScalar
bdgPortPriority = _BdgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 17),
    _BdgPortPriority_Type()
)
bdgPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgPortPriority.setStatus("mandatory")
_BdgPortState_Type = OctetString
_BdgPortState_Object = MibScalar
bdgPortState = _BdgPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 18),
    _BdgPortState_Type()
)
bdgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortState.setStatus("mandatory")
_BdgPortPathCost_Type = Integer32
_BdgPortPathCost_Object = MibScalar
bdgPortPathCost = _BdgPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 19),
    _BdgPortPathCost_Type()
)
bdgPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdgPortPathCost.setStatus("mandatory")
_BdgPortDesigCost_Type = Integer32
_BdgPortDesigCost_Object = MibScalar
bdgPortDesigCost = _BdgPortDesigCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 20),
    _BdgPortDesigCost_Type()
)
bdgPortDesigCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDesigCost.setStatus("mandatory")
_BdgPortDesigBrdg_Type = OctetString
_BdgPortDesigBrdg_Object = MibScalar
bdgPortDesigBrdg = _BdgPortDesigBrdg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 21),
    _BdgPortDesigBrdg_Type()
)
bdgPortDesigBrdg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDesigBrdg.setStatus("mandatory")
_BdgPortDesigPort_Type = Integer32
_BdgPortDesigPort_Object = MibScalar
bdgPortDesigPort = _BdgPortDesigPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 22),
    _BdgPortDesigPort_Type()
)
bdgPortDesigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDesigPort.setStatus("mandatory")


class _BdgPortTopChgAck_Type(Integer32):
    """Custom type bdgPortTopChgAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noTopologyChangeIsOccurring", 0),
          ("topologyChangeIsOccurring", 1))
    )


_BdgPortTopChgAck_Type.__name__ = "Integer32"
_BdgPortTopChgAck_Object = MibScalar
bdgPortTopChgAck = _BdgPortTopChgAck_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 23),
    _BdgPortTopChgAck_Type()
)
bdgPortTopChgAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortTopChgAck.setStatus("mandatory")
_BdgPortDesigRoot_Type = OctetString
_BdgPortDesigRoot_Object = MibScalar
bdgPortDesigRoot = _BdgPortDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 24),
    _BdgPortDesigRoot_Type()
)
bdgPortDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortDesigRoot.setStatus("mandatory")
_BdgPortRuntPackets_Type = Counter32
_BdgPortRuntPackets_Object = MibScalar
bdgPortRuntPackets = _BdgPortRuntPackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 25),
    _BdgPortRuntPackets_Type()
)
bdgPortRuntPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortRuntPackets.setStatus("mandatory")
_BdgPortOversizePackets_Type = Counter32
_BdgPortOversizePackets_Object = MibScalar
bdgPortOversizePackets = _BdgPortOversizePackets_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 26),
    _BdgPortOversizePackets_Type()
)
bdgPortOversizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortOversizePackets.setStatus("mandatory")
_BdgPortFrFilt_Type = Counter32
_BdgPortFrFilt_Object = MibScalar
bdgPortFrFilt = _BdgPortFrFilt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 2, 27),
    _BdgPortFrFilt_Type()
)
bdgPortFrFilt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdgPortFrFilt.setStatus("mandatory")
_FilterDB_ObjectIdentity = ObjectIdentity
filterDB = _FilterDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3)
)
_AcqDB_ObjectIdentity = ObjectIdentity
acqDB = _AcqDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1)
)
_AcqStats_ObjectIdentity = ObjectIdentity
acqStats = _AcqStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1)
)
_AcqTotalEntries_Type = Integer32
_AcqTotalEntries_Object = MibScalar
acqTotalEntries = _AcqTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 1),
    _AcqTotalEntries_Type()
)
acqTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqTotalEntries.setStatus("mandatory")
_AcqMaxEntries_Type = Integer32
_AcqMaxEntries_Object = MibScalar
acqMaxEntries = _AcqMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 2),
    _AcqMaxEntries_Type()
)
acqMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqMaxEntries.setStatus("mandatory")
_AcqStaticEntries_Type = Integer32
_AcqStaticEntries_Object = MibScalar
acqStaticEntries = _AcqStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 3),
    _AcqStaticEntries_Type()
)
acqStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqStaticEntries.setStatus("mandatory")
_AcqStaticAgeTime_Type = Integer32
_AcqStaticAgeTime_Object = MibScalar
acqStaticAgeTime = _AcqStaticAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 4),
    _AcqStaticAgeTime_Type()
)
acqStaticAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqStaticAgeTime.setStatus("mandatory")
_AcqDynEntries_Type = Integer32
_AcqDynEntries_Object = MibScalar
acqDynEntries = _AcqDynEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 5),
    _AcqDynEntries_Type()
)
acqDynEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqDynEntries.setStatus("mandatory")
_AcqDynAgeTime_Type = Integer32
_AcqDynAgeTime_Object = MibScalar
acqDynAgeTime = _AcqDynAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 6),
    _AcqDynAgeTime_Type()
)
acqDynAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqDynAgeTime.setStatus("mandatory")


class _AcqEraseDatabase_Type(Integer32):
    """Custom type acqEraseDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("eraseAcquiredDatabase", 0)
    )


_AcqEraseDatabase_Type.__name__ = "Integer32"
_AcqEraseDatabase_Object = MibScalar
acqEraseDatabase = _AcqEraseDatabase_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 1, 7),
    _AcqEraseDatabase_Type()
)
acqEraseDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqEraseDatabase.setStatus("mandatory")
_AcqOptions_ObjectIdentity = ObjectIdentity
acqOptions = _AcqOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2)
)


class _AcqCreate00_Type(Integer32):
    """Custom type acqCreate00 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createAcquiredEntryFilterPort1FilterPort2", 0)
    )


_AcqCreate00_Type.__name__ = "Integer32"
_AcqCreate00_Object = MibScalar
acqCreate00 = _AcqCreate00_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 1),
    _AcqCreate00_Type()
)
acqCreate00.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqCreate00.setStatus("mandatory")


class _AcqCreate20_Type(Integer32):
    """Custom type acqCreate20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createAcquiredEntryForwardPort1FilterPort2", 0)
    )


_AcqCreate20_Type.__name__ = "Integer32"
_AcqCreate20_Object = MibScalar
acqCreate20 = _AcqCreate20_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 2),
    _AcqCreate20_Type()
)
acqCreate20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqCreate20.setStatus("mandatory")


class _AcqCreate01_Type(Integer32):
    """Custom type acqCreate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createAcquiredEntryFilterPort1ForwardPort2", 0)
    )


_AcqCreate01_Type.__name__ = "Integer32"
_AcqCreate01_Object = MibScalar
acqCreate01 = _AcqCreate01_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 3),
    _AcqCreate01_Type()
)
acqCreate01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqCreate01.setStatus("mandatory")


class _AcqCreate21_Type(Integer32):
    """Custom type acqCreate21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createAcquiredEntryForwardPort1ForwardPort2", 0)
    )


_AcqCreate21_Type.__name__ = "Integer32"
_AcqCreate21_Object = MibScalar
acqCreate21 = _AcqCreate21_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 4),
    _AcqCreate21_Type()
)
acqCreate21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqCreate21.setStatus("mandatory")


class _AcqDelete_Type(Integer32):
    """Custom type acqDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("deleteAcquiredEntry", 0)
    )


_AcqDelete_Type.__name__ = "Integer32"
_AcqDelete_Object = MibScalar
acqDelete = _AcqDelete_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 5),
    _AcqDelete_Type()
)
acqDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acqDelete.setStatus("mandatory")
_AcqDispType_Type = OctetString
_AcqDispType_Object = MibScalar
acqDispType = _AcqDispType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 6),
    _AcqDispType_Type()
)
acqDispType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqDispType.setStatus("mandatory")


class _AcqDispOutp1_Type(Integer32):
    """Custom type acqDispOutp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 2))
    )


_AcqDispOutp1_Type.__name__ = "Integer32"
_AcqDispOutp1_Object = MibScalar
acqDispOutp1 = _AcqDispOutp1_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 7),
    _AcqDispOutp1_Type()
)
acqDispOutp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqDispOutp1.setStatus("mandatory")


class _AcqDispOutp2_Type(Integer32):
    """Custom type acqDispOutp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 1))
    )


_AcqDispOutp2_Type.__name__ = "Integer32"
_AcqDispOutp2_Object = MibScalar
acqDispOutp2 = _AcqDispOutp2_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 8),
    _AcqDispOutp2_Type()
)
acqDispOutp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqDispOutp2.setStatus("mandatory")
_AcqSrcAddress_Type = OctetString
_AcqSrcAddress_Object = MibScalar
acqSrcAddress = _AcqSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 1, 2, 9),
    _AcqSrcAddress_Type()
)
acqSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acqSrcAddress.setStatus("mandatory")
_PermDB_ObjectIdentity = ObjectIdentity
permDB = _PermDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2)
)
_PermStats_ObjectIdentity = ObjectIdentity
permStats = _PermStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1)
)
_PermMaxEntries_Type = Integer32
_PermMaxEntries_Object = MibScalar
permMaxEntries = _PermMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1, 1),
    _PermMaxEntries_Type()
)
permMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permMaxEntries.setStatus("mandatory")
_PermCurrEntries_Type = Integer32
_PermCurrEntries_Object = MibScalar
permCurrEntries = _PermCurrEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1, 2),
    _PermCurrEntries_Type()
)
permCurrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permCurrEntries.setStatus("mandatory")


class _PermEraseDatabase_Type(Integer32):
    """Custom type permEraseDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("erasePermanentDatabase", 0)
    )


_PermEraseDatabase_Type.__name__ = "Integer32"
_PermEraseDatabase_Object = MibScalar
permEraseDatabase = _PermEraseDatabase_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 1, 3),
    _PermEraseDatabase_Type()
)
permEraseDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permEraseDatabase.setStatus("mandatory")
_PermOptions_ObjectIdentity = ObjectIdentity
permOptions = _PermOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2)
)


class _PermCreate00_Type(Integer32):
    """Custom type permCreate00 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createPermanentEntryFilterPort1FilterPort2", 0)
    )


_PermCreate00_Type.__name__ = "Integer32"
_PermCreate00_Object = MibScalar
permCreate00 = _PermCreate00_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 1),
    _PermCreate00_Type()
)
permCreate00.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permCreate00.setStatus("mandatory")


class _PermCreate20_Type(Integer32):
    """Custom type permCreate20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createPermanentEntryForwardPort1FilterPort2", 0)
    )


_PermCreate20_Type.__name__ = "Integer32"
_PermCreate20_Object = MibScalar
permCreate20 = _PermCreate20_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 2),
    _PermCreate20_Type()
)
permCreate20.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permCreate20.setStatus("mandatory")


class _PermCreate01_Type(Integer32):
    """Custom type permCreate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createPermanentEntryFilterPort1ForwardPort2", 0)
    )


_PermCreate01_Type.__name__ = "Integer32"
_PermCreate01_Object = MibScalar
permCreate01 = _PermCreate01_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 3),
    _PermCreate01_Type()
)
permCreate01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permCreate01.setStatus("mandatory")


class _PermCreate21_Type(Integer32):
    """Custom type permCreate21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("createPermanentEntryForwardPort1ForwardPort2", 0)
    )


_PermCreate21_Type.__name__ = "Integer32"
_PermCreate21_Object = MibScalar
permCreate21 = _PermCreate21_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 4),
    _PermCreate21_Type()
)
permCreate21.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permCreate21.setStatus("mandatory")


class _PermDelete_Type(Integer32):
    """Custom type permDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("deletePermanentEntry", 0)
    )


_PermDelete_Type.__name__ = "Integer32"
_PermDelete_Object = MibScalar
permDelete = _PermDelete_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 5),
    _PermDelete_Type()
)
permDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    permDelete.setStatus("mandatory")
_PermDispType_Type = OctetString
_PermDispType_Object = MibScalar
permDispType = _PermDispType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 6),
    _PermDispType_Type()
)
permDispType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permDispType.setStatus("mandatory")


class _PermDispOutp1_Type(Integer32):
    """Custom type permDispOutp1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 2))
    )


_PermDispOutp1_Type.__name__ = "Integer32"
_PermDispOutp1_Object = MibScalar
permDispOutp1 = _PermDispOutp1_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 7),
    _PermDispOutp1_Type()
)
permDispOutp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permDispOutp1.setStatus("mandatory")


class _PermDispOutp2_Type(Integer32):
    """Custom type permDispOutp2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 1))
    )


_PermDispOutp2_Type.__name__ = "Integer32"
_PermDispOutp2_Object = MibScalar
permDispOutp2 = _PermDispOutp2_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 8),
    _PermDispOutp2_Type()
)
permDispOutp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permDispOutp2.setStatus("mandatory")
_PermSrcAddress_Type = OctetString
_PermSrcAddress_Object = MibScalar
permSrcAddress = _PermSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 2, 2, 9),
    _PermSrcAddress_Type()
)
permSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    permSrcAddress.setStatus("mandatory")
_SpecialDB_ObjectIdentity = ObjectIdentity
specialDB = _SpecialDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3)
)
_SpecStats_ObjectIdentity = ObjectIdentity
specStats = _SpecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1)
)
_SpecNumEntries_Type = Integer32
_SpecNumEntries_Object = MibScalar
specNumEntries = _SpecNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1, 1),
    _SpecNumEntries_Type()
)
specNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specNumEntries.setStatus("mandatory")
_SpecMaxEntries_Type = Integer32
_SpecMaxEntries_Object = MibScalar
specMaxEntries = _SpecMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1, 2),
    _SpecMaxEntries_Type()
)
specMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specMaxEntries.setStatus("mandatory")
_SpecNextFilterNum_Type = Integer32
_SpecNextFilterNum_Object = MibScalar
specNextFilterNum = _SpecNextFilterNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 1, 3),
    _SpecNextFilterNum_Type()
)
specNextFilterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    specNextFilterNum.setStatus("mandatory")
_SpecFilters_ObjectIdentity = ObjectIdentity
specFilters = _SpecFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2)
)


class _SpecEnable_Type(Integer32):
    """Custom type specEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disableFilter", 0),
          ("enableFilter", 1))
    )


_SpecEnable_Type.__name__ = "Integer32"
_SpecEnable_Object = MibScalar
specEnable = _SpecEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 1),
    _SpecEnable_Type()
)
specEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specEnable.setStatus("mandatory")


class _SpecPort1_Type(Integer32):
    """Custom type specPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 2))
    )


_SpecPort1_Type.__name__ = "Integer32"
_SpecPort1_Object = MibScalar
specPort1 = _SpecPort1_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 2),
    _SpecPort1_Type()
)
specPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specPort1.setStatus("mandatory")


class _SpecPort2_Type(Integer32):
    """Custom type specPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("filter", 0),
          ("relay", 1))
    )


_SpecPort2_Type.__name__ = "Integer32"
_SpecPort2_Object = MibScalar
specPort2 = _SpecPort2_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 3),
    _SpecPort2_Type()
)
specPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specPort2.setStatus("mandatory")
_SpecDestAddress_Type = OctetString
_SpecDestAddress_Object = MibScalar
specDestAddress = _SpecDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 4),
    _SpecDestAddress_Type()
)
specDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specDestAddress.setStatus("mandatory")
_SpecSrcAddress_Type = OctetString
_SpecSrcAddress_Object = MibScalar
specSrcAddress = _SpecSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 5),
    _SpecSrcAddress_Type()
)
specSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specSrcAddress.setStatus("mandatory")
_SpecType_Type = OctetString
_SpecType_Object = MibScalar
specType = _SpecType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 6),
    _SpecType_Type()
)
specType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specType.setStatus("mandatory")
_SpecDataField_Type = OctetString
_SpecDataField_Object = MibScalar
specDataField = _SpecDataField_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 7),
    _SpecDataField_Type()
)
specDataField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specDataField.setStatus("mandatory")


class _SpecDeleteFilter_Type(Integer32):
    """Custom type specDeleteFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("deleteFilter", 0)
    )


_SpecDeleteFilter_Type.__name__ = "Integer32"
_SpecDeleteFilter_Object = MibScalar
specDeleteFilter = _SpecDeleteFilter_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 3, 3, 2, 8),
    _SpecDeleteFilter_Type()
)
specDeleteFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    specDeleteFilter.setStatus("mandatory")
_TrapTypes_ObjectIdentity = ObjectIdentity
trapTypes = _TrapTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 4)
)
_BdgTables_ObjectIdentity = ObjectIdentity
bdgTables = _BdgTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 3, 1, 5)
)
_Lmcommon_ObjectIdentity = ObjectIdentity
lmcommon = _Lmcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2, 1)
)
_MAC_ObjectIdentity = ObjectIdentity
mAC = _MAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2, 2)
)
_Ieee8023_ObjectIdentity = ObjectIdentity
ieee8023 = _Ieee8023_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1)
)
_PcIF_ObjectIdentity = ObjectIdentity
pcIF = _PcIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1)
)
_PcIfRev_ObjectIdentity = ObjectIdentity
pcIfRev = _PcIfRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1)
)
_PcDeviceName_Type = OctetString
_PcDeviceName_Object = MibScalar
pcDeviceName = _PcDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 1),
    _PcDeviceName_Type()
)
pcDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcDeviceName.setStatus("mandatory")
_PcBoardType_Type = ObjectIdentifier
_PcBoardType_Object = MibScalar
pcBoardType = _PcBoardType_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 2),
    _PcBoardType_Type()
)
pcBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcBoardType.setStatus("mandatory")
_PcOwnerName_Type = OctetString
_PcOwnerName_Object = MibScalar
pcOwnerName = _PcOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 3),
    _PcOwnerName_Type()
)
pcOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcOwnerName.setStatus("mandatory")
_PcLocation_Type = OctetString
_PcLocation_Object = MibScalar
pcLocation = _PcLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 4),
    _PcLocation_Type()
)
pcLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcLocation.setStatus("mandatory")
_PcMMACAddr_Type = OctetString
_PcMMACAddr_Object = MibScalar
pcMMACAddr = _PcMMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 5),
    _PcMMACAddr_Type()
)
pcMMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMMACAddr.setStatus("mandatory")
_PcMMACBoard_Type = OctetString
_PcMMACBoard_Object = MibScalar
pcMMACBoard = _PcMMACBoard_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 6),
    _PcMMACBoard_Type()
)
pcMMACBoard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMMACBoard.setStatus("mandatory")
_PcMMACPort_Type = OctetString
_PcMMACPort_Object = MibScalar
pcMMACPort = _PcMMACPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 7),
    _PcMMACPort_Type()
)
pcMMACPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMMACPort.setStatus("mandatory")
_PcApplication_Type = OctetString
_PcApplication_Object = MibScalar
pcApplication = _PcApplication_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 8),
    _PcApplication_Type()
)
pcApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcApplication.setStatus("mandatory")
_PcDriverRev_Type = OctetString
_PcDriverRev_Object = MibScalar
pcDriverRev = _PcDriverRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 9),
    _PcDriverRev_Type()
)
pcDriverRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcDriverRev.setStatus("mandatory")
_PcOnboardMemory_Type = Integer32
_PcOnboardMemory_Object = MibScalar
pcOnboardMemory = _PcOnboardMemory_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 10),
    _PcOnboardMemory_Type()
)
pcOnboardMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcOnboardMemory.setStatus("mandatory")
_PcComment_Type = OctetString
_PcComment_Object = MibScalar
pcComment = _PcComment_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 11),
    _PcComment_Type()
)
pcComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcComment.setStatus("mandatory")
_PcMACAddr_Type = OctetString
_PcMACAddr_Object = MibScalar
pcMACAddr = _PcMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 12),
    _PcMACAddr_Type()
)
pcMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMACAddr.setStatus("mandatory")
_PcFramesXmit_Type = Integer32
_PcFramesXmit_Object = MibScalar
pcFramesXmit = _PcFramesXmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 13),
    _PcFramesXmit_Type()
)
pcFramesXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcFramesXmit.setStatus("mandatory")
_PcBytesXmit_Type = Integer32
_PcBytesXmit_Object = MibScalar
pcBytesXmit = _PcBytesXmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 14),
    _PcBytesXmit_Type()
)
pcBytesXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcBytesXmit.setStatus("mandatory")
_PcMcastXmit_Type = Integer32
_PcMcastXmit_Object = MibScalar
pcMcastXmit = _PcMcastXmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 15),
    _PcMcastXmit_Type()
)
pcMcastXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMcastXmit.setStatus("mandatory")
_PcBcastXmit_Type = Integer32
_PcBcastXmit_Object = MibScalar
pcBcastXmit = _PcBcastXmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 16),
    _PcBcastXmit_Type()
)
pcBcastXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcBcastXmit.setStatus("mandatory")
_PcDeferXmit_Type = Integer32
_PcDeferXmit_Object = MibScalar
pcDeferXmit = _PcDeferXmit_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 17),
    _PcDeferXmit_Type()
)
pcDeferXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcDeferXmit.setStatus("mandatory")
_PcSglColl_Type = Integer32
_PcSglColl_Object = MibScalar
pcSglColl = _PcSglColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 18),
    _PcSglColl_Type()
)
pcSglColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcSglColl.setStatus("mandatory")
_PcMultiColl_Type = Integer32
_PcMultiColl_Object = MibScalar
pcMultiColl = _PcMultiColl_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 19),
    _PcMultiColl_Type()
)
pcMultiColl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMultiColl.setStatus("mandatory")
_PcTotXmitErrs_Type = Integer32
_PcTotXmitErrs_Object = MibScalar
pcTotXmitErrs = _PcTotXmitErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 20),
    _PcTotXmitErrs_Type()
)
pcTotXmitErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcTotXmitErrs.setStatus("mandatory")
_PcLateColls_Type = Integer32
_PcLateColls_Object = MibScalar
pcLateColls = _PcLateColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 21),
    _PcLateColls_Type()
)
pcLateColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcLateColls.setStatus("mandatory")
_PcXcessColls_Type = Integer32
_PcXcessColls_Object = MibScalar
pcXcessColls = _PcXcessColls_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 22),
    _PcXcessColls_Type()
)
pcXcessColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcXcessColls.setStatus("mandatory")
_PcCarrErr_Type = Integer32
_PcCarrErr_Object = MibScalar
pcCarrErr = _PcCarrErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 23),
    _PcCarrErr_Type()
)
pcCarrErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCarrErr.setStatus("mandatory")
_PcFramesRec_Type = Integer32
_PcFramesRec_Object = MibScalar
pcFramesRec = _PcFramesRec_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 24),
    _PcFramesRec_Type()
)
pcFramesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcFramesRec.setStatus("mandatory")
_PcBytesRec_Type = Integer32
_PcBytesRec_Object = MibScalar
pcBytesRec = _PcBytesRec_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 25),
    _PcBytesRec_Type()
)
pcBytesRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcBytesRec.setStatus("mandatory")
_PcMcastRec_Type = Integer32
_PcMcastRec_Object = MibScalar
pcMcastRec = _PcMcastRec_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 26),
    _PcMcastRec_Type()
)
pcMcastRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcMcastRec.setStatus("mandatory")
_PcBcastRec_Type = Integer32
_PcBcastRec_Object = MibScalar
pcBcastRec = _PcBcastRec_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 27),
    _PcBcastRec_Type()
)
pcBcastRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcBcastRec.setStatus("mandatory")
_PcTotRecErrs_Type = Integer32
_PcTotRecErrs_Object = MibScalar
pcTotRecErrs = _PcTotRecErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 28),
    _PcTotRecErrs_Type()
)
pcTotRecErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcTotRecErrs.setStatus("mandatory")
_PcTooLong_Type = Integer32
_PcTooLong_Object = MibScalar
pcTooLong = _PcTooLong_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 29),
    _PcTooLong_Type()
)
pcTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcTooLong.setStatus("mandatory")
_PcTooShort_Type = Integer32
_PcTooShort_Object = MibScalar
pcTooShort = _PcTooShort_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 30),
    _PcTooShort_Type()
)
pcTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcTooShort.setStatus("mandatory")
_PcAlignErrs_Type = Integer32
_PcAlignErrs_Object = MibScalar
pcAlignErrs = _PcAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 31),
    _PcAlignErrs_Type()
)
pcAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcAlignErrs.setStatus("mandatory")
_PcCRCErrs_Type = Integer32
_PcCRCErrs_Object = MibScalar
pcCRCErrs = _PcCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 32),
    _PcCRCErrs_Type()
)
pcCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcCRCErrs.setStatus("mandatory")
_PcLenErrs_Type = Integer32
_PcLenErrs_Object = MibScalar
pcLenErrs = _PcLenErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 33),
    _PcLenErrs_Type()
)
pcLenErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcLenErrs.setStatus("mandatory")
_PcIntRecErr_Type = Integer32
_PcIntRecErr_Object = MibScalar
pcIntRecErr = _PcIntRecErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 34),
    _PcIntRecErr_Type()
)
pcIntRecErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcIntRecErr.setStatus("mandatory")
_PcSqeErr_Type = Integer32
_PcSqeErr_Object = MibScalar
pcSqeErr = _PcSqeErr_Object(
    (1, 3, 6, 1, 4, 1, 52, 2, 2, 1, 1, 1, 35),
    _PcSqeErr_Type()
)
pcSqeErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pcSqeErr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-BDG-MIB",
    **{"bridgeRev1": bridgeRev1,
       "bdgdevice": bdgdevice,
       "bdgdeviceDisableBdg": bdgdeviceDisableBdg,
       "bdgdeviceRestoreSettings": bdgdeviceRestoreSettings,
       "bdgdeviceBdgName": bdgdeviceBdgName,
       "bdgdeviceNumPorts": bdgdeviceNumPorts,
       "bdgdeviceType": bdgdeviceType,
       "bdgdeviceVersion": bdgdeviceVersion,
       "bdgdeviceLocation": bdgdeviceLocation,
       "bdgdeviceStatus": bdgdeviceStatus,
       "bdgdeviceRestartBdg": bdgdeviceRestartBdg,
       "bdgdeviceFrFwd": bdgdeviceFrFwd,
       "bdgdeviceFrRx": bdgdeviceFrRx,
       "bdgdeviceFrFlt": bdgdeviceFrFlt,
       "bdgdeviceErr": bdgdeviceErr,
       "bdgdeviceSwitchSetting": bdgdeviceSwitchSetting,
       "bdgdeviceNumRestarts": bdgdeviceNumRestarts,
       "bdgdeviceTypeFiltering": bdgdeviceTypeFiltering,
       "bdgdeviceSTAProtocol": bdgdeviceSTAProtocol,
       "bdgdeviceBridgeID": bdgdeviceBridgeID,
       "bdgdeviceTopChgCnt": bdgdeviceTopChgCnt,
       "bdgdeviceRootCost": bdgdeviceRootCost,
       "bdgdeviceRootPort": bdgdeviceRootPort,
       "bdgdeviceHelloTime": bdgdeviceHelloTime,
       "bdgdeviceBdgMaxAge": bdgdeviceBdgMaxAge,
       "bdgdeviceBdgFwdDly": bdgdeviceBdgFwdDly,
       "bdgdeviceTimeTopChg": bdgdeviceTimeTopChg,
       "bdgdeviceTopChg": bdgdeviceTopChg,
       "bdgdeviceDesigRoot": bdgdeviceDesigRoot,
       "bdgdeviceMaxAge": bdgdeviceMaxAge,
       "bdgdeviceHoldTime": bdgdeviceHoldTime,
       "bdgdeviceFwdDly": bdgdeviceFwdDly,
       "bdgdeviceBdgHello": bdgdeviceBdgHello,
       "bdgdeviceBdgPriority": bdgdeviceBdgPriority,
       "bdgdeviceResetCounts": bdgdeviceResetCounts,
       "bdgdeviceUptime": bdgdeviceUptime,
       "bdgdeviceTrapType": bdgdeviceTrapType,
       "bdgPort": bdgPort,
       "bdgPortAddress": bdgPortAddress,
       "bdgPortName": bdgPortName,
       "bdgPortType": bdgPortType,
       "bdgPortStatus": bdgPortStatus,
       "bdgPortNetName": bdgPortNetName,
       "bdgPortFrRx": bdgPortFrRx,
       "bdgPortDisInb": bdgPortDisInb,
       "bdgPortFwdOutb": bdgPortFwdOutb,
       "bdgPortDisLOB": bdgPortDisLOB,
       "bdgPortDisTDE": bdgPortDisTDE,
       "bdgPortDisErr": bdgPortDisErr,
       "bdgPortColl": bdgPortColl,
       "bdgPortTxAbrt": bdgPortTxAbrt,
       "bdgPortOowColl": bdgPortOowColl,
       "bdgPortCRCErr": bdgPortCRCErr,
       "bdgPortFrAlErr": bdgPortFrAlErr,
       "bdgPortPriority": bdgPortPriority,
       "bdgPortState": bdgPortState,
       "bdgPortPathCost": bdgPortPathCost,
       "bdgPortDesigCost": bdgPortDesigCost,
       "bdgPortDesigBrdg": bdgPortDesigBrdg,
       "bdgPortDesigPort": bdgPortDesigPort,
       "bdgPortTopChgAck": bdgPortTopChgAck,
       "bdgPortDesigRoot": bdgPortDesigRoot,
       "bdgPortRuntPackets": bdgPortRuntPackets,
       "bdgPortOversizePackets": bdgPortOversizePackets,
       "bdgPortFrFilt": bdgPortFrFilt,
       "filterDB": filterDB,
       "acqDB": acqDB,
       "acqStats": acqStats,
       "acqTotalEntries": acqTotalEntries,
       "acqMaxEntries": acqMaxEntries,
       "acqStaticEntries": acqStaticEntries,
       "acqStaticAgeTime": acqStaticAgeTime,
       "acqDynEntries": acqDynEntries,
       "acqDynAgeTime": acqDynAgeTime,
       "acqEraseDatabase": acqEraseDatabase,
       "acqOptions": acqOptions,
       "acqCreate00": acqCreate00,
       "acqCreate20": acqCreate20,
       "acqCreate01": acqCreate01,
       "acqCreate21": acqCreate21,
       "acqDelete": acqDelete,
       "acqDispType": acqDispType,
       "acqDispOutp1": acqDispOutp1,
       "acqDispOutp2": acqDispOutp2,
       "acqSrcAddress": acqSrcAddress,
       "permDB": permDB,
       "permStats": permStats,
       "permMaxEntries": permMaxEntries,
       "permCurrEntries": permCurrEntries,
       "permEraseDatabase": permEraseDatabase,
       "permOptions": permOptions,
       "permCreate00": permCreate00,
       "permCreate20": permCreate20,
       "permCreate01": permCreate01,
       "permCreate21": permCreate21,
       "permDelete": permDelete,
       "permDispType": permDispType,
       "permDispOutp1": permDispOutp1,
       "permDispOutp2": permDispOutp2,
       "permSrcAddress": permSrcAddress,
       "specialDB": specialDB,
       "specStats": specStats,
       "specNumEntries": specNumEntries,
       "specMaxEntries": specMaxEntries,
       "specNextFilterNum": specNextFilterNum,
       "specFilters": specFilters,
       "specEnable": specEnable,
       "specPort1": specPort1,
       "specPort2": specPort2,
       "specDestAddress": specDestAddress,
       "specSrcAddress": specSrcAddress,
       "specType": specType,
       "specDataField": specDataField,
       "specDeleteFilter": specDeleteFilter,
       "trapTypes": trapTypes,
       "bdgTables": bdgTables,
       "lmcommon": lmcommon,
       "mAC": mAC,
       "ieee8023": ieee8023,
       "pcIF": pcIF,
       "pcIfRev": pcIfRev,
       "pcDeviceName": pcDeviceName,
       "pcBoardType": pcBoardType,
       "pcOwnerName": pcOwnerName,
       "pcLocation": pcLocation,
       "pcMMACAddr": pcMMACAddr,
       "pcMMACBoard": pcMMACBoard,
       "pcMMACPort": pcMMACPort,
       "pcApplication": pcApplication,
       "pcDriverRev": pcDriverRev,
       "pcOnboardMemory": pcOnboardMemory,
       "pcComment": pcComment,
       "pcMACAddr": pcMACAddr,
       "pcFramesXmit": pcFramesXmit,
       "pcBytesXmit": pcBytesXmit,
       "pcMcastXmit": pcMcastXmit,
       "pcBcastXmit": pcBcastXmit,
       "pcDeferXmit": pcDeferXmit,
       "pcSglColl": pcSglColl,
       "pcMultiColl": pcMultiColl,
       "pcTotXmitErrs": pcTotXmitErrs,
       "pcLateColls": pcLateColls,
       "pcXcessColls": pcXcessColls,
       "pcCarrErr": pcCarrErr,
       "pcFramesRec": pcFramesRec,
       "pcBytesRec": pcBytesRec,
       "pcMcastRec": pcMcastRec,
       "pcBcastRec": pcBcastRec,
       "pcTotRecErrs": pcTotRecErrs,
       "pcTooLong": pcTooLong,
       "pcTooShort": pcTooShort,
       "pcAlignErrs": pcAlignErrs,
       "pcCRCErrs": pcCRCErrs,
       "pcLenErrs": pcLenErrs,
       "pcIntRecErr": pcIntRecErr,
       "pcSqeErr": pcSqeErr}
)
