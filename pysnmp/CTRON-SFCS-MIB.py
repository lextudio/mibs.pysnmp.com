# SNMP MIB module (CTRON-SFCS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFCS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:15 2024
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

(atmVcCrossConnectHighIfIndex,
 atmVcCrossConnectHighVci,
 atmVcCrossConnectHighVpi,
 atmVcCrossConnectIndex,
 atmVcCrossConnectLowIfIndex,
 atmVcCrossConnectLowVci,
 atmVcCrossConnectLowVpi) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmVcCrossConnectHighIfIndex",
    "atmVcCrossConnectHighVci",
    "atmVcCrossConnectHighVpi",
    "atmVcCrossConnectIndex",
    "atmVcCrossConnectLowIfIndex",
    "atmVcCrossConnectLowVci",
    "atmVcCrossConnectLowVpi")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cabletron_ObjectIdentity = ObjectIdentity
cabletron = _Cabletron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4)
)
_Ctron_ObjectIdentity = ObjectIdentity
ctron = _Ctron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1)
)
_CtDataLink_ObjectIdentity = ObjectIdentity
ctDataLink = _CtDataLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2)
)
_CtSwitch_ObjectIdentity = ObjectIdentity
ctSwitch = _CtSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11)
)
_CtsfSwitch_ObjectIdentity = ObjectIdentity
ctsfSwitch = _CtsfSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1)
)
_CtSFCS_ObjectIdentity = ObjectIdentity
ctSFCS = _CtSFCS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1)
)
_SfcsSystem_ObjectIdentity = ObjectIdentity
sfcsSystem = _SfcsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1)
)
_SfcsSysConfig_ObjectIdentity = ObjectIdentity
sfcsSysConfig = _SfcsSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1)
)
_SfcsSysConfigTable_ObjectIdentity = ObjectIdentity
sfcsSysConfigTable = _SfcsSysConfigTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1)
)
_SfcsSysConfigEnt_ObjectIdentity = ObjectIdentity
sfcsSysConfigEnt = _SfcsSysConfigEnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1)
)


class _SfcsSysConfigAdminStatus_Type(Integer32):
    """Custom type sfcsSysConfigAdminStatus based on Integer32"""
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
          ("enabled", 1),
          ("other", 3))
    )


_SfcsSysConfigAdminStatus_Type.__name__ = "Integer32"
_SfcsSysConfigAdminStatus_Object = MibScalar
sfcsSysConfigAdminStatus = _SfcsSysConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 1),
    _SfcsSysConfigAdminStatus_Type()
)
sfcsSysConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysConfigAdminStatus.setStatus("mandatory")


class _SfcsSysConfigOperStatus_Type(Integer32):
    """Custom type sfcsSysConfigOperStatus based on Integer32"""
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
          ("enabled", 1),
          ("invalid-config", 6),
          ("other", 3),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_SfcsSysConfigOperStatus_Type.__name__ = "Integer32"
_SfcsSysConfigOperStatus_Object = MibScalar
sfcsSysConfigOperStatus = _SfcsSysConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 2),
    _SfcsSysConfigOperStatus_Type()
)
sfcsSysConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigOperStatus.setStatus("mandatory")
_SfcsSysConfigOperTime_Type = TimeTicks
_SfcsSysConfigOperTime_Object = MibScalar
sfcsSysConfigOperTime = _SfcsSysConfigOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 3),
    _SfcsSysConfigOperTime_Type()
)
sfcsSysConfigOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigOperTime.setStatus("mandatory")
_SfcsSysConfigLastChange_Type = TimeTicks
_SfcsSysConfigLastChange_Object = MibScalar
sfcsSysConfigLastChange = _SfcsSysConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 4),
    _SfcsSysConfigLastChange_Type()
)
sfcsSysConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigLastChange.setStatus("mandatory")
_SfcsSysConfigSwitchCapacity_Type = Integer32
_SfcsSysConfigSwitchCapacity_Object = MibScalar
sfcsSysConfigSwitchCapacity = _SfcsSysConfigSwitchCapacity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 5),
    _SfcsSysConfigSwitchCapacity_Type()
)
sfcsSysConfigSwitchCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigSwitchCapacity.setStatus("mandatory")
_SfcsSysConfigMaxCnxEntries_Type = Integer32
_SfcsSysConfigMaxCnxEntries_Object = MibScalar
sfcsSysConfigMaxCnxEntries = _SfcsSysConfigMaxCnxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 6),
    _SfcsSysConfigMaxCnxEntries_Type()
)
sfcsSysConfigMaxCnxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigMaxCnxEntries.setStatus("mandatory")
_SfcsSysConfigMaxStatEntries_Type = Integer32
_SfcsSysConfigMaxStatEntries_Object = MibScalar
sfcsSysConfigMaxStatEntries = _SfcsSysConfigMaxStatEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 7),
    _SfcsSysConfigMaxStatEntries_Type()
)
sfcsSysConfigMaxStatEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigMaxStatEntries.setStatus("mandatory")
_SfcsSysConfigMaxUpcEntries_Type = Integer32
_SfcsSysConfigMaxUpcEntries_Object = MibScalar
sfcsSysConfigMaxUpcEntries = _SfcsSysConfigMaxUpcEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 8),
    _SfcsSysConfigMaxUpcEntries_Type()
)
sfcsSysConfigMaxUpcEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigMaxUpcEntries.setStatus("mandatory")
_SfcsSysConfigNumberANIMS_Type = Integer32
_SfcsSysConfigNumberANIMS_Object = MibScalar
sfcsSysConfigNumberANIMS = _SfcsSysConfigNumberANIMS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 9),
    _SfcsSysConfigNumberANIMS_Type()
)
sfcsSysConfigNumberANIMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigNumberANIMS.setStatus("mandatory")
_SfcsSysConfigInterfaceCapability_Type = Integer32
_SfcsSysConfigInterfaceCapability_Object = MibScalar
sfcsSysConfigInterfaceCapability = _SfcsSysConfigInterfaceCapability_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 10),
    _SfcsSysConfigInterfaceCapability_Type()
)
sfcsSysConfigInterfaceCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigInterfaceCapability.setStatus("mandatory")


class _SfcsSysConfigTypeofSwitch_Type(Integer32):
    """Custom type sfcsSysConfigTypeofSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("sfcellswitch", 2),
          ("sfpacketswitch", 3))
    )


_SfcsSysConfigTypeofSwitch_Type.__name__ = "Integer32"
_SfcsSysConfigTypeofSwitch_Object = MibScalar
sfcsSysConfigTypeofSwitch = _SfcsSysConfigTypeofSwitch_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 11),
    _SfcsSysConfigTypeofSwitch_Type()
)
sfcsSysConfigTypeofSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigTypeofSwitch.setStatus("mandatory")
_SfcsSysConfigPolicingSupport_Type = TruthValue
_SfcsSysConfigPolicingSupport_Object = MibScalar
sfcsSysConfigPolicingSupport = _SfcsSysConfigPolicingSupport_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 12),
    _SfcsSysConfigPolicingSupport_Type()
)
sfcsSysConfigPolicingSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigPolicingSupport.setStatus("mandatory")


class _SfcsSysConfigPnniNsapPrefix_Type(OctetString):
    """Custom type sfcsSysConfigPnniNsapPrefix based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 13),
    )


_SfcsSysConfigPnniNsapPrefix_Type.__name__ = "OctetString"
_SfcsSysConfigPnniNsapPrefix_Object = MibScalar
sfcsSysConfigPnniNsapPrefix = _SfcsSysConfigPnniNsapPrefix_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 13),
    _SfcsSysConfigPnniNsapPrefix_Type()
)
sfcsSysConfigPnniNsapPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysConfigPnniNsapPrefix.setStatus("mandatory")
_SfcsSysConfigPnniNodeLevel_Type = Integer32
_SfcsSysConfigPnniNodeLevel_Object = MibScalar
sfcsSysConfigPnniNodeLevel = _SfcsSysConfigPnniNodeLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 14),
    _SfcsSysConfigPnniNodeLevel_Type()
)
sfcsSysConfigPnniNodeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysConfigPnniNodeLevel.setStatus("mandatory")
_SfcsSysConfigPnniAddessingMode_Type = Integer32
_SfcsSysConfigPnniAddessingMode_Object = MibScalar
sfcsSysConfigPnniAddessingMode = _SfcsSysConfigPnniAddessingMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 15),
    _SfcsSysConfigPnniAddessingMode_Type()
)
sfcsSysConfigPnniAddessingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysConfigPnniAddessingMode.setStatus("mandatory")
_SfcsSysConfigPnniAddessingAdmnStatus_Type = Integer32
_SfcsSysConfigPnniAddessingAdmnStatus_Object = MibScalar
sfcsSysConfigPnniAddessingAdmnStatus = _SfcsSysConfigPnniAddessingAdmnStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 16),
    _SfcsSysConfigPnniAddessingAdmnStatus_Type()
)
sfcsSysConfigPnniAddessingAdmnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysConfigPnniAddessingAdmnStatus.setStatus("mandatory")


class _SfcsSysConfigFMVer_Type(OctetString):
    """Custom type sfcsSysConfigFMVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SfcsSysConfigFMVer_Type.__name__ = "OctetString"
_SfcsSysConfigFMVer_Object = MibScalar
sfcsSysConfigFMVer = _SfcsSysConfigFMVer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 17),
    _SfcsSysConfigFMVer_Type()
)
sfcsSysConfigFMVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigFMVer.setStatus("mandatory")
_SfcsSysConfigCTMSlotMask_Type = Integer32
_SfcsSysConfigCTMSlotMask_Object = MibScalar
sfcsSysConfigCTMSlotMask = _SfcsSysConfigCTMSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 18),
    _SfcsSysConfigCTMSlotMask_Type()
)
sfcsSysConfigCTMSlotMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysConfigCTMSlotMask.setStatus("mandatory")
_SfcsSysConfigMaxfreecva_Type = Integer32
_SfcsSysConfigMaxfreecva_Object = MibScalar
sfcsSysConfigMaxfreecva = _SfcsSysConfigMaxfreecva_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 19),
    _SfcsSysConfigMaxfreecva_Type()
)
sfcsSysConfigMaxfreecva.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysConfigMaxfreecva.setStatus("mandatory")
_SfcsSysConfigUBR_Type = Integer32
_SfcsSysConfigUBR_Object = MibScalar
sfcsSysConfigUBR = _SfcsSysConfigUBR_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 1, 1, 1, 20),
    _SfcsSysConfigUBR_Type()
)
sfcsSysConfigUBR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysConfigUBR.setStatus("mandatory")
_SfcsSysStatus_ObjectIdentity = ObjectIdentity
sfcsSysStatus = _SfcsSysStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 2)
)
_SfcsSysStatusTable_ObjectIdentity = ObjectIdentity
sfcsSysStatusTable = _SfcsSysStatusTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 2, 1)
)
_SfcsSysStatusEnt_ObjectIdentity = ObjectIdentity
sfcsSysStatusEnt = _SfcsSysStatusEnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 2, 1, 1)
)
_SfcsSysStatusTdmCellCount_Type = OctetString
_SfcsSysStatusTdmCellCount_Object = MibScalar
sfcsSysStatusTdmCellCount = _SfcsSysStatusTdmCellCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 2, 1, 1, 1),
    _SfcsSysStatusTdmCellCount_Type()
)
sfcsSysStatusTdmCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysStatusTdmCellCount.setStatus("mandatory")


class _SfcsSysStatusTdmUtilization_Type(Integer32):
    """Custom type sfcsSysStatusTdmUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsSysStatusTdmUtilization_Type.__name__ = "Integer32"
_SfcsSysStatusTdmUtilization_Object = MibScalar
sfcsSysStatusTdmUtilization = _SfcsSysStatusTdmUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 2, 1, 1, 2),
    _SfcsSysStatusTdmUtilization_Type()
)
sfcsSysStatusTdmUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysStatusTdmUtilization.setStatus("mandatory")
_SfcsSysStatusCurrCnxEntries_Type = Integer32
_SfcsSysStatusCurrCnxEntries_Object = MibScalar
sfcsSysStatusCurrCnxEntries = _SfcsSysStatusCurrCnxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 2, 1, 1, 3),
    _SfcsSysStatusCurrCnxEntries_Type()
)
sfcsSysStatusCurrCnxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysStatusCurrCnxEntries.setStatus("mandatory")
_SfcsSysStatusCurrUPCEntries_Type = Integer32
_SfcsSysStatusCurrUPCEntries_Object = MibScalar
sfcsSysStatusCurrUPCEntries = _SfcsSysStatusCurrUPCEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 2, 1, 1, 4),
    _SfcsSysStatusCurrUPCEntries_Type()
)
sfcsSysStatusCurrUPCEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysStatusCurrUPCEntries.setStatus("mandatory")
_SfcsSysStatusCurrStatsEntries_Type = Integer32
_SfcsSysStatusCurrStatsEntries_Object = MibScalar
sfcsSysStatusCurrStatsEntries = _SfcsSysStatusCurrStatsEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 2, 1, 1, 5),
    _SfcsSysStatusCurrStatsEntries_Type()
)
sfcsSysStatusCurrStatsEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysStatusCurrStatsEntries.setStatus("mandatory")
_SfcsSysStatusAllocatedBw_Type = Integer32
_SfcsSysStatusAllocatedBw_Object = MibScalar
sfcsSysStatusAllocatedBw = _SfcsSysStatusAllocatedBw_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 2, 1, 1, 6),
    _SfcsSysStatusAllocatedBw_Type()
)
sfcsSysStatusAllocatedBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsSysStatusAllocatedBw.setStatus("mandatory")
_SfcsSysSystemCfg_ObjectIdentity = ObjectIdentity
sfcsSysSystemCfg = _SfcsSysSystemCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 3)
)
_SfcsSysSystemCfgTable_ObjectIdentity = ObjectIdentity
sfcsSysSystemCfgTable = _SfcsSysSystemCfgTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 3, 1)
)
_SfcsSysSystemCfgEnt_ObjectIdentity = ObjectIdentity
sfcsSysSystemCfgEnt = _SfcsSysSystemCfgEnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 3, 1, 1)
)


class _SfcsSysConfigAdminReset_Type(Integer32):
    """Custom type sfcsSysConfigAdminReset based on Integer32"""
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


_SfcsSysConfigAdminReset_Type.__name__ = "Integer32"
_SfcsSysConfigAdminReset_Object = MibScalar
sfcsSysConfigAdminReset = _SfcsSysConfigAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 3, 1, 1, 1),
    _SfcsSysConfigAdminReset_Type()
)
sfcsSysConfigAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysConfigAdminReset.setStatus("mandatory")


class _SfcsSysConfigATOMPersistance_Type(Integer32):
    """Custom type sfcsSysConfigATOMPersistance based on Integer32"""
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


_SfcsSysConfigATOMPersistance_Type.__name__ = "Integer32"
_SfcsSysConfigATOMPersistance_Object = MibScalar
sfcsSysConfigATOMPersistance = _SfcsSysConfigATOMPersistance_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 3, 1, 1, 2),
    _SfcsSysConfigATOMPersistance_Type()
)
sfcsSysConfigATOMPersistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysConfigATOMPersistance.setStatus("mandatory")
_SfcsSysConfigVcSize_Type = Integer32
_SfcsSysConfigVcSize_Object = MibScalar
sfcsSysConfigVcSize = _SfcsSysConfigVcSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 3, 1, 1, 3),
    _SfcsSysConfigVcSize_Type()
)
sfcsSysConfigVcSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysConfigVcSize.setStatus("mandatory")


class _SfcsSysConfigPowerUpDiags_Type(Integer32):
    """Custom type sfcsSysConfigPowerUpDiags based on Integer32"""
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


_SfcsSysConfigPowerUpDiags_Type.__name__ = "Integer32"
_SfcsSysConfigPowerUpDiags_Object = MibScalar
sfcsSysConfigPowerUpDiags = _SfcsSysConfigPowerUpDiags_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 3, 1, 1, 4),
    _SfcsSysConfigPowerUpDiags_Type()
)
sfcsSysConfigPowerUpDiags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysConfigPowerUpDiags.setStatus("mandatory")
_SfcsSysBPCfg_ObjectIdentity = ObjectIdentity
sfcsSysBPCfg = _SfcsSysBPCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 4)
)
_SfcsSysBPTable_ObjectIdentity = ObjectIdentity
sfcsSysBPTable = _SfcsSysBPTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 4, 1)
)
_SfcsSysBPEnt_ObjectIdentity = ObjectIdentity
sfcsSysBPEnt = _SfcsSysBPEnt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 4, 1, 1)
)
_SfcsSysBPClkSelect_Type = Integer32
_SfcsSysBPClkSelect_Object = MibScalar
sfcsSysBPClkSelect = _SfcsSysBPClkSelect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 1, 4, 1, 1, 1),
    _SfcsSysBPClkSelect_Type()
)
sfcsSysBPClkSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsSysBPClkSelect.setStatus("mandatory")
_SfcsEngine_ObjectIdentity = ObjectIdentity
sfcsEngine = _SfcsEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2)
)
_SfcsConfig_ObjectIdentity = ObjectIdentity
sfcsConfig = _SfcsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1)
)
_SfcsConfigTable_Object = MibTable
sfcsConfigTable = _SfcsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sfcsConfigTable.setStatus("mandatory")
_SfcsConfigEntry_Object = MibTableRow
sfcsConfigEntry = _SfcsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1)
)
sfcsConfigEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsConfigSlotIndex"),
)
if mibBuilder.loadTexts:
    sfcsConfigEntry.setStatus("mandatory")
_SfcsConfigSlotIndex_Type = Integer32
_SfcsConfigSlotIndex_Object = MibTableColumn
sfcsConfigSlotIndex = _SfcsConfigSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 1),
    _SfcsConfigSlotIndex_Type()
)
sfcsConfigSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigSlotIndex.setStatus("mandatory")


class _SfcsConfigAdminStatus_Type(Integer32):
    """Custom type sfcsConfigAdminStatus based on Integer32"""
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
          ("enabled", 1),
          ("other", 3))
    )


_SfcsConfigAdminStatus_Type.__name__ = "Integer32"
_SfcsConfigAdminStatus_Object = MibTableColumn
sfcsConfigAdminStatus = _SfcsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 2),
    _SfcsConfigAdminStatus_Type()
)
sfcsConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsConfigAdminStatus.setStatus("mandatory")


class _SfcsConfigAdminReset_Type(Integer32):
    """Custom type sfcsConfigAdminReset based on Integer32"""
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


_SfcsConfigAdminReset_Type.__name__ = "Integer32"
_SfcsConfigAdminReset_Object = MibTableColumn
sfcsConfigAdminReset = _SfcsConfigAdminReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 3),
    _SfcsConfigAdminReset_Type()
)
sfcsConfigAdminReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsConfigAdminReset.setStatus("mandatory")


class _SfcsConfigOperStatus_Type(Integer32):
    """Custom type sfcsConfigOperStatus based on Integer32"""
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
          ("enabled", 1),
          ("invalid-config", 6),
          ("other", 3),
          ("pending-disable", 4),
          ("pending-enable", 5))
    )


_SfcsConfigOperStatus_Type.__name__ = "Integer32"
_SfcsConfigOperStatus_Object = MibTableColumn
sfcsConfigOperStatus = _SfcsConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 4),
    _SfcsConfigOperStatus_Type()
)
sfcsConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigOperStatus.setStatus("mandatory")
_SfcsConfigOperTime_Type = TimeTicks
_SfcsConfigOperTime_Object = MibTableColumn
sfcsConfigOperTime = _SfcsConfigOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 5),
    _SfcsConfigOperTime_Type()
)
sfcsConfigOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigOperTime.setStatus("mandatory")
_SfcsConfigLastChange_Type = TimeTicks
_SfcsConfigLastChange_Object = MibTableColumn
sfcsConfigLastChange = _SfcsConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 6),
    _SfcsConfigLastChange_Type()
)
sfcsConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigLastChange.setStatus("mandatory")
_SfcsConfigVersion_Type = Integer32
_SfcsConfigVersion_Object = MibTableColumn
sfcsConfigVersion = _SfcsConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 7),
    _SfcsConfigVersion_Type()
)
sfcsConfigVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigVersion.setStatus("mandatory")
_SfcsConfigMibRev_Type = DisplayString
_SfcsConfigMibRev_Object = MibTableColumn
sfcsConfigMibRev = _SfcsConfigMibRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 8),
    _SfcsConfigMibRev_Type()
)
sfcsConfigMibRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigMibRev.setStatus("mandatory")
_SfcsConfigSwitchHostPort_Type = Integer32
_SfcsConfigSwitchHostPort_Object = MibTableColumn
sfcsConfigSwitchHostPort = _SfcsConfigSwitchHostPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 9),
    _SfcsConfigSwitchHostPort_Type()
)
sfcsConfigSwitchHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigSwitchHostPort.setStatus("mandatory")
_SfcsConfigHostCtrlATMAddr_Type = OctetString
_SfcsConfigHostCtrlATMAddr_Object = MibTableColumn
sfcsConfigHostCtrlATMAddr = _SfcsConfigHostCtrlATMAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 10),
    _SfcsConfigHostCtrlATMAddr_Type()
)
sfcsConfigHostCtrlATMAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigHostCtrlATMAddr.setStatus("mandatory")
_SfcsConfigSwitchCapacity_Type = Integer32
_SfcsConfigSwitchCapacity_Object = MibTableColumn
sfcsConfigSwitchCapacity = _SfcsConfigSwitchCapacity_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 11),
    _SfcsConfigSwitchCapacity_Type()
)
sfcsConfigSwitchCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigSwitchCapacity.setStatus("mandatory")
_SfcsConfigMaxCnxEntries_Type = Integer32
_SfcsConfigMaxCnxEntries_Object = MibTableColumn
sfcsConfigMaxCnxEntries = _SfcsConfigMaxCnxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 12),
    _SfcsConfigMaxCnxEntries_Type()
)
sfcsConfigMaxCnxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigMaxCnxEntries.setStatus("mandatory")
_SfcsConfigMaxStatEntries_Type = Integer32
_SfcsConfigMaxStatEntries_Object = MibTableColumn
sfcsConfigMaxStatEntries = _SfcsConfigMaxStatEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 13),
    _SfcsConfigMaxStatEntries_Type()
)
sfcsConfigMaxStatEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigMaxStatEntries.setStatus("mandatory")
_SfcsConfigMaxUpcEntries_Type = Integer32
_SfcsConfigMaxUpcEntries_Object = MibTableColumn
sfcsConfigMaxUpcEntries = _SfcsConfigMaxUpcEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 14),
    _SfcsConfigMaxUpcEntries_Type()
)
sfcsConfigMaxUpcEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigMaxUpcEntries.setStatus("mandatory")
_SfcsConfigNumberANIMS_Type = Integer32
_SfcsConfigNumberANIMS_Object = MibTableColumn
sfcsConfigNumberANIMS = _SfcsConfigNumberANIMS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 15),
    _SfcsConfigNumberANIMS_Type()
)
sfcsConfigNumberANIMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigNumberANIMS.setStatus("mandatory")
_SfcsConfigBwCapability_Type = Integer32
_SfcsConfigBwCapability_Object = MibTableColumn
sfcsConfigBwCapability = _SfcsConfigBwCapability_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 16),
    _SfcsConfigBwCapability_Type()
)
sfcsConfigBwCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsConfigBwCapability.setStatus("mandatory")


class _SfcsConfigMasterClock1Source_Type(Integer32):
    """Custom type sfcsConfigMasterClock1Source based on Integer32"""
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
        *(("anim-four-clk", 4),
          ("anim-one-clk", 1),
          ("anim-three-clk", 3),
          ("anim-two-clk", 2),
          ("backplane-one", 5),
          ("backplane-two", 6))
    )


_SfcsConfigMasterClock1Source_Type.__name__ = "Integer32"
_SfcsConfigMasterClock1Source_Object = MibTableColumn
sfcsConfigMasterClock1Source = _SfcsConfigMasterClock1Source_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 17),
    _SfcsConfigMasterClock1Source_Type()
)
sfcsConfigMasterClock1Source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsConfigMasterClock1Source.setStatus("mandatory")


class _SfcsConfigMasterClock2Source_Type(Integer32):
    """Custom type sfcsConfigMasterClock2Source based on Integer32"""
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
        *(("anim-four-clk", 4),
          ("anim-one-clk", 1),
          ("anim-three-clk", 3),
          ("anim-two-clk", 2),
          ("backplane-one", 5),
          ("backplane-two", 6))
    )


_SfcsConfigMasterClock2Source_Type.__name__ = "Integer32"
_SfcsConfigMasterClock2Source_Object = MibTableColumn
sfcsConfigMasterClock2Source = _SfcsConfigMasterClock2Source_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 18),
    _SfcsConfigMasterClock2Source_Type()
)
sfcsConfigMasterClock2Source.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsConfigMasterClock2Source.setStatus("mandatory")


class _SfcsConfigMasterClock1Standby_Type(Integer32):
    """Custom type sfcsConfigMasterClock1Standby based on Integer32"""
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
        *(("anim-four-clk", 4),
          ("anim-one-clk", 1),
          ("anim-three-clk", 3),
          ("anim-two-clk", 2),
          ("backplane-one", 5),
          ("backplane-two", 6),
          ("none", 7))
    )


_SfcsConfigMasterClock1Standby_Type.__name__ = "Integer32"
_SfcsConfigMasterClock1Standby_Object = MibTableColumn
sfcsConfigMasterClock1Standby = _SfcsConfigMasterClock1Standby_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 19),
    _SfcsConfigMasterClock1Standby_Type()
)
sfcsConfigMasterClock1Standby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsConfigMasterClock1Standby.setStatus("mandatory")


class _SfcsConfigMasterClock2Standby_Type(Integer32):
    """Custom type sfcsConfigMasterClock2Standby based on Integer32"""
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
        *(("anim-four-clk", 4),
          ("anim-one-clk", 1),
          ("anim-three-clk", 3),
          ("anim-two-clk", 2),
          ("backplane-one", 5),
          ("backplane-two", 6),
          ("none", 7))
    )


_SfcsConfigMasterClock2Standby_Type.__name__ = "Integer32"
_SfcsConfigMasterClock2Standby_Object = MibTableColumn
sfcsConfigMasterClock2Standby = _SfcsConfigMasterClock2Standby_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 1, 1, 1, 20),
    _SfcsConfigMasterClock2Standby_Type()
)
sfcsConfigMasterClock2Standby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsConfigMasterClock2Standby.setStatus("mandatory")
_SfcsStatus_ObjectIdentity = ObjectIdentity
sfcsStatus = _SfcsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 2)
)
_SfcsStatusTable_Object = MibTable
sfcsStatusTable = _SfcsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sfcsStatusTable.setStatus("mandatory")
_SfcsStatusEntry_Object = MibTableRow
sfcsStatusEntry = _SfcsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 2, 1, 1)
)
sfcsStatusEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsStatusSlotIndex"),
)
if mibBuilder.loadTexts:
    sfcsStatusEntry.setStatus("mandatory")
_SfcsStatusSlotIndex_Type = Integer32
_SfcsStatusSlotIndex_Object = MibTableColumn
sfcsStatusSlotIndex = _SfcsStatusSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 2, 1, 1, 1),
    _SfcsStatusSlotIndex_Type()
)
sfcsStatusSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsStatusSlotIndex.setStatus("mandatory")
_SfcsStatusTdmCellCount_Type = OctetString
_SfcsStatusTdmCellCount_Object = MibTableColumn
sfcsStatusTdmCellCount = _SfcsStatusTdmCellCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 2, 1, 1, 2),
    _SfcsStatusTdmCellCount_Type()
)
sfcsStatusTdmCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsStatusTdmCellCount.setStatus("mandatory")


class _SfcsStatusTdmUtilization_Type(Integer32):
    """Custom type sfcsStatusTdmUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsStatusTdmUtilization_Type.__name__ = "Integer32"
_SfcsStatusTdmUtilization_Object = MibTableColumn
sfcsStatusTdmUtilization = _SfcsStatusTdmUtilization_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 2, 1, 1, 3),
    _SfcsStatusTdmUtilization_Type()
)
sfcsStatusTdmUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsStatusTdmUtilization.setStatus("mandatory")
_SfcsStatusCurrCnxEntries_Type = Integer32
_SfcsStatusCurrCnxEntries_Object = MibTableColumn
sfcsStatusCurrCnxEntries = _SfcsStatusCurrCnxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 2, 1, 1, 4),
    _SfcsStatusCurrCnxEntries_Type()
)
sfcsStatusCurrCnxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsStatusCurrCnxEntries.setStatus("mandatory")
_SfcsStatusCurrUPCEntries_Type = Integer32
_SfcsStatusCurrUPCEntries_Object = MibTableColumn
sfcsStatusCurrUPCEntries = _SfcsStatusCurrUPCEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 2, 1, 1, 5),
    _SfcsStatusCurrUPCEntries_Type()
)
sfcsStatusCurrUPCEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsStatusCurrUPCEntries.setStatus("mandatory")
_SfcsStatusCurrStatsEntries_Type = Integer32
_SfcsStatusCurrStatsEntries_Object = MibTableColumn
sfcsStatusCurrStatsEntries = _SfcsStatusCurrStatsEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 2, 1, 1, 6),
    _SfcsStatusCurrStatsEntries_Type()
)
sfcsStatusCurrStatsEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsStatusCurrStatsEntries.setStatus("mandatory")
_SfcsStatusCurrCtmAgent_Type = Integer32
_SfcsStatusCurrCtmAgent_Object = MibTableColumn
sfcsStatusCurrCtmAgent = _SfcsStatusCurrCtmAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 2, 1, 1, 7),
    _SfcsStatusCurrCtmAgent_Type()
)
sfcsStatusCurrCtmAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsStatusCurrCtmAgent.setStatus("mandatory")
_SfcsUPCEngine_ObjectIdentity = ObjectIdentity
sfcsUPCEngine = _SfcsUPCEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 3)
)
_SfcsUPCTable_Object = MibTable
sfcsUPCTable = _SfcsUPCTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sfcsUPCTable.setStatus("mandatory")
_SfcsUPCEntry_Object = MibTableRow
sfcsUPCEntry = _SfcsUPCEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 3, 1, 1)
)
sfcsUPCEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsUPCSlotIndex"),
)
if mibBuilder.loadTexts:
    sfcsUPCEntry.setStatus("mandatory")
_SfcsUPCSlotIndex_Type = Integer32
_SfcsUPCSlotIndex_Object = MibTableColumn
sfcsUPCSlotIndex = _SfcsUPCSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 3, 1, 1, 1),
    _SfcsUPCSlotIndex_Type()
)
sfcsUPCSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsUPCSlotIndex.setStatus("mandatory")


class _SfcsUPCAdminStatus_Type(Integer32):
    """Custom type sfcsUPCAdminStatus based on Integer32"""
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
          ("enabled", 1),
          ("other", 3))
    )


_SfcsUPCAdminStatus_Type.__name__ = "Integer32"
_SfcsUPCAdminStatus_Object = MibTableColumn
sfcsUPCAdminStatus = _SfcsUPCAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 3, 1, 1, 2),
    _SfcsUPCAdminStatus_Type()
)
sfcsUPCAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsUPCAdminStatus.setStatus("mandatory")


class _SfcsUPCOperStatus_Type(Integer32):
    """Custom type sfcsUPCOperStatus based on Integer32"""
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
          ("enabled", 1),
          ("other", 3))
    )


_SfcsUPCOperStatus_Type.__name__ = "Integer32"
_SfcsUPCOperStatus_Object = MibTableColumn
sfcsUPCOperStatus = _SfcsUPCOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 3, 1, 1, 3),
    _SfcsUPCOperStatus_Type()
)
sfcsUPCOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsUPCOperStatus.setStatus("mandatory")


class _SfcsUPCReset_Type(Integer32):
    """Custom type sfcsUPCReset based on Integer32"""
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


_SfcsUPCReset_Type.__name__ = "Integer32"
_SfcsUPCReset_Object = MibTableColumn
sfcsUPCReset = _SfcsUPCReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 3, 1, 1, 4),
    _SfcsUPCReset_Type()
)
sfcsUPCReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsUPCReset.setStatus("mandatory")
_SfcsUPCOperTime_Type = TimeTicks
_SfcsUPCOperTime_Object = MibTableColumn
sfcsUPCOperTime = _SfcsUPCOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 3, 1, 1, 5),
    _SfcsUPCOperTime_Type()
)
sfcsUPCOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsUPCOperTime.setStatus("mandatory")
_SfcsStatisticsEngine_ObjectIdentity = ObjectIdentity
sfcsStatisticsEngine = _SfcsStatisticsEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 4)
)
_SfcsStatsEngineTable_Object = MibTable
sfcsStatsEngineTable = _SfcsStatsEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sfcsStatsEngineTable.setStatus("mandatory")
_SfcsStatsEngineEntry_Object = MibTableRow
sfcsStatsEngineEntry = _SfcsStatsEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 4, 1, 1)
)
sfcsStatsEngineEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsStatsEngineSlotIndex"),
)
if mibBuilder.loadTexts:
    sfcsStatsEngineEntry.setStatus("mandatory")
_SfcsStatsEngineSlotIndex_Type = Integer32
_SfcsStatsEngineSlotIndex_Object = MibTableColumn
sfcsStatsEngineSlotIndex = _SfcsStatsEngineSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 4, 1, 1, 1),
    _SfcsStatsEngineSlotIndex_Type()
)
sfcsStatsEngineSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsStatsEngineSlotIndex.setStatus("mandatory")


class _SfcsStatsEngineAdminStatus_Type(Integer32):
    """Custom type sfcsStatsEngineAdminStatus based on Integer32"""
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
          ("enabled", 1),
          ("other", 3))
    )


_SfcsStatsEngineAdminStatus_Type.__name__ = "Integer32"
_SfcsStatsEngineAdminStatus_Object = MibTableColumn
sfcsStatsEngineAdminStatus = _SfcsStatsEngineAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 4, 1, 1, 2),
    _SfcsStatsEngineAdminStatus_Type()
)
sfcsStatsEngineAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsStatsEngineAdminStatus.setStatus("mandatory")


class _SfcsStatsEngineOperStatus_Type(Integer32):
    """Custom type sfcsStatsEngineOperStatus based on Integer32"""
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
          ("enabled", 1),
          ("other", 3))
    )


_SfcsStatsEngineOperStatus_Type.__name__ = "Integer32"
_SfcsStatsEngineOperStatus_Object = MibTableColumn
sfcsStatsEngineOperStatus = _SfcsStatsEngineOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 4, 1, 1, 3),
    _SfcsStatsEngineOperStatus_Type()
)
sfcsStatsEngineOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsStatsEngineOperStatus.setStatus("mandatory")


class _SfcsStatsEngineReset_Type(Integer32):
    """Custom type sfcsStatsEngineReset based on Integer32"""
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


_SfcsStatsEngineReset_Type.__name__ = "Integer32"
_SfcsStatsEngineReset_Object = MibTableColumn
sfcsStatsEngineReset = _SfcsStatsEngineReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 4, 1, 1, 4),
    _SfcsStatsEngineReset_Type()
)
sfcsStatsEngineReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsStatsEngineReset.setStatus("mandatory")
_SfcsStatsEngineOperTime_Type = TimeTicks
_SfcsStatsEngineOperTime_Object = MibTableColumn
sfcsStatsEngineOperTime = _SfcsStatsEngineOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 4, 1, 1, 5),
    _SfcsStatsEngineOperTime_Type()
)
sfcsStatsEngineOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsStatsEngineOperTime.setStatus("mandatory")
_SfcsPacketDiscardEngine_ObjectIdentity = ObjectIdentity
sfcsPacketDiscardEngine = _SfcsPacketDiscardEngine_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 5)
)
_SfcsPacketDiscardEngineTable_Object = MibTable
sfcsPacketDiscardEngineTable = _SfcsPacketDiscardEngineTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sfcsPacketDiscardEngineTable.setStatus("mandatory")
_SfcsPacketDiscardEngineEntry_Object = MibTableRow
sfcsPacketDiscardEngineEntry = _SfcsPacketDiscardEngineEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 5, 1, 1)
)
sfcsPacketDiscardEngineEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsPacketDiscardEngineSlotIndex"),
)
if mibBuilder.loadTexts:
    sfcsPacketDiscardEngineEntry.setStatus("mandatory")
_SfcsPacketDiscardEngineSlotIndex_Type = Integer32
_SfcsPacketDiscardEngineSlotIndex_Object = MibTableColumn
sfcsPacketDiscardEngineSlotIndex = _SfcsPacketDiscardEngineSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 5, 1, 1, 1),
    _SfcsPacketDiscardEngineSlotIndex_Type()
)
sfcsPacketDiscardEngineSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsPacketDiscardEngineSlotIndex.setStatus("mandatory")


class _SfcsPacketDiscardEngineAdminStatus_Type(Integer32):
    """Custom type sfcsPacketDiscardEngineAdminStatus based on Integer32"""
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
          ("enabled", 1),
          ("other", 3))
    )


_SfcsPacketDiscardEngineAdminStatus_Type.__name__ = "Integer32"
_SfcsPacketDiscardEngineAdminStatus_Object = MibTableColumn
sfcsPacketDiscardEngineAdminStatus = _SfcsPacketDiscardEngineAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 5, 1, 1, 2),
    _SfcsPacketDiscardEngineAdminStatus_Type()
)
sfcsPacketDiscardEngineAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsPacketDiscardEngineAdminStatus.setStatus("mandatory")


class _SfcsPacketDiscardEngineOperStatus_Type(Integer32):
    """Custom type sfcsPacketDiscardEngineOperStatus based on Integer32"""
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
          ("enabled", 1),
          ("other", 3))
    )


_SfcsPacketDiscardEngineOperStatus_Type.__name__ = "Integer32"
_SfcsPacketDiscardEngineOperStatus_Object = MibTableColumn
sfcsPacketDiscardEngineOperStatus = _SfcsPacketDiscardEngineOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 5, 1, 1, 3),
    _SfcsPacketDiscardEngineOperStatus_Type()
)
sfcsPacketDiscardEngineOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsPacketDiscardEngineOperStatus.setStatus("mandatory")


class _SfcsPacketDiscardEngineReset_Type(Integer32):
    """Custom type sfcsPacketDiscardEngineReset based on Integer32"""
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


_SfcsPacketDiscardEngineReset_Type.__name__ = "Integer32"
_SfcsPacketDiscardEngineReset_Object = MibTableColumn
sfcsPacketDiscardEngineReset = _SfcsPacketDiscardEngineReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 5, 1, 1, 4),
    _SfcsPacketDiscardEngineReset_Type()
)
sfcsPacketDiscardEngineReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsPacketDiscardEngineReset.setStatus("mandatory")


class _SfcsPacketDiscardEngineEPDPercentage_Type(Integer32):
    """Custom type sfcsPacketDiscardEngineEPDPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsPacketDiscardEngineEPDPercentage_Type.__name__ = "Integer32"
_SfcsPacketDiscardEngineEPDPercentage_Object = MibTableColumn
sfcsPacketDiscardEngineEPDPercentage = _SfcsPacketDiscardEngineEPDPercentage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 5, 1, 1, 5),
    _SfcsPacketDiscardEngineEPDPercentage_Type()
)
sfcsPacketDiscardEngineEPDPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsPacketDiscardEngineEPDPercentage.setStatus("mandatory")
_SfcsPacketDiscardEngineOperTime_Type = TimeTicks
_SfcsPacketDiscardEngineOperTime_Object = MibTableColumn
sfcsPacketDiscardEngineOperTime = _SfcsPacketDiscardEngineOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 2, 5, 1, 1, 6),
    _SfcsPacketDiscardEngineOperTime_Type()
)
sfcsPacketDiscardEngineOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsPacketDiscardEngineOperTime.setStatus("mandatory")
_SfcsANIM_ObjectIdentity = ObjectIdentity
sfcsANIM = _SfcsANIM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3)
)
_SfcsANIMConfig_ObjectIdentity = ObjectIdentity
sfcsANIMConfig = _SfcsANIMConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 1)
)
_SfcsANIMConfigTable_Object = MibTable
sfcsANIMConfigTable = _SfcsANIMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    sfcsANIMConfigTable.setStatus("mandatory")
_SfcsANIMConfigEntry_Object = MibTableRow
sfcsANIMConfigEntry = _SfcsANIMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 1, 1, 1)
)
sfcsANIMConfigEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsANIMConfigANIMIndex"),
)
if mibBuilder.loadTexts:
    sfcsANIMConfigEntry.setStatus("mandatory")
_SfcsANIMConfigANIMIndex_Type = Integer32
_SfcsANIMConfigANIMIndex_Object = MibTableColumn
sfcsANIMConfigANIMIndex = _SfcsANIMConfigANIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 1, 1, 1, 1),
    _SfcsANIMConfigANIMIndex_Type()
)
sfcsANIMConfigANIMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMConfigANIMIndex.setStatus("mandatory")


class _SfcsANIMConfigAdminStatus_Type(Integer32):
    """Custom type sfcsANIMConfigAdminStatus based on Integer32"""
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
          ("enabled", 1),
          ("other", 3))
    )


_SfcsANIMConfigAdminStatus_Type.__name__ = "Integer32"
_SfcsANIMConfigAdminStatus_Object = MibTableColumn
sfcsANIMConfigAdminStatus = _SfcsANIMConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 1, 1, 1, 2),
    _SfcsANIMConfigAdminStatus_Type()
)
sfcsANIMConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsANIMConfigAdminStatus.setStatus("mandatory")


class _SfcsANIMConfigOperStatus_Type(Integer32):
    """Custom type sfcsANIMConfigOperStatus based on Integer32"""
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
          ("enabled", 1),
          ("other", 3))
    )


_SfcsANIMConfigOperStatus_Type.__name__ = "Integer32"
_SfcsANIMConfigOperStatus_Object = MibTableColumn
sfcsANIMConfigOperStatus = _SfcsANIMConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 1, 1, 1, 3),
    _SfcsANIMConfigOperStatus_Type()
)
sfcsANIMConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMConfigOperStatus.setStatus("mandatory")
_SfcsANIMConfigANIMType_Type = ObjectIdentifier
_SfcsANIMConfigANIMType_Object = MibTableColumn
sfcsANIMConfigANIMType = _SfcsANIMConfigANIMType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 1, 1, 1, 4),
    _SfcsANIMConfigANIMType_Type()
)
sfcsANIMConfigANIMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMConfigANIMType.setStatus("mandatory")
_SfcsANIMConfigNumInterfaces_Type = Integer32
_SfcsANIMConfigNumInterfaces_Object = MibTableColumn
sfcsANIMConfigNumInterfaces = _SfcsANIMConfigNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 1, 1, 1, 5),
    _SfcsANIMConfigNumInterfaces_Type()
)
sfcsANIMConfigNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMConfigNumInterfaces.setStatus("mandatory")
_SfcsANIMConfigLineRate_Type = Integer32
_SfcsANIMConfigLineRate_Object = MibTableColumn
sfcsANIMConfigLineRate = _SfcsANIMConfigLineRate_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 1, 1, 1, 6),
    _SfcsANIMConfigLineRate_Type()
)
sfcsANIMConfigLineRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMConfigLineRate.setStatus("mandatory")


class _SfcsANIMConfigToMB_Type(Integer32):
    """Custom type sfcsANIMConfigToMB based on Integer32"""
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
        *(("local-anim-clock", 1),
          ("port-four-clock", 5),
          ("port-one-clock", 2),
          ("port-three-clock", 4),
          ("port-two-clock", 3))
    )


_SfcsANIMConfigToMB_Type.__name__ = "Integer32"
_SfcsANIMConfigToMB_Object = MibTableColumn
sfcsANIMConfigToMB = _SfcsANIMConfigToMB_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 1, 1, 1, 7),
    _SfcsANIMConfigToMB_Type()
)
sfcsANIMConfigToMB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsANIMConfigToMB.setStatus("mandatory")


class _SfcsANIMConfigMBClockSelect_Type(Integer32):
    """Custom type sfcsANIMConfigMBClockSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master-clk-one", 1),
          ("master-clk-two", 2))
    )


_SfcsANIMConfigMBClockSelect_Type.__name__ = "Integer32"
_SfcsANIMConfigMBClockSelect_Object = MibTableColumn
sfcsANIMConfigMBClockSelect = _SfcsANIMConfigMBClockSelect_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 1, 1, 1, 8),
    _SfcsANIMConfigMBClockSelect_Type()
)
sfcsANIMConfigMBClockSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsANIMConfigMBClockSelect.setStatus("mandatory")
_SfcsANIMStatistics_ObjectIdentity = ObjectIdentity
sfcsANIMStatistics = _SfcsANIMStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 2)
)
_SfcsANIMStatsTable_Object = MibTable
sfcsANIMStatsTable = _SfcsANIMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    sfcsANIMStatsTable.setStatus("mandatory")
_SfcsANIMStatsEntry_Object = MibTableRow
sfcsANIMStatsEntry = _SfcsANIMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 2, 1, 1)
)
sfcsANIMStatsEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsANIMStatsANIMIndex"),
)
if mibBuilder.loadTexts:
    sfcsANIMStatsEntry.setStatus("mandatory")
_SfcsANIMStatsANIMIndex_Type = Integer32
_SfcsANIMStatsANIMIndex_Object = MibTableColumn
sfcsANIMStatsANIMIndex = _SfcsANIMStatsANIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 2, 1, 1, 1),
    _SfcsANIMStatsANIMIndex_Type()
)
sfcsANIMStatsANIMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMStatsANIMIndex.setStatus("mandatory")
_SfcsANIMStatsRxCells_Type = OctetString
_SfcsANIMStatsRxCells_Object = MibTableColumn
sfcsANIMStatsRxCells = _SfcsANIMStatsRxCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 2, 1, 1, 2),
    _SfcsANIMStatsRxCells_Type()
)
sfcsANIMStatsRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMStatsRxCells.setStatus("mandatory")
_SfcsANIMStatsTxCells_Type = OctetString
_SfcsANIMStatsTxCells_Object = MibTableColumn
sfcsANIMStatsTxCells = _SfcsANIMStatsTxCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 2, 1, 1, 3),
    _SfcsANIMStatsTxCells_Type()
)
sfcsANIMStatsTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMStatsTxCells.setStatus("mandatory")
_SfcsANIMPic_ObjectIdentity = ObjectIdentity
sfcsANIMPic = _SfcsANIMPic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3)
)
_SfcsANIMPicTable_Object = MibTable
sfcsANIMPicTable = _SfcsANIMPicTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sfcsANIMPicTable.setStatus("mandatory")
_SfcsANIMPicEntry_Object = MibTableRow
sfcsANIMPicEntry = _SfcsANIMPicEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1)
)
sfcsANIMPicEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsANIMPicIndex"),
)
if mibBuilder.loadTexts:
    sfcsANIMPicEntry.setStatus("mandatory")
_SfcsANIMPicSlot_Type = Integer32
_SfcsANIMPicSlot_Object = MibTableColumn
sfcsANIMPicSlot = _SfcsANIMPicSlot_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 1),
    _SfcsANIMPicSlot_Type()
)
sfcsANIMPicSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicSlot.setStatus("mandatory")
_SfcsANIMPicIndex_Type = Integer32
_SfcsANIMPicIndex_Object = MibTableColumn
sfcsANIMPicIndex = _SfcsANIMPicIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 2),
    _SfcsANIMPicIndex_Type()
)
sfcsANIMPicIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicIndex.setStatus("mandatory")
_SfcsANIMPicLocation_Type = ObjectIdentifier
_SfcsANIMPicLocation_Object = MibTableColumn
sfcsANIMPicLocation = _SfcsANIMPicLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 3),
    _SfcsANIMPicLocation_Type()
)
sfcsANIMPicLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicLocation.setStatus("mandatory")


class _SfcsANIMPicStatus_Type(Integer32):
    """Custom type sfcsANIMPicStatus based on Integer32"""
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
        *(("checkSum", 4),
          ("error", 5),
          ("limited", 6),
          ("notPresent", 3),
          ("other", 1),
          ("present", 2))
    )


_SfcsANIMPicStatus_Type.__name__ = "Integer32"
_SfcsANIMPicStatus_Object = MibTableColumn
sfcsANIMPicStatus = _SfcsANIMPicStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 4),
    _SfcsANIMPicStatus_Type()
)
sfcsANIMPicStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicStatus.setStatus("mandatory")


class _SfcsANIMPicVersion_Type(DisplayString):
    """Custom type sfcsANIMPicVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SfcsANIMPicVersion_Type.__name__ = "DisplayString"
_SfcsANIMPicVersion_Object = MibTableColumn
sfcsANIMPicVersion = _SfcsANIMPicVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 5),
    _SfcsANIMPicVersion_Type()
)
sfcsANIMPicVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicVersion.setStatus("mandatory")
_SfcsANIMPicModuleType_Type = ObjectIdentifier
_SfcsANIMPicModuleType_Object = MibTableColumn
sfcsANIMPicModuleType = _SfcsANIMPicModuleType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 6),
    _SfcsANIMPicModuleType_Type()
)
sfcsANIMPicModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicModuleType.setStatus("mandatory")


class _SfcsANIMPicMfgPN_Type(DisplayString):
    """Custom type sfcsANIMPicMfgPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_SfcsANIMPicMfgPN_Type.__name__ = "DisplayString"
_SfcsANIMPicMfgPN_Object = MibTableColumn
sfcsANIMPicMfgPN = _SfcsANIMPicMfgPN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 7),
    _SfcsANIMPicMfgPN_Type()
)
sfcsANIMPicMfgPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicMfgPN.setStatus("mandatory")


class _SfcsANIMPicMfgSN_Type(DisplayString):
    """Custom type sfcsANIMPicMfgSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_SfcsANIMPicMfgSN_Type.__name__ = "DisplayString"
_SfcsANIMPicMfgSN_Object = MibTableColumn
sfcsANIMPicMfgSN = _SfcsANIMPicMfgSN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 8),
    _SfcsANIMPicMfgSN_Type()
)
sfcsANIMPicMfgSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicMfgSN.setStatus("mandatory")


class _SfcsANIMPicMfgPartNumb_Type(DisplayString):
    """Custom type sfcsANIMPicMfgPartNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SfcsANIMPicMfgPartNumb_Type.__name__ = "DisplayString"
_SfcsANIMPicMfgPartNumb_Object = MibTableColumn
sfcsANIMPicMfgPartNumb = _SfcsANIMPicMfgPartNumb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 9),
    _SfcsANIMPicMfgPartNumb_Type()
)
sfcsANIMPicMfgPartNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicMfgPartNumb.setStatus("mandatory")


class _SfcsANIMPicMfgSerialNumb_Type(DisplayString):
    """Custom type sfcsANIMPicMfgSerialNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SfcsANIMPicMfgSerialNumb_Type.__name__ = "DisplayString"
_SfcsANIMPicMfgSerialNumb_Object = MibTableColumn
sfcsANIMPicMfgSerialNumb = _SfcsANIMPicMfgSerialNumb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 10),
    _SfcsANIMPicMfgSerialNumb_Type()
)
sfcsANIMPicMfgSerialNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicMfgSerialNumb.setStatus("mandatory")


class _SfcsANIMPicMfgReworkLocation_Type(DisplayString):
    """Custom type sfcsANIMPicMfgReworkLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SfcsANIMPicMfgReworkLocation_Type.__name__ = "DisplayString"
_SfcsANIMPicMfgReworkLocation_Object = MibTableColumn
sfcsANIMPicMfgReworkLocation = _SfcsANIMPicMfgReworkLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 11),
    _SfcsANIMPicMfgReworkLocation_Type()
)
sfcsANIMPicMfgReworkLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicMfgReworkLocation.setStatus("mandatory")


class _SfcsANIMPicMfgMfgLocation_Type(DisplayString):
    """Custom type sfcsANIMPicMfgMfgLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SfcsANIMPicMfgMfgLocation_Type.__name__ = "DisplayString"
_SfcsANIMPicMfgMfgLocation_Object = MibTableColumn
sfcsANIMPicMfgMfgLocation = _SfcsANIMPicMfgMfgLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 12),
    _SfcsANIMPicMfgMfgLocation_Type()
)
sfcsANIMPicMfgMfgLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicMfgMfgLocation.setStatus("mandatory")


class _SfcsANIMPicMfgDateCode_Type(DisplayString):
    """Custom type sfcsANIMPicMfgDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SfcsANIMPicMfgDateCode_Type.__name__ = "DisplayString"
_SfcsANIMPicMfgDateCode_Object = MibTableColumn
sfcsANIMPicMfgDateCode = _SfcsANIMPicMfgDateCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 13),
    _SfcsANIMPicMfgDateCode_Type()
)
sfcsANIMPicMfgDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicMfgDateCode.setStatus("mandatory")


class _SfcsANIMPicMfgRevisionCode_Type(DisplayString):
    """Custom type sfcsANIMPicMfgRevisionCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SfcsANIMPicMfgRevisionCode_Type.__name__ = "DisplayString"
_SfcsANIMPicMfgRevisionCode_Object = MibTableColumn
sfcsANIMPicMfgRevisionCode = _SfcsANIMPicMfgRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 14),
    _SfcsANIMPicMfgRevisionCode_Type()
)
sfcsANIMPicMfgRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicMfgRevisionCode.setStatus("mandatory")


class _SfcsANIMPicTLPN_Type(DisplayString):
    """Custom type sfcsANIMPicTLPN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 9),
    )


_SfcsANIMPicTLPN_Type.__name__ = "DisplayString"
_SfcsANIMPicTLPN_Object = MibTableColumn
sfcsANIMPicTLPN = _SfcsANIMPicTLPN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 15),
    _SfcsANIMPicTLPN_Type()
)
sfcsANIMPicTLPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicTLPN.setStatus("mandatory")


class _SfcsANIMPicTLSN_Type(DisplayString):
    """Custom type sfcsANIMPicTLSN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_SfcsANIMPicTLSN_Type.__name__ = "DisplayString"
_SfcsANIMPicTLSN_Object = MibTableColumn
sfcsANIMPicTLSN = _SfcsANIMPicTLSN_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 16),
    _SfcsANIMPicTLSN_Type()
)
sfcsANIMPicTLSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicTLSN.setStatus("mandatory")


class _SfcsANIMPicTLPartNumb_Type(DisplayString):
    """Custom type sfcsANIMPicTLPartNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 7),
    )


_SfcsANIMPicTLPartNumb_Type.__name__ = "DisplayString"
_SfcsANIMPicTLPartNumb_Object = MibTableColumn
sfcsANIMPicTLPartNumb = _SfcsANIMPicTLPartNumb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 17),
    _SfcsANIMPicTLPartNumb_Type()
)
sfcsANIMPicTLPartNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicTLPartNumb.setStatus("mandatory")


class _SfcsANIMPicTLSerialNumb_Type(DisplayString):
    """Custom type sfcsANIMPicTLSerialNumb based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SfcsANIMPicTLSerialNumb_Type.__name__ = "DisplayString"
_SfcsANIMPicTLSerialNumb_Object = MibTableColumn
sfcsANIMPicTLSerialNumb = _SfcsANIMPicTLSerialNumb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 18),
    _SfcsANIMPicTLSerialNumb_Type()
)
sfcsANIMPicTLSerialNumb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicTLSerialNumb.setStatus("mandatory")


class _SfcsANIMPicTLReworkLocation_Type(DisplayString):
    """Custom type sfcsANIMPicTLReworkLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SfcsANIMPicTLReworkLocation_Type.__name__ = "DisplayString"
_SfcsANIMPicTLReworkLocation_Object = MibTableColumn
sfcsANIMPicTLReworkLocation = _SfcsANIMPicTLReworkLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 19),
    _SfcsANIMPicTLReworkLocation_Type()
)
sfcsANIMPicTLReworkLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicTLReworkLocation.setStatus("mandatory")


class _SfcsANIMPicTLMfgLocation_Type(DisplayString):
    """Custom type sfcsANIMPicTLMfgLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SfcsANIMPicTLMfgLocation_Type.__name__ = "DisplayString"
_SfcsANIMPicTLMfgLocation_Object = MibTableColumn
sfcsANIMPicTLMfgLocation = _SfcsANIMPicTLMfgLocation_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 20),
    _SfcsANIMPicTLMfgLocation_Type()
)
sfcsANIMPicTLMfgLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicTLMfgLocation.setStatus("mandatory")


class _SfcsANIMPicTLDateCode_Type(DisplayString):
    """Custom type sfcsANIMPicTLDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SfcsANIMPicTLDateCode_Type.__name__ = "DisplayString"
_SfcsANIMPicTLDateCode_Object = MibTableColumn
sfcsANIMPicTLDateCode = _SfcsANIMPicTLDateCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 21),
    _SfcsANIMPicTLDateCode_Type()
)
sfcsANIMPicTLDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicTLDateCode.setStatus("mandatory")


class _SfcsANIMPicTLRevisionCode_Type(DisplayString):
    """Custom type sfcsANIMPicTLRevisionCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SfcsANIMPicTLRevisionCode_Type.__name__ = "DisplayString"
_SfcsANIMPicTLRevisionCode_Object = MibTableColumn
sfcsANIMPicTLRevisionCode = _SfcsANIMPicTLRevisionCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 22),
    _SfcsANIMPicTLRevisionCode_Type()
)
sfcsANIMPicTLRevisionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicTLRevisionCode.setStatus("mandatory")


class _SfcsANIMPicTLPcbRevision_Type(DisplayString):
    """Custom type sfcsANIMPicTLPcbRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SfcsANIMPicTLPcbRevision_Type.__name__ = "DisplayString"
_SfcsANIMPicTLPcbRevision_Object = MibTableColumn
sfcsANIMPicTLPcbRevision = _SfcsANIMPicTLPcbRevision_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 23),
    _SfcsANIMPicTLPcbRevision_Type()
)
sfcsANIMPicTLPcbRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicTLPcbRevision.setStatus("mandatory")


class _SfcsANIMPicMacAddr_Type(OctetString):
    """Custom type sfcsANIMPicMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_SfcsANIMPicMacAddr_Type.__name__ = "OctetString"
_SfcsANIMPicMacAddr_Object = MibTableColumn
sfcsANIMPicMacAddr = _SfcsANIMPicMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 24),
    _SfcsANIMPicMacAddr_Type()
)
sfcsANIMPicMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicMacAddr.setStatus("mandatory")
_SfcsANIMPicNumbRsvdAddrs_Type = Integer32
_SfcsANIMPicNumbRsvdAddrs_Object = MibTableColumn
sfcsANIMPicNumbRsvdAddrs = _SfcsANIMPicNumbRsvdAddrs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 25),
    _SfcsANIMPicNumbRsvdAddrs_Type()
)
sfcsANIMPicNumbRsvdAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicNumbRsvdAddrs.setStatus("mandatory")


class _SfcsANIMPicBoardLevelRevision_Type(DisplayString):
    """Custom type sfcsANIMPicBoardLevelRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SfcsANIMPicBoardLevelRevision_Type.__name__ = "DisplayString"
_SfcsANIMPicBoardLevelRevision_Object = MibTableColumn
sfcsANIMPicBoardLevelRevision = _SfcsANIMPicBoardLevelRevision_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 26),
    _SfcsANIMPicBoardLevelRevision_Type()
)
sfcsANIMPicBoardLevelRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicBoardLevelRevision.setStatus("mandatory")


class _SfcsANIMPicModuleTypeString_Type(DisplayString):
    """Custom type sfcsANIMPicModuleTypeString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_SfcsANIMPicModuleTypeString_Type.__name__ = "DisplayString"
_SfcsANIMPicModuleTypeString_Object = MibTableColumn
sfcsANIMPicModuleTypeString = _SfcsANIMPicModuleTypeString_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 27),
    _SfcsANIMPicModuleTypeString_Type()
)
sfcsANIMPicModuleTypeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicModuleTypeString.setStatus("mandatory")


class _SfcsANIMPicDcDcConverterType_Type(DisplayString):
    """Custom type sfcsANIMPicDcDcConverterType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )


_SfcsANIMPicDcDcConverterType_Type.__name__ = "DisplayString"
_SfcsANIMPicDcDcConverterType_Object = MibTableColumn
sfcsANIMPicDcDcConverterType = _SfcsANIMPicDcDcConverterType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 28),
    _SfcsANIMPicDcDcConverterType_Type()
)
sfcsANIMPicDcDcConverterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicDcDcConverterType.setStatus("mandatory")


class _SfcsANIMPicDcDcConverterInputPower_Type(DisplayString):
    """Custom type sfcsANIMPicDcDcConverterInputPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SfcsANIMPicDcDcConverterInputPower_Type.__name__ = "DisplayString"
_SfcsANIMPicDcDcConverterInputPower_Object = MibTableColumn
sfcsANIMPicDcDcConverterInputPower = _SfcsANIMPicDcDcConverterInputPower_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 29),
    _SfcsANIMPicDcDcConverterInputPower_Type()
)
sfcsANIMPicDcDcConverterInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicDcDcConverterInputPower.setStatus("mandatory")


class _SfcsANIMPicSmb1PromVersion_Type(DisplayString):
    """Custom type sfcsANIMPicSmb1PromVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SfcsANIMPicSmb1PromVersion_Type.__name__ = "DisplayString"
_SfcsANIMPicSmb1PromVersion_Object = MibTableColumn
sfcsANIMPicSmb1PromVersion = _SfcsANIMPicSmb1PromVersion_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 3, 3, 1, 1, 30),
    _SfcsANIMPicSmb1PromVersion_Type()
)
sfcsANIMPicSmb1PromVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsANIMPicSmb1PromVersion.setStatus("mandatory")
_SfcsInterface_ObjectIdentity = ObjectIdentity
sfcsInterface = _SfcsInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4)
)
_SfcsInterfaceConfig_ObjectIdentity = ObjectIdentity
sfcsInterfaceConfig = _SfcsInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 1)
)
_SfcsInterfaceConfigTable_Object = MibTable
sfcsInterfaceConfigTable = _SfcsInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    sfcsInterfaceConfigTable.setStatus("mandatory")
_SfcsInterfaceConfigEntry_Object = MibTableRow
sfcsInterfaceConfigEntry = _SfcsInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 1, 1, 1)
)
sfcsInterfaceConfigEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsInterfaceConfigInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sfcsInterfaceConfigEntry.setStatus("mandatory")
_SfcsInterfaceConfigInterfaceIndex_Type = Integer32
_SfcsInterfaceConfigInterfaceIndex_Object = MibTableColumn
sfcsInterfaceConfigInterfaceIndex = _SfcsInterfaceConfigInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 1, 1, 1, 1),
    _SfcsInterfaceConfigInterfaceIndex_Type()
)
sfcsInterfaceConfigInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfaceConfigInterfaceIndex.setStatus("mandatory")


class _SfcsInterfaceConfigType_Type(Integer32):
    """Custom type sfcsInterfaceConfigType based on Integer32"""
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
        *(("access-port", 2),
          ("host-ctl-port", 5),
          ("host-mgmt-port", 4),
          ("network-port", 3),
          ("other", 1))
    )


_SfcsInterfaceConfigType_Type.__name__ = "Integer32"
_SfcsInterfaceConfigType_Object = MibTableColumn
sfcsInterfaceConfigType = _SfcsInterfaceConfigType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 1, 1, 1, 2),
    _SfcsInterfaceConfigType_Type()
)
sfcsInterfaceConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfaceConfigType.setStatus("deprecated")


class _SfcsInterfacePeakBufferUseage_Type(Integer32):
    """Custom type sfcsInterfacePeakBufferUseage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsInterfacePeakBufferUseage_Type.__name__ = "Integer32"
_SfcsInterfacePeakBufferUseage_Object = MibTableColumn
sfcsInterfacePeakBufferUseage = _SfcsInterfacePeakBufferUseage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 1, 1, 1, 3),
    _SfcsInterfacePeakBufferUseage_Type()
)
sfcsInterfacePeakBufferUseage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfacePeakBufferUseage.setStatus("mandatory")
_SfcsInterfaceConfigNumberOfQueues_Type = Integer32
_SfcsInterfaceConfigNumberOfQueues_Object = MibTableColumn
sfcsInterfaceConfigNumberOfQueues = _SfcsInterfaceConfigNumberOfQueues_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 1, 1, 1, 4),
    _SfcsInterfaceConfigNumberOfQueues_Type()
)
sfcsInterfaceConfigNumberOfQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfaceConfigNumberOfQueues.setStatus("mandatory")
_SfcsInterfaceConfigSigStackID_Type = Integer32
_SfcsInterfaceConfigSigStackID_Object = MibTableColumn
sfcsInterfaceConfigSigStackID = _SfcsInterfaceConfigSigStackID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 1, 1, 1, 5),
    _SfcsInterfaceConfigSigStackID_Type()
)
sfcsInterfaceConfigSigStackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfaceConfigSigStackID.setStatus("mandatory")


class _SfcsInterfaceConfigClockingSource_Type(Integer32):
    """Custom type sfcsInterfaceConfigClockingSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local-anim-clock", 1),
          ("mother-board-master-clock", 2))
    )


_SfcsInterfaceConfigClockingSource_Type.__name__ = "Integer32"
_SfcsInterfaceConfigClockingSource_Object = MibTableColumn
sfcsInterfaceConfigClockingSource = _SfcsInterfaceConfigClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 1, 1, 1, 6),
    _SfcsInterfaceConfigClockingSource_Type()
)
sfcsInterfaceConfigClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsInterfaceConfigClockingSource.setStatus("mandatory")
_SfcsInterfaceStatistics_ObjectIdentity = ObjectIdentity
sfcsInterfaceStatistics = _SfcsInterfaceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 2)
)
_SfcsInterfaceStatsTable_Object = MibTable
sfcsInterfaceStatsTable = _SfcsInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    sfcsInterfaceStatsTable.setStatus("mandatory")
_SfcsInterfaceStatsEntry_Object = MibTableRow
sfcsInterfaceStatsEntry = _SfcsInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 2, 1, 1)
)
sfcsInterfaceStatsEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsInterfaceStatsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sfcsInterfaceStatsEntry.setStatus("mandatory")
_SfcsInterfaceStatsInterfaceIndex_Type = Integer32
_SfcsInterfaceStatsInterfaceIndex_Object = MibTableColumn
sfcsInterfaceStatsInterfaceIndex = _SfcsInterfaceStatsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 2, 1, 1, 1),
    _SfcsInterfaceStatsInterfaceIndex_Type()
)
sfcsInterfaceStatsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfaceStatsInterfaceIndex.setStatus("mandatory")
_SfcsInterfaceStatsRxErrors_Type = OctetString
_SfcsInterfaceStatsRxErrors_Object = MibTableColumn
sfcsInterfaceStatsRxErrors = _SfcsInterfaceStatsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 2, 1, 1, 2),
    _SfcsInterfaceStatsRxErrors_Type()
)
sfcsInterfaceStatsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfaceStatsRxErrors.setStatus("mandatory")
_SfcsInterfaceStatsVPILookupInvalidErrors_Type = OctetString
_SfcsInterfaceStatsVPILookupInvalidErrors_Object = MibTableColumn
sfcsInterfaceStatsVPILookupInvalidErrors = _SfcsInterfaceStatsVPILookupInvalidErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 2, 1, 1, 3),
    _SfcsInterfaceStatsVPILookupInvalidErrors_Type()
)
sfcsInterfaceStatsVPILookupInvalidErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfaceStatsVPILookupInvalidErrors.setStatus("mandatory")
_SfcsInterfaceStatsRxCnxLookupInvalidErrors_Type = OctetString
_SfcsInterfaceStatsRxCnxLookupInvalidErrors_Object = MibTableColumn
sfcsInterfaceStatsRxCnxLookupInvalidErrors = _SfcsInterfaceStatsRxCnxLookupInvalidErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 2, 1, 1, 4),
    _SfcsInterfaceStatsRxCnxLookupInvalidErrors_Type()
)
sfcsInterfaceStatsRxCnxLookupInvalidErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfaceStatsRxCnxLookupInvalidErrors.setStatus("mandatory")
_SfcsInterfaceStatsRxCellCnt_Type = OctetString
_SfcsInterfaceStatsRxCellCnt_Object = MibTableColumn
sfcsInterfaceStatsRxCellCnt = _SfcsInterfaceStatsRxCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 2, 1, 1, 5),
    _SfcsInterfaceStatsRxCellCnt_Type()
)
sfcsInterfaceStatsRxCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfaceStatsRxCellCnt.setStatus("mandatory")
_SfcsInterfaceStatsTxCellCnt_Type = OctetString
_SfcsInterfaceStatsTxCellCnt_Object = MibTableColumn
sfcsInterfaceStatsTxCellCnt = _SfcsInterfaceStatsTxCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 2, 1, 1, 6),
    _SfcsInterfaceStatsTxCellCnt_Type()
)
sfcsInterfaceStatsTxCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfaceStatsTxCellCnt.setStatus("mandatory")
_SfcsInterfaceStatsOverflowDropCellCnt_Type = OctetString
_SfcsInterfaceStatsOverflowDropCellCnt_Object = MibTableColumn
sfcsInterfaceStatsOverflowDropCellCnt = _SfcsInterfaceStatsOverflowDropCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 4, 2, 1, 1, 7),
    _SfcsInterfaceStatsOverflowDropCellCnt_Type()
)
sfcsInterfaceStatsOverflowDropCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsInterfaceStatsOverflowDropCellCnt.setStatus("mandatory")
_SfcsQueue_ObjectIdentity = ObjectIdentity
sfcsQueue = _SfcsQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5)
)
_SfcsQueueConfig_ObjectIdentity = ObjectIdentity
sfcsQueueConfig = _SfcsQueueConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1)
)
_SfcsQueueConfigTable_Object = MibTable
sfcsQueueConfigTable = _SfcsQueueConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    sfcsQueueConfigTable.setStatus("mandatory")
_SfcsQueueConfigEntry_Object = MibTableRow
sfcsQueueConfigEntry = _SfcsQueueConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1, 1, 1)
)
sfcsQueueConfigEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsQueueConfigInterfaceIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsQueueConfigQueueIndex"),
)
if mibBuilder.loadTexts:
    sfcsQueueConfigEntry.setStatus("mandatory")
_SfcsQueueConfigInterfaceIndex_Type = Integer32
_SfcsQueueConfigInterfaceIndex_Object = MibTableColumn
sfcsQueueConfigInterfaceIndex = _SfcsQueueConfigInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1, 1, 1, 1),
    _SfcsQueueConfigInterfaceIndex_Type()
)
sfcsQueueConfigInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsQueueConfigInterfaceIndex.setStatus("mandatory")
_SfcsQueueConfigQueueIndex_Type = Integer32
_SfcsQueueConfigQueueIndex_Object = MibTableColumn
sfcsQueueConfigQueueIndex = _SfcsQueueConfigQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1, 1, 1, 2),
    _SfcsQueueConfigQueueIndex_Type()
)
sfcsQueueConfigQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsQueueConfigQueueIndex.setStatus("mandatory")
_SfcsQueueConfigQueueSize_Type = Integer32
_SfcsQueueConfigQueueSize_Object = MibTableColumn
sfcsQueueConfigQueueSize = _SfcsQueueConfigQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1, 1, 1, 3),
    _SfcsQueueConfigQueueSize_Type()
)
sfcsQueueConfigQueueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsQueueConfigQueueSize.setStatus("mandatory")


class _SfcsQueueConfigQueueBandwidth_Type(Integer32):
    """Custom type sfcsQueueConfigQueueBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsQueueConfigQueueBandwidth_Type.__name__ = "Integer32"
_SfcsQueueConfigQueueBandwidth_Object = MibTableColumn
sfcsQueueConfigQueueBandwidth = _SfcsQueueConfigQueueBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1, 1, 1, 4),
    _SfcsQueueConfigQueueBandwidth_Type()
)
sfcsQueueConfigQueueBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsQueueConfigQueueBandwidth.setStatus("mandatory")


class _SfcsQueueConfigClpDropThreshold_Type(Integer32):
    """Custom type sfcsQueueConfigClpDropThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsQueueConfigClpDropThreshold_Type.__name__ = "Integer32"
_SfcsQueueConfigClpDropThreshold_Object = MibTableColumn
sfcsQueueConfigClpDropThreshold = _SfcsQueueConfigClpDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1, 1, 1, 5),
    _SfcsQueueConfigClpDropThreshold_Type()
)
sfcsQueueConfigClpDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsQueueConfigClpDropThreshold.setStatus("mandatory")


class _SfcsQueueConfigCongestionThreshold_Type(Integer32):
    """Custom type sfcsQueueConfigCongestionThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsQueueConfigCongestionThreshold_Type.__name__ = "Integer32"
_SfcsQueueConfigCongestionThreshold_Object = MibTableColumn
sfcsQueueConfigCongestionThreshold = _SfcsQueueConfigCongestionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1, 1, 1, 6),
    _SfcsQueueConfigCongestionThreshold_Type()
)
sfcsQueueConfigCongestionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsQueueConfigCongestionThreshold.setStatus("mandatory")


class _SfcsQueueConfigEFCILowThreshold_Type(Integer32):
    """Custom type sfcsQueueConfigEFCILowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsQueueConfigEFCILowThreshold_Type.__name__ = "Integer32"
_SfcsQueueConfigEFCILowThreshold_Object = MibTableColumn
sfcsQueueConfigEFCILowThreshold = _SfcsQueueConfigEFCILowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1, 1, 1, 7),
    _SfcsQueueConfigEFCILowThreshold_Type()
)
sfcsQueueConfigEFCILowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsQueueConfigEFCILowThreshold.setStatus("mandatory")


class _SfcsQueueConfigRMThreshold_Type(Integer32):
    """Custom type sfcsQueueConfigRMThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsQueueConfigRMThreshold_Type.__name__ = "Integer32"
_SfcsQueueConfigRMThreshold_Object = MibTableColumn
sfcsQueueConfigRMThreshold = _SfcsQueueConfigRMThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1, 1, 1, 8),
    _SfcsQueueConfigRMThreshold_Type()
)
sfcsQueueConfigRMThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsQueueConfigRMThreshold.setStatus("mandatory")


class _SfcsQueueConfigEPDThreshold_Type(Integer32):
    """Custom type sfcsQueueConfigEPDThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsQueueConfigEPDThreshold_Type.__name__ = "Integer32"
_SfcsQueueConfigEPDThreshold_Object = MibTableColumn
sfcsQueueConfigEPDThreshold = _SfcsQueueConfigEPDThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 1, 1, 1, 9),
    _SfcsQueueConfigEPDThreshold_Type()
)
sfcsQueueConfigEPDThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsQueueConfigEPDThreshold.setStatus("mandatory")
_SfcsQueueStatistics_ObjectIdentity = ObjectIdentity
sfcsQueueStatistics = _SfcsQueueStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 2)
)
_SfcsQueueStatsTable_Object = MibTable
sfcsQueueStatsTable = _SfcsQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    sfcsQueueStatsTable.setStatus("mandatory")
_SfcsQueueStatsEntry_Object = MibTableRow
sfcsQueueStatsEntry = _SfcsQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 2, 1, 1)
)
sfcsQueueStatsEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsQueueStatsInterfaceIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsQueueStatsQueue"),
)
if mibBuilder.loadTexts:
    sfcsQueueStatsEntry.setStatus("mandatory")
_SfcsQueueStatsInterfaceIndex_Type = Integer32
_SfcsQueueStatsInterfaceIndex_Object = MibTableColumn
sfcsQueueStatsInterfaceIndex = _SfcsQueueStatsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 2, 1, 1, 1),
    _SfcsQueueStatsInterfaceIndex_Type()
)
sfcsQueueStatsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsQueueStatsInterfaceIndex.setStatus("mandatory")
_SfcsQueueStatsQueue_Type = Integer32
_SfcsQueueStatsQueue_Object = MibTableColumn
sfcsQueueStatsQueue = _SfcsQueueStatsQueue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 2, 1, 1, 2),
    _SfcsQueueStatsQueue_Type()
)
sfcsQueueStatsQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsQueueStatsQueue.setStatus("mandatory")
_SfcsQueueStatsTxClpCellsDiscarded_Type = OctetString
_SfcsQueueStatsTxClpCellsDiscarded_Object = MibTableColumn
sfcsQueueStatsTxClpCellsDiscarded = _SfcsQueueStatsTxClpCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 2, 1, 1, 3),
    _SfcsQueueStatsTxClpCellsDiscarded_Type()
)
sfcsQueueStatsTxClpCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsQueueStatsTxClpCellsDiscarded.setStatus("mandatory")
_SfcsQueueStatsTxCellsDropped_Type = OctetString
_SfcsQueueStatsTxCellsDropped_Object = MibTableColumn
sfcsQueueStatsTxCellsDropped = _SfcsQueueStatsTxCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 2, 1, 1, 4),
    _SfcsQueueStatsTxCellsDropped_Type()
)
sfcsQueueStatsTxCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsQueueStatsTxCellsDropped.setStatus("mandatory")
_SfcsQueueStatsQueuePeakLevel_Type = Integer32
_SfcsQueueStatsQueuePeakLevel_Object = MibTableColumn
sfcsQueueStatsQueuePeakLevel = _SfcsQueueStatsQueuePeakLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 2, 1, 1, 5),
    _SfcsQueueStatsQueuePeakLevel_Type()
)
sfcsQueueStatsQueuePeakLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsQueueStatsQueuePeakLevel.setStatus("mandatory")
_SfcsQueueStatsTxCellCnt_Type = OctetString
_SfcsQueueStatsTxCellCnt_Object = MibTableColumn
sfcsQueueStatsTxCellCnt = _SfcsQueueStatsTxCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 5, 2, 1, 1, 6),
    _SfcsQueueStatsTxCellCnt_Type()
)
sfcsQueueStatsTxCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsQueueStatsTxCellCnt.setStatus("mandatory")
_SfcsConnection_ObjectIdentity = ObjectIdentity
sfcsConnection = _SfcsConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7)
)
_SfcsConnectionConfig_ObjectIdentity = ObjectIdentity
sfcsConnectionConfig = _SfcsConnectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1)
)
_SfcsCnxCfgTable_Object = MibTable
sfcsCnxCfgTable = _SfcsCnxCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    sfcsCnxCfgTable.setStatus("mandatory")
_SfcsCnxCfgEntry_Object = MibTableRow
sfcsCnxCfgEntry = _SfcsCnxCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1)
)
sfcsCnxCfgEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsCnxCfgCrossConnectIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxCfgCrossConnectLowIfIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxCfgCrossConnectLowVpi"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxCfgCrossConnectLowVci"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxCfgCrossConnectHighIfIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxCfgCrossConnectHighVpi"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxCfgCrossConnectHighVci"),
)
if mibBuilder.loadTexts:
    sfcsCnxCfgEntry.setStatus("mandatory")
_SfcsCnxCfgCrossConnectIndex_Type = Integer32
_SfcsCnxCfgCrossConnectIndex_Object = MibTableColumn
sfcsCnxCfgCrossConnectIndex = _SfcsCnxCfgCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 1),
    _SfcsCnxCfgCrossConnectIndex_Type()
)
sfcsCnxCfgCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgCrossConnectIndex.setStatus("mandatory")
_SfcsCnxCfgCrossConnectLowIfIndex_Type = Integer32
_SfcsCnxCfgCrossConnectLowIfIndex_Object = MibTableColumn
sfcsCnxCfgCrossConnectLowIfIndex = _SfcsCnxCfgCrossConnectLowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 2),
    _SfcsCnxCfgCrossConnectLowIfIndex_Type()
)
sfcsCnxCfgCrossConnectLowIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgCrossConnectLowIfIndex.setStatus("mandatory")


class _SfcsCnxCfgCrossConnectLowVpi_Type(Integer32):
    """Custom type sfcsCnxCfgCrossConnectLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SfcsCnxCfgCrossConnectLowVpi_Type.__name__ = "Integer32"
_SfcsCnxCfgCrossConnectLowVpi_Object = MibTableColumn
sfcsCnxCfgCrossConnectLowVpi = _SfcsCnxCfgCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 3),
    _SfcsCnxCfgCrossConnectLowVpi_Type()
)
sfcsCnxCfgCrossConnectLowVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgCrossConnectLowVpi.setStatus("mandatory")


class _SfcsCnxCfgCrossConnectLowVci_Type(Integer32):
    """Custom type sfcsCnxCfgCrossConnectLowVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfcsCnxCfgCrossConnectLowVci_Type.__name__ = "Integer32"
_SfcsCnxCfgCrossConnectLowVci_Object = MibTableColumn
sfcsCnxCfgCrossConnectLowVci = _SfcsCnxCfgCrossConnectLowVci_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 4),
    _SfcsCnxCfgCrossConnectLowVci_Type()
)
sfcsCnxCfgCrossConnectLowVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgCrossConnectLowVci.setStatus("mandatory")
_SfcsCnxCfgCrossConnectHighIfIndex_Type = Integer32
_SfcsCnxCfgCrossConnectHighIfIndex_Object = MibTableColumn
sfcsCnxCfgCrossConnectHighIfIndex = _SfcsCnxCfgCrossConnectHighIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 5),
    _SfcsCnxCfgCrossConnectHighIfIndex_Type()
)
sfcsCnxCfgCrossConnectHighIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgCrossConnectHighIfIndex.setStatus("mandatory")


class _SfcsCnxCfgCrossConnectHighVpi_Type(Integer32):
    """Custom type sfcsCnxCfgCrossConnectHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SfcsCnxCfgCrossConnectHighVpi_Type.__name__ = "Integer32"
_SfcsCnxCfgCrossConnectHighVpi_Object = MibTableColumn
sfcsCnxCfgCrossConnectHighVpi = _SfcsCnxCfgCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 6),
    _SfcsCnxCfgCrossConnectHighVpi_Type()
)
sfcsCnxCfgCrossConnectHighVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgCrossConnectHighVpi.setStatus("mandatory")


class _SfcsCnxCfgCrossConnectHighVci_Type(Integer32):
    """Custom type sfcsCnxCfgCrossConnectHighVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfcsCnxCfgCrossConnectHighVci_Type.__name__ = "Integer32"
_SfcsCnxCfgCrossConnectHighVci_Object = MibTableColumn
sfcsCnxCfgCrossConnectHighVci = _SfcsCnxCfgCrossConnectHighVci_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 7),
    _SfcsCnxCfgCrossConnectHighVci_Type()
)
sfcsCnxCfgCrossConnectHighVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgCrossConnectHighVci.setStatus("mandatory")


class _SfcsCnxCfgType_Type(Integer32):
    """Custom type sfcsCnxCfgType based on Integer32"""
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
        *(("mpoint-to-mpoint-vcl", 6),
          ("mpoint-to-mpoint-vpl", 3),
          ("point-to-mpoint-vcl", 5),
          ("point-to-mpoint-vpl", 2),
          ("point-to-point-vcl", 4),
          ("point-to-point-vpl", 1))
    )


_SfcsCnxCfgType_Type.__name__ = "Integer32"
_SfcsCnxCfgType_Object = MibTableColumn
sfcsCnxCfgType = _SfcsCnxCfgType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 8),
    _SfcsCnxCfgType_Type()
)
sfcsCnxCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgType.setStatus("mandatory")


class _SfcsCnxCfgTmType_Type(Integer32):
    """Custom type sfcsCnxCfgTmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("efci", 2),
          ("er", 3),
          ("other", 1))
    )


_SfcsCnxCfgTmType_Type.__name__ = "Integer32"
_SfcsCnxCfgTmType_Object = MibTableColumn
sfcsCnxCfgTmType = _SfcsCnxCfgTmType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 9),
    _SfcsCnxCfgTmType_Type()
)
sfcsCnxCfgTmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgTmType.setStatus("mandatory")


class _SfcsCnxCfgUPCEnable_Type(Integer32):
    """Custom type sfcsCnxCfgUPCEnable based on Integer32"""
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
        *(("h-l-tag-enabled", 8),
          ("h-l-upc-enabled", 4),
          ("h-l-upc-tag-enabled", 12),
          ("l-h-Tag-and-h-l-upc-enabled", 6),
          ("l-h-tag-and-h-l-tag-enabled", 10),
          ("l-h-tag-and-h-l-upc-tag-enabled", 14),
          ("l-h-tag-enabled", 2),
          ("l-h-upc-and-h-l-tag-enabled", 9),
          ("l-h-upc-and-h-l-upc-enabled", 5),
          ("l-h-upc-and-h-l-upc-tag-enabled", 13),
          ("l-h-upc-enabled", 1),
          ("l-h-upc-tag-and-h-l-tag-enabled", 11),
          ("l-h-upc-tag-and-h-l-upc-enabled", 7),
          ("l-h-upc-tag-and-h-l-upc-tag-enabled", 15),
          ("l-h-upc-tag-enabled", 3))
    )


_SfcsCnxCfgUPCEnable_Type.__name__ = "Integer32"
_SfcsCnxCfgUPCEnable_Object = MibTableColumn
sfcsCnxCfgUPCEnable = _SfcsCnxCfgUPCEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 10),
    _SfcsCnxCfgUPCEnable_Type()
)
sfcsCnxCfgUPCEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgUPCEnable.setStatus("mandatory")


class _SfcsCnxCfgStatsEnable_Type(Integer32):
    """Custom type sfcsCnxCfgStatsEnable based on Integer32"""
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
          ("enabled", 1),
          ("other", 3))
    )


_SfcsCnxCfgStatsEnable_Type.__name__ = "Integer32"
_SfcsCnxCfgStatsEnable_Object = MibTableColumn
sfcsCnxCfgStatsEnable = _SfcsCnxCfgStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 11),
    _SfcsCnxCfgStatsEnable_Type()
)
sfcsCnxCfgStatsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgStatsEnable.setStatus("mandatory")


class _SfcsCnxCfgStatsTableCounterSizes_Type(Integer32):
    """Custom type sfcsCnxCfgStatsTableCounterSizes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sixteenbiteachcounter", 3),
          ("thirtytwobitdropcounter", 2),
          ("thirtytwobittagcounter", 1))
    )


_SfcsCnxCfgStatsTableCounterSizes_Type.__name__ = "Integer32"
_SfcsCnxCfgStatsTableCounterSizes_Object = MibTableColumn
sfcsCnxCfgStatsTableCounterSizes = _SfcsCnxCfgStatsTableCounterSizes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 12),
    _SfcsCnxCfgStatsTableCounterSizes_Type()
)
sfcsCnxCfgStatsTableCounterSizes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgStatsTableCounterSizes.setStatus("mandatory")


class _SfcsCnxCfgOwner_Type(Integer32):
    """Custom type sfcsCnxCfgOwner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dontown", 3),
          ("other", 1),
          ("own", 2))
    )


_SfcsCnxCfgOwner_Type.__name__ = "Integer32"
_SfcsCnxCfgOwner_Object = MibTableColumn
sfcsCnxCfgOwner = _SfcsCnxCfgOwner_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 1, 1, 1, 13),
    _SfcsCnxCfgOwner_Type()
)
sfcsCnxCfgOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxCfgOwner.setStatus("mandatory")
_SfcsConnectionStatistics_ObjectIdentity = ObjectIdentity
sfcsConnectionStatistics = _SfcsConnectionStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2)
)
_SfcsCnxStatsTable_Object = MibTable
sfcsCnxStatsTable = _SfcsCnxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    sfcsCnxStatsTable.setStatus("mandatory")
_SfcsCnxStatsEntry_Object = MibTableRow
sfcsCnxStatsEntry = _SfcsCnxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1)
)
sfcsCnxStatsEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsCnxStatsCrossConnectIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxStatsCrossConnectLowIfIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxStatsCrossConnectLowVpi"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxStatsCrossConnectLowVci"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxStatsCrossConnectHighIfIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxStatsCrossConnectHighVpi"),
    (0, "CTRON-SFCS-MIB", "sfcsCnxStatsCrossConnectHighVci"),
)
if mibBuilder.loadTexts:
    sfcsCnxStatsEntry.setStatus("mandatory")
_SfcsCnxStatsCrossConnectIndex_Type = Integer32
_SfcsCnxStatsCrossConnectIndex_Object = MibTableColumn
sfcsCnxStatsCrossConnectIndex = _SfcsCnxStatsCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 1),
    _SfcsCnxStatsCrossConnectIndex_Type()
)
sfcsCnxStatsCrossConnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsCrossConnectIndex.setStatus("mandatory")
_SfcsCnxStatsCrossConnectLowIfIndex_Type = Integer32
_SfcsCnxStatsCrossConnectLowIfIndex_Object = MibTableColumn
sfcsCnxStatsCrossConnectLowIfIndex = _SfcsCnxStatsCrossConnectLowIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 2),
    _SfcsCnxStatsCrossConnectLowIfIndex_Type()
)
sfcsCnxStatsCrossConnectLowIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsCrossConnectLowIfIndex.setStatus("mandatory")


class _SfcsCnxStatsCrossConnectLowVpi_Type(Integer32):
    """Custom type sfcsCnxStatsCrossConnectLowVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SfcsCnxStatsCrossConnectLowVpi_Type.__name__ = "Integer32"
_SfcsCnxStatsCrossConnectLowVpi_Object = MibTableColumn
sfcsCnxStatsCrossConnectLowVpi = _SfcsCnxStatsCrossConnectLowVpi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 3),
    _SfcsCnxStatsCrossConnectLowVpi_Type()
)
sfcsCnxStatsCrossConnectLowVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsCrossConnectLowVpi.setStatus("mandatory")


class _SfcsCnxStatsCrossConnectLowVci_Type(Integer32):
    """Custom type sfcsCnxStatsCrossConnectLowVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfcsCnxStatsCrossConnectLowVci_Type.__name__ = "Integer32"
_SfcsCnxStatsCrossConnectLowVci_Object = MibTableColumn
sfcsCnxStatsCrossConnectLowVci = _SfcsCnxStatsCrossConnectLowVci_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 4),
    _SfcsCnxStatsCrossConnectLowVci_Type()
)
sfcsCnxStatsCrossConnectLowVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsCrossConnectLowVci.setStatus("mandatory")
_SfcsCnxStatsCrossConnectHighIfIndex_Type = Integer32
_SfcsCnxStatsCrossConnectHighIfIndex_Object = MibTableColumn
sfcsCnxStatsCrossConnectHighIfIndex = _SfcsCnxStatsCrossConnectHighIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 5),
    _SfcsCnxStatsCrossConnectHighIfIndex_Type()
)
sfcsCnxStatsCrossConnectHighIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsCrossConnectHighIfIndex.setStatus("mandatory")


class _SfcsCnxStatsCrossConnectHighVpi_Type(Integer32):
    """Custom type sfcsCnxStatsCrossConnectHighVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_SfcsCnxStatsCrossConnectHighVpi_Type.__name__ = "Integer32"
_SfcsCnxStatsCrossConnectHighVpi_Object = MibTableColumn
sfcsCnxStatsCrossConnectHighVpi = _SfcsCnxStatsCrossConnectHighVpi_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 6),
    _SfcsCnxStatsCrossConnectHighVpi_Type()
)
sfcsCnxStatsCrossConnectHighVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsCrossConnectHighVpi.setStatus("mandatory")


class _SfcsCnxStatsCrossConnectHighVci_Type(Integer32):
    """Custom type sfcsCnxStatsCrossConnectHighVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SfcsCnxStatsCrossConnectHighVci_Type.__name__ = "Integer32"
_SfcsCnxStatsCrossConnectHighVci_Object = MibTableColumn
sfcsCnxStatsCrossConnectHighVci = _SfcsCnxStatsCrossConnectHighVci_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 7),
    _SfcsCnxStatsCrossConnectHighVci_Type()
)
sfcsCnxStatsCrossConnectHighVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsCrossConnectHighVci.setStatus("mandatory")
_SfcsCnxStatsLoToHiHTxCells_Type = OctetString
_SfcsCnxStatsLoToHiHTxCells_Object = MibTableColumn
sfcsCnxStatsLoToHiHTxCells = _SfcsCnxStatsLoToHiHTxCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 8),
    _SfcsCnxStatsLoToHiHTxCells_Type()
)
sfcsCnxStatsLoToHiHTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsLoToHiHTxCells.setStatus("mandatory")
_SfcsCnxStatsLoToHiDroppedCells_Type = OctetString
_SfcsCnxStatsLoToHiDroppedCells_Object = MibTableColumn
sfcsCnxStatsLoToHiDroppedCells = _SfcsCnxStatsLoToHiDroppedCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 9),
    _SfcsCnxStatsLoToHiDroppedCells_Type()
)
sfcsCnxStatsLoToHiDroppedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsLoToHiDroppedCells.setStatus("mandatory")
_SfcsCnxStatsLoToHiTaggedCells_Type = OctetString
_SfcsCnxStatsLoToHiTaggedCells_Object = MibTableColumn
sfcsCnxStatsLoToHiTaggedCells = _SfcsCnxStatsLoToHiTaggedCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 10),
    _SfcsCnxStatsLoToHiTaggedCells_Type()
)
sfcsCnxStatsLoToHiTaggedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsLoToHiTaggedCells.setStatus("mandatory")
_SfcsCnxStatsHiToLoHTxCells_Type = OctetString
_SfcsCnxStatsHiToLoHTxCells_Object = MibTableColumn
sfcsCnxStatsHiToLoHTxCells = _SfcsCnxStatsHiToLoHTxCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 11),
    _SfcsCnxStatsHiToLoHTxCells_Type()
)
sfcsCnxStatsHiToLoHTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsHiToLoHTxCells.setStatus("mandatory")
_SfcsCnxStatsHiToLoDroppedCells_Type = OctetString
_SfcsCnxStatsHiToLoDroppedCells_Object = MibTableColumn
sfcsCnxStatsHiToLoDroppedCells = _SfcsCnxStatsHiToLoDroppedCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 12),
    _SfcsCnxStatsHiToLoDroppedCells_Type()
)
sfcsCnxStatsHiToLoDroppedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsHiToLoDroppedCells.setStatus("mandatory")
_SfcsCnxStatsHiToLoTaggedCells_Type = OctetString
_SfcsCnxStatsHiToLoTaggedCells_Object = MibTableColumn
sfcsCnxStatsHiToLoTaggedCells = _SfcsCnxStatsHiToLoTaggedCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 2, 1, 1, 13),
    _SfcsCnxStatsHiToLoTaggedCells_Type()
)
sfcsCnxStatsHiToLoTaggedCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxStatsHiToLoTaggedCells.setStatus("mandatory")
_SfcsConnectionError_ObjectIdentity = ObjectIdentity
sfcsConnectionError = _SfcsConnectionError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 3)
)
_SfcsCnxErrorTable_Object = MibTable
sfcsCnxErrorTable = _SfcsCnxErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    sfcsCnxErrorTable.setStatus("mandatory")
_SfcsCnxErrorEntry_Object = MibTableRow
sfcsCnxErrorEntry = _SfcsCnxErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 3, 1, 1)
)
sfcsCnxErrorEntry.setIndexNames(
    (0, "ATM-MIB", "atmVcCrossConnectIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectLowIfIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectLowVpi"),
    (0, "ATM-MIB", "atmVcCrossConnectLowVci"),
    (0, "ATM-MIB", "atmVcCrossConnectHighIfIndex"),
    (0, "ATM-MIB", "atmVcCrossConnectHighVpi"),
    (0, "ATM-MIB", "atmVcCrossConnectHighVci"),
)
if mibBuilder.loadTexts:
    sfcsCnxErrorEntry.setStatus("mandatory")
_SfcsCnxErrorCode_Type = OctetString
_SfcsCnxErrorCode_Object = MibTableColumn
sfcsCnxErrorCode = _SfcsCnxErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 3, 1, 1, 1),
    _SfcsCnxErrorCode_Type()
)
sfcsCnxErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxErrorCode.setStatus("mandatory")
_SfcsCnxErrorTimeStamp_Type = TimeTicks
_SfcsCnxErrorTimeStamp_Object = MibTableColumn
sfcsCnxErrorTimeStamp = _SfcsCnxErrorTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 3, 1, 1, 2),
    _SfcsCnxErrorTimeStamp_Type()
)
sfcsCnxErrorTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxErrorTimeStamp.setStatus("mandatory")


class _SfcsCnxErrorRowStatus_Type(Integer32):
    """Custom type sfcsCnxErrorRowStatus based on Integer32"""
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
        *(("active", 3),
          ("delete", 4),
          ("inactive", 2),
          ("other", 1))
    )


_SfcsCnxErrorRowStatus_Type.__name__ = "Integer32"
_SfcsCnxErrorRowStatus_Object = MibTableColumn
sfcsCnxErrorRowStatus = _SfcsCnxErrorRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 7, 3, 1, 1, 3),
    _SfcsCnxErrorRowStatus_Type()
)
sfcsCnxErrorRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsCnxErrorRowStatus.setStatus("mandatory")
_SfcsConnectionAPI_ObjectIdentity = ObjectIdentity
sfcsConnectionAPI = _SfcsConnectionAPI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 8)
)


class _SfcsCnxAPIEntry_Type(Integer32):
    """Custom type sfcsCnxAPIEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SfcsCnxAPIEntry_Type.__name__ = "Integer32"
_SfcsCnxAPIEntry_Object = MibScalar
sfcsCnxAPIEntry = _SfcsCnxAPIEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 8, 1),
    _SfcsCnxAPIEntry_Type()
)
sfcsCnxAPIEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCnxAPIEntry.setStatus("mandatory")
_SfcsCTM_ObjectIdentity = ObjectIdentity
sfcsCTM = _SfcsCTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9)
)
_SfcsCTMInterfaceConfig_ObjectIdentity = ObjectIdentity
sfcsCTMInterfaceConfig = _SfcsCTMInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 1)
)
_SfcsCTMInterfaceConfigTable_Object = MibTable
sfcsCTMInterfaceConfigTable = _SfcsCTMInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    sfcsCTMInterfaceConfigTable.setStatus("mandatory")
_SfcsCTMInterfaceConfigEntry_Object = MibTableRow
sfcsCTMInterfaceConfigEntry = _SfcsCTMInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 1, 1, 1)
)
sfcsCTMInterfaceConfigEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsCTMInterfaceConfigInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sfcsCTMInterfaceConfigEntry.setStatus("mandatory")
_SfcsCTMInterfaceConfigInterfaceIndex_Type = Integer32
_SfcsCTMInterfaceConfigInterfaceIndex_Object = MibTableColumn
sfcsCTMInterfaceConfigInterfaceIndex = _SfcsCTMInterfaceConfigInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 1, 1, 1, 1),
    _SfcsCTMInterfaceConfigInterfaceIndex_Type()
)
sfcsCTMInterfaceConfigInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceConfigInterfaceIndex.setStatus("mandatory")


class _SfcsCTMInterfaceConfigType_Type(Integer32):
    """Custom type sfcsCTMInterfaceConfigType based on Integer32"""
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
        *(("access-port", 2),
          ("host-ctl-port", 5),
          ("host-mgmt-port", 4),
          ("network-port", 3),
          ("other", 1))
    )


_SfcsCTMInterfaceConfigType_Type.__name__ = "Integer32"
_SfcsCTMInterfaceConfigType_Object = MibTableColumn
sfcsCTMInterfaceConfigType = _SfcsCTMInterfaceConfigType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 1, 1, 1, 2),
    _SfcsCTMInterfaceConfigType_Type()
)
sfcsCTMInterfaceConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceConfigType.setStatus("mandatory")


class _SfcsCTMInterfacePeakBufferUseage_Type(Integer32):
    """Custom type sfcsCTMInterfacePeakBufferUseage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsCTMInterfacePeakBufferUseage_Type.__name__ = "Integer32"
_SfcsCTMInterfacePeakBufferUseage_Object = MibTableColumn
sfcsCTMInterfacePeakBufferUseage = _SfcsCTMInterfacePeakBufferUseage_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 1, 1, 1, 3),
    _SfcsCTMInterfacePeakBufferUseage_Type()
)
sfcsCTMInterfacePeakBufferUseage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfacePeakBufferUseage.setStatus("mandatory")
_SfcsCTMInterfaceConfigNumberOfQueues_Type = Integer32
_SfcsCTMInterfaceConfigNumberOfQueues_Object = MibTableColumn
sfcsCTMInterfaceConfigNumberOfQueues = _SfcsCTMInterfaceConfigNumberOfQueues_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 1, 1, 1, 4),
    _SfcsCTMInterfaceConfigNumberOfQueues_Type()
)
sfcsCTMInterfaceConfigNumberOfQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceConfigNumberOfQueues.setStatus("mandatory")
_SfcsCTMInterfaceConfigSigStackID_Type = Integer32
_SfcsCTMInterfaceConfigSigStackID_Object = MibTableColumn
sfcsCTMInterfaceConfigSigStackID = _SfcsCTMInterfaceConfigSigStackID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 1, 1, 1, 5),
    _SfcsCTMInterfaceConfigSigStackID_Type()
)
sfcsCTMInterfaceConfigSigStackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceConfigSigStackID.setStatus("mandatory")


class _SfcsCTMInterfaceConfigClocking_Type(Integer32):
    """Custom type sfcsCTMInterfaceConfigClocking based on Integer32"""
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
        *(("channel-recovered-clock", 2),
          ("generated-transmit-clock", 1),
          ("not-supported", 4),
          ("system-master-clock", 3))
    )


_SfcsCTMInterfaceConfigClocking_Type.__name__ = "Integer32"
_SfcsCTMInterfaceConfigClocking_Object = MibTableColumn
sfcsCTMInterfaceConfigClocking = _SfcsCTMInterfaceConfigClocking_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 1, 1, 1, 6),
    _SfcsCTMInterfaceConfigClocking_Type()
)
sfcsCTMInterfaceConfigClocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceConfigClocking.setStatus("mandatory")
_SfcsCTMInterfaceConfigNextVPI_Type = Integer32
_SfcsCTMInterfaceConfigNextVPI_Object = MibTableColumn
sfcsCTMInterfaceConfigNextVPI = _SfcsCTMInterfaceConfigNextVPI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 1, 1, 1, 7),
    _SfcsCTMInterfaceConfigNextVPI_Type()
)
sfcsCTMInterfaceConfigNextVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceConfigNextVPI.setStatus("mandatory")
_SfcsCTMInterfaceConfigNextVCI_Type = Integer32
_SfcsCTMInterfaceConfigNextVCI_Object = MibTableColumn
sfcsCTMInterfaceConfigNextVCI = _SfcsCTMInterfaceConfigNextVCI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 1, 1, 1, 8),
    _SfcsCTMInterfaceConfigNextVCI_Type()
)
sfcsCTMInterfaceConfigNextVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceConfigNextVCI.setStatus("mandatory")
_SfcsCTMInterfaceStatistics_ObjectIdentity = ObjectIdentity
sfcsCTMInterfaceStatistics = _SfcsCTMInterfaceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 2)
)
_SfcsCTMInterfaceStatsTable_Object = MibTable
sfcsCTMInterfaceStatsTable = _SfcsCTMInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    sfcsCTMInterfaceStatsTable.setStatus("mandatory")
_SfcsCTMInterfaceStatsEntry_Object = MibTableRow
sfcsCTMInterfaceStatsEntry = _SfcsCTMInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 2, 1, 1)
)
sfcsCTMInterfaceStatsEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsCTMInterfaceStatsInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sfcsCTMInterfaceStatsEntry.setStatus("mandatory")
_SfcsCTMInterfaceStatsInterfaceIndex_Type = Integer32
_SfcsCTMInterfaceStatsInterfaceIndex_Object = MibTableColumn
sfcsCTMInterfaceStatsInterfaceIndex = _SfcsCTMInterfaceStatsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 2, 1, 1, 1),
    _SfcsCTMInterfaceStatsInterfaceIndex_Type()
)
sfcsCTMInterfaceStatsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceStatsInterfaceIndex.setStatus("mandatory")
_SfcsCTMInterfaceStatsRxErrors_Type = OctetString
_SfcsCTMInterfaceStatsRxErrors_Object = MibTableColumn
sfcsCTMInterfaceStatsRxErrors = _SfcsCTMInterfaceStatsRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 2, 1, 1, 2),
    _SfcsCTMInterfaceStatsRxErrors_Type()
)
sfcsCTMInterfaceStatsRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceStatsRxErrors.setStatus("mandatory")
_SfcsCTMInterfaceStatsVPILookupInvalidErrors_Type = OctetString
_SfcsCTMInterfaceStatsVPILookupInvalidErrors_Object = MibTableColumn
sfcsCTMInterfaceStatsVPILookupInvalidErrors = _SfcsCTMInterfaceStatsVPILookupInvalidErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 2, 1, 1, 3),
    _SfcsCTMInterfaceStatsVPILookupInvalidErrors_Type()
)
sfcsCTMInterfaceStatsVPILookupInvalidErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceStatsVPILookupInvalidErrors.setStatus("mandatory")
_SfcsCTMInterfaceStatsRxCnxLookupInvalidErrors_Type = OctetString
_SfcsCTMInterfaceStatsRxCnxLookupInvalidErrors_Object = MibTableColumn
sfcsCTMInterfaceStatsRxCnxLookupInvalidErrors = _SfcsCTMInterfaceStatsRxCnxLookupInvalidErrors_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 2, 1, 1, 4),
    _SfcsCTMInterfaceStatsRxCnxLookupInvalidErrors_Type()
)
sfcsCTMInterfaceStatsRxCnxLookupInvalidErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceStatsRxCnxLookupInvalidErrors.setStatus("mandatory")
_SfcsCTMInterfaceStatsRxCellCnt_Type = OctetString
_SfcsCTMInterfaceStatsRxCellCnt_Object = MibTableColumn
sfcsCTMInterfaceStatsRxCellCnt = _SfcsCTMInterfaceStatsRxCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 2, 1, 1, 7),
    _SfcsCTMInterfaceStatsRxCellCnt_Type()
)
sfcsCTMInterfaceStatsRxCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceStatsRxCellCnt.setStatus("mandatory")
_SfcsCTMInterfaceStatsTxCellCnt_Type = OctetString
_SfcsCTMInterfaceStatsTxCellCnt_Object = MibTableColumn
sfcsCTMInterfaceStatsTxCellCnt = _SfcsCTMInterfaceStatsTxCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 2, 1, 1, 8),
    _SfcsCTMInterfaceStatsTxCellCnt_Type()
)
sfcsCTMInterfaceStatsTxCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceStatsTxCellCnt.setStatus("mandatory")
_SfcsCTMInterfaceStatsOverflowDropCellCnt_Type = OctetString
_SfcsCTMInterfaceStatsOverflowDropCellCnt_Object = MibTableColumn
sfcsCTMInterfaceStatsOverflowDropCellCnt = _SfcsCTMInterfaceStatsOverflowDropCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 2, 1, 1, 9),
    _SfcsCTMInterfaceStatsOverflowDropCellCnt_Type()
)
sfcsCTMInterfaceStatsOverflowDropCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMInterfaceStatsOverflowDropCellCnt.setStatus("mandatory")
_SfcsCTMQueueConfig_ObjectIdentity = ObjectIdentity
sfcsCTMQueueConfig = _SfcsCTMQueueConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 3)
)
_SfcsCTMQueueConfigTable_Object = MibTable
sfcsCTMQueueConfigTable = _SfcsCTMQueueConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    sfcsCTMQueueConfigTable.setStatus("mandatory")
_SfcsCTMQueueConfigEntry_Object = MibTableRow
sfcsCTMQueueConfigEntry = _SfcsCTMQueueConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 3, 1, 1)
)
sfcsCTMQueueConfigEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsCTMQueueConfigInterfaceIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsQueueConfigQueueIndex"),
)
if mibBuilder.loadTexts:
    sfcsCTMQueueConfigEntry.setStatus("mandatory")
_SfcsCTMQueueConfigInterfaceIndex_Type = Integer32
_SfcsCTMQueueConfigInterfaceIndex_Object = MibTableColumn
sfcsCTMQueueConfigInterfaceIndex = _SfcsCTMQueueConfigInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 3, 1, 1, 1),
    _SfcsCTMQueueConfigInterfaceIndex_Type()
)
sfcsCTMQueueConfigInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMQueueConfigInterfaceIndex.setStatus("mandatory")
_SfcsCTMQueueConfigQueueIndex_Type = Integer32
_SfcsCTMQueueConfigQueueIndex_Object = MibTableColumn
sfcsCTMQueueConfigQueueIndex = _SfcsCTMQueueConfigQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 3, 1, 1, 2),
    _SfcsCTMQueueConfigQueueIndex_Type()
)
sfcsCTMQueueConfigQueueIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMQueueConfigQueueIndex.setStatus("mandatory")
_SfcsCTMQueueConfigQueueSize_Type = Integer32
_SfcsCTMQueueConfigQueueSize_Object = MibTableColumn
sfcsCTMQueueConfigQueueSize = _SfcsCTMQueueConfigQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 3, 1, 1, 3),
    _SfcsCTMQueueConfigQueueSize_Type()
)
sfcsCTMQueueConfigQueueSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsCTMQueueConfigQueueSize.setStatus("mandatory")


class _SfcsCTMQueueConfigQueueBandwidth_Type(Integer32):
    """Custom type sfcsCTMQueueConfigQueueBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsCTMQueueConfigQueueBandwidth_Type.__name__ = "Integer32"
_SfcsCTMQueueConfigQueueBandwidth_Object = MibTableColumn
sfcsCTMQueueConfigQueueBandwidth = _SfcsCTMQueueConfigQueueBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 3, 1, 1, 4),
    _SfcsCTMQueueConfigQueueBandwidth_Type()
)
sfcsCTMQueueConfigQueueBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsCTMQueueConfigQueueBandwidth.setStatus("mandatory")


class _SfcsCTMQueueConfigClpDropThreshold_Type(Integer32):
    """Custom type sfcsCTMQueueConfigClpDropThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsCTMQueueConfigClpDropThreshold_Type.__name__ = "Integer32"
_SfcsCTMQueueConfigClpDropThreshold_Object = MibTableColumn
sfcsCTMQueueConfigClpDropThreshold = _SfcsCTMQueueConfigClpDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 3, 1, 1, 5),
    _SfcsCTMQueueConfigClpDropThreshold_Type()
)
sfcsCTMQueueConfigClpDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsCTMQueueConfigClpDropThreshold.setStatus("mandatory")


class _SfcsCTMQueueConfigCongestionThreshold_Type(Integer32):
    """Custom type sfcsCTMQueueConfigCongestionThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsCTMQueueConfigCongestionThreshold_Type.__name__ = "Integer32"
_SfcsCTMQueueConfigCongestionThreshold_Object = MibTableColumn
sfcsCTMQueueConfigCongestionThreshold = _SfcsCTMQueueConfigCongestionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 3, 1, 1, 6),
    _SfcsCTMQueueConfigCongestionThreshold_Type()
)
sfcsCTMQueueConfigCongestionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsCTMQueueConfigCongestionThreshold.setStatus("mandatory")


class _SfcsCTMQueueConfigEFCILowThreshold_Type(Integer32):
    """Custom type sfcsCTMQueueConfigEFCILowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsCTMQueueConfigEFCILowThreshold_Type.__name__ = "Integer32"
_SfcsCTMQueueConfigEFCILowThreshold_Object = MibTableColumn
sfcsCTMQueueConfigEFCILowThreshold = _SfcsCTMQueueConfigEFCILowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 3, 1, 1, 7),
    _SfcsCTMQueueConfigEFCILowThreshold_Type()
)
sfcsCTMQueueConfigEFCILowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsCTMQueueConfigEFCILowThreshold.setStatus("mandatory")


class _SfcsCTMQueueConfigRMThreshold_Type(Integer32):
    """Custom type sfcsCTMQueueConfigRMThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SfcsCTMQueueConfigRMThreshold_Type.__name__ = "Integer32"
_SfcsCTMQueueConfigRMThreshold_Object = MibTableColumn
sfcsCTMQueueConfigRMThreshold = _SfcsCTMQueueConfigRMThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 3, 1, 1, 8),
    _SfcsCTMQueueConfigRMThreshold_Type()
)
sfcsCTMQueueConfigRMThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsCTMQueueConfigRMThreshold.setStatus("mandatory")
_SfcsCTMQueueStatistics_ObjectIdentity = ObjectIdentity
sfcsCTMQueueStatistics = _SfcsCTMQueueStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 4)
)
_SfcsCTMQueueStatsTable_Object = MibTable
sfcsCTMQueueStatsTable = _SfcsCTMQueueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 4, 1)
)
if mibBuilder.loadTexts:
    sfcsCTMQueueStatsTable.setStatus("mandatory")
_SfcsCTMQueueStatsEntry_Object = MibTableRow
sfcsCTMQueueStatsEntry = _SfcsCTMQueueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 4, 1, 1)
)
sfcsCTMQueueStatsEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsCTMQueueStatsInterfaceIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsQueueStatsQueue"),
)
if mibBuilder.loadTexts:
    sfcsCTMQueueStatsEntry.setStatus("mandatory")
_SfcsCTMQueueStatsInterfaceIndex_Type = Integer32
_SfcsCTMQueueStatsInterfaceIndex_Object = MibTableColumn
sfcsCTMQueueStatsInterfaceIndex = _SfcsCTMQueueStatsInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 4, 1, 1, 1),
    _SfcsCTMQueueStatsInterfaceIndex_Type()
)
sfcsCTMQueueStatsInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMQueueStatsInterfaceIndex.setStatus("mandatory")
_SfcsCTMQueueStatsQueue_Type = Integer32
_SfcsCTMQueueStatsQueue_Object = MibTableColumn
sfcsCTMQueueStatsQueue = _SfcsCTMQueueStatsQueue_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 4, 1, 1, 2),
    _SfcsCTMQueueStatsQueue_Type()
)
sfcsCTMQueueStatsQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMQueueStatsQueue.setStatus("mandatory")
_SfcsCTMQueueStatsTxClpCellsDiscarded_Type = OctetString
_SfcsCTMQueueStatsTxClpCellsDiscarded_Object = MibTableColumn
sfcsCTMQueueStatsTxClpCellsDiscarded = _SfcsCTMQueueStatsTxClpCellsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 4, 1, 1, 3),
    _SfcsCTMQueueStatsTxClpCellsDiscarded_Type()
)
sfcsCTMQueueStatsTxClpCellsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMQueueStatsTxClpCellsDiscarded.setStatus("mandatory")
_SfcsCTMQueueStatsTxCellsDropped_Type = OctetString
_SfcsCTMQueueStatsTxCellsDropped_Object = MibTableColumn
sfcsCTMQueueStatsTxCellsDropped = _SfcsCTMQueueStatsTxCellsDropped_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 4, 1, 1, 4),
    _SfcsCTMQueueStatsTxCellsDropped_Type()
)
sfcsCTMQueueStatsTxCellsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMQueueStatsTxCellsDropped.setStatus("mandatory")
_SfcsCTMQueueStatsQueuePeakLevel_Type = Integer32
_SfcsCTMQueueStatsQueuePeakLevel_Object = MibTableColumn
sfcsCTMQueueStatsQueuePeakLevel = _SfcsCTMQueueStatsQueuePeakLevel_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 4, 1, 1, 5),
    _SfcsCTMQueueStatsQueuePeakLevel_Type()
)
sfcsCTMQueueStatsQueuePeakLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMQueueStatsQueuePeakLevel.setStatus("mandatory")
_SfcsCTMQueueStatsTxCellCnt_Type = OctetString
_SfcsCTMQueueStatsTxCellCnt_Object = MibTableColumn
sfcsCTMQueueStatsTxCellCnt = _SfcsCTMQueueStatsTxCellCnt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 9, 4, 1, 1, 6),
    _SfcsCTMQueueStatsTxCellCnt_Type()
)
sfcsCTMQueueStatsTxCellCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsCTMQueueStatsTxCellCnt.setStatus("mandatory")
_SfcsBWMgr_ObjectIdentity = ObjectIdentity
sfcsBWMgr = _SfcsBWMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12)
)
_SfcsBwNims_ObjectIdentity = ObjectIdentity
sfcsBwNims = _SfcsBwNims_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 1)
)
_SfcsBwNimsTable_Object = MibTable
sfcsBwNimsTable = _SfcsBwNimsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    sfcsBwNimsTable.setStatus("mandatory")
_SfcsBwNimsEntry_Object = MibTableRow
sfcsBwNimsEntry = _SfcsBwNimsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 1, 1, 1)
)
sfcsBwNimsEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsBwNimsIndex"),
)
if mibBuilder.loadTexts:
    sfcsBwNimsEntry.setStatus("mandatory")
_SfcsBwNimsIndex_Type = Integer32
_SfcsBwNimsIndex_Object = MibTableColumn
sfcsBwNimsIndex = _SfcsBwNimsIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 1, 1, 1, 1),
    _SfcsBwNimsIndex_Type()
)
sfcsBwNimsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwNimsIndex.setStatus("mandatory")
_SfcsBwNimsAdminStatus_Type = Integer32
_SfcsBwNimsAdminStatus_Object = MibTableColumn
sfcsBwNimsAdminStatus = _SfcsBwNimsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 1, 1, 1, 2),
    _SfcsBwNimsAdminStatus_Type()
)
sfcsBwNimsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwNimsAdminStatus.setStatus("mandatory")
_SfcsBWNimsBuffCount_Type = Integer32
_SfcsBWNimsBuffCount_Object = MibTableColumn
sfcsBWNimsBuffCount = _SfcsBWNimsBuffCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 1, 1, 1, 3),
    _SfcsBWNimsBuffCount_Type()
)
sfcsBWNimsBuffCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBWNimsBuffCount.setStatus("mandatory")
_SfcsBWNimsPortCount_Type = Integer32
_SfcsBWNimsPortCount_Object = MibTableColumn
sfcsBWNimsPortCount = _SfcsBWNimsPortCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 1, 1, 1, 4),
    _SfcsBWNimsPortCount_Type()
)
sfcsBWNimsPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBWNimsPortCount.setStatus("mandatory")
_SfcsBWNimsPrioCount_Type = Integer32
_SfcsBWNimsPrioCount_Object = MibTableColumn
sfcsBWNimsPrioCount = _SfcsBWNimsPrioCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 1, 1, 1, 5),
    _SfcsBWNimsPrioCount_Type()
)
sfcsBWNimsPrioCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBWNimsPrioCount.setStatus("mandatory")
_SfcsBwPorts_ObjectIdentity = ObjectIdentity
sfcsBwPorts = _SfcsBwPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 2)
)
_SfcsBwPortsTable_Object = MibTable
sfcsBwPortsTable = _SfcsBwPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 2, 1)
)
if mibBuilder.loadTexts:
    sfcsBwPortsTable.setStatus("mandatory")
_SfcsBwPortsEntry_Object = MibTableRow
sfcsBwPortsEntry = _SfcsBwPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 2, 1, 1)
)
sfcsBwPortsEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsBwPortsIndex"),
)
if mibBuilder.loadTexts:
    sfcsBwPortsEntry.setStatus("mandatory")
_SfcsBwPortsIndex_Type = Integer32
_SfcsBwPortsIndex_Object = MibTableColumn
sfcsBwPortsIndex = _SfcsBwPortsIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 2, 1, 1, 1),
    _SfcsBwPortsIndex_Type()
)
sfcsBwPortsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortsIndex.setStatus("mandatory")
_SfcsBwPortsAdminStatus_Type = Integer32
_SfcsBwPortsAdminStatus_Object = MibTableColumn
sfcsBwPortsAdminStatus = _SfcsBwPortsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 2, 1, 1, 2),
    _SfcsBwPortsAdminStatus_Type()
)
sfcsBwPortsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortsAdminStatus.setStatus("mandatory")
_SfcsBwPortsPhysBwFwd_Type = Integer32
_SfcsBwPortsPhysBwFwd_Object = MibTableColumn
sfcsBwPortsPhysBwFwd = _SfcsBwPortsPhysBwFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 2, 1, 1, 3),
    _SfcsBwPortsPhysBwFwd_Type()
)
sfcsBwPortsPhysBwFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortsPhysBwFwd.setStatus("mandatory")
_SfcsBwPortsPhysBwRev_Type = Integer32
_SfcsBwPortsPhysBwRev_Object = MibTableColumn
sfcsBwPortsPhysBwRev = _SfcsBwPortsPhysBwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 2, 1, 1, 4),
    _SfcsBwPortsPhysBwRev_Type()
)
sfcsBwPortsPhysBwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortsPhysBwRev.setStatus("mandatory")
_SfcsBwPortsZone_Type = Integer32
_SfcsBwPortsZone_Object = MibTableColumn
sfcsBwPortsZone = _SfcsBwPortsZone_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 2, 1, 1, 5),
    _SfcsBwPortsZone_Type()
)
sfcsBwPortsZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortsZone.setStatus("mandatory")
_SfcsBwPortsMetric_Type = Integer32
_SfcsBwPortsMetric_Object = MibTableColumn
sfcsBwPortsMetric = _SfcsBwPortsMetric_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 2, 1, 1, 6),
    _SfcsBwPortsMetric_Type()
)
sfcsBwPortsMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortsMetric.setStatus("mandatory")
_SfcsBwPortPools_ObjectIdentity = ObjectIdentity
sfcsBwPortPools = _SfcsBwPortPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3)
)
_SfcsBwPortPoolLimitsTable_Object = MibTable
sfcsBwPortPoolLimitsTable = _SfcsBwPortPoolLimitsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1)
)
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsTable.setStatus("mandatory")
_SfcsBwPortPoolLimitsEntry_Object = MibTableRow
sfcsBwPortPoolLimitsEntry = _SfcsBwPortPoolLimitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1)
)
sfcsBwPortPoolLimitsEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsBwPortPoolLimitsIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsBwPortPoolLimitsPoolIndex"),
)
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsEntry.setStatus("mandatory")
_SfcsBwPortPoolLimitsIndex_Type = Integer32
_SfcsBwPortPoolLimitsIndex_Object = MibTableColumn
sfcsBwPortPoolLimitsIndex = _SfcsBwPortPoolLimitsIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 1),
    _SfcsBwPortPoolLimitsIndex_Type()
)
sfcsBwPortPoolLimitsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsIndex.setStatus("mandatory")
_SfcsBwPortPoolLimitsPoolIndex_Type = Integer32
_SfcsBwPortPoolLimitsPoolIndex_Object = MibTableColumn
sfcsBwPortPoolLimitsPoolIndex = _SfcsBwPortPoolLimitsPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 2),
    _SfcsBwPortPoolLimitsPoolIndex_Type()
)
sfcsBwPortPoolLimitsPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsPoolIndex.setStatus("mandatory")
_SfcsBwPortPoolLimitsMaxAllocBwFwd_Type = Integer32
_SfcsBwPortPoolLimitsMaxAllocBwFwd_Object = MibTableColumn
sfcsBwPortPoolLimitsMaxAllocBwFwd = _SfcsBwPortPoolLimitsMaxAllocBwFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 3),
    _SfcsBwPortPoolLimitsMaxAllocBwFwd_Type()
)
sfcsBwPortPoolLimitsMaxAllocBwFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsMaxAllocBwFwd.setStatus("mandatory")
_SfcsBwPortPoolLimitsMaxAllocBwRev_Type = Integer32
_SfcsBwPortPoolLimitsMaxAllocBwRev_Object = MibTableColumn
sfcsBwPortPoolLimitsMaxAllocBwRev = _SfcsBwPortPoolLimitsMaxAllocBwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 4),
    _SfcsBwPortPoolLimitsMaxAllocBwRev_Type()
)
sfcsBwPortPoolLimitsMaxAllocBwRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsMaxAllocBwRev.setStatus("mandatory")
_SfcsBwPortPoolLimitsBwAllocStrat_Type = Integer32
_SfcsBwPortPoolLimitsBwAllocStrat_Object = MibTableColumn
sfcsBwPortPoolLimitsBwAllocStrat = _SfcsBwPortPoolLimitsBwAllocStrat_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 5),
    _SfcsBwPortPoolLimitsBwAllocStrat_Type()
)
sfcsBwPortPoolLimitsBwAllocStrat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsBwAllocStrat.setStatus("mandatory")
_SfcsBwPortPoolLimitsBwConstant_Type = Integer32
_SfcsBwPortPoolLimitsBwConstant_Object = MibTableColumn
sfcsBwPortPoolLimitsBwConstant = _SfcsBwPortPoolLimitsBwConstant_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 6),
    _SfcsBwPortPoolLimitsBwConstant_Type()
)
sfcsBwPortPoolLimitsBwConstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsBwConstant.setStatus("mandatory")
_SfcsBwPortPoolLimitsCBRLimitFwd_Type = Integer32
_SfcsBwPortPoolLimitsCBRLimitFwd_Object = MibTableColumn
sfcsBwPortPoolLimitsCBRLimitFwd = _SfcsBwPortPoolLimitsCBRLimitFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 7),
    _SfcsBwPortPoolLimitsCBRLimitFwd_Type()
)
sfcsBwPortPoolLimitsCBRLimitFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsCBRLimitFwd.setStatus("mandatory")
_SfcsBwPortPoolLimitsCBRLimitRev_Type = Integer32
_SfcsBwPortPoolLimitsCBRLimitRev_Object = MibTableColumn
sfcsBwPortPoolLimitsCBRLimitRev = _SfcsBwPortPoolLimitsCBRLimitRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 8),
    _SfcsBwPortPoolLimitsCBRLimitRev_Type()
)
sfcsBwPortPoolLimitsCBRLimitRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsCBRLimitRev.setStatus("mandatory")
_SfcsBwPortPoolLimitsABRLimitFwd_Type = Integer32
_SfcsBwPortPoolLimitsABRLimitFwd_Object = MibTableColumn
sfcsBwPortPoolLimitsABRLimitFwd = _SfcsBwPortPoolLimitsABRLimitFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 9),
    _SfcsBwPortPoolLimitsABRLimitFwd_Type()
)
sfcsBwPortPoolLimitsABRLimitFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsABRLimitFwd.setStatus("mandatory")
_SfcsBwPortPoolLimitsABRLimitRev_Type = Integer32
_SfcsBwPortPoolLimitsABRLimitRev_Object = MibTableColumn
sfcsBwPortPoolLimitsABRLimitRev = _SfcsBwPortPoolLimitsABRLimitRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 10),
    _SfcsBwPortPoolLimitsABRLimitRev_Type()
)
sfcsBwPortPoolLimitsABRLimitRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsABRLimitRev.setStatus("mandatory")
_SfcsBwPortPoolLimitsVBRLimitFwd_Type = Integer32
_SfcsBwPortPoolLimitsVBRLimitFwd_Object = MibTableColumn
sfcsBwPortPoolLimitsVBRLimitFwd = _SfcsBwPortPoolLimitsVBRLimitFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 11),
    _SfcsBwPortPoolLimitsVBRLimitFwd_Type()
)
sfcsBwPortPoolLimitsVBRLimitFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsVBRLimitFwd.setStatus("mandatory")
_SfcsBwPortPoolLimitsVBRLimitRev_Type = Integer32
_SfcsBwPortPoolLimitsVBRLimitRev_Object = MibTableColumn
sfcsBwPortPoolLimitsVBRLimitRev = _SfcsBwPortPoolLimitsVBRLimitRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 12),
    _SfcsBwPortPoolLimitsVBRLimitRev_Type()
)
sfcsBwPortPoolLimitsVBRLimitRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsVBRLimitRev.setStatus("mandatory")
_SfcsBwPortPoolLimitsUBRLimitFwd_Type = Integer32
_SfcsBwPortPoolLimitsUBRLimitFwd_Object = MibTableColumn
sfcsBwPortPoolLimitsUBRLimitFwd = _SfcsBwPortPoolLimitsUBRLimitFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 13),
    _SfcsBwPortPoolLimitsUBRLimitFwd_Type()
)
sfcsBwPortPoolLimitsUBRLimitFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsUBRLimitFwd.setStatus("mandatory")
_SfcsBwPortPoolLimitsUBRLimitRev_Type = Integer32
_SfcsBwPortPoolLimitsUBRLimitRev_Object = MibTableColumn
sfcsBwPortPoolLimitsUBRLimitRev = _SfcsBwPortPoolLimitsUBRLimitRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 14),
    _SfcsBwPortPoolLimitsUBRLimitRev_Type()
)
sfcsBwPortPoolLimitsUBRLimitRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsUBRLimitRev.setStatus("mandatory")
_SfcsBwPortPoolLimitsUBRConnLimitFwd_Type = Integer32
_SfcsBwPortPoolLimitsUBRConnLimitFwd_Object = MibTableColumn
sfcsBwPortPoolLimitsUBRConnLimitFwd = _SfcsBwPortPoolLimitsUBRConnLimitFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 15),
    _SfcsBwPortPoolLimitsUBRConnLimitFwd_Type()
)
sfcsBwPortPoolLimitsUBRConnLimitFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsUBRConnLimitFwd.setStatus("mandatory")
_SfcsBwPortPoolLimitsUBRConnLimitRev_Type = Integer32
_SfcsBwPortPoolLimitsUBRConnLimitRev_Object = MibTableColumn
sfcsBwPortPoolLimitsUBRConnLimitRev = _SfcsBwPortPoolLimitsUBRConnLimitRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 1, 1, 16),
    _SfcsBwPortPoolLimitsUBRConnLimitRev_Type()
)
sfcsBwPortPoolLimitsUBRConnLimitRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolLimitsUBRConnLimitRev.setStatus("mandatory")
_SfcsBwPortPoolStatTable_Object = MibTable
sfcsBwPortPoolStatTable = _SfcsBwPortPoolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2)
)
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatTable.setStatus("mandatory")
_SfcsBwPortPoolStatEntry_Object = MibTableRow
sfcsBwPortPoolStatEntry = _SfcsBwPortPoolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1)
)
sfcsBwPortPoolStatEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsBwPortPoolStatsIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsBwPortPoolStatsPoolIndex"),
)
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatEntry.setStatus("mandatory")
_SfcsBwPortPoolStatsIndex_Type = Integer32
_SfcsBwPortPoolStatsIndex_Object = MibTableColumn
sfcsBwPortPoolStatsIndex = _SfcsBwPortPoolStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 1),
    _SfcsBwPortPoolStatsIndex_Type()
)
sfcsBwPortPoolStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatsIndex.setStatus("mandatory")
_SfcsBwPortPoolStatsPoolIndex_Type = Integer32
_SfcsBwPortPoolStatsPoolIndex_Object = MibTableColumn
sfcsBwPortPoolStatsPoolIndex = _SfcsBwPortPoolStatsPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 2),
    _SfcsBwPortPoolStatsPoolIndex_Type()
)
sfcsBwPortPoolStatsPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatsPoolIndex.setStatus("mandatory")
_SfcsBwPortPoolStatConnCntFwd_Type = Integer32
_SfcsBwPortPoolStatConnCntFwd_Object = MibTableColumn
sfcsBwPortPoolStatConnCntFwd = _SfcsBwPortPoolStatConnCntFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 3),
    _SfcsBwPortPoolStatConnCntFwd_Type()
)
sfcsBwPortPoolStatConnCntFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatConnCntFwd.setStatus("mandatory")
_SfcsBwPortPoolStatConnCntRev_Type = Integer32
_SfcsBwPortPoolStatConnCntRev_Object = MibTableColumn
sfcsBwPortPoolStatConnCntRev = _SfcsBwPortPoolStatConnCntRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 4),
    _SfcsBwPortPoolStatConnCntRev_Type()
)
sfcsBwPortPoolStatConnCntRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatConnCntRev.setStatus("mandatory")
_SfcsBwPortPoolStatAllocBwFwd_Type = Integer32
_SfcsBwPortPoolStatAllocBwFwd_Object = MibTableColumn
sfcsBwPortPoolStatAllocBwFwd = _SfcsBwPortPoolStatAllocBwFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 5),
    _SfcsBwPortPoolStatAllocBwFwd_Type()
)
sfcsBwPortPoolStatAllocBwFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatAllocBwFwd.setStatus("mandatory")
_SfcsBwPortPoolStatAllocBwRev_Type = Integer32
_SfcsBwPortPoolStatAllocBwRev_Object = MibTableColumn
sfcsBwPortPoolStatAllocBwRev = _SfcsBwPortPoolStatAllocBwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 6),
    _SfcsBwPortPoolStatAllocBwRev_Type()
)
sfcsBwPortPoolStatAllocBwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatAllocBwRev.setStatus("mandatory")
_SfcsBwPortPoolStatAvailBwFwd_Type = Integer32
_SfcsBwPortPoolStatAvailBwFwd_Object = MibTableColumn
sfcsBwPortPoolStatAvailBwFwd = _SfcsBwPortPoolStatAvailBwFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 7),
    _SfcsBwPortPoolStatAvailBwFwd_Type()
)
sfcsBwPortPoolStatAvailBwFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatAvailBwFwd.setStatus("mandatory")
_SfcsBwPortPoolStatAvailBwRev_Type = Integer32
_SfcsBwPortPoolStatAvailBwRev_Object = MibTableColumn
sfcsBwPortPoolStatAvailBwRev = _SfcsBwPortPoolStatAvailBwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 8),
    _SfcsBwPortPoolStatAvailBwRev_Type()
)
sfcsBwPortPoolStatAvailBwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatAvailBwRev.setStatus("mandatory")
_SfcsBwPortPoolStatPeakBwFwd_Type = Integer32
_SfcsBwPortPoolStatPeakBwFwd_Object = MibTableColumn
sfcsBwPortPoolStatPeakBwFwd = _SfcsBwPortPoolStatPeakBwFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 9),
    _SfcsBwPortPoolStatPeakBwFwd_Type()
)
sfcsBwPortPoolStatPeakBwFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatPeakBwFwd.setStatus("mandatory")
_SfcsBwPortPoolStatPeakBwRev_Type = Integer32
_SfcsBwPortPoolStatPeakBwRev_Object = MibTableColumn
sfcsBwPortPoolStatPeakBwRev = _SfcsBwPortPoolStatPeakBwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 10),
    _SfcsBwPortPoolStatPeakBwRev_Type()
)
sfcsBwPortPoolStatPeakBwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatPeakBwRev.setStatus("mandatory")
_SfcsBwPortPoolStatRejConnFwd_Type = Integer32
_SfcsBwPortPoolStatRejConnFwd_Object = MibTableColumn
sfcsBwPortPoolStatRejConnFwd = _SfcsBwPortPoolStatRejConnFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 11),
    _SfcsBwPortPoolStatRejConnFwd_Type()
)
sfcsBwPortPoolStatRejConnFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatRejConnFwd.setStatus("mandatory")
_SfcsBwPortPoolStatRejConnRev_Type = Integer32
_SfcsBwPortPoolStatRejConnRev_Object = MibTableColumn
sfcsBwPortPoolStatRejConnRev = _SfcsBwPortPoolStatRejConnRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 12),
    _SfcsBwPortPoolStatRejConnRev_Type()
)
sfcsBwPortPoolStatRejConnRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatRejConnRev.setStatus("mandatory")
_SfcsBwPortPoolStatPrevAdverMAXCRFwd_Type = Integer32
_SfcsBwPortPoolStatPrevAdverMAXCRFwd_Object = MibTableColumn
sfcsBwPortPoolStatPrevAdverMAXCRFwd = _SfcsBwPortPoolStatPrevAdverMAXCRFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 13),
    _SfcsBwPortPoolStatPrevAdverMAXCRFwd_Type()
)
sfcsBwPortPoolStatPrevAdverMAXCRFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatPrevAdverMAXCRFwd.setStatus("mandatory")
_SfcsBwPortPoolStatPrevAdverMAXCRRev_Type = Integer32
_SfcsBwPortPoolStatPrevAdverMAXCRRev_Object = MibTableColumn
sfcsBwPortPoolStatPrevAdverMAXCRRev = _SfcsBwPortPoolStatPrevAdverMAXCRRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 14),
    _SfcsBwPortPoolStatPrevAdverMAXCRRev_Type()
)
sfcsBwPortPoolStatPrevAdverMAXCRRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatPrevAdverMAXCRRev.setStatus("mandatory")
_SfcsBwPortPoolStatPrevAdverAvailCRFwd_Type = Integer32
_SfcsBwPortPoolStatPrevAdverAvailCRFwd_Object = MibTableColumn
sfcsBwPortPoolStatPrevAdverAvailCRFwd = _SfcsBwPortPoolStatPrevAdverAvailCRFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 15),
    _SfcsBwPortPoolStatPrevAdverAvailCRFwd_Type()
)
sfcsBwPortPoolStatPrevAdverAvailCRFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatPrevAdverAvailCRFwd.setStatus("mandatory")
_SfcsBwPortPoolStatPrevAdverAvailCRRev_Type = Integer32
_SfcsBwPortPoolStatPrevAdverAvailCRRev_Object = MibTableColumn
sfcsBwPortPoolStatPrevAdverAvailCRRev = _SfcsBwPortPoolStatPrevAdverAvailCRRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 16),
    _SfcsBwPortPoolStatPrevAdverAvailCRRev_Type()
)
sfcsBwPortPoolStatPrevAdverAvailCRRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatPrevAdverAvailCRRev.setStatus("mandatory")
_SfcsBwPortPoolStatCBRConnCntFwd_Type = Integer32
_SfcsBwPortPoolStatCBRConnCntFwd_Object = MibTableColumn
sfcsBwPortPoolStatCBRConnCntFwd = _SfcsBwPortPoolStatCBRConnCntFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 17),
    _SfcsBwPortPoolStatCBRConnCntFwd_Type()
)
sfcsBwPortPoolStatCBRConnCntFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatCBRConnCntFwd.setStatus("mandatory")
_SfcsBwPortPoolStatCBRConnCntRev_Type = Integer32
_SfcsBwPortPoolStatCBRConnCntRev_Object = MibTableColumn
sfcsBwPortPoolStatCBRConnCntRev = _SfcsBwPortPoolStatCBRConnCntRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 18),
    _SfcsBwPortPoolStatCBRConnCntRev_Type()
)
sfcsBwPortPoolStatCBRConnCntRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatCBRConnCntRev.setStatus("mandatory")
_SfcsBwPortPoolStatCBRConnRejFwd_Type = Integer32
_SfcsBwPortPoolStatCBRConnRejFwd_Object = MibTableColumn
sfcsBwPortPoolStatCBRConnRejFwd = _SfcsBwPortPoolStatCBRConnRejFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 19),
    _SfcsBwPortPoolStatCBRConnRejFwd_Type()
)
sfcsBwPortPoolStatCBRConnRejFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatCBRConnRejFwd.setStatus("mandatory")
_SfcsBwPortPoolStatCBRConnRejRev_Type = Integer32
_SfcsBwPortPoolStatCBRConnRejRev_Object = MibTableColumn
sfcsBwPortPoolStatCBRConnRejRev = _SfcsBwPortPoolStatCBRConnRejRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 20),
    _SfcsBwPortPoolStatCBRConnRejRev_Type()
)
sfcsBwPortPoolStatCBRConnRejRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatCBRConnRejRev.setStatus("mandatory")
_SfcsBwPortPoolStatCBRAllocBwFwd_Type = Integer32
_SfcsBwPortPoolStatCBRAllocBwFwd_Object = MibTableColumn
sfcsBwPortPoolStatCBRAllocBwFwd = _SfcsBwPortPoolStatCBRAllocBwFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 21),
    _SfcsBwPortPoolStatCBRAllocBwFwd_Type()
)
sfcsBwPortPoolStatCBRAllocBwFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatCBRAllocBwFwd.setStatus("mandatory")
_SfcsBwPortPoolStatCBRAllocBwRev_Type = Integer32
_SfcsBwPortPoolStatCBRAllocBwRev_Object = MibTableColumn
sfcsBwPortPoolStatCBRAllocBwRev = _SfcsBwPortPoolStatCBRAllocBwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 22),
    _SfcsBwPortPoolStatCBRAllocBwRev_Type()
)
sfcsBwPortPoolStatCBRAllocBwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatCBRAllocBwRev.setStatus("mandatory")
_SfcsBwPortPoolStatCBRAggPCRFwd_Type = Integer32
_SfcsBwPortPoolStatCBRAggPCRFwd_Object = MibTableColumn
sfcsBwPortPoolStatCBRAggPCRFwd = _SfcsBwPortPoolStatCBRAggPCRFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 23),
    _SfcsBwPortPoolStatCBRAggPCRFwd_Type()
)
sfcsBwPortPoolStatCBRAggPCRFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatCBRAggPCRFwd.setStatus("mandatory")
_SfcsBwPortPoolStatCBRAggPCRRev_Type = Integer32
_SfcsBwPortPoolStatCBRAggPCRRev_Object = MibTableColumn
sfcsBwPortPoolStatCBRAggPCRRev = _SfcsBwPortPoolStatCBRAggPCRRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 24),
    _SfcsBwPortPoolStatCBRAggPCRRev_Type()
)
sfcsBwPortPoolStatCBRAggPCRRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatCBRAggPCRRev.setStatus("mandatory")
_SfcsBwPortPoolStatCBRPrevAdverMAXCTD_Type = Integer32
_SfcsBwPortPoolStatCBRPrevAdverMAXCTD_Object = MibTableColumn
sfcsBwPortPoolStatCBRPrevAdverMAXCTD = _SfcsBwPortPoolStatCBRPrevAdverMAXCTD_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 25),
    _SfcsBwPortPoolStatCBRPrevAdverMAXCTD_Type()
)
sfcsBwPortPoolStatCBRPrevAdverMAXCTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatCBRPrevAdverMAXCTD.setStatus("mandatory")
_SfcsBwPortPoolStatCBRPrevAdverCDV_Type = Integer32
_SfcsBwPortPoolStatCBRPrevAdverCDV_Object = MibTableColumn
sfcsBwPortPoolStatCBRPrevAdverCDV = _SfcsBwPortPoolStatCBRPrevAdverCDV_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 26),
    _SfcsBwPortPoolStatCBRPrevAdverCDV_Type()
)
sfcsBwPortPoolStatCBRPrevAdverCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatCBRPrevAdverCDV.setStatus("mandatory")
_SfcsBwPortPoolStatABRConnCntFwd_Type = Integer32
_SfcsBwPortPoolStatABRConnCntFwd_Object = MibTableColumn
sfcsBwPortPoolStatABRConnCntFwd = _SfcsBwPortPoolStatABRConnCntFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 27),
    _SfcsBwPortPoolStatABRConnCntFwd_Type()
)
sfcsBwPortPoolStatABRConnCntFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatABRConnCntFwd.setStatus("mandatory")
_SfcsBwPortPoolStatABRConnCntRev_Type = Integer32
_SfcsBwPortPoolStatABRConnCntRev_Object = MibTableColumn
sfcsBwPortPoolStatABRConnCntRev = _SfcsBwPortPoolStatABRConnCntRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 28),
    _SfcsBwPortPoolStatABRConnCntRev_Type()
)
sfcsBwPortPoolStatABRConnCntRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatABRConnCntRev.setStatus("mandatory")
_SfcsBwPortPoolStatABRConnRejFwd_Type = Integer32
_SfcsBwPortPoolStatABRConnRejFwd_Object = MibTableColumn
sfcsBwPortPoolStatABRConnRejFwd = _SfcsBwPortPoolStatABRConnRejFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 29),
    _SfcsBwPortPoolStatABRConnRejFwd_Type()
)
sfcsBwPortPoolStatABRConnRejFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatABRConnRejFwd.setStatus("mandatory")
_SfcsBwPortPoolStatABRConnRejRev_Type = Integer32
_SfcsBwPortPoolStatABRConnRejRev_Object = MibTableColumn
sfcsBwPortPoolStatABRConnRejRev = _SfcsBwPortPoolStatABRConnRejRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 30),
    _SfcsBwPortPoolStatABRConnRejRev_Type()
)
sfcsBwPortPoolStatABRConnRejRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatABRConnRejRev.setStatus("mandatory")
_SfcsBwPortPoolStatABRAllocBwFwd_Type = Integer32
_SfcsBwPortPoolStatABRAllocBwFwd_Object = MibTableColumn
sfcsBwPortPoolStatABRAllocBwFwd = _SfcsBwPortPoolStatABRAllocBwFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 31),
    _SfcsBwPortPoolStatABRAllocBwFwd_Type()
)
sfcsBwPortPoolStatABRAllocBwFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatABRAllocBwFwd.setStatus("mandatory")
_SfcsBwPortPoolStatABRAllocBwRev_Type = Integer32
_SfcsBwPortPoolStatABRAllocBwRev_Object = MibTableColumn
sfcsBwPortPoolStatABRAllocBwRev = _SfcsBwPortPoolStatABRAllocBwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 32),
    _SfcsBwPortPoolStatABRAllocBwRev_Type()
)
sfcsBwPortPoolStatABRAllocBwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatABRAllocBwRev.setStatus("mandatory")
_SfcsBwPortPoolStatABRAggPCRFwd_Type = Integer32
_SfcsBwPortPoolStatABRAggPCRFwd_Object = MibTableColumn
sfcsBwPortPoolStatABRAggPCRFwd = _SfcsBwPortPoolStatABRAggPCRFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 33),
    _SfcsBwPortPoolStatABRAggPCRFwd_Type()
)
sfcsBwPortPoolStatABRAggPCRFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatABRAggPCRFwd.setStatus("mandatory")
_SfcsBwPortPoolStatABRAggPCRRev_Type = Integer32
_SfcsBwPortPoolStatABRAggPCRRev_Object = MibTableColumn
sfcsBwPortPoolStatABRAggPCRRev = _SfcsBwPortPoolStatABRAggPCRRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 34),
    _SfcsBwPortPoolStatABRAggPCRRev_Type()
)
sfcsBwPortPoolStatABRAggPCRRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatABRAggPCRRev.setStatus("mandatory")
_SfcsBwPortPoolStatABRPrevAdverMAXCTD_Type = Integer32
_SfcsBwPortPoolStatABRPrevAdverMAXCTD_Object = MibTableColumn
sfcsBwPortPoolStatABRPrevAdverMAXCTD = _SfcsBwPortPoolStatABRPrevAdverMAXCTD_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 35),
    _SfcsBwPortPoolStatABRPrevAdverMAXCTD_Type()
)
sfcsBwPortPoolStatABRPrevAdverMAXCTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatABRPrevAdverMAXCTD.setStatus("mandatory")
_SfcsBwPortPoolStatABRPrevAdverCDV_Type = Integer32
_SfcsBwPortPoolStatABRPrevAdverCDV_Object = MibTableColumn
sfcsBwPortPoolStatABRPrevAdverCDV = _SfcsBwPortPoolStatABRPrevAdverCDV_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 36),
    _SfcsBwPortPoolStatABRPrevAdverCDV_Type()
)
sfcsBwPortPoolStatABRPrevAdverCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatABRPrevAdverCDV.setStatus("mandatory")
_SfcsBwPortPoolStatVBRConnCntFwd_Type = Integer32
_SfcsBwPortPoolStatVBRConnCntFwd_Object = MibTableColumn
sfcsBwPortPoolStatVBRConnCntFwd = _SfcsBwPortPoolStatVBRConnCntFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 37),
    _SfcsBwPortPoolStatVBRConnCntFwd_Type()
)
sfcsBwPortPoolStatVBRConnCntFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatVBRConnCntFwd.setStatus("mandatory")
_SfcsBwPortPoolStatVBRConnCntRev_Type = Integer32
_SfcsBwPortPoolStatVBRConnCntRev_Object = MibTableColumn
sfcsBwPortPoolStatVBRConnCntRev = _SfcsBwPortPoolStatVBRConnCntRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 38),
    _SfcsBwPortPoolStatVBRConnCntRev_Type()
)
sfcsBwPortPoolStatVBRConnCntRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatVBRConnCntRev.setStatus("mandatory")
_SfcsBwPortPoolStatVBRConnRejFwd_Type = Integer32
_SfcsBwPortPoolStatVBRConnRejFwd_Object = MibTableColumn
sfcsBwPortPoolStatVBRConnRejFwd = _SfcsBwPortPoolStatVBRConnRejFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 39),
    _SfcsBwPortPoolStatVBRConnRejFwd_Type()
)
sfcsBwPortPoolStatVBRConnRejFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatVBRConnRejFwd.setStatus("mandatory")
_SfcsBwPortPoolStatVBRConnRejRev_Type = Integer32
_SfcsBwPortPoolStatVBRConnRejRev_Object = MibTableColumn
sfcsBwPortPoolStatVBRConnRejRev = _SfcsBwPortPoolStatVBRConnRejRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 40),
    _SfcsBwPortPoolStatVBRConnRejRev_Type()
)
sfcsBwPortPoolStatVBRConnRejRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatVBRConnRejRev.setStatus("mandatory")
_SfcsBwPortPoolStatVBRAllocBwFwd_Type = Integer32
_SfcsBwPortPoolStatVBRAllocBwFwd_Object = MibTableColumn
sfcsBwPortPoolStatVBRAllocBwFwd = _SfcsBwPortPoolStatVBRAllocBwFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 41),
    _SfcsBwPortPoolStatVBRAllocBwFwd_Type()
)
sfcsBwPortPoolStatVBRAllocBwFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatVBRAllocBwFwd.setStatus("mandatory")
_SfcsBwPortPoolStatVBRAllocBwRev_Type = Integer32
_SfcsBwPortPoolStatVBRAllocBwRev_Object = MibTableColumn
sfcsBwPortPoolStatVBRAllocBwRev = _SfcsBwPortPoolStatVBRAllocBwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 42),
    _SfcsBwPortPoolStatVBRAllocBwRev_Type()
)
sfcsBwPortPoolStatVBRAllocBwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatVBRAllocBwRev.setStatus("mandatory")
_SfcsBwPortPoolStatVBRAggPCRFwd_Type = Integer32
_SfcsBwPortPoolStatVBRAggPCRFwd_Object = MibTableColumn
sfcsBwPortPoolStatVBRAggPCRFwd = _SfcsBwPortPoolStatVBRAggPCRFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 43),
    _SfcsBwPortPoolStatVBRAggPCRFwd_Type()
)
sfcsBwPortPoolStatVBRAggPCRFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatVBRAggPCRFwd.setStatus("mandatory")
_SfcsBwPortPoolStatVBRAggPCRRev_Type = Integer32
_SfcsBwPortPoolStatVBRAggPCRRev_Object = MibTableColumn
sfcsBwPortPoolStatVBRAggPCRRev = _SfcsBwPortPoolStatVBRAggPCRRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 44),
    _SfcsBwPortPoolStatVBRAggPCRRev_Type()
)
sfcsBwPortPoolStatVBRAggPCRRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatVBRAggPCRRev.setStatus("mandatory")
_SfcsBwPortPoolStatVBRPrevAdverMAXCTD_Type = Integer32
_SfcsBwPortPoolStatVBRPrevAdverMAXCTD_Object = MibTableColumn
sfcsBwPortPoolStatVBRPrevAdverMAXCTD = _SfcsBwPortPoolStatVBRPrevAdverMAXCTD_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 45),
    _SfcsBwPortPoolStatVBRPrevAdverMAXCTD_Type()
)
sfcsBwPortPoolStatVBRPrevAdverMAXCTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatVBRPrevAdverMAXCTD.setStatus("mandatory")
_SfcsBwPortPoolStatVBRPrevAdverCDV_Type = Integer32
_SfcsBwPortPoolStatVBRPrevAdverCDV_Object = MibTableColumn
sfcsBwPortPoolStatVBRPrevAdverCDV = _SfcsBwPortPoolStatVBRPrevAdverCDV_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 46),
    _SfcsBwPortPoolStatVBRPrevAdverCDV_Type()
)
sfcsBwPortPoolStatVBRPrevAdverCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatVBRPrevAdverCDV.setStatus("mandatory")
_SfcsBwPortPoolStatUBRConnCntFwd_Type = Integer32
_SfcsBwPortPoolStatUBRConnCntFwd_Object = MibTableColumn
sfcsBwPortPoolStatUBRConnCntFwd = _SfcsBwPortPoolStatUBRConnCntFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 47),
    _SfcsBwPortPoolStatUBRConnCntFwd_Type()
)
sfcsBwPortPoolStatUBRConnCntFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatUBRConnCntFwd.setStatus("mandatory")
_SfcsBwPortPoolStatUBRConnCntRev_Type = Integer32
_SfcsBwPortPoolStatUBRConnCntRev_Object = MibTableColumn
sfcsBwPortPoolStatUBRConnCntRev = _SfcsBwPortPoolStatUBRConnCntRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 48),
    _SfcsBwPortPoolStatUBRConnCntRev_Type()
)
sfcsBwPortPoolStatUBRConnCntRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatUBRConnCntRev.setStatus("mandatory")
_SfcsBwPortPoolStatUBRConnRejFwd_Type = Integer32
_SfcsBwPortPoolStatUBRConnRejFwd_Object = MibTableColumn
sfcsBwPortPoolStatUBRConnRejFwd = _SfcsBwPortPoolStatUBRConnRejFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 49),
    _SfcsBwPortPoolStatUBRConnRejFwd_Type()
)
sfcsBwPortPoolStatUBRConnRejFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatUBRConnRejFwd.setStatus("mandatory")
_SfcsBwPortPoolStatUBRConnRejRev_Type = Integer32
_SfcsBwPortPoolStatUBRConnRejRev_Object = MibTableColumn
sfcsBwPortPoolStatUBRConnRejRev = _SfcsBwPortPoolStatUBRConnRejRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 50),
    _SfcsBwPortPoolStatUBRConnRejRev_Type()
)
sfcsBwPortPoolStatUBRConnRejRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatUBRConnRejRev.setStatus("mandatory")
_SfcsBwPortPoolStatUBRAllocBwFwd_Type = Integer32
_SfcsBwPortPoolStatUBRAllocBwFwd_Object = MibTableColumn
sfcsBwPortPoolStatUBRAllocBwFwd = _SfcsBwPortPoolStatUBRAllocBwFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 51),
    _SfcsBwPortPoolStatUBRAllocBwFwd_Type()
)
sfcsBwPortPoolStatUBRAllocBwFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatUBRAllocBwFwd.setStatus("mandatory")
_SfcsBwPortPoolStatUBRAllocBwRev_Type = Integer32
_SfcsBwPortPoolStatUBRAllocBwRev_Object = MibTableColumn
sfcsBwPortPoolStatUBRAllocBwRev = _SfcsBwPortPoolStatUBRAllocBwRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 52),
    _SfcsBwPortPoolStatUBRAllocBwRev_Type()
)
sfcsBwPortPoolStatUBRAllocBwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatUBRAllocBwRev.setStatus("mandatory")
_SfcsBwPortPoolStatUBRAggPCRFwd_Type = Integer32
_SfcsBwPortPoolStatUBRAggPCRFwd_Object = MibTableColumn
sfcsBwPortPoolStatUBRAggPCRFwd = _SfcsBwPortPoolStatUBRAggPCRFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 53),
    _SfcsBwPortPoolStatUBRAggPCRFwd_Type()
)
sfcsBwPortPoolStatUBRAggPCRFwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatUBRAggPCRFwd.setStatus("mandatory")
_SfcsBwPortPoolStatUBRAggPCRRev_Type = Integer32
_SfcsBwPortPoolStatUBRAggPCRRev_Object = MibTableColumn
sfcsBwPortPoolStatUBRAggPCRRev = _SfcsBwPortPoolStatUBRAggPCRRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 54),
    _SfcsBwPortPoolStatUBRAggPCRRev_Type()
)
sfcsBwPortPoolStatUBRAggPCRRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatUBRAggPCRRev.setStatus("mandatory")
_SfcsBwPortPoolStatUBRPrevAdverMAXCTD_Type = Integer32
_SfcsBwPortPoolStatUBRPrevAdverMAXCTD_Object = MibTableColumn
sfcsBwPortPoolStatUBRPrevAdverMAXCTD = _SfcsBwPortPoolStatUBRPrevAdverMAXCTD_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 55),
    _SfcsBwPortPoolStatUBRPrevAdverMAXCTD_Type()
)
sfcsBwPortPoolStatUBRPrevAdverMAXCTD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatUBRPrevAdverMAXCTD.setStatus("mandatory")
_SfcsBwPortPoolStatUBRPrevAdverCDV_Type = Integer32
_SfcsBwPortPoolStatUBRPrevAdverCDV_Object = MibTableColumn
sfcsBwPortPoolStatUBRPrevAdverCDV = _SfcsBwPortPoolStatUBRPrevAdverCDV_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 2, 1, 56),
    _SfcsBwPortPoolStatUBRPrevAdverCDV_Type()
)
sfcsBwPortPoolStatUBRPrevAdverCDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolStatUBRPrevAdverCDV.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtTable_Object = MibTable
sfcsBwPortPoolTrapMgmtTable = _SfcsBwPortPoolTrapMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3)
)
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtTable.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtEntry_Object = MibTableRow
sfcsBwPortPoolTrapMgmtEntry = _SfcsBwPortPoolTrapMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1)
)
sfcsBwPortPoolTrapMgmtEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsBwPortPoolTrapMgmtIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsBwPortPoolTrapMgmtPoolIndex"),
)
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtEntry.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtIndex_Type = Integer32
_SfcsBwPortPoolTrapMgmtIndex_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtIndex = _SfcsBwPortPoolTrapMgmtIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 1),
    _SfcsBwPortPoolTrapMgmtIndex_Type()
)
sfcsBwPortPoolTrapMgmtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtIndex.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtPoolIndex_Type = Integer32
_SfcsBwPortPoolTrapMgmtPoolIndex_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtPoolIndex = _SfcsBwPortPoolTrapMgmtPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 2),
    _SfcsBwPortPoolTrapMgmtPoolIndex_Type()
)
sfcsBwPortPoolTrapMgmtPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtPoolIndex.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd = _SfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 3),
    _SfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd_Type()
)
sfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtAllocBwTholdHiRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtAllocBwTholdHiRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtAllocBwTholdHiRev = _SfcsBwPortPoolTrapMgmtAllocBwTholdHiRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 4),
    _SfcsBwPortPoolTrapMgmtAllocBwTholdHiRev_Type()
)
sfcsBwPortPoolTrapMgmtAllocBwTholdHiRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtAllocBwTholdHiRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd = _SfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 5),
    _SfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd_Type()
)
sfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtAllocBwTholdLoRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtAllocBwTholdLoRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtAllocBwTholdLoRev = _SfcsBwPortPoolTrapMgmtAllocBwTholdLoRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 6),
    _SfcsBwPortPoolTrapMgmtAllocBwTholdLoRev_Type()
)
sfcsBwPortPoolTrapMgmtAllocBwTholdLoRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtAllocBwTholdLoRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtPeakBwTholdFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtPeakBwTholdFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtPeakBwTholdFwd = _SfcsBwPortPoolTrapMgmtPeakBwTholdFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 7),
    _SfcsBwPortPoolTrapMgmtPeakBwTholdFwd_Type()
)
sfcsBwPortPoolTrapMgmtPeakBwTholdFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtPeakBwTholdFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtPeakBwTholdRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtPeakBwTholdRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtPeakBwTholdRev = _SfcsBwPortPoolTrapMgmtPeakBwTholdRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 8),
    _SfcsBwPortPoolTrapMgmtPeakBwTholdRev_Type()
)
sfcsBwPortPoolTrapMgmtPeakBwTholdRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtPeakBwTholdRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtHoldDownTime_Type = Integer32
_SfcsBwPortPoolTrapMgmtHoldDownTime_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtHoldDownTime = _SfcsBwPortPoolTrapMgmtHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 9),
    _SfcsBwPortPoolTrapMgmtHoldDownTime_Type()
)
sfcsBwPortPoolTrapMgmtHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtHoldDownTime.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd = _SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 10),
    _SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd_Type()
)
sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev = _SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 11),
    _SfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev_Type()
)
sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd = _SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 12),
    _SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd_Type()
)
sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev = _SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 13),
    _SfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev_Type()
)
sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd = _SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 14),
    _SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd_Type()
)
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev = _SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 15),
    _SfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev_Type()
)
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd = _SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 16),
    _SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd_Type()
)
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev = _SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 17),
    _SfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev_Type()
)
sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd = _SfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 18),
    _SfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd_Type()
)
sfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev = _SfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 19),
    _SfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev_Type()
)
sfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd = _SfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 20),
    _SfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd_Type()
)
sfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev = _SfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 21),
    _SfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev_Type()
)
sfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd = _SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 22),
    _SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd_Type()
)
sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev = _SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 23),
    _SfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev_Type()
)
sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd = _SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 24),
    _SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd_Type()
)
sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev = _SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 25),
    _SfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev_Type()
)
sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd = _SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 26),
    _SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd_Type()
)
sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev = _SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 27),
    _SfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev_Type()
)
sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd = _SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 28),
    _SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd_Type()
)
sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev = _SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 29),
    _SfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev_Type()
)
sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd = _SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 30),
    _SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd_Type()
)
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev = _SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 31),
    _SfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev_Type()
)
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd = _SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 32),
    _SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd_Type()
)
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev = _SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 33),
    _SfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev_Type()
)
sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd = _SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 34),
    _SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd_Type()
)
sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev = _SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 35),
    _SfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev_Type()
)
sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd = _SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 36),
    _SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd_Type()
)
sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev = _SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 37),
    _SfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev_Type()
)
sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd = _SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 38),
    _SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd_Type()
)
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev = _SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 39),
    _SfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev_Type()
)
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd_Type = Integer32
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd = _SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 40),
    _SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd_Type()
)
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd.setStatus("mandatory")
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev_Type = Integer32
_SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev_Object = MibTableColumn
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev = _SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 41),
    _SfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev_Type()
)
sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev.setStatus("mandatory")
_SfcsBWPortPoolTrapMgmtBuffUpThold_Type = Integer32
_SfcsBWPortPoolTrapMgmtBuffUpThold_Object = MibTableColumn
sfcsBWPortPoolTrapMgmtBuffUpThold = _SfcsBWPortPoolTrapMgmtBuffUpThold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 42),
    _SfcsBWPortPoolTrapMgmtBuffUpThold_Type()
)
sfcsBWPortPoolTrapMgmtBuffUpThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBWPortPoolTrapMgmtBuffUpThold.setStatus("mandatory")
_SfcsBWPortPoolTrapMgmtBuffLoThold_Type = Integer32
_SfcsBWPortPoolTrapMgmtBuffLoThold_Object = MibTableColumn
sfcsBWPortPoolTrapMgmtBuffLoThold = _SfcsBWPortPoolTrapMgmtBuffLoThold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 43),
    _SfcsBWPortPoolTrapMgmtBuffLoThold_Type()
)
sfcsBWPortPoolTrapMgmtBuffLoThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBWPortPoolTrapMgmtBuffLoThold.setStatus("mandatory")
_SfcsBWPortPoolTrapMgmtConnRejThold_Type = Integer32
_SfcsBWPortPoolTrapMgmtConnRejThold_Object = MibTableColumn
sfcsBWPortPoolTrapMgmtConnRejThold = _SfcsBWPortPoolTrapMgmtConnRejThold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 3, 3, 1, 44),
    _SfcsBWPortPoolTrapMgmtConnRejThold_Type()
)
sfcsBWPortPoolTrapMgmtConnRejThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBWPortPoolTrapMgmtConnRejThold.setStatus("mandatory")
_SfcsBuffPools_ObjectIdentity = ObjectIdentity
sfcsBuffPools = _SfcsBuffPools_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4)
)
_SfcsBuffPrioTable_Object = MibTable
sfcsBuffPrioTable = _SfcsBuffPrioTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1)
)
if mibBuilder.loadTexts:
    sfcsBuffPrioTable.setStatus("mandatory")
_SfcsBuffPrioEntry_Object = MibTableRow
sfcsBuffPrioEntry = _SfcsBuffPrioEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1)
)
sfcsBuffPrioEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsBuffPrioPortIndex"),
    (0, "CTRON-SFCS-MIB", "sfcsBuffPrioPriority"),
)
if mibBuilder.loadTexts:
    sfcsBuffPrioEntry.setStatus("mandatory")
_SfcsBuffPrioPortIndex_Type = Integer32
_SfcsBuffPrioPortIndex_Object = MibTableColumn
sfcsBuffPrioPortIndex = _SfcsBuffPrioPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 1),
    _SfcsBuffPrioPortIndex_Type()
)
sfcsBuffPrioPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBuffPrioPortIndex.setStatus("mandatory")
_SfcsBuffPrioPriority_Type = Integer32
_SfcsBuffPrioPriority_Object = MibTableColumn
sfcsBuffPrioPriority = _SfcsBuffPrioPriority_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 2),
    _SfcsBuffPrioPriority_Type()
)
sfcsBuffPrioPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBuffPrioPriority.setStatus("mandatory")
_SfcsBuffPrioAssignCtl_Type = Integer32
_SfcsBuffPrioAssignCtl_Object = MibTableColumn
sfcsBuffPrioAssignCtl = _SfcsBuffPrioAssignCtl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 3),
    _SfcsBuffPrioAssignCtl_Type()
)
sfcsBuffPrioAssignCtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBuffPrioAssignCtl.setStatus("mandatory")
_SfcsBuffPrioMinCtl_Type = Integer32
_SfcsBuffPrioMinCtl_Object = MibTableColumn
sfcsBuffPrioMinCtl = _SfcsBuffPrioMinCtl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 4),
    _SfcsBuffPrioMinCtl_Type()
)
sfcsBuffPrioMinCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBuffPrioMinCtl.setStatus("mandatory")
_SfcsBuffPrioAssigned_Type = Integer32
_SfcsBuffPrioAssigned_Object = MibTableColumn
sfcsBuffPrioAssigned = _SfcsBuffPrioAssigned_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 5),
    _SfcsBuffPrioAssigned_Type()
)
sfcsBuffPrioAssigned.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBuffPrioAssigned.setStatus("mandatory")
_SfcsBuffPrioAllocated_Type = Integer32
_SfcsBuffPrioAllocated_Object = MibTableColumn
sfcsBuffPrioAllocated = _SfcsBuffPrioAllocated_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 6),
    _SfcsBuffPrioAllocated_Type()
)
sfcsBuffPrioAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBuffPrioAllocated.setStatus("mandatory")
_SfcsBuffPrioAvailable_Type = Integer32
_SfcsBuffPrioAvailable_Object = MibTableColumn
sfcsBuffPrioAvailable = _SfcsBuffPrioAvailable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 7),
    _SfcsBuffPrioAvailable_Type()
)
sfcsBuffPrioAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBuffPrioAvailable.setStatus("mandatory")
_SfcsBuffPrioPeakAlloc_Type = Integer32
_SfcsBuffPrioPeakAlloc_Object = MibTableColumn
sfcsBuffPrioPeakAlloc = _SfcsBuffPrioPeakAlloc_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 8),
    _SfcsBuffPrioPeakAlloc_Type()
)
sfcsBuffPrioPeakAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsBuffPrioPeakAlloc.setStatus("mandatory")
_SfcsBuffPrioConnRejs_Type = Integer32
_SfcsBuffPrioConnRejs_Object = MibTableColumn
sfcsBuffPrioConnRejs = _SfcsBuffPrioConnRejs_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 9),
    _SfcsBuffPrioConnRejs_Type()
)
sfcsBuffPrioConnRejs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBuffPrioConnRejs.setStatus("mandatory")
_SfcsBuffPrioUpTholdTrap_Type = Integer32
_SfcsBuffPrioUpTholdTrap_Object = MibTableColumn
sfcsBuffPrioUpTholdTrap = _SfcsBuffPrioUpTholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 10),
    _SfcsBuffPrioUpTholdTrap_Type()
)
sfcsBuffPrioUpTholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBuffPrioUpTholdTrap.setStatus("mandatory")
_SfcsBuffPrioLoTholdTrap_Type = Integer32
_SfcsBuffPrioLoTholdTrap_Object = MibTableColumn
sfcsBuffPrioLoTholdTrap = _SfcsBuffPrioLoTholdTrap_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 11),
    _SfcsBuffPrioLoTholdTrap_Type()
)
sfcsBuffPrioLoTholdTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBuffPrioLoTholdTrap.setStatus("mandatory")
_SfcsBuffPrioConnRejThold_Type = Integer32
_SfcsBuffPrioConnRejThold_Object = MibTableColumn
sfcsBuffPrioConnRejThold = _SfcsBuffPrioConnRejThold_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 12, 4, 1, 1, 12),
    _SfcsBuffPrioConnRejThold_Type()
)
sfcsBuffPrioConnRejThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsBuffPrioConnRejThold.setStatus("mandatory")
_SfcsProxy_ObjectIdentity = ObjectIdentity
sfcsProxy = _SfcsProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13)
)
_SfcsProxyConfig_ObjectIdentity = ObjectIdentity
sfcsProxyConfig = _SfcsProxyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1)
)
_SfcsProxyConfigTable_Object = MibTable
sfcsProxyConfigTable = _SfcsProxyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    sfcsProxyConfigTable.setStatus("mandatory")
_SfcsProxyConfigEntry_Object = MibTableRow
sfcsProxyConfigEntry = _SfcsProxyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1)
)
sfcsProxyConfigEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsProxyConfigANIMIndex"),
)
if mibBuilder.loadTexts:
    sfcsProxyConfigEntry.setStatus("mandatory")
_SfcsProxyConfigANIMIndex_Type = Integer32
_SfcsProxyConfigANIMIndex_Object = MibTableColumn
sfcsProxyConfigANIMIndex = _SfcsProxyConfigANIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 1),
    _SfcsProxyConfigANIMIndex_Type()
)
sfcsProxyConfigANIMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyConfigANIMIndex.setStatus("mandatory")
_SfcsProxyConfigNUMPORTS_Type = Integer32
_SfcsProxyConfigNUMPORTS_Object = MibTableColumn
sfcsProxyConfigNUMPORTS = _SfcsProxyConfigNUMPORTS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 2),
    _SfcsProxyConfigNUMPORTS_Type()
)
sfcsProxyConfigNUMPORTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyConfigNUMPORTS.setStatus("mandatory")
_SfcsProxyConfigTxMemSize_Type = Integer32
_SfcsProxyConfigTxMemSize_Object = MibTableColumn
sfcsProxyConfigTxMemSize = _SfcsProxyConfigTxMemSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 3),
    _SfcsProxyConfigTxMemSize_Type()
)
sfcsProxyConfigTxMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyConfigTxMemSize.setStatus("mandatory")
_SfcsProxyConfigRxMaxPduSize_Type = Integer32
_SfcsProxyConfigRxMaxPduSize_Object = MibTableColumn
sfcsProxyConfigRxMaxPduSize = _SfcsProxyConfigRxMaxPduSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 4),
    _SfcsProxyConfigRxMaxPduSize_Type()
)
sfcsProxyConfigRxMaxPduSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyConfigRxMaxPduSize.setStatus("mandatory")
_SfcsProxyConfigBandWidth_Type = Integer32
_SfcsProxyConfigBandWidth_Object = MibTableColumn
sfcsProxyConfigBandWidth = _SfcsProxyConfigBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 5),
    _SfcsProxyConfigBandWidth_Type()
)
sfcsProxyConfigBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyConfigBandWidth.setStatus("mandatory")


class _SfcsProxyConfigTransmitDone_Type(Integer32):
    """Custom type sfcsProxyConfigTransmitDone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_SfcsProxyConfigTransmitDone_Type.__name__ = "Integer32"
_SfcsProxyConfigTransmitDone_Object = MibTableColumn
sfcsProxyConfigTransmitDone = _SfcsProxyConfigTransmitDone_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 6),
    _SfcsProxyConfigTransmitDone_Type()
)
sfcsProxyConfigTransmitDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyConfigTransmitDone.setStatus("mandatory")


class _SfcsProxyConfigReceiveFifoState_Type(Integer32):
    """Custom type sfcsProxyConfigReceiveFifoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("not-full", 2))
    )


_SfcsProxyConfigReceiveFifoState_Type.__name__ = "Integer32"
_SfcsProxyConfigReceiveFifoState_Object = MibTableColumn
sfcsProxyConfigReceiveFifoState = _SfcsProxyConfigReceiveFifoState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 7),
    _SfcsProxyConfigReceiveFifoState_Type()
)
sfcsProxyConfigReceiveFifoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyConfigReceiveFifoState.setStatus("mandatory")


class _SfcsProxyConfigPortTransmitMode_Type(Integer32):
    """Custom type sfcsProxyConfigPortTransmitMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("reread", 3),
          ("start-stay", 2),
          ("stop", 1))
    )


_SfcsProxyConfigPortTransmitMode_Type.__name__ = "Integer32"
_SfcsProxyConfigPortTransmitMode_Object = MibTableColumn
sfcsProxyConfigPortTransmitMode = _SfcsProxyConfigPortTransmitMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 8),
    _SfcsProxyConfigPortTransmitMode_Type()
)
sfcsProxyConfigPortTransmitMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyConfigPortTransmitMode.setStatus("mandatory")
_SfcsProxyConfigReceiveFifoReset_Type = Integer32
_SfcsProxyConfigReceiveFifoReset_Object = MibTableColumn
sfcsProxyConfigReceiveFifoReset = _SfcsProxyConfigReceiveFifoReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 9),
    _SfcsProxyConfigReceiveFifoReset_Type()
)
sfcsProxyConfigReceiveFifoReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfcsProxyConfigReceiveFifoReset.setStatus("mandatory")
_SfcsProxyConfigTxFifoReset_Type = Integer32
_SfcsProxyConfigTxFifoReset_Object = MibTableColumn
sfcsProxyConfigTxFifoReset = _SfcsProxyConfigTxFifoReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 10),
    _SfcsProxyConfigTxFifoReset_Type()
)
sfcsProxyConfigTxFifoReset.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfcsProxyConfigTxFifoReset.setStatus("mandatory")


class _SfcsProxyConfigReceiveMode_Type(Integer32):
    """Custom type sfcsProxyConfigReceiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-receiving", 2),
          ("receiving", 1))
    )


_SfcsProxyConfigReceiveMode_Type.__name__ = "Integer32"
_SfcsProxyConfigReceiveMode_Object = MibTableColumn
sfcsProxyConfigReceiveMode = _SfcsProxyConfigReceiveMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 11),
    _SfcsProxyConfigReceiveMode_Type()
)
sfcsProxyConfigReceiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyConfigReceiveMode.setStatus("mandatory")


class _SfcsProxyConfigCaptureMode_Type(Integer32):
    """Custom type sfcsProxyConfigCaptureMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("header", 2))
    )


_SfcsProxyConfigCaptureMode_Type.__name__ = "Integer32"
_SfcsProxyConfigCaptureMode_Object = MibTableColumn
sfcsProxyConfigCaptureMode = _SfcsProxyConfigCaptureMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 12),
    _SfcsProxyConfigCaptureMode_Type()
)
sfcsProxyConfigCaptureMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyConfigCaptureMode.setStatus("mandatory")
_SfcsProxyConfigInitPort_Type = Integer32
_SfcsProxyConfigInitPort_Object = MibTableColumn
sfcsProxyConfigInitPort = _SfcsProxyConfigInitPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 13),
    _SfcsProxyConfigInitPort_Type()
)
sfcsProxyConfigInitPort.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfcsProxyConfigInitPort.setStatus("mandatory")
_SfcsProxyConfigLoad_Type = Integer32
_SfcsProxyConfigLoad_Object = MibTableColumn
sfcsProxyConfigLoad = _SfcsProxyConfigLoad_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 14),
    _SfcsProxyConfigLoad_Type()
)
sfcsProxyConfigLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyConfigLoad.setStatus("mandatory")
_SfcsProxyConfigGumbo_Type = OctetString
_SfcsProxyConfigGumbo_Object = MibTableColumn
sfcsProxyConfigGumbo = _SfcsProxyConfigGumbo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 1, 1, 1, 15),
    _SfcsProxyConfigGumbo_Type()
)
sfcsProxyConfigGumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyConfigGumbo.setStatus("mandatory")
_SfcsProxyTrans_ObjectIdentity = ObjectIdentity
sfcsProxyTrans = _SfcsProxyTrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2)
)
_SfcsProxyTransTable_Object = MibTable
sfcsProxyTransTable = _SfcsProxyTransTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1)
)
if mibBuilder.loadTexts:
    sfcsProxyTransTable.setStatus("mandatory")
_SfcsProxyTransEntry_Object = MibTableRow
sfcsProxyTransEntry = _SfcsProxyTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1)
)
sfcsProxyTransEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsProxyTransANIMIndex"),
)
if mibBuilder.loadTexts:
    sfcsProxyTransEntry.setStatus("mandatory")
_SfcsProxyTransANIMIndex_Type = Integer32
_SfcsProxyTransANIMIndex_Object = MibTableColumn
sfcsProxyTransANIMIndex = _SfcsProxyTransANIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 1),
    _SfcsProxyTransANIMIndex_Type()
)
sfcsProxyTransANIMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyTransANIMIndex.setStatus("mandatory")
_SfcsProxyTransEncodeNewPdu_Type = Integer32
_SfcsProxyTransEncodeNewPdu_Object = MibTableColumn
sfcsProxyTransEncodeNewPdu = _SfcsProxyTransEncodeNewPdu_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 2),
    _SfcsProxyTransEncodeNewPdu_Type()
)
sfcsProxyTransEncodeNewPdu.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfcsProxyTransEncodeNewPdu.setStatus("mandatory")
_SfcsProxyTransVPI_Type = Integer32
_SfcsProxyTransVPI_Object = MibTableColumn
sfcsProxyTransVPI = _SfcsProxyTransVPI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 3),
    _SfcsProxyTransVPI_Type()
)
sfcsProxyTransVPI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyTransVPI.setStatus("mandatory")
_SfcsProxyTransVCI_Type = Integer32
_SfcsProxyTransVCI_Object = MibTableColumn
sfcsProxyTransVCI = _SfcsProxyTransVCI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 4),
    _SfcsProxyTransVCI_Type()
)
sfcsProxyTransVCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyTransVCI.setStatus("mandatory")


class _SfcsProxyTransPTI_Type(Integer32):
    """Custom type sfcsProxyTransPTI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SfcsProxyTransPTI_Type.__name__ = "Integer32"
_SfcsProxyTransPTI_Object = MibTableColumn
sfcsProxyTransPTI = _SfcsProxyTransPTI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 5),
    _SfcsProxyTransPTI_Type()
)
sfcsProxyTransPTI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyTransPTI.setStatus("mandatory")
_SfcsProxyTransCLP_Type = Integer32
_SfcsProxyTransCLP_Object = MibTableColumn
sfcsProxyTransCLP = _SfcsProxyTransCLP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 6),
    _SfcsProxyTransCLP_Type()
)
sfcsProxyTransCLP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyTransCLP.setStatus("mandatory")


class _SfcsProxyTransPayloadType_Type(Integer32):
    """Custom type sfcsProxyTransPayloadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sequential", 2),
          ("uniform", 3),
          ("user-input", 1))
    )


_SfcsProxyTransPayloadType_Type.__name__ = "Integer32"
_SfcsProxyTransPayloadType_Object = MibTableColumn
sfcsProxyTransPayloadType = _SfcsProxyTransPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 7),
    _SfcsProxyTransPayloadType_Type()
)
sfcsProxyTransPayloadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyTransPayloadType.setStatus("mandatory")
_SfcsProxyTransPayloadLength_Type = Integer32
_SfcsProxyTransPayloadLength_Object = MibTableColumn
sfcsProxyTransPayloadLength = _SfcsProxyTransPayloadLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 8),
    _SfcsProxyTransPayloadLength_Type()
)
sfcsProxyTransPayloadLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyTransPayloadLength.setStatus("mandatory")
_SfcsProxyTransPayloadData_Type = OctetString
_SfcsProxyTransPayloadData_Object = MibTableColumn
sfcsProxyTransPayloadData = _SfcsProxyTransPayloadData_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 9),
    _SfcsProxyTransPayloadData_Type()
)
sfcsProxyTransPayloadData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyTransPayloadData.setStatus("mandatory")
_SfcsProxyTransCount_Type = Integer32
_SfcsProxyTransCount_Object = MibTableColumn
sfcsProxyTransCount = _SfcsProxyTransCount_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 10),
    _SfcsProxyTransCount_Type()
)
sfcsProxyTransCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyTransCount.setStatus("mandatory")


class _SfcsProxyTransPayloadAdaptionLayer_Type(Integer32):
    """Custom type sfcsProxyTransPayloadAdaptionLayer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 2),
          ("raw", 1))
    )


_SfcsProxyTransPayloadAdaptionLayer_Type.__name__ = "Integer32"
_SfcsProxyTransPayloadAdaptionLayer_Object = MibTableColumn
sfcsProxyTransPayloadAdaptionLayer = _SfcsProxyTransPayloadAdaptionLayer_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 11),
    _SfcsProxyTransPayloadAdaptionLayer_Type()
)
sfcsProxyTransPayloadAdaptionLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyTransPayloadAdaptionLayer.setStatus("mandatory")
_SfcsProxyTransMpxMethod_Type = Integer32
_SfcsProxyTransMpxMethod_Object = MibTableColumn
sfcsProxyTransMpxMethod = _SfcsProxyTransMpxMethod_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 12),
    _SfcsProxyTransMpxMethod_Type()
)
sfcsProxyTransMpxMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyTransMpxMethod.setStatus("mandatory")


class _SfcsProxyTransControl_Type(Integer32):
    """Custom type sfcsProxyTransControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("repeat", 2),
          ("send-once", 1))
    )


_SfcsProxyTransControl_Type.__name__ = "Integer32"
_SfcsProxyTransControl_Object = MibTableColumn
sfcsProxyTransControl = _SfcsProxyTransControl_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 13),
    _SfcsProxyTransControl_Type()
)
sfcsProxyTransControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyTransControl.setStatus("mandatory")
_SfcsProxyTransGumbo_Type = OctetString
_SfcsProxyTransGumbo_Object = MibTableColumn
sfcsProxyTransGumbo = _SfcsProxyTransGumbo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 2, 1, 1, 14),
    _SfcsProxyTransGumbo_Type()
)
sfcsProxyTransGumbo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyTransGumbo.setStatus("mandatory")
_SfcsProxyRead_ObjectIdentity = ObjectIdentity
sfcsProxyRead = _SfcsProxyRead_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3)
)
_SfcsProxyReadTable_Object = MibTable
sfcsProxyReadTable = _SfcsProxyReadTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1)
)
if mibBuilder.loadTexts:
    sfcsProxyReadTable.setStatus("mandatory")
_SfcsProxyReadEntry_Object = MibTableRow
sfcsProxyReadEntry = _SfcsProxyReadEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1)
)
sfcsProxyReadEntry.setIndexNames(
    (0, "CTRON-SFCS-MIB", "sfcsProxyReadANIMIndex"),
)
if mibBuilder.loadTexts:
    sfcsProxyReadEntry.setStatus("mandatory")
_SfcsProxyReadANIMIndex_Type = Integer32
_SfcsProxyReadANIMIndex_Object = MibTableColumn
sfcsProxyReadANIMIndex = _SfcsProxyReadANIMIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 1),
    _SfcsProxyReadANIMIndex_Type()
)
sfcsProxyReadANIMIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadANIMIndex.setStatus("mandatory")


class _SfcsProxyReadMode_Type(Integer32):
    """Custom type sfcsProxyReadMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all-data", 3),
          ("cell-by-cell", 2),
          ("reassemble-PDU", 1))
    )


_SfcsProxyReadMode_Type.__name__ = "Integer32"
_SfcsProxyReadMode_Object = MibTableColumn
sfcsProxyReadMode = _SfcsProxyReadMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 2),
    _SfcsProxyReadMode_Type()
)
sfcsProxyReadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfcsProxyReadMode.setStatus("mandatory")


class _SfcsProxyReadNewPdu_Type(Integer32):
    """Custom type sfcsProxyReadNewPdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get-next-pdu", 1),
          ("reread-from-beginning", 2))
    )


_SfcsProxyReadNewPdu_Type.__name__ = "Integer32"
_SfcsProxyReadNewPdu_Object = MibTableColumn
sfcsProxyReadNewPdu = _SfcsProxyReadNewPdu_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 3),
    _SfcsProxyReadNewPdu_Type()
)
sfcsProxyReadNewPdu.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfcsProxyReadNewPdu.setStatus("mandatory")
_SfcsProxyReadGumbo_Type = OctetString
_SfcsProxyReadGumbo_Object = MibTableColumn
sfcsProxyReadGumbo = _SfcsProxyReadGumbo_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 4),
    _SfcsProxyReadGumbo_Type()
)
sfcsProxyReadGumbo.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sfcsProxyReadGumbo.setStatus("mandatory")
_SfcsProxyReadVPI_Type = Integer32
_SfcsProxyReadVPI_Object = MibTableColumn
sfcsProxyReadVPI = _SfcsProxyReadVPI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 5),
    _SfcsProxyReadVPI_Type()
)
sfcsProxyReadVPI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadVPI.setStatus("mandatory")
_SfcsProxyReadVCI_Type = Integer32
_SfcsProxyReadVCI_Object = MibTableColumn
sfcsProxyReadVCI = _SfcsProxyReadVCI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 6),
    _SfcsProxyReadVCI_Type()
)
sfcsProxyReadVCI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadVCI.setStatus("mandatory")


class _SfcsProxyReadPTI_Type(Integer32):
    """Custom type sfcsProxyReadPTI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SfcsProxyReadPTI_Type.__name__ = "Integer32"
_SfcsProxyReadPTI_Object = MibTableColumn
sfcsProxyReadPTI = _SfcsProxyReadPTI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 7),
    _SfcsProxyReadPTI_Type()
)
sfcsProxyReadPTI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadPTI.setStatus("mandatory")
_SfcsProxyReadCLP_Type = Integer32
_SfcsProxyReadCLP_Object = MibTableColumn
sfcsProxyReadCLP = _SfcsProxyReadCLP_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 8),
    _SfcsProxyReadCLP_Type()
)
sfcsProxyReadCLP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadCLP.setStatus("mandatory")
_SfcsProxyReadDataLength_Type = Integer32
_SfcsProxyReadDataLength_Object = MibTableColumn
sfcsProxyReadDataLength = _SfcsProxyReadDataLength_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 9),
    _SfcsProxyReadDataLength_Type()
)
sfcsProxyReadDataLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadDataLength.setStatus("mandatory")
_SfcsProxyReadData_Type = OctetString
_SfcsProxyReadData_Object = MibTableColumn
sfcsProxyReadData = _SfcsProxyReadData_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 10),
    _SfcsProxyReadData_Type()
)
sfcsProxyReadData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadData.setStatus("mandatory")


class _SfcsProxyReadPal_Type(Integer32):
    """Custom type sfcsProxyReadPal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 2),
          ("raw", 1))
    )


_SfcsProxyReadPal_Type.__name__ = "Integer32"
_SfcsProxyReadPal_Object = MibTableColumn
sfcsProxyReadPal = _SfcsProxyReadPal_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 11),
    _SfcsProxyReadPal_Type()
)
sfcsProxyReadPal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadPal.setStatus("mandatory")
_SfcsProxyReadInbyteslosts_Type = Integer32
_SfcsProxyReadInbyteslosts_Object = MibTableColumn
sfcsProxyReadInbyteslosts = _SfcsProxyReadInbyteslosts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 12),
    _SfcsProxyReadInbyteslosts_Type()
)
sfcsProxyReadInbyteslosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadInbyteslosts.setStatus("mandatory")
_SfcsProxyReadInCells_Type = Integer32
_SfcsProxyReadInCells_Object = MibTableColumn
sfcsProxyReadInCells = _SfcsProxyReadInCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 13),
    _SfcsProxyReadInCells_Type()
)
sfcsProxyReadInCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadInCells.setStatus("mandatory")
_SfcsProxyReadInError_Type = Integer32
_SfcsProxyReadInError_Object = MibTableColumn
sfcsProxyReadInError = _SfcsProxyReadInError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 14),
    _SfcsProxyReadInError_Type()
)
sfcsProxyReadInError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadInError.setStatus("mandatory")
_SfcsProxyReadInCellReadError_Type = Integer32
_SfcsProxyReadInCellReadError_Object = MibTableColumn
sfcsProxyReadInCellReadError = _SfcsProxyReadInCellReadError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 15),
    _SfcsProxyReadInCellReadError_Type()
)
sfcsProxyReadInCellReadError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadInCellReadError.setStatus("mandatory")
_SfcsProxyReadInHecError_Type = Integer32
_SfcsProxyReadInHecError_Object = MibTableColumn
sfcsProxyReadInHecError = _SfcsProxyReadInHecError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 16),
    _SfcsProxyReadInHecError_Type()
)
sfcsProxyReadInHecError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadInHecError.setStatus("mandatory")
_SfcsProxyReadInTooBigError_Type = Integer32
_SfcsProxyReadInTooBigError_Object = MibTableColumn
sfcsProxyReadInTooBigError = _SfcsProxyReadInTooBigError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 17),
    _SfcsProxyReadInTooBigError_Type()
)
sfcsProxyReadInTooBigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadInTooBigError.setStatus("mandatory")
_SfcsProxyReadInCRCError_Type = Integer32
_SfcsProxyReadInCRCError_Object = MibTableColumn
sfcsProxyReadInCRCError = _SfcsProxyReadInCRCError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 18),
    _SfcsProxyReadInCRCError_Type()
)
sfcsProxyReadInCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadInCRCError.setStatus("mandatory")
_SfcsProxyReadInLengthMismatchError_Type = Integer32
_SfcsProxyReadInLengthMismatchError_Object = MibTableColumn
sfcsProxyReadInLengthMismatchError = _SfcsProxyReadInLengthMismatchError_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 19),
    _SfcsProxyReadInLengthMismatchError_Type()
)
sfcsProxyReadInLengthMismatchError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadInLengthMismatchError.setStatus("mandatory")
_SfcsProxyReadInTotalCells_Type = Integer32
_SfcsProxyReadInTotalCells_Object = MibTableColumn
sfcsProxyReadInTotalCells = _SfcsProxyReadInTotalCells_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1, 13, 3, 1, 1, 20),
    _SfcsProxyReadInTotalCells_Type()
)
sfcsProxyReadInTotalCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfcsProxyReadInTotalCells.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFCS-MIB",
    **{"cabletron": cabletron,
       "mibs": mibs,
       "ctron": ctron,
       "ctDataLink": ctDataLink,
       "ctSwitch": ctSwitch,
       "ctsfSwitch": ctsfSwitch,
       "ctSFCS": ctSFCS,
       "sfcsSystem": sfcsSystem,
       "sfcsSysConfig": sfcsSysConfig,
       "sfcsSysConfigTable": sfcsSysConfigTable,
       "sfcsSysConfigEnt": sfcsSysConfigEnt,
       "sfcsSysConfigAdminStatus": sfcsSysConfigAdminStatus,
       "sfcsSysConfigOperStatus": sfcsSysConfigOperStatus,
       "sfcsSysConfigOperTime": sfcsSysConfigOperTime,
       "sfcsSysConfigLastChange": sfcsSysConfigLastChange,
       "sfcsSysConfigSwitchCapacity": sfcsSysConfigSwitchCapacity,
       "sfcsSysConfigMaxCnxEntries": sfcsSysConfigMaxCnxEntries,
       "sfcsSysConfigMaxStatEntries": sfcsSysConfigMaxStatEntries,
       "sfcsSysConfigMaxUpcEntries": sfcsSysConfigMaxUpcEntries,
       "sfcsSysConfigNumberANIMS": sfcsSysConfigNumberANIMS,
       "sfcsSysConfigInterfaceCapability": sfcsSysConfigInterfaceCapability,
       "sfcsSysConfigTypeofSwitch": sfcsSysConfigTypeofSwitch,
       "sfcsSysConfigPolicingSupport": sfcsSysConfigPolicingSupport,
       "sfcsSysConfigPnniNsapPrefix": sfcsSysConfigPnniNsapPrefix,
       "sfcsSysConfigPnniNodeLevel": sfcsSysConfigPnniNodeLevel,
       "sfcsSysConfigPnniAddessingMode": sfcsSysConfigPnniAddessingMode,
       "sfcsSysConfigPnniAddessingAdmnStatus": sfcsSysConfigPnniAddessingAdmnStatus,
       "sfcsSysConfigFMVer": sfcsSysConfigFMVer,
       "sfcsSysConfigCTMSlotMask": sfcsSysConfigCTMSlotMask,
       "sfcsSysConfigMaxfreecva": sfcsSysConfigMaxfreecva,
       "sfcsSysConfigUBR": sfcsSysConfigUBR,
       "sfcsSysStatus": sfcsSysStatus,
       "sfcsSysStatusTable": sfcsSysStatusTable,
       "sfcsSysStatusEnt": sfcsSysStatusEnt,
       "sfcsSysStatusTdmCellCount": sfcsSysStatusTdmCellCount,
       "sfcsSysStatusTdmUtilization": sfcsSysStatusTdmUtilization,
       "sfcsSysStatusCurrCnxEntries": sfcsSysStatusCurrCnxEntries,
       "sfcsSysStatusCurrUPCEntries": sfcsSysStatusCurrUPCEntries,
       "sfcsSysStatusCurrStatsEntries": sfcsSysStatusCurrStatsEntries,
       "sfcsSysStatusAllocatedBw": sfcsSysStatusAllocatedBw,
       "sfcsSysSystemCfg": sfcsSysSystemCfg,
       "sfcsSysSystemCfgTable": sfcsSysSystemCfgTable,
       "sfcsSysSystemCfgEnt": sfcsSysSystemCfgEnt,
       "sfcsSysConfigAdminReset": sfcsSysConfigAdminReset,
       "sfcsSysConfigATOMPersistance": sfcsSysConfigATOMPersistance,
       "sfcsSysConfigVcSize": sfcsSysConfigVcSize,
       "sfcsSysConfigPowerUpDiags": sfcsSysConfigPowerUpDiags,
       "sfcsSysBPCfg": sfcsSysBPCfg,
       "sfcsSysBPTable": sfcsSysBPTable,
       "sfcsSysBPEnt": sfcsSysBPEnt,
       "sfcsSysBPClkSelect": sfcsSysBPClkSelect,
       "sfcsEngine": sfcsEngine,
       "sfcsConfig": sfcsConfig,
       "sfcsConfigTable": sfcsConfigTable,
       "sfcsConfigEntry": sfcsConfigEntry,
       "sfcsConfigSlotIndex": sfcsConfigSlotIndex,
       "sfcsConfigAdminStatus": sfcsConfigAdminStatus,
       "sfcsConfigAdminReset": sfcsConfigAdminReset,
       "sfcsConfigOperStatus": sfcsConfigOperStatus,
       "sfcsConfigOperTime": sfcsConfigOperTime,
       "sfcsConfigLastChange": sfcsConfigLastChange,
       "sfcsConfigVersion": sfcsConfigVersion,
       "sfcsConfigMibRev": sfcsConfigMibRev,
       "sfcsConfigSwitchHostPort": sfcsConfigSwitchHostPort,
       "sfcsConfigHostCtrlATMAddr": sfcsConfigHostCtrlATMAddr,
       "sfcsConfigSwitchCapacity": sfcsConfigSwitchCapacity,
       "sfcsConfigMaxCnxEntries": sfcsConfigMaxCnxEntries,
       "sfcsConfigMaxStatEntries": sfcsConfigMaxStatEntries,
       "sfcsConfigMaxUpcEntries": sfcsConfigMaxUpcEntries,
       "sfcsConfigNumberANIMS": sfcsConfigNumberANIMS,
       "sfcsConfigBwCapability": sfcsConfigBwCapability,
       "sfcsConfigMasterClock1Source": sfcsConfigMasterClock1Source,
       "sfcsConfigMasterClock2Source": sfcsConfigMasterClock2Source,
       "sfcsConfigMasterClock1Standby": sfcsConfigMasterClock1Standby,
       "sfcsConfigMasterClock2Standby": sfcsConfigMasterClock2Standby,
       "sfcsStatus": sfcsStatus,
       "sfcsStatusTable": sfcsStatusTable,
       "sfcsStatusEntry": sfcsStatusEntry,
       "sfcsStatusSlotIndex": sfcsStatusSlotIndex,
       "sfcsStatusTdmCellCount": sfcsStatusTdmCellCount,
       "sfcsStatusTdmUtilization": sfcsStatusTdmUtilization,
       "sfcsStatusCurrCnxEntries": sfcsStatusCurrCnxEntries,
       "sfcsStatusCurrUPCEntries": sfcsStatusCurrUPCEntries,
       "sfcsStatusCurrStatsEntries": sfcsStatusCurrStatsEntries,
       "sfcsStatusCurrCtmAgent": sfcsStatusCurrCtmAgent,
       "sfcsUPCEngine": sfcsUPCEngine,
       "sfcsUPCTable": sfcsUPCTable,
       "sfcsUPCEntry": sfcsUPCEntry,
       "sfcsUPCSlotIndex": sfcsUPCSlotIndex,
       "sfcsUPCAdminStatus": sfcsUPCAdminStatus,
       "sfcsUPCOperStatus": sfcsUPCOperStatus,
       "sfcsUPCReset": sfcsUPCReset,
       "sfcsUPCOperTime": sfcsUPCOperTime,
       "sfcsStatisticsEngine": sfcsStatisticsEngine,
       "sfcsStatsEngineTable": sfcsStatsEngineTable,
       "sfcsStatsEngineEntry": sfcsStatsEngineEntry,
       "sfcsStatsEngineSlotIndex": sfcsStatsEngineSlotIndex,
       "sfcsStatsEngineAdminStatus": sfcsStatsEngineAdminStatus,
       "sfcsStatsEngineOperStatus": sfcsStatsEngineOperStatus,
       "sfcsStatsEngineReset": sfcsStatsEngineReset,
       "sfcsStatsEngineOperTime": sfcsStatsEngineOperTime,
       "sfcsPacketDiscardEngine": sfcsPacketDiscardEngine,
       "sfcsPacketDiscardEngineTable": sfcsPacketDiscardEngineTable,
       "sfcsPacketDiscardEngineEntry": sfcsPacketDiscardEngineEntry,
       "sfcsPacketDiscardEngineSlotIndex": sfcsPacketDiscardEngineSlotIndex,
       "sfcsPacketDiscardEngineAdminStatus": sfcsPacketDiscardEngineAdminStatus,
       "sfcsPacketDiscardEngineOperStatus": sfcsPacketDiscardEngineOperStatus,
       "sfcsPacketDiscardEngineReset": sfcsPacketDiscardEngineReset,
       "sfcsPacketDiscardEngineEPDPercentage": sfcsPacketDiscardEngineEPDPercentage,
       "sfcsPacketDiscardEngineOperTime": sfcsPacketDiscardEngineOperTime,
       "sfcsANIM": sfcsANIM,
       "sfcsANIMConfig": sfcsANIMConfig,
       "sfcsANIMConfigTable": sfcsANIMConfigTable,
       "sfcsANIMConfigEntry": sfcsANIMConfigEntry,
       "sfcsANIMConfigANIMIndex": sfcsANIMConfigANIMIndex,
       "sfcsANIMConfigAdminStatus": sfcsANIMConfigAdminStatus,
       "sfcsANIMConfigOperStatus": sfcsANIMConfigOperStatus,
       "sfcsANIMConfigANIMType": sfcsANIMConfigANIMType,
       "sfcsANIMConfigNumInterfaces": sfcsANIMConfigNumInterfaces,
       "sfcsANIMConfigLineRate": sfcsANIMConfigLineRate,
       "sfcsANIMConfigToMB": sfcsANIMConfigToMB,
       "sfcsANIMConfigMBClockSelect": sfcsANIMConfigMBClockSelect,
       "sfcsANIMStatistics": sfcsANIMStatistics,
       "sfcsANIMStatsTable": sfcsANIMStatsTable,
       "sfcsANIMStatsEntry": sfcsANIMStatsEntry,
       "sfcsANIMStatsANIMIndex": sfcsANIMStatsANIMIndex,
       "sfcsANIMStatsRxCells": sfcsANIMStatsRxCells,
       "sfcsANIMStatsTxCells": sfcsANIMStatsTxCells,
       "sfcsANIMPic": sfcsANIMPic,
       "sfcsANIMPicTable": sfcsANIMPicTable,
       "sfcsANIMPicEntry": sfcsANIMPicEntry,
       "sfcsANIMPicSlot": sfcsANIMPicSlot,
       "sfcsANIMPicIndex": sfcsANIMPicIndex,
       "sfcsANIMPicLocation": sfcsANIMPicLocation,
       "sfcsANIMPicStatus": sfcsANIMPicStatus,
       "sfcsANIMPicVersion": sfcsANIMPicVersion,
       "sfcsANIMPicModuleType": sfcsANIMPicModuleType,
       "sfcsANIMPicMfgPN": sfcsANIMPicMfgPN,
       "sfcsANIMPicMfgSN": sfcsANIMPicMfgSN,
       "sfcsANIMPicMfgPartNumb": sfcsANIMPicMfgPartNumb,
       "sfcsANIMPicMfgSerialNumb": sfcsANIMPicMfgSerialNumb,
       "sfcsANIMPicMfgReworkLocation": sfcsANIMPicMfgReworkLocation,
       "sfcsANIMPicMfgMfgLocation": sfcsANIMPicMfgMfgLocation,
       "sfcsANIMPicMfgDateCode": sfcsANIMPicMfgDateCode,
       "sfcsANIMPicMfgRevisionCode": sfcsANIMPicMfgRevisionCode,
       "sfcsANIMPicTLPN": sfcsANIMPicTLPN,
       "sfcsANIMPicTLSN": sfcsANIMPicTLSN,
       "sfcsANIMPicTLPartNumb": sfcsANIMPicTLPartNumb,
       "sfcsANIMPicTLSerialNumb": sfcsANIMPicTLSerialNumb,
       "sfcsANIMPicTLReworkLocation": sfcsANIMPicTLReworkLocation,
       "sfcsANIMPicTLMfgLocation": sfcsANIMPicTLMfgLocation,
       "sfcsANIMPicTLDateCode": sfcsANIMPicTLDateCode,
       "sfcsANIMPicTLRevisionCode": sfcsANIMPicTLRevisionCode,
       "sfcsANIMPicTLPcbRevision": sfcsANIMPicTLPcbRevision,
       "sfcsANIMPicMacAddr": sfcsANIMPicMacAddr,
       "sfcsANIMPicNumbRsvdAddrs": sfcsANIMPicNumbRsvdAddrs,
       "sfcsANIMPicBoardLevelRevision": sfcsANIMPicBoardLevelRevision,
       "sfcsANIMPicModuleTypeString": sfcsANIMPicModuleTypeString,
       "sfcsANIMPicDcDcConverterType": sfcsANIMPicDcDcConverterType,
       "sfcsANIMPicDcDcConverterInputPower": sfcsANIMPicDcDcConverterInputPower,
       "sfcsANIMPicSmb1PromVersion": sfcsANIMPicSmb1PromVersion,
       "sfcsInterface": sfcsInterface,
       "sfcsInterfaceConfig": sfcsInterfaceConfig,
       "sfcsInterfaceConfigTable": sfcsInterfaceConfigTable,
       "sfcsInterfaceConfigEntry": sfcsInterfaceConfigEntry,
       "sfcsInterfaceConfigInterfaceIndex": sfcsInterfaceConfigInterfaceIndex,
       "sfcsInterfaceConfigType": sfcsInterfaceConfigType,
       "sfcsInterfacePeakBufferUseage": sfcsInterfacePeakBufferUseage,
       "sfcsInterfaceConfigNumberOfQueues": sfcsInterfaceConfigNumberOfQueues,
       "sfcsInterfaceConfigSigStackID": sfcsInterfaceConfigSigStackID,
       "sfcsInterfaceConfigClockingSource": sfcsInterfaceConfigClockingSource,
       "sfcsInterfaceStatistics": sfcsInterfaceStatistics,
       "sfcsInterfaceStatsTable": sfcsInterfaceStatsTable,
       "sfcsInterfaceStatsEntry": sfcsInterfaceStatsEntry,
       "sfcsInterfaceStatsInterfaceIndex": sfcsInterfaceStatsInterfaceIndex,
       "sfcsInterfaceStatsRxErrors": sfcsInterfaceStatsRxErrors,
       "sfcsInterfaceStatsVPILookupInvalidErrors": sfcsInterfaceStatsVPILookupInvalidErrors,
       "sfcsInterfaceStatsRxCnxLookupInvalidErrors": sfcsInterfaceStatsRxCnxLookupInvalidErrors,
       "sfcsInterfaceStatsRxCellCnt": sfcsInterfaceStatsRxCellCnt,
       "sfcsInterfaceStatsTxCellCnt": sfcsInterfaceStatsTxCellCnt,
       "sfcsInterfaceStatsOverflowDropCellCnt": sfcsInterfaceStatsOverflowDropCellCnt,
       "sfcsQueue": sfcsQueue,
       "sfcsQueueConfig": sfcsQueueConfig,
       "sfcsQueueConfigTable": sfcsQueueConfigTable,
       "sfcsQueueConfigEntry": sfcsQueueConfigEntry,
       "sfcsQueueConfigInterfaceIndex": sfcsQueueConfigInterfaceIndex,
       "sfcsQueueConfigQueueIndex": sfcsQueueConfigQueueIndex,
       "sfcsQueueConfigQueueSize": sfcsQueueConfigQueueSize,
       "sfcsQueueConfigQueueBandwidth": sfcsQueueConfigQueueBandwidth,
       "sfcsQueueConfigClpDropThreshold": sfcsQueueConfigClpDropThreshold,
       "sfcsQueueConfigCongestionThreshold": sfcsQueueConfigCongestionThreshold,
       "sfcsQueueConfigEFCILowThreshold": sfcsQueueConfigEFCILowThreshold,
       "sfcsQueueConfigRMThreshold": sfcsQueueConfigRMThreshold,
       "sfcsQueueConfigEPDThreshold": sfcsQueueConfigEPDThreshold,
       "sfcsQueueStatistics": sfcsQueueStatistics,
       "sfcsQueueStatsTable": sfcsQueueStatsTable,
       "sfcsQueueStatsEntry": sfcsQueueStatsEntry,
       "sfcsQueueStatsInterfaceIndex": sfcsQueueStatsInterfaceIndex,
       "sfcsQueueStatsQueue": sfcsQueueStatsQueue,
       "sfcsQueueStatsTxClpCellsDiscarded": sfcsQueueStatsTxClpCellsDiscarded,
       "sfcsQueueStatsTxCellsDropped": sfcsQueueStatsTxCellsDropped,
       "sfcsQueueStatsQueuePeakLevel": sfcsQueueStatsQueuePeakLevel,
       "sfcsQueueStatsTxCellCnt": sfcsQueueStatsTxCellCnt,
       "sfcsConnection": sfcsConnection,
       "sfcsConnectionConfig": sfcsConnectionConfig,
       "sfcsCnxCfgTable": sfcsCnxCfgTable,
       "sfcsCnxCfgEntry": sfcsCnxCfgEntry,
       "sfcsCnxCfgCrossConnectIndex": sfcsCnxCfgCrossConnectIndex,
       "sfcsCnxCfgCrossConnectLowIfIndex": sfcsCnxCfgCrossConnectLowIfIndex,
       "sfcsCnxCfgCrossConnectLowVpi": sfcsCnxCfgCrossConnectLowVpi,
       "sfcsCnxCfgCrossConnectLowVci": sfcsCnxCfgCrossConnectLowVci,
       "sfcsCnxCfgCrossConnectHighIfIndex": sfcsCnxCfgCrossConnectHighIfIndex,
       "sfcsCnxCfgCrossConnectHighVpi": sfcsCnxCfgCrossConnectHighVpi,
       "sfcsCnxCfgCrossConnectHighVci": sfcsCnxCfgCrossConnectHighVci,
       "sfcsCnxCfgType": sfcsCnxCfgType,
       "sfcsCnxCfgTmType": sfcsCnxCfgTmType,
       "sfcsCnxCfgUPCEnable": sfcsCnxCfgUPCEnable,
       "sfcsCnxCfgStatsEnable": sfcsCnxCfgStatsEnable,
       "sfcsCnxCfgStatsTableCounterSizes": sfcsCnxCfgStatsTableCounterSizes,
       "sfcsCnxCfgOwner": sfcsCnxCfgOwner,
       "sfcsConnectionStatistics": sfcsConnectionStatistics,
       "sfcsCnxStatsTable": sfcsCnxStatsTable,
       "sfcsCnxStatsEntry": sfcsCnxStatsEntry,
       "sfcsCnxStatsCrossConnectIndex": sfcsCnxStatsCrossConnectIndex,
       "sfcsCnxStatsCrossConnectLowIfIndex": sfcsCnxStatsCrossConnectLowIfIndex,
       "sfcsCnxStatsCrossConnectLowVpi": sfcsCnxStatsCrossConnectLowVpi,
       "sfcsCnxStatsCrossConnectLowVci": sfcsCnxStatsCrossConnectLowVci,
       "sfcsCnxStatsCrossConnectHighIfIndex": sfcsCnxStatsCrossConnectHighIfIndex,
       "sfcsCnxStatsCrossConnectHighVpi": sfcsCnxStatsCrossConnectHighVpi,
       "sfcsCnxStatsCrossConnectHighVci": sfcsCnxStatsCrossConnectHighVci,
       "sfcsCnxStatsLoToHiHTxCells": sfcsCnxStatsLoToHiHTxCells,
       "sfcsCnxStatsLoToHiDroppedCells": sfcsCnxStatsLoToHiDroppedCells,
       "sfcsCnxStatsLoToHiTaggedCells": sfcsCnxStatsLoToHiTaggedCells,
       "sfcsCnxStatsHiToLoHTxCells": sfcsCnxStatsHiToLoHTxCells,
       "sfcsCnxStatsHiToLoDroppedCells": sfcsCnxStatsHiToLoDroppedCells,
       "sfcsCnxStatsHiToLoTaggedCells": sfcsCnxStatsHiToLoTaggedCells,
       "sfcsConnectionError": sfcsConnectionError,
       "sfcsCnxErrorTable": sfcsCnxErrorTable,
       "sfcsCnxErrorEntry": sfcsCnxErrorEntry,
       "sfcsCnxErrorCode": sfcsCnxErrorCode,
       "sfcsCnxErrorTimeStamp": sfcsCnxErrorTimeStamp,
       "sfcsCnxErrorRowStatus": sfcsCnxErrorRowStatus,
       "sfcsConnectionAPI": sfcsConnectionAPI,
       "sfcsCnxAPIEntry": sfcsCnxAPIEntry,
       "sfcsCTM": sfcsCTM,
       "sfcsCTMInterfaceConfig": sfcsCTMInterfaceConfig,
       "sfcsCTMInterfaceConfigTable": sfcsCTMInterfaceConfigTable,
       "sfcsCTMInterfaceConfigEntry": sfcsCTMInterfaceConfigEntry,
       "sfcsCTMInterfaceConfigInterfaceIndex": sfcsCTMInterfaceConfigInterfaceIndex,
       "sfcsCTMInterfaceConfigType": sfcsCTMInterfaceConfigType,
       "sfcsCTMInterfacePeakBufferUseage": sfcsCTMInterfacePeakBufferUseage,
       "sfcsCTMInterfaceConfigNumberOfQueues": sfcsCTMInterfaceConfigNumberOfQueues,
       "sfcsCTMInterfaceConfigSigStackID": sfcsCTMInterfaceConfigSigStackID,
       "sfcsCTMInterfaceConfigClocking": sfcsCTMInterfaceConfigClocking,
       "sfcsCTMInterfaceConfigNextVPI": sfcsCTMInterfaceConfigNextVPI,
       "sfcsCTMInterfaceConfigNextVCI": sfcsCTMInterfaceConfigNextVCI,
       "sfcsCTMInterfaceStatistics": sfcsCTMInterfaceStatistics,
       "sfcsCTMInterfaceStatsTable": sfcsCTMInterfaceStatsTable,
       "sfcsCTMInterfaceStatsEntry": sfcsCTMInterfaceStatsEntry,
       "sfcsCTMInterfaceStatsInterfaceIndex": sfcsCTMInterfaceStatsInterfaceIndex,
       "sfcsCTMInterfaceStatsRxErrors": sfcsCTMInterfaceStatsRxErrors,
       "sfcsCTMInterfaceStatsVPILookupInvalidErrors": sfcsCTMInterfaceStatsVPILookupInvalidErrors,
       "sfcsCTMInterfaceStatsRxCnxLookupInvalidErrors": sfcsCTMInterfaceStatsRxCnxLookupInvalidErrors,
       "sfcsCTMInterfaceStatsRxCellCnt": sfcsCTMInterfaceStatsRxCellCnt,
       "sfcsCTMInterfaceStatsTxCellCnt": sfcsCTMInterfaceStatsTxCellCnt,
       "sfcsCTMInterfaceStatsOverflowDropCellCnt": sfcsCTMInterfaceStatsOverflowDropCellCnt,
       "sfcsCTMQueueConfig": sfcsCTMQueueConfig,
       "sfcsCTMQueueConfigTable": sfcsCTMQueueConfigTable,
       "sfcsCTMQueueConfigEntry": sfcsCTMQueueConfigEntry,
       "sfcsCTMQueueConfigInterfaceIndex": sfcsCTMQueueConfigInterfaceIndex,
       "sfcsCTMQueueConfigQueueIndex": sfcsCTMQueueConfigQueueIndex,
       "sfcsCTMQueueConfigQueueSize": sfcsCTMQueueConfigQueueSize,
       "sfcsCTMQueueConfigQueueBandwidth": sfcsCTMQueueConfigQueueBandwidth,
       "sfcsCTMQueueConfigClpDropThreshold": sfcsCTMQueueConfigClpDropThreshold,
       "sfcsCTMQueueConfigCongestionThreshold": sfcsCTMQueueConfigCongestionThreshold,
       "sfcsCTMQueueConfigEFCILowThreshold": sfcsCTMQueueConfigEFCILowThreshold,
       "sfcsCTMQueueConfigRMThreshold": sfcsCTMQueueConfigRMThreshold,
       "sfcsCTMQueueStatistics": sfcsCTMQueueStatistics,
       "sfcsCTMQueueStatsTable": sfcsCTMQueueStatsTable,
       "sfcsCTMQueueStatsEntry": sfcsCTMQueueStatsEntry,
       "sfcsCTMQueueStatsInterfaceIndex": sfcsCTMQueueStatsInterfaceIndex,
       "sfcsCTMQueueStatsQueue": sfcsCTMQueueStatsQueue,
       "sfcsCTMQueueStatsTxClpCellsDiscarded": sfcsCTMQueueStatsTxClpCellsDiscarded,
       "sfcsCTMQueueStatsTxCellsDropped": sfcsCTMQueueStatsTxCellsDropped,
       "sfcsCTMQueueStatsQueuePeakLevel": sfcsCTMQueueStatsQueuePeakLevel,
       "sfcsCTMQueueStatsTxCellCnt": sfcsCTMQueueStatsTxCellCnt,
       "sfcsBWMgr": sfcsBWMgr,
       "sfcsBwNims": sfcsBwNims,
       "sfcsBwNimsTable": sfcsBwNimsTable,
       "sfcsBwNimsEntry": sfcsBwNimsEntry,
       "sfcsBwNimsIndex": sfcsBwNimsIndex,
       "sfcsBwNimsAdminStatus": sfcsBwNimsAdminStatus,
       "sfcsBWNimsBuffCount": sfcsBWNimsBuffCount,
       "sfcsBWNimsPortCount": sfcsBWNimsPortCount,
       "sfcsBWNimsPrioCount": sfcsBWNimsPrioCount,
       "sfcsBwPorts": sfcsBwPorts,
       "sfcsBwPortsTable": sfcsBwPortsTable,
       "sfcsBwPortsEntry": sfcsBwPortsEntry,
       "sfcsBwPortsIndex": sfcsBwPortsIndex,
       "sfcsBwPortsAdminStatus": sfcsBwPortsAdminStatus,
       "sfcsBwPortsPhysBwFwd": sfcsBwPortsPhysBwFwd,
       "sfcsBwPortsPhysBwRev": sfcsBwPortsPhysBwRev,
       "sfcsBwPortsZone": sfcsBwPortsZone,
       "sfcsBwPortsMetric": sfcsBwPortsMetric,
       "sfcsBwPortPools": sfcsBwPortPools,
       "sfcsBwPortPoolLimitsTable": sfcsBwPortPoolLimitsTable,
       "sfcsBwPortPoolLimitsEntry": sfcsBwPortPoolLimitsEntry,
       "sfcsBwPortPoolLimitsIndex": sfcsBwPortPoolLimitsIndex,
       "sfcsBwPortPoolLimitsPoolIndex": sfcsBwPortPoolLimitsPoolIndex,
       "sfcsBwPortPoolLimitsMaxAllocBwFwd": sfcsBwPortPoolLimitsMaxAllocBwFwd,
       "sfcsBwPortPoolLimitsMaxAllocBwRev": sfcsBwPortPoolLimitsMaxAllocBwRev,
       "sfcsBwPortPoolLimitsBwAllocStrat": sfcsBwPortPoolLimitsBwAllocStrat,
       "sfcsBwPortPoolLimitsBwConstant": sfcsBwPortPoolLimitsBwConstant,
       "sfcsBwPortPoolLimitsCBRLimitFwd": sfcsBwPortPoolLimitsCBRLimitFwd,
       "sfcsBwPortPoolLimitsCBRLimitRev": sfcsBwPortPoolLimitsCBRLimitRev,
       "sfcsBwPortPoolLimitsABRLimitFwd": sfcsBwPortPoolLimitsABRLimitFwd,
       "sfcsBwPortPoolLimitsABRLimitRev": sfcsBwPortPoolLimitsABRLimitRev,
       "sfcsBwPortPoolLimitsVBRLimitFwd": sfcsBwPortPoolLimitsVBRLimitFwd,
       "sfcsBwPortPoolLimitsVBRLimitRev": sfcsBwPortPoolLimitsVBRLimitRev,
       "sfcsBwPortPoolLimitsUBRLimitFwd": sfcsBwPortPoolLimitsUBRLimitFwd,
       "sfcsBwPortPoolLimitsUBRLimitRev": sfcsBwPortPoolLimitsUBRLimitRev,
       "sfcsBwPortPoolLimitsUBRConnLimitFwd": sfcsBwPortPoolLimitsUBRConnLimitFwd,
       "sfcsBwPortPoolLimitsUBRConnLimitRev": sfcsBwPortPoolLimitsUBRConnLimitRev,
       "sfcsBwPortPoolStatTable": sfcsBwPortPoolStatTable,
       "sfcsBwPortPoolStatEntry": sfcsBwPortPoolStatEntry,
       "sfcsBwPortPoolStatsIndex": sfcsBwPortPoolStatsIndex,
       "sfcsBwPortPoolStatsPoolIndex": sfcsBwPortPoolStatsPoolIndex,
       "sfcsBwPortPoolStatConnCntFwd": sfcsBwPortPoolStatConnCntFwd,
       "sfcsBwPortPoolStatConnCntRev": sfcsBwPortPoolStatConnCntRev,
       "sfcsBwPortPoolStatAllocBwFwd": sfcsBwPortPoolStatAllocBwFwd,
       "sfcsBwPortPoolStatAllocBwRev": sfcsBwPortPoolStatAllocBwRev,
       "sfcsBwPortPoolStatAvailBwFwd": sfcsBwPortPoolStatAvailBwFwd,
       "sfcsBwPortPoolStatAvailBwRev": sfcsBwPortPoolStatAvailBwRev,
       "sfcsBwPortPoolStatPeakBwFwd": sfcsBwPortPoolStatPeakBwFwd,
       "sfcsBwPortPoolStatPeakBwRev": sfcsBwPortPoolStatPeakBwRev,
       "sfcsBwPortPoolStatRejConnFwd": sfcsBwPortPoolStatRejConnFwd,
       "sfcsBwPortPoolStatRejConnRev": sfcsBwPortPoolStatRejConnRev,
       "sfcsBwPortPoolStatPrevAdverMAXCRFwd": sfcsBwPortPoolStatPrevAdverMAXCRFwd,
       "sfcsBwPortPoolStatPrevAdverMAXCRRev": sfcsBwPortPoolStatPrevAdverMAXCRRev,
       "sfcsBwPortPoolStatPrevAdverAvailCRFwd": sfcsBwPortPoolStatPrevAdverAvailCRFwd,
       "sfcsBwPortPoolStatPrevAdverAvailCRRev": sfcsBwPortPoolStatPrevAdverAvailCRRev,
       "sfcsBwPortPoolStatCBRConnCntFwd": sfcsBwPortPoolStatCBRConnCntFwd,
       "sfcsBwPortPoolStatCBRConnCntRev": sfcsBwPortPoolStatCBRConnCntRev,
       "sfcsBwPortPoolStatCBRConnRejFwd": sfcsBwPortPoolStatCBRConnRejFwd,
       "sfcsBwPortPoolStatCBRConnRejRev": sfcsBwPortPoolStatCBRConnRejRev,
       "sfcsBwPortPoolStatCBRAllocBwFwd": sfcsBwPortPoolStatCBRAllocBwFwd,
       "sfcsBwPortPoolStatCBRAllocBwRev": sfcsBwPortPoolStatCBRAllocBwRev,
       "sfcsBwPortPoolStatCBRAggPCRFwd": sfcsBwPortPoolStatCBRAggPCRFwd,
       "sfcsBwPortPoolStatCBRAggPCRRev": sfcsBwPortPoolStatCBRAggPCRRev,
       "sfcsBwPortPoolStatCBRPrevAdverMAXCTD": sfcsBwPortPoolStatCBRPrevAdverMAXCTD,
       "sfcsBwPortPoolStatCBRPrevAdverCDV": sfcsBwPortPoolStatCBRPrevAdverCDV,
       "sfcsBwPortPoolStatABRConnCntFwd": sfcsBwPortPoolStatABRConnCntFwd,
       "sfcsBwPortPoolStatABRConnCntRev": sfcsBwPortPoolStatABRConnCntRev,
       "sfcsBwPortPoolStatABRConnRejFwd": sfcsBwPortPoolStatABRConnRejFwd,
       "sfcsBwPortPoolStatABRConnRejRev": sfcsBwPortPoolStatABRConnRejRev,
       "sfcsBwPortPoolStatABRAllocBwFwd": sfcsBwPortPoolStatABRAllocBwFwd,
       "sfcsBwPortPoolStatABRAllocBwRev": sfcsBwPortPoolStatABRAllocBwRev,
       "sfcsBwPortPoolStatABRAggPCRFwd": sfcsBwPortPoolStatABRAggPCRFwd,
       "sfcsBwPortPoolStatABRAggPCRRev": sfcsBwPortPoolStatABRAggPCRRev,
       "sfcsBwPortPoolStatABRPrevAdverMAXCTD": sfcsBwPortPoolStatABRPrevAdverMAXCTD,
       "sfcsBwPortPoolStatABRPrevAdverCDV": sfcsBwPortPoolStatABRPrevAdverCDV,
       "sfcsBwPortPoolStatVBRConnCntFwd": sfcsBwPortPoolStatVBRConnCntFwd,
       "sfcsBwPortPoolStatVBRConnCntRev": sfcsBwPortPoolStatVBRConnCntRev,
       "sfcsBwPortPoolStatVBRConnRejFwd": sfcsBwPortPoolStatVBRConnRejFwd,
       "sfcsBwPortPoolStatVBRConnRejRev": sfcsBwPortPoolStatVBRConnRejRev,
       "sfcsBwPortPoolStatVBRAllocBwFwd": sfcsBwPortPoolStatVBRAllocBwFwd,
       "sfcsBwPortPoolStatVBRAllocBwRev": sfcsBwPortPoolStatVBRAllocBwRev,
       "sfcsBwPortPoolStatVBRAggPCRFwd": sfcsBwPortPoolStatVBRAggPCRFwd,
       "sfcsBwPortPoolStatVBRAggPCRRev": sfcsBwPortPoolStatVBRAggPCRRev,
       "sfcsBwPortPoolStatVBRPrevAdverMAXCTD": sfcsBwPortPoolStatVBRPrevAdverMAXCTD,
       "sfcsBwPortPoolStatVBRPrevAdverCDV": sfcsBwPortPoolStatVBRPrevAdverCDV,
       "sfcsBwPortPoolStatUBRConnCntFwd": sfcsBwPortPoolStatUBRConnCntFwd,
       "sfcsBwPortPoolStatUBRConnCntRev": sfcsBwPortPoolStatUBRConnCntRev,
       "sfcsBwPortPoolStatUBRConnRejFwd": sfcsBwPortPoolStatUBRConnRejFwd,
       "sfcsBwPortPoolStatUBRConnRejRev": sfcsBwPortPoolStatUBRConnRejRev,
       "sfcsBwPortPoolStatUBRAllocBwFwd": sfcsBwPortPoolStatUBRAllocBwFwd,
       "sfcsBwPortPoolStatUBRAllocBwRev": sfcsBwPortPoolStatUBRAllocBwRev,
       "sfcsBwPortPoolStatUBRAggPCRFwd": sfcsBwPortPoolStatUBRAggPCRFwd,
       "sfcsBwPortPoolStatUBRAggPCRRev": sfcsBwPortPoolStatUBRAggPCRRev,
       "sfcsBwPortPoolStatUBRPrevAdverMAXCTD": sfcsBwPortPoolStatUBRPrevAdverMAXCTD,
       "sfcsBwPortPoolStatUBRPrevAdverCDV": sfcsBwPortPoolStatUBRPrevAdverCDV,
       "sfcsBwPortPoolTrapMgmtTable": sfcsBwPortPoolTrapMgmtTable,
       "sfcsBwPortPoolTrapMgmtEntry": sfcsBwPortPoolTrapMgmtEntry,
       "sfcsBwPortPoolTrapMgmtIndex": sfcsBwPortPoolTrapMgmtIndex,
       "sfcsBwPortPoolTrapMgmtPoolIndex": sfcsBwPortPoolTrapMgmtPoolIndex,
       "sfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd": sfcsBwPortPoolTrapMgmtAllocBwTholdHiFwd,
       "sfcsBwPortPoolTrapMgmtAllocBwTholdHiRev": sfcsBwPortPoolTrapMgmtAllocBwTholdHiRev,
       "sfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd": sfcsBwPortPoolTrapMgmtAllocBwTholdLoFwd,
       "sfcsBwPortPoolTrapMgmtAllocBwTholdLoRev": sfcsBwPortPoolTrapMgmtAllocBwTholdLoRev,
       "sfcsBwPortPoolTrapMgmtPeakBwTholdFwd": sfcsBwPortPoolTrapMgmtPeakBwTholdFwd,
       "sfcsBwPortPoolTrapMgmtPeakBwTholdRev": sfcsBwPortPoolTrapMgmtPeakBwTholdRev,
       "sfcsBwPortPoolTrapMgmtHoldDownTime": sfcsBwPortPoolTrapMgmtHoldDownTime,
       "sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd": sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiFwd,
       "sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev": sfcsBwPortPoolTrapMgmtCBRConnCntTholdHiRev,
       "sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd": sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoFwd,
       "sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev": sfcsBwPortPoolTrapMgmtCBRConnCntTholdLoRev,
       "sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd": sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiFwd,
       "sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev": sfcsBwPortPoolTrapMgmtCBRAllocBwTholdHiRev,
       "sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd": sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoFwd,
       "sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev": sfcsBwPortPoolTrapMgmtCBRAllocBwTholdLoRev,
       "sfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd": sfcsBwPortPoolTrapMgmtABRConnCntTholdHiFwd,
       "sfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev": sfcsBwPortPoolTrapMgmtABRConnCntTholdHiRev,
       "sfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd": sfcsBwPortPoolTrapMgmtABRConnCntTholdLoFwd,
       "sfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev": sfcsBwPortPoolTrapMgmtABRConnCntTholdLoRev,
       "sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd": sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiFwd,
       "sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev": sfcsBwPortPoolTrapMgmtABRAllocBwTholdHiRev,
       "sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd": sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoFwd,
       "sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev": sfcsBwPortPoolTrapMgmtABRAllocBwTholdLoRev,
       "sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd": sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiFwd,
       "sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev": sfcsBwPortPoolTrapMgmtVBRConnCntTholdHiRev,
       "sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd": sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoFwd,
       "sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev": sfcsBwPortPoolTrapMgmtVBRConnCntTholdLoRev,
       "sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd": sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiFwd,
       "sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev": sfcsBwPortPoolTrapMgmtVBRAllocBwTholdHiRev,
       "sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd": sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoFwd,
       "sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev": sfcsBwPortPoolTrapMgmtVBRAllocBwTholdLoRev,
       "sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd": sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiFwd,
       "sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev": sfcsBwPortPoolTrapMgmtUBRConnCntTholdHiRev,
       "sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd": sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoFwd,
       "sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev": sfcsBwPortPoolTrapMgmtUBRConnCntTholdLoRev,
       "sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd": sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiFwd,
       "sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev": sfcsBwPortPoolTrapMgmtUBRAllocBwTholdHiRev,
       "sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd": sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoFwd,
       "sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev": sfcsBwPortPoolTrapMgmtUBRAllocBwTholdLoRev,
       "sfcsBWPortPoolTrapMgmtBuffUpThold": sfcsBWPortPoolTrapMgmtBuffUpThold,
       "sfcsBWPortPoolTrapMgmtBuffLoThold": sfcsBWPortPoolTrapMgmtBuffLoThold,
       "sfcsBWPortPoolTrapMgmtConnRejThold": sfcsBWPortPoolTrapMgmtConnRejThold,
       "sfcsBuffPools": sfcsBuffPools,
       "sfcsBuffPrioTable": sfcsBuffPrioTable,
       "sfcsBuffPrioEntry": sfcsBuffPrioEntry,
       "sfcsBuffPrioPortIndex": sfcsBuffPrioPortIndex,
       "sfcsBuffPrioPriority": sfcsBuffPrioPriority,
       "sfcsBuffPrioAssignCtl": sfcsBuffPrioAssignCtl,
       "sfcsBuffPrioMinCtl": sfcsBuffPrioMinCtl,
       "sfcsBuffPrioAssigned": sfcsBuffPrioAssigned,
       "sfcsBuffPrioAllocated": sfcsBuffPrioAllocated,
       "sfcsBuffPrioAvailable": sfcsBuffPrioAvailable,
       "sfcsBuffPrioPeakAlloc": sfcsBuffPrioPeakAlloc,
       "sfcsBuffPrioConnRejs": sfcsBuffPrioConnRejs,
       "sfcsBuffPrioUpTholdTrap": sfcsBuffPrioUpTholdTrap,
       "sfcsBuffPrioLoTholdTrap": sfcsBuffPrioLoTholdTrap,
       "sfcsBuffPrioConnRejThold": sfcsBuffPrioConnRejThold,
       "sfcsProxy": sfcsProxy,
       "sfcsProxyConfig": sfcsProxyConfig,
       "sfcsProxyConfigTable": sfcsProxyConfigTable,
       "sfcsProxyConfigEntry": sfcsProxyConfigEntry,
       "sfcsProxyConfigANIMIndex": sfcsProxyConfigANIMIndex,
       "sfcsProxyConfigNUMPORTS": sfcsProxyConfigNUMPORTS,
       "sfcsProxyConfigTxMemSize": sfcsProxyConfigTxMemSize,
       "sfcsProxyConfigRxMaxPduSize": sfcsProxyConfigRxMaxPduSize,
       "sfcsProxyConfigBandWidth": sfcsProxyConfigBandWidth,
       "sfcsProxyConfigTransmitDone": sfcsProxyConfigTransmitDone,
       "sfcsProxyConfigReceiveFifoState": sfcsProxyConfigReceiveFifoState,
       "sfcsProxyConfigPortTransmitMode": sfcsProxyConfigPortTransmitMode,
       "sfcsProxyConfigReceiveFifoReset": sfcsProxyConfigReceiveFifoReset,
       "sfcsProxyConfigTxFifoReset": sfcsProxyConfigTxFifoReset,
       "sfcsProxyConfigReceiveMode": sfcsProxyConfigReceiveMode,
       "sfcsProxyConfigCaptureMode": sfcsProxyConfigCaptureMode,
       "sfcsProxyConfigInitPort": sfcsProxyConfigInitPort,
       "sfcsProxyConfigLoad": sfcsProxyConfigLoad,
       "sfcsProxyConfigGumbo": sfcsProxyConfigGumbo,
       "sfcsProxyTrans": sfcsProxyTrans,
       "sfcsProxyTransTable": sfcsProxyTransTable,
       "sfcsProxyTransEntry": sfcsProxyTransEntry,
       "sfcsProxyTransANIMIndex": sfcsProxyTransANIMIndex,
       "sfcsProxyTransEncodeNewPdu": sfcsProxyTransEncodeNewPdu,
       "sfcsProxyTransVPI": sfcsProxyTransVPI,
       "sfcsProxyTransVCI": sfcsProxyTransVCI,
       "sfcsProxyTransPTI": sfcsProxyTransPTI,
       "sfcsProxyTransCLP": sfcsProxyTransCLP,
       "sfcsProxyTransPayloadType": sfcsProxyTransPayloadType,
       "sfcsProxyTransPayloadLength": sfcsProxyTransPayloadLength,
       "sfcsProxyTransPayloadData": sfcsProxyTransPayloadData,
       "sfcsProxyTransCount": sfcsProxyTransCount,
       "sfcsProxyTransPayloadAdaptionLayer": sfcsProxyTransPayloadAdaptionLayer,
       "sfcsProxyTransMpxMethod": sfcsProxyTransMpxMethod,
       "sfcsProxyTransControl": sfcsProxyTransControl,
       "sfcsProxyTransGumbo": sfcsProxyTransGumbo,
       "sfcsProxyRead": sfcsProxyRead,
       "sfcsProxyReadTable": sfcsProxyReadTable,
       "sfcsProxyReadEntry": sfcsProxyReadEntry,
       "sfcsProxyReadANIMIndex": sfcsProxyReadANIMIndex,
       "sfcsProxyReadMode": sfcsProxyReadMode,
       "sfcsProxyReadNewPdu": sfcsProxyReadNewPdu,
       "sfcsProxyReadGumbo": sfcsProxyReadGumbo,
       "sfcsProxyReadVPI": sfcsProxyReadVPI,
       "sfcsProxyReadVCI": sfcsProxyReadVCI,
       "sfcsProxyReadPTI": sfcsProxyReadPTI,
       "sfcsProxyReadCLP": sfcsProxyReadCLP,
       "sfcsProxyReadDataLength": sfcsProxyReadDataLength,
       "sfcsProxyReadData": sfcsProxyReadData,
       "sfcsProxyReadPal": sfcsProxyReadPal,
       "sfcsProxyReadInbyteslosts": sfcsProxyReadInbyteslosts,
       "sfcsProxyReadInCells": sfcsProxyReadInCells,
       "sfcsProxyReadInError": sfcsProxyReadInError,
       "sfcsProxyReadInCellReadError": sfcsProxyReadInCellReadError,
       "sfcsProxyReadInHecError": sfcsProxyReadInHecError,
       "sfcsProxyReadInTooBigError": sfcsProxyReadInTooBigError,
       "sfcsProxyReadInCRCError": sfcsProxyReadInCRCError,
       "sfcsProxyReadInLengthMismatchError": sfcsProxyReadInLengthMismatchError,
       "sfcsProxyReadInTotalCells": sfcsProxyReadInTotalCells}
)
