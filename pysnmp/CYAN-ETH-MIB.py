# SNMP MIB module (CYAN-ETH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CYAN-ETH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:21:07 2024
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

(cyanEntityModules,) = mibBuilder.importSymbols(
    "CYAN-MIB",
    "cyanEntityModules")

(CyanAdminStateTc,
 CyanEnDisabledTc,
 CyanFppSubTypeTc,
 CyanFppTypeTc,
 CyanOpStateQualTc,
 CyanOpStateTc,
 CyanSecServiceStateTc) = mibBuilder.importSymbols(
    "CYAN-TC-MIB",
    "CyanAdminStateTc",
    "CyanEnDisabledTc",
    "CyanFppSubTypeTc",
    "CyanFppTypeTc",
    "CyanOpStateQualTc",
    "CyanOpStateTc",
    "CyanSecServiceStateTc")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

cyanEthModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180)
)
cyanEthModule.setRevisions(
        ("2014-12-07 05:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CyanEthMibObjects_ObjectIdentity = ObjectIdentity
cyanEthMibObjects = _CyanEthMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1)
)
_CyanEthTable_Object = MibTable
cyanEthTable = _CyanEthTable_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1)
)
if mibBuilder.loadTexts:
    cyanEthTable.setStatus("current")
_CyanEthEntry_Object = MibTableRow
cyanEthEntry = _CyanEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1)
)
cyanEthEntry.setIndexNames(
    (0, "CYAN-ETH-MIB", "cyanEthShelfId"),
    (0, "CYAN-ETH-MIB", "cyanEthModuleId"),
    (0, "CYAN-ETH-MIB", "cyanEthEthTermId"),
)
if mibBuilder.loadTexts:
    cyanEthEntry.setStatus("current")


class _CyanEthShelfId_Type(Unsigned32):
    """Custom type cyanEthShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CyanEthShelfId_Type.__name__ = "Unsigned32"
_CyanEthShelfId_Object = MibTableColumn
cyanEthShelfId = _CyanEthShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 1),
    _CyanEthShelfId_Type()
)
cyanEthShelfId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanEthShelfId.setStatus("current")
_CyanEthModuleId_Type = Unsigned32
_CyanEthModuleId_Object = MibTableColumn
cyanEthModuleId = _CyanEthModuleId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 2),
    _CyanEthModuleId_Type()
)
cyanEthModuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanEthModuleId.setStatus("current")
_CyanEthEthTermId_Type = Unsigned32
_CyanEthEthTermId_Object = MibTableColumn
cyanEthEthTermId = _CyanEthEthTermId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 3),
    _CyanEthEthTermId_Type()
)
cyanEthEthTermId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cyanEthEthTermId.setStatus("current")
_CyanEthAdminState_Type = CyanAdminStateTc
_CyanEthAdminState_Object = MibTableColumn
cyanEthAdminState = _CyanEthAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 4),
    _CyanEthAdminState_Type()
)
cyanEthAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthAdminState.setStatus("current")
_CyanEthAutoinserviceSoakTimeSec_Type = Integer32
_CyanEthAutoinserviceSoakTimeSec_Object = MibTableColumn
cyanEthAutoinserviceSoakTimeSec = _CyanEthAutoinserviceSoakTimeSec_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 5),
    _CyanEthAutoinserviceSoakTimeSec_Type()
)
cyanEthAutoinserviceSoakTimeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthAutoinserviceSoakTimeSec.setStatus("current")


class _CyanEthFarEndPtpId_Type(Unsigned32):
    """Custom type cyanEthFarEndPtpId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CyanEthFarEndPtpId_Type.__name__ = "Unsigned32"
_CyanEthFarEndPtpId_Object = MibTableColumn
cyanEthFarEndPtpId = _CyanEthFarEndPtpId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 6),
    _CyanEthFarEndPtpId_Type()
)
cyanEthFarEndPtpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthFarEndPtpId.setStatus("current")


class _CyanEthFarEndShelfId_Type(Unsigned32):
    """Custom type cyanEthFarEndShelfId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CyanEthFarEndShelfId_Type.__name__ = "Unsigned32"
_CyanEthFarEndShelfId_Object = MibTableColumn
cyanEthFarEndShelfId = _CyanEthFarEndShelfId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 7),
    _CyanEthFarEndShelfId_Type()
)
cyanEthFarEndShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthFarEndShelfId.setStatus("current")


class _CyanEthFarEndSlotId_Type(Unsigned32):
    """Custom type cyanEthFarEndSlotId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CyanEthFarEndSlotId_Type.__name__ = "Unsigned32"
_CyanEthFarEndSlotId_Object = MibTableColumn
cyanEthFarEndSlotId = _CyanEthFarEndSlotId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 8),
    _CyanEthFarEndSlotId_Type()
)
cyanEthFarEndSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthFarEndSlotId.setStatus("current")
_CyanEthFarEndSystemId_Type = Unsigned32
_CyanEthFarEndSystemId_Object = MibTableColumn
cyanEthFarEndSystemId = _CyanEthFarEndSystemId_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 9),
    _CyanEthFarEndSystemId_Type()
)
cyanEthFarEndSystemId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthFarEndSystemId.setStatus("current")
_CyanEthFlowPointPoolSubtype_Type = CyanFppSubTypeTc
_CyanEthFlowPointPoolSubtype_Object = MibTableColumn
cyanEthFlowPointPoolSubtype = _CyanEthFlowPointPoolSubtype_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 10),
    _CyanEthFlowPointPoolSubtype_Type()
)
cyanEthFlowPointPoolSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthFlowPointPoolSubtype.setStatus("current")
_CyanEthFppType_Type = CyanFppTypeTc
_CyanEthFppType_Object = MibTableColumn
cyanEthFppType = _CyanEthFppType_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 11),
    _CyanEthFppType_Type()
)
cyanEthFppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthFppType.setStatus("current")
_CyanEthIpForwarding_Type = CyanEnDisabledTc
_CyanEthIpForwarding_Object = MibTableColumn
cyanEthIpForwarding = _CyanEthIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 12),
    _CyanEthIpForwarding_Type()
)
cyanEthIpForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthIpForwarding.setStatus("current")
_CyanEthLinkOamEnableState_Type = CyanEnDisabledTc
_CyanEthLinkOamEnableState_Object = MibTableColumn
cyanEthLinkOamEnableState = _CyanEthLinkOamEnableState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 13),
    _CyanEthLinkOamEnableState_Type()
)
cyanEthLinkOamEnableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthLinkOamEnableState.setStatus("current")
_CyanEthOperState_Type = CyanOpStateTc
_CyanEthOperState_Object = MibTableColumn
cyanEthOperState = _CyanEthOperState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 14),
    _CyanEthOperState_Type()
)
cyanEthOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthOperState.setStatus("current")
_CyanEthOperStateQual_Type = CyanOpStateQualTc
_CyanEthOperStateQual_Object = MibTableColumn
cyanEthOperStateQual = _CyanEthOperStateQual_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 15),
    _CyanEthOperStateQual_Type()
)
cyanEthOperStateQual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthOperStateQual.setStatus("current")
_CyanEthPortSpeedMbps_Type = Unsigned32
_CyanEthPortSpeedMbps_Object = MibTableColumn
cyanEthPortSpeedMbps = _CyanEthPortSpeedMbps_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 16),
    _CyanEthPortSpeedMbps_Type()
)
cyanEthPortSpeedMbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthPortSpeedMbps.setStatus("current")
_CyanEthRouting_Type = CyanEnDisabledTc
_CyanEthRouting_Object = MibTableColumn
cyanEthRouting = _CyanEthRouting_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 17),
    _CyanEthRouting_Type()
)
cyanEthRouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthRouting.setStatus("current")
_CyanEthSecServState_Type = CyanSecServiceStateTc
_CyanEthSecServState_Object = MibTableColumn
cyanEthSecServState = _CyanEthSecServState_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 18),
    _CyanEthSecServState_Type()
)
cyanEthSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthSecServState.setStatus("current")
_CyanEthTopologyDiscovery_Type = CyanEnDisabledTc
_CyanEthTopologyDiscovery_Object = MibTableColumn
cyanEthTopologyDiscovery = _CyanEthTopologyDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 1, 1, 1, 19),
    _CyanEthTopologyDiscovery_Type()
)
cyanEthTopologyDiscovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cyanEthTopologyDiscovery.setStatus("current")

# Managed Objects groups

cyanEthObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 20)
)
cyanEthObjectGroup.setObjects(
      *(("CYAN-ETH-MIB", "cyanEthAdminState"),
        ("CYAN-ETH-MIB", "cyanEthAutoinserviceSoakTimeSec"),
        ("CYAN-ETH-MIB", "cyanEthFarEndPtpId"),
        ("CYAN-ETH-MIB", "cyanEthFarEndShelfId"),
        ("CYAN-ETH-MIB", "cyanEthFarEndSlotId"),
        ("CYAN-ETH-MIB", "cyanEthFarEndSystemId"),
        ("CYAN-ETH-MIB", "cyanEthFlowPointPoolSubtype"),
        ("CYAN-ETH-MIB", "cyanEthFppType"),
        ("CYAN-ETH-MIB", "cyanEthIpForwarding"),
        ("CYAN-ETH-MIB", "cyanEthLinkOamEnableState"),
        ("CYAN-ETH-MIB", "cyanEthOperState"),
        ("CYAN-ETH-MIB", "cyanEthOperStateQual"),
        ("CYAN-ETH-MIB", "cyanEthPortSpeedMbps"),
        ("CYAN-ETH-MIB", "cyanEthRouting"),
        ("CYAN-ETH-MIB", "cyanEthSecServState"),
        ("CYAN-ETH-MIB", "cyanEthTopologyDiscovery"))
)
if mibBuilder.loadTexts:
    cyanEthObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cyanEthCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 28533, 5, 30, 180, 30)
)
if mibBuilder.loadTexts:
    cyanEthCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CYAN-ETH-MIB",
    **{"cyanEthModule": cyanEthModule,
       "cyanEthMibObjects": cyanEthMibObjects,
       "cyanEthTable": cyanEthTable,
       "cyanEthEntry": cyanEthEntry,
       "cyanEthShelfId": cyanEthShelfId,
       "cyanEthModuleId": cyanEthModuleId,
       "cyanEthEthTermId": cyanEthEthTermId,
       "cyanEthAdminState": cyanEthAdminState,
       "cyanEthAutoinserviceSoakTimeSec": cyanEthAutoinserviceSoakTimeSec,
       "cyanEthFarEndPtpId": cyanEthFarEndPtpId,
       "cyanEthFarEndShelfId": cyanEthFarEndShelfId,
       "cyanEthFarEndSlotId": cyanEthFarEndSlotId,
       "cyanEthFarEndSystemId": cyanEthFarEndSystemId,
       "cyanEthFlowPointPoolSubtype": cyanEthFlowPointPoolSubtype,
       "cyanEthFppType": cyanEthFppType,
       "cyanEthIpForwarding": cyanEthIpForwarding,
       "cyanEthLinkOamEnableState": cyanEthLinkOamEnableState,
       "cyanEthOperState": cyanEthOperState,
       "cyanEthOperStateQual": cyanEthOperStateQual,
       "cyanEthPortSpeedMbps": cyanEthPortSpeedMbps,
       "cyanEthRouting": cyanEthRouting,
       "cyanEthSecServState": cyanEthSecServState,
       "cyanEthTopologyDiscovery": cyanEthTopologyDiscovery,
       "cyanEthObjectGroup": cyanEthObjectGroup,
       "cyanEthCompliance": cyanEthCompliance}
)
