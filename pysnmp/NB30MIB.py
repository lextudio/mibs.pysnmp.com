# SNMP MIB module (NB30MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NB30MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:42 2024
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

(nb30Rev1,) = mibBuilder.importSymbols(
    "IRM-OIDS",
    "nb30Rev1")

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

_Nb30Device_ObjectIdentity = ObjectIdentity
nb30Device = _Nb30Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1)
)


class _Nb30DeviceDisableBdg_Type(Integer32):
    """Custom type nb30DeviceDisableBdg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableBridge", 2),
          ("enableBridge", 1))
    )


_Nb30DeviceDisableBdg_Type.__name__ = "Integer32"
_Nb30DeviceDisableBdg_Object = MibScalar
nb30DeviceDisableBdg = _Nb30DeviceDisableBdg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 1),
    _Nb30DeviceDisableBdg_Type()
)
nb30DeviceDisableBdg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceDisableBdg.setStatus("mandatory")


class _Nb30DeviceRestoreSettings_Type(Integer32):
    """Custom type nb30DeviceRestoreSettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restoreSettings", 1)
    )


_Nb30DeviceRestoreSettings_Type.__name__ = "Integer32"
_Nb30DeviceRestoreSettings_Object = MibScalar
nb30DeviceRestoreSettings = _Nb30DeviceRestoreSettings_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 2),
    _Nb30DeviceRestoreSettings_Type()
)
nb30DeviceRestoreSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceRestoreSettings.setStatus("mandatory")
_Nb30DeviceBdgName_Type = OctetString
_Nb30DeviceBdgName_Object = MibScalar
nb30DeviceBdgName = _Nb30DeviceBdgName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 3),
    _Nb30DeviceBdgName_Type()
)
nb30DeviceBdgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceBdgName.setStatus("mandatory")
_Nb30DeviceNumPorts_Type = Integer32
_Nb30DeviceNumPorts_Object = MibScalar
nb30DeviceNumPorts = _Nb30DeviceNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 4),
    _Nb30DeviceNumPorts_Type()
)
nb30DeviceNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceNumPorts.setStatus("mandatory")
_Nb30DeviceType_Type = OctetString
_Nb30DeviceType_Object = MibScalar
nb30DeviceType = _Nb30DeviceType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 5),
    _Nb30DeviceType_Type()
)
nb30DeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceType.setStatus("mandatory")
_Nb30DeviceVersion_Type = OctetString
_Nb30DeviceVersion_Object = MibScalar
nb30DeviceVersion = _Nb30DeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 6),
    _Nb30DeviceVersion_Type()
)
nb30DeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceVersion.setStatus("mandatory")
_Nb30DeviceLocation_Type = OctetString
_Nb30DeviceLocation_Object = MibScalar
nb30DeviceLocation = _Nb30DeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 7),
    _Nb30DeviceLocation_Type()
)
nb30DeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceLocation.setStatus("mandatory")
_Nb30DeviceStatus_Type = OctetString
_Nb30DeviceStatus_Object = MibScalar
nb30DeviceStatus = _Nb30DeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 8),
    _Nb30DeviceStatus_Type()
)
nb30DeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceStatus.setStatus("mandatory")


class _Nb30DeviceRestartBdg_Type(Integer32):
    """Custom type nb30DeviceRestartBdg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restartBridge", 1)
    )


_Nb30DeviceRestartBdg_Type.__name__ = "Integer32"
_Nb30DeviceRestartBdg_Object = MibScalar
nb30DeviceRestartBdg = _Nb30DeviceRestartBdg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 9),
    _Nb30DeviceRestartBdg_Type()
)
nb30DeviceRestartBdg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceRestartBdg.setStatus("mandatory")
_Nb30DeviceFrFwds_Type = Counter32
_Nb30DeviceFrFwds_Object = MibScalar
nb30DeviceFrFwds = _Nb30DeviceFrFwds_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 10),
    _Nb30DeviceFrFwds_Type()
)
nb30DeviceFrFwds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceFrFwds.setStatus("mandatory")
_Nb30DeviceFrRxs_Type = Counter32
_Nb30DeviceFrRxs_Object = MibScalar
nb30DeviceFrRxs = _Nb30DeviceFrRxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 11),
    _Nb30DeviceFrRxs_Type()
)
nb30DeviceFrRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceFrRxs.setStatus("mandatory")
_Nb30DeviceFrFlts_Type = Counter32
_Nb30DeviceFrFlts_Object = MibScalar
nb30DeviceFrFlts = _Nb30DeviceFrFlts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 12),
    _Nb30DeviceFrFlts_Type()
)
nb30DeviceFrFlts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceFrFlts.setStatus("mandatory")
_Nb30DeviceErrs_Type = Counter32
_Nb30DeviceErrs_Object = MibScalar
nb30DeviceErrs = _Nb30DeviceErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 13),
    _Nb30DeviceErrs_Type()
)
nb30DeviceErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceErrs.setStatus("mandatory")
_Nb30DeviceNumRestarts_Type = Counter32
_Nb30DeviceNumRestarts_Object = MibScalar
nb30DeviceNumRestarts = _Nb30DeviceNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 14),
    _Nb30DeviceNumRestarts_Type()
)
nb30DeviceNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceNumRestarts.setStatus("mandatory")


class _Nb30DeviceTypeFiltering_Type(Integer32):
    """Custom type nb30DeviceTypeFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("ieee8021", 1),
          ("specialDB", 2))
    )


_Nb30DeviceTypeFiltering_Type.__name__ = "Integer32"
_Nb30DeviceTypeFiltering_Object = MibScalar
nb30DeviceTypeFiltering = _Nb30DeviceTypeFiltering_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 15),
    _Nb30DeviceTypeFiltering_Type()
)
nb30DeviceTypeFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceTypeFiltering.setStatus("mandatory")


class _Nb30DeviceSTAProtocol_Type(Integer32):
    """Custom type nb30DeviceSTAProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dec", 2),
          ("ieee8021", 1),
          ("none", 3))
    )


_Nb30DeviceSTAProtocol_Type.__name__ = "Integer32"
_Nb30DeviceSTAProtocol_Object = MibScalar
nb30DeviceSTAProtocol = _Nb30DeviceSTAProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 16),
    _Nb30DeviceSTAProtocol_Type()
)
nb30DeviceSTAProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceSTAProtocol.setStatus("mandatory")
_Nb30DeviceBridgeID_Type = OctetString
_Nb30DeviceBridgeID_Object = MibScalar
nb30DeviceBridgeID = _Nb30DeviceBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 17),
    _Nb30DeviceBridgeID_Type()
)
nb30DeviceBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceBridgeID.setStatus("mandatory")
_Nb30DeviceTopChgCnts_Type = Counter32
_Nb30DeviceTopChgCnts_Object = MibScalar
nb30DeviceTopChgCnts = _Nb30DeviceTopChgCnts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 18),
    _Nb30DeviceTopChgCnts_Type()
)
nb30DeviceTopChgCnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceTopChgCnts.setStatus("mandatory")
_Nb30DeviceTimeTopChg_Type = Integer32
_Nb30DeviceTimeTopChg_Object = MibScalar
nb30DeviceTimeTopChg = _Nb30DeviceTimeTopChg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 19),
    _Nb30DeviceTimeTopChg_Type()
)
nb30DeviceTimeTopChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceTimeTopChg.setStatus("mandatory")


class _Nb30DeviceTopChg_Type(Integer32):
    """Custom type nb30DeviceTopChg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTopologyChangeInProgress", 1),
          ("topologyChangeInProgress", 2))
    )


_Nb30DeviceTopChg_Type.__name__ = "Integer32"
_Nb30DeviceTopChg_Object = MibScalar
nb30DeviceTopChg = _Nb30DeviceTopChg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 20),
    _Nb30DeviceTopChg_Type()
)
nb30DeviceTopChg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceTopChg.setStatus("mandatory")
_Nb30DeviceRootCost_Type = Integer32
_Nb30DeviceRootCost_Object = MibScalar
nb30DeviceRootCost = _Nb30DeviceRootCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 21),
    _Nb30DeviceRootCost_Type()
)
nb30DeviceRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceRootCost.setStatus("mandatory")
_Nb30DeviceRootPort_Type = Integer32
_Nb30DeviceRootPort_Object = MibScalar
nb30DeviceRootPort = _Nb30DeviceRootPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 22),
    _Nb30DeviceRootPort_Type()
)
nb30DeviceRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceRootPort.setStatus("mandatory")
_Nb30DeviceDesigRoot_Type = OctetString
_Nb30DeviceDesigRoot_Object = MibScalar
nb30DeviceDesigRoot = _Nb30DeviceDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 23),
    _Nb30DeviceDesigRoot_Type()
)
nb30DeviceDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceDesigRoot.setStatus("mandatory")
_Nb30DeviceMaxAge_Type = Integer32
_Nb30DeviceMaxAge_Object = MibScalar
nb30DeviceMaxAge = _Nb30DeviceMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 24),
    _Nb30DeviceMaxAge_Type()
)
nb30DeviceMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceMaxAge.setStatus("mandatory")
_Nb30DeviceHoldTime_Type = Integer32
_Nb30DeviceHoldTime_Object = MibScalar
nb30DeviceHoldTime = _Nb30DeviceHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 25),
    _Nb30DeviceHoldTime_Type()
)
nb30DeviceHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceHoldTime.setStatus("mandatory")
_Nb30DeviceFwdDly_Type = Integer32
_Nb30DeviceFwdDly_Object = MibScalar
nb30DeviceFwdDly = _Nb30DeviceFwdDly_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 26),
    _Nb30DeviceFwdDly_Type()
)
nb30DeviceFwdDly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceFwdDly.setStatus("mandatory")
_Nb30DeviceHelloTime_Type = Integer32
_Nb30DeviceHelloTime_Object = MibScalar
nb30DeviceHelloTime = _Nb30DeviceHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 27),
    _Nb30DeviceHelloTime_Type()
)
nb30DeviceHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceHelloTime.setStatus("mandatory")
_Nb30DeviceBdgFwdDly_Type = Integer32
_Nb30DeviceBdgFwdDly_Object = MibScalar
nb30DeviceBdgFwdDly = _Nb30DeviceBdgFwdDly_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 28),
    _Nb30DeviceBdgFwdDly_Type()
)
nb30DeviceBdgFwdDly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceBdgFwdDly.setStatus("mandatory")
_Nb30DeviceBdgMaxAge_Type = Integer32
_Nb30DeviceBdgMaxAge_Object = MibScalar
nb30DeviceBdgMaxAge = _Nb30DeviceBdgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 29),
    _Nb30DeviceBdgMaxAge_Type()
)
nb30DeviceBdgMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceBdgMaxAge.setStatus("mandatory")
_Nb30DeviceBdgHello_Type = Integer32
_Nb30DeviceBdgHello_Object = MibScalar
nb30DeviceBdgHello = _Nb30DeviceBdgHello_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 30),
    _Nb30DeviceBdgHello_Type()
)
nb30DeviceBdgHello.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceBdgHello.setStatus("mandatory")
_Nb30DeviceBdgPriority_Type = Integer32
_Nb30DeviceBdgPriority_Object = MibScalar
nb30DeviceBdgPriority = _Nb30DeviceBdgPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 31),
    _Nb30DeviceBdgPriority_Type()
)
nb30DeviceBdgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceBdgPriority.setStatus("mandatory")


class _Nb30DeviceResetCounts_Type(Integer32):
    """Custom type nb30DeviceResetCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetCounts", 1)
    )


_Nb30DeviceResetCounts_Type.__name__ = "Integer32"
_Nb30DeviceResetCounts_Object = MibScalar
nb30DeviceResetCounts = _Nb30DeviceResetCounts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 32),
    _Nb30DeviceResetCounts_Type()
)
nb30DeviceResetCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceResetCounts.setStatus("mandatory")
_Nb30DeviceUptime_Type = Integer32
_Nb30DeviceUptime_Object = MibScalar
nb30DeviceUptime = _Nb30DeviceUptime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 33),
    _Nb30DeviceUptime_Type()
)
nb30DeviceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceUptime.setStatus("mandatory")


class _Nb30DeviceRootSwitch_Type(Integer32):
    """Custom type nb30DeviceRootSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRoot", 1),
          ("root", 2))
    )


_Nb30DeviceRootSwitch_Type.__name__ = "Integer32"
_Nb30DeviceRootSwitch_Object = MibScalar
nb30DeviceRootSwitch = _Nb30DeviceRootSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 34),
    _Nb30DeviceRootSwitch_Type()
)
nb30DeviceRootSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceRootSwitch.setStatus("mandatory")


class _Nb30DeviceFwdBroadcast_Type(Integer32):
    """Custom type nb30DeviceFwdBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filterBroadcast", 2),
          ("forwardBroadcast", 1))
    )


_Nb30DeviceFwdBroadcast_Type.__name__ = "Integer32"
_Nb30DeviceFwdBroadcast_Object = MibScalar
nb30DeviceFwdBroadcast = _Nb30DeviceFwdBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 35),
    _Nb30DeviceFwdBroadcast_Type()
)
nb30DeviceFwdBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceFwdBroadcast.setStatus("mandatory")


class _Nb30DeviceConfigSw1_Type(Integer32):
    """Custom type nb30DeviceConfigSw1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchOff", 1),
          ("switchOn", 2))
    )


_Nb30DeviceConfigSw1_Type.__name__ = "Integer32"
_Nb30DeviceConfigSw1_Object = MibScalar
nb30DeviceConfigSw1 = _Nb30DeviceConfigSw1_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 36),
    _Nb30DeviceConfigSw1_Type()
)
nb30DeviceConfigSw1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceConfigSw1.setStatus("mandatory")


class _Nb30DeviceConfigSw2_Type(Integer32):
    """Custom type nb30DeviceConfigSw2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchOff", 1),
          ("switchOn", 2))
    )


_Nb30DeviceConfigSw2_Type.__name__ = "Integer32"
_Nb30DeviceConfigSw2_Object = MibScalar
nb30DeviceConfigSw2 = _Nb30DeviceConfigSw2_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 37),
    _Nb30DeviceConfigSw2_Type()
)
nb30DeviceConfigSw2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceConfigSw2.setStatus("mandatory")


class _Nb30DeviceConfigSw3_Type(Integer32):
    """Custom type nb30DeviceConfigSw3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchOff", 1),
          ("switchOn", 2))
    )


_Nb30DeviceConfigSw3_Type.__name__ = "Integer32"
_Nb30DeviceConfigSw3_Object = MibScalar
nb30DeviceConfigSw3 = _Nb30DeviceConfigSw3_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 38),
    _Nb30DeviceConfigSw3_Type()
)
nb30DeviceConfigSw3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceConfigSw3.setStatus("mandatory")


class _Nb30DeviceConfigSw4_Type(Integer32):
    """Custom type nb30DeviceConfigSw4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchOff", 1),
          ("switchOn", 2))
    )


_Nb30DeviceConfigSw4_Type.__name__ = "Integer32"
_Nb30DeviceConfigSw4_Object = MibScalar
nb30DeviceConfigSw4 = _Nb30DeviceConfigSw4_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 39),
    _Nb30DeviceConfigSw4_Type()
)
nb30DeviceConfigSw4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DeviceConfigSw4.setStatus("mandatory")
_Nb30DevicePortActive_Type = Integer32
_Nb30DevicePortActive_Object = MibScalar
nb30DevicePortActive = _Nb30DevicePortActive_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 40),
    _Nb30DevicePortActive_Type()
)
nb30DevicePortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DevicePortActive.setStatus("mandatory")


class _Nb30DeviceDefPort_Type(Integer32):
    """Custom type nb30DeviceDefPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernetPort1", 1),
          ("ethernetPort2", 2))
    )


_Nb30DeviceDefPort_Type.__name__ = "Integer32"
_Nb30DeviceDefPort_Object = MibScalar
nb30DeviceDefPort = _Nb30DeviceDefPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 41),
    _Nb30DeviceDefPort_Type()
)
nb30DeviceDefPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceDefPort.setStatus("mandatory")


class _Nb30DeviceRedEnable_Type(Integer32):
    """Custom type nb30DeviceRedEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableRedundancy", 1),
          ("enableRedundancy", 2))
    )


_Nb30DeviceRedEnable_Type.__name__ = "Integer32"
_Nb30DeviceRedEnable_Object = MibScalar
nb30DeviceRedEnable = _Nb30DeviceRedEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 1, 42),
    _Nb30DeviceRedEnable_Type()
)
nb30DeviceRedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DeviceRedEnable.setStatus("mandatory")
_Nb30Dsx_ObjectIdentity = ObjectIdentity
nb30Dsx = _Nb30Dsx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 2)
)


class _Nb30DsxLoopUp_Type(Integer32):
    """Custom type nb30DsxLoopUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("loopUp", 1)
    )


_Nb30DsxLoopUp_Type.__name__ = "Integer32"
_Nb30DsxLoopUp_Object = MibScalar
nb30DsxLoopUp = _Nb30DsxLoopUp_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 2, 1),
    _Nb30DsxLoopUp_Type()
)
nb30DsxLoopUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DsxLoopUp.setStatus("mandatory")


class _Nb30DsxLoopDn_Type(Integer32):
    """Custom type nb30DsxLoopDn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("loopDown", 1)
    )


_Nb30DsxLoopDn_Type.__name__ = "Integer32"
_Nb30DsxLoopDn_Object = MibScalar
nb30DsxLoopDn = _Nb30DsxLoopDn_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 2, 2),
    _Nb30DsxLoopDn_Type()
)
nb30DsxLoopDn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DsxLoopDn.setStatus("mandatory")


class _Nb30DsxLoopSt_Type(Integer32):
    """Custom type nb30DsxLoopSt based on Integer32"""
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
        *(("loopbackFailed", 5),
          ("loopbackInProgress", 2),
          ("loopbackPassed", 4),
          ("networkLoopback", 3),
          ("notInLoopback", 1))
    )


_Nb30DsxLoopSt_Type.__name__ = "Integer32"
_Nb30DsxLoopSt_Object = MibScalar
nb30DsxLoopSt = _Nb30DsxLoopSt_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 2, 3),
    _Nb30DsxLoopSt_Type()
)
nb30DsxLoopSt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30DsxLoopSt.setStatus("mandatory")


class _Nb30DsxLoopPattern_Type(Integer32):
    """Custom type nb30DsxLoopPattern based on Integer32"""
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
        *(("all0s", 3),
          ("all1s", 2),
          ("alternate1sAnd0s", 1),
          ("incrementingData", 4))
    )


_Nb30DsxLoopPattern_Type.__name__ = "Integer32"
_Nb30DsxLoopPattern_Object = MibScalar
nb30DsxLoopPattern = _Nb30DsxLoopPattern_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 2, 4),
    _Nb30DsxLoopPattern_Type()
)
nb30DsxLoopPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DsxLoopPattern.setStatus("mandatory")
_Nb30DsxChannel_ObjectIdentity = ObjectIdentity
nb30DsxChannel = _Nb30DsxChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 3)
)
_Nb30DsxChannelTable_Object = MibTable
nb30DsxChannelTable = _Nb30DsxChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 3, 1)
)
if mibBuilder.loadTexts:
    nb30DsxChannelTable.setStatus("mandatory")
_Nb30DsxEntry_Object = MibTableRow
nb30DsxEntry = _Nb30DsxEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 3, 1, 1)
)
nb30DsxEntry.setIndexNames(
    (0, "NB30MIB", "nb30DsxChannelId"),
)
if mibBuilder.loadTexts:
    nb30DsxEntry.setStatus("mandatory")


class _Nb30DsxChannelControl_Type(Integer32):
    """Custom type nb30DsxChannelControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableChannel", 1),
          ("enableChannel", 2))
    )


_Nb30DsxChannelControl_Type.__name__ = "Integer32"
_Nb30DsxChannelControl_Object = MibTableColumn
nb30DsxChannelControl = _Nb30DsxChannelControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 3, 1, 1, 1),
    _Nb30DsxChannelControl_Type()
)
nb30DsxChannelControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DsxChannelControl.setStatus("mandatory")
_Nb30DsxChannelId_Type = Integer32
_Nb30DsxChannelId_Object = MibTableColumn
nb30DsxChannelId = _Nb30DsxChannelId_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 3, 1, 1, 2),
    _Nb30DsxChannelId_Type()
)
nb30DsxChannelId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30DsxChannelId.setStatus("mandatory")
_Nb30Port_ObjectIdentity = ObjectIdentity
nb30Port = _Nb30Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4)
)
_Nb30PortTable_Object = MibTable
nb30PortTable = _Nb30PortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1)
)
if mibBuilder.loadTexts:
    nb30PortTable.setStatus("mandatory")
_Nb30PortEntry_Object = MibTableRow
nb30PortEntry = _Nb30PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1)
)
nb30PortEntry.setIndexNames(
    (0, "NB30MIB", "nb30PortId"),
)
if mibBuilder.loadTexts:
    nb30PortEntry.setStatus("mandatory")
_Nb30PortAddress_Type = OctetString
_Nb30PortAddress_Object = MibTableColumn
nb30PortAddress = _Nb30PortAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 1),
    _Nb30PortAddress_Type()
)
nb30PortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortAddress.setStatus("mandatory")
_Nb30PortName_Type = OctetString
_Nb30PortName_Object = MibTableColumn
nb30PortName = _Nb30PortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 2),
    _Nb30PortName_Type()
)
nb30PortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30PortName.setStatus("mandatory")
_Nb30PortType_Type = OctetString
_Nb30PortType_Object = MibTableColumn
nb30PortType = _Nb30PortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 3),
    _Nb30PortType_Type()
)
nb30PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortType.setStatus("mandatory")
_Nb30PortStatus_Type = OctetString
_Nb30PortStatus_Object = MibTableColumn
nb30PortStatus = _Nb30PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 4),
    _Nb30PortStatus_Type()
)
nb30PortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortStatus.setStatus("mandatory")
_Nb30PortNetName_Type = OctetString
_Nb30PortNetName_Object = MibTableColumn
nb30PortNetName = _Nb30PortNetName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 5),
    _Nb30PortNetName_Type()
)
nb30PortNetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30PortNetName.setStatus("mandatory")
_Nb30PortFrRxs_Type = Counter32
_Nb30PortFrRxs_Object = MibTableColumn
nb30PortFrRxs = _Nb30PortFrRxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 6),
    _Nb30PortFrRxs_Type()
)
nb30PortFrRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortFrRxs.setStatus("mandatory")
_Nb30PortDisInbounds_Type = Counter32
_Nb30PortDisInbounds_Object = MibTableColumn
nb30PortDisInbounds = _Nb30PortDisInbounds_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 7),
    _Nb30PortDisInbounds_Type()
)
nb30PortDisInbounds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortDisInbounds.setStatus("mandatory")
_Nb30PortFwdOutbs_Type = Counter32
_Nb30PortFwdOutbs_Object = MibTableColumn
nb30PortFwdOutbs = _Nb30PortFwdOutbs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 8),
    _Nb30PortFwdOutbs_Type()
)
nb30PortFwdOutbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortFwdOutbs.setStatus("mandatory")
_Nb30PortDisLOBs_Type = Counter32
_Nb30PortDisLOBs_Object = MibTableColumn
nb30PortDisLOBs = _Nb30PortDisLOBs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 9),
    _Nb30PortDisLOBs_Type()
)
nb30PortDisLOBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortDisLOBs.setStatus("mandatory")
_Nb30PortDisTDEs_Type = Counter32
_Nb30PortDisTDEs_Object = MibTableColumn
nb30PortDisTDEs = _Nb30PortDisTDEs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 10),
    _Nb30PortDisTDEs_Type()
)
nb30PortDisTDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortDisTDEs.setStatus("mandatory")
_Nb30PortCollisions_Type = Counter32
_Nb30PortCollisions_Object = MibTableColumn
nb30PortCollisions = _Nb30PortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 11),
    _Nb30PortCollisions_Type()
)
nb30PortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortCollisions.setStatus("mandatory")
_Nb30PortTxAborts_Type = Counter32
_Nb30PortTxAborts_Object = MibTableColumn
nb30PortTxAborts = _Nb30PortTxAborts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 12),
    _Nb30PortTxAborts_Type()
)
nb30PortTxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortTxAborts.setStatus("mandatory")
_Nb30PortOowCollisions_Type = Counter32
_Nb30PortOowCollisions_Object = MibTableColumn
nb30PortOowCollisions = _Nb30PortOowCollisions_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 13),
    _Nb30PortOowCollisions_Type()
)
nb30PortOowCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortOowCollisions.setStatus("mandatory")
_Nb30PortCRCErrs_Type = Counter32
_Nb30PortCRCErrs_Object = MibTableColumn
nb30PortCRCErrs = _Nb30PortCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 14),
    _Nb30PortCRCErrs_Type()
)
nb30PortCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortCRCErrs.setStatus("mandatory")
_Nb30PortFrAlignErrs_Type = Counter32
_Nb30PortFrAlignErrs_Object = MibTableColumn
nb30PortFrAlignErrs = _Nb30PortFrAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 15),
    _Nb30PortFrAlignErrs_Type()
)
nb30PortFrAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortFrAlignErrs.setStatus("mandatory")
_Nb30PortPriority_Type = Integer32
_Nb30PortPriority_Object = MibTableColumn
nb30PortPriority = _Nb30PortPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 16),
    _Nb30PortPriority_Type()
)
nb30PortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30PortPriority.setStatus("mandatory")
_Nb30PortState_Type = OctetString
_Nb30PortState_Object = MibTableColumn
nb30PortState = _Nb30PortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 17),
    _Nb30PortState_Type()
)
nb30PortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortState.setStatus("mandatory")
_Nb30PortPathCost_Type = Integer32
_Nb30PortPathCost_Object = MibTableColumn
nb30PortPathCost = _Nb30PortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 18),
    _Nb30PortPathCost_Type()
)
nb30PortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30PortPathCost.setStatus("mandatory")
_Nb30PortDesigCost_Type = Integer32
_Nb30PortDesigCost_Object = MibTableColumn
nb30PortDesigCost = _Nb30PortDesigCost_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 19),
    _Nb30PortDesigCost_Type()
)
nb30PortDesigCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortDesigCost.setStatus("mandatory")
_Nb30PortDesigBrdg_Type = OctetString
_Nb30PortDesigBrdg_Object = MibTableColumn
nb30PortDesigBrdg = _Nb30PortDesigBrdg_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 20),
    _Nb30PortDesigBrdg_Type()
)
nb30PortDesigBrdg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortDesigBrdg.setStatus("mandatory")
_Nb30PortDesigPort_Type = Integer32
_Nb30PortDesigPort_Object = MibTableColumn
nb30PortDesigPort = _Nb30PortDesigPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 21),
    _Nb30PortDesigPort_Type()
)
nb30PortDesigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortDesigPort.setStatus("mandatory")


class _Nb30PortTopChgAck_Type(Integer32):
    """Custom type nb30PortTopChgAck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noTopologyChangeIsOccurring", 1),
          ("topologyChangeIsOccurring", 2))
    )


_Nb30PortTopChgAck_Type.__name__ = "Integer32"
_Nb30PortTopChgAck_Object = MibTableColumn
nb30PortTopChgAck = _Nb30PortTopChgAck_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 22),
    _Nb30PortTopChgAck_Type()
)
nb30PortTopChgAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortTopChgAck.setStatus("mandatory")
_Nb30PortDesigRoot_Type = OctetString
_Nb30PortDesigRoot_Object = MibTableColumn
nb30PortDesigRoot = _Nb30PortDesigRoot_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 23),
    _Nb30PortDesigRoot_Type()
)
nb30PortDesigRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortDesigRoot.setStatus("mandatory")
_Nb30PortOversizePkts_Type = Counter32
_Nb30PortOversizePkts_Object = MibTableColumn
nb30PortOversizePkts = _Nb30PortOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 24),
    _Nb30PortOversizePkts_Type()
)
nb30PortOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortOversizePkts.setStatus("mandatory")
_Nb30PortFrFiltereds_Type = Counter32
_Nb30PortFrFiltereds_Object = MibTableColumn
nb30PortFrFiltereds = _Nb30PortFrFiltereds_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 25),
    _Nb30PortFrFiltereds_Type()
)
nb30PortFrFiltereds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortFrFiltereds.setStatus("mandatory")
_Nb30PortPollAddress_Type = OctetString
_Nb30PortPollAddress_Object = MibTableColumn
nb30PortPollAddress = _Nb30PortPollAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 26),
    _Nb30PortPollAddress_Type()
)
nb30PortPollAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30PortPollAddress.setStatus("mandatory")
_Nb30PortPollInterval_Type = Integer32
_Nb30PortPollInterval_Object = MibTableColumn
nb30PortPollInterval = _Nb30PortPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 27),
    _Nb30PortPollInterval_Type()
)
nb30PortPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30PortPollInterval.setStatus("mandatory")
_Nb30PortMaxRetry_Type = Integer32
_Nb30PortMaxRetry_Object = MibTableColumn
nb30PortMaxRetry = _Nb30PortMaxRetry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 28),
    _Nb30PortMaxRetry_Type()
)
nb30PortMaxRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30PortMaxRetry.setStatus("mandatory")
_Nb30PortId_Type = Integer32
_Nb30PortId_Object = MibTableColumn
nb30PortId = _Nb30PortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 4, 1, 1, 29),
    _Nb30PortId_Type()
)
nb30PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PortId.setStatus("mandatory")
_Nb30RemPort_ObjectIdentity = ObjectIdentity
nb30RemPort = _Nb30RemPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5)
)
_Nb30RemPortTable_Object = MibTable
nb30RemPortTable = _Nb30RemPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1)
)
if mibBuilder.loadTexts:
    nb30RemPortTable.setStatus("mandatory")
_Nb30RemPortEntry_Object = MibTableRow
nb30RemPortEntry = _Nb30RemPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1)
)
nb30RemPortEntry.setIndexNames(
    (0, "NB30MIB", "nb30RemPortId"),
)
if mibBuilder.loadTexts:
    nb30RemPortEntry.setStatus("mandatory")
_Nb30RemPortName_Type = OctetString
_Nb30RemPortName_Object = MibTableColumn
nb30RemPortName = _Nb30RemPortName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 1),
    _Nb30RemPortName_Type()
)
nb30RemPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30RemPortName.setStatus("mandatory")
_Nb30RemPortType_Type = OctetString
_Nb30RemPortType_Object = MibTableColumn
nb30RemPortType = _Nb30RemPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 2),
    _Nb30RemPortType_Type()
)
nb30RemPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30RemPortType.setStatus("mandatory")
_Nb30RemPortStatus_Type = OctetString
_Nb30RemPortStatus_Object = MibTableColumn
nb30RemPortStatus = _Nb30RemPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 3),
    _Nb30RemPortStatus_Type()
)
nb30RemPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30RemPortStatus.setStatus("mandatory")
_Nb30RemPortNetName_Type = OctetString
_Nb30RemPortNetName_Object = MibTableColumn
nb30RemPortNetName = _Nb30RemPortNetName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 4),
    _Nb30RemPortNetName_Type()
)
nb30RemPortNetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30RemPortNetName.setStatus("mandatory")
_Nb30RemPortFrRxs_Type = Counter32
_Nb30RemPortFrRxs_Object = MibTableColumn
nb30RemPortFrRxs = _Nb30RemPortFrRxs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 5),
    _Nb30RemPortFrRxs_Type()
)
nb30RemPortFrRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30RemPortFrRxs.setStatus("mandatory")
_Nb30RemPortFwdOutbs_Type = Counter32
_Nb30RemPortFwdOutbs_Object = MibTableColumn
nb30RemPortFwdOutbs = _Nb30RemPortFwdOutbs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 6),
    _Nb30RemPortFwdOutbs_Type()
)
nb30RemPortFwdOutbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30RemPortFwdOutbs.setStatus("mandatory")
_Nb30RemPortDisLOBs_Type = Counter32
_Nb30RemPortDisLOBs_Object = MibTableColumn
nb30RemPortDisLOBs = _Nb30RemPortDisLOBs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 7),
    _Nb30RemPortDisLOBs_Type()
)
nb30RemPortDisLOBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30RemPortDisLOBs.setStatus("mandatory")
_Nb30RemPortDisTDEs_Type = Counter32
_Nb30RemPortDisTDEs_Object = MibTableColumn
nb30RemPortDisTDEs = _Nb30RemPortDisTDEs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 8),
    _Nb30RemPortDisTDEs_Type()
)
nb30RemPortDisTDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30RemPortDisTDEs.setStatus("mandatory")
_Nb30RemPortCRCErrs_Type = Counter32
_Nb30RemPortCRCErrs_Object = MibTableColumn
nb30RemPortCRCErrs = _Nb30RemPortCRCErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 9),
    _Nb30RemPortCRCErrs_Type()
)
nb30RemPortCRCErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30RemPortCRCErrs.setStatus("mandatory")
_Nb30RemPortFrAlErrs_Type = Counter32
_Nb30RemPortFrAlErrs_Object = MibTableColumn
nb30RemPortFrAlErrs = _Nb30RemPortFrAlErrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 10),
    _Nb30RemPortFrAlErrs_Type()
)
nb30RemPortFrAlErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30RemPortFrAlErrs.setStatus("mandatory")
_Nb30RemPortId_Type = Integer32
_Nb30RemPortId_Object = MibTableColumn
nb30RemPortId = _Nb30RemPortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 5, 1, 1, 11),
    _Nb30RemPortId_Type()
)
nb30RemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30RemPortId.setStatus("mandatory")
_Nb30FilterDB_ObjectIdentity = ObjectIdentity
nb30FilterDB = _Nb30FilterDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6)
)
_Nb30AcqDB_ObjectIdentity = ObjectIdentity
nb30AcqDB = _Nb30AcqDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1)
)
_Nb30AcqTotalEntries_Type = Integer32
_Nb30AcqTotalEntries_Object = MibScalar
nb30AcqTotalEntries = _Nb30AcqTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 1),
    _Nb30AcqTotalEntries_Type()
)
nb30AcqTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30AcqTotalEntries.setStatus("mandatory")
_Nb30AcqMaxEntries_Type = Integer32
_Nb30AcqMaxEntries_Object = MibScalar
nb30AcqMaxEntries = _Nb30AcqMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 2),
    _Nb30AcqMaxEntries_Type()
)
nb30AcqMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30AcqMaxEntries.setStatus("mandatory")
_Nb30AcqStaticEntries_Type = Integer32
_Nb30AcqStaticEntries_Object = MibScalar
nb30AcqStaticEntries = _Nb30AcqStaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 3),
    _Nb30AcqStaticEntries_Type()
)
nb30AcqStaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30AcqStaticEntries.setStatus("mandatory")
_Nb30AcqDynamicEntries_Type = Integer32
_Nb30AcqDynamicEntries_Object = MibScalar
nb30AcqDynamicEntries = _Nb30AcqDynamicEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 4),
    _Nb30AcqDynamicEntries_Type()
)
nb30AcqDynamicEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30AcqDynamicEntries.setStatus("mandatory")
_Nb30AcqDynAgeTime_Type = Integer32
_Nb30AcqDynAgeTime_Object = MibScalar
nb30AcqDynAgeTime = _Nb30AcqDynAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 5),
    _Nb30AcqDynAgeTime_Type()
)
nb30AcqDynAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30AcqDynAgeTime.setStatus("mandatory")


class _Nb30AcqEraseDatabase_Type(Integer32):
    """Custom type nb30AcqEraseDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eraseAcquiredDatabase", 1)
    )


_Nb30AcqEraseDatabase_Type.__name__ = "Integer32"
_Nb30AcqEraseDatabase_Object = MibScalar
nb30AcqEraseDatabase = _Nb30AcqEraseDatabase_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 6),
    _Nb30AcqEraseDatabase_Type()
)
nb30AcqEraseDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30AcqEraseDatabase.setStatus("mandatory")
_Nb30AcqDBTable_Object = MibTable
nb30AcqDBTable = _Nb30AcqDBTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7)
)
if mibBuilder.loadTexts:
    nb30AcqDBTable.setStatus("mandatory")
_Nb30AcqDBEntry_Object = MibTableRow
nb30AcqDBEntry = _Nb30AcqDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1)
)
nb30AcqDBEntry.setIndexNames(
    (0, "NB30MIB", "nb30AcqMacAddress"),
)
if mibBuilder.loadTexts:
    nb30AcqDBEntry.setStatus("mandatory")


class _Nb30AcqCreateFilter_Type(Integer32):
    """Custom type nb30AcqCreateFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("createAcquiredFilter", 1)
    )


_Nb30AcqCreateFilter_Type.__name__ = "Integer32"
_Nb30AcqCreateFilter_Object = MibTableColumn
nb30AcqCreateFilter = _Nb30AcqCreateFilter_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 1),
    _Nb30AcqCreateFilter_Type()
)
nb30AcqCreateFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30AcqCreateFilter.setStatus("mandatory")


class _Nb30AcqCreateForward_Type(Integer32):
    """Custom type nb30AcqCreateForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("createAcquiredForward", 1)
    )


_Nb30AcqCreateForward_Type.__name__ = "Integer32"
_Nb30AcqCreateForward_Object = MibTableColumn
nb30AcqCreateForward = _Nb30AcqCreateForward_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 2),
    _Nb30AcqCreateForward_Type()
)
nb30AcqCreateForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30AcqCreateForward.setStatus("mandatory")


class _Nb30AcqDeleteFilter_Type(Integer32):
    """Custom type nb30AcqDeleteFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deleteAcquiredEntry", 1)
    )


_Nb30AcqDeleteFilter_Type.__name__ = "Integer32"
_Nb30AcqDeleteFilter_Object = MibTableColumn
nb30AcqDeleteFilter = _Nb30AcqDeleteFilter_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 3),
    _Nb30AcqDeleteFilter_Type()
)
nb30AcqDeleteFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30AcqDeleteFilter.setStatus("mandatory")
_Nb30AcqFilterType_Type = OctetString
_Nb30AcqFilterType_Object = MibTableColumn
nb30AcqFilterType = _Nb30AcqFilterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 4),
    _Nb30AcqFilterType_Type()
)
nb30AcqFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30AcqFilterType.setStatus("mandatory")


class _Nb30AcqFilterAction_Type(Integer32):
    """Custom type nb30AcqFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("relay", 2))
    )


_Nb30AcqFilterAction_Type.__name__ = "Integer32"
_Nb30AcqFilterAction_Object = MibTableColumn
nb30AcqFilterAction = _Nb30AcqFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 5),
    _Nb30AcqFilterAction_Type()
)
nb30AcqFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30AcqFilterAction.setStatus("mandatory")
_Nb30AcqSourceAddress_Type = OctetString
_Nb30AcqSourceAddress_Object = MibTableColumn
nb30AcqSourceAddress = _Nb30AcqSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 6),
    _Nb30AcqSourceAddress_Type()
)
nb30AcqSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30AcqSourceAddress.setStatus("mandatory")


class _Nb30AcqMacAddress_Type(OctetString):
    """Custom type nb30AcqMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Nb30AcqMacAddress_Type.__name__ = "OctetString"
_Nb30AcqMacAddress_Object = MibTableColumn
nb30AcqMacAddress = _Nb30AcqMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 1, 7, 1, 7),
    _Nb30AcqMacAddress_Type()
)
nb30AcqMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30AcqMacAddress.setStatus("mandatory")
_Nb30PermDB_ObjectIdentity = ObjectIdentity
nb30PermDB = _Nb30PermDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2)
)
_Nb30PermMaxEntries_Type = Integer32
_Nb30PermMaxEntries_Object = MibScalar
nb30PermMaxEntries = _Nb30PermMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 1),
    _Nb30PermMaxEntries_Type()
)
nb30PermMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PermMaxEntries.setStatus("mandatory")
_Nb30PermCurrentEntries_Type = Integer32
_Nb30PermCurrentEntries_Object = MibScalar
nb30PermCurrentEntries = _Nb30PermCurrentEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 2),
    _Nb30PermCurrentEntries_Type()
)
nb30PermCurrentEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PermCurrentEntries.setStatus("mandatory")


class _Nb30PermEraseDatabase_Type(Integer32):
    """Custom type nb30PermEraseDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("erasePermanentDatabase", 1)
    )


_Nb30PermEraseDatabase_Type.__name__ = "Integer32"
_Nb30PermEraseDatabase_Object = MibScalar
nb30PermEraseDatabase = _Nb30PermEraseDatabase_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 3),
    _Nb30PermEraseDatabase_Type()
)
nb30PermEraseDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30PermEraseDatabase.setStatus("mandatory")
_Nb30PermDBTable_Object = MibTable
nb30PermDBTable = _Nb30PermDBTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4)
)
if mibBuilder.loadTexts:
    nb30PermDBTable.setStatus("mandatory")
_Nb30PermDBEntry_Object = MibTableRow
nb30PermDBEntry = _Nb30PermDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1)
)
nb30PermDBEntry.setIndexNames(
    (0, "NB30MIB", "nb30PermDBMacAddress"),
)
if mibBuilder.loadTexts:
    nb30PermDBEntry.setStatus("mandatory")


class _Nb30PermCreateFilter_Type(Integer32):
    """Custom type nb30PermCreateFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("createPermanentFilter", 1)
    )


_Nb30PermCreateFilter_Type.__name__ = "Integer32"
_Nb30PermCreateFilter_Object = MibTableColumn
nb30PermCreateFilter = _Nb30PermCreateFilter_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 1),
    _Nb30PermCreateFilter_Type()
)
nb30PermCreateFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30PermCreateFilter.setStatus("mandatory")


class _Nb30PermCreateForward_Type(Integer32):
    """Custom type nb30PermCreateForward based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("createPermanentForward", 1)
    )


_Nb30PermCreateForward_Type.__name__ = "Integer32"
_Nb30PermCreateForward_Object = MibTableColumn
nb30PermCreateForward = _Nb30PermCreateForward_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 2),
    _Nb30PermCreateForward_Type()
)
nb30PermCreateForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30PermCreateForward.setStatus("mandatory")


class _Nb30PermDeleteEntry_Type(Integer32):
    """Custom type nb30PermDeleteEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deletePermanentEntry", 1)
    )


_Nb30PermDeleteEntry_Type.__name__ = "Integer32"
_Nb30PermDeleteEntry_Object = MibTableColumn
nb30PermDeleteEntry = _Nb30PermDeleteEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 3),
    _Nb30PermDeleteEntry_Type()
)
nb30PermDeleteEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30PermDeleteEntry.setStatus("mandatory")
_Nb30PermFilterType_Type = OctetString
_Nb30PermFilterType_Object = MibTableColumn
nb30PermFilterType = _Nb30PermFilterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 4),
    _Nb30PermFilterType_Type()
)
nb30PermFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PermFilterType.setStatus("mandatory")


class _Nb30PermFilterAction_Type(Integer32):
    """Custom type nb30PermFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("relay", 2))
    )


_Nb30PermFilterAction_Type.__name__ = "Integer32"
_Nb30PermFilterAction_Object = MibTableColumn
nb30PermFilterAction = _Nb30PermFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 5),
    _Nb30PermFilterAction_Type()
)
nb30PermFilterAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PermFilterAction.setStatus("mandatory")
_Nb30PermSourceAddress_Type = OctetString
_Nb30PermSourceAddress_Object = MibTableColumn
nb30PermSourceAddress = _Nb30PermSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 6),
    _Nb30PermSourceAddress_Type()
)
nb30PermSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PermSourceAddress.setStatus("mandatory")


class _Nb30PermDBMacAddress_Type(OctetString):
    """Custom type nb30PermDBMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Nb30PermDBMacAddress_Type.__name__ = "OctetString"
_Nb30PermDBMacAddress_Object = MibTableColumn
nb30PermDBMacAddress = _Nb30PermDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 2, 4, 1, 7),
    _Nb30PermDBMacAddress_Type()
)
nb30PermDBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30PermDBMacAddress.setStatus("mandatory")
_Nb30SpecDB_ObjectIdentity = ObjectIdentity
nb30SpecDB = _Nb30SpecDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3)
)
_Nb30SpecNumEntries_Type = Integer32
_Nb30SpecNumEntries_Object = MibScalar
nb30SpecNumEntries = _Nb30SpecNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 1),
    _Nb30SpecNumEntries_Type()
)
nb30SpecNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30SpecNumEntries.setStatus("mandatory")
_Nb30SpecMaxEntries_Type = Integer32
_Nb30SpecMaxEntries_Object = MibScalar
nb30SpecMaxEntries = _Nb30SpecMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 2),
    _Nb30SpecMaxEntries_Type()
)
nb30SpecMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30SpecMaxEntries.setStatus("mandatory")
_Nb30SpecNextFilterNum_Type = Integer32
_Nb30SpecNextFilterNum_Object = MibScalar
nb30SpecNextFilterNum = _Nb30SpecNextFilterNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 3),
    _Nb30SpecNextFilterNum_Type()
)
nb30SpecNextFilterNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30SpecNextFilterNum.setStatus("mandatory")
_Nb30SpecDBTable_Object = MibTable
nb30SpecDBTable = _Nb30SpecDBTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4)
)
if mibBuilder.loadTexts:
    nb30SpecDBTable.setStatus("mandatory")
_Nb30SpecDBEntry_Object = MibTableRow
nb30SpecDBEntry = _Nb30SpecDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1)
)
nb30SpecDBEntry.setIndexNames(
    (0, "NB30MIB", "nb30SpecDbFilterNumber"),
)
if mibBuilder.loadTexts:
    nb30SpecDBEntry.setStatus("mandatory")


class _Nb30SpecEnable_Type(Integer32):
    """Custom type nb30SpecEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableFilter", 1),
          ("enableFilter", 2))
    )


_Nb30SpecEnable_Type.__name__ = "Integer32"
_Nb30SpecEnable_Object = MibTableColumn
nb30SpecEnable = _Nb30SpecEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 1),
    _Nb30SpecEnable_Type()
)
nb30SpecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30SpecEnable.setStatus("mandatory")


class _Nb30SpecPort1_Type(Integer32):
    """Custom type nb30SpecPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("relay", 2))
    )


_Nb30SpecPort1_Type.__name__ = "Integer32"
_Nb30SpecPort1_Object = MibTableColumn
nb30SpecPort1 = _Nb30SpecPort1_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 2),
    _Nb30SpecPort1_Type()
)
nb30SpecPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30SpecPort1.setStatus("mandatory")
_Nb30SpecDestAddress_Type = OctetString
_Nb30SpecDestAddress_Object = MibTableColumn
nb30SpecDestAddress = _Nb30SpecDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 3),
    _Nb30SpecDestAddress_Type()
)
nb30SpecDestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30SpecDestAddress.setStatus("mandatory")
_Nb30SpecSrcAddress_Type = OctetString
_Nb30SpecSrcAddress_Object = MibTableColumn
nb30SpecSrcAddress = _Nb30SpecSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 4),
    _Nb30SpecSrcAddress_Type()
)
nb30SpecSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30SpecSrcAddress.setStatus("mandatory")
_Nb30SpecType_Type = OctetString
_Nb30SpecType_Object = MibTableColumn
nb30SpecType = _Nb30SpecType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 5),
    _Nb30SpecType_Type()
)
nb30SpecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30SpecType.setStatus("mandatory")
_Nb30SpecDataField_Type = OctetString
_Nb30SpecDataField_Object = MibTableColumn
nb30SpecDataField = _Nb30SpecDataField_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 6),
    _Nb30SpecDataField_Type()
)
nb30SpecDataField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30SpecDataField.setStatus("mandatory")


class _Nb30SpecDeleteFilter_Type(Integer32):
    """Custom type nb30SpecDeleteFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deleteFilter", 1)
    )


_Nb30SpecDeleteFilter_Type.__name__ = "Integer32"
_Nb30SpecDeleteFilter_Object = MibTableColumn
nb30SpecDeleteFilter = _Nb30SpecDeleteFilter_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 7),
    _Nb30SpecDeleteFilter_Type()
)
nb30SpecDeleteFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nb30SpecDeleteFilter.setStatus("mandatory")
_Nb30SpecDbFilterNumber_Type = Integer32
_Nb30SpecDbFilterNumber_Object = MibTableColumn
nb30SpecDbFilterNumber = _Nb30SpecDbFilterNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 12, 6, 3, 4, 1, 8),
    _Nb30SpecDbFilterNumber_Type()
)
nb30SpecDbFilterNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nb30SpecDbFilterNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NB30MIB",
    **{"nb30Device": nb30Device,
       "nb30DeviceDisableBdg": nb30DeviceDisableBdg,
       "nb30DeviceRestoreSettings": nb30DeviceRestoreSettings,
       "nb30DeviceBdgName": nb30DeviceBdgName,
       "nb30DeviceNumPorts": nb30DeviceNumPorts,
       "nb30DeviceType": nb30DeviceType,
       "nb30DeviceVersion": nb30DeviceVersion,
       "nb30DeviceLocation": nb30DeviceLocation,
       "nb30DeviceStatus": nb30DeviceStatus,
       "nb30DeviceRestartBdg": nb30DeviceRestartBdg,
       "nb30DeviceFrFwds": nb30DeviceFrFwds,
       "nb30DeviceFrRxs": nb30DeviceFrRxs,
       "nb30DeviceFrFlts": nb30DeviceFrFlts,
       "nb30DeviceErrs": nb30DeviceErrs,
       "nb30DeviceNumRestarts": nb30DeviceNumRestarts,
       "nb30DeviceTypeFiltering": nb30DeviceTypeFiltering,
       "nb30DeviceSTAProtocol": nb30DeviceSTAProtocol,
       "nb30DeviceBridgeID": nb30DeviceBridgeID,
       "nb30DeviceTopChgCnts": nb30DeviceTopChgCnts,
       "nb30DeviceTimeTopChg": nb30DeviceTimeTopChg,
       "nb30DeviceTopChg": nb30DeviceTopChg,
       "nb30DeviceRootCost": nb30DeviceRootCost,
       "nb30DeviceRootPort": nb30DeviceRootPort,
       "nb30DeviceDesigRoot": nb30DeviceDesigRoot,
       "nb30DeviceMaxAge": nb30DeviceMaxAge,
       "nb30DeviceHoldTime": nb30DeviceHoldTime,
       "nb30DeviceFwdDly": nb30DeviceFwdDly,
       "nb30DeviceHelloTime": nb30DeviceHelloTime,
       "nb30DeviceBdgFwdDly": nb30DeviceBdgFwdDly,
       "nb30DeviceBdgMaxAge": nb30DeviceBdgMaxAge,
       "nb30DeviceBdgHello": nb30DeviceBdgHello,
       "nb30DeviceBdgPriority": nb30DeviceBdgPriority,
       "nb30DeviceResetCounts": nb30DeviceResetCounts,
       "nb30DeviceUptime": nb30DeviceUptime,
       "nb30DeviceRootSwitch": nb30DeviceRootSwitch,
       "nb30DeviceFwdBroadcast": nb30DeviceFwdBroadcast,
       "nb30DeviceConfigSw1": nb30DeviceConfigSw1,
       "nb30DeviceConfigSw2": nb30DeviceConfigSw2,
       "nb30DeviceConfigSw3": nb30DeviceConfigSw3,
       "nb30DeviceConfigSw4": nb30DeviceConfigSw4,
       "nb30DevicePortActive": nb30DevicePortActive,
       "nb30DeviceDefPort": nb30DeviceDefPort,
       "nb30DeviceRedEnable": nb30DeviceRedEnable,
       "nb30Dsx": nb30Dsx,
       "nb30DsxLoopUp": nb30DsxLoopUp,
       "nb30DsxLoopDn": nb30DsxLoopDn,
       "nb30DsxLoopSt": nb30DsxLoopSt,
       "nb30DsxLoopPattern": nb30DsxLoopPattern,
       "nb30DsxChannel": nb30DsxChannel,
       "nb30DsxChannelTable": nb30DsxChannelTable,
       "nb30DsxEntry": nb30DsxEntry,
       "nb30DsxChannelControl": nb30DsxChannelControl,
       "nb30DsxChannelId": nb30DsxChannelId,
       "nb30Port": nb30Port,
       "nb30PortTable": nb30PortTable,
       "nb30PortEntry": nb30PortEntry,
       "nb30PortAddress": nb30PortAddress,
       "nb30PortName": nb30PortName,
       "nb30PortType": nb30PortType,
       "nb30PortStatus": nb30PortStatus,
       "nb30PortNetName": nb30PortNetName,
       "nb30PortFrRxs": nb30PortFrRxs,
       "nb30PortDisInbounds": nb30PortDisInbounds,
       "nb30PortFwdOutbs": nb30PortFwdOutbs,
       "nb30PortDisLOBs": nb30PortDisLOBs,
       "nb30PortDisTDEs": nb30PortDisTDEs,
       "nb30PortCollisions": nb30PortCollisions,
       "nb30PortTxAborts": nb30PortTxAborts,
       "nb30PortOowCollisions": nb30PortOowCollisions,
       "nb30PortCRCErrs": nb30PortCRCErrs,
       "nb30PortFrAlignErrs": nb30PortFrAlignErrs,
       "nb30PortPriority": nb30PortPriority,
       "nb30PortState": nb30PortState,
       "nb30PortPathCost": nb30PortPathCost,
       "nb30PortDesigCost": nb30PortDesigCost,
       "nb30PortDesigBrdg": nb30PortDesigBrdg,
       "nb30PortDesigPort": nb30PortDesigPort,
       "nb30PortTopChgAck": nb30PortTopChgAck,
       "nb30PortDesigRoot": nb30PortDesigRoot,
       "nb30PortOversizePkts": nb30PortOversizePkts,
       "nb30PortFrFiltereds": nb30PortFrFiltereds,
       "nb30PortPollAddress": nb30PortPollAddress,
       "nb30PortPollInterval": nb30PortPollInterval,
       "nb30PortMaxRetry": nb30PortMaxRetry,
       "nb30PortId": nb30PortId,
       "nb30RemPort": nb30RemPort,
       "nb30RemPortTable": nb30RemPortTable,
       "nb30RemPortEntry": nb30RemPortEntry,
       "nb30RemPortName": nb30RemPortName,
       "nb30RemPortType": nb30RemPortType,
       "nb30RemPortStatus": nb30RemPortStatus,
       "nb30RemPortNetName": nb30RemPortNetName,
       "nb30RemPortFrRxs": nb30RemPortFrRxs,
       "nb30RemPortFwdOutbs": nb30RemPortFwdOutbs,
       "nb30RemPortDisLOBs": nb30RemPortDisLOBs,
       "nb30RemPortDisTDEs": nb30RemPortDisTDEs,
       "nb30RemPortCRCErrs": nb30RemPortCRCErrs,
       "nb30RemPortFrAlErrs": nb30RemPortFrAlErrs,
       "nb30RemPortId": nb30RemPortId,
       "nb30FilterDB": nb30FilterDB,
       "nb30AcqDB": nb30AcqDB,
       "nb30AcqTotalEntries": nb30AcqTotalEntries,
       "nb30AcqMaxEntries": nb30AcqMaxEntries,
       "nb30AcqStaticEntries": nb30AcqStaticEntries,
       "nb30AcqDynamicEntries": nb30AcqDynamicEntries,
       "nb30AcqDynAgeTime": nb30AcqDynAgeTime,
       "nb30AcqEraseDatabase": nb30AcqEraseDatabase,
       "nb30AcqDBTable": nb30AcqDBTable,
       "nb30AcqDBEntry": nb30AcqDBEntry,
       "nb30AcqCreateFilter": nb30AcqCreateFilter,
       "nb30AcqCreateForward": nb30AcqCreateForward,
       "nb30AcqDeleteFilter": nb30AcqDeleteFilter,
       "nb30AcqFilterType": nb30AcqFilterType,
       "nb30AcqFilterAction": nb30AcqFilterAction,
       "nb30AcqSourceAddress": nb30AcqSourceAddress,
       "nb30AcqMacAddress": nb30AcqMacAddress,
       "nb30PermDB": nb30PermDB,
       "nb30PermMaxEntries": nb30PermMaxEntries,
       "nb30PermCurrentEntries": nb30PermCurrentEntries,
       "nb30PermEraseDatabase": nb30PermEraseDatabase,
       "nb30PermDBTable": nb30PermDBTable,
       "nb30PermDBEntry": nb30PermDBEntry,
       "nb30PermCreateFilter": nb30PermCreateFilter,
       "nb30PermCreateForward": nb30PermCreateForward,
       "nb30PermDeleteEntry": nb30PermDeleteEntry,
       "nb30PermFilterType": nb30PermFilterType,
       "nb30PermFilterAction": nb30PermFilterAction,
       "nb30PermSourceAddress": nb30PermSourceAddress,
       "nb30PermDBMacAddress": nb30PermDBMacAddress,
       "nb30SpecDB": nb30SpecDB,
       "nb30SpecNumEntries": nb30SpecNumEntries,
       "nb30SpecMaxEntries": nb30SpecMaxEntries,
       "nb30SpecNextFilterNum": nb30SpecNextFilterNum,
       "nb30SpecDBTable": nb30SpecDBTable,
       "nb30SpecDBEntry": nb30SpecDBEntry,
       "nb30SpecEnable": nb30SpecEnable,
       "nb30SpecPort1": nb30SpecPort1,
       "nb30SpecDestAddress": nb30SpecDestAddress,
       "nb30SpecSrcAddress": nb30SpecSrcAddress,
       "nb30SpecType": nb30SpecType,
       "nb30SpecDataField": nb30SpecDataField,
       "nb30SpecDeleteFilter": nb30SpecDeleteFilter,
       "nb30SpecDbFilterNumber": nb30SpecDbFilterNumber}
)
