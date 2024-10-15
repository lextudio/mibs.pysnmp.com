# SNMP MIB module (DES3200-18-L2MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DES3200-18-L2MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:25:11 2024
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(des3200_18,) = mibBuilder.importSymbols(
    "SWPRIMGMT-DES3200-MIB",
    "des3200-18")


# MODULE-IDENTITY

swL2MgmtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2)
)


# Types definitions



class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )





class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )





class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwL2DevMgmt_ObjectIdentity = ObjectIdentity
swL2DevMgmt = _SwL2DevMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1)
)
_SwL2DevInfo_ObjectIdentity = ObjectIdentity
swL2DevInfo = _SwL2DevInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 1)
)


class _SwL2DevInfoFrontPanelLedStatus_Type(OctetString):
    """Custom type swL2DevInfoFrontPanelLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwL2DevInfoFrontPanelLedStatus_Type.__name__ = "OctetString"
_SwL2DevInfoFrontPanelLedStatus_Object = MibScalar
swL2DevInfoFrontPanelLedStatus = _SwL2DevInfoFrontPanelLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 1, 5),
    _SwL2DevInfoFrontPanelLedStatus_Type()
)
swL2DevInfoFrontPanelLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DevInfoFrontPanelLedStatus.setStatus("current")
_SwL2DevCtrl_ObjectIdentity = ObjectIdentity
swL2DevCtrl = _SwL2DevCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2)
)


class _SwL2DevCtrlSystemReboot_Type(Integer32):
    """Custom type swL2DevCtrlSystemReboot based on Integer32"""
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
        *(("other", 1),
          ("reboot", 2),
          ("reboot-and-load-factory-default-config", 4),
          ("save-config-and-reboot", 3))
    )


_SwL2DevCtrlSystemReboot_Type.__name__ = "Integer32"
_SwL2DevCtrlSystemReboot_Object = MibScalar
swL2DevCtrlSystemReboot = _SwL2DevCtrlSystemReboot_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 1),
    _SwL2DevCtrlSystemReboot_Type()
)
swL2DevCtrlSystemReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlSystemReboot.setStatus("current")
_SwL2DevCtrlSystemIP_Type = IpAddress
_SwL2DevCtrlSystemIP_Object = MibScalar
swL2DevCtrlSystemIP = _SwL2DevCtrlSystemIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 2),
    _SwL2DevCtrlSystemIP_Type()
)
swL2DevCtrlSystemIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlSystemIP.setStatus("current")
_SwL2DevCtrlSubnetMask_Type = IpAddress
_SwL2DevCtrlSubnetMask_Object = MibScalar
swL2DevCtrlSubnetMask = _SwL2DevCtrlSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 3),
    _SwL2DevCtrlSubnetMask_Type()
)
swL2DevCtrlSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlSubnetMask.setStatus("current")
_SwL2DevCtrlDefaultGateway_Type = IpAddress
_SwL2DevCtrlDefaultGateway_Object = MibScalar
swL2DevCtrlDefaultGateway = _SwL2DevCtrlDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 4),
    _SwL2DevCtrlDefaultGateway_Type()
)
swL2DevCtrlDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlDefaultGateway.setStatus("current")
_SwL2DevCtrlManagementVlanId_Type = VlanId
_SwL2DevCtrlManagementVlanId_Object = MibScalar
swL2DevCtrlManagementVlanId = _SwL2DevCtrlManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 5),
    _SwL2DevCtrlManagementVlanId_Type()
)
swL2DevCtrlManagementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlManagementVlanId.setStatus("current")


class _SwL2DevCtrlIGMPSnooping_Type(Integer32):
    """Custom type swL2DevCtrlIGMPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevCtrlIGMPSnooping_Type.__name__ = "Integer32"
_SwL2DevCtrlIGMPSnooping_Object = MibScalar
swL2DevCtrlIGMPSnooping = _SwL2DevCtrlIGMPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 7),
    _SwL2DevCtrlIGMPSnooping_Type()
)
swL2DevCtrlIGMPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIGMPSnooping.setStatus("current")


class _SwL2DevCtrlCleanAllStatisticCounter_Type(Integer32):
    """Custom type swL2DevCtrlCleanAllStatisticCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("normal", 1))
    )


_SwL2DevCtrlCleanAllStatisticCounter_Type.__name__ = "Integer32"
_SwL2DevCtrlCleanAllStatisticCounter_Object = MibScalar
swL2DevCtrlCleanAllStatisticCounter = _SwL2DevCtrlCleanAllStatisticCounter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 12),
    _SwL2DevCtrlCleanAllStatisticCounter_Type()
)
swL2DevCtrlCleanAllStatisticCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCleanAllStatisticCounter.setStatus("current")


class _SwL2DevCtrlSnmpEnableAuthenTraps_Type(Integer32):
    """Custom type swL2DevCtrlSnmpEnableAuthenTraps based on Integer32"""
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


_SwL2DevCtrlSnmpEnableAuthenTraps_Type.__name__ = "Integer32"
_SwL2DevCtrlSnmpEnableAuthenTraps_Object = MibScalar
swL2DevCtrlSnmpEnableAuthenTraps = _SwL2DevCtrlSnmpEnableAuthenTraps_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 13),
    _SwL2DevCtrlSnmpEnableAuthenTraps_Type()
)
swL2DevCtrlSnmpEnableAuthenTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlSnmpEnableAuthenTraps.setStatus("current")


class _SwL2DevCtrlRmonState_Type(Integer32):
    """Custom type swL2DevCtrlRmonState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevCtrlRmonState_Type.__name__ = "Integer32"
_SwL2DevCtrlRmonState_Object = MibScalar
swL2DevCtrlRmonState = _SwL2DevCtrlRmonState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 16),
    _SwL2DevCtrlRmonState_Type()
)
swL2DevCtrlRmonState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlRmonState.setStatus("current")


class _SwL2DevCtrlIpAutoConfig_Type(Integer32):
    """Custom type swL2DevCtrlIpAutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevCtrlIpAutoConfig_Type.__name__ = "Integer32"
_SwL2DevCtrlIpAutoConfig_Object = MibScalar
swL2DevCtrlIpAutoConfig = _SwL2DevCtrlIpAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 17),
    _SwL2DevCtrlIpAutoConfig_Type()
)
swL2DevCtrlIpAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlIpAutoConfig.setStatus("current")


class _SwL2MACNotifyState_Type(Integer32):
    """Custom type swL2MACNotifyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2MACNotifyState_Type.__name__ = "Integer32"
_SwL2MACNotifyState_Object = MibScalar
swL2MACNotifyState = _SwL2MACNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 19),
    _SwL2MACNotifyState_Type()
)
swL2MACNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MACNotifyState.setStatus("current")


class _SwL2MACNotifyHistorySize_Type(Integer32):
    """Custom type swL2MACNotifyHistorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_SwL2MACNotifyHistorySize_Type.__name__ = "Integer32"
_SwL2MACNotifyHistorySize_Object = MibScalar
swL2MACNotifyHistorySize = _SwL2MACNotifyHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 20),
    _SwL2MACNotifyHistorySize_Type()
)
swL2MACNotifyHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MACNotifyHistorySize.setStatus("current")


class _SwL2MACNotifyInterval_Type(Integer32):
    """Custom type swL2MACNotifyInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SwL2MACNotifyInterval_Type.__name__ = "Integer32"
_SwL2MACNotifyInterval_Object = MibScalar
swL2MACNotifyInterval = _SwL2MACNotifyInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 21),
    _SwL2MACNotifyInterval_Type()
)
swL2MACNotifyInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2MACNotifyInterval.setStatus("current")


class _SwL2DevCtrlLLDPState_Type(Integer32):
    """Custom type swL2DevCtrlLLDPState based on Integer32"""
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


_SwL2DevCtrlLLDPState_Type.__name__ = "Integer32"
_SwL2DevCtrlLLDPState_Object = MibScalar
swL2DevCtrlLLDPState = _SwL2DevCtrlLLDPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 22),
    _SwL2DevCtrlLLDPState_Type()
)
swL2DevCtrlLLDPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlLLDPState.setStatus("current")


class _SwL2DevCtrlLLDPForwardMessageState_Type(Integer32):
    """Custom type swL2DevCtrlLLDPForwardMessageState based on Integer32"""
    defaultValue = 2

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


_SwL2DevCtrlLLDPForwardMessageState_Type.__name__ = "Integer32"
_SwL2DevCtrlLLDPForwardMessageState_Object = MibScalar
swL2DevCtrlLLDPForwardMessageState = _SwL2DevCtrlLLDPForwardMessageState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 23),
    _SwL2DevCtrlLLDPForwardMessageState_Type()
)
swL2DevCtrlLLDPForwardMessageState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlLLDPForwardMessageState.setStatus("current")


class _SwL2DevCtrlAsymVlanState_Type(Integer32):
    """Custom type swL2DevCtrlAsymVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevCtrlAsymVlanState_Type.__name__ = "Integer32"
_SwL2DevCtrlAsymVlanState_Object = MibScalar
swL2DevCtrlAsymVlanState = _SwL2DevCtrlAsymVlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 24),
    _SwL2DevCtrlAsymVlanState_Type()
)
swL2DevCtrlAsymVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlAsymVlanState.setStatus("current")


class _SwL2IGMPSnoopingMulticastVlanState_Type(Integer32):
    """Custom type swL2IGMPSnoopingMulticastVlanState based on Integer32"""
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


_SwL2IGMPSnoopingMulticastVlanState_Type.__name__ = "Integer32"
_SwL2IGMPSnoopingMulticastVlanState_Object = MibScalar
swL2IGMPSnoopingMulticastVlanState = _SwL2IGMPSnoopingMulticastVlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 25),
    _SwL2IGMPSnoopingMulticastVlanState_Type()
)
swL2IGMPSnoopingMulticastVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingMulticastVlanState.setStatus("current")


class _SwL2DevCtrlVLANTrunkState_Type(Integer32):
    """Custom type swL2DevCtrlVLANTrunkState based on Integer32"""
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


_SwL2DevCtrlVLANTrunkState_Type.__name__ = "Integer32"
_SwL2DevCtrlVLANTrunkState_Object = MibScalar
swL2DevCtrlVLANTrunkState = _SwL2DevCtrlVLANTrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 26),
    _SwL2DevCtrlVLANTrunkState_Type()
)
swL2DevCtrlVLANTrunkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlVLANTrunkState.setStatus("current")


class _SwL2DevArpAgingTime_Type(Integer32):
    """Custom type swL2DevArpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2DevArpAgingTime_Type.__name__ = "Integer32"
_SwL2DevArpAgingTime_Object = MibScalar
swL2DevArpAgingTime = _SwL2DevArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 27),
    _SwL2DevArpAgingTime_Type()
)
swL2DevArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevArpAgingTime.setStatus("current")


class _SwL2DevPasswordEncryptionState_Type(Integer32):
    """Custom type swL2DevPasswordEncryptionState based on Integer32"""
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


_SwL2DevPasswordEncryptionState_Type.__name__ = "Integer32"
_SwL2DevPasswordEncryptionState_Object = MibScalar
swL2DevPasswordEncryptionState = _SwL2DevPasswordEncryptionState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 28),
    _SwL2DevPasswordEncryptionState_Type()
)
swL2DevPasswordEncryptionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevPasswordEncryptionState.setStatus("current")
_SwL2DevCtrlCFM_ObjectIdentity = ObjectIdentity
swL2DevCtrlCFM = _SwL2DevCtrlCFM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 29)
)


class _SwL2DevCtrlCFMState_Type(Integer32):
    """Custom type swL2DevCtrlCFMState based on Integer32"""
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


_SwL2DevCtrlCFMState_Type.__name__ = "Integer32"
_SwL2DevCtrlCFMState_Object = MibScalar
swL2DevCtrlCFMState = _SwL2DevCtrlCFMState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 29, 1),
    _SwL2DevCtrlCFMState_Type()
)
swL2DevCtrlCFMState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMState.setStatus("current")
_SwL2DevCtrlCFMPortTable_Object = MibTable
swL2DevCtrlCFMPortTable = _SwL2DevCtrlCFMPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 29, 2)
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortTable.setStatus("current")
_SwL2DevCtrlCFMPortEntry_Object = MibTableRow
swL2DevCtrlCFMPortEntry = _SwL2DevCtrlCFMPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 29, 2, 1)
)
swL2DevCtrlCFMPortEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2DevCtrlCFMPortIndex"),
)
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortEntry.setStatus("current")
_SwL2DevCtrlCFMPortIndex_Type = Integer32
_SwL2DevCtrlCFMPortIndex_Object = MibTableColumn
swL2DevCtrlCFMPortIndex = _SwL2DevCtrlCFMPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 29, 2, 1, 1),
    _SwL2DevCtrlCFMPortIndex_Type()
)
swL2DevCtrlCFMPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortIndex.setStatus("current")


class _SwL2DevCtrlCFMPortState_Type(Integer32):
    """Custom type swL2DevCtrlCFMPortState based on Integer32"""
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


_SwL2DevCtrlCFMPortState_Type.__name__ = "Integer32"
_SwL2DevCtrlCFMPortState_Object = MibTableColumn
swL2DevCtrlCFMPortState = _SwL2DevCtrlCFMPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 29, 2, 1, 2),
    _SwL2DevCtrlCFMPortState_Type()
)
swL2DevCtrlCFMPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlCFMPortState.setStatus("current")
_SwL2DevCtrlWeb_ObjectIdentity = ObjectIdentity
swL2DevCtrlWeb = _SwL2DevCtrlWeb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 30)
)


class _SwL2DevCtrlWebState_Type(Integer32):
    """Custom type swL2DevCtrlWebState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevCtrlWebState_Type.__name__ = "Integer32"
_SwL2DevCtrlWebState_Object = MibScalar
swL2DevCtrlWebState = _SwL2DevCtrlWebState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 2, 30, 1),
    _SwL2DevCtrlWebState_Type()
)
swL2DevCtrlWebState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevCtrlWebState.setStatus("current")
_SwL2DevAlarm_ObjectIdentity = ObjectIdentity
swL2DevAlarm = _SwL2DevAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 3)
)


class _SwL2DevAlarmLinkChange_Type(Integer32):
    """Custom type swL2DevAlarmLinkChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DevAlarmLinkChange_Type.__name__ = "Integer32"
_SwL2DevAlarmLinkChange_Object = MibScalar
swL2DevAlarmLinkChange = _SwL2DevAlarmLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 1, 3, 3),
    _SwL2DevAlarmLinkChange_Type()
)
swL2DevAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DevAlarmLinkChange.setStatus("current")
_SwL2PortMgmt_ObjectIdentity = ObjectIdentity
swL2PortMgmt = _SwL2PortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2)
)
_SwL2PortInfoTable_Object = MibTable
swL2PortInfoTable = _SwL2PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    swL2PortInfoTable.setStatus("current")
_SwL2PortInfoEntry_Object = MibTableRow
swL2PortInfoEntry = _SwL2PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 1, 1)
)
swL2PortInfoEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2PortInfoPortIndex"),
    (0, "DES3200-18-L2MGMT-MIB", "swL2PortInfoMediumType"),
)
if mibBuilder.loadTexts:
    swL2PortInfoEntry.setStatus("current")


class _SwL2PortInfoPortIndex_Type(Integer32):
    """Custom type swL2PortInfoPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2PortInfoPortIndex_Type.__name__ = "Integer32"
_SwL2PortInfoPortIndex_Object = MibTableColumn
swL2PortInfoPortIndex = _SwL2PortInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 1, 1, 1),
    _SwL2PortInfoPortIndex_Type()
)
swL2PortInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoPortIndex.setStatus("current")


class _SwL2PortInfoMediumType_Type(Integer32):
    """Custom type swL2PortInfoMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("copper", 100),
          ("fiber", 101))
    )


_SwL2PortInfoMediumType_Type.__name__ = "Integer32"
_SwL2PortInfoMediumType_Object = MibTableColumn
swL2PortInfoMediumType = _SwL2PortInfoMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 1, 1, 2),
    _SwL2PortInfoMediumType_Type()
)
swL2PortInfoMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoMediumType.setStatus("current")


class _SwL2PortInfoLinkStatus_Type(Integer32):
    """Custom type swL2PortInfoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-fail", 3),
          ("link-pass", 2),
          ("other", 1))
    )


_SwL2PortInfoLinkStatus_Type.__name__ = "Integer32"
_SwL2PortInfoLinkStatus_Object = MibTableColumn
swL2PortInfoLinkStatus = _SwL2PortInfoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 1, 1, 4),
    _SwL2PortInfoLinkStatus_Type()
)
swL2PortInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoLinkStatus.setStatus("current")


class _SwL2PortInfoNwayStatus_Type(Integer32):
    """Custom type swL2PortInfoNwayStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("full-100Mbps", 5),
          ("full-10Mbps", 3),
          ("full-1Gigabps", 7),
          ("half-100Mbps", 4),
          ("half-10Mbps", 2))
    )


_SwL2PortInfoNwayStatus_Type.__name__ = "Integer32"
_SwL2PortInfoNwayStatus_Object = MibTableColumn
swL2PortInfoNwayStatus = _SwL2PortInfoNwayStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 1, 1, 5),
    _SwL2PortInfoNwayStatus_Type()
)
swL2PortInfoNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoNwayStatus.setStatus("current")


class _SwL2PortInfoFlowCtrlOperStatus_Type(Integer32):
    """Custom type swL2PortInfoFlowCtrlOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backPressure", 3),
          ("ieee8023x", 2),
          ("none", 1))
    )


_SwL2PortInfoFlowCtrlOperStatus_Type.__name__ = "Integer32"
_SwL2PortInfoFlowCtrlOperStatus_Object = MibTableColumn
swL2PortInfoFlowCtrlOperStatus = _SwL2PortInfoFlowCtrlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 1, 1, 10),
    _SwL2PortInfoFlowCtrlOperStatus_Type()
)
swL2PortInfoFlowCtrlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortInfoFlowCtrlOperStatus.setStatus("current")
_SwL2PortCtrlTable_Object = MibTable
swL2PortCtrlTable = _SwL2PortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    swL2PortCtrlTable.setStatus("current")
_SwL2PortCtrlEntry_Object = MibTableRow
swL2PortCtrlEntry = _SwL2PortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2, 1)
)
swL2PortCtrlEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2PortCtrlPortIndex"),
    (0, "DES3200-18-L2MGMT-MIB", "swL2PortCtrlPortMediumType"),
)
if mibBuilder.loadTexts:
    swL2PortCtrlEntry.setStatus("current")


class _SwL2PortCtrlPortIndex_Type(Integer32):
    """Custom type swL2PortCtrlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2PortCtrlPortIndex_Type.__name__ = "Integer32"
_SwL2PortCtrlPortIndex_Object = MibTableColumn
swL2PortCtrlPortIndex = _SwL2PortCtrlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2, 1, 1),
    _SwL2PortCtrlPortIndex_Type()
)
swL2PortCtrlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlPortIndex.setStatus("current")


class _SwL2PortCtrlPortMediumType_Type(Integer32):
    """Custom type swL2PortCtrlPortMediumType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("copper", 100),
          ("fiber", 101))
    )


_SwL2PortCtrlPortMediumType_Type.__name__ = "Integer32"
_SwL2PortCtrlPortMediumType_Object = MibTableColumn
swL2PortCtrlPortMediumType = _SwL2PortCtrlPortMediumType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2, 1, 2),
    _SwL2PortCtrlPortMediumType_Type()
)
swL2PortCtrlPortMediumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlPortMediumType.setStatus("current")


class _SwL2PortCtrlAdminState_Type(Integer32):
    """Custom type swL2PortCtrlAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2PortCtrlAdminState_Type.__name__ = "Integer32"
_SwL2PortCtrlAdminState_Object = MibTableColumn
swL2PortCtrlAdminState = _SwL2PortCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2, 1, 3),
    _SwL2PortCtrlAdminState_Type()
)
swL2PortCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAdminState.setStatus("current")


class _SwL2PortCtrlNwayState_Type(Integer32):
    """Custom type swL2PortCtrlNwayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("nway-auto", 1),
          ("nway-disabled-100Mbps-Full", 5),
          ("nway-disabled-100Mbps-Half", 4),
          ("nway-disabled-10Mbps-Full", 3),
          ("nway-disabled-10Mbps-Half", 2),
          ("nway-disabled-1Gigabps-Full", 7),
          ("nway-disabled-1Gigabps-Full-Master", 8),
          ("nway-disabled-1Gigabps-Full-Slave", 9))
    )


_SwL2PortCtrlNwayState_Type.__name__ = "Integer32"
_SwL2PortCtrlNwayState_Object = MibTableColumn
swL2PortCtrlNwayState = _SwL2PortCtrlNwayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2, 1, 4),
    _SwL2PortCtrlNwayState_Type()
)
swL2PortCtrlNwayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlNwayState.setStatus("current")


class _SwL2PortCtrlFlowCtrlState_Type(Integer32):
    """Custom type swL2PortCtrlFlowCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2PortCtrlFlowCtrlState_Type.__name__ = "Integer32"
_SwL2PortCtrlFlowCtrlState_Object = MibTableColumn
swL2PortCtrlFlowCtrlState = _SwL2PortCtrlFlowCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2, 1, 5),
    _SwL2PortCtrlFlowCtrlState_Type()
)
swL2PortCtrlFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlFlowCtrlState.setStatus("current")


class _SwL2PortCtrlDescription_Type(DisplayString):
    """Custom type swL2PortCtrlDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2PortCtrlDescription_Type.__name__ = "DisplayString"
_SwL2PortCtrlDescription_Object = MibTableColumn
swL2PortCtrlDescription = _SwL2PortCtrlDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2, 1, 6),
    _SwL2PortCtrlDescription_Type()
)
swL2PortCtrlDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlDescription.setStatus("current")


class _SwL2PortCtrlAddressLearning_Type(Integer32):
    """Custom type swL2PortCtrlAddressLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2PortCtrlAddressLearning_Type.__name__ = "Integer32"
_SwL2PortCtrlAddressLearning_Object = MibTableColumn
swL2PortCtrlAddressLearning = _SwL2PortCtrlAddressLearning_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2, 1, 7),
    _SwL2PortCtrlAddressLearning_Type()
)
swL2PortCtrlAddressLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlAddressLearning.setStatus("current")


class _SwL2PortCtrlMACNotifyState_Type(Integer32):
    """Custom type swL2PortCtrlMACNotifyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2PortCtrlMACNotifyState_Type.__name__ = "Integer32"
_SwL2PortCtrlMACNotifyState_Object = MibTableColumn
swL2PortCtrlMACNotifyState = _SwL2PortCtrlMACNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2, 1, 8),
    _SwL2PortCtrlMACNotifyState_Type()
)
swL2PortCtrlMACNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlMACNotifyState.setStatus("current")


class _SwL2PortCtrlMulticastfilter_Type(Integer32):
    """Custom type swL2PortCtrlMulticastfilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter-unregistered-groups", 3),
          ("forward-unregistered-groups", 2))
    )


_SwL2PortCtrlMulticastfilter_Type.__name__ = "Integer32"
_SwL2PortCtrlMulticastfilter_Object = MibTableColumn
swL2PortCtrlMulticastfilter = _SwL2PortCtrlMulticastfilter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2, 1, 9),
    _SwL2PortCtrlMulticastfilter_Type()
)
swL2PortCtrlMulticastfilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlMulticastfilter.setStatus("current")


class _SwL2PortCtrlMDIXState_Type(Integer32):
    """Custom type swL2PortCtrlMDIXState based on Integer32"""
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
        *(("auto", 1),
          ("cross", 3),
          ("normal", 2),
          ("other", 4))
    )


_SwL2PortCtrlMDIXState_Type.__name__ = "Integer32"
_SwL2PortCtrlMDIXState_Object = MibTableColumn
swL2PortCtrlMDIXState = _SwL2PortCtrlMDIXState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 2, 1, 10),
    _SwL2PortCtrlMDIXState_Type()
)
swL2PortCtrlMDIXState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlMDIXState.setStatus("current")
_SwL2PortErrTable_Object = MibTable
swL2PortErrTable = _SwL2PortErrTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 3)
)
if mibBuilder.loadTexts:
    swL2PortErrTable.setStatus("current")
_SwL2PortErrEntry_Object = MibTableRow
swL2PortErrEntry = _SwL2PortErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 3, 1)
)
swL2PortErrEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2PortErrPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortErrEntry.setStatus("current")


class _SwL2PortErrPortIndex_Type(Integer32):
    """Custom type swL2PortErrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2PortErrPortIndex_Type.__name__ = "Integer32"
_SwL2PortErrPortIndex_Object = MibTableColumn
swL2PortErrPortIndex = _SwL2PortErrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 3, 1, 1),
    _SwL2PortErrPortIndex_Type()
)
swL2PortErrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortIndex.setStatus("current")


class _SwL2PortErrPortState_Type(Integer32):
    """Custom type swL2PortErrPortState based on Integer32"""
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


_SwL2PortErrPortState_Type.__name__ = "Integer32"
_SwL2PortErrPortState_Object = MibTableColumn
swL2PortErrPortState = _SwL2PortErrPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 3, 1, 2),
    _SwL2PortErrPortState_Type()
)
swL2PortErrPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortState.setStatus("current")


class _SwL2PortErrPortStatus_Type(Integer32):
    """Custom type swL2PortErrPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("err-disabled", 2),
          ("other", 1))
    )


_SwL2PortErrPortStatus_Type.__name__ = "Integer32"
_SwL2PortErrPortStatus_Object = MibTableColumn
swL2PortErrPortStatus = _SwL2PortErrPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 3, 1, 3),
    _SwL2PortErrPortStatus_Type()
)
swL2PortErrPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortStatus.setStatus("current")


class _SwL2PortErrPortReason_Type(Integer32):
    """Custom type swL2PortErrPortReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ddm", 5),
          ("loopdetect", 4),
          ("none", 0),
          ("storm-control", 2),
          ("storm-control-lbd", 3),
          ("stp-lbd", 1))
    )


_SwL2PortErrPortReason_Type.__name__ = "Integer32"
_SwL2PortErrPortReason_Object = MibTableColumn
swL2PortErrPortReason = _SwL2PortErrPortReason_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 3, 1, 4),
    _SwL2PortErrPortReason_Type()
)
swL2PortErrPortReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrPortReason.setStatus("current")


class _SwL2PortErrDescription_Type(DisplayString):
    """Custom type swL2PortErrDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2PortErrDescription_Type.__name__ = "DisplayString"
_SwL2PortErrDescription_Object = MibTableColumn
swL2PortErrDescription = _SwL2PortErrDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 3, 1, 5),
    _SwL2PortErrDescription_Type()
)
swL2PortErrDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortErrDescription.setStatus("current")


class _SwL2PortCtrlJumboFrame_Type(Integer32):
    """Custom type swL2PortCtrlJumboFrame based on Integer32"""
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


_SwL2PortCtrlJumboFrame_Type.__name__ = "Integer32"
_SwL2PortCtrlJumboFrame_Object = MibScalar
swL2PortCtrlJumboFrame = _SwL2PortCtrlJumboFrame_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 4),
    _SwL2PortCtrlJumboFrame_Type()
)
swL2PortCtrlJumboFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortCtrlJumboFrame.setStatus("current")
_SwL2PortCtrlJumboFrameMaxSize_Type = Integer32
_SwL2PortCtrlJumboFrameMaxSize_Object = MibScalar
swL2PortCtrlJumboFrameMaxSize = _SwL2PortCtrlJumboFrameMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 2, 5),
    _SwL2PortCtrlJumboFrameMaxSize_Type()
)
swL2PortCtrlJumboFrameMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortCtrlJumboFrameMaxSize.setStatus("current")
_SwL2QOSMgmt_ObjectIdentity = ObjectIdentity
swL2QOSMgmt = _SwL2QOSMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3)
)
_SwL2QOSBandwidthControlTable_Object = MibTable
swL2QOSBandwidthControlTable = _SwL2QOSBandwidthControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    swL2QOSBandwidthControlTable.setStatus("current")
_SwL2QOSBandwidthControlEntry_Object = MibTableRow
swL2QOSBandwidthControlEntry = _SwL2QOSBandwidthControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 1, 1)
)
swL2QOSBandwidthControlEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2QOSBandwidthPortIndex"),
)
if mibBuilder.loadTexts:
    swL2QOSBandwidthControlEntry.setStatus("current")


class _SwL2QOSBandwidthPortIndex_Type(Integer32):
    """Custom type swL2QOSBandwidthPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 650),
    )


_SwL2QOSBandwidthPortIndex_Type.__name__ = "Integer32"
_SwL2QOSBandwidthPortIndex_Object = MibTableColumn
swL2QOSBandwidthPortIndex = _SwL2QOSBandwidthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 1, 1, 1),
    _SwL2QOSBandwidthPortIndex_Type()
)
swL2QOSBandwidthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthPortIndex.setStatus("current")


class _SwL2QOSBandwidthRxRate_Type(Integer32):
    """Custom type swL2QOSBandwidthRxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024000),
    )


_SwL2QOSBandwidthRxRate_Type.__name__ = "Integer32"
_SwL2QOSBandwidthRxRate_Object = MibTableColumn
swL2QOSBandwidthRxRate = _SwL2QOSBandwidthRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 1, 1, 2),
    _SwL2QOSBandwidthRxRate_Type()
)
swL2QOSBandwidthRxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRxRate.setStatus("current")


class _SwL2QOSBandwidthTxRate_Type(Integer32):
    """Custom type swL2QOSBandwidthTxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1024000),
    )


_SwL2QOSBandwidthTxRate_Type.__name__ = "Integer32"
_SwL2QOSBandwidthTxRate_Object = MibTableColumn
swL2QOSBandwidthTxRate = _SwL2QOSBandwidthTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 1, 1, 3),
    _SwL2QOSBandwidthTxRate_Type()
)
swL2QOSBandwidthTxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSBandwidthTxRate.setStatus("current")
_SwL2QOSBandwidthRadiusRxRate_Type = Integer32
_SwL2QOSBandwidthRadiusRxRate_Object = MibTableColumn
swL2QOSBandwidthRadiusRxRate = _SwL2QOSBandwidthRadiusRxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 1, 1, 4),
    _SwL2QOSBandwidthRadiusRxRate_Type()
)
swL2QOSBandwidthRadiusRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRadiusRxRate.setStatus("current")
_SwL2QOSBandwidthRadiusTxRate_Type = Integer32
_SwL2QOSBandwidthRadiusTxRate_Object = MibTableColumn
swL2QOSBandwidthRadiusTxRate = _SwL2QOSBandwidthRadiusTxRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 1, 1, 5),
    _SwL2QOSBandwidthRadiusTxRate_Type()
)
swL2QOSBandwidthRadiusTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSBandwidthRadiusTxRate.setStatus("current")
_SwL2QOSSchedulingTable_Object = MibTable
swL2QOSSchedulingTable = _SwL2QOSSchedulingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 2)
)
if mibBuilder.loadTexts:
    swL2QOSSchedulingTable.setStatus("current")
_SwL2QOSSchedulingEntry_Object = MibTableRow
swL2QOSSchedulingEntry = _SwL2QOSSchedulingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 2, 1)
)
swL2QOSSchedulingEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2QOSSchedulingClassIndex"),
)
if mibBuilder.loadTexts:
    swL2QOSSchedulingEntry.setStatus("current")


class _SwL2QOSSchedulingClassIndex_Type(Integer32):
    """Custom type swL2QOSSchedulingClassIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2QOSSchedulingClassIndex_Type.__name__ = "Integer32"
_SwL2QOSSchedulingClassIndex_Object = MibTableColumn
swL2QOSSchedulingClassIndex = _SwL2QOSSchedulingClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 2, 1, 1),
    _SwL2QOSSchedulingClassIndex_Type()
)
swL2QOSSchedulingClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSSchedulingClassIndex.setStatus("current")


class _SwL2QOSSchedulingMaxWeight_Type(Integer32):
    """Custom type swL2QOSSchedulingMaxWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 55),
    )


_SwL2QOSSchedulingMaxWeight_Type.__name__ = "Integer32"
_SwL2QOSSchedulingMaxWeight_Object = MibTableColumn
swL2QOSSchedulingMaxWeight = _SwL2QOSSchedulingMaxWeight_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 2, 1, 4),
    _SwL2QOSSchedulingMaxWeight_Type()
)
swL2QOSSchedulingMaxWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSSchedulingMaxWeight.setStatus("current")


class _SwL2QOSSchedulingMechanism_Type(Integer32):
    """Custom type swL2QOSSchedulingMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("roundrobin", 2),
          ("strict", 1),
          ("weightfair", 3))
    )


_SwL2QOSSchedulingMechanism_Type.__name__ = "Integer32"
_SwL2QOSSchedulingMechanism_Object = MibTableColumn
swL2QOSSchedulingMechanism = _SwL2QOSSchedulingMechanism_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 2, 1, 5),
    _SwL2QOSSchedulingMechanism_Type()
)
swL2QOSSchedulingMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOSSchedulingMechanism.setStatus("current")
_SwL2QOS8021pUserPriorityTable_Object = MibTable
swL2QOS8021pUserPriorityTable = _SwL2QOS8021pUserPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 3)
)
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityTable.setStatus("current")
_SwL2QOS8021pUserPriorityEntry_Object = MibTableRow
swL2QOS8021pUserPriorityEntry = _SwL2QOS8021pUserPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 3, 1)
)
swL2QOS8021pUserPriorityEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2QOS8021pUserPriorityIndex"),
)
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityEntry.setStatus("current")


class _SwL2QOS8021pUserPriorityIndex_Type(Integer32):
    """Custom type swL2QOS8021pUserPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2QOS8021pUserPriorityIndex_Type.__name__ = "Integer32"
_SwL2QOS8021pUserPriorityIndex_Object = MibTableColumn
swL2QOS8021pUserPriorityIndex = _SwL2QOS8021pUserPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 3, 1, 1),
    _SwL2QOS8021pUserPriorityIndex_Type()
)
swL2QOS8021pUserPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityIndex.setStatus("current")


class _SwL2QOS8021pUserPriorityClass_Type(Integer32):
    """Custom type swL2QOS8021pUserPriorityClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2QOS8021pUserPriorityClass_Type.__name__ = "Integer32"
_SwL2QOS8021pUserPriorityClass_Object = MibTableColumn
swL2QOS8021pUserPriorityClass = _SwL2QOS8021pUserPriorityClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 3, 1, 2),
    _SwL2QOS8021pUserPriorityClass_Type()
)
swL2QOS8021pUserPriorityClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOS8021pUserPriorityClass.setStatus("current")
_SwL2QOS8021pDefaultPriorityTable_Object = MibTable
swL2QOS8021pDefaultPriorityTable = _SwL2QOS8021pDefaultPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 4)
)
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityTable.setStatus("current")
_SwL2QOS8021pDefaultPriorityEntry_Object = MibTableRow
swL2QOS8021pDefaultPriorityEntry = _SwL2QOS8021pDefaultPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 4, 1)
)
swL2QOS8021pDefaultPriorityEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2QOS8021pDefaultPriorityIndex"),
)
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityEntry.setStatus("current")


class _SwL2QOS8021pDefaultPriorityIndex_Type(Integer32):
    """Custom type swL2QOS8021pDefaultPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 650),
    )


_SwL2QOS8021pDefaultPriorityIndex_Type.__name__ = "Integer32"
_SwL2QOS8021pDefaultPriorityIndex_Object = MibTableColumn
swL2QOS8021pDefaultPriorityIndex = _SwL2QOS8021pDefaultPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 4, 1, 1),
    _SwL2QOS8021pDefaultPriorityIndex_Type()
)
swL2QOS8021pDefaultPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriorityIndex.setStatus("current")


class _SwL2QOS8021pDefaultPriority_Type(Integer32):
    """Custom type swL2QOS8021pDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2QOS8021pDefaultPriority_Type.__name__ = "Integer32"
_SwL2QOS8021pDefaultPriority_Object = MibTableColumn
swL2QOS8021pDefaultPriority = _SwL2QOS8021pDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 4, 1, 2),
    _SwL2QOS8021pDefaultPriority_Type()
)
swL2QOS8021pDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOS8021pDefaultPriority.setStatus("current")
_SwL2QOS8021pRadiusPriority_Type = Integer32
_SwL2QOS8021pRadiusPriority_Object = MibTableColumn
swL2QOS8021pRadiusPriority = _SwL2QOS8021pRadiusPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 4, 1, 3),
    _SwL2QOS8021pRadiusPriority_Type()
)
swL2QOS8021pRadiusPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2QOS8021pRadiusPriority.setStatus("current")


class _SwL2QOSSchedulingMechanismCtrl_Type(Integer32):
    """Custom type swL2QOSSchedulingMechanismCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("strict", 1),
          ("weightfair", 2))
    )


_SwL2QOSSchedulingMechanismCtrl_Type.__name__ = "Integer32"
_SwL2QOSSchedulingMechanismCtrl_Object = MibScalar
swL2QOSSchedulingMechanismCtrl = _SwL2QOSSchedulingMechanismCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 3, 5),
    _SwL2QOSSchedulingMechanismCtrl_Type()
)
swL2QOSSchedulingMechanismCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2QOSSchedulingMechanismCtrl.setStatus("current")
_SwL2TrunkMgmt_ObjectIdentity = ObjectIdentity
swL2TrunkMgmt = _SwL2TrunkMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4)
)
_SwPortTrunkMaxEntries_Type = Integer32
_SwPortTrunkMaxEntries_Object = MibScalar
swPortTrunkMaxEntries = _SwPortTrunkMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 1),
    _SwPortTrunkMaxEntries_Type()
)
swPortTrunkMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMaxEntries.setStatus("current")
_SwPortTrunkMaxPortMembers_Type = Integer32
_SwPortTrunkMaxPortMembers_Object = MibScalar
swPortTrunkMaxPortMembers = _SwPortTrunkMaxPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 2),
    _SwPortTrunkMaxPortMembers_Type()
)
swPortTrunkMaxPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMaxPortMembers.setStatus("current")
_SwPortTrunkTable_Object = MibTable
swPortTrunkTable = _SwPortTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 3)
)
if mibBuilder.loadTexts:
    swPortTrunkTable.setStatus("current")
_SwPortTrunkEntry_Object = MibTableRow
swPortTrunkEntry = _SwPortTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 3, 1)
)
swPortTrunkEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swPortTrunkIndex"),
)
if mibBuilder.loadTexts:
    swPortTrunkEntry.setStatus("current")


class _SwPortTrunkIndex_Type(Integer32):
    """Custom type swPortTrunkIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SwPortTrunkIndex_Type.__name__ = "Integer32"
_SwPortTrunkIndex_Object = MibTableColumn
swPortTrunkIndex = _SwPortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 3, 1, 1),
    _SwPortTrunkIndex_Type()
)
swPortTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkIndex.setStatus("current")
_SwPortTrunkMasterPort_Type = Integer32
_SwPortTrunkMasterPort_Object = MibTableColumn
swPortTrunkMasterPort = _SwPortTrunkMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 3, 1, 2),
    _SwPortTrunkMasterPort_Type()
)
swPortTrunkMasterPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortTrunkMasterPort.setStatus("current")
_SwPortTrunkPortList_Type = PortList
_SwPortTrunkPortList_Object = MibTableColumn
swPortTrunkPortList = _SwPortTrunkPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 3, 1, 3),
    _SwPortTrunkPortList_Type()
)
swPortTrunkPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortTrunkPortList.setStatus("current")


class _SwPortTrunkType_Type(Integer32):
    """Custom type swPortTrunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 2),
          ("static", 1))
    )


_SwPortTrunkType_Type.__name__ = "Integer32"
_SwPortTrunkType_Object = MibTableColumn
swPortTrunkType = _SwPortTrunkType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 3, 1, 4),
    _SwPortTrunkType_Type()
)
swPortTrunkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortTrunkType.setStatus("current")
_SwPortTrunkActivePort_Type = PortList
_SwPortTrunkActivePort_Object = MibTableColumn
swPortTrunkActivePort = _SwPortTrunkActivePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 3, 1, 5),
    _SwPortTrunkActivePort_Type()
)
swPortTrunkActivePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkActivePort.setStatus("current")
_SwPortTrunkState_Type = RowStatus
_SwPortTrunkState_Object = MibTableColumn
swPortTrunkState = _SwPortTrunkState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 3, 1, 6),
    _SwPortTrunkState_Type()
)
swPortTrunkState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPortTrunkState.setStatus("current")
_SwPortTrunkFloodingPort_Type = Integer32
_SwPortTrunkFloodingPort_Object = MibTableColumn
swPortTrunkFloodingPort = _SwPortTrunkFloodingPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 3, 1, 7),
    _SwPortTrunkFloodingPort_Type()
)
swPortTrunkFloodingPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkFloodingPort.setStatus("current")


class _SwL2TrunkAlgorithm_Type(Integer32):
    """Custom type swL2TrunkAlgorithm based on Integer32"""
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
        *(("ip-destination", 6),
          ("ip-source", 5),
          ("ip-source-dest", 7),
          ("mac-destination", 3),
          ("mac-source", 2),
          ("mac-source-dest", 4),
          ("other", 1))
    )


_SwL2TrunkAlgorithm_Type.__name__ = "Integer32"
_SwL2TrunkAlgorithm_Object = MibScalar
swL2TrunkAlgorithm = _SwL2TrunkAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 4),
    _SwL2TrunkAlgorithm_Type()
)
swL2TrunkAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkAlgorithm.setStatus("current")
_SwL2TrunkLACPPortTable_Object = MibTable
swL2TrunkLACPPortTable = _SwL2TrunkLACPPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 5)
)
if mibBuilder.loadTexts:
    swL2TrunkLACPPortTable.setStatus("current")
_SwL2TrunkLACPPortEntry_Object = MibTableRow
swL2TrunkLACPPortEntry = _SwL2TrunkLACPPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 5, 1)
)
swL2TrunkLACPPortEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2TrunkLACPPortIndex"),
)
if mibBuilder.loadTexts:
    swL2TrunkLACPPortEntry.setStatus("current")


class _SwL2TrunkLACPPortIndex_Type(Integer32):
    """Custom type swL2TrunkLACPPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrunkLACPPortIndex_Type.__name__ = "Integer32"
_SwL2TrunkLACPPortIndex_Object = MibTableColumn
swL2TrunkLACPPortIndex = _SwL2TrunkLACPPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 5, 1, 1),
    _SwL2TrunkLACPPortIndex_Type()
)
swL2TrunkLACPPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkLACPPortIndex.setStatus("current")


class _SwL2TrunkLACPPortState_Type(Integer32):
    """Custom type swL2TrunkLACPPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_SwL2TrunkLACPPortState_Type.__name__ = "Integer32"
_SwL2TrunkLACPPortState_Object = MibTableColumn
swL2TrunkLACPPortState = _SwL2TrunkLACPPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 5, 1, 2),
    _SwL2TrunkLACPPortState_Type()
)
swL2TrunkLACPPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkLACPPortState.setStatus("current")
_SwL2TrunkVLANTable_Object = MibTable
swL2TrunkVLANTable = _SwL2TrunkVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 6)
)
if mibBuilder.loadTexts:
    swL2TrunkVLANTable.setStatus("current")
_SwL2TrunkVLANEntry_Object = MibTableRow
swL2TrunkVLANEntry = _SwL2TrunkVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 6, 1)
)
swL2TrunkVLANEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2TrunkVLANPort"),
)
if mibBuilder.loadTexts:
    swL2TrunkVLANEntry.setStatus("current")


class _SwL2TrunkVLANPort_Type(Integer32):
    """Custom type swL2TrunkVLANPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrunkVLANPort_Type.__name__ = "Integer32"
_SwL2TrunkVLANPort_Object = MibTableColumn
swL2TrunkVLANPort = _SwL2TrunkVLANPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 6, 1, 1),
    _SwL2TrunkVLANPort_Type()
)
swL2TrunkVLANPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrunkVLANPort.setStatus("current")


class _SwL2TrunkVLANState_Type(Integer32):
    """Custom type swL2TrunkVLANState based on Integer32"""
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


_SwL2TrunkVLANState_Type.__name__ = "Integer32"
_SwL2TrunkVLANState_Object = MibTableColumn
swL2TrunkVLANState = _SwL2TrunkVLANState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 4, 6, 1, 2),
    _SwL2TrunkVLANState_Type()
)
swL2TrunkVLANState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrunkVLANState.setStatus("current")
_SwPortMirrorPackage_ObjectIdentity = ObjectIdentity
swPortMirrorPackage = _SwPortMirrorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 6)
)
_SwPortMirrorRxPortList_Type = PortList
_SwPortMirrorRxPortList_Object = MibScalar
swPortMirrorRxPortList = _SwPortMirrorRxPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 6, 2),
    _SwPortMirrorRxPortList_Type()
)
swPortMirrorRxPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorRxPortList.setStatus("current")
_SwPortMirrorTxPortList_Type = PortList
_SwPortMirrorTxPortList_Object = MibScalar
swPortMirrorTxPortList = _SwPortMirrorTxPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 6, 3),
    _SwPortMirrorTxPortList_Type()
)
swPortMirrorTxPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorTxPortList.setStatus("current")
_SwPortMirrorTargetPort_Type = Integer32
_SwPortMirrorTargetPort_Object = MibScalar
swPortMirrorTargetPort = _SwPortMirrorTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 6, 4),
    _SwPortMirrorTargetPort_Type()
)
swPortMirrorTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorTargetPort.setStatus("current")


class _SwPortMirrorState_Type(Integer32):
    """Custom type swPortMirrorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwPortMirrorState_Type.__name__ = "Integer32"
_SwPortMirrorState_Object = MibScalar
swPortMirrorState = _SwPortMirrorState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 6, 5),
    _SwPortMirrorState_Type()
)
swPortMirrorState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortMirrorState.setStatus("current")
_SwIGMPPackage_ObjectIdentity = ObjectIdentity
swIGMPPackage = _SwIGMPPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7)
)


class _SwL2IGMPMaxSupportedVlans_Type(Integer32):
    """Custom type swL2IGMPMaxSupportedVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPMaxSupportedVlans_Type.__name__ = "Integer32"
_SwL2IGMPMaxSupportedVlans_Object = MibScalar
swL2IGMPMaxSupportedVlans = _SwL2IGMPMaxSupportedVlans_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 1),
    _SwL2IGMPMaxSupportedVlans_Type()
)
swL2IGMPMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMaxSupportedVlans.setStatus("current")


class _SwL2IGMPMaxIpGroupNumPerVlan_Type(Integer32):
    """Custom type swL2IGMPMaxIpGroupNumPerVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPMaxIpGroupNumPerVlan_Type.__name__ = "Integer32"
_SwL2IGMPMaxIpGroupNumPerVlan_Object = MibScalar
swL2IGMPMaxIpGroupNumPerVlan = _SwL2IGMPMaxIpGroupNumPerVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 2),
    _SwL2IGMPMaxIpGroupNumPerVlan_Type()
)
swL2IGMPMaxIpGroupNumPerVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMaxIpGroupNumPerVlan.setStatus("current")
_SwL2IGMPCtrlTable_Object = MibTable
swL2IGMPCtrlTable = _SwL2IGMPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3)
)
if mibBuilder.loadTexts:
    swL2IGMPCtrlTable.setStatus("current")
_SwL2IGMPCtrlEntry_Object = MibTableRow
swL2IGMPCtrlEntry = _SwL2IGMPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3, 1)
)
swL2IGMPCtrlEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2IGMPCtrlVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPCtrlEntry.setStatus("current")


class _SwL2IGMPCtrlVid_Type(Integer32):
    """Custom type swL2IGMPCtrlVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPCtrlVid_Type.__name__ = "Integer32"
_SwL2IGMPCtrlVid_Object = MibTableColumn
swL2IGMPCtrlVid = _SwL2IGMPCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3, 1, 1),
    _SwL2IGMPCtrlVid_Type()
)
swL2IGMPCtrlVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPCtrlVid.setStatus("current")


class _SwL2IGMPQueryInterval_Type(Integer32):
    """Custom type swL2IGMPQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2IGMPQueryInterval_Type.__name__ = "Integer32"
_SwL2IGMPQueryInterval_Object = MibTableColumn
swL2IGMPQueryInterval = _SwL2IGMPQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3, 1, 2),
    _SwL2IGMPQueryInterval_Type()
)
swL2IGMPQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPQueryInterval.setStatus("current")


class _SwL2IGMPMaxResponseTime_Type(Integer32):
    """Custom type swL2IGMPMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_SwL2IGMPMaxResponseTime_Type.__name__ = "Integer32"
_SwL2IGMPMaxResponseTime_Object = MibTableColumn
swL2IGMPMaxResponseTime = _SwL2IGMPMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3, 1, 3),
    _SwL2IGMPMaxResponseTime_Type()
)
swL2IGMPMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMaxResponseTime.setStatus("current")


class _SwL2IGMPRobustness_Type(Integer32):
    """Custom type swL2IGMPRobustness based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2IGMPRobustness_Type.__name__ = "Integer32"
_SwL2IGMPRobustness_Object = MibTableColumn
swL2IGMPRobustness = _SwL2IGMPRobustness_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3, 1, 4),
    _SwL2IGMPRobustness_Type()
)
swL2IGMPRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRobustness.setStatus("current")


class _SwL2IGMPLastMemberQueryInterval_Type(Integer32):
    """Custom type swL2IGMPLastMemberQueryInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_SwL2IGMPLastMemberQueryInterval_Type.__name__ = "Integer32"
_SwL2IGMPLastMemberQueryInterval_Object = MibTableColumn
swL2IGMPLastMemberQueryInterval = _SwL2IGMPLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3, 1, 5),
    _SwL2IGMPLastMemberQueryInterval_Type()
)
swL2IGMPLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPLastMemberQueryInterval.setStatus("current")


class _SwL2IGMPQueryState_Type(Integer32):
    """Custom type swL2IGMPQueryState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2IGMPQueryState_Type.__name__ = "Integer32"
_SwL2IGMPQueryState_Object = MibTableColumn
swL2IGMPQueryState = _SwL2IGMPQueryState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3, 1, 9),
    _SwL2IGMPQueryState_Type()
)
swL2IGMPQueryState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPQueryState.setStatus("current")


class _SwL2IGMPCurrentState_Type(Integer32):
    """Custom type swL2IGMPCurrentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("non-querier", 3),
          ("other", 1),
          ("querier", 2))
    )


_SwL2IGMPCurrentState_Type.__name__ = "Integer32"
_SwL2IGMPCurrentState_Object = MibTableColumn
swL2IGMPCurrentState = _SwL2IGMPCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3, 1, 10),
    _SwL2IGMPCurrentState_Type()
)
swL2IGMPCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPCurrentState.setStatus("current")


class _SwL2IGMPCtrlState_Type(Integer32):
    """Custom type swL2IGMPCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SwL2IGMPCtrlState_Type.__name__ = "Integer32"
_SwL2IGMPCtrlState_Object = MibTableColumn
swL2IGMPCtrlState = _SwL2IGMPCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3, 1, 11),
    _SwL2IGMPCtrlState_Type()
)
swL2IGMPCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPCtrlState.setStatus("current")


class _SwL2IGMPFastLeave_Type(Integer32):
    """Custom type swL2IGMPFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SwL2IGMPFastLeave_Type.__name__ = "Integer32"
_SwL2IGMPFastLeave_Object = MibTableColumn
swL2IGMPFastLeave = _SwL2IGMPFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3, 1, 12),
    _SwL2IGMPFastLeave_Type()
)
swL2IGMPFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPFastLeave.setStatus("current")


class _SwL2IGMPDynIPMultVlanAge_Type(Integer32):
    """Custom type swL2IGMPDynIPMultVlanAge based on Integer32"""
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


_SwL2IGMPDynIPMultVlanAge_Type.__name__ = "Integer32"
_SwL2IGMPDynIPMultVlanAge_Object = MibTableColumn
swL2IGMPDynIPMultVlanAge = _SwL2IGMPDynIPMultVlanAge_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 3, 1, 14),
    _SwL2IGMPDynIPMultVlanAge_Type()
)
swL2IGMPDynIPMultVlanAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPDynIPMultVlanAge.setStatus("current")
_SwL2IGMPQueryInfoTable_Object = MibTable
swL2IGMPQueryInfoTable = _SwL2IGMPQueryInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 4)
)
if mibBuilder.loadTexts:
    swL2IGMPQueryInfoTable.setStatus("current")
_SwL2IGMPQueryInfoEntry_Object = MibTableRow
swL2IGMPQueryInfoEntry = _SwL2IGMPQueryInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 4, 1)
)
swL2IGMPQueryInfoEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2IGMPInfoVid"),
)
if mibBuilder.loadTexts:
    swL2IGMPQueryInfoEntry.setStatus("current")


class _SwL2IGMPInfoVid_Type(Integer32):
    """Custom type swL2IGMPInfoVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPInfoVid_Type.__name__ = "Integer32"
_SwL2IGMPInfoVid_Object = MibTableColumn
swL2IGMPInfoVid = _SwL2IGMPInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 4, 1, 1),
    _SwL2IGMPInfoVid_Type()
)
swL2IGMPInfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoVid.setStatus("current")


class _SwL2IGMPInfoQueryCount_Type(Integer32):
    """Custom type swL2IGMPInfoQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPInfoQueryCount_Type.__name__ = "Integer32"
_SwL2IGMPInfoQueryCount_Object = MibTableColumn
swL2IGMPInfoQueryCount = _SwL2IGMPInfoQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 4, 1, 2),
    _SwL2IGMPInfoQueryCount_Type()
)
swL2IGMPInfoQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoQueryCount.setStatus("current")


class _SwL2IGMPInfoTxQueryCount_Type(Integer32):
    """Custom type swL2IGMPInfoTxQueryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2IGMPInfoTxQueryCount_Type.__name__ = "Integer32"
_SwL2IGMPInfoTxQueryCount_Object = MibTableColumn
swL2IGMPInfoTxQueryCount = _SwL2IGMPInfoTxQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 4, 1, 3),
    _SwL2IGMPInfoTxQueryCount_Type()
)
swL2IGMPInfoTxQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPInfoTxQueryCount.setStatus("current")
_SwL2IGMPRouterPortTable_Object = MibTable
swL2IGMPRouterPortTable = _SwL2IGMPRouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 6)
)
if mibBuilder.loadTexts:
    swL2IGMPRouterPortTable.setStatus("current")
_SwL2IGMPRouterPortEntry_Object = MibTableRow
swL2IGMPRouterPortEntry = _SwL2IGMPRouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 6, 1)
)
swL2IGMPRouterPortEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2IGMPRouterPortVlanid"),
)
if mibBuilder.loadTexts:
    swL2IGMPRouterPortEntry.setStatus("current")


class _SwL2IGMPRouterPortVlanid_Type(Integer32):
    """Custom type swL2IGMPRouterPortVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2IGMPRouterPortVlanid_Type.__name__ = "Integer32"
_SwL2IGMPRouterPortVlanid_Object = MibTableColumn
swL2IGMPRouterPortVlanid = _SwL2IGMPRouterPortVlanid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 6, 1, 1),
    _SwL2IGMPRouterPortVlanid_Type()
)
swL2IGMPRouterPortVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortVlanid.setStatus("current")


class _SwL2IGMPRouterPortVlanName_Type(SnmpAdminString):
    """Custom type swL2IGMPRouterPortVlanName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2IGMPRouterPortVlanName_Type.__name__ = "SnmpAdminString"
_SwL2IGMPRouterPortVlanName_Object = MibTableColumn
swL2IGMPRouterPortVlanName = _SwL2IGMPRouterPortVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 6, 1, 2),
    _SwL2IGMPRouterPortVlanName_Type()
)
swL2IGMPRouterPortVlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortVlanName.setStatus("current")
_SwL2IGMPRouterPortStaticPortList_Type = PortList
_SwL2IGMPRouterPortStaticPortList_Object = MibTableColumn
swL2IGMPRouterPortStaticPortList = _SwL2IGMPRouterPortStaticPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 6, 1, 3),
    _SwL2IGMPRouterPortStaticPortList_Type()
)
swL2IGMPRouterPortStaticPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortStaticPortList.setStatus("current")
_SwL2IGMPRouterPortDynamicPortList_Type = PortList
_SwL2IGMPRouterPortDynamicPortList_Object = MibTableColumn
swL2IGMPRouterPortDynamicPortList = _SwL2IGMPRouterPortDynamicPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 6, 1, 4),
    _SwL2IGMPRouterPortDynamicPortList_Type()
)
swL2IGMPRouterPortDynamicPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortDynamicPortList.setStatus("current")
_SwL2IGMPRouterPortForbiddenPortList_Type = PortList
_SwL2IGMPRouterPortForbiddenPortList_Object = MibTableColumn
swL2IGMPRouterPortForbiddenPortList = _SwL2IGMPRouterPortForbiddenPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 6, 1, 5),
    _SwL2IGMPRouterPortForbiddenPortList_Type()
)
swL2IGMPRouterPortForbiddenPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPRouterPortForbiddenPortList.setStatus("current")
_SwL2IGMPAccessAuthTable_Object = MibTable
swL2IGMPAccessAuthTable = _SwL2IGMPAccessAuthTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 7)
)
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthTable.setStatus("current")
_SwL2IGMPAccessAuthEntry_Object = MibTableRow
swL2IGMPAccessAuthEntry = _SwL2IGMPAccessAuthEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 7, 1)
)
swL2IGMPAccessAuthEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2IGMPAccessAuthPort"),
)
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthEntry.setStatus("current")
_SwL2IGMPAccessAuthPort_Type = Integer32
_SwL2IGMPAccessAuthPort_Object = MibTableColumn
swL2IGMPAccessAuthPort = _SwL2IGMPAccessAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 7, 1, 1),
    _SwL2IGMPAccessAuthPort_Type()
)
swL2IGMPAccessAuthPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthPort.setStatus("current")


class _SwL2IGMPAccessAuthState_Type(Integer32):
    """Custom type swL2IGMPAccessAuthState based on Integer32"""
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


_SwL2IGMPAccessAuthState_Type.__name__ = "Integer32"
_SwL2IGMPAccessAuthState_Object = MibTableColumn
swL2IGMPAccessAuthState = _SwL2IGMPAccessAuthState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 7, 1, 2),
    _SwL2IGMPAccessAuthState_Type()
)
swL2IGMPAccessAuthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPAccessAuthState.setStatus("current")
_SwL2IGMPMulticastVlanTable_Object = MibTable
swL2IGMPMulticastVlanTable = _SwL2IGMPMulticastVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8)
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanTable.setStatus("current")
_SwL2IGMPMulticastVlanEntry_Object = MibTableRow
swL2IGMPMulticastVlanEntry = _SwL2IGMPMulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1)
)
swL2IGMPMulticastVlanEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2IGMPMulticastVlanid"),
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanEntry.setStatus("current")


class _SwL2IGMPMulticastVlanid_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4094),
    )


_SwL2IGMPMulticastVlanid_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanid_Object = MibTableColumn
swL2IGMPMulticastVlanid = _SwL2IGMPMulticastVlanid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1, 1),
    _SwL2IGMPMulticastVlanid_Type()
)
swL2IGMPMulticastVlanid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanid.setStatus("current")


class _SwL2IGMPMulticastVlanName_Type(DisplayString):
    """Custom type swL2IGMPMulticastVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2IGMPMulticastVlanName_Type.__name__ = "DisplayString"
_SwL2IGMPMulticastVlanName_Object = MibTableColumn
swL2IGMPMulticastVlanName = _SwL2IGMPMulticastVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1, 2),
    _SwL2IGMPMulticastVlanName_Type()
)
swL2IGMPMulticastVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanName.setStatus("current")
_SwL2IGMPMulticastVlanSourcePort_Type = PortList
_SwL2IGMPMulticastVlanSourcePort_Object = MibTableColumn
swL2IGMPMulticastVlanSourcePort = _SwL2IGMPMulticastVlanSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1, 3),
    _SwL2IGMPMulticastVlanSourcePort_Type()
)
swL2IGMPMulticastVlanSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanSourcePort.setStatus("current")
_SwL2IGMPMulticastVlanMemberPort_Type = PortList
_SwL2IGMPMulticastVlanMemberPort_Object = MibTableColumn
swL2IGMPMulticastVlanMemberPort = _SwL2IGMPMulticastVlanMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1, 4),
    _SwL2IGMPMulticastVlanMemberPort_Type()
)
swL2IGMPMulticastVlanMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanMemberPort.setStatus("current")
_SwL2IGMPMulticastVlanTagMemberPort_Type = PortList
_SwL2IGMPMulticastVlanTagMemberPort_Object = MibTableColumn
swL2IGMPMulticastVlanTagMemberPort = _SwL2IGMPMulticastVlanTagMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1, 5),
    _SwL2IGMPMulticastVlanTagMemberPort_Type()
)
swL2IGMPMulticastVlanTagMemberPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanTagMemberPort.setStatus("current")


class _SwL2IGMPMulticastVlanState_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanState based on Integer32"""
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


_SwL2IGMPMulticastVlanState_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanState_Object = MibTableColumn
swL2IGMPMulticastVlanState = _SwL2IGMPMulticastVlanState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1, 6),
    _SwL2IGMPMulticastVlanState_Type()
)
swL2IGMPMulticastVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanState.setStatus("current")
_SwL2IGMPMulticastVlanReplaceSourceIp_Type = IpAddress
_SwL2IGMPMulticastVlanReplaceSourceIp_Object = MibTableColumn
swL2IGMPMulticastVlanReplaceSourceIp = _SwL2IGMPMulticastVlanReplaceSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1, 7),
    _SwL2IGMPMulticastVlanReplaceSourceIp_Type()
)
swL2IGMPMulticastVlanReplaceSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanReplaceSourceIp.setStatus("current")
_SwL2IGMPMulticastVlanRowStatus_Type = RowStatus
_SwL2IGMPMulticastVlanRowStatus_Object = MibTableColumn
swL2IGMPMulticastVlanRowStatus = _SwL2IGMPMulticastVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1, 8),
    _SwL2IGMPMulticastVlanRowStatus_Type()
)
swL2IGMPMulticastVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanRowStatus.setStatus("current")
_SwL2IGMPMulticastVlanUntagSourcePort_Type = PortList
_SwL2IGMPMulticastVlanUntagSourcePort_Object = MibTableColumn
swL2IGMPMulticastVlanUntagSourcePort = _SwL2IGMPMulticastVlanUntagSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1, 9),
    _SwL2IGMPMulticastVlanUntagSourcePort_Type()
)
swL2IGMPMulticastVlanUntagSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanUntagSourcePort.setStatus("current")


class _SwL2IGMPMulticastVlanRemapPriority_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanRemapPriority based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_SwL2IGMPMulticastVlanRemapPriority_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanRemapPriority_Object = MibTableColumn
swL2IGMPMulticastVlanRemapPriority = _SwL2IGMPMulticastVlanRemapPriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1, 10),
    _SwL2IGMPMulticastVlanRemapPriority_Type()
)
swL2IGMPMulticastVlanRemapPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanRemapPriority.setStatus("current")


class _SwL2IGMPMulticastVlanReplacePriority_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanReplacePriority based on Integer32"""
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


_SwL2IGMPMulticastVlanReplacePriority_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanReplacePriority_Object = MibTableColumn
swL2IGMPMulticastVlanReplacePriority = _SwL2IGMPMulticastVlanReplacePriority_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 8, 1, 11),
    _SwL2IGMPMulticastVlanReplacePriority_Type()
)
swL2IGMPMulticastVlanReplacePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanReplacePriority.setStatus("current")
_SwL2IGMPMulticastVlanGroupTable_Object = MibTable
swL2IGMPMulticastVlanGroupTable = _SwL2IGMPMulticastVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 9)
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupTable.setStatus("current")
_SwL2IGMPMulticastVlanGroupEntry_Object = MibTableRow
swL2IGMPMulticastVlanGroupEntry = _SwL2IGMPMulticastVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 9, 1)
)
swL2IGMPMulticastVlanGroupEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2IGMPMulticastVlanGroupVid"),
    (0, "DES3200-18-L2MGMT-MIB", "swL2IGMPMulticastVlanGroupFromIp"),
    (0, "DES3200-18-L2MGMT-MIB", "swL2IGMPMulticastVlanGroupToIp"),
)
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupEntry.setStatus("current")


class _SwL2IGMPMulticastVlanGroupVid_Type(Integer32):
    """Custom type swL2IGMPMulticastVlanGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2IGMPMulticastVlanGroupVid_Type.__name__ = "Integer32"
_SwL2IGMPMulticastVlanGroupVid_Object = MibTableColumn
swL2IGMPMulticastVlanGroupVid = _SwL2IGMPMulticastVlanGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 9, 1, 1),
    _SwL2IGMPMulticastVlanGroupVid_Type()
)
swL2IGMPMulticastVlanGroupVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupVid.setStatus("current")
_SwL2IGMPMulticastVlanGroupFromIp_Type = IpAddress
_SwL2IGMPMulticastVlanGroupFromIp_Object = MibTableColumn
swL2IGMPMulticastVlanGroupFromIp = _SwL2IGMPMulticastVlanGroupFromIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 9, 1, 2),
    _SwL2IGMPMulticastVlanGroupFromIp_Type()
)
swL2IGMPMulticastVlanGroupFromIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupFromIp.setStatus("current")
_SwL2IGMPMulticastVlanGroupToIp_Type = IpAddress
_SwL2IGMPMulticastVlanGroupToIp_Object = MibTableColumn
swL2IGMPMulticastVlanGroupToIp = _SwL2IGMPMulticastVlanGroupToIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 9, 1, 3),
    _SwL2IGMPMulticastVlanGroupToIp_Type()
)
swL2IGMPMulticastVlanGroupToIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupToIp.setStatus("current")
_SwL2IGMPMulticastVlanGroupStatus_Type = RowStatus
_SwL2IGMPMulticastVlanGroupStatus_Object = MibTableColumn
swL2IGMPMulticastVlanGroupStatus = _SwL2IGMPMulticastVlanGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 9, 1, 4),
    _SwL2IGMPMulticastVlanGroupStatus_Type()
)
swL2IGMPMulticastVlanGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2IGMPMulticastVlanGroupStatus.setStatus("current")
_SwL2IGMPDynIpMultMgmt_ObjectIdentity = ObjectIdentity
swL2IGMPDynIpMultMgmt = _SwL2IGMPDynIpMultMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 12)
)
_SwL2IGMPDynIPMultMaxEntry_Type = Integer32
_SwL2IGMPDynIPMultMaxEntry_Object = MibScalar
swL2IGMPDynIPMultMaxEntry = _SwL2IGMPDynIPMultMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 12, 1),
    _SwL2IGMPDynIPMultMaxEntry_Type()
)
swL2IGMPDynIPMultMaxEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPDynIPMultMaxEntry.setStatus("current")
_SwL2IGMPSnoopingClearDynIpMult_ObjectIdentity = ObjectIdentity
swL2IGMPSnoopingClearDynIpMult = _SwL2IGMPSnoopingClearDynIpMult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 12, 2)
)
_SwL2IGMPSnoopingClearDynIpMultVID_Type = VlanId
_SwL2IGMPSnoopingClearDynIpMultVID_Object = MibScalar
swL2IGMPSnoopingClearDynIpMultVID = _SwL2IGMPSnoopingClearDynIpMultVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 12, 2, 1),
    _SwL2IGMPSnoopingClearDynIpMultVID_Type()
)
swL2IGMPSnoopingClearDynIpMultVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingClearDynIpMultVID.setStatus("current")
_SwL2IGMPSnoopingClearDynIpMultIP_Type = IpAddress
_SwL2IGMPSnoopingClearDynIpMultIP_Object = MibScalar
swL2IGMPSnoopingClearDynIpMultIP = _SwL2IGMPSnoopingClearDynIpMultIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 12, 2, 2),
    _SwL2IGMPSnoopingClearDynIpMultIP_Type()
)
swL2IGMPSnoopingClearDynIpMultIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingClearDynIpMultIP.setStatus("current")


class _SwL2IGMPSnoopingClearDynIpMultAction_Type(Integer32):
    """Custom type swL2IGMPSnoopingClearDynIpMultAction based on Integer32"""
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
        *(("all", 1),
          ("group", 3),
          ("other", 4),
          ("vlan", 2))
    )


_SwL2IGMPSnoopingClearDynIpMultAction_Type.__name__ = "Integer32"
_SwL2IGMPSnoopingClearDynIpMultAction_Object = MibScalar
swL2IGMPSnoopingClearDynIpMultAction = _SwL2IGMPSnoopingClearDynIpMultAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 12, 2, 3),
    _SwL2IGMPSnoopingClearDynIpMultAction_Type()
)
swL2IGMPSnoopingClearDynIpMultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2IGMPSnoopingClearDynIpMultAction.setStatus("current")
_SwIGMPSnoopingHostTable_Object = MibTable
swIGMPSnoopingHostTable = _SwIGMPSnoopingHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 13)
)
if mibBuilder.loadTexts:
    swIGMPSnoopingHostTable.setStatus("current")
_SwIGMPSnoopingHostEntry_Object = MibTableRow
swIGMPSnoopingHostEntry = _SwIGMPSnoopingHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 13, 1)
)
swIGMPSnoopingHostEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swIGMPSnoopingHostVid"),
    (0, "DES3200-18-L2MGMT-MIB", "swIGMPSnoopingHostGroup"),
    (0, "DES3200-18-L2MGMT-MIB", "swIGMPSnoopingHostPort"),
    (0, "DES3200-18-L2MGMT-MIB", "swIGMPSnoopingHostIp"),
)
if mibBuilder.loadTexts:
    swIGMPSnoopingHostEntry.setStatus("current")
_SwIGMPSnoopingHostVid_Type = VlanId
_SwIGMPSnoopingHostVid_Object = MibTableColumn
swIGMPSnoopingHostVid = _SwIGMPSnoopingHostVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 13, 1, 1),
    _SwIGMPSnoopingHostVid_Type()
)
swIGMPSnoopingHostVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingHostVid.setStatus("current")
_SwIGMPSnoopingHostGroup_Type = IpAddress
_SwIGMPSnoopingHostGroup_Object = MibTableColumn
swIGMPSnoopingHostGroup = _SwIGMPSnoopingHostGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 13, 1, 2),
    _SwIGMPSnoopingHostGroup_Type()
)
swIGMPSnoopingHostGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingHostGroup.setStatus("current")
_SwIGMPSnoopingHostPort_Type = Integer32
_SwIGMPSnoopingHostPort_Object = MibTableColumn
swIGMPSnoopingHostPort = _SwIGMPSnoopingHostPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 13, 1, 3),
    _SwIGMPSnoopingHostPort_Type()
)
swIGMPSnoopingHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingHostPort.setStatus("current")
_SwIGMPSnoopingHostIp_Type = IpAddress
_SwIGMPSnoopingHostIp_Object = MibTableColumn
swIGMPSnoopingHostIp = _SwIGMPSnoopingHostIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 7, 13, 1, 4),
    _SwIGMPSnoopingHostIp_Type()
)
swIGMPSnoopingHostIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPSnoopingHostIp.setStatus("current")
_SwL2TrafficSegMgmt_ObjectIdentity = ObjectIdentity
swL2TrafficSegMgmt = _SwL2TrafficSegMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 12)
)
_SwL2TrafficSegTable_Object = MibTable
swL2TrafficSegTable = _SwL2TrafficSegTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 12, 1)
)
if mibBuilder.loadTexts:
    swL2TrafficSegTable.setStatus("current")
_SwL2TrafficSegEntry_Object = MibTableRow
swL2TrafficSegEntry = _SwL2TrafficSegEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 12, 1, 1)
)
swL2TrafficSegEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2TrafficSegPort"),
)
if mibBuilder.loadTexts:
    swL2TrafficSegEntry.setStatus("current")


class _SwL2TrafficSegPort_Type(Integer32):
    """Custom type swL2TrafficSegPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2TrafficSegPort_Type.__name__ = "Integer32"
_SwL2TrafficSegPort_Object = MibTableColumn
swL2TrafficSegPort = _SwL2TrafficSegPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 12, 1, 1, 1),
    _SwL2TrafficSegPort_Type()
)
swL2TrafficSegPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2TrafficSegPort.setStatus("current")
_SwL2TrafficSegForwardPorts_Type = PortList
_SwL2TrafficSegForwardPorts_Object = MibTableColumn
swL2TrafficSegForwardPorts = _SwL2TrafficSegForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 12, 1, 1, 2),
    _SwL2TrafficSegForwardPorts_Type()
)
swL2TrafficSegForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2TrafficSegForwardPorts.setStatus("current")
_SwL2PortSecurityMgmt_ObjectIdentity = ObjectIdentity
swL2PortSecurityMgmt = _SwL2PortSecurityMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15)
)
_SwL2PortSecurityControlTable_Object = MibTable
swL2PortSecurityControlTable = _SwL2PortSecurityControlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 1)
)
if mibBuilder.loadTexts:
    swL2PortSecurityControlTable.setStatus("current")
_SwL2PortSecurityControlEntry_Object = MibTableRow
swL2PortSecurityControlEntry = _SwL2PortSecurityControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 1, 1)
)
swL2PortSecurityControlEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2PortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PortSecurityControlEntry.setStatus("current")


class _SwL2PortSecurityPortIndex_Type(Integer32):
    """Custom type swL2PortSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwL2PortSecurityPortIndex_Type.__name__ = "Integer32"
_SwL2PortSecurityPortIndex_Object = MibTableColumn
swL2PortSecurityPortIndex = _SwL2PortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 1, 1, 1),
    _SwL2PortSecurityPortIndex_Type()
)
swL2PortSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2PortSecurityPortIndex.setStatus("current")


class _SwL2PortSecurityMaxLernAddr_Type(Integer32):
    """Custom type swL2PortSecurityMaxLernAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_SwL2PortSecurityMaxLernAddr_Type.__name__ = "Integer32"
_SwL2PortSecurityMaxLernAddr_Object = MibTableColumn
swL2PortSecurityMaxLernAddr = _SwL2PortSecurityMaxLernAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 1, 1, 2),
    _SwL2PortSecurityMaxLernAddr_Type()
)
swL2PortSecurityMaxLernAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityMaxLernAddr.setStatus("current")


class _SwL2PortSecurityMode_Type(Integer32):
    """Custom type swL2PortSecurityMode based on Integer32"""
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
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 3),
          ("other", 1),
          ("permanent", 2))
    )


_SwL2PortSecurityMode_Type.__name__ = "Integer32"
_SwL2PortSecurityMode_Object = MibTableColumn
swL2PortSecurityMode = _SwL2PortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 1, 1, 3),
    _SwL2PortSecurityMode_Type()
)
swL2PortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityMode.setStatus("current")


class _SwL2PortSecurityAdmState_Type(Integer32):
    """Custom type swL2PortSecurityAdmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_SwL2PortSecurityAdmState_Type.__name__ = "Integer32"
_SwL2PortSecurityAdmState_Object = MibTableColumn
swL2PortSecurityAdmState = _SwL2PortSecurityAdmState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 1, 1, 4),
    _SwL2PortSecurityAdmState_Type()
)
swL2PortSecurityAdmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityAdmState.setStatus("current")


class _SwL2PortSecurityEntryClearCtrl_Type(Integer32):
    """Custom type swL2PortSecurityEntryClearCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_SwL2PortSecurityEntryClearCtrl_Type.__name__ = "Integer32"
_SwL2PortSecurityEntryClearCtrl_Object = MibTableColumn
swL2PortSecurityEntryClearCtrl = _SwL2PortSecurityEntryClearCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 1, 1, 5),
    _SwL2PortSecurityEntryClearCtrl_Type()
)
swL2PortSecurityEntryClearCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityEntryClearCtrl.setStatus("current")


class _SwL2PortSecurityTrapLogState_Type(Integer32):
    """Custom type swL2PortSecurityTrapLogState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_SwL2PortSecurityTrapLogState_Type.__name__ = "Integer32"
_SwL2PortSecurityTrapLogState_Object = MibScalar
swL2PortSecurityTrapLogState = _SwL2PortSecurityTrapLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 2),
    _SwL2PortSecurityTrapLogState_Type()
)
swL2PortSecurityTrapLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityTrapLogState.setStatus("current")
_SwL2PortSecurityDelCtrl_ObjectIdentity = ObjectIdentity
swL2PortSecurityDelCtrl = _SwL2PortSecurityDelCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 3)
)


class _SwL2PortSecurityDelVlanName_Type(DisplayString):
    """Custom type swL2PortSecurityDelVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2PortSecurityDelVlanName_Type.__name__ = "DisplayString"
_SwL2PortSecurityDelVlanName_Object = MibScalar
swL2PortSecurityDelVlanName = _SwL2PortSecurityDelVlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 3, 1),
    _SwL2PortSecurityDelVlanName_Type()
)
swL2PortSecurityDelVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityDelVlanName.setStatus("current")


class _SwL2PortSecurityDelPort_Type(Integer32):
    """Custom type swL2PortSecurityDelPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 768),
    )


_SwL2PortSecurityDelPort_Type.__name__ = "Integer32"
_SwL2PortSecurityDelPort_Object = MibScalar
swL2PortSecurityDelPort = _SwL2PortSecurityDelPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 3, 2),
    _SwL2PortSecurityDelPort_Type()
)
swL2PortSecurityDelPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityDelPort.setStatus("current")
_SwL2PortSecurityDelMacAddress_Type = MacAddress
_SwL2PortSecurityDelMacAddress_Object = MibScalar
swL2PortSecurityDelMacAddress = _SwL2PortSecurityDelMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 3, 3),
    _SwL2PortSecurityDelMacAddress_Type()
)
swL2PortSecurityDelMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityDelMacAddress.setStatus("current")


class _SwL2PortSecurityDelActivity_Type(Integer32):
    """Custom type swL2PortSecurityDelActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_SwL2PortSecurityDelActivity_Type.__name__ = "Integer32"
_SwL2PortSecurityDelActivity_Object = MibScalar
swL2PortSecurityDelActivity = _SwL2PortSecurityDelActivity_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 15, 3, 4),
    _SwL2PortSecurityDelActivity_Type()
)
swL2PortSecurityDelActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PortSecurityDelActivity.setStatus("current")
_SwL2CosMgmt_ObjectIdentity = ObjectIdentity
swL2CosMgmt = _SwL2CosMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17)
)
_SwL2CosPriorityCtrl_ObjectIdentity = ObjectIdentity
swL2CosPriorityCtrl = _SwL2CosPriorityCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3)
)
_SwL2CosPriorityTable_Object = MibTable
swL2CosPriorityTable = _SwL2CosPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 1)
)
if mibBuilder.loadTexts:
    swL2CosPriorityTable.setStatus("current")
_SwL2CosPriorityEntry_Object = MibTableRow
swL2CosPriorityEntry = _SwL2CosPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 1, 1)
)
swL2CosPriorityEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2CosPriorityPort"),
)
if mibBuilder.loadTexts:
    swL2CosPriorityEntry.setStatus("current")


class _SwL2CosPriorityPort_Type(Integer32):
    """Custom type swL2CosPriorityPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2CosPriorityPort_Type.__name__ = "Integer32"
_SwL2CosPriorityPort_Object = MibTableColumn
swL2CosPriorityPort = _SwL2CosPriorityPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 1, 1, 1),
    _SwL2CosPriorityPort_Type()
)
swL2CosPriorityPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CosPriorityPort.setStatus("current")


class _SwL2CosPriorityEtherPRI_Type(Integer32):
    """Custom type swL2CosPriorityEtherPRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("ether8021p", 2),
          ("macBase", 3))
    )


_SwL2CosPriorityEtherPRI_Type.__name__ = "Integer32"
_SwL2CosPriorityEtherPRI_Object = MibTableColumn
swL2CosPriorityEtherPRI = _SwL2CosPriorityEtherPRI_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 1, 1, 3),
    _SwL2CosPriorityEtherPRI_Type()
)
swL2CosPriorityEtherPRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosPriorityEtherPRI.setStatus("current")


class _SwL2CosPriorityIpPRI_Type(Integer32):
    """Custom type swL2CosPriorityIpPRI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("dscp", 3),
          ("tos", 2))
    )


_SwL2CosPriorityIpPRI_Type.__name__ = "Integer32"
_SwL2CosPriorityIpPRI_Object = MibTableColumn
swL2CosPriorityIpPRI = _SwL2CosPriorityIpPRI_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 1, 1, 4),
    _SwL2CosPriorityIpPRI_Type()
)
swL2CosPriorityIpPRI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosPriorityIpPRI.setStatus("current")


class _SwL2CosPriorityNone_Type(Integer32):
    """Custom type swL2CosPriorityNone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SwL2CosPriorityNone_Type.__name__ = "Integer32"
_SwL2CosPriorityNone_Object = MibTableColumn
swL2CosPriorityNone = _SwL2CosPriorityNone_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 1, 1, 5),
    _SwL2CosPriorityNone_Type()
)
swL2CosPriorityNone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosPriorityNone.setStatus("current")
_SwL2CosTosPRITable_Object = MibTable
swL2CosTosPRITable = _SwL2CosTosPRITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 4)
)
if mibBuilder.loadTexts:
    swL2CosTosPRITable.setStatus("current")
_SwL2CosTosPRIEntry_Object = MibTableRow
swL2CosTosPRIEntry = _SwL2CosTosPRIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 4, 1)
)
swL2CosTosPRIEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2CosTosPRIIndex"),
)
if mibBuilder.loadTexts:
    swL2CosTosPRIEntry.setStatus("current")


class _SwL2CosTosPRIIndex_Type(Integer32):
    """Custom type swL2CosTosPRIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwL2CosTosPRIIndex_Type.__name__ = "Integer32"
_SwL2CosTosPRIIndex_Object = MibTableColumn
swL2CosTosPRIIndex = _SwL2CosTosPRIIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 4, 1, 1),
    _SwL2CosTosPRIIndex_Type()
)
swL2CosTosPRIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CosTosPRIIndex.setStatus("current")


class _SwL2CosTosPRIClass_Type(Integer32):
    """Custom type swL2CosTosPRIClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2CosTosPRIClass_Type.__name__ = "Integer32"
_SwL2CosTosPRIClass_Object = MibTableColumn
swL2CosTosPRIClass = _SwL2CosTosPRIClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 4, 1, 2),
    _SwL2CosTosPRIClass_Type()
)
swL2CosTosPRIClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosTosPRIClass.setStatus("current")
_SwL2CosDscpPRITable_Object = MibTable
swL2CosDscpPRITable = _SwL2CosDscpPRITable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 5)
)
if mibBuilder.loadTexts:
    swL2CosDscpPRITable.setStatus("current")
_SwL2CosDscpPRIEntry_Object = MibTableRow
swL2CosDscpPRIEntry = _SwL2CosDscpPRIEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 5, 1)
)
swL2CosDscpPRIEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2CosDscpPRIIndex"),
)
if mibBuilder.loadTexts:
    swL2CosDscpPRIEntry.setStatus("current")


class _SwL2CosDscpPRIIndex_Type(Integer32):
    """Custom type swL2CosDscpPRIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwL2CosDscpPRIIndex_Type.__name__ = "Integer32"
_SwL2CosDscpPRIIndex_Object = MibTableColumn
swL2CosDscpPRIIndex = _SwL2CosDscpPRIIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 5, 1, 1),
    _SwL2CosDscpPRIIndex_Type()
)
swL2CosDscpPRIIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2CosDscpPRIIndex.setStatus("current")


class _SwL2CosDscpPRIClass_Type(Integer32):
    """Custom type swL2CosDscpPRIClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_SwL2CosDscpPRIClass_Type.__name__ = "Integer32"
_SwL2CosDscpPRIClass_Object = MibTableColumn
swL2CosDscpPRIClass = _SwL2CosDscpPRIClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 17, 3, 5, 1, 2),
    _SwL2CosDscpPRIClass_Type()
)
swL2CosDscpPRIClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2CosDscpPRIClass.setStatus("current")
_SwL2DhcpRelayMgmt_ObjectIdentity = ObjectIdentity
swL2DhcpRelayMgmt = _SwL2DhcpRelayMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18)
)


class _SwL2DhcpRelayState_Type(Integer32):
    """Custom type swL2DhcpRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DhcpRelayState_Type.__name__ = "Integer32"
_SwL2DhcpRelayState_Object = MibScalar
swL2DhcpRelayState = _SwL2DhcpRelayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18, 1),
    _SwL2DhcpRelayState_Type()
)
swL2DhcpRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayState.setStatus("obsolete")


class _SwL2DhcpRelayHopCount_Type(Integer32):
    """Custom type swL2DhcpRelayHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SwL2DhcpRelayHopCount_Type.__name__ = "Integer32"
_SwL2DhcpRelayHopCount_Object = MibScalar
swL2DhcpRelayHopCount = _SwL2DhcpRelayHopCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18, 2),
    _SwL2DhcpRelayHopCount_Type()
)
swL2DhcpRelayHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayHopCount.setStatus("obsolete")


class _SwL2DhcpRelayTimeThreshold_Type(Integer32):
    """Custom type swL2DhcpRelayTimeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2DhcpRelayTimeThreshold_Type.__name__ = "Integer32"
_SwL2DhcpRelayTimeThreshold_Object = MibScalar
swL2DhcpRelayTimeThreshold = _SwL2DhcpRelayTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18, 3),
    _SwL2DhcpRelayTimeThreshold_Type()
)
swL2DhcpRelayTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayTimeThreshold.setStatus("obsolete")


class _SwL2DhcpRelayOption82State_Type(Integer32):
    """Custom type swL2DhcpRelayOption82State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DhcpRelayOption82State_Type.__name__ = "Integer32"
_SwL2DhcpRelayOption82State_Object = MibScalar
swL2DhcpRelayOption82State = _SwL2DhcpRelayOption82State_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18, 4),
    _SwL2DhcpRelayOption82State_Type()
)
swL2DhcpRelayOption82State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayOption82State.setStatus("obsolete")


class _SwL2DhcpRelayOption82Check_Type(Integer32):
    """Custom type swL2DhcpRelayOption82Check based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DhcpRelayOption82Check_Type.__name__ = "Integer32"
_SwL2DhcpRelayOption82Check_Object = MibScalar
swL2DhcpRelayOption82Check = _SwL2DhcpRelayOption82Check_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18, 5),
    _SwL2DhcpRelayOption82Check_Type()
)
swL2DhcpRelayOption82Check.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayOption82Check.setStatus("obsolete")


class _SwL2DhcpRelayOption82Policy_Type(Integer32):
    """Custom type swL2DhcpRelayOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("keep", 3),
          ("replace", 1))
    )


_SwL2DhcpRelayOption82Policy_Type.__name__ = "Integer32"
_SwL2DhcpRelayOption82Policy_Object = MibScalar
swL2DhcpRelayOption82Policy = _SwL2DhcpRelayOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18, 6),
    _SwL2DhcpRelayOption82Policy_Type()
)
swL2DhcpRelayOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayOption82Policy.setStatus("obsolete")
_SwL2DhcpRelayCtrlTable_Object = MibTable
swL2DhcpRelayCtrlTable = _SwL2DhcpRelayCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18, 7)
)
if mibBuilder.loadTexts:
    swL2DhcpRelayCtrlTable.setStatus("obsolete")
_SwL2DhcpRelayCtrlEntry_Object = MibTableRow
swL2DhcpRelayCtrlEntry = _SwL2DhcpRelayCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18, 7, 1)
)
swL2DhcpRelayCtrlEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2DhcpRelayCtrlInterfaceName"),
    (0, "DES3200-18-L2MGMT-MIB", "swL2DhcpRelayCtrlServer"),
)
if mibBuilder.loadTexts:
    swL2DhcpRelayCtrlEntry.setStatus("obsolete")


class _SwL2DhcpRelayCtrlInterfaceName_Type(DisplayString):
    """Custom type swL2DhcpRelayCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_SwL2DhcpRelayCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwL2DhcpRelayCtrlInterfaceName_Object = MibTableColumn
swL2DhcpRelayCtrlInterfaceName = _SwL2DhcpRelayCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18, 7, 1, 1),
    _SwL2DhcpRelayCtrlInterfaceName_Type()
)
swL2DhcpRelayCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DhcpRelayCtrlInterfaceName.setStatus("obsolete")
_SwL2DhcpRelayCtrlServer_Type = IpAddress
_SwL2DhcpRelayCtrlServer_Object = MibTableColumn
swL2DhcpRelayCtrlServer = _SwL2DhcpRelayCtrlServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18, 7, 1, 2),
    _SwL2DhcpRelayCtrlServer_Type()
)
swL2DhcpRelayCtrlServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DhcpRelayCtrlServer.setStatus("obsolete")


class _SwL2DhcpRelayCtrlState_Type(Integer32):
    """Custom type swL2DhcpRelayCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_SwL2DhcpRelayCtrlState_Type.__name__ = "Integer32"
_SwL2DhcpRelayCtrlState_Object = MibTableColumn
swL2DhcpRelayCtrlState = _SwL2DhcpRelayCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 18, 7, 1, 3),
    _SwL2DhcpRelayCtrlState_Type()
)
swL2DhcpRelayCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpRelayCtrlState.setStatus("obsolete")
_SwL2MgmtMIBTraps_ObjectIdentity = ObjectIdentity
swL2MgmtMIBTraps = _SwL2MgmtMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20)
)
_SwL2MgmtMIBTrapPrefix_ObjectIdentity = ObjectIdentity
swL2MgmtMIBTrapPrefix = _SwL2MgmtMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 0)
)
_Swl2PortSecurityBindings_ObjectIdentity = ObjectIdentity
swl2PortSecurityBindings = _Swl2PortSecurityBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 1)
)
_SwL2PortSecurityViolationMac_Type = MacAddress
_SwL2PortSecurityViolationMac_Object = MibScalar
swL2PortSecurityViolationMac = _SwL2PortSecurityViolationMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 1, 1),
    _SwL2PortSecurityViolationMac_Type()
)
swL2PortSecurityViolationMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swL2PortSecurityViolationMac.setStatus("current")
_Swl2NotificationBindings_ObjectIdentity = ObjectIdentity
swl2NotificationBindings = _Swl2NotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 2)
)


class _SwL2macNotifyInfo_Type(OctetString):
    """Custom type swL2macNotifyInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SwL2macNotifyInfo_Type.__name__ = "OctetString"
_SwL2macNotifyInfo_Object = MibScalar
swL2macNotifyInfo = _SwL2macNotifyInfo_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 2, 1),
    _SwL2macNotifyInfo_Type()
)
swL2macNotifyInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2macNotifyInfo.setStatus("current")
_SwL2VlanLoopDetectVID_Type = Integer32
_SwL2VlanLoopDetectVID_Object = MibScalar
swL2VlanLoopDetectVID = _SwL2VlanLoopDetectVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 2, 2),
    _SwL2VlanLoopDetectVID_Type()
)
swL2VlanLoopDetectVID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swL2VlanLoopDetectVID.setStatus("current")


class _SwL2FloodMacDetectedMacVid_Type(Integer32):
    """Custom type swL2FloodMacDetectedMacVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2FloodMacDetectedMacVid_Type.__name__ = "Integer32"
_SwL2FloodMacDetectedMacVid_Object = MibScalar
swL2FloodMacDetectedMacVid = _SwL2FloodMacDetectedMacVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 2, 3),
    _SwL2FloodMacDetectedMacVid_Type()
)
swL2FloodMacDetectedMacVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2FloodMacDetectedMacVid.setStatus("current")
_SwL2FloodMacDetectedMacAddress_Type = MacAddress
_SwL2FloodMacDetectedMacAddress_Object = MibScalar
swL2FloodMacDetectedMacAddress = _SwL2FloodMacDetectedMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 2, 4),
    _SwL2FloodMacDetectedMacAddress_Type()
)
swL2FloodMacDetectedMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2FloodMacDetectedMacAddress.setStatus("current")
_SwL2LoopDetectMgmt_ObjectIdentity = ObjectIdentity
swL2LoopDetectMgmt = _SwL2LoopDetectMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21)
)
_SwL2LoopDetectCtrl_ObjectIdentity = ObjectIdentity
swL2LoopDetectCtrl = _SwL2LoopDetectCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 1)
)


class _SwL2LoopDetectAdminState_Type(Integer32):
    """Custom type swL2LoopDetectAdminState based on Integer32"""
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


_SwL2LoopDetectAdminState_Type.__name__ = "Integer32"
_SwL2LoopDetectAdminState_Object = MibScalar
swL2LoopDetectAdminState = _SwL2LoopDetectAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 1, 1),
    _SwL2LoopDetectAdminState_Type()
)
swL2LoopDetectAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectAdminState.setStatus("current")


class _SwL2LoopDetectInterval_Type(Integer32):
    """Custom type swL2LoopDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_SwL2LoopDetectInterval_Type.__name__ = "Integer32"
_SwL2LoopDetectInterval_Object = MibScalar
swL2LoopDetectInterval = _SwL2LoopDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 1, 2),
    _SwL2LoopDetectInterval_Type()
)
swL2LoopDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectInterval.setStatus("current")


class _SwL2LoopDetectRecoverTime_Type(Integer32):
    """Custom type swL2LoopDetectRecoverTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SwL2LoopDetectRecoverTime_Type.__name__ = "Integer32"
_SwL2LoopDetectRecoverTime_Object = MibScalar
swL2LoopDetectRecoverTime = _SwL2LoopDetectRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 1, 3),
    _SwL2LoopDetectRecoverTime_Type()
)
swL2LoopDetectRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectRecoverTime.setStatus("current")


class _SwL2LoopDetectMode_Type(Integer32):
    """Custom type swL2LoopDetectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-based", 2),
          ("vlan-based", 1))
    )


_SwL2LoopDetectMode_Type.__name__ = "Integer32"
_SwL2LoopDetectMode_Object = MibScalar
swL2LoopDetectMode = _SwL2LoopDetectMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 1, 4),
    _SwL2LoopDetectMode_Type()
)
swL2LoopDetectMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectMode.setStatus("current")


class _SwL2LoopDetectTrapMode_Type(Integer32):
    """Custom type swL2LoopDetectTrapMode based on Integer32"""
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
        *(("both", 4),
          ("loop_cleared", 3),
          ("loop_detected", 2),
          ("none", 1))
    )


_SwL2LoopDetectTrapMode_Type.__name__ = "Integer32"
_SwL2LoopDetectTrapMode_Object = MibScalar
swL2LoopDetectTrapMode = _SwL2LoopDetectTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 1, 5),
    _SwL2LoopDetectTrapMode_Type()
)
swL2LoopDetectTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectTrapMode.setStatus("current")
_SwL2LoopDetectPortMgmt_ObjectIdentity = ObjectIdentity
swL2LoopDetectPortMgmt = _SwL2LoopDetectPortMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 2)
)
_SwL2LoopDetectPortTable_Object = MibTable
swL2LoopDetectPortTable = _SwL2LoopDetectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 2, 1)
)
if mibBuilder.loadTexts:
    swL2LoopDetectPortTable.setStatus("current")
_SwL2LoopDetectPortEntry_Object = MibTableRow
swL2LoopDetectPortEntry = _SwL2LoopDetectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 2, 1, 1)
)
swL2LoopDetectPortEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
)
if mibBuilder.loadTexts:
    swL2LoopDetectPortEntry.setStatus("current")


class _SwL2LoopDetectPortIndex_Type(Integer32):
    """Custom type swL2LoopDetectPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwL2LoopDetectPortIndex_Type.__name__ = "Integer32"
_SwL2LoopDetectPortIndex_Object = MibTableColumn
swL2LoopDetectPortIndex = _SwL2LoopDetectPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 2, 1, 1, 1),
    _SwL2LoopDetectPortIndex_Type()
)
swL2LoopDetectPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LoopDetectPortIndex.setStatus("current")


class _SwL2LoopDetectPortState_Type(Integer32):
    """Custom type swL2LoopDetectPortState based on Integer32"""
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


_SwL2LoopDetectPortState_Type.__name__ = "Integer32"
_SwL2LoopDetectPortState_Object = MibTableColumn
swL2LoopDetectPortState = _SwL2LoopDetectPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 2, 1, 1, 2),
    _SwL2LoopDetectPortState_Type()
)
swL2LoopDetectPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2LoopDetectPortState.setStatus("current")
_SwL2LoopDetectPortLoopVLAN_Type = DisplayString
_SwL2LoopDetectPortLoopVLAN_Object = MibTableColumn
swL2LoopDetectPortLoopVLAN = _SwL2LoopDetectPortLoopVLAN_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 2, 1, 1, 3),
    _SwL2LoopDetectPortLoopVLAN_Type()
)
swL2LoopDetectPortLoopVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LoopDetectPortLoopVLAN.setStatus("current")


class _SwL2LoopDetectPortLoopStatus_Type(Integer32):
    """Custom type swL2LoopDetectPortLoopStatus based on Integer32"""
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
        *(("error", 3),
          ("loop", 2),
          ("none", 4),
          ("normal", 1))
    )


_SwL2LoopDetectPortLoopStatus_Type.__name__ = "Integer32"
_SwL2LoopDetectPortLoopStatus_Object = MibTableColumn
swL2LoopDetectPortLoopStatus = _SwL2LoopDetectPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 21, 2, 1, 1, 4),
    _SwL2LoopDetectPortLoopStatus_Type()
)
swL2LoopDetectPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2LoopDetectPortLoopStatus.setStatus("current")
_SwL2MultiFilter_ObjectIdentity = ObjectIdentity
swL2MultiFilter = _SwL2MultiFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22)
)
_SwL2McastFilterTable_Object = MibTable
swL2McastFilterTable = _SwL2McastFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 2)
)
if mibBuilder.loadTexts:
    swL2McastFilterTable.setStatus("current")
_SwL2McastFilterEntry_Object = MibTableRow
swL2McastFilterEntry = _SwL2McastFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 2, 1)
)
swL2McastFilterEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2McastFilterProfileIndex"),
)
if mibBuilder.loadTexts:
    swL2McastFilterEntry.setStatus("current")


class _SwL2McastFilterProfileIndex_Type(Integer32):
    """Custom type swL2McastFilterProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SwL2McastFilterProfileIndex_Type.__name__ = "Integer32"
_SwL2McastFilterProfileIndex_Object = MibTableColumn
swL2McastFilterProfileIndex = _SwL2McastFilterProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 2, 1, 1),
    _SwL2McastFilterProfileIndex_Type()
)
swL2McastFilterProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2McastFilterProfileIndex.setStatus("current")


class _SwL2McastFilterProfileName_Type(DisplayString):
    """Custom type swL2McastFilterProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwL2McastFilterProfileName_Type.__name__ = "DisplayString"
_SwL2McastFilterProfileName_Object = MibTableColumn
swL2McastFilterProfileName = _SwL2McastFilterProfileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 2, 1, 2),
    _SwL2McastFilterProfileName_Type()
)
swL2McastFilterProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2McastFilterProfileName.setStatus("current")


class _SwL2McastFilterAddOrDelState_Type(Integer32):
    """Custom type swL2McastFilterAddOrDelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("none", 1))
    )


_SwL2McastFilterAddOrDelState_Type.__name__ = "Integer32"
_SwL2McastFilterAddOrDelState_Object = MibTableColumn
swL2McastFilterAddOrDelState = _SwL2McastFilterAddOrDelState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 2, 1, 3),
    _SwL2McastFilterAddOrDelState_Type()
)
swL2McastFilterAddOrDelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2McastFilterAddOrDelState.setStatus("current")
_SwL2McastFilterGroupList_Type = DisplayString
_SwL2McastFilterGroupList_Object = MibTableColumn
swL2McastFilterGroupList = _SwL2McastFilterGroupList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 2, 1, 4),
    _SwL2McastFilterGroupList_Type()
)
swL2McastFilterGroupList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2McastFilterGroupList.setStatus("current")
_SwL2McastFilterStatus_Type = RowStatus
_SwL2McastFilterStatus_Object = MibTableColumn
swL2McastFilterStatus = _SwL2McastFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 2, 1, 5),
    _SwL2McastFilterStatus_Type()
)
swL2McastFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2McastFilterStatus.setStatus("current")
_SwL2McastFilterPortTable_Object = MibTable
swL2McastFilterPortTable = _SwL2McastFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 3)
)
if mibBuilder.loadTexts:
    swL2McastFilterPortTable.setStatus("current")
_SwL2McastFilterPortEntry_Object = MibTableRow
swL2McastFilterPortEntry = _SwL2McastFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 3, 1)
)
swL2McastFilterPortEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2McastFilterPortGroupPortIndex"),
)
if mibBuilder.loadTexts:
    swL2McastFilterPortEntry.setStatus("current")
_SwL2McastFilterPortGroupPortIndex_Type = Integer32
_SwL2McastFilterPortGroupPortIndex_Object = MibTableColumn
swL2McastFilterPortGroupPortIndex = _SwL2McastFilterPortGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 3, 1, 1),
    _SwL2McastFilterPortGroupPortIndex_Type()
)
swL2McastFilterPortGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2McastFilterPortGroupPortIndex.setStatus("current")


class _SwL2McastFilterPortProfileAddOrDelState_Type(Integer32):
    """Custom type swL2McastFilterPortProfileAddOrDelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("delete", 3),
          ("none", 1))
    )


_SwL2McastFilterPortProfileAddOrDelState_Type.__name__ = "Integer32"
_SwL2McastFilterPortProfileAddOrDelState_Object = MibTableColumn
swL2McastFilterPortProfileAddOrDelState = _SwL2McastFilterPortProfileAddOrDelState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 3, 1, 2),
    _SwL2McastFilterPortProfileAddOrDelState_Type()
)
swL2McastFilterPortProfileAddOrDelState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2McastFilterPortProfileAddOrDelState.setStatus("current")


class _SwL2McastFilterPortProfileID_Type(Integer32):
    """Custom type swL2McastFilterPortProfileID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_SwL2McastFilterPortProfileID_Type.__name__ = "Integer32"
_SwL2McastFilterPortProfileID_Object = MibTableColumn
swL2McastFilterPortProfileID = _SwL2McastFilterPortProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 3, 1, 3),
    _SwL2McastFilterPortProfileID_Type()
)
swL2McastFilterPortProfileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2McastFilterPortProfileID.setStatus("current")


class _SwL2McastFilterPortAccess_Type(Integer32):
    """Custom type swL2McastFilterPortAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("none", 0),
          ("permit", 1))
    )


_SwL2McastFilterPortAccess_Type.__name__ = "Integer32"
_SwL2McastFilterPortAccess_Object = MibTableColumn
swL2McastFilterPortAccess = _SwL2McastFilterPortAccess_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 3, 1, 4),
    _SwL2McastFilterPortAccess_Type()
)
swL2McastFilterPortAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2McastFilterPortAccess.setStatus("current")
_SwL2McastFilterPortMaxGroupTable_Object = MibTable
swL2McastFilterPortMaxGroupTable = _SwL2McastFilterPortMaxGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 4)
)
if mibBuilder.loadTexts:
    swL2McastFilterPortMaxGroupTable.setStatus("current")
_SwL2McastFilterPortMaxGroupEntry_Object = MibTableRow
swL2McastFilterPortMaxGroupEntry = _SwL2McastFilterPortMaxGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 4, 1)
)
swL2McastFilterPortMaxGroupEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2McastFilterPortMaxGroupPortIndex"),
)
if mibBuilder.loadTexts:
    swL2McastFilterPortMaxGroupEntry.setStatus("current")
_SwL2McastFilterPortMaxGroupPortIndex_Type = Integer32
_SwL2McastFilterPortMaxGroupPortIndex_Object = MibTableColumn
swL2McastFilterPortMaxGroupPortIndex = _SwL2McastFilterPortMaxGroupPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 4, 1, 1),
    _SwL2McastFilterPortMaxGroupPortIndex_Type()
)
swL2McastFilterPortMaxGroupPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2McastFilterPortMaxGroupPortIndex.setStatus("current")


class _SwL2McastFilterPortMaxGroup_Type(Integer32):
    """Custom type swL2McastFilterPortMaxGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_SwL2McastFilterPortMaxGroup_Type.__name__ = "Integer32"
_SwL2McastFilterPortMaxGroup_Object = MibTableColumn
swL2McastFilterPortMaxGroup = _SwL2McastFilterPortMaxGroup_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 4, 1, 2),
    _SwL2McastFilterPortMaxGroup_Type()
)
swL2McastFilterPortMaxGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2McastFilterPortMaxGroup.setStatus("current")
_SwL2McastFilterPortInfoTable_Object = MibTable
swL2McastFilterPortInfoTable = _SwL2McastFilterPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 5)
)
if mibBuilder.loadTexts:
    swL2McastFilterPortInfoTable.setStatus("current")
_SwL2McastFilterPortInfoEntry_Object = MibTableRow
swL2McastFilterPortInfoEntry = _SwL2McastFilterPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 5, 1)
)
swL2McastFilterPortInfoEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2McastFilterPortInfoPortIndex"),
)
if mibBuilder.loadTexts:
    swL2McastFilterPortInfoEntry.setStatus("current")
_SwL2McastFilterPortInfoPortIndex_Type = Integer32
_SwL2McastFilterPortInfoPortIndex_Object = MibTableColumn
swL2McastFilterPortInfoPortIndex = _SwL2McastFilterPortInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 5, 1, 1),
    _SwL2McastFilterPortInfoPortIndex_Type()
)
swL2McastFilterPortInfoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2McastFilterPortInfoPortIndex.setStatus("current")
_SwL2McastFilterPortInfoProfileID_Type = DisplayString
_SwL2McastFilterPortInfoProfileID_Object = MibTableColumn
swL2McastFilterPortInfoProfileID = _SwL2McastFilterPortInfoProfileID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 5, 1, 2),
    _SwL2McastFilterPortInfoProfileID_Type()
)
swL2McastFilterPortInfoProfileID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2McastFilterPortInfoProfileID.setStatus("current")


class _SwL2McastFilterPortInfoAccess_Type(Integer32):
    """Custom type swL2McastFilterPortInfoAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )


_SwL2McastFilterPortInfoAccess_Type.__name__ = "Integer32"
_SwL2McastFilterPortInfoAccess_Object = MibTableColumn
swL2McastFilterPortInfoAccess = _SwL2McastFilterPortInfoAccess_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 22, 5, 1, 3),
    _SwL2McastFilterPortInfoAccess_Type()
)
swL2McastFilterPortInfoAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2McastFilterPortInfoAccess.setStatus("current")
_SwL2VlanMgmt_ObjectIdentity = ObjectIdentity
swL2VlanMgmt = _SwL2VlanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23)
)
_SwL2VlanAdvertisementTable_Object = MibTable
swL2VlanAdvertisementTable = _SwL2VlanAdvertisementTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 1)
)
if mibBuilder.loadTexts:
    swL2VlanAdvertisementTable.setStatus("current")
_SwL2VlanAdvertisementEntry_Object = MibTableRow
swL2VlanAdvertisementEntry = _SwL2VlanAdvertisementEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 1, 1)
)
swL2VlanAdvertisementEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2VlanIndex"),
)
if mibBuilder.loadTexts:
    swL2VlanAdvertisementEntry.setStatus("current")


class _SwL2VlanIndex_Type(Integer32):
    """Custom type swL2VlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2VlanIndex_Type.__name__ = "Integer32"
_SwL2VlanIndex_Object = MibTableColumn
swL2VlanIndex = _SwL2VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 1, 1, 1),
    _SwL2VlanIndex_Type()
)
swL2VlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanIndex.setStatus("current")


class _SwL2VlanName_Type(DisplayString):
    """Custom type swL2VlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwL2VlanName_Type.__name__ = "DisplayString"
_SwL2VlanName_Object = MibTableColumn
swL2VlanName = _SwL2VlanName_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 1, 1, 2),
    _SwL2VlanName_Type()
)
swL2VlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2VlanName.setStatus("current")


class _SwL2VlanAdvertiseState_Type(Integer32):
    """Custom type swL2VlanAdvertiseState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2VlanAdvertiseState_Type.__name__ = "Integer32"
_SwL2VlanAdvertiseState_Object = MibTableColumn
swL2VlanAdvertiseState = _SwL2VlanAdvertiseState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 1, 1, 3),
    _SwL2VlanAdvertiseState_Type()
)
swL2VlanAdvertiseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2VlanAdvertiseState.setStatus("current")
_SwL2VlanMultiplyMgmt_ObjectIdentity = ObjectIdentity
swL2VlanMultiplyMgmt = _SwL2VlanMultiplyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 2)
)


class _SwL2VlanMultiplyVlanList_Type(DisplayString):
    """Custom type swL2VlanMultiplyVlanList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwL2VlanMultiplyVlanList_Type.__name__ = "DisplayString"
_SwL2VlanMultiplyVlanList_Object = MibScalar
swL2VlanMultiplyVlanList = _SwL2VlanMultiplyVlanList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 2, 1),
    _SwL2VlanMultiplyVlanList_Type()
)
swL2VlanMultiplyVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2VlanMultiplyVlanList.setStatus("current")


class _SwL2VlanMultiplyAdvertisement_Type(Integer32):
    """Custom type swL2VlanMultiplyAdvertisement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SwL2VlanMultiplyAdvertisement_Type.__name__ = "Integer32"
_SwL2VlanMultiplyAdvertisement_Object = MibScalar
swL2VlanMultiplyAdvertisement = _SwL2VlanMultiplyAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 2, 2),
    _SwL2VlanMultiplyAdvertisement_Type()
)
swL2VlanMultiplyAdvertisement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2VlanMultiplyAdvertisement.setStatus("current")
_SwL2VlanMultiplyPortList_Type = PortList
_SwL2VlanMultiplyPortList_Object = MibScalar
swL2VlanMultiplyPortList = _SwL2VlanMultiplyPortList_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 2, 3),
    _SwL2VlanMultiplyPortList_Type()
)
swL2VlanMultiplyPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2VlanMultiplyPortList.setStatus("current")


class _SwL2VlanMultiplyPortListAction_Type(Integer32):
    """Custom type swL2VlanMultiplyPortListAction based on Integer32"""
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
        *(("add-forbidden", 4),
          ("add-tagged", 2),
          ("add-untagged", 3),
          ("delete", 5),
          ("other", 1))
    )


_SwL2VlanMultiplyPortListAction_Type.__name__ = "Integer32"
_SwL2VlanMultiplyPortListAction_Object = MibScalar
swL2VlanMultiplyPortListAction = _SwL2VlanMultiplyPortListAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 2, 4),
    _SwL2VlanMultiplyPortListAction_Type()
)
swL2VlanMultiplyPortListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2VlanMultiplyPortListAction.setStatus("current")


class _SwL2VlanMultiplyAction_Type(Integer32):
    """Custom type swL2VlanMultiplyAction based on Integer32"""
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
        *(("configure", 3),
          ("create", 2),
          ("delete", 4),
          ("other", 1))
    )


_SwL2VlanMultiplyAction_Type.__name__ = "Integer32"
_SwL2VlanMultiplyAction_Object = MibScalar
swL2VlanMultiplyAction = _SwL2VlanMultiplyAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 2, 5),
    _SwL2VlanMultiplyAction_Type()
)
swL2VlanMultiplyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2VlanMultiplyAction.setStatus("current")


class _SwL2PVIDAutoAssignmentState_Type(Integer32):
    """Custom type swL2PVIDAutoAssignmentState based on Integer32"""
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


_SwL2PVIDAutoAssignmentState_Type.__name__ = "Integer32"
_SwL2PVIDAutoAssignmentState_Object = MibScalar
swL2PVIDAutoAssignmentState = _SwL2PVIDAutoAssignmentState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 23, 3),
    _SwL2PVIDAutoAssignmentState_Type()
)
swL2PVIDAutoAssignmentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PVIDAutoAssignmentState.setStatus("current")
_SwL2DhcpLocalRelayMgmt_ObjectIdentity = ObjectIdentity
swL2DhcpLocalRelayMgmt = _SwL2DhcpLocalRelayMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 24)
)


class _SwL2DhcpLocalRelayState_Type(Integer32):
    """Custom type swL2DhcpLocalRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DhcpLocalRelayState_Type.__name__ = "Integer32"
_SwL2DhcpLocalRelayState_Object = MibScalar
swL2DhcpLocalRelayState = _SwL2DhcpLocalRelayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 24, 1),
    _SwL2DhcpLocalRelayState_Type()
)
swL2DhcpLocalRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpLocalRelayState.setStatus("current")
_SwL2DhcpLocalRelayVLANTable_Object = MibTable
swL2DhcpLocalRelayVLANTable = _SwL2DhcpLocalRelayVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 24, 2)
)
if mibBuilder.loadTexts:
    swL2DhcpLocalRelayVLANTable.setStatus("current")
_SwL2DhcpLocalRelayVLANEntry_Object = MibTableRow
swL2DhcpLocalRelayVLANEntry = _SwL2DhcpLocalRelayVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 24, 2, 1)
)
swL2DhcpLocalRelayVLANEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2DhcpLocalRelayVLANID"),
)
if mibBuilder.loadTexts:
    swL2DhcpLocalRelayVLANEntry.setStatus("current")


class _SwL2DhcpLocalRelayVLANID_Type(Integer32):
    """Custom type swL2DhcpLocalRelayVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2DhcpLocalRelayVLANID_Type.__name__ = "Integer32"
_SwL2DhcpLocalRelayVLANID_Object = MibTableColumn
swL2DhcpLocalRelayVLANID = _SwL2DhcpLocalRelayVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 24, 2, 1, 1),
    _SwL2DhcpLocalRelayVLANID_Type()
)
swL2DhcpLocalRelayVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2DhcpLocalRelayVLANID.setStatus("current")


class _SwL2DhcpLocalRelayVLANState_Type(Integer32):
    """Custom type swL2DhcpLocalRelayVLANState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwL2DhcpLocalRelayVLANState_Type.__name__ = "Integer32"
_SwL2DhcpLocalRelayVLANState_Object = MibTableColumn
swL2DhcpLocalRelayVLANState = _SwL2DhcpLocalRelayVLANState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 24, 2, 1, 2),
    _SwL2DhcpLocalRelayVLANState_Type()
)
swL2DhcpLocalRelayVLANState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2DhcpLocalRelayVLANState.setStatus("current")
_SwL2FloodMAC_ObjectIdentity = ObjectIdentity
swL2FloodMAC = _SwL2FloodMAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25)
)
_SwL2FloodMACMgmt_ObjectIdentity = ObjectIdentity
swL2FloodMACMgmt = _SwL2FloodMACMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 1)
)
_SwL2FloodMACGlobalSettings_ObjectIdentity = ObjectIdentity
swL2FloodMACGlobalSettings = _SwL2FloodMACGlobalSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 1, 1)
)


class _SwL2FloodMACState_Type(Integer32):
    """Custom type swL2FloodMACState based on Integer32"""
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


_SwL2FloodMACState_Type.__name__ = "Integer32"
_SwL2FloodMACState_Object = MibScalar
swL2FloodMACState = _SwL2FloodMACState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 1, 1, 1),
    _SwL2FloodMACState_Type()
)
swL2FloodMACState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2FloodMACState.setStatus("current")


class _SwL2FloodMACLogState_Type(Integer32):
    """Custom type swL2FloodMACLogState based on Integer32"""
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


_SwL2FloodMACLogState_Type.__name__ = "Integer32"
_SwL2FloodMACLogState_Object = MibScalar
swL2FloodMACLogState = _SwL2FloodMACLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 1, 1, 2),
    _SwL2FloodMACLogState_Type()
)
swL2FloodMACLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2FloodMACLogState.setStatus("current")


class _SwL2FloodMACTrapState_Type(Integer32):
    """Custom type swL2FloodMACTrapState based on Integer32"""
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


_SwL2FloodMACTrapState_Type.__name__ = "Integer32"
_SwL2FloodMACTrapState_Object = MibScalar
swL2FloodMACTrapState = _SwL2FloodMACTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 1, 1, 3),
    _SwL2FloodMACTrapState_Type()
)
swL2FloodMACTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2FloodMACTrapState.setStatus("current")


class _SwL2FloodMACClearFDB_Type(Integer32):
    """Custom type swL2FloodMACClearFDB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-action", 1),
          ("start", 2))
    )


_SwL2FloodMACClearFDB_Type.__name__ = "Integer32"
_SwL2FloodMACClearFDB_Object = MibScalar
swL2FloodMACClearFDB = _SwL2FloodMACClearFDB_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 1, 1, 4),
    _SwL2FloodMACClearFDB_Type()
)
swL2FloodMACClearFDB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2FloodMACClearFDB.setStatus("current")
_SwL2FloodMACAutoFDBCtrlTable_Object = MibTable
swL2FloodMACAutoFDBCtrlTable = _SwL2FloodMACAutoFDBCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 1, 2)
)
if mibBuilder.loadTexts:
    swL2FloodMACAutoFDBCtrlTable.setStatus("current")
_SwL2FloodMACAutoFDBCtrlEntry_Object = MibTableRow
swL2FloodMACAutoFDBCtrlEntry = _SwL2FloodMACAutoFDBCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 1, 2, 1)
)
swL2FloodMACAutoFDBCtrlEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2FloodMACAutoFDBIPAddress"),
)
if mibBuilder.loadTexts:
    swL2FloodMACAutoFDBCtrlEntry.setStatus("current")
_SwL2FloodMACAutoFDBIPAddress_Type = IpAddress
_SwL2FloodMACAutoFDBIPAddress_Object = MibTableColumn
swL2FloodMACAutoFDBIPAddress = _SwL2FloodMACAutoFDBIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 1, 2, 1, 1),
    _SwL2FloodMACAutoFDBIPAddress_Type()
)
swL2FloodMACAutoFDBIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2FloodMACAutoFDBIPAddress.setStatus("current")
_SwL2FloodMACAutoFDBRowStatus_Type = RowStatus
_SwL2FloodMACAutoFDBRowStatus_Object = MibTableColumn
swL2FloodMACAutoFDBRowStatus = _SwL2FloodMACAutoFDBRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 1, 2, 1, 2),
    _SwL2FloodMACAutoFDBRowStatus_Type()
)
swL2FloodMACAutoFDBRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swL2FloodMACAutoFDBRowStatus.setStatus("current")
_SwL2FloodMACInfo_ObjectIdentity = ObjectIdentity
swL2FloodMACInfo = _SwL2FloodMACInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2)
)
_SwL2FloodMACFDBTable_Object = MibTable
swL2FloodMACFDBTable = _SwL2FloodMACFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 1)
)
if mibBuilder.loadTexts:
    swL2FloodMACFDBTable.setStatus("current")
_SwL2FloodMACFDBEntry_Object = MibTableRow
swL2FloodMACFDBEntry = _SwL2FloodMACFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 1, 1)
)
swL2FloodMACFDBEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2FloodMACFDBIndex"),
    (0, "DES3200-18-L2MGMT-MIB", "swL2FloodMACFDBVID"),
    (0, "DES3200-18-L2MGMT-MIB", "swL2FloodMACFDBMacAddress"),
)
if mibBuilder.loadTexts:
    swL2FloodMACFDBEntry.setStatus("current")
_SwL2FloodMACFDBIndex_Type = Integer32
_SwL2FloodMACFDBIndex_Object = MibTableColumn
swL2FloodMACFDBIndex = _SwL2FloodMACFDBIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 1, 1, 1),
    _SwL2FloodMACFDBIndex_Type()
)
swL2FloodMACFDBIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2FloodMACFDBIndex.setStatus("current")


class _SwL2FloodMACFDBVID_Type(Integer32):
    """Custom type swL2FloodMACFDBVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2FloodMACFDBVID_Type.__name__ = "Integer32"
_SwL2FloodMACFDBVID_Object = MibTableColumn
swL2FloodMACFDBVID = _SwL2FloodMACFDBVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 1, 1, 2),
    _SwL2FloodMACFDBVID_Type()
)
swL2FloodMACFDBVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2FloodMACFDBVID.setStatus("current")
_SwL2FloodMACFDBMacAddress_Type = MacAddress
_SwL2FloodMACFDBMacAddress_Object = MibTableColumn
swL2FloodMACFDBMacAddress = _SwL2FloodMACFDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 1, 1, 3),
    _SwL2FloodMACFDBMacAddress_Type()
)
swL2FloodMACFDBMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2FloodMACFDBMacAddress.setStatus("current")


class _SwL2FloodMACFDBStatus_Type(Integer32):
    """Custom type swL2FloodMACFDBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SwL2FloodMACFDBStatus_Type.__name__ = "Integer32"
_SwL2FloodMACFDBStatus_Object = MibTableColumn
swL2FloodMACFDBStatus = _SwL2FloodMACFDBStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 1, 1, 4),
    _SwL2FloodMACFDBStatus_Type()
)
swL2FloodMACFDBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2FloodMACFDBStatus.setStatus("current")
_SwL2FloodMACFDBTimestamp_Type = Integer32
_SwL2FloodMACFDBTimestamp_Object = MibTableColumn
swL2FloodMACFDBTimestamp = _SwL2FloodMACFDBTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 1, 1, 5),
    _SwL2FloodMACFDBTimestamp_Type()
)
swL2FloodMACFDBTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2FloodMACFDBTimestamp.setStatus("current")
_SwL2FloodMACAutoFDBTable_Object = MibTable
swL2FloodMACAutoFDBTable = _SwL2FloodMACAutoFDBTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 2)
)
if mibBuilder.loadTexts:
    swL2FloodMACAutoFDBTable.setStatus("current")
_SwL2FloodMACAutoFDBEntry_Object = MibTableRow
swL2FloodMACAutoFDBEntry = _SwL2FloodMACAutoFDBEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 2, 1)
)
swL2FloodMACAutoFDBEntry.setIndexNames(
    (0, "DES3200-18-L2MGMT-MIB", "swL2FloodMACAutoFDBIPAddress"),
)
if mibBuilder.loadTexts:
    swL2FloodMACAutoFDBEntry.setStatus("current")


class _SwL2FloodMACAutoFDBVID_Type(Integer32):
    """Custom type swL2FloodMACAutoFDBVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwL2FloodMACAutoFDBVID_Type.__name__ = "Integer32"
_SwL2FloodMACAutoFDBVID_Object = MibTableColumn
swL2FloodMACAutoFDBVID = _SwL2FloodMACAutoFDBVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 2, 1, 1),
    _SwL2FloodMACAutoFDBVID_Type()
)
swL2FloodMACAutoFDBVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2FloodMACAutoFDBVID.setStatus("current")
_SwL2FloodMACAutoFDBMacAddress_Type = MacAddress
_SwL2FloodMACAutoFDBMacAddress_Object = MibTableColumn
swL2FloodMACAutoFDBMacAddress = _SwL2FloodMACAutoFDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 2, 1, 2),
    _SwL2FloodMACAutoFDBMacAddress_Type()
)
swL2FloodMACAutoFDBMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2FloodMACAutoFDBMacAddress.setStatus("current")
_SwL2FloodMACAutoFDBPort_Type = Integer32
_SwL2FloodMACAutoFDBPort_Object = MibTableColumn
swL2FloodMACAutoFDBPort = _SwL2FloodMACAutoFDBPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 2, 1, 3),
    _SwL2FloodMACAutoFDBPort_Type()
)
swL2FloodMACAutoFDBPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2FloodMACAutoFDBPort.setStatus("current")
_SwL2FloodMACAutoFDBTimestamp_Type = Integer32
_SwL2FloodMACAutoFDBTimestamp_Object = MibTableColumn
swL2FloodMACAutoFDBTimestamp = _SwL2FloodMACAutoFDBTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 25, 2, 2, 1, 4),
    _SwL2FloodMACAutoFDBTimestamp_Type()
)
swL2FloodMACAutoFDBTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swL2FloodMACAutoFDBTimestamp.setStatus("current")

# Managed Objects groups


# Notification objects

swL2PortSecurityViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 0, 1)
)
swL2PortSecurityViolationTrap.setObjects(
      *(("DES3200-18-L2MGMT-MIB", "swL2PortSecurityPortIndex"),
        ("DES3200-18-L2MGMT-MIB", "swL2PortSecurityViolationMac"))
)
if mibBuilder.loadTexts:
    swL2PortSecurityViolationTrap.setStatus(
        "current"
    )

swL2macNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 0, 2)
)
swL2macNotification.setObjects(
    ("DES3200-18-L2MGMT-MIB", "swL2macNotifyInfo")
)
if mibBuilder.loadTexts:
    swL2macNotification.setStatus(
        "current"
    )

swL2PortLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 0, 3)
)
swL2PortLoopOccurred.setObjects(
    ("DES3200-18-L2MGMT-MIB", "swL2LoopDetectPortIndex")
)
if mibBuilder.loadTexts:
    swL2PortLoopOccurred.setStatus(
        "current"
    )

swL2PortLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 0, 4)
)
swL2PortLoopRestart.setObjects(
    ("DES3200-18-L2MGMT-MIB", "swL2LoopDetectPortIndex")
)
if mibBuilder.loadTexts:
    swL2PortLoopRestart.setStatus(
        "current"
    )

swL2VlanLoopOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 0, 5)
)
swL2VlanLoopOccurred.setObjects(
      *(("DES3200-18-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
        ("DES3200-18-L2MGMT-MIB", "swL2VlanLoopDetectVID"))
)
if mibBuilder.loadTexts:
    swL2VlanLoopOccurred.setStatus(
        "current"
    )

swL2VlanLoopRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 0, 6)
)
swL2VlanLoopRestart.setObjects(
      *(("DES3200-18-L2MGMT-MIB", "swL2LoopDetectPortIndex"),
        ("DES3200-18-L2MGMT-MIB", "swL2VlanLoopDetectVID"))
)
if mibBuilder.loadTexts:
    swL2VlanLoopRestart.setStatus(
        "current"
    )

swL2FloodMacDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 11, 113, 3, 2, 20, 0, 7)
)
swL2FloodMacDetectedTrap.setObjects(
      *(("DES3200-18-L2MGMT-MIB", "swL2FloodMacDetectedMacVid"),
        ("DES3200-18-L2MGMT-MIB", "swL2FloodMacDetectedMacAddress"))
)
if mibBuilder.loadTexts:
    swL2FloodMacDetectedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES3200-18-L2MGMT-MIB",
    **{"VlanId": VlanId,
       "PortList": PortList,
       "MacAddress": MacAddress,
       "swL2MgmtMIB": swL2MgmtMIB,
       "swL2DevMgmt": swL2DevMgmt,
       "swL2DevInfo": swL2DevInfo,
       "swL2DevInfoFrontPanelLedStatus": swL2DevInfoFrontPanelLedStatus,
       "swL2DevCtrl": swL2DevCtrl,
       "swL2DevCtrlSystemReboot": swL2DevCtrlSystemReboot,
       "swL2DevCtrlSystemIP": swL2DevCtrlSystemIP,
       "swL2DevCtrlSubnetMask": swL2DevCtrlSubnetMask,
       "swL2DevCtrlDefaultGateway": swL2DevCtrlDefaultGateway,
       "swL2DevCtrlManagementVlanId": swL2DevCtrlManagementVlanId,
       "swL2DevCtrlIGMPSnooping": swL2DevCtrlIGMPSnooping,
       "swL2DevCtrlCleanAllStatisticCounter": swL2DevCtrlCleanAllStatisticCounter,
       "swL2DevCtrlSnmpEnableAuthenTraps": swL2DevCtrlSnmpEnableAuthenTraps,
       "swL2DevCtrlRmonState": swL2DevCtrlRmonState,
       "swL2DevCtrlIpAutoConfig": swL2DevCtrlIpAutoConfig,
       "swL2MACNotifyState": swL2MACNotifyState,
       "swL2MACNotifyHistorySize": swL2MACNotifyHistorySize,
       "swL2MACNotifyInterval": swL2MACNotifyInterval,
       "swL2DevCtrlLLDPState": swL2DevCtrlLLDPState,
       "swL2DevCtrlLLDPForwardMessageState": swL2DevCtrlLLDPForwardMessageState,
       "swL2DevCtrlAsymVlanState": swL2DevCtrlAsymVlanState,
       "swL2IGMPSnoopingMulticastVlanState": swL2IGMPSnoopingMulticastVlanState,
       "swL2DevCtrlVLANTrunkState": swL2DevCtrlVLANTrunkState,
       "swL2DevArpAgingTime": swL2DevArpAgingTime,
       "swL2DevPasswordEncryptionState": swL2DevPasswordEncryptionState,
       "swL2DevCtrlCFM": swL2DevCtrlCFM,
       "swL2DevCtrlCFMState": swL2DevCtrlCFMState,
       "swL2DevCtrlCFMPortTable": swL2DevCtrlCFMPortTable,
       "swL2DevCtrlCFMPortEntry": swL2DevCtrlCFMPortEntry,
       "swL2DevCtrlCFMPortIndex": swL2DevCtrlCFMPortIndex,
       "swL2DevCtrlCFMPortState": swL2DevCtrlCFMPortState,
       "swL2DevCtrlWeb": swL2DevCtrlWeb,
       "swL2DevCtrlWebState": swL2DevCtrlWebState,
       "swL2DevAlarm": swL2DevAlarm,
       "swL2DevAlarmLinkChange": swL2DevAlarmLinkChange,
       "swL2PortMgmt": swL2PortMgmt,
       "swL2PortInfoTable": swL2PortInfoTable,
       "swL2PortInfoEntry": swL2PortInfoEntry,
       "swL2PortInfoPortIndex": swL2PortInfoPortIndex,
       "swL2PortInfoMediumType": swL2PortInfoMediumType,
       "swL2PortInfoLinkStatus": swL2PortInfoLinkStatus,
       "swL2PortInfoNwayStatus": swL2PortInfoNwayStatus,
       "swL2PortInfoFlowCtrlOperStatus": swL2PortInfoFlowCtrlOperStatus,
       "swL2PortCtrlTable": swL2PortCtrlTable,
       "swL2PortCtrlEntry": swL2PortCtrlEntry,
       "swL2PortCtrlPortIndex": swL2PortCtrlPortIndex,
       "swL2PortCtrlPortMediumType": swL2PortCtrlPortMediumType,
       "swL2PortCtrlAdminState": swL2PortCtrlAdminState,
       "swL2PortCtrlNwayState": swL2PortCtrlNwayState,
       "swL2PortCtrlFlowCtrlState": swL2PortCtrlFlowCtrlState,
       "swL2PortCtrlDescription": swL2PortCtrlDescription,
       "swL2PortCtrlAddressLearning": swL2PortCtrlAddressLearning,
       "swL2PortCtrlMACNotifyState": swL2PortCtrlMACNotifyState,
       "swL2PortCtrlMulticastfilter": swL2PortCtrlMulticastfilter,
       "swL2PortCtrlMDIXState": swL2PortCtrlMDIXState,
       "swL2PortErrTable": swL2PortErrTable,
       "swL2PortErrEntry": swL2PortErrEntry,
       "swL2PortErrPortIndex": swL2PortErrPortIndex,
       "swL2PortErrPortState": swL2PortErrPortState,
       "swL2PortErrPortStatus": swL2PortErrPortStatus,
       "swL2PortErrPortReason": swL2PortErrPortReason,
       "swL2PortErrDescription": swL2PortErrDescription,
       "swL2PortCtrlJumboFrame": swL2PortCtrlJumboFrame,
       "swL2PortCtrlJumboFrameMaxSize": swL2PortCtrlJumboFrameMaxSize,
       "swL2QOSMgmt": swL2QOSMgmt,
       "swL2QOSBandwidthControlTable": swL2QOSBandwidthControlTable,
       "swL2QOSBandwidthControlEntry": swL2QOSBandwidthControlEntry,
       "swL2QOSBandwidthPortIndex": swL2QOSBandwidthPortIndex,
       "swL2QOSBandwidthRxRate": swL2QOSBandwidthRxRate,
       "swL2QOSBandwidthTxRate": swL2QOSBandwidthTxRate,
       "swL2QOSBandwidthRadiusRxRate": swL2QOSBandwidthRadiusRxRate,
       "swL2QOSBandwidthRadiusTxRate": swL2QOSBandwidthRadiusTxRate,
       "swL2QOSSchedulingTable": swL2QOSSchedulingTable,
       "swL2QOSSchedulingEntry": swL2QOSSchedulingEntry,
       "swL2QOSSchedulingClassIndex": swL2QOSSchedulingClassIndex,
       "swL2QOSSchedulingMaxWeight": swL2QOSSchedulingMaxWeight,
       "swL2QOSSchedulingMechanism": swL2QOSSchedulingMechanism,
       "swL2QOS8021pUserPriorityTable": swL2QOS8021pUserPriorityTable,
       "swL2QOS8021pUserPriorityEntry": swL2QOS8021pUserPriorityEntry,
       "swL2QOS8021pUserPriorityIndex": swL2QOS8021pUserPriorityIndex,
       "swL2QOS8021pUserPriorityClass": swL2QOS8021pUserPriorityClass,
       "swL2QOS8021pDefaultPriorityTable": swL2QOS8021pDefaultPriorityTable,
       "swL2QOS8021pDefaultPriorityEntry": swL2QOS8021pDefaultPriorityEntry,
       "swL2QOS8021pDefaultPriorityIndex": swL2QOS8021pDefaultPriorityIndex,
       "swL2QOS8021pDefaultPriority": swL2QOS8021pDefaultPriority,
       "swL2QOS8021pRadiusPriority": swL2QOS8021pRadiusPriority,
       "swL2QOSSchedulingMechanismCtrl": swL2QOSSchedulingMechanismCtrl,
       "swL2TrunkMgmt": swL2TrunkMgmt,
       "swPortTrunkMaxEntries": swPortTrunkMaxEntries,
       "swPortTrunkMaxPortMembers": swPortTrunkMaxPortMembers,
       "swPortTrunkTable": swPortTrunkTable,
       "swPortTrunkEntry": swPortTrunkEntry,
       "swPortTrunkIndex": swPortTrunkIndex,
       "swPortTrunkMasterPort": swPortTrunkMasterPort,
       "swPortTrunkPortList": swPortTrunkPortList,
       "swPortTrunkType": swPortTrunkType,
       "swPortTrunkActivePort": swPortTrunkActivePort,
       "swPortTrunkState": swPortTrunkState,
       "swPortTrunkFloodingPort": swPortTrunkFloodingPort,
       "swL2TrunkAlgorithm": swL2TrunkAlgorithm,
       "swL2TrunkLACPPortTable": swL2TrunkLACPPortTable,
       "swL2TrunkLACPPortEntry": swL2TrunkLACPPortEntry,
       "swL2TrunkLACPPortIndex": swL2TrunkLACPPortIndex,
       "swL2TrunkLACPPortState": swL2TrunkLACPPortState,
       "swL2TrunkVLANTable": swL2TrunkVLANTable,
       "swL2TrunkVLANEntry": swL2TrunkVLANEntry,
       "swL2TrunkVLANPort": swL2TrunkVLANPort,
       "swL2TrunkVLANState": swL2TrunkVLANState,
       "swPortMirrorPackage": swPortMirrorPackage,
       "swPortMirrorRxPortList": swPortMirrorRxPortList,
       "swPortMirrorTxPortList": swPortMirrorTxPortList,
       "swPortMirrorTargetPort": swPortMirrorTargetPort,
       "swPortMirrorState": swPortMirrorState,
       "swIGMPPackage": swIGMPPackage,
       "swL2IGMPMaxSupportedVlans": swL2IGMPMaxSupportedVlans,
       "swL2IGMPMaxIpGroupNumPerVlan": swL2IGMPMaxIpGroupNumPerVlan,
       "swL2IGMPCtrlTable": swL2IGMPCtrlTable,
       "swL2IGMPCtrlEntry": swL2IGMPCtrlEntry,
       "swL2IGMPCtrlVid": swL2IGMPCtrlVid,
       "swL2IGMPQueryInterval": swL2IGMPQueryInterval,
       "swL2IGMPMaxResponseTime": swL2IGMPMaxResponseTime,
       "swL2IGMPRobustness": swL2IGMPRobustness,
       "swL2IGMPLastMemberQueryInterval": swL2IGMPLastMemberQueryInterval,
       "swL2IGMPQueryState": swL2IGMPQueryState,
       "swL2IGMPCurrentState": swL2IGMPCurrentState,
       "swL2IGMPCtrlState": swL2IGMPCtrlState,
       "swL2IGMPFastLeave": swL2IGMPFastLeave,
       "swL2IGMPDynIPMultVlanAge": swL2IGMPDynIPMultVlanAge,
       "swL2IGMPQueryInfoTable": swL2IGMPQueryInfoTable,
       "swL2IGMPQueryInfoEntry": swL2IGMPQueryInfoEntry,
       "swL2IGMPInfoVid": swL2IGMPInfoVid,
       "swL2IGMPInfoQueryCount": swL2IGMPInfoQueryCount,
       "swL2IGMPInfoTxQueryCount": swL2IGMPInfoTxQueryCount,
       "swL2IGMPRouterPortTable": swL2IGMPRouterPortTable,
       "swL2IGMPRouterPortEntry": swL2IGMPRouterPortEntry,
       "swL2IGMPRouterPortVlanid": swL2IGMPRouterPortVlanid,
       "swL2IGMPRouterPortVlanName": swL2IGMPRouterPortVlanName,
       "swL2IGMPRouterPortStaticPortList": swL2IGMPRouterPortStaticPortList,
       "swL2IGMPRouterPortDynamicPortList": swL2IGMPRouterPortDynamicPortList,
       "swL2IGMPRouterPortForbiddenPortList": swL2IGMPRouterPortForbiddenPortList,
       "swL2IGMPAccessAuthTable": swL2IGMPAccessAuthTable,
       "swL2IGMPAccessAuthEntry": swL2IGMPAccessAuthEntry,
       "swL2IGMPAccessAuthPort": swL2IGMPAccessAuthPort,
       "swL2IGMPAccessAuthState": swL2IGMPAccessAuthState,
       "swL2IGMPMulticastVlanTable": swL2IGMPMulticastVlanTable,
       "swL2IGMPMulticastVlanEntry": swL2IGMPMulticastVlanEntry,
       "swL2IGMPMulticastVlanid": swL2IGMPMulticastVlanid,
       "swL2IGMPMulticastVlanName": swL2IGMPMulticastVlanName,
       "swL2IGMPMulticastVlanSourcePort": swL2IGMPMulticastVlanSourcePort,
       "swL2IGMPMulticastVlanMemberPort": swL2IGMPMulticastVlanMemberPort,
       "swL2IGMPMulticastVlanTagMemberPort": swL2IGMPMulticastVlanTagMemberPort,
       "swL2IGMPMulticastVlanState": swL2IGMPMulticastVlanState,
       "swL2IGMPMulticastVlanReplaceSourceIp": swL2IGMPMulticastVlanReplaceSourceIp,
       "swL2IGMPMulticastVlanRowStatus": swL2IGMPMulticastVlanRowStatus,
       "swL2IGMPMulticastVlanUntagSourcePort": swL2IGMPMulticastVlanUntagSourcePort,
       "swL2IGMPMulticastVlanRemapPriority": swL2IGMPMulticastVlanRemapPriority,
       "swL2IGMPMulticastVlanReplacePriority": swL2IGMPMulticastVlanReplacePriority,
       "swL2IGMPMulticastVlanGroupTable": swL2IGMPMulticastVlanGroupTable,
       "swL2IGMPMulticastVlanGroupEntry": swL2IGMPMulticastVlanGroupEntry,
       "swL2IGMPMulticastVlanGroupVid": swL2IGMPMulticastVlanGroupVid,
       "swL2IGMPMulticastVlanGroupFromIp": swL2IGMPMulticastVlanGroupFromIp,
       "swL2IGMPMulticastVlanGroupToIp": swL2IGMPMulticastVlanGroupToIp,
       "swL2IGMPMulticastVlanGroupStatus": swL2IGMPMulticastVlanGroupStatus,
       "swL2IGMPDynIpMultMgmt": swL2IGMPDynIpMultMgmt,
       "swL2IGMPDynIPMultMaxEntry": swL2IGMPDynIPMultMaxEntry,
       "swL2IGMPSnoopingClearDynIpMult": swL2IGMPSnoopingClearDynIpMult,
       "swL2IGMPSnoopingClearDynIpMultVID": swL2IGMPSnoopingClearDynIpMultVID,
       "swL2IGMPSnoopingClearDynIpMultIP": swL2IGMPSnoopingClearDynIpMultIP,
       "swL2IGMPSnoopingClearDynIpMultAction": swL2IGMPSnoopingClearDynIpMultAction,
       "swIGMPSnoopingHostTable": swIGMPSnoopingHostTable,
       "swIGMPSnoopingHostEntry": swIGMPSnoopingHostEntry,
       "swIGMPSnoopingHostVid": swIGMPSnoopingHostVid,
       "swIGMPSnoopingHostGroup": swIGMPSnoopingHostGroup,
       "swIGMPSnoopingHostPort": swIGMPSnoopingHostPort,
       "swIGMPSnoopingHostIp": swIGMPSnoopingHostIp,
       "swL2TrafficSegMgmt": swL2TrafficSegMgmt,
       "swL2TrafficSegTable": swL2TrafficSegTable,
       "swL2TrafficSegEntry": swL2TrafficSegEntry,
       "swL2TrafficSegPort": swL2TrafficSegPort,
       "swL2TrafficSegForwardPorts": swL2TrafficSegForwardPorts,
       "swL2PortSecurityMgmt": swL2PortSecurityMgmt,
       "swL2PortSecurityControlTable": swL2PortSecurityControlTable,
       "swL2PortSecurityControlEntry": swL2PortSecurityControlEntry,
       "swL2PortSecurityPortIndex": swL2PortSecurityPortIndex,
       "swL2PortSecurityMaxLernAddr": swL2PortSecurityMaxLernAddr,
       "swL2PortSecurityMode": swL2PortSecurityMode,
       "swL2PortSecurityAdmState": swL2PortSecurityAdmState,
       "swL2PortSecurityEntryClearCtrl": swL2PortSecurityEntryClearCtrl,
       "swL2PortSecurityTrapLogState": swL2PortSecurityTrapLogState,
       "swL2PortSecurityDelCtrl": swL2PortSecurityDelCtrl,
       "swL2PortSecurityDelVlanName": swL2PortSecurityDelVlanName,
       "swL2PortSecurityDelPort": swL2PortSecurityDelPort,
       "swL2PortSecurityDelMacAddress": swL2PortSecurityDelMacAddress,
       "swL2PortSecurityDelActivity": swL2PortSecurityDelActivity,
       "swL2CosMgmt": swL2CosMgmt,
       "swL2CosPriorityCtrl": swL2CosPriorityCtrl,
       "swL2CosPriorityTable": swL2CosPriorityTable,
       "swL2CosPriorityEntry": swL2CosPriorityEntry,
       "swL2CosPriorityPort": swL2CosPriorityPort,
       "swL2CosPriorityEtherPRI": swL2CosPriorityEtherPRI,
       "swL2CosPriorityIpPRI": swL2CosPriorityIpPRI,
       "swL2CosPriorityNone": swL2CosPriorityNone,
       "swL2CosTosPRITable": swL2CosTosPRITable,
       "swL2CosTosPRIEntry": swL2CosTosPRIEntry,
       "swL2CosTosPRIIndex": swL2CosTosPRIIndex,
       "swL2CosTosPRIClass": swL2CosTosPRIClass,
       "swL2CosDscpPRITable": swL2CosDscpPRITable,
       "swL2CosDscpPRIEntry": swL2CosDscpPRIEntry,
       "swL2CosDscpPRIIndex": swL2CosDscpPRIIndex,
       "swL2CosDscpPRIClass": swL2CosDscpPRIClass,
       "swL2DhcpRelayMgmt": swL2DhcpRelayMgmt,
       "swL2DhcpRelayState": swL2DhcpRelayState,
       "swL2DhcpRelayHopCount": swL2DhcpRelayHopCount,
       "swL2DhcpRelayTimeThreshold": swL2DhcpRelayTimeThreshold,
       "swL2DhcpRelayOption82State": swL2DhcpRelayOption82State,
       "swL2DhcpRelayOption82Check": swL2DhcpRelayOption82Check,
       "swL2DhcpRelayOption82Policy": swL2DhcpRelayOption82Policy,
       "swL2DhcpRelayCtrlTable": swL2DhcpRelayCtrlTable,
       "swL2DhcpRelayCtrlEntry": swL2DhcpRelayCtrlEntry,
       "swL2DhcpRelayCtrlInterfaceName": swL2DhcpRelayCtrlInterfaceName,
       "swL2DhcpRelayCtrlServer": swL2DhcpRelayCtrlServer,
       "swL2DhcpRelayCtrlState": swL2DhcpRelayCtrlState,
       "swL2MgmtMIBTraps": swL2MgmtMIBTraps,
       "swL2MgmtMIBTrapPrefix": swL2MgmtMIBTrapPrefix,
       "swL2PortSecurityViolationTrap": swL2PortSecurityViolationTrap,
       "swL2macNotification": swL2macNotification,
       "swL2PortLoopOccurred": swL2PortLoopOccurred,
       "swL2PortLoopRestart": swL2PortLoopRestart,
       "swL2VlanLoopOccurred": swL2VlanLoopOccurred,
       "swL2VlanLoopRestart": swL2VlanLoopRestart,
       "swL2FloodMacDetectedTrap": swL2FloodMacDetectedTrap,
       "swl2PortSecurityBindings": swl2PortSecurityBindings,
       "swL2PortSecurityViolationMac": swL2PortSecurityViolationMac,
       "swl2NotificationBindings": swl2NotificationBindings,
       "swL2macNotifyInfo": swL2macNotifyInfo,
       "swL2VlanLoopDetectVID": swL2VlanLoopDetectVID,
       "swL2FloodMacDetectedMacVid": swL2FloodMacDetectedMacVid,
       "swL2FloodMacDetectedMacAddress": swL2FloodMacDetectedMacAddress,
       "swL2LoopDetectMgmt": swL2LoopDetectMgmt,
       "swL2LoopDetectCtrl": swL2LoopDetectCtrl,
       "swL2LoopDetectAdminState": swL2LoopDetectAdminState,
       "swL2LoopDetectInterval": swL2LoopDetectInterval,
       "swL2LoopDetectRecoverTime": swL2LoopDetectRecoverTime,
       "swL2LoopDetectMode": swL2LoopDetectMode,
       "swL2LoopDetectTrapMode": swL2LoopDetectTrapMode,
       "swL2LoopDetectPortMgmt": swL2LoopDetectPortMgmt,
       "swL2LoopDetectPortTable": swL2LoopDetectPortTable,
       "swL2LoopDetectPortEntry": swL2LoopDetectPortEntry,
       "swL2LoopDetectPortIndex": swL2LoopDetectPortIndex,
       "swL2LoopDetectPortState": swL2LoopDetectPortState,
       "swL2LoopDetectPortLoopVLAN": swL2LoopDetectPortLoopVLAN,
       "swL2LoopDetectPortLoopStatus": swL2LoopDetectPortLoopStatus,
       "swL2MultiFilter": swL2MultiFilter,
       "swL2McastFilterTable": swL2McastFilterTable,
       "swL2McastFilterEntry": swL2McastFilterEntry,
       "swL2McastFilterProfileIndex": swL2McastFilterProfileIndex,
       "swL2McastFilterProfileName": swL2McastFilterProfileName,
       "swL2McastFilterAddOrDelState": swL2McastFilterAddOrDelState,
       "swL2McastFilterGroupList": swL2McastFilterGroupList,
       "swL2McastFilterStatus": swL2McastFilterStatus,
       "swL2McastFilterPortTable": swL2McastFilterPortTable,
       "swL2McastFilterPortEntry": swL2McastFilterPortEntry,
       "swL2McastFilterPortGroupPortIndex": swL2McastFilterPortGroupPortIndex,
       "swL2McastFilterPortProfileAddOrDelState": swL2McastFilterPortProfileAddOrDelState,
       "swL2McastFilterPortProfileID": swL2McastFilterPortProfileID,
       "swL2McastFilterPortAccess": swL2McastFilterPortAccess,
       "swL2McastFilterPortMaxGroupTable": swL2McastFilterPortMaxGroupTable,
       "swL2McastFilterPortMaxGroupEntry": swL2McastFilterPortMaxGroupEntry,
       "swL2McastFilterPortMaxGroupPortIndex": swL2McastFilterPortMaxGroupPortIndex,
       "swL2McastFilterPortMaxGroup": swL2McastFilterPortMaxGroup,
       "swL2McastFilterPortInfoTable": swL2McastFilterPortInfoTable,
       "swL2McastFilterPortInfoEntry": swL2McastFilterPortInfoEntry,
       "swL2McastFilterPortInfoPortIndex": swL2McastFilterPortInfoPortIndex,
       "swL2McastFilterPortInfoProfileID": swL2McastFilterPortInfoProfileID,
       "swL2McastFilterPortInfoAccess": swL2McastFilterPortInfoAccess,
       "swL2VlanMgmt": swL2VlanMgmt,
       "swL2VlanAdvertisementTable": swL2VlanAdvertisementTable,
       "swL2VlanAdvertisementEntry": swL2VlanAdvertisementEntry,
       "swL2VlanIndex": swL2VlanIndex,
       "swL2VlanName": swL2VlanName,
       "swL2VlanAdvertiseState": swL2VlanAdvertiseState,
       "swL2VlanMultiplyMgmt": swL2VlanMultiplyMgmt,
       "swL2VlanMultiplyVlanList": swL2VlanMultiplyVlanList,
       "swL2VlanMultiplyAdvertisement": swL2VlanMultiplyAdvertisement,
       "swL2VlanMultiplyPortList": swL2VlanMultiplyPortList,
       "swL2VlanMultiplyPortListAction": swL2VlanMultiplyPortListAction,
       "swL2VlanMultiplyAction": swL2VlanMultiplyAction,
       "swL2PVIDAutoAssignmentState": swL2PVIDAutoAssignmentState,
       "swL2DhcpLocalRelayMgmt": swL2DhcpLocalRelayMgmt,
       "swL2DhcpLocalRelayState": swL2DhcpLocalRelayState,
       "swL2DhcpLocalRelayVLANTable": swL2DhcpLocalRelayVLANTable,
       "swL2DhcpLocalRelayVLANEntry": swL2DhcpLocalRelayVLANEntry,
       "swL2DhcpLocalRelayVLANID": swL2DhcpLocalRelayVLANID,
       "swL2DhcpLocalRelayVLANState": swL2DhcpLocalRelayVLANState,
       "swL2FloodMAC": swL2FloodMAC,
       "swL2FloodMACMgmt": swL2FloodMACMgmt,
       "swL2FloodMACGlobalSettings": swL2FloodMACGlobalSettings,
       "swL2FloodMACState": swL2FloodMACState,
       "swL2FloodMACLogState": swL2FloodMACLogState,
       "swL2FloodMACTrapState": swL2FloodMACTrapState,
       "swL2FloodMACClearFDB": swL2FloodMACClearFDB,
       "swL2FloodMACAutoFDBCtrlTable": swL2FloodMACAutoFDBCtrlTable,
       "swL2FloodMACAutoFDBCtrlEntry": swL2FloodMACAutoFDBCtrlEntry,
       "swL2FloodMACAutoFDBIPAddress": swL2FloodMACAutoFDBIPAddress,
       "swL2FloodMACAutoFDBRowStatus": swL2FloodMACAutoFDBRowStatus,
       "swL2FloodMACInfo": swL2FloodMACInfo,
       "swL2FloodMACFDBTable": swL2FloodMACFDBTable,
       "swL2FloodMACFDBEntry": swL2FloodMACFDBEntry,
       "swL2FloodMACFDBIndex": swL2FloodMACFDBIndex,
       "swL2FloodMACFDBVID": swL2FloodMACFDBVID,
       "swL2FloodMACFDBMacAddress": swL2FloodMACFDBMacAddress,
       "swL2FloodMACFDBStatus": swL2FloodMACFDBStatus,
       "swL2FloodMACFDBTimestamp": swL2FloodMACFDBTimestamp,
       "swL2FloodMACAutoFDBTable": swL2FloodMACAutoFDBTable,
       "swL2FloodMACAutoFDBEntry": swL2FloodMACAutoFDBEntry,
       "swL2FloodMACAutoFDBVID": swL2FloodMACAutoFDBVID,
       "swL2FloodMACAutoFDBMacAddress": swL2FloodMACAutoFDBMacAddress,
       "swL2FloodMACAutoFDBPort": swL2FloodMACAutoFDBPort,
       "swL2FloodMACAutoFDBTimestamp": swL2FloodMACAutoFDBTimestamp}
)
