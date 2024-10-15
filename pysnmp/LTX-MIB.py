# SNMP MIB module (LTX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LTX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:28 2024
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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class OwnerString(DisplayString):
    """Custom type OwnerString based on DisplayString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ltx_ObjectIdentity = ObjectIdentity
ltx = _Ltx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244)
)
_Ltxlna_ObjectIdentity = ObjectIdentity
ltxlna = _Ltxlna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 10)
)
_Ltxlrp_ObjectIdentity = ObjectIdentity
ltxlrp = _Ltxlrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11)
)
_LtxLRPCommInfo_ObjectIdentity = ObjectIdentity
ltxLRPCommInfo = _LtxLRPCommInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 1)
)
_CommInfoTable_Object = MibTable
commInfoTable = _CommInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 1, 1)
)
if mibBuilder.loadTexts:
    commInfoTable.setStatus("mandatory")
_CommInfoEntry_Object = MibTableRow
commInfoEntry = _CommInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 1, 1, 1)
)
commInfoEntry.setIndexNames(
    (0, "LTX-MIB", "commInfoIndex"),
)
if mibBuilder.loadTexts:
    commInfoEntry.setStatus("mandatory")


class _CommInfoIndex_Type(Integer32):
    """Custom type commInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CommInfoIndex_Type.__name__ = "Integer32"
_CommInfoIndex_Object = MibTableColumn
commInfoIndex = _CommInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 1, 1, 1, 1),
    _CommInfoIndex_Type()
)
commInfoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commInfoIndex.setStatus("mandatory")
_CommInfoName_Type = DisplayString
_CommInfoName_Object = MibTableColumn
commInfoName = _CommInfoName_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 1, 1, 1, 2),
    _CommInfoName_Type()
)
commInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commInfoName.setStatus("mandatory")
_CommInfoGet_Type = Integer32
_CommInfoGet_Object = MibTableColumn
commInfoGet = _CommInfoGet_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 1, 1, 1, 3),
    _CommInfoGet_Type()
)
commInfoGet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commInfoGet.setStatus("mandatory")
_CommInfoSet_Type = Integer32
_CommInfoSet_Object = MibTableColumn
commInfoSet = _CommInfoSet_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 1, 1, 1, 4),
    _CommInfoSet_Type()
)
commInfoSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commInfoSet.setStatus("mandatory")
_CommInfoTrap_Type = Integer32
_CommInfoTrap_Object = MibTableColumn
commInfoTrap = _CommInfoTrap_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 1, 1, 1, 5),
    _CommInfoTrap_Type()
)
commInfoTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commInfoTrap.setStatus("mandatory")
_LtxLRPHostInfo_ObjectIdentity = ObjectIdentity
ltxLRPHostInfo = _LtxLRPHostInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 2)
)
_HostInfoTable_Object = MibTable
hostInfoTable = _HostInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 2, 1)
)
if mibBuilder.loadTexts:
    hostInfoTable.setStatus("mandatory")
_HostInfoEntry_Object = MibTableRow
hostInfoEntry = _HostInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 2, 1, 1)
)
hostInfoEntry.setIndexNames(
    (0, "LTX-MIB", "hostInfoIndex"),
)
if mibBuilder.loadTexts:
    hostInfoEntry.setStatus("mandatory")


class _HostInfoIndex_Type(Integer32):
    """Custom type hostInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HostInfoIndex_Type.__name__ = "Integer32"
_HostInfoIndex_Object = MibTableColumn
hostInfoIndex = _HostInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 2, 1, 1, 1),
    _HostInfoIndex_Type()
)
hostInfoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostInfoIndex.setStatus("mandatory")
_HostInfoName_Type = DisplayString
_HostInfoName_Object = MibTableColumn
hostInfoName = _HostInfoName_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 2, 1, 1, 2),
    _HostInfoName_Type()
)
hostInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostInfoName.setStatus("mandatory")
_HostInfoIP_Type = IpAddress
_HostInfoIP_Object = MibTableColumn
hostInfoIP = _HostInfoIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 2, 1, 1, 3),
    _HostInfoIP_Type()
)
hostInfoIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostInfoIP.setStatus("mandatory")
_HostInfoComm_Type = DisplayString
_HostInfoComm_Object = MibTableColumn
hostInfoComm = _HostInfoComm_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 2, 1, 1, 4),
    _HostInfoComm_Type()
)
hostInfoComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostInfoComm.setStatus("mandatory")
_LtxLRPGroupInfo_ObjectIdentity = ObjectIdentity
ltxLRPGroupInfo = _LtxLRPGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 3)
)
_GroupInfoTable_Object = MibTable
groupInfoTable = _GroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 3, 1)
)
if mibBuilder.loadTexts:
    groupInfoTable.setStatus("mandatory")
_GroupInfoEntry_Object = MibTableRow
groupInfoEntry = _GroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 3, 1, 1)
)
groupInfoEntry.setIndexNames(
    (0, "LTX-MIB", "groupInfoIndex"),
)
if mibBuilder.loadTexts:
    groupInfoEntry.setStatus("mandatory")


class _GroupInfoIndex_Type(Integer32):
    """Custom type groupInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GroupInfoIndex_Type.__name__ = "Integer32"
_GroupInfoIndex_Object = MibTableColumn
groupInfoIndex = _GroupInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 3, 1, 1, 1),
    _GroupInfoIndex_Type()
)
groupInfoIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupInfoIndex.setStatus("mandatory")
_GroupInfoCapFilt_Type = Integer32
_GroupInfoCapFilt_Object = MibTableColumn
groupInfoCapFilt = _GroupInfoCapFilt_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 3, 1, 1, 2),
    _GroupInfoCapFilt_Type()
)
groupInfoCapFilt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupInfoCapFilt.setStatus("mandatory")
_GroupInfoHostTopN_Type = Integer32
_GroupInfoHostTopN_Object = MibTableColumn
groupInfoHostTopN = _GroupInfoHostTopN_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 3, 1, 1, 3),
    _GroupInfoHostTopN_Type()
)
groupInfoHostTopN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupInfoHostTopN.setStatus("mandatory")
_GroupInfoMatrix_Type = Integer32
_GroupInfoMatrix_Object = MibTableColumn
groupInfoMatrix = _GroupInfoMatrix_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 3, 1, 1, 4),
    _GroupInfoMatrix_Type()
)
groupInfoMatrix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    groupInfoMatrix.setStatus("mandatory")
_LtxLRPMaxInfo_ObjectIdentity = ObjectIdentity
ltxLRPMaxInfo = _LtxLRPMaxInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 4)
)


class _MaxHTS_Type(Integer32):
    """Custom type maxHTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_MaxHTS_Type.__name__ = "Integer32"
_MaxHTS_Object = MibScalar
maxHTS = _MaxHTS_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 4, 1),
    _MaxHTS_Type()
)
maxHTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxHTS.setStatus("mandatory")


class _MaxMTS_Type(Integer32):
    """Custom type maxMTS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_MaxMTS_Type.__name__ = "Integer32"
_MaxMTS_Object = MibScalar
maxMTS = _MaxMTS_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 4, 2),
    _MaxMTS_Type()
)
maxMTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxMTS.setStatus("mandatory")


class _MaxBuckets_Type(Integer32):
    """Custom type maxBuckets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_MaxBuckets_Type.__name__ = "Integer32"
_MaxBuckets_Object = MibScalar
maxBuckets = _MaxBuckets_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 4, 3),
    _MaxBuckets_Type()
)
maxBuckets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxBuckets.setStatus("mandatory")


class _MaxLogs_Type(Integer32):
    """Custom type maxLogs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_MaxLogs_Type.__name__ = "Integer32"
_MaxLogs_Object = MibScalar
maxLogs = _MaxLogs_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 4, 4),
    _MaxLogs_Type()
)
maxLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxLogs.setStatus("mandatory")


class _MaxTopN_Type(Integer32):
    """Custom type maxTopN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_MaxTopN_Type.__name__ = "Integer32"
_MaxTopN_Object = MibScalar
maxTopN = _MaxTopN_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 4, 5),
    _MaxTopN_Type()
)
maxTopN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxTopN.setStatus("mandatory")


class _MaxBuff_Type(Integer32):
    """Custom type maxBuff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_MaxBuff_Type.__name__ = "Integer32"
_MaxBuff_Object = MibScalar
maxBuff = _MaxBuff_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 4, 6),
    _MaxBuff_Type()
)
maxBuff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxBuff.setStatus("mandatory")
_LtxLRPRoverInfo_ObjectIdentity = ObjectIdentity
ltxLRPRoverInfo = _LtxLRPRoverInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 5)
)
_RoverControl_Type = Integer32
_RoverControl_Object = MibScalar
roverControl = _RoverControl_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 1),
    _RoverControl_Type()
)
roverControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverControl.setStatus("mandatory")
_RoverSeconds_Type = Counter32
_RoverSeconds_Object = MibScalar
roverSeconds = _RoverSeconds_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 2),
    _RoverSeconds_Type()
)
roverSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverSeconds.setStatus("mandatory")
_RoverTErrs_Type = Counter32
_RoverTErrs_Object = MibScalar
roverTErrs = _RoverTErrs_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 3),
    _RoverTErrs_Type()
)
roverTErrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverTErrs.setStatus("mandatory")
_RoverBPS_Type = Counter32
_RoverBPS_Object = MibScalar
roverBPS = _RoverBPS_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 4),
    _RoverBPS_Type()
)
roverBPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverBPS.setStatus("mandatory")
_RoverEPS_Type = Counter32
_RoverEPS_Object = MibScalar
roverEPS = _RoverEPS_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 5),
    _RoverEPS_Type()
)
roverEPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverEPS.setStatus("mandatory")
_RoverPPS_Type = Counter32
_RoverPPS_Object = MibScalar
roverPPS = _RoverPPS_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 6),
    _RoverPPS_Type()
)
roverPPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverPPS.setStatus("mandatory")
_RoverUtil_Type = Counter32
_RoverUtil_Object = MibScalar
roverUtil = _RoverUtil_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 7),
    _RoverUtil_Type()
)
roverUtil.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverUtil.setStatus("mandatory")
_RoverTCRC_Type = Counter32
_RoverTCRC_Object = MibScalar
roverTCRC = _RoverTCRC_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 8),
    _RoverTCRC_Type()
)
roverTCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverTCRC.setStatus("mandatory")
_RoverTRunt_Type = Counter32
_RoverTRunt_Object = MibScalar
roverTRunt = _RoverTRunt_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 9),
    _RoverTRunt_Type()
)
roverTRunt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverTRunt.setStatus("mandatory")
_RoverTGiant_Type = Counter32
_RoverTGiant_Object = MibScalar
roverTGiant = _RoverTGiant_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 10),
    _RoverTGiant_Type()
)
roverTGiant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverTGiant.setStatus("mandatory")
_RoverTColl_Type = Counter32
_RoverTColl_Object = MibScalar
roverTColl = _RoverTColl_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 11),
    _RoverTColl_Type()
)
roverTColl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverTColl.setStatus("mandatory")
_RoverTJabb_Type = Counter32
_RoverTJabb_Object = MibScalar
roverTJabb = _RoverTJabb_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 5, 12),
    _RoverTJabb_Type()
)
roverTJabb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    roverTJabb.setStatus("mandatory")
_LtxLRPMiscInfo_ObjectIdentity = ObjectIdentity
ltxLRPMiscInfo = _LtxLRPMiscInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 6)
)
_MiscInfoPortTable_Object = MibTable
miscInfoPortTable = _MiscInfoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 1)
)
if mibBuilder.loadTexts:
    miscInfoPortTable.setStatus("mandatory")
_MiscInfoPortEntry_Object = MibTableRow
miscInfoPortEntry = _MiscInfoPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 1, 1)
)
miscInfoPortEntry.setIndexNames(
    (0, "LTX-MIB", "miscInfoPortIndex"),
)
if mibBuilder.loadTexts:
    miscInfoPortEntry.setStatus("mandatory")


class _MiscInfoPortIndex_Type(Integer32):
    """Custom type miscInfoPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_MiscInfoPortIndex_Type.__name__ = "Integer32"
_MiscInfoPortIndex_Object = MibTableColumn
miscInfoPortIndex = _MiscInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 1, 1, 1),
    _MiscInfoPortIndex_Type()
)
miscInfoPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoPortIndex.setStatus("mandatory")
_MiscInfoPortName_Type = DisplayString
_MiscInfoPortName_Object = MibTableColumn
miscInfoPortName = _MiscInfoPortName_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 1, 1, 2),
    _MiscInfoPortName_Type()
)
miscInfoPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoPortName.setStatus("mandatory")
_MiscInfoPortIP_Type = IpAddress
_MiscInfoPortIP_Object = MibTableColumn
miscInfoPortIP = _MiscInfoPortIP_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 1, 1, 3),
    _MiscInfoPortIP_Type()
)
miscInfoPortIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoPortIP.setStatus("mandatory")
_MiscInfoPortMask_Type = IpAddress
_MiscInfoPortMask_Object = MibTableColumn
miscInfoPortMask = _MiscInfoPortMask_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 1, 1, 4),
    _MiscInfoPortMask_Type()
)
miscInfoPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoPortMask.setStatus("mandatory")
_MiscInfoDate_Type = DisplayString
_MiscInfoDate_Object = MibScalar
miscInfoDate = _MiscInfoDate_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 2),
    _MiscInfoDate_Type()
)
miscInfoDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoDate.setStatus("mandatory")
_MiscInfoTMO_Type = Integer32
_MiscInfoTMO_Object = MibScalar
miscInfoTMO = _MiscInfoTMO_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 3),
    _MiscInfoTMO_Type()
)
miscInfoTMO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoTMO.setStatus("mandatory")
_MiscInfoRefresh_Type = Integer32
_MiscInfoRefresh_Object = MibScalar
miscInfoRefresh = _MiscInfoRefresh_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 4),
    _MiscInfoRefresh_Type()
)
miscInfoRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoRefresh.setStatus("mandatory")
_MiscInfoBaud_Type = Integer32
_MiscInfoBaud_Object = MibScalar
miscInfoBaud = _MiscInfoBaud_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 5),
    _MiscInfoBaud_Type()
)
miscInfoBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoBaud.setStatus("mandatory")
_MiscInfoTelnetControl_Type = Integer32
_MiscInfoTelnetControl_Object = MibScalar
miscInfoTelnetControl = _MiscInfoTelnetControl_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 6),
    _MiscInfoTelnetControl_Type()
)
miscInfoTelnetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoTelnetControl.setStatus("mandatory")
_MiscInfoSNMPPort_Type = Integer32
_MiscInfoSNMPPort_Object = MibScalar
miscInfoSNMPPort = _MiscInfoSNMPPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 7),
    _MiscInfoSNMPPort_Type()
)
miscInfoSNMPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoSNMPPort.setStatus("mandatory")
_MiscInfoAuthenTrap_Type = Integer32
_MiscInfoAuthenTrap_Object = MibScalar
miscInfoAuthenTrap = _MiscInfoAuthenTrap_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 8),
    _MiscInfoAuthenTrap_Type()
)
miscInfoAuthenTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoAuthenTrap.setStatus("mandatory")
_MiscInfoColdstartTrap_Type = Integer32
_MiscInfoColdstartTrap_Object = MibScalar
miscInfoColdstartTrap = _MiscInfoColdstartTrap_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 9),
    _MiscInfoColdstartTrap_Type()
)
miscInfoColdstartTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoColdstartTrap.setStatus("mandatory")
_MiscInfoLRPName_Type = DisplayString
_MiscInfoLRPName_Object = MibScalar
miscInfoLRPName = _MiscInfoLRPName_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 10),
    _MiscInfoLRPName_Type()
)
miscInfoLRPName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoLRPName.setStatus("mandatory")
_MiscInfoGateway_Type = IpAddress
_MiscInfoGateway_Object = MibScalar
miscInfoGateway = _MiscInfoGateway_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 11),
    _MiscInfoGateway_Type()
)
miscInfoGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoGateway.setStatus("mandatory")
_MiscInfoRoverPort_Type = Integer32
_MiscInfoRoverPort_Object = MibScalar
miscInfoRoverPort = _MiscInfoRoverPort_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 12),
    _MiscInfoRoverPort_Type()
)
miscInfoRoverPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    miscInfoRoverPort.setStatus("mandatory")
_MiscInfoReset_Type = Integer32
_MiscInfoReset_Object = MibScalar
miscInfoReset = _MiscInfoReset_Object(
    (1, 3, 6, 1, 4, 1, 244, 11, 6, 13),
    _MiscInfoReset_Type()
)
miscInfoReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    miscInfoReset.setStatus("mandatory")
_LtxLRPBadPkt_ObjectIdentity = ObjectIdentity
ltxLRPBadPkt = _LtxLRPBadPkt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 7)
)
_LtxLRPEnetIPMap_ObjectIdentity = ObjectIdentity
ltxLRPEnetIPMap = _LtxLRPEnetIPMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 8)
)
_LtxLRPTopNProt_ObjectIdentity = ObjectIdentity
ltxLRPTopNProt = _LtxLRPTopNProt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 9)
)
_LtxLRPDupIPDet_ObjectIdentity = ObjectIdentity
ltxLRPDupIPDet = _LtxLRPDupIPDet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 10)
)
_LtxLRPNewIPDet_ObjectIdentity = ObjectIdentity
ltxLRPNewIPDet = _LtxLRPNewIPDet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 11)
)
_LtxLRPIPChgDet_ObjectIdentity = ObjectIdentity
ltxLRPIPChgDet = _LtxLRPIPChgDet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 11, 12)
)
_Ltxlsw_ObjectIdentity = ObjectIdentity
ltxlsw = _Ltxlsw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 244, 12)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LTX-MIB",
    **{"OwnerString": OwnerString,
       "ltx": ltx,
       "ltxlna": ltxlna,
       "ltxlrp": ltxlrp,
       "ltxLRPCommInfo": ltxLRPCommInfo,
       "commInfoTable": commInfoTable,
       "commInfoEntry": commInfoEntry,
       "commInfoIndex": commInfoIndex,
       "commInfoName": commInfoName,
       "commInfoGet": commInfoGet,
       "commInfoSet": commInfoSet,
       "commInfoTrap": commInfoTrap,
       "ltxLRPHostInfo": ltxLRPHostInfo,
       "hostInfoTable": hostInfoTable,
       "hostInfoEntry": hostInfoEntry,
       "hostInfoIndex": hostInfoIndex,
       "hostInfoName": hostInfoName,
       "hostInfoIP": hostInfoIP,
       "hostInfoComm": hostInfoComm,
       "ltxLRPGroupInfo": ltxLRPGroupInfo,
       "groupInfoTable": groupInfoTable,
       "groupInfoEntry": groupInfoEntry,
       "groupInfoIndex": groupInfoIndex,
       "groupInfoCapFilt": groupInfoCapFilt,
       "groupInfoHostTopN": groupInfoHostTopN,
       "groupInfoMatrix": groupInfoMatrix,
       "ltxLRPMaxInfo": ltxLRPMaxInfo,
       "maxHTS": maxHTS,
       "maxMTS": maxMTS,
       "maxBuckets": maxBuckets,
       "maxLogs": maxLogs,
       "maxTopN": maxTopN,
       "maxBuff": maxBuff,
       "ltxLRPRoverInfo": ltxLRPRoverInfo,
       "roverControl": roverControl,
       "roverSeconds": roverSeconds,
       "roverTErrs": roverTErrs,
       "roverBPS": roverBPS,
       "roverEPS": roverEPS,
       "roverPPS": roverPPS,
       "roverUtil": roverUtil,
       "roverTCRC": roverTCRC,
       "roverTRunt": roverTRunt,
       "roverTGiant": roverTGiant,
       "roverTColl": roverTColl,
       "roverTJabb": roverTJabb,
       "ltxLRPMiscInfo": ltxLRPMiscInfo,
       "miscInfoPortTable": miscInfoPortTable,
       "miscInfoPortEntry": miscInfoPortEntry,
       "miscInfoPortIndex": miscInfoPortIndex,
       "miscInfoPortName": miscInfoPortName,
       "miscInfoPortIP": miscInfoPortIP,
       "miscInfoPortMask": miscInfoPortMask,
       "miscInfoDate": miscInfoDate,
       "miscInfoTMO": miscInfoTMO,
       "miscInfoRefresh": miscInfoRefresh,
       "miscInfoBaud": miscInfoBaud,
       "miscInfoTelnetControl": miscInfoTelnetControl,
       "miscInfoSNMPPort": miscInfoSNMPPort,
       "miscInfoAuthenTrap": miscInfoAuthenTrap,
       "miscInfoColdstartTrap": miscInfoColdstartTrap,
       "miscInfoLRPName": miscInfoLRPName,
       "miscInfoGateway": miscInfoGateway,
       "miscInfoRoverPort": miscInfoRoverPort,
       "miscInfoReset": miscInfoReset,
       "ltxLRPBadPkt": ltxLRPBadPkt,
       "ltxLRPEnetIPMap": ltxLRPEnetIPMap,
       "ltxLRPTopNProt": ltxLRPTopNProt,
       "ltxLRPDupIPDet": ltxLRPDupIPDet,
       "ltxLRPNewIPDet": ltxLRPNewIPDet,
       "ltxLRPIPChgDet": ltxLRPIPChgDet,
       "ltxlsw": ltxlsw}
)
