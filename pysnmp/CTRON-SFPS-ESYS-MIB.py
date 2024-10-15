# SNMP MIB module (CTRON-SFPS-ESYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-ESYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:23 2024
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

(sfpsATMAnibIfoStats,
 sfpsATMElan,
 sfpsATMPorts,
 sfpsATMPortsMgr,
 sfpsATMResolver,
 sfpsATMResolverCounters,
 sfpsATMSvcHistoryEvent,
 sfpsATMSvcHistoryMgr,
 sfpsMemHeapStats,
 sfpsSystemConfig,
 sfpsSystemPool,
 sfpsSystemStats) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsATMAnibIfoStats",
    "sfpsATMElan",
    "sfpsATMPorts",
    "sfpsATMPortsMgr",
    "sfpsATMResolver",
    "sfpsATMResolverCounters",
    "sfpsATMSvcHistoryEvent",
    "sfpsATMSvcHistoryMgr",
    "sfpsMemHeapStats",
    "sfpsSystemConfig",
    "sfpsSystemPool",
    "sfpsSystemStats")

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



class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""




class SfpsSwitchInstance(Integer32):
    """Custom type SfpsSwitchInstance based on Integer32"""




class SfpsAddress(OctetString):
    """Custom type SfpsAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsSysConfigTable_Object = MibTable
sfpsSysConfigTable = _SfpsSysConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsSysConfigTable.setStatus("mandatory")
_SfpsSysConfigEntry_Object = MibTableRow
sfpsSysConfigEntry = _SfpsSysConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1)
)
sfpsSysConfigEntry.setIndexNames(
    (0, "CTRON-SFPS-ESYS-MIB", "sfpsSysConfigSwitchInstance"),
)
if mibBuilder.loadTexts:
    sfpsSysConfigEntry.setStatus("mandatory")
_SfpsSysConfigSwitchInstance_Type = Integer32
_SfpsSysConfigSwitchInstance_Object = MibTableColumn
sfpsSysConfigSwitchInstance = _SfpsSysConfigSwitchInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 1),
    _SfpsSysConfigSwitchInstance_Type()
)
sfpsSysConfigSwitchInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigSwitchInstance.setStatus("mandatory")


class _SfpsSysConfigAdminStatus_Type(Integer32):
    """Custom type sfpsSysConfigAdminStatus based on Integer32"""
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


_SfpsSysConfigAdminStatus_Type.__name__ = "Integer32"
_SfpsSysConfigAdminStatus_Object = MibTableColumn
sfpsSysConfigAdminStatus = _SfpsSysConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 2),
    _SfpsSysConfigAdminStatus_Type()
)
sfpsSysConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSysConfigAdminStatus.setStatus("mandatory")


class _SfpsSysConfigAdminReset_Type(Integer32):
    """Custom type sfpsSysConfigAdminReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_SfpsSysConfigAdminReset_Type.__name__ = "Integer32"
_SfpsSysConfigAdminReset_Object = MibTableColumn
sfpsSysConfigAdminReset = _SfpsSysConfigAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 3),
    _SfpsSysConfigAdminReset_Type()
)
sfpsSysConfigAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSysConfigAdminReset.setStatus("mandatory")


class _SfpsSysConfigOperStatus_Type(Integer32):
    """Custom type sfpsSysConfigOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_SfpsSysConfigOperStatus_Type.__name__ = "Integer32"
_SfpsSysConfigOperStatus_Object = MibTableColumn
sfpsSysConfigOperStatus = _SfpsSysConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 4),
    _SfpsSysConfigOperStatus_Type()
)
sfpsSysConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigOperStatus.setStatus("mandatory")
_SfpsSysConfigOperTime_Type = TimeTicks
_SfpsSysConfigOperTime_Object = MibTableColumn
sfpsSysConfigOperTime = _SfpsSysConfigOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 5),
    _SfpsSysConfigOperTime_Type()
)
sfpsSysConfigOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigOperTime.setStatus("mandatory")
_SfpsSysConfigLastChange_Type = TimeTicks
_SfpsSysConfigLastChange_Object = MibTableColumn
sfpsSysConfigLastChange = _SfpsSysConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 6),
    _SfpsSysConfigLastChange_Type()
)
sfpsSysConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigLastChange.setStatus("mandatory")
_SfpsSysConfigVersion_Type = DisplayString
_SfpsSysConfigVersion_Object = MibTableColumn
sfpsSysConfigVersion = _SfpsSysConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 7),
    _SfpsSysConfigVersion_Type()
)
sfpsSysConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigVersion.setStatus("mandatory")
_SfpsSysConfigMIBRev_Type = DisplayString
_SfpsSysConfigMIBRev_Object = MibTableColumn
sfpsSysConfigMIBRev = _SfpsSysConfigMIBRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 8),
    _SfpsSysConfigMIBRev_Type()
)
sfpsSysConfigMIBRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigMIBRev.setStatus("mandatory")
_SfpsSysConfigHostMgmtPort_Type = Integer32
_SfpsSysConfigHostMgmtPort_Object = MibTableColumn
sfpsSysConfigHostMgmtPort = _SfpsSysConfigHostMgmtPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 9),
    _SfpsSysConfigHostMgmtPort_Type()
)
sfpsSysConfigHostMgmtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSysConfigHostMgmtPort.setStatus("mandatory")
_SfpsSysConfigHostCtrlPort_Type = Integer32
_SfpsSysConfigHostCtrlPort_Object = MibTableColumn
sfpsSysConfigHostCtrlPort = _SfpsSysConfigHostCtrlPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 10),
    _SfpsSysConfigHostCtrlPort_Type()
)
sfpsSysConfigHostCtrlPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigHostCtrlPort.setStatus("mandatory")
_SfpsSysConfigHostDataPort_Type = Integer32
_SfpsSysConfigHostDataPort_Object = MibTableColumn
sfpsSysConfigHostDataPort = _SfpsSysConfigHostDataPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 11),
    _SfpsSysConfigHostDataPort_Type()
)
sfpsSysConfigHostDataPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigHostDataPort.setStatus("mandatory")
_SfpsSysConfigHostCtrlThrottleCount_Type = Integer32
_SfpsSysConfigHostCtrlThrottleCount_Object = MibTableColumn
sfpsSysConfigHostCtrlThrottleCount = _SfpsSysConfigHostCtrlThrottleCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 12),
    _SfpsSysConfigHostCtrlThrottleCount_Type()
)
sfpsSysConfigHostCtrlThrottleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigHostCtrlThrottleCount.setStatus("mandatory")
_SfpsSysConfigHostDataThrottleCount_Type = Integer32
_SfpsSysConfigHostDataThrottleCount_Object = MibTableColumn
sfpsSysConfigHostDataThrottleCount = _SfpsSysConfigHostDataThrottleCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 13),
    _SfpsSysConfigHostDataThrottleCount_Type()
)
sfpsSysConfigHostDataThrottleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigHostDataThrottleCount.setStatus("mandatory")
_SfpsSysConfigTrunkSwitch_Type = Integer32
_SfpsSysConfigTrunkSwitch_Object = MibTableColumn
sfpsSysConfigTrunkSwitch = _SfpsSysConfigTrunkSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 14),
    _SfpsSysConfigTrunkSwitch_Type()
)
sfpsSysConfigTrunkSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSysConfigTrunkSwitch.setStatus("mandatory")


class _SfpsSysConfigSwitchMode_Type(Integer32):
    """Custom type sfpsSysConfigSwitchMode based on Integer32"""
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
        *(("aNVLFrontEnd", 4),
          ("aNVLLobo", 3),
          ("vLAN", 2),
          ("vNET", 1))
    )


_SfpsSysConfigSwitchMode_Type.__name__ = "Integer32"
_SfpsSysConfigSwitchMode_Object = MibTableColumn
sfpsSysConfigSwitchMode = _SfpsSysConfigSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 20),
    _SfpsSysConfigSwitchMode_Type()
)
sfpsSysConfigSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSysConfigSwitchMode.setStatus("mandatory")
_SfpsSysConfigSwitchMAC_Type = SfpsAddress
_SfpsSysConfigSwitchMAC_Object = MibTableColumn
sfpsSysConfigSwitchMAC = _SfpsSysConfigSwitchMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 21),
    _SfpsSysConfigSwitchMAC_Type()
)
sfpsSysConfigSwitchMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigSwitchMAC.setStatus("mandatory")


class _SfpsSysConfigMgmtAccessType_Type(Integer32):
    """Custom type sfpsSysConfigMgmtAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mgmt-Only", 1),
          ("mgmt-and-Access", 2))
    )


_SfpsSysConfigMgmtAccessType_Type.__name__ = "Integer32"
_SfpsSysConfigMgmtAccessType_Object = MibTableColumn
sfpsSysConfigMgmtAccessType = _SfpsSysConfigMgmtAccessType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 22),
    _SfpsSysConfigMgmtAccessType_Type()
)
sfpsSysConfigMgmtAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSysConfigMgmtAccessType.setStatus("mandatory")
_SfpsSysConfigChassisMAC_Type = SfpsAddress
_SfpsSysConfigChassisMAC_Object = MibTableColumn
sfpsSysConfigChassisMAC = _SfpsSysConfigChassisMAC_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 23),
    _SfpsSysConfigChassisMAC_Type()
)
sfpsSysConfigChassisMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigChassisMAC.setStatus("mandatory")
_SfpsSysConfigChassisIP_Type = IpAddress
_SfpsSysConfigChassisIP_Object = MibTableColumn
sfpsSysConfigChassisIP = _SfpsSysConfigChassisIP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 1, 1, 1, 24),
    _SfpsSysConfigChassisIP_Type()
)
sfpsSysConfigChassisIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysConfigChassisIP.setStatus("mandatory")
_SfpsSysStatsTable_Object = MibTable
sfpsSysStatsTable = _SfpsSysStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsSysStatsTable.setStatus("mandatory")
_SfpsSysStatsEntry_Object = MibTableRow
sfpsSysStatsEntry = _SfpsSysStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1)
)
sfpsSysStatsEntry.setIndexNames(
    (0, "CTRON-SFPS-ESYS-MIB", "sfpsSysStatsSwitchInstance"),
)
if mibBuilder.loadTexts:
    sfpsSysStatsEntry.setStatus("mandatory")
_SfpsSysStatsSwitchInstance_Type = SfpsSwitchInstance
_SfpsSysStatsSwitchInstance_Object = MibTableColumn
sfpsSysStatsSwitchInstance = _SfpsSysStatsSwitchInstance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 1),
    _SfpsSysStatsSwitchInstance_Type()
)
sfpsSysStatsSwitchInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysStatsSwitchInstance.setStatus("mandatory")


class _SfpsSysStatsAdminStatus_Type(Integer32):
    """Custom type sfpsSysStatsAdminStatus based on Integer32"""
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


_SfpsSysStatsAdminStatus_Type.__name__ = "Integer32"
_SfpsSysStatsAdminStatus_Object = MibTableColumn
sfpsSysStatsAdminStatus = _SfpsSysStatsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 2),
    _SfpsSysStatsAdminStatus_Type()
)
sfpsSysStatsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSysStatsAdminStatus.setStatus("mandatory")


class _SfpsSysStatsReset_Type(Integer32):
    """Custom type sfpsSysStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_SfpsSysStatsReset_Type.__name__ = "Integer32"
_SfpsSysStatsReset_Object = MibTableColumn
sfpsSysStatsReset = _SfpsSysStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 3),
    _SfpsSysStatsReset_Type()
)
sfpsSysStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsSysStatsReset.setStatus("mandatory")
_SfpsSysStatsOperTime_Type = TimeTicks
_SfpsSysStatsOperTime_Object = MibTableColumn
sfpsSysStatsOperTime = _SfpsSysStatsOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 4),
    _SfpsSysStatsOperTime_Type()
)
sfpsSysStatsOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysStatsOperTime.setStatus("mandatory")
_SfpsSysStatsInPkts_Type = Counter32
_SfpsSysStatsInPkts_Object = MibTableColumn
sfpsSysStatsInPkts = _SfpsSysStatsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 5),
    _SfpsSysStatsInPkts_Type()
)
sfpsSysStatsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysStatsInPkts.setStatus("mandatory")
_SfpsSysStatsOutPkts_Type = Counter32
_SfpsSysStatsOutPkts_Object = MibTableColumn
sfpsSysStatsOutPkts = _SfpsSysStatsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 6),
    _SfpsSysStatsOutPkts_Type()
)
sfpsSysStatsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysStatsOutPkts.setStatus("mandatory")
_SfpsSysStatsDiscardPkts_Type = Counter32
_SfpsSysStatsDiscardPkts_Object = MibTableColumn
sfpsSysStatsDiscardPkts = _SfpsSysStatsDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 7),
    _SfpsSysStatsDiscardPkts_Type()
)
sfpsSysStatsDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysStatsDiscardPkts.setStatus("mandatory")
_SfpsSysStatsFilteredPkts_Type = Counter32
_SfpsSysStatsFilteredPkts_Object = MibTableColumn
sfpsSysStatsFilteredPkts = _SfpsSysStatsFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 8),
    _SfpsSysStatsFilteredPkts_Type()
)
sfpsSysStatsFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysStatsFilteredPkts.setStatus("mandatory")
_SfpsSysStatsInOctets_Type = Counter32
_SfpsSysStatsInOctets_Object = MibTableColumn
sfpsSysStatsInOctets = _SfpsSysStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 9),
    _SfpsSysStatsInOctets_Type()
)
sfpsSysStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysStatsInOctets.setStatus("mandatory")
_SfpsSysStatsOutOctets_Type = Counter32
_SfpsSysStatsOutOctets_Object = MibTableColumn
sfpsSysStatsOutOctets = _SfpsSysStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 10),
    _SfpsSysStatsOutOctets_Type()
)
sfpsSysStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysStatsOutOctets.setStatus("mandatory")
_SfpsSysStatsDiscardOctets_Type = Counter32
_SfpsSysStatsDiscardOctets_Object = MibTableColumn
sfpsSysStatsDiscardOctets = _SfpsSysStatsDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 11),
    _SfpsSysStatsDiscardOctets_Type()
)
sfpsSysStatsDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysStatsDiscardOctets.setStatus("mandatory")
_SfpsSysStatsFilteredOctets_Type = Counter32
_SfpsSysStatsFilteredOctets_Object = MibTableColumn
sfpsSysStatsFilteredOctets = _SfpsSysStatsFilteredOctets_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 1, 1, 12),
    _SfpsSysStatsFilteredOctets_Type()
)
sfpsSysStatsFilteredOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsSysStatsFilteredOctets.setStatus("mandatory")
_SfpsMemHeapStatsHeapInit_Type = HexInteger
_SfpsMemHeapStatsHeapInit_Object = MibScalar
sfpsMemHeapStatsHeapInit = _SfpsMemHeapStatsHeapInit_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1, 1),
    _SfpsMemHeapStatsHeapInit_Type()
)
sfpsMemHeapStatsHeapInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMemHeapStatsHeapInit.setStatus("mandatory")
_SfpsMemHeapStatsHeapMax_Type = HexInteger
_SfpsMemHeapStatsHeapMax_Object = MibScalar
sfpsMemHeapStatsHeapMax = _SfpsMemHeapStatsHeapMax_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1, 2),
    _SfpsMemHeapStatsHeapMax_Type()
)
sfpsMemHeapStatsHeapMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMemHeapStatsHeapMax.setStatus("mandatory")
_SfpsMemHeapStatsHeapEnd_Type = HexInteger
_SfpsMemHeapStatsHeapEnd_Object = MibScalar
sfpsMemHeapStatsHeapEnd = _SfpsMemHeapStatsHeapEnd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1, 3),
    _SfpsMemHeapStatsHeapEnd_Type()
)
sfpsMemHeapStatsHeapEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMemHeapStatsHeapEnd.setStatus("mandatory")
_SfpsMemHeapStatsHeapSize_Type = Integer32
_SfpsMemHeapStatsHeapSize_Object = MibScalar
sfpsMemHeapStatsHeapSize = _SfpsMemHeapStatsHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1, 4),
    _SfpsMemHeapStatsHeapSize_Type()
)
sfpsMemHeapStatsHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMemHeapStatsHeapSize.setStatus("mandatory")
_SfpsMemHeapStatsFragCount_Type = Integer32
_SfpsMemHeapStatsFragCount_Object = MibScalar
sfpsMemHeapStatsFragCount = _SfpsMemHeapStatsFragCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1, 5),
    _SfpsMemHeapStatsFragCount_Type()
)
sfpsMemHeapStatsFragCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMemHeapStatsFragCount.setStatus("mandatory")
_SfpsMemHeapStatsFragLargest_Type = Integer32
_SfpsMemHeapStatsFragLargest_Object = MibScalar
sfpsMemHeapStatsFragLargest = _SfpsMemHeapStatsFragLargest_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1, 6),
    _SfpsMemHeapStatsFragLargest_Type()
)
sfpsMemHeapStatsFragLargest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMemHeapStatsFragLargest.setStatus("mandatory")
_SfpsMemHeapStatsFragBytes_Type = Integer32
_SfpsMemHeapStatsFragBytes_Object = MibScalar
sfpsMemHeapStatsFragBytes = _SfpsMemHeapStatsFragBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1, 7),
    _SfpsMemHeapStatsFragBytes_Type()
)
sfpsMemHeapStatsFragBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMemHeapStatsFragBytes.setStatus("mandatory")
_SfpsMemHeapStatsHeapUsed_Type = Integer32
_SfpsMemHeapStatsHeapUsed_Object = MibScalar
sfpsMemHeapStatsHeapUsed = _SfpsMemHeapStatsHeapUsed_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1, 8),
    _SfpsMemHeapStatsHeapUsed_Type()
)
sfpsMemHeapStatsHeapUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMemHeapStatsHeapUsed.setStatus("mandatory")
_SfpsMemHeapStatsHeapAvail_Type = Integer32
_SfpsMemHeapStatsHeapAvail_Object = MibScalar
sfpsMemHeapStatsHeapAvail = _SfpsMemHeapStatsHeapAvail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1, 9),
    _SfpsMemHeapStatsHeapAvail_Type()
)
sfpsMemHeapStatsHeapAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMemHeapStatsHeapAvail.setStatus("mandatory")
_SfpsMemHeapStatsHeapUseMax_Type = OctetString
_SfpsMemHeapStatsHeapUseMax_Object = MibScalar
sfpsMemHeapStatsHeapUseMax = _SfpsMemHeapStatsHeapUseMax_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1, 10),
    _SfpsMemHeapStatsHeapUseMax_Type()
)
sfpsMemHeapStatsHeapUseMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMemHeapStatsHeapUseMax.setStatus("mandatory")
_SfpsMemHeapStatsHeapUsePercent_Type = OctetString
_SfpsMemHeapStatsHeapUsePercent_Object = MibScalar
sfpsMemHeapStatsHeapUsePercent = _SfpsMemHeapStatsHeapUsePercent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 2, 2, 1, 11),
    _SfpsMemHeapStatsHeapUsePercent_Type()
)
sfpsMemHeapStatsHeapUsePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsMemHeapStatsHeapUsePercent.setStatus("mandatory")
_SfpsPoolTable_Object = MibTable
sfpsPoolTable = _SfpsPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    sfpsPoolTable.setStatus("mandatory")
_SfpsPoolTableEntry_Object = MibTableRow
sfpsPoolTableEntry = _SfpsPoolTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1, 1)
)
sfpsPoolTableEntry.setIndexNames(
    (0, "CTRON-SFPS-ESYS-MIB", "sfpsPoolTableIndex"),
)
if mibBuilder.loadTexts:
    sfpsPoolTableEntry.setStatus("mandatory")
_SfpsPoolTableIndex_Type = Integer32
_SfpsPoolTableIndex_Object = MibTableColumn
sfpsPoolTableIndex = _SfpsPoolTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1, 1, 1),
    _SfpsPoolTableIndex_Type()
)
sfpsPoolTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPoolTableIndex.setStatus("mandatory")
_SfpsPoolTableName_Type = DisplayString
_SfpsPoolTableName_Object = MibTableColumn
sfpsPoolTableName = _SfpsPoolTableName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1, 1, 2),
    _SfpsPoolTableName_Type()
)
sfpsPoolTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPoolTableName.setStatus("mandatory")
_SfpsPoolTableRAM_Type = Integer32
_SfpsPoolTableRAM_Object = MibTableColumn
sfpsPoolTableRAM = _SfpsPoolTableRAM_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1, 1, 3),
    _SfpsPoolTableRAM_Type()
)
sfpsPoolTableRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPoolTableRAM.setStatus("mandatory")
_SfpsPoolTableBlockSize_Type = Integer32
_SfpsPoolTableBlockSize_Object = MibTableColumn
sfpsPoolTableBlockSize = _SfpsPoolTableBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1, 1, 4),
    _SfpsPoolTableBlockSize_Type()
)
sfpsPoolTableBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPoolTableBlockSize.setStatus("mandatory")
_SfpsPoolTableBlockCount_Type = Integer32
_SfpsPoolTableBlockCount_Object = MibTableColumn
sfpsPoolTableBlockCount = _SfpsPoolTableBlockCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1, 1, 5),
    _SfpsPoolTableBlockCount_Type()
)
sfpsPoolTableBlockCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPoolTableBlockCount.setStatus("mandatory")
_SfpsPoolTableBlockMax_Type = Integer32
_SfpsPoolTableBlockMax_Object = MibTableColumn
sfpsPoolTableBlockMax = _SfpsPoolTableBlockMax_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1, 1, 6),
    _SfpsPoolTableBlockMax_Type()
)
sfpsPoolTableBlockMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPoolTableBlockMax.setStatus("mandatory")
_SfpsPoolTableObjSize_Type = Integer32
_SfpsPoolTableObjSize_Object = MibTableColumn
sfpsPoolTableObjSize = _SfpsPoolTableObjSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1, 1, 7),
    _SfpsPoolTableObjSize_Type()
)
sfpsPoolTableObjSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPoolTableObjSize.setStatus("mandatory")
_SfpsPoolTableObjInUse_Type = Integer32
_SfpsPoolTableObjInUse_Object = MibTableColumn
sfpsPoolTableObjInUse = _SfpsPoolTableObjInUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1, 1, 8),
    _SfpsPoolTableObjInUse_Type()
)
sfpsPoolTableObjInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPoolTableObjInUse.setStatus("mandatory")
_SfpsPoolTableObjMax_Type = Integer32
_SfpsPoolTableObjMax_Object = MibTableColumn
sfpsPoolTableObjMax = _SfpsPoolTableObjMax_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1, 1, 9),
    _SfpsPoolTableObjMax_Type()
)
sfpsPoolTableObjMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPoolTableObjMax.setStatus("mandatory")
_SfpsPoolTableObjInBlock_Type = Integer32
_SfpsPoolTableObjInBlock_Object = MibTableColumn
sfpsPoolTableObjInBlock = _SfpsPoolTableObjInBlock_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 4, 1, 1, 10),
    _SfpsPoolTableObjInBlock_Type()
)
sfpsPoolTableObjInBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPoolTableObjInBlock.setStatus("mandatory")
_SfpsVccPortTable_Object = MibTable
sfpsVccPortTable = _SfpsVccPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 6)
)
if mibBuilder.loadTexts:
    sfpsVccPortTable.setStatus("mandatory")
_SfpsVccPortEntry_Object = MibTableRow
sfpsVccPortEntry = _SfpsVccPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 6, 1)
)
sfpsVccPortEntry.setIndexNames(
    (0, "CTRON-SFPS-ESYS-MIB", "sfpsVccPortLogPort"),
)
if mibBuilder.loadTexts:
    sfpsVccPortEntry.setStatus("mandatory")
_SfpsVccPortLogPort_Type = Integer32
_SfpsVccPortLogPort_Object = MibTableColumn
sfpsVccPortLogPort = _SfpsVccPortLogPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 6, 1, 1),
    _SfpsVccPortLogPort_Type()
)
sfpsVccPortLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVccPortLogPort.setStatus("mandatory")
_SfpsVccPortPhyPort_Type = Integer32
_SfpsVccPortPhyPort_Object = MibTableColumn
sfpsVccPortPhyPort = _SfpsVccPortPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 6, 1, 2),
    _SfpsVccPortPhyPort_Type()
)
sfpsVccPortPhyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVccPortPhyPort.setStatus("mandatory")
_SfpsVccPortVpi_Type = Integer32
_SfpsVccPortVpi_Object = MibTableColumn
sfpsVccPortVpi = _SfpsVccPortVpi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 6, 1, 3),
    _SfpsVccPortVpi_Type()
)
sfpsVccPortVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVccPortVpi.setStatus("mandatory")
_SfpsVccPortVci_Type = Integer32
_SfpsVccPortVci_Object = MibTableColumn
sfpsVccPortVci = _SfpsVccPortVci_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 6, 1, 4),
    _SfpsVccPortVci_Type()
)
sfpsVccPortVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVccPortVci.setStatus("mandatory")


class _SfpsVccPortPortType_Type(Integer32):
    """Custom type sfpsVccPortPortType based on Integer32"""
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
        *(("atmLec", 1),
          ("atmPvc", 3),
          ("atmSvc", 2),
          ("other", 4))
    )


_SfpsVccPortPortType_Type.__name__ = "Integer32"
_SfpsVccPortPortType_Object = MibTableColumn
sfpsVccPortPortType = _SfpsVccPortPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 6, 1, 5),
    _SfpsVccPortPortType_Type()
)
sfpsVccPortPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVccPortPortType.setStatus("mandatory")


class _SfpsVccPortLogPortType_Type(Integer32):
    """Custom type sfpsVccPortLogPortType based on Integer32"""
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
        *(("other", 4),
          ("pendingUp", 1),
          ("portDown", 3),
          ("portUp", 2))
    )


_SfpsVccPortLogPortType_Type.__name__ = "Integer32"
_SfpsVccPortLogPortType_Object = MibTableColumn
sfpsVccPortLogPortType = _SfpsVccPortLogPortType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 6, 1, 6),
    _SfpsVccPortLogPortType_Type()
)
sfpsVccPortLogPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVccPortLogPortType.setStatus("mandatory")


class _SfpsVccPortPhyLinkState_Type(Integer32):
    """Custom type sfpsVccPortPhyLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("linkUp", 1),
          ("other", 3))
    )


_SfpsVccPortPhyLinkState_Type.__name__ = "Integer32"
_SfpsVccPortPhyLinkState_Object = MibTableColumn
sfpsVccPortPhyLinkState = _SfpsVccPortPhyLinkState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 6, 1, 7),
    _SfpsVccPortPhyLinkState_Type()
)
sfpsVccPortPhyLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsVccPortPhyLinkState.setStatus("mandatory")
_SfpsATMLecPortTable_Object = MibTable
sfpsATMLecPortTable = _SfpsATMLecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 7)
)
if mibBuilder.loadTexts:
    sfpsATMLecPortTable.setStatus("mandatory")
_SfpsATMLecPortTableEntry_Object = MibTableRow
sfpsATMLecPortTableEntry = _SfpsATMLecPortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 7, 1)
)
sfpsATMLecPortTableEntry.setIndexNames(
    (0, "CTRON-SFPS-ESYS-MIB", "sfpsATMLecPortLogPort"),
)
if mibBuilder.loadTexts:
    sfpsATMLecPortTableEntry.setStatus("mandatory")
_SfpsATMLecPortLogPort_Type = Integer32
_SfpsATMLecPortLogPort_Object = MibTableColumn
sfpsATMLecPortLogPort = _SfpsATMLecPortLogPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 7, 1, 1),
    _SfpsATMLecPortLogPort_Type()
)
sfpsATMLecPortLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMLecPortLogPort.setStatus("mandatory")
_SfpsATMLecPortPhyPort_Type = Integer32
_SfpsATMLecPortPhyPort_Object = MibTableColumn
sfpsATMLecPortPhyPort = _SfpsATMLecPortPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 7, 1, 2),
    _SfpsATMLecPortPhyPort_Type()
)
sfpsATMLecPortPhyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMLecPortPhyPort.setStatus("mandatory")
_SfpsATMLecPortElanName_Type = Integer32
_SfpsATMLecPortElanName_Object = MibTableColumn
sfpsATMLecPortElanName = _SfpsATMLecPortElanName_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 7, 1, 3),
    _SfpsATMLecPortElanName_Type()
)
sfpsATMLecPortElanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMLecPortElanName.setStatus("mandatory")
_SfpsATMLecPortPhyLinkState_Type = Integer32
_SfpsATMLecPortPhyLinkState_Object = MibTableColumn
sfpsATMLecPortPhyLinkState = _SfpsATMLecPortPhyLinkState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 7, 1, 4),
    _SfpsATMLecPortPhyLinkState_Type()
)
sfpsATMLecPortPhyLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMLecPortPhyLinkState.setStatus("mandatory")
_SfpsATMLecPortLECType_Type = Integer32
_SfpsATMLecPortLECType_Object = MibTableColumn
sfpsATMLecPortLECType = _SfpsATMLecPortLECType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 1, 7, 1, 5),
    _SfpsATMLecPortLECType_Type()
)
sfpsATMLecPortLECType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMLecPortLECType.setStatus("mandatory")
_SfpsATMResolveSystemLearnTableSize_Type = Integer32
_SfpsATMResolveSystemLearnTableSize_Object = MibScalar
sfpsATMResolveSystemLearnTableSize = _SfpsATMResolveSystemLearnTableSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 1),
    _SfpsATMResolveSystemLearnTableSize_Type()
)
sfpsATMResolveSystemLearnTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMResolveSystemLearnTableSize.setStatus("mandatory")


class _SfpsATMResolveCountersVerb_Type(Integer32):
    """Custom type sfpsATMResolveCountersVerb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_SfpsATMResolveCountersVerb_Type.__name__ = "Integer32"
_SfpsATMResolveCountersVerb_Object = MibScalar
sfpsATMResolveCountersVerb = _SfpsATMResolveCountersVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 1),
    _SfpsATMResolveCountersVerb_Type()
)
sfpsATMResolveCountersVerb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersVerb.setStatus("mandatory")
_SfpsATMResolveCountersUptime_Type = Integer32
_SfpsATMResolveCountersUptime_Object = MibScalar
sfpsATMResolveCountersUptime = _SfpsATMResolveCountersUptime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 2),
    _SfpsATMResolveCountersUptime_Type()
)
sfpsATMResolveCountersUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersUptime.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACReq_Type = Integer32
_SfpsATMResolveCountersQueryMACReq_Object = MibScalar
sfpsATMResolveCountersQueryMACReq = _SfpsATMResolveCountersQueryMACReq_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 3),
    _SfpsATMResolveCountersQueryMACReq_Type()
)
sfpsATMResolveCountersQueryMACReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACReq.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACFail_Type = Integer32
_SfpsATMResolveCountersQueryMACFail_Object = MibScalar
sfpsATMResolveCountersQueryMACFail = _SfpsATMResolveCountersQueryMACFail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 4),
    _SfpsATMResolveCountersQueryMACFail_Type()
)
sfpsATMResolveCountersQueryMACFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACFail.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACGood_Type = Integer32
_SfpsATMResolveCountersQueryMACGood_Object = MibScalar
sfpsATMResolveCountersQueryMACGood = _SfpsATMResolveCountersQueryMACGood_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 5),
    _SfpsATMResolveCountersQueryMACGood_Type()
)
sfpsATMResolveCountersQueryMACGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACGood.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACDaSaChecks_Type = Integer32
_SfpsATMResolveCountersQueryMACDaSaChecks_Object = MibScalar
sfpsATMResolveCountersQueryMACDaSaChecks = _SfpsATMResolveCountersQueryMACDaSaChecks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 6),
    _SfpsATMResolveCountersQueryMACDaSaChecks_Type()
)
sfpsATMResolveCountersQueryMACDaSaChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACDaSaChecks.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACDaSaHits_Type = Integer32
_SfpsATMResolveCountersQueryMACDaSaHits_Object = MibScalar
sfpsATMResolveCountersQueryMACDaSaHits = _SfpsATMResolveCountersQueryMACDaSaHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 7),
    _SfpsATMResolveCountersQueryMACDaSaHits_Type()
)
sfpsATMResolveCountersQueryMACDaSaHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACDaSaHits.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACDaSaMissess_Type = Integer32
_SfpsATMResolveCountersQueryMACDaSaMissess_Object = MibScalar
sfpsATMResolveCountersQueryMACDaSaMissess = _SfpsATMResolveCountersQueryMACDaSaMissess_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 8),
    _SfpsATMResolveCountersQueryMACDaSaMissess_Type()
)
sfpsATMResolveCountersQueryMACDaSaMissess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACDaSaMissess.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACVdirChecks_Type = Integer32
_SfpsATMResolveCountersQueryMACVdirChecks_Object = MibScalar
sfpsATMResolveCountersQueryMACVdirChecks = _SfpsATMResolveCountersQueryMACVdirChecks_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 9),
    _SfpsATMResolveCountersQueryMACVdirChecks_Type()
)
sfpsATMResolveCountersQueryMACVdirChecks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACVdirChecks.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACVdirHits_Type = Integer32
_SfpsATMResolveCountersQueryMACVdirHits_Object = MibScalar
sfpsATMResolveCountersQueryMACVdirHits = _SfpsATMResolveCountersQueryMACVdirHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 10),
    _SfpsATMResolveCountersQueryMACVdirHits_Type()
)
sfpsATMResolveCountersQueryMACVdirHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACVdirHits.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACVdirMisses_Type = Integer32
_SfpsATMResolveCountersQueryMACVdirMisses_Object = MibScalar
sfpsATMResolveCountersQueryMACVdirMisses = _SfpsATMResolveCountersQueryMACVdirMisses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 11),
    _SfpsATMResolveCountersQueryMACVdirMisses_Type()
)
sfpsATMResolveCountersQueryMACVdirMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACVdirMisses.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACErrors_Type = Integer32
_SfpsATMResolveCountersQueryMACErrors_Object = MibScalar
sfpsATMResolveCountersQueryMACErrors = _SfpsATMResolveCountersQueryMACErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 12),
    _SfpsATMResolveCountersQueryMACErrors_Type()
)
sfpsATMResolveCountersQueryMACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACErrors.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACLecPortSuppress_Type = Integer32
_SfpsATMResolveCountersQueryMACLecPortSuppress_Object = MibScalar
sfpsATMResolveCountersQueryMACLecPortSuppress = _SfpsATMResolveCountersQueryMACLecPortSuppress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 13),
    _SfpsATMResolveCountersQueryMACLecPortSuppress_Type()
)
sfpsATMResolveCountersQueryMACLecPortSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACLecPortSuppress.setStatus("mandatory")
_SfpsATMResolveCountersQueryMACStandbyDrops_Type = Integer32
_SfpsATMResolveCountersQueryMACStandbyDrops_Object = MibScalar
sfpsATMResolveCountersQueryMACStandbyDrops = _SfpsATMResolveCountersQueryMACStandbyDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 14),
    _SfpsATMResolveCountersQueryMACStandbyDrops_Type()
)
sfpsATMResolveCountersQueryMACStandbyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryMACStandbyDrops.setStatus("mandatory")
_SfpsATMResolveCountersQueryDaSaRequests_Type = Integer32
_SfpsATMResolveCountersQueryDaSaRequests_Object = MibScalar
sfpsATMResolveCountersQueryDaSaRequests = _SfpsATMResolveCountersQueryDaSaRequests_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 15),
    _SfpsATMResolveCountersQueryDaSaRequests_Type()
)
sfpsATMResolveCountersQueryDaSaRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryDaSaRequests.setStatus("mandatory")
_SfpsATMResolveCountersQueryDaSaHits_Type = Integer32
_SfpsATMResolveCountersQueryDaSaHits_Object = MibScalar
sfpsATMResolveCountersQueryDaSaHits = _SfpsATMResolveCountersQueryDaSaHits_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 16),
    _SfpsATMResolveCountersQueryDaSaHits_Type()
)
sfpsATMResolveCountersQueryDaSaHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryDaSaHits.setStatus("mandatory")
_SfpsATMResolveCountersQueryDaSaMisses_Type = Integer32
_SfpsATMResolveCountersQueryDaSaMisses_Object = MibScalar
sfpsATMResolveCountersQueryDaSaMisses = _SfpsATMResolveCountersQueryDaSaMisses_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 17),
    _SfpsATMResolveCountersQueryDaSaMisses_Type()
)
sfpsATMResolveCountersQueryDaSaMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryDaSaMisses.setStatus("mandatory")
_SfpsATMResolveCountersQueryDaSaErrors_Type = Integer32
_SfpsATMResolveCountersQueryDaSaErrors_Object = MibScalar
sfpsATMResolveCountersQueryDaSaErrors = _SfpsATMResolveCountersQueryDaSaErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 2, 18),
    _SfpsATMResolveCountersQueryDaSaErrors_Type()
)
sfpsATMResolveCountersQueryDaSaErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveCountersQueryDaSaErrors.setStatus("mandatory")
_SfpsATMResolveDiagAPIVerb_Type = Integer32
_SfpsATMResolveDiagAPIVerb_Object = MibScalar
sfpsATMResolveDiagAPIVerb = _SfpsATMResolveDiagAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 3),
    _SfpsATMResolveDiagAPIVerb_Type()
)
sfpsATMResolveDiagAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMResolveDiagAPIVerb.setStatus("mandatory")
_SfpsATMResolveDiagAPIInDA_Type = Integer32
_SfpsATMResolveDiagAPIInDA_Object = MibScalar
sfpsATMResolveDiagAPIInDA = _SfpsATMResolveDiagAPIInDA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 8),
    _SfpsATMResolveDiagAPIInDA_Type()
)
sfpsATMResolveDiagAPIInDA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMResolveDiagAPIInDA.setStatus("mandatory")
_SfpsATMResolveDiagAPIInSA_Type = Integer32
_SfpsATMResolveDiagAPIInSA_Object = MibScalar
sfpsATMResolveDiagAPIInSA = _SfpsATMResolveDiagAPIInSA_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 9),
    _SfpsATMResolveDiagAPIInSA_Type()
)
sfpsATMResolveDiagAPIInSA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMResolveDiagAPIInSA.setStatus("mandatory")
_SfpsATMResolveDiagAPIInSrcLecPort_Type = Integer32
_SfpsATMResolveDiagAPIInSrcLecPort_Object = MibScalar
sfpsATMResolveDiagAPIInSrcLecPort = _SfpsATMResolveDiagAPIInSrcLecPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 10),
    _SfpsATMResolveDiagAPIInSrcLecPort_Type()
)
sfpsATMResolveDiagAPIInSrcLecPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMResolveDiagAPIInSrcLecPort.setStatus("mandatory")
_SfpsATMResolveDiagAPIOutStatus_Type = Integer32
_SfpsATMResolveDiagAPIOutStatus_Object = MibScalar
sfpsATMResolveDiagAPIOutStatus = _SfpsATMResolveDiagAPIOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 11),
    _SfpsATMResolveDiagAPIOutStatus_Type()
)
sfpsATMResolveDiagAPIOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveDiagAPIOutStatus.setStatus("mandatory")
_SfpsATMResolveDiagAPIOutPort_Type = Integer32
_SfpsATMResolveDiagAPIOutPort_Object = MibScalar
sfpsATMResolveDiagAPIOutPort = _SfpsATMResolveDiagAPIOutPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 3, 12),
    _SfpsATMResolveDiagAPIOutPort_Type()
)
sfpsATMResolveDiagAPIOutPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMResolveDiagAPIOutPort.setStatus("mandatory")
_SfpsAnibIfoStatsTable_Object = MibTable
sfpsAnibIfoStatsTable = _SfpsAnibIfoStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsTable.setStatus("mandatory")
_SfpsAnibIfoStatsTableEntry_Object = MibTableRow
sfpsAnibIfoStatsTableEntry = _SfpsAnibIfoStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1)
)
sfpsAnibIfoStatsTableEntry.setIndexNames(
    (0, "CTRON-SFPS-ESYS-MIB", "sfpsAnibIfoStatsPhysIntf"),
)
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsTableEntry.setStatus("mandatory")
_SfpsAnibIfoStatsPhysIntf_Type = Integer32
_SfpsAnibIfoStatsPhysIntf_Object = MibTableColumn
sfpsAnibIfoStatsPhysIntf = _SfpsAnibIfoStatsPhysIntf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 1),
    _SfpsAnibIfoStatsPhysIntf_Type()
)
sfpsAnibIfoStatsPhysIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsPhysIntf.setStatus("mandatory")
_SfpsAnibIfoStatsCtrlMessages_Type = Integer32
_SfpsAnibIfoStatsCtrlMessages_Object = MibTableColumn
sfpsAnibIfoStatsCtrlMessages = _SfpsAnibIfoStatsCtrlMessages_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 2),
    _SfpsAnibIfoStatsCtrlMessages_Type()
)
sfpsAnibIfoStatsCtrlMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsCtrlMessages.setStatus("mandatory")
_SfpsAnibIfoStatsIlmiMessages_Type = Integer32
_SfpsAnibIfoStatsIlmiMessages_Object = MibTableColumn
sfpsAnibIfoStatsIlmiMessages = _SfpsAnibIfoStatsIlmiMessages_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 3),
    _SfpsAnibIfoStatsIlmiMessages_Type()
)
sfpsAnibIfoStatsIlmiMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsIlmiMessages.setStatus("mandatory")
_SfpsAnibIfoStatsUniMessages_Type = Integer32
_SfpsAnibIfoStatsUniMessages_Object = MibTableColumn
sfpsAnibIfoStatsUniMessages = _SfpsAnibIfoStatsUniMessages_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 4),
    _SfpsAnibIfoStatsUniMessages_Type()
)
sfpsAnibIfoStatsUniMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsUniMessages.setStatus("mandatory")
_SfpsAnibIfoStatsLaneMessages_Type = Integer32
_SfpsAnibIfoStatsLaneMessages_Object = MibTableColumn
sfpsAnibIfoStatsLaneMessages = _SfpsAnibIfoStatsLaneMessages_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 5),
    _SfpsAnibIfoStatsLaneMessages_Type()
)
sfpsAnibIfoStatsLaneMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsLaneMessages.setStatus("mandatory")
_SfpsAnibIfoStatsPCSPoolSize_Type = Integer32
_SfpsAnibIfoStatsPCSPoolSize_Object = MibTableColumn
sfpsAnibIfoStatsPCSPoolSize = _SfpsAnibIfoStatsPCSPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 6),
    _SfpsAnibIfoStatsPCSPoolSize_Type()
)
sfpsAnibIfoStatsPCSPoolSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsPCSPoolSize.setStatus("mandatory")
_SfpsAnibIfoStatsPCSPoolDrops_Type = Integer32
_SfpsAnibIfoStatsPCSPoolDrops_Object = MibTableColumn
sfpsAnibIfoStatsPCSPoolDrops = _SfpsAnibIfoStatsPCSPoolDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 7),
    _SfpsAnibIfoStatsPCSPoolDrops_Type()
)
sfpsAnibIfoStatsPCSPoolDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsPCSPoolDrops.setStatus("mandatory")
_SfpsAnibIfoStatsPoolIlmiDrops_Type = Integer32
_SfpsAnibIfoStatsPoolIlmiDrops_Object = MibTableColumn
sfpsAnibIfoStatsPoolIlmiDrops = _SfpsAnibIfoStatsPoolIlmiDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 8),
    _SfpsAnibIfoStatsPoolIlmiDrops_Type()
)
sfpsAnibIfoStatsPoolIlmiDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsPoolIlmiDrops.setStatus("mandatory")
_SfpsAnibIfoStatsPoolUniDrops_Type = Integer32
_SfpsAnibIfoStatsPoolUniDrops_Object = MibTableColumn
sfpsAnibIfoStatsPoolUniDrops = _SfpsAnibIfoStatsPoolUniDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 9),
    _SfpsAnibIfoStatsPoolUniDrops_Type()
)
sfpsAnibIfoStatsPoolUniDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsPoolUniDrops.setStatus("mandatory")
_SfpsAnibIfoStatsPCSAvail_Type = Integer32
_SfpsAnibIfoStatsPCSAvail_Object = MibTableColumn
sfpsAnibIfoStatsPCSAvail = _SfpsAnibIfoStatsPCSAvail_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 11),
    _SfpsAnibIfoStatsPCSAvail_Type()
)
sfpsAnibIfoStatsPCSAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsPCSAvail.setStatus("mandatory")
_SfpsAnibIfoStatsPCSInUse_Type = Integer32
_SfpsAnibIfoStatsPCSInUse_Object = MibTableColumn
sfpsAnibIfoStatsPCSInUse = _SfpsAnibIfoStatsPCSInUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 12),
    _SfpsAnibIfoStatsPCSInUse_Type()
)
sfpsAnibIfoStatsPCSInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsPCSInUse.setStatus("mandatory")
_SfpsAnibIfoStatsStandbyLeArpsDrops_Type = Integer32
_SfpsAnibIfoStatsStandbyLeArpsDrops_Object = MibTableColumn
sfpsAnibIfoStatsStandbyLeArpsDrops = _SfpsAnibIfoStatsStandbyLeArpsDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 13),
    _SfpsAnibIfoStatsStandbyLeArpsDrops_Type()
)
sfpsAnibIfoStatsStandbyLeArpsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsStandbyLeArpsDrops.setStatus("mandatory")
_SfpsAnibIfoStatsStandbyUnknownsDrops_Type = Integer32
_SfpsAnibIfoStatsStandbyUnknownsDrops_Object = MibTableColumn
sfpsAnibIfoStatsStandbyUnknownsDrops = _SfpsAnibIfoStatsStandbyUnknownsDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 14),
    _SfpsAnibIfoStatsStandbyUnknownsDrops_Type()
)
sfpsAnibIfoStatsStandbyUnknownsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsStandbyUnknownsDrops.setStatus("mandatory")
_SfpsAnibIfoStatsStandbyANIBUnknownsDrops_Type = Integer32
_SfpsAnibIfoStatsStandbyANIBUnknownsDrops_Object = MibTableColumn
sfpsAnibIfoStatsStandbyANIBUnknownsDrops = _SfpsAnibIfoStatsStandbyANIBUnknownsDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 15),
    _SfpsAnibIfoStatsStandbyANIBUnknownsDrops_Type()
)
sfpsAnibIfoStatsStandbyANIBUnknownsDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsStandbyANIBUnknownsDrops.setStatus("mandatory")
_SfpsAnibIfoStatsPoolLaneDrops_Type = Integer32
_SfpsAnibIfoStatsPoolLaneDrops_Object = MibTableColumn
sfpsAnibIfoStatsPoolLaneDrops = _SfpsAnibIfoStatsPoolLaneDrops_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 4, 1, 1, 19),
    _SfpsAnibIfoStatsPoolLaneDrops_Type()
)
sfpsAnibIfoStatsPoolLaneDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsAnibIfoStatsPoolLaneDrops.setStatus("mandatory")
_SfpsATMPortsTable_Object = MibTable
sfpsATMPortsTable = _SfpsATMPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    sfpsATMPortsTable.setStatus("mandatory")
_SfpsATMPortsTableEntry_Object = MibTableRow
sfpsATMPortsTableEntry = _SfpsATMPortsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 1, 1)
)
sfpsATMPortsTableEntry.setIndexNames(
    (0, "CTRON-SFPS-ESYS-MIB", "sfpsATMPortsPhysIntf"),
)
if mibBuilder.loadTexts:
    sfpsATMPortsTableEntry.setStatus("mandatory")
_SfpsATMPortsPhysIntf_Type = Integer32
_SfpsATMPortsPhysIntf_Object = MibTableColumn
sfpsATMPortsPhysIntf = _SfpsATMPortsPhysIntf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 1, 1, 1),
    _SfpsATMPortsPhysIntf_Type()
)
sfpsATMPortsPhysIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMPortsPhysIntf.setStatus("mandatory")
_SfpsATMPortsTotalLECPorts_Type = Integer32
_SfpsATMPortsTotalLECPorts_Object = MibTableColumn
sfpsATMPortsTotalLECPorts = _SfpsATMPortsTotalLECPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 1, 1, 2),
    _SfpsATMPortsTotalLECPorts_Type()
)
sfpsATMPortsTotalLECPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMPortsTotalLECPorts.setStatus("mandatory")
_SfpsATMPortsTotalPVCPorts_Type = Integer32
_SfpsATMPortsTotalPVCPorts_Object = MibTableColumn
sfpsATMPortsTotalPVCPorts = _SfpsATMPortsTotalPVCPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 1, 1, 3),
    _SfpsATMPortsTotalPVCPorts_Type()
)
sfpsATMPortsTotalPVCPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMPortsTotalPVCPorts.setStatus("mandatory")
_SfpsATMPortsTotalSVCPorts_Type = Integer32
_SfpsATMPortsTotalSVCPorts_Object = MibTableColumn
sfpsATMPortsTotalSVCPorts = _SfpsATMPortsTotalSVCPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 1, 1, 4),
    _SfpsATMPortsTotalSVCPorts_Type()
)
sfpsATMPortsTotalSVCPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMPortsTotalSVCPorts.setStatus("mandatory")
_SfpsATMPortsBaseIntfNum_Type = Integer32
_SfpsATMPortsBaseIntfNum_Object = MibTableColumn
sfpsATMPortsBaseIntfNum = _SfpsATMPortsBaseIntfNum_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 1, 1, 5),
    _SfpsATMPortsBaseIntfNum_Type()
)
sfpsATMPortsBaseIntfNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMPortsBaseIntfNum.setStatus("mandatory")
_SfpsATMPortsInUse_Type = Integer32
_SfpsATMPortsInUse_Object = MibTableColumn
sfpsATMPortsInUse = _SfpsATMPortsInUse_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 1, 1, 6),
    _SfpsATMPortsInUse_Type()
)
sfpsATMPortsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMPortsInUse.setStatus("mandatory")


class _SfpsATMPortsMgrVerb_Type(Integer32):
    """Custom type sfpsATMPortsMgrVerb based on Integer32"""
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
        *(("coldResetNV", 4),
          ("other", 1),
          ("set", 2),
          ("setToDefaults", 3),
          ("warmResetNB", 5))
    )


_SfpsATMPortsMgrVerb_Type.__name__ = "Integer32"
_SfpsATMPortsMgrVerb_Object = MibScalar
sfpsATMPortsMgrVerb = _SfpsATMPortsMgrVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 2, 1),
    _SfpsATMPortsMgrVerb_Type()
)
sfpsATMPortsMgrVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMPortsMgrVerb.setStatus("mandatory")
_SfpsATMPortsMgrPhysIntf_Type = Integer32
_SfpsATMPortsMgrPhysIntf_Object = MibScalar
sfpsATMPortsMgrPhysIntf = _SfpsATMPortsMgrPhysIntf_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 2, 2),
    _SfpsATMPortsMgrPhysIntf_Type()
)
sfpsATMPortsMgrPhysIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMPortsMgrPhysIntf.setStatus("mandatory")
_SfpsATMPortsMgrTotalLECPorts_Type = Integer32
_SfpsATMPortsMgrTotalLECPorts_Object = MibScalar
sfpsATMPortsMgrTotalLECPorts = _SfpsATMPortsMgrTotalLECPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 2, 3),
    _SfpsATMPortsMgrTotalLECPorts_Type()
)
sfpsATMPortsMgrTotalLECPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMPortsMgrTotalLECPorts.setStatus("mandatory")
_SfpsATMPortsMgrTotalPVCPorts_Type = Integer32
_SfpsATMPortsMgrTotalPVCPorts_Object = MibScalar
sfpsATMPortsMgrTotalPVCPorts = _SfpsATMPortsMgrTotalPVCPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 2, 4),
    _SfpsATMPortsMgrTotalPVCPorts_Type()
)
sfpsATMPortsMgrTotalPVCPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMPortsMgrTotalPVCPorts.setStatus("mandatory")
_SfpsATMPortsMgrTotalSVCPorts_Type = Integer32
_SfpsATMPortsMgrTotalSVCPorts_Object = MibScalar
sfpsATMPortsMgrTotalSVCPorts = _SfpsATMPortsMgrTotalSVCPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 2, 5),
    _SfpsATMPortsMgrTotalSVCPorts_Type()
)
sfpsATMPortsMgrTotalSVCPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMPortsMgrTotalSVCPorts.setStatus("mandatory")


class _SfpsATMPortsMgrVerbStatus_Type(Integer32):
    """Custom type sfpsATMPortsMgrVerbStatus based on Integer32"""
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
        *(("badIf", 3),
          ("error", 4),
          ("exceededMaxAllotment", 2),
          ("ok", 1))
    )


_SfpsATMPortsMgrVerbStatus_Type.__name__ = "Integer32"
_SfpsATMPortsMgrVerbStatus_Object = MibScalar
sfpsATMPortsMgrVerbStatus = _SfpsATMPortsMgrVerbStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 5, 2, 6),
    _SfpsATMPortsMgrVerbStatus_Type()
)
sfpsATMPortsMgrVerbStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMPortsMgrVerbStatus.setStatus("mandatory")


class _SfpsATMSvcHistoryMgrVerb_Type(Integer32):
    """Custom type sfpsATMSvcHistoryMgrVerb based on Integer32"""
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
        *(("enableSvcLogging", 4),
          ("enableSvcLogsNoWrapping", 5),
          ("isableSvcLogging", 3),
          ("other", 1),
          ("resetSvcHistory", 2))
    )


_SfpsATMSvcHistoryMgrVerb_Type.__name__ = "Integer32"
_SfpsATMSvcHistoryMgrVerb_Object = MibScalar
sfpsATMSvcHistoryMgrVerb = _SfpsATMSvcHistoryMgrVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 1, 1),
    _SfpsATMSvcHistoryMgrVerb_Type()
)
sfpsATMSvcHistoryMgrVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryMgrVerb.setStatus("mandatory")
_SfpsATMSvcHistoryMgrSvcHistoryWraps_Type = Integer32
_SfpsATMSvcHistoryMgrSvcHistoryWraps_Object = MibScalar
sfpsATMSvcHistoryMgrSvcHistoryWraps = _SfpsATMSvcHistoryMgrSvcHistoryWraps_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 1, 2),
    _SfpsATMSvcHistoryMgrSvcHistoryWraps_Type()
)
sfpsATMSvcHistoryMgrSvcHistoryWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryMgrSvcHistoryWraps.setStatus("mandatory")


class _SfpsATMSvcHistoryMgrLogState_Type(Integer32):
    """Custom type sfpsATMSvcHistoryMgrLogState based on Integer32"""
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
          ("enabled", 1),
          ("enabledNoWrap", 2))
    )


_SfpsATMSvcHistoryMgrLogState_Type.__name__ = "Integer32"
_SfpsATMSvcHistoryMgrLogState_Object = MibScalar
sfpsATMSvcHistoryMgrLogState = _SfpsATMSvcHistoryMgrLogState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 1, 3),
    _SfpsATMSvcHistoryMgrLogState_Type()
)
sfpsATMSvcHistoryMgrLogState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryMgrLogState.setStatus("mandatory")
_SfpsATMSvcHistoryMgrEntriesCount_Type = Integer32
_SfpsATMSvcHistoryMgrEntriesCount_Object = MibScalar
sfpsATMSvcHistoryMgrEntriesCount = _SfpsATMSvcHistoryMgrEntriesCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 1, 4),
    _SfpsATMSvcHistoryMgrEntriesCount_Type()
)
sfpsATMSvcHistoryMgrEntriesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryMgrEntriesCount.setStatus("mandatory")
_SfpsATMSvcHistoryEventTable_Object = MibTable
sfpsATMSvcHistoryEventTable = _SfpsATMSvcHistoryEventTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryEventTable.setStatus("mandatory")
_SfpsATMSvcHistoryEventTableEntry_Object = MibTableRow
sfpsATMSvcHistoryEventTableEntry = _SfpsATMSvcHistoryEventTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2, 1, 1)
)
sfpsATMSvcHistoryEventTableEntry.setIndexNames(
    (0, "CTRON-SFPS-ESYS-MIB", "sfpsATMSvcHistoryEventIndex"),
)
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryEventTableEntry.setStatus("mandatory")
_SfpsATMSvcHistoryEventIndex_Type = Integer32
_SfpsATMSvcHistoryEventIndex_Object = MibTableColumn
sfpsATMSvcHistoryEventIndex = _SfpsATMSvcHistoryEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2, 1, 1, 1),
    _SfpsATMSvcHistoryEventIndex_Type()
)
sfpsATMSvcHistoryEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryEventIndex.setStatus("mandatory")
_SfpsATMSvcHistoryEventATMAddr_Type = OctetString
_SfpsATMSvcHistoryEventATMAddr_Object = MibTableColumn
sfpsATMSvcHistoryEventATMAddr = _SfpsATMSvcHistoryEventATMAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2, 1, 1, 2),
    _SfpsATMSvcHistoryEventATMAddr_Type()
)
sfpsATMSvcHistoryEventATMAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryEventATMAddr.setStatus("mandatory")
_SfpsATMSvcHistoryEventPortNumber_Type = Integer32
_SfpsATMSvcHistoryEventPortNumber_Object = MibTableColumn
sfpsATMSvcHistoryEventPortNumber = _SfpsATMSvcHistoryEventPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2, 1, 1, 3),
    _SfpsATMSvcHistoryEventPortNumber_Type()
)
sfpsATMSvcHistoryEventPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryEventPortNumber.setStatus("mandatory")


class _SfpsATMSvcHistoryEventEvent_Type(Integer32):
    """Custom type sfpsATMSvcHistoryEventEvent based on Integer32"""
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
        *(("clean", 10),
          ("cleanCloseAck", 12),
          ("cleanCloseResp", 11),
          ("close", 9),
          ("closeAck", 8),
          ("closeResponse", 7),
          ("idle", 1),
          ("open", 6),
          ("openAck", 5),
          ("openResponse", 3),
          ("opening", 2),
          ("peerOpenResponse", 4))
    )


_SfpsATMSvcHistoryEventEvent_Type.__name__ = "Integer32"
_SfpsATMSvcHistoryEventEvent_Object = MibTableColumn
sfpsATMSvcHistoryEventEvent = _SfpsATMSvcHistoryEventEvent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2, 1, 1, 4),
    _SfpsATMSvcHistoryEventEvent_Type()
)
sfpsATMSvcHistoryEventEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryEventEvent.setStatus("mandatory")


class _SfpsATMSvcHistoryEventEventChange_Type(Integer32):
    """Custom type sfpsATMSvcHistoryEventEventChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("normal", 2))
    )


_SfpsATMSvcHistoryEventEventChange_Type.__name__ = "Integer32"
_SfpsATMSvcHistoryEventEventChange_Object = MibTableColumn
sfpsATMSvcHistoryEventEventChange = _SfpsATMSvcHistoryEventEventChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2, 1, 1, 5),
    _SfpsATMSvcHistoryEventEventChange_Type()
)
sfpsATMSvcHistoryEventEventChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryEventEventChange.setStatus("mandatory")
_SfpsATMSvcHistoryEventVccHand_Type = Integer32
_SfpsATMSvcHistoryEventVccHand_Object = MibTableColumn
sfpsATMSvcHistoryEventVccHand = _SfpsATMSvcHistoryEventVccHand_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2, 1, 1, 6),
    _SfpsATMSvcHistoryEventVccHand_Type()
)
sfpsATMSvcHistoryEventVccHand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryEventVccHand.setStatus("mandatory")
_SfpsATMSvcHistoryEventVpi_Type = Integer32
_SfpsATMSvcHistoryEventVpi_Object = MibTableColumn
sfpsATMSvcHistoryEventVpi = _SfpsATMSvcHistoryEventVpi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2, 1, 1, 7),
    _SfpsATMSvcHistoryEventVpi_Type()
)
sfpsATMSvcHistoryEventVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryEventVpi.setStatus("mandatory")
_SfpsATMSvcHistoryEventVci_Type = Integer32
_SfpsATMSvcHistoryEventVci_Object = MibTableColumn
sfpsATMSvcHistoryEventVci = _SfpsATMSvcHistoryEventVci_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2, 1, 1, 8),
    _SfpsATMSvcHistoryEventVci_Type()
)
sfpsATMSvcHistoryEventVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryEventVci.setStatus("mandatory")
_SfpsATMSvcHistoryEventTime_Type = TimeTicks
_SfpsATMSvcHistoryEventTime_Object = MibTableColumn
sfpsATMSvcHistoryEventTime = _SfpsATMSvcHistoryEventTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 4, 8, 2, 1, 1, 9),
    _SfpsATMSvcHistoryEventTime_Type()
)
sfpsATMSvcHistoryEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsATMSvcHistoryEventTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-ESYS-MIB",
    **{"HexInteger": HexInteger,
       "SfpsSwitchInstance": SfpsSwitchInstance,
       "SfpsAddress": SfpsAddress,
       "sfpsSysConfigTable": sfpsSysConfigTable,
       "sfpsSysConfigEntry": sfpsSysConfigEntry,
       "sfpsSysConfigSwitchInstance": sfpsSysConfigSwitchInstance,
       "sfpsSysConfigAdminStatus": sfpsSysConfigAdminStatus,
       "sfpsSysConfigAdminReset": sfpsSysConfigAdminReset,
       "sfpsSysConfigOperStatus": sfpsSysConfigOperStatus,
       "sfpsSysConfigOperTime": sfpsSysConfigOperTime,
       "sfpsSysConfigLastChange": sfpsSysConfigLastChange,
       "sfpsSysConfigVersion": sfpsSysConfigVersion,
       "sfpsSysConfigMIBRev": sfpsSysConfigMIBRev,
       "sfpsSysConfigHostMgmtPort": sfpsSysConfigHostMgmtPort,
       "sfpsSysConfigHostCtrlPort": sfpsSysConfigHostCtrlPort,
       "sfpsSysConfigHostDataPort": sfpsSysConfigHostDataPort,
       "sfpsSysConfigHostCtrlThrottleCount": sfpsSysConfigHostCtrlThrottleCount,
       "sfpsSysConfigHostDataThrottleCount": sfpsSysConfigHostDataThrottleCount,
       "sfpsSysConfigTrunkSwitch": sfpsSysConfigTrunkSwitch,
       "sfpsSysConfigSwitchMode": sfpsSysConfigSwitchMode,
       "sfpsSysConfigSwitchMAC": sfpsSysConfigSwitchMAC,
       "sfpsSysConfigMgmtAccessType": sfpsSysConfigMgmtAccessType,
       "sfpsSysConfigChassisMAC": sfpsSysConfigChassisMAC,
       "sfpsSysConfigChassisIP": sfpsSysConfigChassisIP,
       "sfpsSysStatsTable": sfpsSysStatsTable,
       "sfpsSysStatsEntry": sfpsSysStatsEntry,
       "sfpsSysStatsSwitchInstance": sfpsSysStatsSwitchInstance,
       "sfpsSysStatsAdminStatus": sfpsSysStatsAdminStatus,
       "sfpsSysStatsReset": sfpsSysStatsReset,
       "sfpsSysStatsOperTime": sfpsSysStatsOperTime,
       "sfpsSysStatsInPkts": sfpsSysStatsInPkts,
       "sfpsSysStatsOutPkts": sfpsSysStatsOutPkts,
       "sfpsSysStatsDiscardPkts": sfpsSysStatsDiscardPkts,
       "sfpsSysStatsFilteredPkts": sfpsSysStatsFilteredPkts,
       "sfpsSysStatsInOctets": sfpsSysStatsInOctets,
       "sfpsSysStatsOutOctets": sfpsSysStatsOutOctets,
       "sfpsSysStatsDiscardOctets": sfpsSysStatsDiscardOctets,
       "sfpsSysStatsFilteredOctets": sfpsSysStatsFilteredOctets,
       "sfpsMemHeapStatsHeapInit": sfpsMemHeapStatsHeapInit,
       "sfpsMemHeapStatsHeapMax": sfpsMemHeapStatsHeapMax,
       "sfpsMemHeapStatsHeapEnd": sfpsMemHeapStatsHeapEnd,
       "sfpsMemHeapStatsHeapSize": sfpsMemHeapStatsHeapSize,
       "sfpsMemHeapStatsFragCount": sfpsMemHeapStatsFragCount,
       "sfpsMemHeapStatsFragLargest": sfpsMemHeapStatsFragLargest,
       "sfpsMemHeapStatsFragBytes": sfpsMemHeapStatsFragBytes,
       "sfpsMemHeapStatsHeapUsed": sfpsMemHeapStatsHeapUsed,
       "sfpsMemHeapStatsHeapAvail": sfpsMemHeapStatsHeapAvail,
       "sfpsMemHeapStatsHeapUseMax": sfpsMemHeapStatsHeapUseMax,
       "sfpsMemHeapStatsHeapUsePercent": sfpsMemHeapStatsHeapUsePercent,
       "sfpsPoolTable": sfpsPoolTable,
       "sfpsPoolTableEntry": sfpsPoolTableEntry,
       "sfpsPoolTableIndex": sfpsPoolTableIndex,
       "sfpsPoolTableName": sfpsPoolTableName,
       "sfpsPoolTableRAM": sfpsPoolTableRAM,
       "sfpsPoolTableBlockSize": sfpsPoolTableBlockSize,
       "sfpsPoolTableBlockCount": sfpsPoolTableBlockCount,
       "sfpsPoolTableBlockMax": sfpsPoolTableBlockMax,
       "sfpsPoolTableObjSize": sfpsPoolTableObjSize,
       "sfpsPoolTableObjInUse": sfpsPoolTableObjInUse,
       "sfpsPoolTableObjMax": sfpsPoolTableObjMax,
       "sfpsPoolTableObjInBlock": sfpsPoolTableObjInBlock,
       "sfpsVccPortTable": sfpsVccPortTable,
       "sfpsVccPortEntry": sfpsVccPortEntry,
       "sfpsVccPortLogPort": sfpsVccPortLogPort,
       "sfpsVccPortPhyPort": sfpsVccPortPhyPort,
       "sfpsVccPortVpi": sfpsVccPortVpi,
       "sfpsVccPortVci": sfpsVccPortVci,
       "sfpsVccPortPortType": sfpsVccPortPortType,
       "sfpsVccPortLogPortType": sfpsVccPortLogPortType,
       "sfpsVccPortPhyLinkState": sfpsVccPortPhyLinkState,
       "sfpsATMLecPortTable": sfpsATMLecPortTable,
       "sfpsATMLecPortTableEntry": sfpsATMLecPortTableEntry,
       "sfpsATMLecPortLogPort": sfpsATMLecPortLogPort,
       "sfpsATMLecPortPhyPort": sfpsATMLecPortPhyPort,
       "sfpsATMLecPortElanName": sfpsATMLecPortElanName,
       "sfpsATMLecPortPhyLinkState": sfpsATMLecPortPhyLinkState,
       "sfpsATMLecPortLECType": sfpsATMLecPortLECType,
       "sfpsATMResolveSystemLearnTableSize": sfpsATMResolveSystemLearnTableSize,
       "sfpsATMResolveCountersVerb": sfpsATMResolveCountersVerb,
       "sfpsATMResolveCountersUptime": sfpsATMResolveCountersUptime,
       "sfpsATMResolveCountersQueryMACReq": sfpsATMResolveCountersQueryMACReq,
       "sfpsATMResolveCountersQueryMACFail": sfpsATMResolveCountersQueryMACFail,
       "sfpsATMResolveCountersQueryMACGood": sfpsATMResolveCountersQueryMACGood,
       "sfpsATMResolveCountersQueryMACDaSaChecks": sfpsATMResolveCountersQueryMACDaSaChecks,
       "sfpsATMResolveCountersQueryMACDaSaHits": sfpsATMResolveCountersQueryMACDaSaHits,
       "sfpsATMResolveCountersQueryMACDaSaMissess": sfpsATMResolveCountersQueryMACDaSaMissess,
       "sfpsATMResolveCountersQueryMACVdirChecks": sfpsATMResolveCountersQueryMACVdirChecks,
       "sfpsATMResolveCountersQueryMACVdirHits": sfpsATMResolveCountersQueryMACVdirHits,
       "sfpsATMResolveCountersQueryMACVdirMisses": sfpsATMResolveCountersQueryMACVdirMisses,
       "sfpsATMResolveCountersQueryMACErrors": sfpsATMResolveCountersQueryMACErrors,
       "sfpsATMResolveCountersQueryMACLecPortSuppress": sfpsATMResolveCountersQueryMACLecPortSuppress,
       "sfpsATMResolveCountersQueryMACStandbyDrops": sfpsATMResolveCountersQueryMACStandbyDrops,
       "sfpsATMResolveCountersQueryDaSaRequests": sfpsATMResolveCountersQueryDaSaRequests,
       "sfpsATMResolveCountersQueryDaSaHits": sfpsATMResolveCountersQueryDaSaHits,
       "sfpsATMResolveCountersQueryDaSaMisses": sfpsATMResolveCountersQueryDaSaMisses,
       "sfpsATMResolveCountersQueryDaSaErrors": sfpsATMResolveCountersQueryDaSaErrors,
       "sfpsATMResolveDiagAPIVerb": sfpsATMResolveDiagAPIVerb,
       "sfpsATMResolveDiagAPIInDA": sfpsATMResolveDiagAPIInDA,
       "sfpsATMResolveDiagAPIInSA": sfpsATMResolveDiagAPIInSA,
       "sfpsATMResolveDiagAPIInSrcLecPort": sfpsATMResolveDiagAPIInSrcLecPort,
       "sfpsATMResolveDiagAPIOutStatus": sfpsATMResolveDiagAPIOutStatus,
       "sfpsATMResolveDiagAPIOutPort": sfpsATMResolveDiagAPIOutPort,
       "sfpsAnibIfoStatsTable": sfpsAnibIfoStatsTable,
       "sfpsAnibIfoStatsTableEntry": sfpsAnibIfoStatsTableEntry,
       "sfpsAnibIfoStatsPhysIntf": sfpsAnibIfoStatsPhysIntf,
       "sfpsAnibIfoStatsCtrlMessages": sfpsAnibIfoStatsCtrlMessages,
       "sfpsAnibIfoStatsIlmiMessages": sfpsAnibIfoStatsIlmiMessages,
       "sfpsAnibIfoStatsUniMessages": sfpsAnibIfoStatsUniMessages,
       "sfpsAnibIfoStatsLaneMessages": sfpsAnibIfoStatsLaneMessages,
       "sfpsAnibIfoStatsPCSPoolSize": sfpsAnibIfoStatsPCSPoolSize,
       "sfpsAnibIfoStatsPCSPoolDrops": sfpsAnibIfoStatsPCSPoolDrops,
       "sfpsAnibIfoStatsPoolIlmiDrops": sfpsAnibIfoStatsPoolIlmiDrops,
       "sfpsAnibIfoStatsPoolUniDrops": sfpsAnibIfoStatsPoolUniDrops,
       "sfpsAnibIfoStatsPCSAvail": sfpsAnibIfoStatsPCSAvail,
       "sfpsAnibIfoStatsPCSInUse": sfpsAnibIfoStatsPCSInUse,
       "sfpsAnibIfoStatsStandbyLeArpsDrops": sfpsAnibIfoStatsStandbyLeArpsDrops,
       "sfpsAnibIfoStatsStandbyUnknownsDrops": sfpsAnibIfoStatsStandbyUnknownsDrops,
       "sfpsAnibIfoStatsStandbyANIBUnknownsDrops": sfpsAnibIfoStatsStandbyANIBUnknownsDrops,
       "sfpsAnibIfoStatsPoolLaneDrops": sfpsAnibIfoStatsPoolLaneDrops,
       "sfpsATMPortsTable": sfpsATMPortsTable,
       "sfpsATMPortsTableEntry": sfpsATMPortsTableEntry,
       "sfpsATMPortsPhysIntf": sfpsATMPortsPhysIntf,
       "sfpsATMPortsTotalLECPorts": sfpsATMPortsTotalLECPorts,
       "sfpsATMPortsTotalPVCPorts": sfpsATMPortsTotalPVCPorts,
       "sfpsATMPortsTotalSVCPorts": sfpsATMPortsTotalSVCPorts,
       "sfpsATMPortsBaseIntfNum": sfpsATMPortsBaseIntfNum,
       "sfpsATMPortsInUse": sfpsATMPortsInUse,
       "sfpsATMPortsMgrVerb": sfpsATMPortsMgrVerb,
       "sfpsATMPortsMgrPhysIntf": sfpsATMPortsMgrPhysIntf,
       "sfpsATMPortsMgrTotalLECPorts": sfpsATMPortsMgrTotalLECPorts,
       "sfpsATMPortsMgrTotalPVCPorts": sfpsATMPortsMgrTotalPVCPorts,
       "sfpsATMPortsMgrTotalSVCPorts": sfpsATMPortsMgrTotalSVCPorts,
       "sfpsATMPortsMgrVerbStatus": sfpsATMPortsMgrVerbStatus,
       "sfpsATMSvcHistoryMgrVerb": sfpsATMSvcHistoryMgrVerb,
       "sfpsATMSvcHistoryMgrSvcHistoryWraps": sfpsATMSvcHistoryMgrSvcHistoryWraps,
       "sfpsATMSvcHistoryMgrLogState": sfpsATMSvcHistoryMgrLogState,
       "sfpsATMSvcHistoryMgrEntriesCount": sfpsATMSvcHistoryMgrEntriesCount,
       "sfpsATMSvcHistoryEventTable": sfpsATMSvcHistoryEventTable,
       "sfpsATMSvcHistoryEventTableEntry": sfpsATMSvcHistoryEventTableEntry,
       "sfpsATMSvcHistoryEventIndex": sfpsATMSvcHistoryEventIndex,
       "sfpsATMSvcHistoryEventATMAddr": sfpsATMSvcHistoryEventATMAddr,
       "sfpsATMSvcHistoryEventPortNumber": sfpsATMSvcHistoryEventPortNumber,
       "sfpsATMSvcHistoryEventEvent": sfpsATMSvcHistoryEventEvent,
       "sfpsATMSvcHistoryEventEventChange": sfpsATMSvcHistoryEventEventChange,
       "sfpsATMSvcHistoryEventVccHand": sfpsATMSvcHistoryEventVccHand,
       "sfpsATMSvcHistoryEventVpi": sfpsATMSvcHistoryEventVpi,
       "sfpsATMSvcHistoryEventVci": sfpsATMSvcHistoryEventVci,
       "sfpsATMSvcHistoryEventTime": sfpsATMSvcHistoryEventTime}
)
