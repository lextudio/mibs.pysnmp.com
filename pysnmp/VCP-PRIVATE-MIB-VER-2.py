# SNMP MIB module (VCP-PRIVATE-MIB-VER-2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VCP-PRIVATE-MIB-VER-2
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:02 2024
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



class Character(Integer32):
    """Custom type Character based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class DisplayChar(Integer32):
    """Custom type DisplayChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 126),
    )





class LtGroupList(OctetString):
    """Custom type LtGroupList based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Datability_ObjectIdentity = ObjectIdentity
datability = _Datability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85)
)
_Port_ObjectIdentity = ObjectIdentity
port = _Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 1)
)
_Server_ObjectIdentity = ObjectIdentity
server = _Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 2)
)
_Service_ObjectIdentity = ObjectIdentity
service = _Service_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 3)
)
_Slot_ObjectIdentity = ObjectIdentity
slot = _Slot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 4)
)
_DssAdmin_ObjectIdentity = ObjectIdentity
dssAdmin = _DssAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 5)
)
_DssDevice_ObjectIdentity = ObjectIdentity
dssDevice = _DssDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 5, 1)
)
_Vcp_1000_ObjectIdentity = ObjectIdentity
vcp_1000 = _Vcp_1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 5, 1, 1)
)
_Vcp_200_ObjectIdentity = ObjectIdentity
vcp_200 = _Vcp_200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 5, 1, 2)
)
_Vcp_300_ObjectIdentity = ObjectIdentity
vcp_300 = _Vcp_300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 5, 1, 3)
)
_DssProtocol_ObjectIdentity = ObjectIdentity
dssProtocol = _DssProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 5, 2)
)
_DssNone_ObjectIdentity = ObjectIdentity
dssNone = _DssNone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 5, 2, 1)
)
_DssTelnet_ObjectIdentity = ObjectIdentity
dssTelnet = _DssTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 5, 2, 2)
)
_DssRlogin_ObjectIdentity = ObjectIdentity
dssRlogin = _DssRlogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 5, 2, 3)
)
_DssLt_ObjectIdentity = ObjectIdentity
dssLt = _DssLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 5, 2, 4)
)
_DssMibs_ObjectIdentity = ObjectIdentity
dssMibs = _DssMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6)
)
_DssServerMibs_ObjectIdentity = ObjectIdentity
dssServerMibs = _DssServerMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1)
)
_VcpMib_ObjectIdentity = ObjectIdentity
vcpMib = _VcpMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1)
)
_VcpSystem_ObjectIdentity = ObjectIdentity
vcpSystem = _VcpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1)
)
_VSysIdentifier_Type = ObjectIdentifier
_VSysIdentifier_Object = MibScalar
vSysIdentifier = _VSysIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 1),
    _VSysIdentifier_Type()
)
vSysIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSysIdentifier.setStatus("mandatory")


class _VSysReboot_Type(Integer32):
    """Custom type vSysReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_VSysReboot_Type.__name__ = "Integer32"
_VSysReboot_Object = MibScalar
vSysReboot = _VSysReboot_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 2),
    _VSysReboot_Type()
)
vSysReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysReboot.setStatus("mandatory")


class _VSysLtGroupStatus_Type(Integer32):
    """Custom type vSysLtGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("present", 1))
    )


_VSysLtGroupStatus_Type.__name__ = "Integer32"
_VSysLtGroupStatus_Object = MibScalar
vSysLtGroupStatus = _VSysLtGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 3),
    _VSysLtGroupStatus_Type()
)
vSysLtGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSysLtGroupStatus.setStatus("mandatory")


class _VSysPrimaryBoot_Type(Integer32):
    """Custom type vSysPrimaryBoot based on Integer32"""
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
        *(("bootp", 3),
          ("card", 5),
          ("mop", 2),
          ("rom", 1),
          ("tftp", 4))
    )


_VSysPrimaryBoot_Type.__name__ = "Integer32"
_VSysPrimaryBoot_Object = MibScalar
vSysPrimaryBoot = _VSysPrimaryBoot_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 4),
    _VSysPrimaryBoot_Type()
)
vSysPrimaryBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysPrimaryBoot.setStatus("mandatory")


class _VSysSecondaryBoot_Type(Integer32):
    """Custom type vSysSecondaryBoot based on Integer32"""
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
        *(("bootp", 3),
          ("card", 5),
          ("mop", 2),
          ("none", 6),
          ("rom", 1),
          ("tftp", 4))
    )


_VSysSecondaryBoot_Type.__name__ = "Integer32"
_VSysSecondaryBoot_Object = MibScalar
vSysSecondaryBoot = _VSysSecondaryBoot_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 5),
    _VSysSecondaryBoot_Type()
)
vSysSecondaryBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysSecondaryBoot.setStatus("mandatory")


class _VSysBootFilePath_Type(DisplayString):
    """Custom type vSysBootFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VSysBootFilePath_Type.__name__ = "DisplayString"
_VSysBootFilePath_Object = MibScalar
vSysBootFilePath = _VSysBootFilePath_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 6),
    _VSysBootFilePath_Type()
)
vSysBootFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysBootFilePath.setStatus("mandatory")


class _VSysBootFileName_Type(DisplayString):
    """Custom type vSysBootFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 9),
    )


_VSysBootFileName_Type.__name__ = "DisplayString"
_VSysBootFileName_Object = MibScalar
vSysBootFileName = _VSysBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 7),
    _VSysBootFileName_Type()
)
vSysBootFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysBootFileName.setStatus("mandatory")
_VSysBootServer_Type = IpAddress
_VSysBootServer_Object = MibScalar
vSysBootServer = _VSysBootServer_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 8),
    _VSysBootServer_Type()
)
vSysBootServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysBootServer.setStatus("mandatory")


class _VSysRemoteBoot_Type(Integer32):
    """Custom type vSysRemoteBoot based on Integer32"""
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


_VSysRemoteBoot_Type.__name__ = "Integer32"
_VSysRemoteBoot_Object = MibScalar
vSysRemoteBoot = _VSysRemoteBoot_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 9),
    _VSysRemoteBoot_Type()
)
vSysRemoteBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysRemoteBoot.setStatus("mandatory")


class _VSysEtherType_Type(Integer32):
    """Custom type vSysEtherType based on Integer32"""
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
        *(("autoSelect", 1),
          ("tenBaseT", 4),
          ("thickWire", 3),
          ("thinWire", 2))
    )


_VSysEtherType_Type.__name__ = "Integer32"
_VSysEtherType_Object = MibScalar
vSysEtherType = _VSysEtherType_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 10),
    _VSysEtherType_Type()
)
vSysEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysEtherType.setStatus("mandatory")


class _VSysBroadband_Type(Integer32):
    """Custom type vSysBroadband based on Integer32"""
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


_VSysBroadband_Type.__name__ = "Integer32"
_VSysBroadband_Object = MibScalar
vSysBroadband = _VSysBroadband_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 11),
    _VSysBroadband_Type()
)
vSysBroadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysBroadband.setStatus("mandatory")


class _VSysPasswordLimit_Type(Integer32):
    """Custom type vSysPasswordLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_VSysPasswordLimit_Type.__name__ = "Integer32"
_VSysPasswordLimit_Object = MibScalar
vSysPasswordLimit = _VSysPasswordLimit_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 12),
    _VSysPasswordLimit_Type()
)
vSysPasswordLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysPasswordLimit.setStatus("mandatory")


class _VSysPrivPassword_Type(DisplayString):
    """Custom type vSysPrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_VSysPrivPassword_Type.__name__ = "DisplayString"
_VSysPrivPassword_Object = MibScalar
vSysPrivPassword = _VSysPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 13),
    _VSysPrivPassword_Type()
)
vSysPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysPrivPassword.setStatus("mandatory")


class _VSysMaintenancePassword_Type(OctetString):
    """Custom type vSysMaintenancePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_VSysMaintenancePassword_Type.__name__ = "OctetString"
_VSysMaintenancePassword_Object = MibScalar
vSysMaintenancePassword = _VSysMaintenancePassword_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 1, 14),
    _VSysMaintenancePassword_Type()
)
vSysMaintenancePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSysMaintenancePassword.setStatus("mandatory")
_VcpPort_ObjectIdentity = ObjectIdentity
vcpPort = _VcpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2)
)


class _VPortBroadcast_Type(Integer32):
    """Custom type vPortBroadcast based on Integer32"""
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


_VPortBroadcast_Type.__name__ = "Integer32"
_VPortBroadcast_Object = MibScalar
vPortBroadcast = _VPortBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 1),
    _VPortBroadcast_Type()
)
vPortBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortBroadcast.setStatus("mandatory")


class _VPortInactivityTimer_Type(Integer32):
    """Custom type vPortInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_VPortInactivityTimer_Type.__name__ = "Integer32"
_VPortInactivityTimer_Object = MibScalar
vPortInactivityTimer = _VPortInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 2),
    _VPortInactivityTimer_Type()
)
vPortInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortInactivityTimer.setStatus("mandatory")


class _VPortAbsoluteTimer_Type(Integer32):
    """Custom type vPortAbsoluteTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1439),
    )


_VPortAbsoluteTimer_Type.__name__ = "Integer32"
_VPortAbsoluteTimer_Object = MibScalar
vPortAbsoluteTimer = _VPortAbsoluteTimer_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 3),
    _VPortAbsoluteTimer_Type()
)
vPortAbsoluteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortAbsoluteTimer.setStatus("mandatory")


class _VPortLock_Type(Integer32):
    """Custom type vPortLock based on Integer32"""
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


_VPortLock_Type.__name__ = "Integer32"
_VPortLock_Object = MibScalar
vPortLock = _VPortLock_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 4),
    _VPortLock_Type()
)
vPortLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortLock.setStatus("mandatory")


class _VPortLoginPassword_Type(DisplayString):
    """Custom type vPortLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_VPortLoginPassword_Type.__name__ = "DisplayString"
_VPortLoginPassword_Object = MibScalar
vPortLoginPassword = _VPortLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 5),
    _VPortLoginPassword_Type()
)
vPortLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortLoginPassword.setStatus("mandatory")
_VPortConsoleIndex_Type = Integer32
_VPortConsoleIndex_Object = MibScalar
vPortConsoleIndex = _VPortConsoleIndex_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 6),
    _VPortConsoleIndex_Type()
)
vPortConsoleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortConsoleIndex.setStatus("mandatory")


class _VPortFailover_Type(Integer32):
    """Custom type vPortFailover based on Integer32"""
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


_VPortFailover_Type.__name__ = "Integer32"
_VPortFailover_Object = MibScalar
vPortFailover = _VPortFailover_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 7),
    _VPortFailover_Type()
)
vPortFailover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortFailover.setStatus("mandatory")


class _VPortSignalCheck_Type(Integer32):
    """Custom type vPortSignalCheck based on Integer32"""
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


_VPortSignalCheck_Type.__name__ = "Integer32"
_VPortSignalCheck_Object = MibScalar
vPortSignalCheck = _VPortSignalCheck_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 8),
    _VPortSignalCheck_Type()
)
vPortSignalCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortSignalCheck.setStatus("mandatory")


class _VPortLoginMsgEnable_Type(Integer32):
    """Custom type vPortLoginMsgEnable based on Integer32"""
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


_VPortLoginMsgEnable_Type.__name__ = "Integer32"
_VPortLoginMsgEnable_Object = MibScalar
vPortLoginMsgEnable = _VPortLoginMsgEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 9),
    _VPortLoginMsgEnable_Type()
)
vPortLoginMsgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortLoginMsgEnable.setStatus("mandatory")


class _VPortBreakDuration_Type(Integer32):
    """Custom type vPortBreakDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_VPortBreakDuration_Type.__name__ = "Integer32"
_VPortBreakDuration_Object = MibScalar
vPortBreakDuration = _VPortBreakDuration_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 10),
    _VPortBreakDuration_Type()
)
vPortBreakDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortBreakDuration.setStatus("mandatory")


class _VPortXoffMark_Type(Integer32):
    """Custom type vPortXoffMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 510),
    )


_VPortXoffMark_Type.__name__ = "Integer32"
_VPortXoffMark_Object = MibScalar
vPortXoffMark = _VPortXoffMark_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 11),
    _VPortXoffMark_Type()
)
vPortXoffMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortXoffMark.setStatus("mandatory")


class _VPortXonMark_Type(Integer32):
    """Custom type vPortXonMark based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 510),
    )


_VPortXonMark_Type.__name__ = "Integer32"
_VPortXonMark_Object = MibScalar
vPortXonMark = _VPortXonMark_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 12),
    _VPortXonMark_Type()
)
vPortXonMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortXonMark.setStatus("mandatory")
_VPortNumber_Type = Integer32
_VPortNumber_Object = MibScalar
vPortNumber = _VPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 13),
    _VPortNumber_Type()
)
vPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortNumber.setStatus("mandatory")
_VPortTable_Object = MibTable
vPortTable = _VPortTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14)
)
if mibBuilder.loadTexts:
    vPortTable.setStatus("mandatory")
_VPortEntry_Object = MibTableRow
vPortEntry = _VPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1)
)
vPortEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vPortIndex"),
)
if mibBuilder.loadTexts:
    vPortEntry.setStatus("mandatory")
_VPortIndex_Type = Integer32
_VPortIndex_Object = MibTableColumn
vPortIndex = _VPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 1),
    _VPortIndex_Type()
)
vPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortIndex.setStatus("mandatory")


class _VPortType_Type(Integer32):
    """Custom type vPortType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("physicalLCDPanel", 5),
          ("physicalModem", 4),
          ("physicalRS-232", 2),
          ("physicalRS-423", 3),
          ("unknown", 1),
          ("virtual3270", 9),
          ("virtualConsole", 6),
          ("virtualNPT", 7),
          ("virtualX25", 8))
    )


_VPortType_Type.__name__ = "Integer32"
_VPortType_Object = MibTableColumn
vPortType = _VPortType_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 2),
    _VPortType_Type()
)
vPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortType.setStatus("mandatory")


class _VPortName_Type(DisplayString):
    """Custom type vPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_VPortName_Type.__name__ = "DisplayString"
_VPortName_Object = MibTableColumn
vPortName = _VPortName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 3),
    _VPortName_Type()
)
vPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortName.setStatus("mandatory")


class _VPortUserName_Type(DisplayString):
    """Custom type vPortUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VPortUserName_Type.__name__ = "DisplayString"
_VPortUserName_Object = MibTableColumn
vPortUserName = _VPortUserName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 4),
    _VPortUserName_Type()
)
vPortUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortUserName.setStatus("mandatory")


class _VPortState_Type(Integer32):
    """Custom type vPortState based on Integer32"""
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
        *(("connected", 5),
          ("connecting", 4),
          ("idle", 2),
          ("local", 3),
          ("locked", 6),
          ("serial-interface", 7),
          ("unknown", 1))
    )


_VPortState_Type.__name__ = "Integer32"
_VPortState_Object = MibTableColumn
vPortState = _VPortState_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 5),
    _VPortState_Type()
)
vPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortState.setStatus("mandatory")


class _VPortLogout_Type(Integer32):
    """Custom type vPortLogout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_VPortLogout_Type.__name__ = "Integer32"
_VPortLogout_Object = MibTableColumn
vPortLogout = _VPortLogout_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 6),
    _VPortLogout_Type()
)
vPortLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortLogout.setStatus("mandatory")
_VPortActiveSessions_Type = Integer32
_VPortActiveSessions_Object = MibTableColumn
vPortActiveSessions = _VPortActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 7),
    _VPortActiveSessions_Type()
)
vPortActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortActiveSessions.setStatus("mandatory")
_VPortCurrSessNumber_Type = Integer32
_VPortCurrSessNumber_Object = MibTableColumn
vPortCurrSessNumber = _VPortCurrSessNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 8),
    _VPortCurrSessNumber_Type()
)
vPortCurrSessNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortCurrSessNumber.setStatus("mandatory")
_VPortCurrSessProt_Type = ObjectIdentifier
_VPortCurrSessProt_Object = MibTableColumn
vPortCurrSessProt = _VPortCurrSessProt_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 9),
    _VPortCurrSessProt_Type()
)
vPortCurrSessProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortCurrSessProt.setStatus("mandatory")


class _VPortAccess_Type(Integer32):
    """Custom type vPortAccess based on Integer32"""
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
        *(("dynamic", 3),
          ("local", 1),
          ("none", 4),
          ("remote", 2))
    )


_VPortAccess_Type.__name__ = "Integer32"
_VPortAccess_Object = MibTableColumn
vPortAccess = _VPortAccess_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 10),
    _VPortAccess_Type()
)
vPortAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortAccess.setStatus("mandatory")


class _VPortVirtualEnable_Type(Integer32):
    """Custom type vPortVirtualEnable based on Integer32"""
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


_VPortVirtualEnable_Type.__name__ = "Integer32"
_VPortVirtualEnable_Object = MibTableColumn
vPortVirtualEnable = _VPortVirtualEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 11),
    _VPortVirtualEnable_Type()
)
vPortVirtualEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortVirtualEnable.setStatus("mandatory")


class _VPortVirtualString_Type(OctetString):
    """Custom type vPortVirtualString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 112),
    )


_VPortVirtualString_Type.__name__ = "OctetString"
_VPortVirtualString_Object = MibTableColumn
vPortVirtualString = _VPortVirtualString_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 12),
    _VPortVirtualString_Type()
)
vPortVirtualString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortVirtualString.setStatus("mandatory")


class _VPortSessionLimit_Type(Integer32):
    """Custom type vPortSessionLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VPortSessionLimit_Type.__name__ = "Integer32"
_VPortSessionLimit_Object = MibTableColumn
vPortSessionLimit = _VPortSessionLimit_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 13),
    _VPortSessionLimit_Type()
)
vPortSessionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortSessionLimit.setStatus("mandatory")


class _VPortProfile_Type(DisplayString):
    """Custom type vPortProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VPortProfile_Type.__name__ = "DisplayString"
_VPortProfile_Object = MibTableColumn
vPortProfile = _VPortProfile_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 14),
    _VPortProfile_Type()
)
vPortProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortProfile.setStatus("mandatory")


class _VPortQueueing_Type(Integer32):
    """Custom type vPortQueueing based on Integer32"""
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


_VPortQueueing_Type.__name__ = "Integer32"
_VPortQueueing_Object = MibTableColumn
vPortQueueing = _VPortQueueing_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 15),
    _VPortQueueing_Type()
)
vPortQueueing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortQueueing.setStatus("mandatory")


class _VPortPasswordEnable_Type(Integer32):
    """Custom type vPortPasswordEnable based on Integer32"""
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


_VPortPasswordEnable_Type.__name__ = "Integer32"
_VPortPasswordEnable_Object = MibTableColumn
vPortPasswordEnable = _VPortPasswordEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 16),
    _VPortPasswordEnable_Type()
)
vPortPasswordEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortPasswordEnable.setStatus("mandatory")


class _VPortTacacsEnable_Type(Integer32):
    """Custom type vPortTacacsEnable based on Integer32"""
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


_VPortTacacsEnable_Type.__name__ = "Integer32"
_VPortTacacsEnable_Object = MibTableColumn
vPortTacacsEnable = _VPortTacacsEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 17),
    _VPortTacacsEnable_Type()
)
vPortTacacsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortTacacsEnable.setStatus("mandatory")


class _VPortSecurityEnable_Type(Integer32):
    """Custom type vPortSecurityEnable based on Integer32"""
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


_VPortSecurityEnable_Type.__name__ = "Integer32"
_VPortSecurityEnable_Object = MibScalar
vPortSecurityEnable = _VPortSecurityEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 18),
    _VPortSecurityEnable_Type()
)
vPortSecurityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortSecurityEnable.setStatus("mandatory")
_VPortGroups_Type = LtGroupList
_VPortGroups_Object = MibTableColumn
vPortGroups = _VPortGroups_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 19),
    _VPortGroups_Type()
)
vPortGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortGroups.setStatus("mandatory")


class _VPortBreakMode_Type(Integer32):
    """Custom type vPortBreakMode based on Integer32"""
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
          ("local", 1),
          ("remote", 2))
    )


_VPortBreakMode_Type.__name__ = "Integer32"
_VPortBreakMode_Object = MibTableColumn
vPortBreakMode = _VPortBreakMode_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 20),
    _VPortBreakMode_Type()
)
vPortBreakMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortBreakMode.setStatus("mandatory")
_VPortBackSwitch_Type = Character
_VPortBackSwitch_Object = MibTableColumn
vPortBackSwitch = _VPortBackSwitch_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 21),
    _VPortBackSwitch_Type()
)
vPortBackSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortBackSwitch.setStatus("mandatory")
_VPortForwSwitch_Type = Character
_VPortForwSwitch_Object = MibTableColumn
vPortForwSwitch = _VPortForwSwitch_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 22),
    _VPortForwSwitch_Type()
)
vPortForwSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortForwSwitch.setStatus("mandatory")
_VPortLocalSwitch_Type = Character
_VPortLocalSwitch_Object = MibTableColumn
vPortLocalSwitch = _VPortLocalSwitch_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 23),
    _VPortLocalSwitch_Type()
)
vPortLocalSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortLocalSwitch.setStatus("mandatory")


class _VPortPrefSvc_Type(DisplayString):
    """Custom type vPortPrefSvc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VPortPrefSvc_Type.__name__ = "DisplayString"
_VPortPrefSvc_Object = MibTableColumn
vPortPrefSvc = _VPortPrefSvc_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 24),
    _VPortPrefSvc_Type()
)
vPortPrefSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortPrefSvc.setStatus("mandatory")


class _VPortPrefNode_Type(DisplayString):
    """Custom type vPortPrefNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VPortPrefNode_Type.__name__ = "DisplayString"
_VPortPrefNode_Object = MibTableColumn
vPortPrefNode = _VPortPrefNode_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 25),
    _VPortPrefNode_Type()
)
vPortPrefNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortPrefNode.setStatus("mandatory")


class _VPortPrefPort_Type(DisplayString):
    """Custom type vPortPrefPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VPortPrefPort_Type.__name__ = "DisplayString"
_VPortPrefPort_Object = MibTableColumn
vPortPrefPort = _VPortPrefPort_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 26),
    _VPortPrefPort_Type()
)
vPortPrefPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortPrefPort.setStatus("mandatory")


class _VPortPrefMode_Type(Integer32):
    """Custom type vPortPrefMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dedicated", 1),
          ("preferred", 2))
    )


_VPortPrefMode_Type.__name__ = "Integer32"
_VPortPrefMode_Object = MibTableColumn
vPortPrefMode = _VPortPrefMode_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 27),
    _VPortPrefMode_Type()
)
vPortPrefMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortPrefMode.setStatus("mandatory")


class _VPortAutoConnect_Type(Integer32):
    """Custom type vPortAutoConnect based on Integer32"""
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


_VPortAutoConnect_Type.__name__ = "Integer32"
_VPortAutoConnect_Object = MibTableColumn
vPortAutoConnect = _VPortAutoConnect_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 28),
    _VPortAutoConnect_Type()
)
vPortAutoConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortAutoConnect.setStatus("mandatory")


class _VPortPrompt_Type(DisplayString):
    """Custom type vPortPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_VPortPrompt_Type.__name__ = "DisplayString"
_VPortPrompt_Object = MibTableColumn
vPortPrompt = _VPortPrompt_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 29),
    _VPortPrompt_Type()
)
vPortPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortPrompt.setStatus("mandatory")


class _VPortInactiveLogout_Type(Integer32):
    """Custom type vPortInactiveLogout based on Integer32"""
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


_VPortInactiveLogout_Type.__name__ = "Integer32"
_VPortInactiveLogout_Object = MibTableColumn
vPortInactiveLogout = _VPortInactiveLogout_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 30),
    _VPortInactiveLogout_Type()
)
vPortInactiveLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortInactiveLogout.setStatus("mandatory")


class _VPortAutoPrompt_Type(Integer32):
    """Custom type vPortAutoPrompt based on Integer32"""
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


_VPortAutoPrompt_Type.__name__ = "Integer32"
_VPortAutoPrompt_Object = MibTableColumn
vPortAutoPrompt = _VPortAutoPrompt_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 31),
    _VPortAutoPrompt_Type()
)
vPortAutoPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortAutoPrompt.setStatus("mandatory")


class _VPortBroadcastEnable_Type(Integer32):
    """Custom type vPortBroadcastEnable based on Integer32"""
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


_VPortBroadcastEnable_Type.__name__ = "Integer32"
_VPortBroadcastEnable_Object = MibTableColumn
vPortBroadcastEnable = _VPortBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 32),
    _VPortBroadcastEnable_Type()
)
vPortBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortBroadcastEnable.setStatus("mandatory")


class _VPortInterrupts_Type(Integer32):
    """Custom type vPortInterrupts based on Integer32"""
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


_VPortInterrupts_Type.__name__ = "Integer32"
_VPortInterrupts_Object = MibTableColumn
vPortInterrupts = _VPortInterrupts_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 33),
    _VPortInterrupts_Type()
)
vPortInterrupts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortInterrupts.setStatus("mandatory")


class _VPortMessageCodes_Type(Integer32):
    """Custom type vPortMessageCodes based on Integer32"""
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


_VPortMessageCodes_Type.__name__ = "Integer32"
_VPortMessageCodes_Object = MibTableColumn
vPortMessageCodes = _VPortMessageCodes_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 34),
    _VPortMessageCodes_Type()
)
vPortMessageCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortMessageCodes.setStatus("mandatory")


class _VPortVerification_Type(Integer32):
    """Custom type vPortVerification based on Integer32"""
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


_VPortVerification_Type.__name__ = "Integer32"
_VPortVerification_Object = MibTableColumn
vPortVerification = _VPortVerification_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 35),
    _VPortVerification_Type()
)
vPortVerification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortVerification.setStatus("mandatory")


class _VPortDialup_Type(Integer32):
    """Custom type vPortDialup based on Integer32"""
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


_VPortDialup_Type.__name__ = "Integer32"
_VPortDialup_Object = MibTableColumn
vPortDialup = _VPortDialup_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 36),
    _VPortDialup_Type()
)
vPortDialup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortDialup.setStatus("mandatory")


class _VPortRemoteModify_Type(Integer32):
    """Custom type vPortRemoteModify based on Integer32"""
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


_VPortRemoteModify_Type.__name__ = "Integer32"
_VPortRemoteModify_Object = MibTableColumn
vPortRemoteModify = _VPortRemoteModify_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 37),
    _VPortRemoteModify_Type()
)
vPortRemoteModify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortRemoteModify.setStatus("mandatory")


class _VPortAbsoluteLogout_Type(Integer32):
    """Custom type vPortAbsoluteLogout based on Integer32"""
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


_VPortAbsoluteLogout_Type.__name__ = "Integer32"
_VPortAbsoluteLogout_Object = MibTableColumn
vPortAbsoluteLogout = _VPortAbsoluteLogout_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 38),
    _VPortAbsoluteLogout_Type()
)
vPortAbsoluteLogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortAbsoluteLogout.setStatus("mandatory")


class _VPortIOflush_Type(Integer32):
    """Custom type vPortIOflush based on Integer32"""
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


_VPortIOflush_Type.__name__ = "Integer32"
_VPortIOflush_Object = MibTableColumn
vPortIOflush = _VPortIOflush_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 39),
    _VPortIOflush_Type()
)
vPortIOflush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortIOflush.setStatus("mandatory")


class _VPortLogoutMsgEnable_Type(Integer32):
    """Custom type vPortLogoutMsgEnable based on Integer32"""
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


_VPortLogoutMsgEnable_Type.__name__ = "Integer32"
_VPortLogoutMsgEnable_Object = MibTableColumn
vPortLogoutMsgEnable = _VPortLogoutMsgEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 40),
    _VPortLogoutMsgEnable_Type()
)
vPortLogoutMsgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortLogoutMsgEnable.setStatus("mandatory")


class _VPortScreenType_Type(Integer32):
    """Custom type vPortScreenType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ansi", 1),
          ("hardcopy", 3),
          ("softcopy", 2))
    )


_VPortScreenType_Type.__name__ = "Integer32"
_VPortScreenType_Object = MibTableColumn
vPortScreenType = _VPortScreenType_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 41),
    _VPortScreenType_Type()
)
vPortScreenType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortScreenType.setStatus("mandatory")


class _VPortFlowType_Type(Integer32):
    """Custom type vPortFlowType based on Integer32"""
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
        *(("ctsRts", 4),
          ("dsrDtr", 5),
          ("hardware", 3),
          ("none", 1),
          ("xonXoff", 2))
    )


_VPortFlowType_Type.__name__ = "Integer32"
_VPortFlowType_Object = MibTableColumn
vPortFlowType = _VPortFlowType_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 42),
    _VPortFlowType_Type()
)
vPortFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortFlowType.setStatus("mandatory")


class _VPortInFlowState_Type(Integer32):
    """Custom type vPortInFlowState based on Integer32"""
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
        *(("go", 4),
          ("none", 1),
          ("stop", 3),
          ("unknown", 2))
    )


_VPortInFlowState_Type.__name__ = "Integer32"
_VPortInFlowState_Object = MibTableColumn
vPortInFlowState = _VPortInFlowState_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 43),
    _VPortInFlowState_Type()
)
vPortInFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortInFlowState.setStatus("mandatory")


class _VPortOutFlowState_Type(Integer32):
    """Custom type vPortOutFlowState based on Integer32"""
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
        *(("go", 4),
          ("none", 1),
          ("stop", 3),
          ("unknown", 2))
    )


_VPortOutFlowState_Type.__name__ = "Integer32"
_VPortOutFlowState_Object = MibTableColumn
vPortOutFlowState = _VPortOutFlowState_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 44),
    _VPortOutFlowState_Type()
)
vPortOutFlowState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortOutFlowState.setStatus("mandatory")


class _VPortCTSstate_Type(Integer32):
    """Custom type vPortCTSstate based on Integer32"""
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
        *(("none", 1),
          ("off", 3),
          ("on", 2),
          ("unknown", 4))
    )


_VPortCTSstate_Type.__name__ = "Integer32"
_VPortCTSstate_Object = MibTableColumn
vPortCTSstate = _VPortCTSstate_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 45),
    _VPortCTSstate_Type()
)
vPortCTSstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortCTSstate.setStatus("mandatory")


class _VPortDSRstate_Type(Integer32):
    """Custom type vPortDSRstate based on Integer32"""
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
        *(("none", 1),
          ("off", 3),
          ("on", 2),
          ("unknown", 4))
    )


_VPortDSRstate_Type.__name__ = "Integer32"
_VPortDSRstate_Object = MibTableColumn
vPortDSRstate = _VPortDSRstate_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 46),
    _VPortDSRstate_Type()
)
vPortDSRstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortDSRstate.setStatus("mandatory")


class _VPortDCDstate_Type(Integer32):
    """Custom type vPortDCDstate based on Integer32"""
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
        *(("none", 1),
          ("off", 3),
          ("on", 2),
          ("unknown", 4))
    )


_VPortDCDstate_Type.__name__ = "Integer32"
_VPortDCDstate_Object = MibTableColumn
vPortDCDstate = _VPortDCDstate_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 47),
    _VPortDCDstate_Type()
)
vPortDCDstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortDCDstate.setStatus("mandatory")


class _VPortDTRstate_Type(Integer32):
    """Custom type vPortDTRstate based on Integer32"""
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
        *(("none", 1),
          ("off", 3),
          ("on", 2),
          ("unknown", 4))
    )


_VPortDTRstate_Type.__name__ = "Integer32"
_VPortDTRstate_Object = MibTableColumn
vPortDTRstate = _VPortDTRstate_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 48),
    _VPortDTRstate_Type()
)
vPortDTRstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortDTRstate.setStatus("mandatory")


class _VPortRIstate_Type(Integer32):
    """Custom type vPortRIstate based on Integer32"""
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
        *(("none", 1),
          ("off", 3),
          ("on", 2),
          ("unknown", 4))
    )


_VPortRIstate_Type.__name__ = "Integer32"
_VPortRIstate_Object = MibTableColumn
vPortRIstate = _VPortRIstate_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 49),
    _VPortRIstate_Type()
)
vPortRIstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortRIstate.setStatus("mandatory")


class _VPortRTSstate_Type(Integer32):
    """Custom type vPortRTSstate based on Integer32"""
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
        *(("none", 1),
          ("off", 3),
          ("on", 2),
          ("unknown", 4))
    )


_VPortRTSstate_Type.__name__ = "Integer32"
_VPortRTSstate_Object = MibTableColumn
vPortRTSstate = _VPortRTSstate_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 50),
    _VPortRTSstate_Type()
)
vPortRTSstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortRTSstate.setStatus("mandatory")


class _VPortSpeed_Type(Integer32):
    """Custom type vPortSpeed based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("baud-110", 2),
          ("baud-1200", 5),
          ("baud-14400", 9),
          ("baud-19200", 10),
          ("baud-2400", 6),
          ("baud-28800", 11),
          ("baud-300", 3),
          ("baud-38400", 12),
          ("baud-4800", 7),
          ("baud-57600", 13),
          ("baud-600", 4),
          ("baud-9600", 8),
          ("none", 1))
    )


_VPortSpeed_Type.__name__ = "Integer32"
_VPortSpeed_Object = MibTableColumn
vPortSpeed = _VPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 51),
    _VPortSpeed_Type()
)
vPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortSpeed.setStatus("mandatory")


class _VPortCharSize_Type(Integer32):
    """Custom type vPortCharSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eight-bits", 3),
          ("none", 1),
          ("seven-bits", 2))
    )


_VPortCharSize_Type.__name__ = "Integer32"
_VPortCharSize_Object = MibTableColumn
vPortCharSize = _VPortCharSize_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 52),
    _VPortCharSize_Type()
)
vPortCharSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortCharSize.setStatus("mandatory")


class _VPortParityType_Type(Integer32):
    """Custom type vPortParityType based on Integer32"""
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
        *(("even", 3),
          ("mark", 5),
          ("none", 2),
          ("not-applicable", 1),
          ("odd", 4),
          ("space", 6))
    )


_VPortParityType_Type.__name__ = "Integer32"
_VPortParityType_Object = MibTableColumn
vPortParityType = _VPortParityType_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 53),
    _VPortParityType_Type()
)
vPortParityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortParityType.setStatus("mandatory")


class _VPortAutobaud_Type(Integer32):
    """Custom type vPortAutobaud based on Integer32"""
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
          ("not-applicable", 3))
    )


_VPortAutobaud_Type.__name__ = "Integer32"
_VPortAutobaud_Object = MibTableColumn
vPortAutobaud = _VPortAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 54),
    _VPortAutobaud_Type()
)
vPortAutobaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortAutobaud.setStatus("mandatory")


class _VPortModemControl_Type(Integer32):
    """Custom type vPortModemControl based on Integer32"""
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
          ("not-applicable", 3))
    )


_VPortModemControl_Type.__name__ = "Integer32"
_VPortModemControl_Object = MibTableColumn
vPortModemControl = _VPortModemControl_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 55),
    _VPortModemControl_Type()
)
vPortModemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortModemControl.setStatus("mandatory")


class _VPortDSRlogout_Type(Integer32):
    """Custom type vPortDSRlogout based on Integer32"""
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
          ("not-applicable", 3))
    )


_VPortDSRlogout_Type.__name__ = "Integer32"
_VPortDSRlogout_Object = MibTableColumn
vPortDSRlogout = _VPortDSRlogout_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 56),
    _VPortDSRlogout_Type()
)
vPortDSRlogout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortDSRlogout.setStatus("mandatory")


class _VPortRing_Type(Integer32):
    """Custom type vPortRing based on Integer32"""
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
          ("not-applicable", 3))
    )


_VPortRing_Type.__name__ = "Integer32"
_VPortRing_Object = MibTableColumn
vPortRing = _VPortRing_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 57),
    _VPortRing_Type()
)
vPortRing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortRing.setStatus("mandatory")


class _VPortDTRwait_Type(Integer32):
    """Custom type vPortDTRwait based on Integer32"""
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
          ("not-applicable", 3))
    )


_VPortDTRwait_Type.__name__ = "Integer32"
_VPortDTRwait_Object = MibTableColumn
vPortDTRwait = _VPortDTRwait_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 58),
    _VPortDTRwait_Type()
)
vPortDTRwait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortDTRwait.setStatus("mandatory")


class _VPortSignalCheckEnable_Type(Integer32):
    """Custom type vPortSignalCheckEnable based on Integer32"""
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
          ("not-applicable", 3))
    )


_VPortSignalCheckEnable_Type.__name__ = "Integer32"
_VPortSignalCheckEnable_Object = MibTableColumn
vPortSignalCheckEnable = _VPortSignalCheckEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 59),
    _VPortSignalCheckEnable_Type()
)
vPortSignalCheckEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortSignalCheckEnable.setStatus("mandatory")


class _VPortHandshake_Type(Integer32):
    """Custom type vPortHandshake based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-applicable", 3),
          ("signalCTS", 1),
          ("signalRI", 2))
    )


_VPortHandshake_Type.__name__ = "Integer32"
_VPortHandshake_Object = MibTableColumn
vPortHandshake = _VPortHandshake_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 60),
    _VPortHandshake_Type()
)
vPortHandshake.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vPortHandshake.setStatus("mandatory")
_VPortRcvChars_Type = Counter32
_VPortRcvChars_Object = MibTableColumn
vPortRcvChars = _VPortRcvChars_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 61),
    _VPortRcvChars_Type()
)
vPortRcvChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortRcvChars.setStatus("mandatory")
_VPortTrnChars_Type = Counter32
_VPortTrnChars_Object = MibTableColumn
vPortTrnChars = _VPortTrnChars_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 62),
    _VPortTrnChars_Type()
)
vPortTrnChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortTrnChars.setStatus("mandatory")
_VPortFrameErrs_Type = Counter32
_VPortFrameErrs_Object = MibTableColumn
vPortFrameErrs = _VPortFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 63),
    _VPortFrameErrs_Type()
)
vPortFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortFrameErrs.setStatus("mandatory")
_VPortOverrunErrs_Type = Counter32
_VPortOverrunErrs_Object = MibTableColumn
vPortOverrunErrs = _VPortOverrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 64),
    _VPortOverrunErrs_Type()
)
vPortOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortOverrunErrs.setStatus("mandatory")
_VPortParityErrs_Type = Counter32
_VPortParityErrs_Object = MibTableColumn
vPortParityErrs = _VPortParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 65),
    _VPortParityErrs_Type()
)
vPortParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortParityErrs.setStatus("mandatory")
_VPortCharsDropped_Type = Counter32
_VPortCharsDropped_Object = MibTableColumn
vPortCharsDropped = _VPortCharsDropped_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 2, 14, 1, 66),
    _VPortCharsDropped_Type()
)
vPortCharsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vPortCharsDropped.setStatus("mandatory")
_VcpService_ObjectIdentity = ObjectIdentity
vcpService = _VcpService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3)
)


class _VSvcRatingMode_Type(Integer32):
    """Custom type vSvcRatingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scaled", 1),
          ("unScaled", 2))
    )


_VSvcRatingMode_Type.__name__ = "Integer32"
_VSvcRatingMode_Object = MibScalar
vSvcRatingMode = _VSvcRatingMode_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 1),
    _VSvcRatingMode_Type()
)
vSvcRatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcRatingMode.setStatus("mandatory")
_VSvcCurrNumber_Type = Integer32
_VSvcCurrNumber_Object = MibScalar
vSvcCurrNumber = _VSvcCurrNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 2),
    _VSvcCurrNumber_Type()
)
vSvcCurrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSvcCurrNumber.setStatus("mandatory")
_VSvcTable_Object = MibTable
vSvcTable = _VSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    vSvcTable.setStatus("mandatory")
_VSvcEntry_Object = MibTableRow
vSvcEntry = _VSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1)
)
vSvcEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vSvcName"),
)
if mibBuilder.loadTexts:
    vSvcEntry.setStatus("mandatory")


class _VSvcName_Type(DisplayString):
    """Custom type vSvcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_VSvcName_Type.__name__ = "DisplayString"
_VSvcName_Object = MibTableColumn
vSvcName = _VSvcName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 1),
    _VSvcName_Type()
)
vSvcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcName.setStatus("mandatory")


class _VSvcPorts_Type(OctetString):
    """Custom type vSvcPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_VSvcPorts_Type.__name__ = "OctetString"
_VSvcPorts_Object = MibTableColumn
vSvcPorts = _VSvcPorts_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 2),
    _VSvcPorts_Type()
)
vSvcPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcPorts.setStatus("mandatory")


class _VSvcIdent_Type(DisplayString):
    """Custom type vSvcIdent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VSvcIdent_Type.__name__ = "DisplayString"
_VSvcIdent_Object = MibTableColumn
vSvcIdent = _VSvcIdent_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 3),
    _VSvcIdent_Type()
)
vSvcIdent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcIdent.setStatus("mandatory")


class _VSvcRating_Type(Integer32):
    """Custom type vSvcRating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VSvcRating_Type.__name__ = "Integer32"
_VSvcRating_Object = MibTableColumn
vSvcRating = _VSvcRating_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 4),
    _VSvcRating_Type()
)
vSvcRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSvcRating.setStatus("mandatory")


class _VSvcLtEnable_Type(Integer32):
    """Custom type vSvcLtEnable based on Integer32"""
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


_VSvcLtEnable_Type.__name__ = "Integer32"
_VSvcLtEnable_Object = MibTableColumn
vSvcLtEnable = _VSvcLtEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 5),
    _VSvcLtEnable_Type()
)
vSvcLtEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcLtEnable.setStatus("mandatory")


class _VSvcTelEnable_Type(Integer32):
    """Custom type vSvcTelEnable based on Integer32"""
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


_VSvcTelEnable_Type.__name__ = "Integer32"
_VSvcTelEnable_Object = MibTableColumn
vSvcTelEnable = _VSvcTelEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 6),
    _VSvcTelEnable_Type()
)
vSvcTelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcTelEnable.setStatus("mandatory")


class _VSvcLprEnable_Type(Integer32):
    """Custom type vSvcLprEnable based on Integer32"""
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


_VSvcLprEnable_Type.__name__ = "Integer32"
_VSvcLprEnable_Object = MibTableColumn
vSvcLprEnable = _VSvcLprEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 7),
    _VSvcLprEnable_Type()
)
vSvcLprEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcLprEnable.setStatus("mandatory")


class _VSvcRawEnable_Type(Integer32):
    """Custom type vSvcRawEnable based on Integer32"""
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


_VSvcRawEnable_Type.__name__ = "Integer32"
_VSvcRawEnable_Object = MibTableColumn
vSvcRawEnable = _VSvcRawEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 8),
    _VSvcRawEnable_Type()
)
vSvcRawEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcRawEnable.setStatus("mandatory")


class _VSvcVirtualEnable_Type(Integer32):
    """Custom type vSvcVirtualEnable based on Integer32"""
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


_VSvcVirtualEnable_Type.__name__ = "Integer32"
_VSvcVirtualEnable_Object = MibTableColumn
vSvcVirtualEnable = _VSvcVirtualEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 9),
    _VSvcVirtualEnable_Type()
)
vSvcVirtualEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcVirtualEnable.setStatus("mandatory")


class _VSvcVirtualText_Type(OctetString):
    """Custom type vSvcVirtualText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 112),
    )


_VSvcVirtualText_Type.__name__ = "OctetString"
_VSvcVirtualText_Object = MibTableColumn
vSvcVirtualText = _VSvcVirtualText_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 10),
    _VSvcVirtualText_Type()
)
vSvcVirtualText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcVirtualText.setStatus("mandatory")


class _VSvcConnectEnable_Type(Integer32):
    """Custom type vSvcConnectEnable based on Integer32"""
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


_VSvcConnectEnable_Type.__name__ = "Integer32"
_VSvcConnectEnable_Object = MibTableColumn
vSvcConnectEnable = _VSvcConnectEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 11),
    _VSvcConnectEnable_Type()
)
vSvcConnectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcConnectEnable.setStatus("mandatory")


class _VSvcPassword_Type(DisplayString):
    """Custom type vSvcPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_VSvcPassword_Type.__name__ = "DisplayString"
_VSvcPassword_Object = MibTableColumn
vSvcPassword = _VSvcPassword_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 12),
    _VSvcPassword_Type()
)
vSvcPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcPassword.setStatus("mandatory")


class _VSvcQueueEnable_Type(Integer32):
    """Custom type vSvcQueueEnable based on Integer32"""
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


_VSvcQueueEnable_Type.__name__ = "Integer32"
_VSvcQueueEnable_Object = MibTableColumn
vSvcQueueEnable = _VSvcQueueEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 13),
    _VSvcQueueEnable_Type()
)
vSvcQueueEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcQueueEnable.setStatus("mandatory")
_VSvcIpAddr_Type = IpAddress
_VSvcIpAddr_Object = MibTableColumn
vSvcIpAddr = _VSvcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 14),
    _VSvcIpAddr_Type()
)
vSvcIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcIpAddr.setStatus("mandatory")


class _VSvcTcpPort_Type(Integer32):
    """Custom type vSvcTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VSvcTcpPort_Type.__name__ = "Integer32"
_VSvcTcpPort_Object = MibTableColumn
vSvcTcpPort = _VSvcTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 15),
    _VSvcTcpPort_Type()
)
vSvcTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcTcpPort.setStatus("mandatory")


class _VSvcProfile_Type(DisplayString):
    """Custom type vSvcProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VSvcProfile_Type.__name__ = "DisplayString"
_VSvcProfile_Object = MibTableColumn
vSvcProfile = _VSvcProfile_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 16),
    _VSvcProfile_Type()
)
vSvcProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcProfile.setStatus("mandatory")


class _VSvcStatus_Type(Integer32):
    """Custom type vSvcStatus based on Integer32"""
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


_VSvcStatus_Type.__name__ = "Integer32"
_VSvcStatus_Object = MibTableColumn
vSvcStatus = _VSvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 3, 3, 1, 17),
    _VSvcStatus_Type()
)
vSvcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSvcStatus.setStatus("mandatory")
_VcpProfile_ObjectIdentity = ObjectIdentity
vcpProfile = _VcpProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4)
)
_VProfCurrNumber_Type = Integer32
_VProfCurrNumber_Object = MibScalar
vProfCurrNumber = _VProfCurrNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 1),
    _VProfCurrNumber_Type()
)
vProfCurrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vProfCurrNumber.setStatus("mandatory")
_VProfTable_Object = MibTable
vProfTable = _VProfTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    vProfTable.setStatus("mandatory")
_VProfEntry_Object = MibTableRow
vProfEntry = _VProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1)
)
vProfEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vProfName"),
)
if mibBuilder.loadTexts:
    vProfEntry.setStatus("mandatory")


class _VProfName_Type(DisplayString):
    """Custom type vProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_VProfName_Type.__name__ = "DisplayString"
_VProfName_Object = MibTableColumn
vProfName = _VProfName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 1),
    _VProfName_Type()
)
vProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfName.setStatus("mandatory")


class _VProfDomain_Type(DisplayString):
    """Custom type vProfDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VProfDomain_Type.__name__ = "DisplayString"
_VProfDomain_Object = MibTableColumn
vProfDomain = _VProfDomain_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 2),
    _VProfDomain_Type()
)
vProfDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfDomain.setStatus("mandatory")


class _VProfConcatenate_Type(Integer32):
    """Custom type vProfConcatenate based on Integer32"""
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


_VProfConcatenate_Type.__name__ = "Integer32"
_VProfConcatenate_Object = MibTableColumn
vProfConcatenate = _VProfConcatenate_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 3),
    _VProfConcatenate_Type()
)
vProfConcatenate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfConcatenate.setStatus("mandatory")


class _VProfPermHostOnly_Type(Integer32):
    """Custom type vProfPermHostOnly based on Integer32"""
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


_VProfPermHostOnly_Type.__name__ = "Integer32"
_VProfPermHostOnly_Object = MibTableColumn
vProfPermHostOnly = _VProfPermHostOnly_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 4),
    _VProfPermHostOnly_Type()
)
vProfPermHostOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfPermHostOnly.setStatus("mandatory")


class _VProfTcpPort_Type(Integer32):
    """Custom type vProfTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VProfTcpPort_Type.__name__ = "Integer32"
_VProfTcpPort_Object = MibTableColumn
vProfTcpPort = _VProfTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 5),
    _VProfTcpPort_Type()
)
vProfTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfTcpPort.setStatus("mandatory")


class _VProfTcpTimeout_Type(Integer32):
    """Custom type vProfTcpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VProfTcpTimeout_Type.__name__ = "Integer32"
_VProfTcpTimeout_Object = MibTableColumn
vProfTcpTimeout = _VProfTcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 6),
    _VProfTcpTimeout_Type()
)
vProfTcpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfTcpTimeout.setStatus("mandatory")


class _VProfTcpKeepalive_Type(Integer32):
    """Custom type vProfTcpKeepalive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VProfTcpKeepalive_Type.__name__ = "Integer32"
_VProfTcpKeepalive_Object = MibTableColumn
vProfTcpKeepalive = _VProfTcpKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 7),
    _VProfTcpKeepalive_Type()
)
vProfTcpKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfTcpKeepalive.setStatus("mandatory")


class _VProfIpTTL_Type(Integer32):
    """Custom type vProfIpTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VProfIpTTL_Type.__name__ = "Integer32"
_VProfIpTTL_Object = MibTableColumn
vProfIpTTL = _VProfIpTTL_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 8),
    _VProfIpTTL_Type()
)
vProfIpTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfIpTTL.setStatus("mandatory")


class _VProfIpPrecedence_Type(Integer32):
    """Custom type vProfIpPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VProfIpPrecedence_Type.__name__ = "Integer32"
_VProfIpPrecedence_Object = MibTableColumn
vProfIpPrecedence = _VProfIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 9),
    _VProfIpPrecedence_Type()
)
vProfIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfIpPrecedence.setStatus("mandatory")


class _VProfTermType_Type(DisplayString):
    """Custom type vProfTermType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VProfTermType_Type.__name__ = "DisplayString"
_VProfTermType_Object = MibTableColumn
vProfTermType = _VProfTermType_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 10),
    _VProfTermType_Type()
)
vProfTermType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfTermType.setStatus("mandatory")


class _VProfCrToNet_Type(OctetString):
    """Custom type vProfCrToNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_VProfCrToNet_Type.__name__ = "OctetString"
_VProfCrToNet_Object = MibTableColumn
vProfCrToNet = _VProfCrToNet_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 11),
    _VProfCrToNet_Type()
)
vProfCrToNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfCrToNet.setStatus("mandatory")


class _VProfCrFromTerm_Type(OctetString):
    """Custom type vProfCrFromTerm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_VProfCrFromTerm_Type.__name__ = "OctetString"
_VProfCrFromTerm_Object = MibTableColumn
vProfCrFromTerm = _VProfCrFromTerm_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 12),
    _VProfCrFromTerm_Type()
)
vProfCrFromTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfCrFromTerm.setStatus("mandatory")
_VProfPadChar_Type = Character
_VProfPadChar_Object = MibTableColumn
vProfPadChar = _VProfPadChar_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 13),
    _VProfPadChar_Type()
)
vProfPadChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfPadChar.setStatus("mandatory")


class _VProfPadLength_Type(Integer32):
    """Custom type vProfPadLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VProfPadLength_Type.__name__ = "Integer32"
_VProfPadLength_Object = MibTableColumn
vProfPadLength = _VProfPadLength_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 14),
    _VProfPadLength_Type()
)
vProfPadLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfPadLength.setStatus("mandatory")
_VProfEndRecord_Type = Character
_VProfEndRecord_Object = MibTableColumn
vProfEndRecord = _VProfEndRecord_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 15),
    _VProfEndRecord_Type()
)
vProfEndRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfEndRecord.setStatus("mandatory")
_VProfNop_Type = Character
_VProfNop_Object = MibTableColumn
vProfNop = _VProfNop_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 16),
    _VProfNop_Type()
)
vProfNop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfNop.setStatus("mandatory")
_VProfDataMark_Type = Character
_VProfDataMark_Object = MibTableColumn
vProfDataMark = _VProfDataMark_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 17),
    _VProfDataMark_Type()
)
vProfDataMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfDataMark.setStatus("mandatory")
_VProfBreak_Type = Character
_VProfBreak_Object = MibTableColumn
vProfBreak = _VProfBreak_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 18),
    _VProfBreak_Type()
)
vProfBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfBreak.setStatus("mandatory")
_VProfIntProcess_Type = Character
_VProfIntProcess_Object = MibTableColumn
vProfIntProcess = _VProfIntProcess_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 19),
    _VProfIntProcess_Type()
)
vProfIntProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfIntProcess.setStatus("mandatory")
_VProfAbortOutput_Type = Character
_VProfAbortOutput_Object = MibTableColumn
vProfAbortOutput = _VProfAbortOutput_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 20),
    _VProfAbortOutput_Type()
)
vProfAbortOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfAbortOutput.setStatus("mandatory")
_VProfAttention_Type = Character
_VProfAttention_Object = MibTableColumn
vProfAttention = _VProfAttention_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 21),
    _VProfAttention_Type()
)
vProfAttention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfAttention.setStatus("mandatory")
_VProfEraseChar_Type = Character
_VProfEraseChar_Object = MibTableColumn
vProfEraseChar = _VProfEraseChar_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 22),
    _VProfEraseChar_Type()
)
vProfEraseChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfEraseChar.setStatus("mandatory")
_VProfEraseLine_Type = Character
_VProfEraseLine_Object = MibTableColumn
vProfEraseLine = _VProfEraseLine_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 23),
    _VProfEraseLine_Type()
)
vProfEraseLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfEraseLine.setStatus("mandatory")
_VProfGoAhead_Type = Character
_VProfGoAhead_Object = MibTableColumn
vProfGoAhead = _VProfGoAhead_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 24),
    _VProfGoAhead_Type()
)
vProfGoAhead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfGoAhead.setStatus("mandatory")


class _VProfNullPass_Type(Integer32):
    """Custom type vProfNullPass based on Integer32"""
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


_VProfNullPass_Type.__name__ = "Integer32"
_VProfNullPass_Object = MibTableColumn
vProfNullPass = _VProfNullPass_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 25),
    _VProfNullPass_Type()
)
vProfNullPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfNullPass.setStatus("mandatory")


class _VProfLocalEcho_Type(Integer32):
    """Custom type vProfLocalEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 3),
          ("attempt", 1),
          ("refuse", 2))
    )


_VProfLocalEcho_Type.__name__ = "Integer32"
_VProfLocalEcho_Object = MibTableColumn
vProfLocalEcho = _VProfLocalEcho_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 26),
    _VProfLocalEcho_Type()
)
vProfLocalEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfLocalEcho.setStatus("mandatory")


class _VProfRemoteEcho_Type(Integer32):
    """Custom type vProfRemoteEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 3),
          ("attempt", 1),
          ("refuse", 2))
    )


_VProfRemoteEcho_Type.__name__ = "Integer32"
_VProfRemoteEcho_Object = MibTableColumn
vProfRemoteEcho = _VProfRemoteEcho_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 27),
    _VProfRemoteEcho_Type()
)
vProfRemoteEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfRemoteEcho.setStatus("mandatory")


class _VProfLocalBinary_Type(Integer32):
    """Custom type vProfLocalBinary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 3),
          ("attempt", 1),
          ("refuse", 2))
    )


_VProfLocalBinary_Type.__name__ = "Integer32"
_VProfLocalBinary_Object = MibTableColumn
vProfLocalBinary = _VProfLocalBinary_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 28),
    _VProfLocalBinary_Type()
)
vProfLocalBinary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfLocalBinary.setStatus("mandatory")


class _VProfRemoteBinary_Type(Integer32):
    """Custom type vProfRemoteBinary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("allow", 3),
          ("attempt", 1),
          ("refuse", 2))
    )


_VProfRemoteBinary_Type.__name__ = "Integer32"
_VProfRemoteBinary_Object = MibTableColumn
vProfRemoteBinary = _VProfRemoteBinary_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 29),
    _VProfRemoteBinary_Type()
)
vProfRemoteBinary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfRemoteBinary.setStatus("mandatory")


class _VProfStatus_Type(Integer32):
    """Custom type vProfStatus based on Integer32"""
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


_VProfStatus_Type.__name__ = "Integer32"
_VProfStatus_Object = MibTableColumn
vProfStatus = _VProfStatus_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 4, 2, 1, 30),
    _VProfStatus_Type()
)
vProfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vProfStatus.setStatus("mandatory")
_VcpIpSecurity_ObjectIdentity = ObjectIdentity
vcpIpSecurity = _VcpIpSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 5)
)


class _VSecEnable_Type(Integer32):
    """Custom type vSecEnable based on Integer32"""
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


_VSecEnable_Type.__name__ = "Integer32"
_VSecEnable_Object = MibScalar
vSecEnable = _VSecEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 5, 1),
    _VSecEnable_Type()
)
vSecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSecEnable.setStatus("mandatory")
_VSecCurrNumber_Type = Integer32
_VSecCurrNumber_Object = MibScalar
vSecCurrNumber = _VSecCurrNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 5, 2),
    _VSecCurrNumber_Type()
)
vSecCurrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSecCurrNumber.setStatus("mandatory")
_VSecTable_Object = MibTable
vSecTable = _VSecTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 5, 3)
)
if mibBuilder.loadTexts:
    vSecTable.setStatus("mandatory")
_VSecEntry_Object = MibTableRow
vSecEntry = _VSecEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 5, 3, 1)
)
vSecEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vSecIndex"),
)
if mibBuilder.loadTexts:
    vSecEntry.setStatus("mandatory")


class _VSecIndex_Type(Integer32):
    """Custom type vSecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VSecIndex_Type.__name__ = "Integer32"
_VSecIndex_Object = MibTableColumn
vSecIndex = _VSecIndex_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 5, 3, 1, 1),
    _VSecIndex_Type()
)
vSecIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSecIndex.setStatus("mandatory")
_VSecAddress_Type = IpAddress
_VSecAddress_Object = MibTableColumn
vSecAddress = _VSecAddress_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 5, 3, 1, 2),
    _VSecAddress_Type()
)
vSecAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSecAddress.setStatus("mandatory")
_VSecMask_Type = IpAddress
_VSecMask_Object = MibTableColumn
vSecMask = _VSecMask_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 5, 3, 1, 3),
    _VSecMask_Type()
)
vSecMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSecMask.setStatus("mandatory")
_VSecGroups_Type = LtGroupList
_VSecGroups_Object = MibTableColumn
vSecGroups = _VSecGroups_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 5, 3, 1, 4),
    _VSecGroups_Type()
)
vSecGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSecGroups.setStatus("mandatory")


class _VSecStatus_Type(Integer32):
    """Custom type vSecStatus based on Integer32"""
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


_VSecStatus_Type.__name__ = "Integer32"
_VSecStatus_Object = MibTableColumn
vSecStatus = _VSecStatus_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 5, 3, 1, 5),
    _VSecStatus_Type()
)
vSecStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSecStatus.setStatus("mandatory")
_VcpHostname_ObjectIdentity = ObjectIdentity
vcpHostname = _VcpHostname_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 6)
)
_VHostCurrNumber_Type = Integer32
_VHostCurrNumber_Object = MibScalar
vHostCurrNumber = _VHostCurrNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 6, 1),
    _VHostCurrNumber_Type()
)
vHostCurrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vHostCurrNumber.setStatus("mandatory")
_VHostTable_Object = MibTable
vHostTable = _VHostTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    vHostTable.setStatus("mandatory")
_VHostEntry_Object = MibTableRow
vHostEntry = _VHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 6, 2, 1)
)
vHostEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vHostHostname"),
)
if mibBuilder.loadTexts:
    vHostEntry.setStatus("mandatory")


class _VHostHostname_Type(OctetString):
    """Custom type vHostHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VHostHostname_Type.__name__ = "OctetString"
_VHostHostname_Object = MibTableColumn
vHostHostname = _VHostHostname_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 6, 2, 1, 1),
    _VHostHostname_Type()
)
vHostHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vHostHostname.setStatus("mandatory")
_VHostAddress_Type = IpAddress
_VHostAddress_Object = MibTableColumn
vHostAddress = _VHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 6, 2, 1, 2),
    _VHostAddress_Type()
)
vHostAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vHostAddress.setStatus("mandatory")
_VHostTTL_Type = Integer32
_VHostTTL_Object = MibTableColumn
vHostTTL = _VHostTTL_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 6, 2, 1, 3),
    _VHostTTL_Type()
)
vHostTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vHostTTL.setStatus("mandatory")


class _VHostStatus_Type(Integer32):
    """Custom type vHostStatus based on Integer32"""
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


_VHostStatus_Type.__name__ = "Integer32"
_VHostStatus_Object = MibTableColumn
vHostStatus = _VHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 6, 2, 1, 4),
    _VHostStatus_Type()
)
vHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vHostStatus.setStatus("mandatory")
_VcpNameserver_ObjectIdentity = ObjectIdentity
vcpNameserver = _VcpNameserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 7)
)


class _VNsRequestMode_Type(Integer32):
    """Custom type vNsRequestMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRecursive", 2),
          ("recursive", 1))
    )


_VNsRequestMode_Type.__name__ = "Integer32"
_VNsRequestMode_Object = MibScalar
vNsRequestMode = _VNsRequestMode_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 7, 1),
    _VNsRequestMode_Type()
)
vNsRequestMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vNsRequestMode.setStatus("mandatory")


class _VNsAllowLowerCase_Type(Integer32):
    """Custom type vNsAllowLowerCase based on Integer32"""
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


_VNsAllowLowerCase_Type.__name__ = "Integer32"
_VNsAllowLowerCase_Object = MibScalar
vNsAllowLowerCase = _VNsAllowLowerCase_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 7, 2),
    _VNsAllowLowerCase_Type()
)
vNsAllowLowerCase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vNsAllowLowerCase.setStatus("mandatory")
_VNsCurrNumber_Type = Integer32
_VNsCurrNumber_Object = MibScalar
vNsCurrNumber = _VNsCurrNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 7, 3),
    _VNsCurrNumber_Type()
)
vNsCurrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vNsCurrNumber.setStatus("mandatory")
_VNsTable_Object = MibTable
vNsTable = _VNsTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 7, 4)
)
if mibBuilder.loadTexts:
    vNsTable.setStatus("mandatory")
_VNsEntry_Object = MibTableRow
vNsEntry = _VNsEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 7, 4, 1)
)
vNsEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vNsAddress"),
)
if mibBuilder.loadTexts:
    vNsEntry.setStatus("mandatory")
_VNsAddress_Type = IpAddress
_VNsAddress_Object = MibTableColumn
vNsAddress = _VNsAddress_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 7, 4, 1, 1),
    _VNsAddress_Type()
)
vNsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vNsAddress.setStatus("mandatory")


class _VNsHostname_Type(OctetString):
    """Custom type vNsHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VNsHostname_Type.__name__ = "OctetString"
_VNsHostname_Object = MibTableColumn
vNsHostname = _VNsHostname_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 7, 4, 1, 2),
    _VNsHostname_Type()
)
vNsHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vNsHostname.setStatus("mandatory")
_VNsTTL_Type = Integer32
_VNsTTL_Object = MibTableColumn
vNsTTL = _VNsTTL_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 7, 4, 1, 3),
    _VNsTTL_Type()
)
vNsTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vNsTTL.setStatus("mandatory")


class _VNsStatus_Type(Integer32):
    """Custom type vNsStatus based on Integer32"""
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


_VNsStatus_Type.__name__ = "Integer32"
_VNsStatus_Object = MibTableColumn
vNsStatus = _VNsStatus_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 7, 4, 1, 4),
    _VNsStatus_Type()
)
vNsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vNsStatus.setStatus("mandatory")
_VcpTacacs_ObjectIdentity = ObjectIdentity
vcpTacacs = _VcpTacacs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 8)
)
_VTacServerCurrNumber_Type = Integer32
_VTacServerCurrNumber_Object = MibScalar
vTacServerCurrNumber = _VTacServerCurrNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 8, 1),
    _VTacServerCurrNumber_Type()
)
vTacServerCurrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTacServerCurrNumber.setStatus("mandatory")
_VTacTable_Object = MibTable
vTacTable = _VTacTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    vTacTable.setStatus("mandatory")
_VTacEntry_Object = MibTableRow
vTacEntry = _VTacEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 8, 2, 1)
)
vTacEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vTacAddress"),
)
if mibBuilder.loadTexts:
    vTacEntry.setStatus("mandatory")
_VTacAddress_Type = IpAddress
_VTacAddress_Object = MibTableColumn
vTacAddress = _VTacAddress_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 8, 2, 1, 1),
    _VTacAddress_Type()
)
vTacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTacAddress.setStatus("mandatory")


class _VTacHostname_Type(OctetString):
    """Custom type vTacHostname based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_VTacHostname_Type.__name__ = "OctetString"
_VTacHostname_Object = MibTableColumn
vTacHostname = _VTacHostname_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 8, 2, 1, 2),
    _VTacHostname_Type()
)
vTacHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTacHostname.setStatus("mandatory")


class _VTacStatus_Type(Integer32):
    """Custom type vTacStatus based on Integer32"""
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


_VTacStatus_Type.__name__ = "Integer32"
_VTacStatus_Object = MibTableColumn
vTacStatus = _VTacStatus_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 8, 2, 1, 3),
    _VTacStatus_Type()
)
vTacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTacStatus.setStatus("mandatory")
_VcpIp_ObjectIdentity = ObjectIdentity
vcpIp = _VcpIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 9)
)
_VIpBcastAddr_Type = IpAddress
_VIpBcastAddr_Object = MibScalar
vIpBcastAddr = _VIpBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 9, 1),
    _VIpBcastAddr_Type()
)
vIpBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpBcastAddr.setStatus("mandatory")


class _VIpMaxAddr_Type(Integer32):
    """Custom type vIpMaxAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 64),
    )


_VIpMaxAddr_Type.__name__ = "Integer32"
_VIpMaxAddr_Object = MibScalar
vIpMaxAddr = _VIpMaxAddr_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 9, 2),
    _VIpMaxAddr_Type()
)
vIpMaxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpMaxAddr.setStatus("mandatory")


class _VIpMaxHostHashEntries_Type(Integer32):
    """Custom type vIpMaxHostHashEntries based on Integer32"""
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
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("size-11", 1),
          ("size-13", 2),
          ("size-17", 3),
          ("size-19", 4),
          ("size-23", 5),
          ("size-29", 6),
          ("size-31", 7),
          ("size-37", 8),
          ("size-41", 9),
          ("size-43", 10),
          ("size-47", 11),
          ("size-49", 12),
          ("size-53", 13),
          ("size-59", 14),
          ("size-61", 15),
          ("size-67", 16))
    )


_VIpMaxHostHashEntries_Type.__name__ = "Integer32"
_VIpMaxHostHashEntries_Object = MibScalar
vIpMaxHostHashEntries = _VIpMaxHostHashEntries_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 9, 3),
    _VIpMaxHostHashEntries_Type()
)
vIpMaxHostHashEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpMaxHostHashEntries.setStatus("mandatory")


class _VIpMaxNetHashEntries_Type(Integer32):
    """Custom type vIpMaxNetHashEntries based on Integer32"""
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
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("size-11", 1),
          ("size-13", 2),
          ("size-17", 3),
          ("size-19", 4),
          ("size-23", 5),
          ("size-29", 6),
          ("size-31", 7),
          ("size-37", 8),
          ("size-41", 9),
          ("size-43", 10),
          ("size-47", 11),
          ("size-49", 12),
          ("size-53", 13),
          ("size-59", 14),
          ("size-61", 15),
          ("size-67", 16))
    )


_VIpMaxNetHashEntries_Type.__name__ = "Integer32"
_VIpMaxNetHashEntries_Object = MibScalar
vIpMaxNetHashEntries = _VIpMaxNetHashEntries_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 9, 4),
    _VIpMaxNetHashEntries_Type()
)
vIpMaxNetHashEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpMaxNetHashEntries.setStatus("mandatory")


class _VIpMaxInterfaces_Type(Integer32):
    """Custom type vIpMaxInterfaces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 128),
    )


_VIpMaxInterfaces_Type.__name__ = "Integer32"
_VIpMaxInterfaces_Object = MibScalar
vIpMaxInterfaces = _VIpMaxInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 9, 5),
    _VIpMaxInterfaces_Type()
)
vIpMaxInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpMaxInterfaces.setStatus("mandatory")


class _VIpMaxRoutes_Type(Integer32):
    """Custom type vIpMaxRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 128),
    )


_VIpMaxRoutes_Type.__name__ = "Integer32"
_VIpMaxRoutes_Object = MibScalar
vIpMaxRoutes = _VIpMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 9, 6),
    _VIpMaxRoutes_Type()
)
vIpMaxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vIpMaxRoutes.setStatus("mandatory")
_VcpArp_ObjectIdentity = ObjectIdentity
vcpArp = _VcpArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 10)
)


class _VArpMaxEntries_Type(Integer32):
    """Custom type vArpMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 128),
    )


_VArpMaxEntries_Type.__name__ = "Integer32"
_VArpMaxEntries_Object = MibScalar
vArpMaxEntries = _VArpMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 10, 1),
    _VArpMaxEntries_Type()
)
vArpMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vArpMaxEntries.setStatus("mandatory")


class _VArpRetryTimeout_Type(Integer32):
    """Custom type vArpRetryTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VArpRetryTimeout_Type.__name__ = "Integer32"
_VArpRetryTimeout_Object = MibScalar
vArpRetryTimeout = _VArpRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 10, 2),
    _VArpRetryTimeout_Type()
)
vArpRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vArpRetryTimeout.setStatus("mandatory")


class _VArpRetryMax_Type(Integer32):
    """Custom type vArpRetryMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_VArpRetryMax_Type.__name__ = "Integer32"
_VArpRetryMax_Object = MibScalar
vArpRetryMax = _VArpRetryMax_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 10, 3),
    _VArpRetryMax_Type()
)
vArpRetryMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vArpRetryMax.setStatus("mandatory")


class _VArpConfirmTimer_Type(Integer32):
    """Custom type vArpConfirmTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_VArpConfirmTimer_Type.__name__ = "Integer32"
_VArpConfirmTimer_Object = MibScalar
vArpConfirmTimer = _VArpConfirmTimer_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 10, 4),
    _VArpConfirmTimer_Type()
)
vArpConfirmTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vArpConfirmTimer.setStatus("mandatory")


class _VArpIdleTimeout_Type(Integer32):
    """Custom type vArpIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1800),
    )


_VArpIdleTimeout_Type.__name__ = "Integer32"
_VArpIdleTimeout_Object = MibScalar
vArpIdleTimeout = _VArpIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 10, 5),
    _VArpIdleTimeout_Type()
)
vArpIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vArpIdleTimeout.setStatus("mandatory")
_VcpTcp_ObjectIdentity = ObjectIdentity
vcpTcp = _VcpTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 11)
)


class _VTcpIpPrecedence_Type(Integer32):
    """Custom type vTcpIpPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VTcpIpPrecedence_Type.__name__ = "Integer32"
_VTcpIpPrecedence_Object = MibScalar
vTcpIpPrecedence = _VTcpIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 11, 1),
    _VTcpIpPrecedence_Type()
)
vTcpIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTcpIpPrecedence.setStatus("mandatory")


class _VTcpSendQSize_Type(Integer32):
    """Custom type vTcpSendQSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 8192),
    )


_VTcpSendQSize_Type.__name__ = "Integer32"
_VTcpSendQSize_Object = MibScalar
vTcpSendQSize = _VTcpSendQSize_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 11, 2),
    _VTcpSendQSize_Type()
)
vTcpSendQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTcpSendQSize.setStatus("mandatory")


class _VTcpRcvWinSize_Type(Integer32):
    """Custom type vTcpRcvWinSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 8192),
    )


_VTcpRcvWinSize_Type.__name__ = "Integer32"
_VTcpRcvWinSize_Object = MibScalar
vTcpRcvWinSize = _VTcpRcvWinSize_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 11, 3),
    _VTcpRcvWinSize_Type()
)
vTcpRcvWinSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTcpRcvWinSize.setStatus("mandatory")


class _VTcpSegSize_Type(Integer32):
    """Custom type vTcpSegSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 511),
    )


_VTcpSegSize_Type.__name__ = "Integer32"
_VTcpSegSize_Object = MibScalar
vTcpSegSize = _VTcpSegSize_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 11, 4),
    _VTcpSegSize_Type()
)
vTcpSegSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTcpSegSize.setStatus("mandatory")


class _VTcpTimerInterval_Type(Integer32):
    """Custom type vTcpTimerInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_VTcpTimerInterval_Type.__name__ = "Integer32"
_VTcpTimerInterval_Object = MibScalar
vTcpTimerInterval = _VTcpTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 11, 5),
    _VTcpTimerInterval_Type()
)
vTcpTimerInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTcpTimerInterval.setStatus("mandatory")


class _VTcpChecksumEnable_Type(Integer32):
    """Custom type vTcpChecksumEnable based on Integer32"""
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


_VTcpChecksumEnable_Type.__name__ = "Integer32"
_VTcpChecksumEnable_Object = MibScalar
vTcpChecksumEnable = _VTcpChecksumEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 11, 6),
    _VTcpChecksumEnable_Type()
)
vTcpChecksumEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTcpChecksumEnable.setStatus("mandatory")
_VcpTelnet_ObjectIdentity = ObjectIdentity
vcpTelnet = _VcpTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12)
)


class _VTelCourierEnable_Type(Integer32):
    """Custom type vTelCourierEnable based on Integer32"""
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


_VTelCourierEnable_Type.__name__ = "Integer32"
_VTelCourierEnable_Object = MibScalar
vTelCourierEnable = _VTelCourierEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 1),
    _VTelCourierEnable_Type()
)
vTelCourierEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelCourierEnable.setStatus("mandatory")


class _VTelCourierText_Type(OctetString):
    """Custom type vTelCourierText based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VTelCourierText_Type.__name__ = "OctetString"
_VTelCourierText_Object = MibScalar
vTelCourierText = _VTelCourierText_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 2),
    _VTelCourierText_Type()
)
vTelCourierText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelCourierText.setStatus("mandatory")
_VTelSessCurrNumber_Type = Integer32
_VTelSessCurrNumber_Object = MibScalar
vTelSessCurrNumber = _VTelSessCurrNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 3),
    _VTelSessCurrNumber_Type()
)
vTelSessCurrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessCurrNumber.setStatus("mandatory")
_VTelSessTable_Object = MibTable
vTelSessTable = _VTelSessTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4)
)
if mibBuilder.loadTexts:
    vTelSessTable.setStatus("mandatory")
_VTelSessEntry_Object = MibTableRow
vTelSessEntry = _VTelSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1)
)
vTelSessEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vTelSessPortIndex"),
    (0, "VCP-PRIVATE-MIB-VER-2", "vTelSessIndex"),
)
if mibBuilder.loadTexts:
    vTelSessEntry.setStatus("mandatory")
_VTelSessPortIndex_Type = Integer32
_VTelSessPortIndex_Object = MibTableColumn
vTelSessPortIndex = _VTelSessPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 1),
    _VTelSessPortIndex_Type()
)
vTelSessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessPortIndex.setStatus("mandatory")
_VTelSessIndex_Type = Integer32
_VTelSessIndex_Object = MibTableColumn
vTelSessIndex = _VTelSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 2),
    _VTelSessIndex_Type()
)
vTelSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessIndex.setStatus("mandatory")


class _VTelSessOrigin_Type(Integer32):
    """Custom type vTelSessOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("network", 2),
          ("unknown", 1))
    )


_VTelSessOrigin_Type.__name__ = "Integer32"
_VTelSessOrigin_Object = MibTableColumn
vTelSessOrigin = _VTelSessOrigin_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 3),
    _VTelSessOrigin_Type()
)
vTelSessOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessOrigin.setStatus("mandatory")


class _VTelSessState_Type(Integer32):
    """Custom type vTelSessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 2),
          ("starting", 1),
          ("stopping", 3))
    )


_VTelSessState_Type.__name__ = "Integer32"
_VTelSessState_Object = MibTableColumn
vTelSessState = _VTelSessState_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 4),
    _VTelSessState_Type()
)
vTelSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessState.setStatus("mandatory")


class _VTelSessDisconnect_Type(Integer32):
    """Custom type vTelSessDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_VTelSessDisconnect_Type.__name__ = "Integer32"
_VTelSessDisconnect_Object = MibTableColumn
vTelSessDisconnect = _VTelSessDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 5),
    _VTelSessDisconnect_Type()
)
vTelSessDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessDisconnect.setStatus("mandatory")
_VTelSessLocalAddr_Type = IpAddress
_VTelSessLocalAddr_Object = MibTableColumn
vTelSessLocalAddr = _VTelSessLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 6),
    _VTelSessLocalAddr_Type()
)
vTelSessLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessLocalAddr.setStatus("mandatory")


class _VTelSessLocalTcpPort_Type(Integer32):
    """Custom type vTelSessLocalTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VTelSessLocalTcpPort_Type.__name__ = "Integer32"
_VTelSessLocalTcpPort_Object = MibTableColumn
vTelSessLocalTcpPort = _VTelSessLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 7),
    _VTelSessLocalTcpPort_Type()
)
vTelSessLocalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessLocalTcpPort.setStatus("mandatory")
_VTelSessRemAddr_Type = IpAddress
_VTelSessRemAddr_Object = MibTableColumn
vTelSessRemAddr = _VTelSessRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 8),
    _VTelSessRemAddr_Type()
)
vTelSessRemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessRemAddr.setStatus("mandatory")


class _VTelSessRemTcpPort_Type(Integer32):
    """Custom type vTelSessRemTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VTelSessRemTcpPort_Type.__name__ = "Integer32"
_VTelSessRemTcpPort_Object = MibTableColumn
vTelSessRemTcpPort = _VTelSessRemTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 9),
    _VTelSessRemTcpPort_Type()
)
vTelSessRemTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessRemTcpPort.setStatus("mandatory")


class _VTelSessCrToNet_Type(OctetString):
    """Custom type vTelSessCrToNet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_VTelSessCrToNet_Type.__name__ = "OctetString"
_VTelSessCrToNet_Object = MibTableColumn
vTelSessCrToNet = _VTelSessCrToNet_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 10),
    _VTelSessCrToNet_Type()
)
vTelSessCrToNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessCrToNet.setStatus("mandatory")


class _VTelSessCrFromTerm_Type(OctetString):
    """Custom type vTelSessCrFromTerm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_VTelSessCrFromTerm_Type.__name__ = "OctetString"
_VTelSessCrFromTerm_Object = MibTableColumn
vTelSessCrFromTerm = _VTelSessCrFromTerm_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 11),
    _VTelSessCrFromTerm_Type()
)
vTelSessCrFromTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessCrFromTerm.setStatus("mandatory")
_VTelSessPadChar_Type = Character
_VTelSessPadChar_Object = MibTableColumn
vTelSessPadChar = _VTelSessPadChar_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 12),
    _VTelSessPadChar_Type()
)
vTelSessPadChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessPadChar.setStatus("mandatory")


class _VTelSessPadLength_Type(Integer32):
    """Custom type vTelSessPadLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VTelSessPadLength_Type.__name__ = "Integer32"
_VTelSessPadLength_Object = MibTableColumn
vTelSessPadLength = _VTelSessPadLength_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 13),
    _VTelSessPadLength_Type()
)
vTelSessPadLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessPadLength.setStatus("mandatory")


class _VTelSessUserTimeout_Type(Integer32):
    """Custom type vTelSessUserTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VTelSessUserTimeout_Type.__name__ = "Integer32"
_VTelSessUserTimeout_Object = MibTableColumn
vTelSessUserTimeout = _VTelSessUserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 14),
    _VTelSessUserTimeout_Type()
)
vTelSessUserTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessUserTimeout.setStatus("mandatory")


class _VTelSessKeepalive_Type(Integer32):
    """Custom type vTelSessKeepalive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VTelSessKeepalive_Type.__name__ = "Integer32"
_VTelSessKeepalive_Object = MibTableColumn
vTelSessKeepalive = _VTelSessKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 15),
    _VTelSessKeepalive_Type()
)
vTelSessKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessKeepalive.setStatus("mandatory")


class _VTelSessIpTTL_Type(Integer32):
    """Custom type vTelSessIpTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VTelSessIpTTL_Type.__name__ = "Integer32"
_VTelSessIpTTL_Object = MibTableColumn
vTelSessIpTTL = _VTelSessIpTTL_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 16),
    _VTelSessIpTTL_Type()
)
vTelSessIpTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessIpTTL.setStatus("mandatory")


class _VTelSessIpPrecedence_Type(Integer32):
    """Custom type vTelSessIpPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VTelSessIpPrecedence_Type.__name__ = "Integer32"
_VTelSessIpPrecedence_Object = MibTableColumn
vTelSessIpPrecedence = _VTelSessIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 17),
    _VTelSessIpPrecedence_Type()
)
vTelSessIpPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessIpPrecedence.setStatus("mandatory")
_VTelSessEndRecord_Type = Character
_VTelSessEndRecord_Object = MibTableColumn
vTelSessEndRecord = _VTelSessEndRecord_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 18),
    _VTelSessEndRecord_Type()
)
vTelSessEndRecord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessEndRecord.setStatus("mandatory")
_VTelSessNop_Type = Character
_VTelSessNop_Object = MibTableColumn
vTelSessNop = _VTelSessNop_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 19),
    _VTelSessNop_Type()
)
vTelSessNop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessNop.setStatus("mandatory")
_VTelSessDataMark_Type = Character
_VTelSessDataMark_Object = MibTableColumn
vTelSessDataMark = _VTelSessDataMark_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 20),
    _VTelSessDataMark_Type()
)
vTelSessDataMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessDataMark.setStatus("mandatory")
_VTelSessBreak_Type = Character
_VTelSessBreak_Object = MibTableColumn
vTelSessBreak = _VTelSessBreak_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 21),
    _VTelSessBreak_Type()
)
vTelSessBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessBreak.setStatus("mandatory")
_VTelSessIntProcess_Type = Character
_VTelSessIntProcess_Object = MibTableColumn
vTelSessIntProcess = _VTelSessIntProcess_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 22),
    _VTelSessIntProcess_Type()
)
vTelSessIntProcess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessIntProcess.setStatus("mandatory")
_VTelSessAbortOutput_Type = Character
_VTelSessAbortOutput_Object = MibTableColumn
vTelSessAbortOutput = _VTelSessAbortOutput_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 23),
    _VTelSessAbortOutput_Type()
)
vTelSessAbortOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessAbortOutput.setStatus("mandatory")
_VTelSessAttention_Type = Character
_VTelSessAttention_Object = MibTableColumn
vTelSessAttention = _VTelSessAttention_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 24),
    _VTelSessAttention_Type()
)
vTelSessAttention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessAttention.setStatus("mandatory")
_VTelSessEraseChar_Type = Character
_VTelSessEraseChar_Object = MibTableColumn
vTelSessEraseChar = _VTelSessEraseChar_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 25),
    _VTelSessEraseChar_Type()
)
vTelSessEraseChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessEraseChar.setStatus("mandatory")
_VTelSessEraseLine_Type = Character
_VTelSessEraseLine_Object = MibTableColumn
vTelSessEraseLine = _VTelSessEraseLine_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 26),
    _VTelSessEraseLine_Type()
)
vTelSessEraseLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessEraseLine.setStatus("mandatory")
_VTelSessGoAhead_Type = Character
_VTelSessGoAhead_Object = MibTableColumn
vTelSessGoAhead = _VTelSessGoAhead_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 27),
    _VTelSessGoAhead_Type()
)
vTelSessGoAhead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessGoAhead.setStatus("mandatory")


class _VTelSessNullPass_Type(Integer32):
    """Custom type vTelSessNullPass based on Integer32"""
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


_VTelSessNullPass_Type.__name__ = "Integer32"
_VTelSessNullPass_Object = MibTableColumn
vTelSessNullPass = _VTelSessNullPass_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 28),
    _VTelSessNullPass_Type()
)
vTelSessNullPass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vTelSessNullPass.setStatus("mandatory")


class _VTelSessTermType_Type(OctetString):
    """Custom type vTelSessTermType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VTelSessTermType_Type.__name__ = "OctetString"
_VTelSessTermType_Object = MibTableColumn
vTelSessTermType = _VTelSessTermType_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 29),
    _VTelSessTermType_Type()
)
vTelSessTermType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessTermType.setStatus("mandatory")


class _VTelSessLocalEcho_Type(Integer32):
    """Custom type vTelSessLocalEcho based on Integer32"""
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


_VTelSessLocalEcho_Type.__name__ = "Integer32"
_VTelSessLocalEcho_Object = MibTableColumn
vTelSessLocalEcho = _VTelSessLocalEcho_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 30),
    _VTelSessLocalEcho_Type()
)
vTelSessLocalEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessLocalEcho.setStatus("mandatory")


class _VTelSessRemoteEcho_Type(Integer32):
    """Custom type vTelSessRemoteEcho based on Integer32"""
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


_VTelSessRemoteEcho_Type.__name__ = "Integer32"
_VTelSessRemoteEcho_Object = MibTableColumn
vTelSessRemoteEcho = _VTelSessRemoteEcho_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 31),
    _VTelSessRemoteEcho_Type()
)
vTelSessRemoteEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessRemoteEcho.setStatus("mandatory")


class _VTelSessLocalBinary_Type(Integer32):
    """Custom type vTelSessLocalBinary based on Integer32"""
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


_VTelSessLocalBinary_Type.__name__ = "Integer32"
_VTelSessLocalBinary_Object = MibTableColumn
vTelSessLocalBinary = _VTelSessLocalBinary_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 32),
    _VTelSessLocalBinary_Type()
)
vTelSessLocalBinary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessLocalBinary.setStatus("mandatory")


class _VTelSessRemoteBinary_Type(Integer32):
    """Custom type vTelSessRemoteBinary based on Integer32"""
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


_VTelSessRemoteBinary_Type.__name__ = "Integer32"
_VTelSessRemoteBinary_Object = MibTableColumn
vTelSessRemoteBinary = _VTelSessRemoteBinary_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 12, 4, 1, 33),
    _VTelSessRemoteBinary_Type()
)
vTelSessRemoteBinary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vTelSessRemoteBinary.setStatus("mandatory")
_VcpRlogin_ObjectIdentity = ObjectIdentity
vcpRlogin = _VcpRlogin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13)
)
_VRlogSessCurrNumber_Type = Integer32
_VRlogSessCurrNumber_Object = MibScalar
vRlogSessCurrNumber = _VRlogSessCurrNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 1),
    _VRlogSessCurrNumber_Type()
)
vRlogSessCurrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRlogSessCurrNumber.setStatus("mandatory")
_VRlogSessTable_Object = MibTable
vRlogSessTable = _VRlogSessTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2)
)
if mibBuilder.loadTexts:
    vRlogSessTable.setStatus("mandatory")
_VRlogSessEntry_Object = MibTableRow
vRlogSessEntry = _VRlogSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2, 1)
)
vRlogSessEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vRlogSessPortIndex"),
    (0, "VCP-PRIVATE-MIB-VER-2", "vRlogSessIndex"),
)
if mibBuilder.loadTexts:
    vRlogSessEntry.setStatus("mandatory")
_VRlogSessPortIndex_Type = Integer32
_VRlogSessPortIndex_Object = MibTableColumn
vRlogSessPortIndex = _VRlogSessPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2, 1, 1),
    _VRlogSessPortIndex_Type()
)
vRlogSessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRlogSessPortIndex.setStatus("mandatory")
_VRlogSessIndex_Type = Integer32
_VRlogSessIndex_Object = MibTableColumn
vRlogSessIndex = _VRlogSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2, 1, 2),
    _VRlogSessIndex_Type()
)
vRlogSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRlogSessIndex.setStatus("mandatory")


class _VRlogSessOrigin_Type(Integer32):
    """Custom type vRlogSessOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("network", 2),
          ("unknown", 1))
    )


_VRlogSessOrigin_Type.__name__ = "Integer32"
_VRlogSessOrigin_Object = MibTableColumn
vRlogSessOrigin = _VRlogSessOrigin_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2, 1, 3),
    _VRlogSessOrigin_Type()
)
vRlogSessOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRlogSessOrigin.setStatus("mandatory")


class _VRlogSessState_Type(Integer32):
    """Custom type vRlogSessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 2),
          ("starting", 1),
          ("stopping", 3))
    )


_VRlogSessState_Type.__name__ = "Integer32"
_VRlogSessState_Object = MibTableColumn
vRlogSessState = _VRlogSessState_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2, 1, 4),
    _VRlogSessState_Type()
)
vRlogSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRlogSessState.setStatus("mandatory")


class _VRlogSessDisconnect_Type(Integer32):
    """Custom type vRlogSessDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_VRlogSessDisconnect_Type.__name__ = "Integer32"
_VRlogSessDisconnect_Object = MibTableColumn
vRlogSessDisconnect = _VRlogSessDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2, 1, 5),
    _VRlogSessDisconnect_Type()
)
vRlogSessDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRlogSessDisconnect.setStatus("mandatory")
_VRlogSessLocalAddr_Type = IpAddress
_VRlogSessLocalAddr_Object = MibTableColumn
vRlogSessLocalAddr = _VRlogSessLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2, 1, 6),
    _VRlogSessLocalAddr_Type()
)
vRlogSessLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRlogSessLocalAddr.setStatus("mandatory")


class _VRlogSessLocalTcpPort_Type(Integer32):
    """Custom type vRlogSessLocalTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRlogSessLocalTcpPort_Type.__name__ = "Integer32"
_VRlogSessLocalTcpPort_Object = MibTableColumn
vRlogSessLocalTcpPort = _VRlogSessLocalTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2, 1, 7),
    _VRlogSessLocalTcpPort_Type()
)
vRlogSessLocalTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRlogSessLocalTcpPort.setStatus("mandatory")
_VRlogSessRemAddr_Type = IpAddress
_VRlogSessRemAddr_Object = MibTableColumn
vRlogSessRemAddr = _VRlogSessRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2, 1, 8),
    _VRlogSessRemAddr_Type()
)
vRlogSessRemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRlogSessRemAddr.setStatus("mandatory")


class _VRlogSessRemTcpPort_Type(Integer32):
    """Custom type vRlogSessRemTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRlogSessRemTcpPort_Type.__name__ = "Integer32"
_VRlogSessRemTcpPort_Object = MibTableColumn
vRlogSessRemTcpPort = _VRlogSessRemTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2, 1, 9),
    _VRlogSessRemTcpPort_Type()
)
vRlogSessRemTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRlogSessRemTcpPort.setStatus("mandatory")


class _VRlogSessTermType_Type(OctetString):
    """Custom type vRlogSessTermType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VRlogSessTermType_Type.__name__ = "OctetString"
_VRlogSessTermType_Object = MibTableColumn
vRlogSessTermType = _VRlogSessTermType_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 13, 2, 1, 10),
    _VRlogSessTermType_Type()
)
vRlogSessTermType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRlogSessTermType.setStatus("mandatory")
_VcpLt_ObjectIdentity = ObjectIdentity
vcpLt = _VcpLt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14)
)


class _VLtNodeName_Type(DisplayString):
    """Custom type vLtNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_VLtNodeName_Type.__name__ = "DisplayString"
_VLtNodeName_Object = MibScalar
vLtNodeName = _VLtNodeName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 1),
    _VLtNodeName_Type()
)
vLtNodeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtNodeName.setStatus("optional")


class _VLtNodeID_Type(DisplayString):
    """Custom type vLtNodeID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VLtNodeID_Type.__name__ = "DisplayString"
_VLtNodeID_Object = MibScalar
vLtNodeID = _VLtNodeID_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 2),
    _VLtNodeID_Type()
)
vLtNodeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtNodeID.setStatus("optional")
_VLtNodeGroups_Type = LtGroupList
_VLtNodeGroups_Object = MibScalar
vLtNodeGroups = _VLtNodeGroups_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 3),
    _VLtNodeGroups_Type()
)
vLtNodeGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtNodeGroups.setStatus("optional")


class _VLtNumber_Type(Integer32):
    """Custom type vLtNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VLtNumber_Type.__name__ = "Integer32"
_VLtNumber_Object = MibScalar
vLtNumber = _VLtNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 4),
    _VLtNumber_Type()
)
vLtNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtNumber.setStatus("optional")


class _VLtMcastEnable_Type(Integer32):
    """Custom type vLtMcastEnable based on Integer32"""
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


_VLtMcastEnable_Type.__name__ = "Integer32"
_VLtMcastEnable_Object = MibScalar
vLtMcastEnable = _VLtMcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 5),
    _VLtMcastEnable_Type()
)
vLtMcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtMcastEnable.setStatus("optional")


class _VLtMcastTimer_Type(Integer32):
    """Custom type vLtMcastTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_VLtMcastTimer_Type.__name__ = "Integer32"
_VLtMcastTimer_Object = MibScalar
vLtMcastTimer = _VLtMcastTimer_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 6),
    _VLtMcastTimer_Type()
)
vLtMcastTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtMcastTimer.setStatus("optional")


class _VLtCktTimer_Type(Integer32):
    """Custom type vLtCktTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_VLtCktTimer_Type.__name__ = "Integer32"
_VLtCktTimer_Object = MibScalar
vLtCktTimer = _VLtCktTimer_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 7),
    _VLtCktTimer_Type()
)
vLtCktTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtCktTimer.setStatus("optional")


class _VLtKeepaliveTimer_Type(Integer32):
    """Custom type vLtKeepaliveTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_VLtKeepaliveTimer_Type.__name__ = "Integer32"
_VLtKeepaliveTimer_Object = MibScalar
vLtKeepaliveTimer = _VLtKeepaliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 8),
    _VLtKeepaliveTimer_Type()
)
vLtKeepaliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtKeepaliveTimer.setStatus("optional")


class _VLtMaxRetran_Type(Integer32):
    """Custom type vLtMaxRetran based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 120),
    )


_VLtMaxRetran_Type.__name__ = "Integer32"
_VLtMaxRetran_Object = MibScalar
vLtMaxRetran = _VLtMaxRetran_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 9),
    _VLtMaxRetran_Type()
)
vLtMaxRetran.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtMaxRetran.setStatus("optional")


class _VLtSlotPerCkt_Type(Integer32):
    """Custom type vLtSlotPerCkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VLtSlotPerCkt_Type.__name__ = "Integer32"
_VLtSlotPerCkt_Object = MibScalar
vLtSlotPerCkt = _VLtSlotPerCkt_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 10),
    _VLtSlotPerCkt_Type()
)
vLtSlotPerCkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtSlotPerCkt.setStatus("optional")


class _VLtMaxNodes_Type(Integer32):
    """Custom type vLtMaxNodes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1024),
    )


_VLtMaxNodes_Type.__name__ = "Integer32"
_VLtMaxNodes_Object = MibScalar
vLtMaxNodes = _VLtMaxNodes_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 11),
    _VLtMaxNodes_Type()
)
vLtMaxNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtMaxNodes.setStatus("optional")


class _VLtMaxSvcs_Type(Integer32):
    """Custom type vLtMaxSvcs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 2048),
    )


_VLtMaxSvcs_Type.__name__ = "Integer32"
_VLtMaxSvcs_Object = MibScalar
vLtMaxSvcs = _VLtMaxSvcs_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 12),
    _VLtMaxSvcs_Type()
)
vLtMaxSvcs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtMaxSvcs.setStatus("optional")


class _VLtMaxCkts_Type(Integer32):
    """Custom type vLtMaxCkts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_VLtMaxCkts_Type.__name__ = "Integer32"
_VLtMaxCkts_Object = MibScalar
vLtMaxCkts = _VLtMaxCkts_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 13),
    _VLtMaxCkts_Type()
)
vLtMaxCkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtMaxCkts.setStatus("optional")
_VLtSessCurrNumber_Type = Integer32
_VLtSessCurrNumber_Object = MibScalar
vLtSessCurrNumber = _VLtSessCurrNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 14),
    _VLtSessCurrNumber_Type()
)
vLtSessCurrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtSessCurrNumber.setStatus("optional")
_VLtSessTable_Object = MibTable
vLtSessTable = _VLtSessTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 15)
)
if mibBuilder.loadTexts:
    vLtSessTable.setStatus("optional")
_VLtSessEntry_Object = MibTableRow
vLtSessEntry = _VLtSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 15, 1)
)
vLtSessEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vLtSessIndex"),
)
if mibBuilder.loadTexts:
    vLtSessEntry.setStatus("optional")
_VLtSessPortIndex_Type = Integer32
_VLtSessPortIndex_Object = MibTableColumn
vLtSessPortIndex = _VLtSessPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 15, 1, 1),
    _VLtSessPortIndex_Type()
)
vLtSessPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtSessPortIndex.setStatus("optional")
_VLtSessIndex_Type = Integer32
_VLtSessIndex_Object = MibTableColumn
vLtSessIndex = _VLtSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 15, 1, 2),
    _VLtSessIndex_Type()
)
vLtSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtSessIndex.setStatus("optional")


class _VLtSessOrigin_Type(Integer32):
    """Custom type vLtSessOrigin based on Integer32"""
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
        *(("local", 3),
          ("network", 2),
          ("remote-port", 4),
          ("unknown", 1))
    )


_VLtSessOrigin_Type.__name__ = "Integer32"
_VLtSessOrigin_Object = MibTableColumn
vLtSessOrigin = _VLtSessOrigin_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 15, 1, 3),
    _VLtSessOrigin_Type()
)
vLtSessOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtSessOrigin.setStatus("optional")


class _VLtSessState_Type(Integer32):
    """Custom type vLtSessState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 2),
          ("starting", 1),
          ("stopping", 3))
    )


_VLtSessState_Type.__name__ = "Integer32"
_VLtSessState_Object = MibTableColumn
vLtSessState = _VLtSessState_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 15, 1, 4),
    _VLtSessState_Type()
)
vLtSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtSessState.setStatus("optional")


class _VLtSessDisconnect_Type(Integer32):
    """Custom type vLtSessDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_VLtSessDisconnect_Type.__name__ = "Integer32"
_VLtSessDisconnect_Object = MibTableColumn
vLtSessDisconnect = _VLtSessDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 15, 1, 5),
    _VLtSessDisconnect_Type()
)
vLtSessDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vLtSessDisconnect.setStatus("optional")
_VLtSessSvcName_Type = DisplayString
_VLtSessSvcName_Object = MibTableColumn
vLtSessSvcName = _VLtSessSvcName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 15, 1, 6),
    _VLtSessSvcName_Type()
)
vLtSessSvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtSessSvcName.setStatus("optional")
_VLtSessNodeName_Type = DisplayString
_VLtSessNodeName_Object = MibTableColumn
vLtSessNodeName = _VLtSessNodeName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 15, 1, 7),
    _VLtSessNodeName_Type()
)
vLtSessNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtSessNodeName.setStatus("optional")
_VLtSessDestName_Type = DisplayString
_VLtSessDestName_Object = MibTableColumn
vLtSessDestName = _VLtSessDestName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 15, 1, 8),
    _VLtSessDestName_Type()
)
vLtSessDestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtSessDestName.setStatus("optional")
_VLtTotalRcvPkts_Type = Counter32
_VLtTotalRcvPkts_Object = MibScalar
vLtTotalRcvPkts = _VLtTotalRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 16),
    _VLtTotalRcvPkts_Type()
)
vLtTotalRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtTotalRcvPkts.setStatus("optional")
_VLtTotalTrnPkts_Type = Counter32
_VLtTotalTrnPkts_Object = MibScalar
vLtTotalTrnPkts = _VLtTotalTrnPkts_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 17),
    _VLtTotalTrnPkts_Type()
)
vLtTotalTrnPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtTotalTrnPkts.setStatus("optional")
_VLtTotalRetranPkts_Type = Counter32
_VLtTotalRetranPkts_Object = MibScalar
vLtTotalRetranPkts = _VLtTotalRetranPkts_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 18),
    _VLtTotalRetranPkts_Type()
)
vLtTotalRetranPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtTotalRetranPkts.setStatus("optional")
_VLtRcvCorruptPkts_Type = Counter32
_VLtRcvCorruptPkts_Object = MibScalar
vLtRcvCorruptPkts = _VLtRcvCorruptPkts_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 19),
    _VLtRcvCorruptPkts_Type()
)
vLtRcvCorruptPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtRcvCorruptPkts.setStatus("optional")
_VLtRcvCorruptMcasts_Type = Counter32
_VLtRcvCorruptMcasts_Object = MibScalar
vLtRcvCorruptMcasts = _VLtRcvCorruptMcasts_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 20),
    _VLtRcvCorruptMcasts_Type()
)
vLtRcvCorruptMcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtRcvCorruptMcasts.setStatus("optional")
_VLtRcvDuplicatePkts_Type = Counter32
_VLtRcvDuplicatePkts_Object = MibScalar
vLtRcvDuplicatePkts = _VLtRcvDuplicatePkts_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 21),
    _VLtRcvDuplicatePkts_Type()
)
vLtRcvDuplicatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtRcvDuplicatePkts.setStatus("optional")
_VLtReqAccepted_Type = Counter32
_VLtReqAccepted_Object = MibScalar
vLtReqAccepted = _VLtReqAccepted_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 22),
    _VLtReqAccepted_Type()
)
vLtReqAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtReqAccepted.setStatus("optional")
_VLtReqRejected_Type = Counter32
_VLtReqRejected_Object = MibScalar
vLtReqRejected = _VLtReqRejected_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 23),
    _VLtReqRejected_Type()
)
vLtReqRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtReqRejected.setStatus("optional")
_VLtTotalNodeDiscards_Type = Counter32
_VLtTotalNodeDiscards_Object = MibScalar
vLtTotalNodeDiscards = _VLtTotalNodeDiscards_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 14, 24),
    _VLtTotalNodeDiscards_Type()
)
vLtTotalNodeDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vLtTotalNodeDiscards.setStatus("optional")
_VcpQueue_ObjectIdentity = ObjectIdentity
vcpQueue = _VcpQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 15)
)


class _VQueMaxEntries_Type(Integer32):
    """Custom type vQueMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_VQueMaxEntries_Type.__name__ = "Integer32"
_VQueMaxEntries_Object = MibScalar
vQueMaxEntries = _VQueMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 15, 1),
    _VQueMaxEntries_Type()
)
vQueMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vQueMaxEntries.setStatus("optional")
_VQueCurrNumber_Type = Integer32
_VQueCurrNumber_Object = MibScalar
vQueCurrNumber = _VQueCurrNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 15, 2),
    _VQueCurrNumber_Type()
)
vQueCurrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vQueCurrNumber.setStatus("optional")
_VQueTable_Object = MibTable
vQueTable = _VQueTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 15, 3)
)
if mibBuilder.loadTexts:
    vQueTable.setStatus("optional")
_VQueEntry_Object = MibTableRow
vQueEntry = _VQueEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 15, 3, 1)
)
vQueEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vQueEntryNumber"),
)
if mibBuilder.loadTexts:
    vQueEntry.setStatus("optional")


class _VQueEntryNumber_Type(Integer32):
    """Custom type vQueEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VQueEntryNumber_Type.__name__ = "Integer32"
_VQueEntryNumber_Object = MibTableColumn
vQueEntryNumber = _VQueEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 15, 3, 1, 1),
    _VQueEntryNumber_Type()
)
vQueEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vQueEntryNumber.setStatus("optional")
_VQueSvcName_Type = OctetString
_VQueSvcName_Object = MibTableColumn
vQueSvcName = _VQueSvcName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 15, 3, 1, 2),
    _VQueSvcName_Type()
)
vQueSvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vQueSvcName.setStatus("optional")
_VQueNodeName_Type = OctetString
_VQueNodeName_Object = MibTableColumn
vQueNodeName = _VQueNodeName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 15, 3, 1, 3),
    _VQueNodeName_Type()
)
vQueNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vQueNodeName.setStatus("optional")
_VQuePortName_Type = OctetString
_VQuePortName_Object = MibTableColumn
vQuePortName = _VQuePortName_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 15, 3, 1, 4),
    _VQuePortName_Type()
)
vQuePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vQuePortName.setStatus("optional")


class _VQueStatus_Type(Integer32):
    """Custom type vQueStatus based on Integer32"""
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


_VQueStatus_Type.__name__ = "Integer32"
_VQueStatus_Object = MibTableColumn
vQueStatus = _VQueStatus_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 15, 3, 1, 5),
    _VQueStatus_Type()
)
vQueStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vQueStatus.setStatus("optional")
_VcpSnmp_ObjectIdentity = ObjectIdentity
vcpSnmp = _VcpSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16)
)


class _VSnmpReadCommunity_Type(OctetString):
    """Custom type vSnmpReadCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_VSnmpReadCommunity_Type.__name__ = "OctetString"
_VSnmpReadCommunity_Object = MibScalar
vSnmpReadCommunity = _VSnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 1),
    _VSnmpReadCommunity_Type()
)
vSnmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSnmpReadCommunity.setStatus("mandatory")


class _VSnmpWriteCommunity_Type(OctetString):
    """Custom type vSnmpWriteCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_VSnmpWriteCommunity_Type.__name__ = "OctetString"
_VSnmpWriteCommunity_Object = MibScalar
vSnmpWriteCommunity = _VSnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 2),
    _VSnmpWriteCommunity_Type()
)
vSnmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSnmpWriteCommunity.setStatus("mandatory")


class _VSnmpReadWriteCommunity_Type(OctetString):
    """Custom type vSnmpReadWriteCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_VSnmpReadWriteCommunity_Type.__name__ = "OctetString"
_VSnmpReadWriteCommunity_Object = MibScalar
vSnmpReadWriteCommunity = _VSnmpReadWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 3),
    _VSnmpReadWriteCommunity_Type()
)
vSnmpReadWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSnmpReadWriteCommunity.setStatus("mandatory")


class _VSnmpWriteEnable_Type(Integer32):
    """Custom type vSnmpWriteEnable based on Integer32"""
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


_VSnmpWriteEnable_Type.__name__ = "Integer32"
_VSnmpWriteEnable_Object = MibScalar
vSnmpWriteEnable = _VSnmpWriteEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 4),
    _VSnmpWriteEnable_Type()
)
vSnmpWriteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSnmpWriteEnable.setStatus("mandatory")
_VSnmpTrapDestCurrNumber_Type = Integer32
_VSnmpTrapDestCurrNumber_Object = MibScalar
vSnmpTrapDestCurrNumber = _VSnmpTrapDestCurrNumber_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 5),
    _VSnmpTrapDestCurrNumber_Type()
)
vSnmpTrapDestCurrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSnmpTrapDestCurrNumber.setStatus("mandatory")
_VSnmpTrapDestTable_Object = MibTable
vSnmpTrapDestTable = _VSnmpTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 6)
)
if mibBuilder.loadTexts:
    vSnmpTrapDestTable.setStatus("mandatory")
_VSnmpTrapDestEntry_Object = MibTableRow
vSnmpTrapDestEntry = _VSnmpTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 6, 1)
)
vSnmpTrapDestEntry.setIndexNames(
    (0, "VCP-PRIVATE-MIB-VER-2", "vSnmpTrapDestAddr"),
)
if mibBuilder.loadTexts:
    vSnmpTrapDestEntry.setStatus("mandatory")
_VSnmpTrapDestAddr_Type = IpAddress
_VSnmpTrapDestAddr_Object = MibTableColumn
vSnmpTrapDestAddr = _VSnmpTrapDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 6, 1, 1),
    _VSnmpTrapDestAddr_Type()
)
vSnmpTrapDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSnmpTrapDestAddr.setStatus("mandatory")


class _VSnmpTrapDestCommunity_Type(Integer32):
    """Custom type vSnmpTrapDestCommunity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("read", 1),
          ("readwrite", 3),
          ("write", 2))
    )


_VSnmpTrapDestCommunity_Type.__name__ = "Integer32"
_VSnmpTrapDestCommunity_Object = MibTableColumn
vSnmpTrapDestCommunity = _VSnmpTrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 6, 1, 2),
    _VSnmpTrapDestCommunity_Type()
)
vSnmpTrapDestCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSnmpTrapDestCommunity.setStatus("mandatory")


class _VSnmpTrapDestColdEnable_Type(Integer32):
    """Custom type vSnmpTrapDestColdEnable based on Integer32"""
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


_VSnmpTrapDestColdEnable_Type.__name__ = "Integer32"
_VSnmpTrapDestColdEnable_Object = MibTableColumn
vSnmpTrapDestColdEnable = _VSnmpTrapDestColdEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 6, 1, 3),
    _VSnmpTrapDestColdEnable_Type()
)
vSnmpTrapDestColdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSnmpTrapDestColdEnable.setStatus("mandatory")


class _VSnmpTrapDestAuthEnable_Type(Integer32):
    """Custom type vSnmpTrapDestAuthEnable based on Integer32"""
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


_VSnmpTrapDestAuthEnable_Type.__name__ = "Integer32"
_VSnmpTrapDestAuthEnable_Object = MibTableColumn
vSnmpTrapDestAuthEnable = _VSnmpTrapDestAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 6, 1, 4),
    _VSnmpTrapDestAuthEnable_Type()
)
vSnmpTrapDestAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSnmpTrapDestAuthEnable.setStatus("mandatory")


class _VSnmpTrapDestStatus_Type(Integer32):
    """Custom type vSnmpTrapDestStatus based on Integer32"""
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


_VSnmpTrapDestStatus_Type.__name__ = "Integer32"
_VSnmpTrapDestStatus_Object = MibTableColumn
vSnmpTrapDestStatus = _VSnmpTrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 85, 6, 1, 1, 16, 6, 1, 5),
    _VSnmpTrapDestStatus_Type()
)
vSnmpTrapDestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vSnmpTrapDestStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VCP-PRIVATE-MIB-VER-2",
    **{"Character": Character,
       "DisplayChar": DisplayChar,
       "LtGroupList": LtGroupList,
       "datability": datability,
       "port": port,
       "server": server,
       "service": service,
       "slot": slot,
       "dssAdmin": dssAdmin,
       "dssDevice": dssDevice,
       "vcp-1000": vcp_1000,
       "vcp-200": vcp_200,
       "vcp-300": vcp_300,
       "dssProtocol": dssProtocol,
       "dssNone": dssNone,
       "dssTelnet": dssTelnet,
       "dssRlogin": dssRlogin,
       "dssLt": dssLt,
       "dssMibs": dssMibs,
       "dssServerMibs": dssServerMibs,
       "vcpMib": vcpMib,
       "vcpSystem": vcpSystem,
       "vSysIdentifier": vSysIdentifier,
       "vSysReboot": vSysReboot,
       "vSysLtGroupStatus": vSysLtGroupStatus,
       "vSysPrimaryBoot": vSysPrimaryBoot,
       "vSysSecondaryBoot": vSysSecondaryBoot,
       "vSysBootFilePath": vSysBootFilePath,
       "vSysBootFileName": vSysBootFileName,
       "vSysBootServer": vSysBootServer,
       "vSysRemoteBoot": vSysRemoteBoot,
       "vSysEtherType": vSysEtherType,
       "vSysBroadband": vSysBroadband,
       "vSysPasswordLimit": vSysPasswordLimit,
       "vSysPrivPassword": vSysPrivPassword,
       "vSysMaintenancePassword": vSysMaintenancePassword,
       "vcpPort": vcpPort,
       "vPortBroadcast": vPortBroadcast,
       "vPortInactivityTimer": vPortInactivityTimer,
       "vPortAbsoluteTimer": vPortAbsoluteTimer,
       "vPortLock": vPortLock,
       "vPortLoginPassword": vPortLoginPassword,
       "vPortConsoleIndex": vPortConsoleIndex,
       "vPortFailover": vPortFailover,
       "vPortSignalCheck": vPortSignalCheck,
       "vPortLoginMsgEnable": vPortLoginMsgEnable,
       "vPortBreakDuration": vPortBreakDuration,
       "vPortXoffMark": vPortXoffMark,
       "vPortXonMark": vPortXonMark,
       "vPortNumber": vPortNumber,
       "vPortTable": vPortTable,
       "vPortEntry": vPortEntry,
       "vPortIndex": vPortIndex,
       "vPortType": vPortType,
       "vPortName": vPortName,
       "vPortUserName": vPortUserName,
       "vPortState": vPortState,
       "vPortLogout": vPortLogout,
       "vPortActiveSessions": vPortActiveSessions,
       "vPortCurrSessNumber": vPortCurrSessNumber,
       "vPortCurrSessProt": vPortCurrSessProt,
       "vPortAccess": vPortAccess,
       "vPortVirtualEnable": vPortVirtualEnable,
       "vPortVirtualString": vPortVirtualString,
       "vPortSessionLimit": vPortSessionLimit,
       "vPortProfile": vPortProfile,
       "vPortQueueing": vPortQueueing,
       "vPortPasswordEnable": vPortPasswordEnable,
       "vPortTacacsEnable": vPortTacacsEnable,
       "vPortSecurityEnable": vPortSecurityEnable,
       "vPortGroups": vPortGroups,
       "vPortBreakMode": vPortBreakMode,
       "vPortBackSwitch": vPortBackSwitch,
       "vPortForwSwitch": vPortForwSwitch,
       "vPortLocalSwitch": vPortLocalSwitch,
       "vPortPrefSvc": vPortPrefSvc,
       "vPortPrefNode": vPortPrefNode,
       "vPortPrefPort": vPortPrefPort,
       "vPortPrefMode": vPortPrefMode,
       "vPortAutoConnect": vPortAutoConnect,
       "vPortPrompt": vPortPrompt,
       "vPortInactiveLogout": vPortInactiveLogout,
       "vPortAutoPrompt": vPortAutoPrompt,
       "vPortBroadcastEnable": vPortBroadcastEnable,
       "vPortInterrupts": vPortInterrupts,
       "vPortMessageCodes": vPortMessageCodes,
       "vPortVerification": vPortVerification,
       "vPortDialup": vPortDialup,
       "vPortRemoteModify": vPortRemoteModify,
       "vPortAbsoluteLogout": vPortAbsoluteLogout,
       "vPortIOflush": vPortIOflush,
       "vPortLogoutMsgEnable": vPortLogoutMsgEnable,
       "vPortScreenType": vPortScreenType,
       "vPortFlowType": vPortFlowType,
       "vPortInFlowState": vPortInFlowState,
       "vPortOutFlowState": vPortOutFlowState,
       "vPortCTSstate": vPortCTSstate,
       "vPortDSRstate": vPortDSRstate,
       "vPortDCDstate": vPortDCDstate,
       "vPortDTRstate": vPortDTRstate,
       "vPortRIstate": vPortRIstate,
       "vPortRTSstate": vPortRTSstate,
       "vPortSpeed": vPortSpeed,
       "vPortCharSize": vPortCharSize,
       "vPortParityType": vPortParityType,
       "vPortAutobaud": vPortAutobaud,
       "vPortModemControl": vPortModemControl,
       "vPortDSRlogout": vPortDSRlogout,
       "vPortRing": vPortRing,
       "vPortDTRwait": vPortDTRwait,
       "vPortSignalCheckEnable": vPortSignalCheckEnable,
       "vPortHandshake": vPortHandshake,
       "vPortRcvChars": vPortRcvChars,
       "vPortTrnChars": vPortTrnChars,
       "vPortFrameErrs": vPortFrameErrs,
       "vPortOverrunErrs": vPortOverrunErrs,
       "vPortParityErrs": vPortParityErrs,
       "vPortCharsDropped": vPortCharsDropped,
       "vcpService": vcpService,
       "vSvcRatingMode": vSvcRatingMode,
       "vSvcCurrNumber": vSvcCurrNumber,
       "vSvcTable": vSvcTable,
       "vSvcEntry": vSvcEntry,
       "vSvcName": vSvcName,
       "vSvcPorts": vSvcPorts,
       "vSvcIdent": vSvcIdent,
       "vSvcRating": vSvcRating,
       "vSvcLtEnable": vSvcLtEnable,
       "vSvcTelEnable": vSvcTelEnable,
       "vSvcLprEnable": vSvcLprEnable,
       "vSvcRawEnable": vSvcRawEnable,
       "vSvcVirtualEnable": vSvcVirtualEnable,
       "vSvcVirtualText": vSvcVirtualText,
       "vSvcConnectEnable": vSvcConnectEnable,
       "vSvcPassword": vSvcPassword,
       "vSvcQueueEnable": vSvcQueueEnable,
       "vSvcIpAddr": vSvcIpAddr,
       "vSvcTcpPort": vSvcTcpPort,
       "vSvcProfile": vSvcProfile,
       "vSvcStatus": vSvcStatus,
       "vcpProfile": vcpProfile,
       "vProfCurrNumber": vProfCurrNumber,
       "vProfTable": vProfTable,
       "vProfEntry": vProfEntry,
       "vProfName": vProfName,
       "vProfDomain": vProfDomain,
       "vProfConcatenate": vProfConcatenate,
       "vProfPermHostOnly": vProfPermHostOnly,
       "vProfTcpPort": vProfTcpPort,
       "vProfTcpTimeout": vProfTcpTimeout,
       "vProfTcpKeepalive": vProfTcpKeepalive,
       "vProfIpTTL": vProfIpTTL,
       "vProfIpPrecedence": vProfIpPrecedence,
       "vProfTermType": vProfTermType,
       "vProfCrToNet": vProfCrToNet,
       "vProfCrFromTerm": vProfCrFromTerm,
       "vProfPadChar": vProfPadChar,
       "vProfPadLength": vProfPadLength,
       "vProfEndRecord": vProfEndRecord,
       "vProfNop": vProfNop,
       "vProfDataMark": vProfDataMark,
       "vProfBreak": vProfBreak,
       "vProfIntProcess": vProfIntProcess,
       "vProfAbortOutput": vProfAbortOutput,
       "vProfAttention": vProfAttention,
       "vProfEraseChar": vProfEraseChar,
       "vProfEraseLine": vProfEraseLine,
       "vProfGoAhead": vProfGoAhead,
       "vProfNullPass": vProfNullPass,
       "vProfLocalEcho": vProfLocalEcho,
       "vProfRemoteEcho": vProfRemoteEcho,
       "vProfLocalBinary": vProfLocalBinary,
       "vProfRemoteBinary": vProfRemoteBinary,
       "vProfStatus": vProfStatus,
       "vcpIpSecurity": vcpIpSecurity,
       "vSecEnable": vSecEnable,
       "vSecCurrNumber": vSecCurrNumber,
       "vSecTable": vSecTable,
       "vSecEntry": vSecEntry,
       "vSecIndex": vSecIndex,
       "vSecAddress": vSecAddress,
       "vSecMask": vSecMask,
       "vSecGroups": vSecGroups,
       "vSecStatus": vSecStatus,
       "vcpHostname": vcpHostname,
       "vHostCurrNumber": vHostCurrNumber,
       "vHostTable": vHostTable,
       "vHostEntry": vHostEntry,
       "vHostHostname": vHostHostname,
       "vHostAddress": vHostAddress,
       "vHostTTL": vHostTTL,
       "vHostStatus": vHostStatus,
       "vcpNameserver": vcpNameserver,
       "vNsRequestMode": vNsRequestMode,
       "vNsAllowLowerCase": vNsAllowLowerCase,
       "vNsCurrNumber": vNsCurrNumber,
       "vNsTable": vNsTable,
       "vNsEntry": vNsEntry,
       "vNsAddress": vNsAddress,
       "vNsHostname": vNsHostname,
       "vNsTTL": vNsTTL,
       "vNsStatus": vNsStatus,
       "vcpTacacs": vcpTacacs,
       "vTacServerCurrNumber": vTacServerCurrNumber,
       "vTacTable": vTacTable,
       "vTacEntry": vTacEntry,
       "vTacAddress": vTacAddress,
       "vTacHostname": vTacHostname,
       "vTacStatus": vTacStatus,
       "vcpIp": vcpIp,
       "vIpBcastAddr": vIpBcastAddr,
       "vIpMaxAddr": vIpMaxAddr,
       "vIpMaxHostHashEntries": vIpMaxHostHashEntries,
       "vIpMaxNetHashEntries": vIpMaxNetHashEntries,
       "vIpMaxInterfaces": vIpMaxInterfaces,
       "vIpMaxRoutes": vIpMaxRoutes,
       "vcpArp": vcpArp,
       "vArpMaxEntries": vArpMaxEntries,
       "vArpRetryTimeout": vArpRetryTimeout,
       "vArpRetryMax": vArpRetryMax,
       "vArpConfirmTimer": vArpConfirmTimer,
       "vArpIdleTimeout": vArpIdleTimeout,
       "vcpTcp": vcpTcp,
       "vTcpIpPrecedence": vTcpIpPrecedence,
       "vTcpSendQSize": vTcpSendQSize,
       "vTcpRcvWinSize": vTcpRcvWinSize,
       "vTcpSegSize": vTcpSegSize,
       "vTcpTimerInterval": vTcpTimerInterval,
       "vTcpChecksumEnable": vTcpChecksumEnable,
       "vcpTelnet": vcpTelnet,
       "vTelCourierEnable": vTelCourierEnable,
       "vTelCourierText": vTelCourierText,
       "vTelSessCurrNumber": vTelSessCurrNumber,
       "vTelSessTable": vTelSessTable,
       "vTelSessEntry": vTelSessEntry,
       "vTelSessPortIndex": vTelSessPortIndex,
       "vTelSessIndex": vTelSessIndex,
       "vTelSessOrigin": vTelSessOrigin,
       "vTelSessState": vTelSessState,
       "vTelSessDisconnect": vTelSessDisconnect,
       "vTelSessLocalAddr": vTelSessLocalAddr,
       "vTelSessLocalTcpPort": vTelSessLocalTcpPort,
       "vTelSessRemAddr": vTelSessRemAddr,
       "vTelSessRemTcpPort": vTelSessRemTcpPort,
       "vTelSessCrToNet": vTelSessCrToNet,
       "vTelSessCrFromTerm": vTelSessCrFromTerm,
       "vTelSessPadChar": vTelSessPadChar,
       "vTelSessPadLength": vTelSessPadLength,
       "vTelSessUserTimeout": vTelSessUserTimeout,
       "vTelSessKeepalive": vTelSessKeepalive,
       "vTelSessIpTTL": vTelSessIpTTL,
       "vTelSessIpPrecedence": vTelSessIpPrecedence,
       "vTelSessEndRecord": vTelSessEndRecord,
       "vTelSessNop": vTelSessNop,
       "vTelSessDataMark": vTelSessDataMark,
       "vTelSessBreak": vTelSessBreak,
       "vTelSessIntProcess": vTelSessIntProcess,
       "vTelSessAbortOutput": vTelSessAbortOutput,
       "vTelSessAttention": vTelSessAttention,
       "vTelSessEraseChar": vTelSessEraseChar,
       "vTelSessEraseLine": vTelSessEraseLine,
       "vTelSessGoAhead": vTelSessGoAhead,
       "vTelSessNullPass": vTelSessNullPass,
       "vTelSessTermType": vTelSessTermType,
       "vTelSessLocalEcho": vTelSessLocalEcho,
       "vTelSessRemoteEcho": vTelSessRemoteEcho,
       "vTelSessLocalBinary": vTelSessLocalBinary,
       "vTelSessRemoteBinary": vTelSessRemoteBinary,
       "vcpRlogin": vcpRlogin,
       "vRlogSessCurrNumber": vRlogSessCurrNumber,
       "vRlogSessTable": vRlogSessTable,
       "vRlogSessEntry": vRlogSessEntry,
       "vRlogSessPortIndex": vRlogSessPortIndex,
       "vRlogSessIndex": vRlogSessIndex,
       "vRlogSessOrigin": vRlogSessOrigin,
       "vRlogSessState": vRlogSessState,
       "vRlogSessDisconnect": vRlogSessDisconnect,
       "vRlogSessLocalAddr": vRlogSessLocalAddr,
       "vRlogSessLocalTcpPort": vRlogSessLocalTcpPort,
       "vRlogSessRemAddr": vRlogSessRemAddr,
       "vRlogSessRemTcpPort": vRlogSessRemTcpPort,
       "vRlogSessTermType": vRlogSessTermType,
       "vcpLt": vcpLt,
       "vLtNodeName": vLtNodeName,
       "vLtNodeID": vLtNodeID,
       "vLtNodeGroups": vLtNodeGroups,
       "vLtNumber": vLtNumber,
       "vLtMcastEnable": vLtMcastEnable,
       "vLtMcastTimer": vLtMcastTimer,
       "vLtCktTimer": vLtCktTimer,
       "vLtKeepaliveTimer": vLtKeepaliveTimer,
       "vLtMaxRetran": vLtMaxRetran,
       "vLtSlotPerCkt": vLtSlotPerCkt,
       "vLtMaxNodes": vLtMaxNodes,
       "vLtMaxSvcs": vLtMaxSvcs,
       "vLtMaxCkts": vLtMaxCkts,
       "vLtSessCurrNumber": vLtSessCurrNumber,
       "vLtSessTable": vLtSessTable,
       "vLtSessEntry": vLtSessEntry,
       "vLtSessPortIndex": vLtSessPortIndex,
       "vLtSessIndex": vLtSessIndex,
       "vLtSessOrigin": vLtSessOrigin,
       "vLtSessState": vLtSessState,
       "vLtSessDisconnect": vLtSessDisconnect,
       "vLtSessSvcName": vLtSessSvcName,
       "vLtSessNodeName": vLtSessNodeName,
       "vLtSessDestName": vLtSessDestName,
       "vLtTotalRcvPkts": vLtTotalRcvPkts,
       "vLtTotalTrnPkts": vLtTotalTrnPkts,
       "vLtTotalRetranPkts": vLtTotalRetranPkts,
       "vLtRcvCorruptPkts": vLtRcvCorruptPkts,
       "vLtRcvCorruptMcasts": vLtRcvCorruptMcasts,
       "vLtRcvDuplicatePkts": vLtRcvDuplicatePkts,
       "vLtReqAccepted": vLtReqAccepted,
       "vLtReqRejected": vLtReqRejected,
       "vLtTotalNodeDiscards": vLtTotalNodeDiscards,
       "vcpQueue": vcpQueue,
       "vQueMaxEntries": vQueMaxEntries,
       "vQueCurrNumber": vQueCurrNumber,
       "vQueTable": vQueTable,
       "vQueEntry": vQueEntry,
       "vQueEntryNumber": vQueEntryNumber,
       "vQueSvcName": vQueSvcName,
       "vQueNodeName": vQueNodeName,
       "vQuePortName": vQuePortName,
       "vQueStatus": vQueStatus,
       "vcpSnmp": vcpSnmp,
       "vSnmpReadCommunity": vSnmpReadCommunity,
       "vSnmpWriteCommunity": vSnmpWriteCommunity,
       "vSnmpReadWriteCommunity": vSnmpReadWriteCommunity,
       "vSnmpWriteEnable": vSnmpWriteEnable,
       "vSnmpTrapDestCurrNumber": vSnmpTrapDestCurrNumber,
       "vSnmpTrapDestTable": vSnmpTrapDestTable,
       "vSnmpTrapDestEntry": vSnmpTrapDestEntry,
       "vSnmpTrapDestAddr": vSnmpTrapDestAddr,
       "vSnmpTrapDestCommunity": vSnmpTrapDestCommunity,
       "vSnmpTrapDestColdEnable": vSnmpTrapDestColdEnable,
       "vSnmpTrapDestAuthEnable": vSnmpTrapDestAuthEnable,
       "vSnmpTrapDestStatus": vSnmpTrapDestStatus}
)
