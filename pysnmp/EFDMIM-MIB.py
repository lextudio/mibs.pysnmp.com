# SNMP MIB module (EFDMIM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EFDMIM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:39 2024
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
 enterprises,
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
    "enterprises",
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

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_CommsDevice_ObjectIdentity = ObjectIdentity
commsDevice = _CommsDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1)
)
_Subsystem_ObjectIdentity = ObjectIdentity
subsystem = _Subsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6)
)
_Nb55_ObjectIdentity = ObjectIdentity
nb55 = _Nb55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4)
)
_Rev1_ObjectIdentity = ObjectIdentity
rev1 = _Rev1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1)
)
_EfdmimRingTable_Object = MibTable
efdmimRingTable = _EfdmimRingTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 1)
)
if mibBuilder.loadTexts:
    efdmimRingTable.setStatus("mandatory")
_EfdmimRingEntry_Object = MibTableRow
efdmimRingEntry = _EfdmimRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    efdmimRingEntry.setStatus("mandatory")
_EfdmimRingUpstreamMac_Type = OctetString
_EfdmimRingUpstreamMac_Object = MibTableColumn
efdmimRingUpstreamMac = _EfdmimRingUpstreamMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 1, 1, 1),
    _EfdmimRingUpstreamMac_Type()
)
efdmimRingUpstreamMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimRingUpstreamMac.setStatus("mandatory")
_EfdmimRingNodeClass_Type = Integer32
_EfdmimRingNodeClass_Object = MibTableColumn
efdmimRingNodeClass = _EfdmimRingNodeClass_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 1, 1, 2),
    _EfdmimRingNodeClass_Type()
)
efdmimRingNodeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimRingNodeClass.setStatus("mandatory")
_EfdmimRingMacs_Type = Counter32
_EfdmimRingMacs_Object = MibTableColumn
efdmimRingMacs = _EfdmimRingMacs_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 1, 1, 3),
    _EfdmimRingMacs_Type()
)
efdmimRingMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimRingMacs.setStatus("mandatory")
_EfdmimRingNonMasterPhys_Type = Integer32
_EfdmimRingNonMasterPhys_Object = MibTableColumn
efdmimRingNonMasterPhys = _EfdmimRingNonMasterPhys_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 1, 1, 4),
    _EfdmimRingNonMasterPhys_Type()
)
efdmimRingNonMasterPhys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimRingNonMasterPhys.setStatus("mandatory")
_EfdmimRingMasterPhys_Type = Integer32
_EfdmimRingMasterPhys_Object = MibTableColumn
efdmimRingMasterPhys = _EfdmimRingMasterPhys_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 1, 1, 5),
    _EfdmimRingMasterPhys_Type()
)
efdmimRingMasterPhys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimRingMasterPhys.setStatus("mandatory")
_EfdmimRingTopology_Type = Integer32
_EfdmimRingTopology_Object = MibTableColumn
efdmimRingTopology = _EfdmimRingTopology_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 1, 1, 6),
    _EfdmimRingTopology_Type()
)
efdmimRingTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimRingTopology.setStatus("mandatory")
_EfdmimRingDuplicate_Type = Integer32
_EfdmimRingDuplicate_Object = MibTableColumn
efdmimRingDuplicate = _EfdmimRingDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 1, 1, 7),
    _EfdmimRingDuplicate_Type()
)
efdmimRingDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimRingDuplicate.setStatus("mandatory")
_EfdmimRingMacAddress_Type = OctetString
_EfdmimRingMacAddress_Object = MibTableColumn
efdmimRingMacAddress = _EfdmimRingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 1, 1, 8),
    _EfdmimRingMacAddress_Type()
)
efdmimRingMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimRingMacAddress.setStatus("mandatory")
_EfdmimBdgPortTable_Object = MibTable
efdmimBdgPortTable = _EfdmimBdgPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    efdmimBdgPortTable.setStatus("mandatory")
_EfdmimBdgPortEntry_Object = MibTableRow
efdmimBdgPortEntry = _EfdmimBdgPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    efdmimBdgPortEntry.setStatus("mandatory")
_EfdmimBdgPortState_Type = OctetString
_EfdmimBdgPortState_Object = MibTableColumn
efdmimBdgPortState = _EfdmimBdgPortState_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 2, 1, 1),
    _EfdmimBdgPortState_Type()
)
efdmimBdgPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimBdgPortState.setStatus("optional")
_EfdmimBdgPortReceivedPkts_Type = Integer32
_EfdmimBdgPortReceivedPkts_Object = MibTableColumn
efdmimBdgPortReceivedPkts = _EfdmimBdgPortReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 2, 1, 2),
    _EfdmimBdgPortReceivedPkts_Type()
)
efdmimBdgPortReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimBdgPortReceivedPkts.setStatus("mandatory")
_EfdmimBdgPortFilteredPkts_Type = Integer32
_EfdmimBdgPortFilteredPkts_Object = MibTableColumn
efdmimBdgPortFilteredPkts = _EfdmimBdgPortFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 2, 1, 3),
    _EfdmimBdgPortFilteredPkts_Type()
)
efdmimBdgPortFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimBdgPortFilteredPkts.setStatus("mandatory")
_EfdmimBdgPortForwardedPkts_Type = Integer32
_EfdmimBdgPortForwardedPkts_Object = MibTableColumn
efdmimBdgPortForwardedPkts = _EfdmimBdgPortForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 2, 1, 4),
    _EfdmimBdgPortForwardedPkts_Type()
)
efdmimBdgPortForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimBdgPortForwardedPkts.setStatus("mandatory")
_EfdmimBdgPortTransmittedPkts_Type = Integer32
_EfdmimBdgPortTransmittedPkts_Object = MibScalar
efdmimBdgPortTransmittedPkts = _EfdmimBdgPortTransmittedPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 2, 1, 5),
    _EfdmimBdgPortTransmittedPkts_Type()
)
efdmimBdgPortTransmittedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimBdgPortTransmittedPkts.setStatus("mandatory")
_EfdmimBdgPortErrorPkts_Type = Integer32
_EfdmimBdgPortErrorPkts_Object = MibScalar
efdmimBdgPortErrorPkts = _EfdmimBdgPortErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 2, 1, 6),
    _EfdmimBdgPortErrorPkts_Type()
)
efdmimBdgPortErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimBdgPortErrorPkts.setStatus("mandatory")
_EfdmimPhyTable_Object = MibTable
efdmimPhyTable = _EfdmimPhyTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 3)
)
if mibBuilder.loadTexts:
    efdmimPhyTable.setStatus("mandatory")
_EfdmimPhyEntry_Object = MibTableRow
efdmimPhyEntry = _EfdmimPhyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    efdmimPhyEntry.setStatus("mandatory")
_EfdmimPhyWithold_Type = Integer32
_EfdmimPhyWithold_Object = MibTableColumn
efdmimPhyWithold = _EfdmimPhyWithold_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 3, 1, 1),
    _EfdmimPhyWithold_Type()
)
efdmimPhyWithold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimPhyWithold.setStatus("mandatory")
_EfdmimDeviceStatus_Type = OctetString
_EfdmimDeviceStatus_Object = MibScalar
efdmimDeviceStatus = _EfdmimDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 20),
    _EfdmimDeviceStatus_Type()
)
efdmimDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDeviceStatus.setStatus("mandatory")
_EfdmimDeviceBdgName_Type = OctetString
_EfdmimDeviceBdgName_Object = MibScalar
efdmimDeviceBdgName = _EfdmimDeviceBdgName_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 21),
    _EfdmimDeviceBdgName_Type()
)
efdmimDeviceBdgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efdmimDeviceBdgName.setStatus("mandatory")
_EfdmimDeviceType_Type = OctetString
_EfdmimDeviceType_Object = MibScalar
efdmimDeviceType = _EfdmimDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 22),
    _EfdmimDeviceType_Type()
)
efdmimDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDeviceType.setStatus("mandatory")
_EfdmimDeviceVersion_Type = OctetString
_EfdmimDeviceVersion_Object = MibScalar
efdmimDeviceVersion = _EfdmimDeviceVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 23),
    _EfdmimDeviceVersion_Type()
)
efdmimDeviceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDeviceVersion.setStatus("mandatory")
_EfdmimDeviceLocation_Type = OctetString
_EfdmimDeviceLocation_Object = MibScalar
efdmimDeviceLocation = _EfdmimDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 24),
    _EfdmimDeviceLocation_Type()
)
efdmimDeviceLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efdmimDeviceLocation.setStatus("mandatory")
_EfdmimDeviceUptime_Type = Counter32
_EfdmimDeviceUptime_Object = MibScalar
efdmimDeviceUptime = _EfdmimDeviceUptime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 25),
    _EfdmimDeviceUptime_Type()
)
efdmimDeviceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDeviceUptime.setStatus("mandatory")


class _EfdmimDeviceDisableBridge_Type(Integer32):
    """Custom type efdmimDeviceDisableBridge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_EfdmimDeviceDisableBridge_Type.__name__ = "Integer32"
_EfdmimDeviceDisableBridge_Object = MibScalar
efdmimDeviceDisableBridge = _EfdmimDeviceDisableBridge_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 26),
    _EfdmimDeviceDisableBridge_Type()
)
efdmimDeviceDisableBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    efdmimDeviceDisableBridge.setStatus("mandatory")


class _EfdmimDeviceResetCounters_Type(Integer32):
    """Custom type efdmimDeviceResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("true", 1)
    )


_EfdmimDeviceResetCounters_Type.__name__ = "Integer32"
_EfdmimDeviceResetCounters_Object = MibScalar
efdmimDeviceResetCounters = _EfdmimDeviceResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 27),
    _EfdmimDeviceResetCounters_Type()
)
efdmimDeviceResetCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    efdmimDeviceResetCounters.setStatus("mandatory")
_EfdmimDeviceSwitchSettings_Type = Integer32
_EfdmimDeviceSwitchSettings_Object = MibScalar
efdmimDeviceSwitchSettings = _EfdmimDeviceSwitchSettings_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 28),
    _EfdmimDeviceSwitchSettings_Type()
)
efdmimDeviceSwitchSettings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDeviceSwitchSettings.setStatus("mandatory")
_EfdmimDeviceReceivedPkts_Type = Integer32
_EfdmimDeviceReceivedPkts_Object = MibScalar
efdmimDeviceReceivedPkts = _EfdmimDeviceReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 29),
    _EfdmimDeviceReceivedPkts_Type()
)
efdmimDeviceReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDeviceReceivedPkts.setStatus("mandatory")
_EfdmimDeviceFilteredPkts_Type = Integer32
_EfdmimDeviceFilteredPkts_Object = MibScalar
efdmimDeviceFilteredPkts = _EfdmimDeviceFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 30),
    _EfdmimDeviceFilteredPkts_Type()
)
efdmimDeviceFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDeviceFilteredPkts.setStatus("mandatory")
_EfdmimDeviceForwardedPkts_Type = Integer32
_EfdmimDeviceForwardedPkts_Object = MibScalar
efdmimDeviceForwardedPkts = _EfdmimDeviceForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 31),
    _EfdmimDeviceForwardedPkts_Type()
)
efdmimDeviceForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDeviceForwardedPkts.setStatus("mandatory")
_EfdmimDeviceTransmittedPkts_Type = Integer32
_EfdmimDeviceTransmittedPkts_Object = MibScalar
efdmimDeviceTransmittedPkts = _EfdmimDeviceTransmittedPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 32),
    _EfdmimDeviceTransmittedPkts_Type()
)
efdmimDeviceTransmittedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDeviceTransmittedPkts.setStatus("mandatory")
_EfdmimDeviceErrorPkts_Type = Integer32
_EfdmimDeviceErrorPkts_Object = MibScalar
efdmimDeviceErrorPkts = _EfdmimDeviceErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 33),
    _EfdmimDeviceErrorPkts_Type()
)
efdmimDeviceErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDeviceErrorPkts.setStatus("mandatory")
_EfdmimCfmState_Type = Integer32
_EfdmimCfmState_Object = MibScalar
efdmimCfmState = _EfdmimCfmState_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 34),
    _EfdmimCfmState_Type()
)
efdmimCfmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimCfmState.setStatus("mandatory")


class _EfdmimBypassAttached_Type(Integer32):
    """Custom type efdmimBypassAttached based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_EfdmimBypassAttached_Type.__name__ = "Integer32"
_EfdmimBypassAttached_Object = MibScalar
efdmimBypassAttached = _EfdmimBypassAttached_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 35),
    _EfdmimBypassAttached_Type()
)
efdmimBypassAttached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimBypassAttached.setStatus("mandatory")
_EfdmimOscillations_Type = Counter32
_EfdmimOscillations_Object = MibScalar
efdmimOscillations = _EfdmimOscillations_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 36),
    _EfdmimOscillations_Type()
)
efdmimOscillations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimOscillations.setStatus("mandatory")
_EfdmimRingUpTime_Type = Counter32
_EfdmimRingUpTime_Object = MibScalar
efdmimRingUpTime = _EfdmimRingUpTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 37),
    _EfdmimRingUpTime_Type()
)
efdmimRingUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimRingUpTime.setStatus("mandatory")
_EfdmimDownstreamMac_Type = OctetString
_EfdmimDownstreamMac_Object = MibScalar
efdmimDownstreamMac = _EfdmimDownstreamMac_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 38),
    _EfdmimDownstreamMac_Type()
)
efdmimDownstreamMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDownstreamMac.setStatus("mandatory")


class _EfdmimBypassStuck_Type(Integer32):
    """Custom type efdmimBypassStuck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_EfdmimBypassStuck_Type.__name__ = "Integer32"
_EfdmimBypassStuck_Object = MibScalar
efdmimBypassStuck = _EfdmimBypassStuck_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 39),
    _EfdmimBypassStuck_Type()
)
efdmimBypassStuck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimBypassStuck.setStatus("mandatory")


class _EfdmimMode_Type(Integer32):
    """Custom type efdmimMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encapsulation", 1),
          ("translation", 2))
    )


_EfdmimMode_Type.__name__ = "Integer32"
_EfdmimMode_Object = MibScalar
efdmimMode = _EfdmimMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 40),
    _EfdmimMode_Type()
)
efdmimMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimMode.setStatus("mandatory")
_EfdmimRmtState_Type = Integer32
_EfdmimRmtState_Object = MibScalar
efdmimRmtState = _EfdmimRmtState_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 41),
    _EfdmimRmtState_Type()
)
efdmimRmtState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimRmtState.setStatus("mandatory")
_EfdmimDeviceBridgeAddr_Type = OctetString
_EfdmimDeviceBridgeAddr_Object = MibScalar
efdmimDeviceBridgeAddr = _EfdmimDeviceBridgeAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 1, 6, 4, 1, 42),
    _EfdmimDeviceBridgeAddr_Type()
)
efdmimDeviceBridgeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efdmimDeviceBridgeAddr.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EFDMIM-MIB",
    **{"cabletron": cabletron,
       "commsDevice": commsDevice,
       "subsystem": subsystem,
       "nb55": nb55,
       "rev1": rev1,
       "efdmimRingTable": efdmimRingTable,
       "efdmimRingEntry": efdmimRingEntry,
       "efdmimRingUpstreamMac": efdmimRingUpstreamMac,
       "efdmimRingNodeClass": efdmimRingNodeClass,
       "efdmimRingMacs": efdmimRingMacs,
       "efdmimRingNonMasterPhys": efdmimRingNonMasterPhys,
       "efdmimRingMasterPhys": efdmimRingMasterPhys,
       "efdmimRingTopology": efdmimRingTopology,
       "efdmimRingDuplicate": efdmimRingDuplicate,
       "efdmimRingMacAddress": efdmimRingMacAddress,
       "efdmimBdgPortTable": efdmimBdgPortTable,
       "efdmimBdgPortEntry": efdmimBdgPortEntry,
       "efdmimBdgPortState": efdmimBdgPortState,
       "efdmimBdgPortReceivedPkts": efdmimBdgPortReceivedPkts,
       "efdmimBdgPortFilteredPkts": efdmimBdgPortFilteredPkts,
       "efdmimBdgPortForwardedPkts": efdmimBdgPortForwardedPkts,
       "efdmimBdgPortTransmittedPkts": efdmimBdgPortTransmittedPkts,
       "efdmimBdgPortErrorPkts": efdmimBdgPortErrorPkts,
       "efdmimPhyTable": efdmimPhyTable,
       "efdmimPhyEntry": efdmimPhyEntry,
       "efdmimPhyWithold": efdmimPhyWithold,
       "efdmimDeviceStatus": efdmimDeviceStatus,
       "efdmimDeviceBdgName": efdmimDeviceBdgName,
       "efdmimDeviceType": efdmimDeviceType,
       "efdmimDeviceVersion": efdmimDeviceVersion,
       "efdmimDeviceLocation": efdmimDeviceLocation,
       "efdmimDeviceUptime": efdmimDeviceUptime,
       "efdmimDeviceDisableBridge": efdmimDeviceDisableBridge,
       "efdmimDeviceResetCounters": efdmimDeviceResetCounters,
       "efdmimDeviceSwitchSettings": efdmimDeviceSwitchSettings,
       "efdmimDeviceReceivedPkts": efdmimDeviceReceivedPkts,
       "efdmimDeviceFilteredPkts": efdmimDeviceFilteredPkts,
       "efdmimDeviceForwardedPkts": efdmimDeviceForwardedPkts,
       "efdmimDeviceTransmittedPkts": efdmimDeviceTransmittedPkts,
       "efdmimDeviceErrorPkts": efdmimDeviceErrorPkts,
       "efdmimCfmState": efdmimCfmState,
       "efdmimBypassAttached": efdmimBypassAttached,
       "efdmimOscillations": efdmimOscillations,
       "efdmimRingUpTime": efdmimRingUpTime,
       "efdmimDownstreamMac": efdmimDownstreamMac,
       "efdmimBypassStuck": efdmimBypassStuck,
       "efdmimMode": efdmimMode,
       "efdmimRmtState": efdmimRmtState,
       "efdmimDeviceBridgeAddr": efdmimDeviceBridgeAddr}
)
