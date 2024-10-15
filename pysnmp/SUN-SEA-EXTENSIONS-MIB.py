# SNMP MIB module (SUN-SEA-EXTENSIONS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUN-SEA-EXTENSIONS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:36 2024
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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(sunMIB,) = mibBuilder.importSymbols(
    "SUN-MIB",
    "sunMIB")


# MODULE-IDENTITY

sunSeaExtensionsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SunSystem_ObjectIdentity = ObjectIdentity
sunSystem = _SunSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 3, 1)
)


class _AgentDescr_Type(DisplayString):
    """Custom type agentDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentDescr_Type.__name__ = "DisplayString"
_AgentDescr_Object = MibScalar
agentDescr = _AgentDescr_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 1, 1),
    _AgentDescr_Type()
)
agentDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDescr.setStatus("mandatory")


class _HostID_Type(OctetString):
    """Custom type hostID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HostID_Type.__name__ = "OctetString"
_HostID_Object = MibScalar
hostID = _HostID_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 1, 2),
    _HostID_Type()
)
hostID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostID.setStatus("mandatory")


class _Motd_Type(DisplayString):
    """Custom type motd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Motd_Type.__name__ = "DisplayString"
_Motd_Object = MibScalar
motd = _Motd_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 1, 3),
    _Motd_Type()
)
motd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motd.setStatus("mandatory")
_UnixTime_Type = Counter32
_UnixTime_Object = MibScalar
unixTime = _UnixTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 1, 4),
    _UnixTime_Type()
)
unixTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unixTime.setStatus("mandatory")
_SunInterfaces_ObjectIdentity = ObjectIdentity
sunInterfaces = _SunInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 3, 2)
)
_SunAt_ObjectIdentity = ObjectIdentity
sunAt = _SunAt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 3, 3)
)
_SunIp_ObjectIdentity = ObjectIdentity
sunIp = _SunIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 3, 4)
)
_SunIcmp_ObjectIdentity = ObjectIdentity
sunIcmp = _SunIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 3, 5)
)
_SunTcp_ObjectIdentity = ObjectIdentity
sunTcp = _SunTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 3, 6)
)
_SunUdp_ObjectIdentity = ObjectIdentity
sunUdp = _SunUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 3, 7)
)
_SunSnmp_ObjectIdentity = ObjectIdentity
sunSnmp = _SunSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 3, 11)
)
_SunProcesses_ObjectIdentity = ObjectIdentity
sunProcesses = _SunProcesses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 3, 12)
)
_SunProcessTable_Object = MibTable
sunProcessTable = _SunProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1)
)
if mibBuilder.loadTexts:
    sunProcessTable.setStatus("mandatory")
_PsEntry_Object = MibTableRow
psEntry = _PsEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1)
)
psEntry.setIndexNames(
    (0, "SUN-SEA-EXTENSIONS-MIB", "psProcessID"),
)
if mibBuilder.loadTexts:
    psEntry.setStatus("mandatory")
_PsProcessID_Type = Integer32
_PsProcessID_Object = MibTableColumn
psProcessID = _PsProcessID_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 1),
    _PsProcessID_Type()
)
psProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProcessID.setStatus("mandatory")
_PsParentProcessID_Type = Integer32
_PsParentProcessID_Object = MibTableColumn
psParentProcessID = _PsParentProcessID_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 2),
    _PsParentProcessID_Type()
)
psParentProcessID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psParentProcessID.setStatus("mandatory")
_PsProcessSize_Type = Integer32
_PsProcessSize_Object = MibTableColumn
psProcessSize = _PsProcessSize_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 3),
    _PsProcessSize_Type()
)
psProcessSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProcessSize.setStatus("mandatory")
_PsProcessCpuTime_Type = Integer32
_PsProcessCpuTime_Object = MibTableColumn
psProcessCpuTime = _PsProcessCpuTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 4),
    _PsProcessCpuTime_Type()
)
psProcessCpuTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProcessCpuTime.setStatus("mandatory")


class _PsProcessState_Type(DisplayString):
    """Custom type psProcessState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PsProcessState_Type.__name__ = "DisplayString"
_PsProcessState_Object = MibTableColumn
psProcessState = _PsProcessState_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 5),
    _PsProcessState_Type()
)
psProcessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProcessState.setStatus("mandatory")


class _PsProcessWaitChannel_Type(DisplayString):
    """Custom type psProcessWaitChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PsProcessWaitChannel_Type.__name__ = "DisplayString"
_PsProcessWaitChannel_Object = MibTableColumn
psProcessWaitChannel = _PsProcessWaitChannel_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 6),
    _PsProcessWaitChannel_Type()
)
psProcessWaitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProcessWaitChannel.setStatus("mandatory")


class _PsProcessTTY_Type(DisplayString):
    """Custom type psProcessTTY based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PsProcessTTY_Type.__name__ = "DisplayString"
_PsProcessTTY_Object = MibTableColumn
psProcessTTY = _PsProcessTTY_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 7),
    _PsProcessTTY_Type()
)
psProcessTTY.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProcessTTY.setStatus("mandatory")


class _PsProcessUserName_Type(DisplayString):
    """Custom type psProcessUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PsProcessUserName_Type.__name__ = "DisplayString"
_PsProcessUserName_Object = MibTableColumn
psProcessUserName = _PsProcessUserName_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 8),
    _PsProcessUserName_Type()
)
psProcessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProcessUserName.setStatus("mandatory")
_PsProcessUserID_Type = Integer32
_PsProcessUserID_Object = MibTableColumn
psProcessUserID = _PsProcessUserID_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 9),
    _PsProcessUserID_Type()
)
psProcessUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProcessUserID.setStatus("mandatory")


class _PsProcessName_Type(DisplayString):
    """Custom type psProcessName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PsProcessName_Type.__name__ = "DisplayString"
_PsProcessName_Object = MibTableColumn
psProcessName = _PsProcessName_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 10),
    _PsProcessName_Type()
)
psProcessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psProcessName.setStatus("mandatory")
_PsProcessStatus_Type = Integer32
_PsProcessStatus_Object = MibTableColumn
psProcessStatus = _PsProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 12, 1, 1, 11),
    _PsProcessStatus_Type()
)
psProcessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    psProcessStatus.setStatus("mandatory")
_SunHostPerf_ObjectIdentity = ObjectIdentity
sunHostPerf = _SunHostPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 3, 13)
)
_RsUserProcessTime_Type = Counter32
_RsUserProcessTime_Object = MibScalar
rsUserProcessTime = _RsUserProcessTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 1),
    _RsUserProcessTime_Type()
)
rsUserProcessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsUserProcessTime.setStatus("mandatory")
_RsNiceModeTime_Type = Counter32
_RsNiceModeTime_Object = MibScalar
rsNiceModeTime = _RsNiceModeTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 2),
    _RsNiceModeTime_Type()
)
rsNiceModeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsNiceModeTime.setStatus("mandatory")
_RsSystemProcessTime_Type = Counter32
_RsSystemProcessTime_Object = MibScalar
rsSystemProcessTime = _RsSystemProcessTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 3),
    _RsSystemProcessTime_Type()
)
rsSystemProcessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsSystemProcessTime.setStatus("mandatory")
_RsIdleModeTime_Type = Counter32
_RsIdleModeTime_Object = MibScalar
rsIdleModeTime = _RsIdleModeTime_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 4),
    _RsIdleModeTime_Type()
)
rsIdleModeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIdleModeTime.setStatus("mandatory")
_RsDiskXfer1_Type = Counter32
_RsDiskXfer1_Object = MibScalar
rsDiskXfer1 = _RsDiskXfer1_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 5),
    _RsDiskXfer1_Type()
)
rsDiskXfer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDiskXfer1.setStatus("mandatory")
_RsDiskXfer2_Type = Counter32
_RsDiskXfer2_Object = MibScalar
rsDiskXfer2 = _RsDiskXfer2_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 6),
    _RsDiskXfer2_Type()
)
rsDiskXfer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDiskXfer2.setStatus("mandatory")
_RsDiskXfer3_Type = Counter32
_RsDiskXfer3_Object = MibScalar
rsDiskXfer3 = _RsDiskXfer3_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 7),
    _RsDiskXfer3_Type()
)
rsDiskXfer3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDiskXfer3.setStatus("mandatory")
_RsDiskXfer4_Type = Counter32
_RsDiskXfer4_Object = MibScalar
rsDiskXfer4 = _RsDiskXfer4_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 8),
    _RsDiskXfer4_Type()
)
rsDiskXfer4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsDiskXfer4.setStatus("mandatory")
_RsVPagesIn_Type = Counter32
_RsVPagesIn_Object = MibScalar
rsVPagesIn = _RsVPagesIn_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 9),
    _RsVPagesIn_Type()
)
rsVPagesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVPagesIn.setStatus("mandatory")
_RsVPagesOut_Type = Counter32
_RsVPagesOut_Object = MibScalar
rsVPagesOut = _RsVPagesOut_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 10),
    _RsVPagesOut_Type()
)
rsVPagesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVPagesOut.setStatus("mandatory")
_RsVSwapIn_Type = Counter32
_RsVSwapIn_Object = MibScalar
rsVSwapIn = _RsVSwapIn_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 11),
    _RsVSwapIn_Type()
)
rsVSwapIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVSwapIn.setStatus("mandatory")
_RsVSwapOut_Type = Counter32
_RsVSwapOut_Object = MibScalar
rsVSwapOut = _RsVSwapOut_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 12),
    _RsVSwapOut_Type()
)
rsVSwapOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVSwapOut.setStatus("mandatory")
_RsVIntr_Type = Counter32
_RsVIntr_Object = MibScalar
rsVIntr = _RsVIntr_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 13),
    _RsVIntr_Type()
)
rsVIntr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsVIntr.setStatus("mandatory")
_RsIfInPackets_Type = Counter32
_RsIfInPackets_Object = MibScalar
rsIfInPackets = _RsIfInPackets_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 14),
    _RsIfInPackets_Type()
)
rsIfInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInPackets.setStatus("mandatory")
_RsIfOutPackets_Type = Counter32
_RsIfOutPackets_Object = MibScalar
rsIfOutPackets = _RsIfOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 15),
    _RsIfOutPackets_Type()
)
rsIfOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfOutPackets.setStatus("mandatory")
_RsIfInErrors_Type = Counter32
_RsIfInErrors_Object = MibScalar
rsIfInErrors = _RsIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 16),
    _RsIfInErrors_Type()
)
rsIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfInErrors.setStatus("mandatory")
_RsIfOutErrors_Type = Counter32
_RsIfOutErrors_Object = MibScalar
rsIfOutErrors = _RsIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 17),
    _RsIfOutErrors_Type()
)
rsIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfOutErrors.setStatus("mandatory")
_RsIfCollisions_Type = Counter32
_RsIfCollisions_Object = MibScalar
rsIfCollisions = _RsIfCollisions_Object(
    (1, 3, 6, 1, 4, 1, 42, 3, 13, 18),
    _RsIfCollisions_Type()
)
rsIfCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsIfCollisions.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUN-SEA-EXTENSIONS-MIB",
    **{"sunSeaExtensionsMIB": sunSeaExtensionsMIB,
       "sunSystem": sunSystem,
       "agentDescr": agentDescr,
       "hostID": hostID,
       "motd": motd,
       "unixTime": unixTime,
       "sunInterfaces": sunInterfaces,
       "sunAt": sunAt,
       "sunIp": sunIp,
       "sunIcmp": sunIcmp,
       "sunTcp": sunTcp,
       "sunUdp": sunUdp,
       "sunSnmp": sunSnmp,
       "sunProcesses": sunProcesses,
       "sunProcessTable": sunProcessTable,
       "psEntry": psEntry,
       "psProcessID": psProcessID,
       "psParentProcessID": psParentProcessID,
       "psProcessSize": psProcessSize,
       "psProcessCpuTime": psProcessCpuTime,
       "psProcessState": psProcessState,
       "psProcessWaitChannel": psProcessWaitChannel,
       "psProcessTTY": psProcessTTY,
       "psProcessUserName": psProcessUserName,
       "psProcessUserID": psProcessUserID,
       "psProcessName": psProcessName,
       "psProcessStatus": psProcessStatus,
       "sunHostPerf": sunHostPerf,
       "rsUserProcessTime": rsUserProcessTime,
       "rsNiceModeTime": rsNiceModeTime,
       "rsSystemProcessTime": rsSystemProcessTime,
       "rsIdleModeTime": rsIdleModeTime,
       "rsDiskXfer1": rsDiskXfer1,
       "rsDiskXfer2": rsDiskXfer2,
       "rsDiskXfer3": rsDiskXfer3,
       "rsDiskXfer4": rsDiskXfer4,
       "rsVPagesIn": rsVPagesIn,
       "rsVPagesOut": rsVPagesOut,
       "rsVSwapIn": rsVSwapIn,
       "rsVSwapOut": rsVSwapOut,
       "rsVIntr": rsVIntr,
       "rsIfInPackets": rsIfInPackets,
       "rsIfOutPackets": rsIfOutPackets,
       "rsIfInErrors": rsIfInErrors,
       "rsIfOutErrors": rsIfOutErrors,
       "rsIfCollisions": rsIfCollisions}
)
