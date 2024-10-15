# SNMP MIB module (ASCEND-MIBSS7NMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-MIBSS7NMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:15 2024
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

(configuration,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "configuration")

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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MibsS7Profile_ObjectIdentity = ObjectIdentity
mibsS7Profile = _MibsS7Profile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 121)
)
_MibsS7ProfileTable_Object = MibTable
mibsS7ProfileTable = _MibsS7ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1)
)
if mibBuilder.loadTexts:
    mibsS7ProfileTable.setStatus("mandatory")
_MibsS7ProfileEntry_Object = MibTableRow
mibsS7ProfileEntry = _MibsS7ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1)
)
mibsS7ProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSS7NMI-MIB", "sS7Profile-Index-o"),
)
if mibBuilder.loadTexts:
    mibsS7ProfileEntry.setStatus("mandatory")
_SS7Profile_Index_o_Type = Integer32
_SS7Profile_Index_o_Object = MibScalar
sS7Profile_Index_o = _SS7Profile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 1),
    _SS7Profile_Index_o_Type()
)
sS7Profile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sS7Profile_Index_o.setStatus("mandatory")


class _SS7Profile_Enabled_Type(Integer32):
    """Custom type sS7Profile_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SS7Profile_Enabled_Type.__name__ = "Integer32"
_SS7Profile_Enabled_Object = MibScalar
sS7Profile_Enabled = _SS7Profile_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 2),
    _SS7Profile_Enabled_Type()
)
sS7Profile_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_Enabled.setStatus("mandatory")


class _SS7Profile_ControlProtocol_Type(Integer32):
    """Custom type sS7Profile_ControlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asgcp", 1),
          ("ipdc0X", 2),
          ("q931Plus", 3))
    )


_SS7Profile_ControlProtocol_Type.__name__ = "Integer32"
_SS7Profile_ControlProtocol_Object = MibScalar
sS7Profile_ControlProtocol = _SS7Profile_ControlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 3),
    _SS7Profile_ControlProtocol_Type()
)
sS7Profile_ControlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_ControlProtocol.setStatus("mandatory")
_SS7Profile_PrimaryIpAddress_Type = IpAddress
_SS7Profile_PrimaryIpAddress_Object = MibScalar
sS7Profile_PrimaryIpAddress = _SS7Profile_PrimaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 4),
    _SS7Profile_PrimaryIpAddress_Type()
)
sS7Profile_PrimaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_PrimaryIpAddress.setStatus("mandatory")
_SS7Profile_PrimaryTcpPort_Type = Integer32
_SS7Profile_PrimaryTcpPort_Object = MibScalar
sS7Profile_PrimaryTcpPort = _SS7Profile_PrimaryTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 5),
    _SS7Profile_PrimaryTcpPort_Type()
)
sS7Profile_PrimaryTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_PrimaryTcpPort.setStatus("mandatory")
_SS7Profile_SecondaryIpAddress_Type = IpAddress
_SS7Profile_SecondaryIpAddress_Object = MibScalar
sS7Profile_SecondaryIpAddress = _SS7Profile_SecondaryIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 6),
    _SS7Profile_SecondaryIpAddress_Type()
)
sS7Profile_SecondaryIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_SecondaryIpAddress.setStatus("mandatory")
_SS7Profile_SecondaryTcpPort_Type = Integer32
_SS7Profile_SecondaryTcpPort_Object = MibScalar
sS7Profile_SecondaryTcpPort = _SS7Profile_SecondaryTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 7),
    _SS7Profile_SecondaryTcpPort_Type()
)
sS7Profile_SecondaryTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_SecondaryTcpPort.setStatus("mandatory")
_SS7Profile_BayId_Type = DisplayString
_SS7Profile_BayId_Object = MibScalar
sS7Profile_BayId = _SS7Profile_BayId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 8),
    _SS7Profile_BayId_Type()
)
sS7Profile_BayId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_BayId.setStatus("mandatory")
_SS7Profile_SystemType_Type = DisplayString
_SS7Profile_SystemType_Object = MibScalar
sS7Profile_SystemType = _SS7Profile_SystemType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 9),
    _SS7Profile_SystemType_Type()
)
sS7Profile_SystemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_SystemType.setStatus("mandatory")


class _SS7Profile_TransportOptions_Type_Type(Integer32):
    """Custom type sS7Profile_TransportOptions_Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ascend", 1),
          ("tcpEncaps2", 2))
    )


_SS7Profile_TransportOptions_Type_Type.__name__ = "Integer32"
_SS7Profile_TransportOptions_Type_Object = MibScalar
sS7Profile_TransportOptions_Type = _SS7Profile_TransportOptions_Type_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 10),
    _SS7Profile_TransportOptions_Type_Type()
)
sS7Profile_TransportOptions_Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_Type.setStatus("mandatory")
_SS7Profile_TransportOptions_DeviceId_Type = Integer32
_SS7Profile_TransportOptions_DeviceId_Object = MibScalar
sS7Profile_TransportOptions_DeviceId = _SS7Profile_TransportOptions_DeviceId_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 11),
    _SS7Profile_TransportOptions_DeviceId_Type()
)
sS7Profile_TransportOptions_DeviceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_DeviceId.setStatus("mandatory")
_SS7Profile_TransportOptions_T1Duration_Type = Integer32
_SS7Profile_TransportOptions_T1Duration_Object = MibScalar
sS7Profile_TransportOptions_T1Duration = _SS7Profile_TransportOptions_T1Duration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 12),
    _SS7Profile_TransportOptions_T1Duration_Type()
)
sS7Profile_TransportOptions_T1Duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_T1Duration.setStatus("mandatory")
_SS7Profile_TransportOptions_T2Duration_Type = Integer32
_SS7Profile_TransportOptions_T2Duration_Object = MibScalar
sS7Profile_TransportOptions_T2Duration = _SS7Profile_TransportOptions_T2Duration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 13),
    _SS7Profile_TransportOptions_T2Duration_Type()
)
sS7Profile_TransportOptions_T2Duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_T2Duration.setStatus("mandatory")
_SS7Profile_TransportOptions_T3Duration_Type = Integer32
_SS7Profile_TransportOptions_T3Duration_Object = MibScalar
sS7Profile_TransportOptions_T3Duration = _SS7Profile_TransportOptions_T3Duration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 14),
    _SS7Profile_TransportOptions_T3Duration_Type()
)
sS7Profile_TransportOptions_T3Duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_T3Duration.setStatus("mandatory")
_SS7Profile_TransportOptions_WindowSize_Type = Integer32
_SS7Profile_TransportOptions_WindowSize_Object = MibScalar
sS7Profile_TransportOptions_WindowSize = _SS7Profile_TransportOptions_WindowSize_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 15),
    _SS7Profile_TransportOptions_WindowSize_Type()
)
sS7Profile_TransportOptions_WindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_WindowSize.setStatus("mandatory")
_SS7Profile_TransportOptions_AckThreshold_Type = Integer32
_SS7Profile_TransportOptions_AckThreshold_Object = MibScalar
sS7Profile_TransportOptions_AckThreshold = _SS7Profile_TransportOptions_AckThreshold_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 16),
    _SS7Profile_TransportOptions_AckThreshold_Type()
)
sS7Profile_TransportOptions_AckThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_AckThreshold.setStatus("mandatory")


class _SS7Profile_TransportOptions_HeartBeat_Type(Integer32):
    """Custom type sS7Profile_TransportOptions_HeartBeat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SS7Profile_TransportOptions_HeartBeat_Type.__name__ = "Integer32"
_SS7Profile_TransportOptions_HeartBeat_Object = MibScalar
sS7Profile_TransportOptions_HeartBeat = _SS7Profile_TransportOptions_HeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 17),
    _SS7Profile_TransportOptions_HeartBeat_Type()
)
sS7Profile_TransportOptions_HeartBeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_HeartBeat.setStatus("mandatory")


class _SS7Profile_UseSystemIpAddressAsSource_Type(Integer32):
    """Custom type sS7Profile_UseSystemIpAddressAsSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SS7Profile_UseSystemIpAddressAsSource_Type.__name__ = "Integer32"
_SS7Profile_UseSystemIpAddressAsSource_Object = MibScalar
sS7Profile_UseSystemIpAddressAsSource = _SS7Profile_UseSystemIpAddressAsSource_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 18),
    _SS7Profile_UseSystemIpAddressAsSource_Type()
)
sS7Profile_UseSystemIpAddressAsSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_UseSystemIpAddressAsSource.setStatus("mandatory")


class _SS7Profile_CongestionControl_CongestionControlType_Type(Integer32):
    """Custom type sS7Profile_CongestionControl_CongestionControlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l3QueueDepth", 2),
          ("none", 1))
    )


_SS7Profile_CongestionControl_CongestionControlType_Type.__name__ = "Integer32"
_SS7Profile_CongestionControl_CongestionControlType_Object = MibScalar
sS7Profile_CongestionControl_CongestionControlType = _SS7Profile_CongestionControl_CongestionControlType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 19),
    _SS7Profile_CongestionControl_CongestionControlType_Type()
)
sS7Profile_CongestionControl_CongestionControlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_CongestionControl_CongestionControlType.setStatus("mandatory")
_SS7Profile_CongestionControl_Cl1Level_Type = Integer32
_SS7Profile_CongestionControl_Cl1Level_Object = MibScalar
sS7Profile_CongestionControl_Cl1Level = _SS7Profile_CongestionControl_Cl1Level_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 20),
    _SS7Profile_CongestionControl_Cl1Level_Type()
)
sS7Profile_CongestionControl_Cl1Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_CongestionControl_Cl1Level.setStatus("mandatory")


class _SS7Profile_CongestionControl_Cl1Action_Type(Integer32):
    """Custom type sS7Profile_CongestionControl_Cl1Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("sendInfoToMgc", 2))
    )


_SS7Profile_CongestionControl_Cl1Action_Type.__name__ = "Integer32"
_SS7Profile_CongestionControl_Cl1Action_Object = MibScalar
sS7Profile_CongestionControl_Cl1Action = _SS7Profile_CongestionControl_Cl1Action_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 21),
    _SS7Profile_CongestionControl_Cl1Action_Type()
)
sS7Profile_CongestionControl_Cl1Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_CongestionControl_Cl1Action.setStatus("mandatory")
_SS7Profile_CongestionControl_Cl2Level_Type = Integer32
_SS7Profile_CongestionControl_Cl2Level_Object = MibScalar
sS7Profile_CongestionControl_Cl2Level = _SS7Profile_CongestionControl_Cl2Level_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 22),
    _SS7Profile_CongestionControl_Cl2Level_Type()
)
sS7Profile_CongestionControl_Cl2Level.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_CongestionControl_Cl2Level.setStatus("mandatory")


class _SS7Profile_CongestionControl_Cl2Action_Type(Integer32):
    """Custom type sS7Profile_CongestionControl_Cl2Action based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 1),
          ("rejectNewCall", 3),
          ("sendInfoToMgc", 2))
    )


_SS7Profile_CongestionControl_Cl2Action_Type.__name__ = "Integer32"
_SS7Profile_CongestionControl_Cl2Action_Object = MibScalar
sS7Profile_CongestionControl_Cl2Action = _SS7Profile_CongestionControl_Cl2Action_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 23),
    _SS7Profile_CongestionControl_Cl2Action_Type()
)
sS7Profile_CongestionControl_Cl2Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_CongestionControl_Cl2Action.setStatus("mandatory")


class _SS7Profile_SignalingHeartbeat_Enabled_Type(Integer32):
    """Custom type sS7Profile_SignalingHeartbeat_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SS7Profile_SignalingHeartbeat_Enabled_Type.__name__ = "Integer32"
_SS7Profile_SignalingHeartbeat_Enabled_Object = MibScalar
sS7Profile_SignalingHeartbeat_Enabled = _SS7Profile_SignalingHeartbeat_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 24),
    _SS7Profile_SignalingHeartbeat_Enabled_Type()
)
sS7Profile_SignalingHeartbeat_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_SignalingHeartbeat_Enabled.setStatus("mandatory")
_SS7Profile_SignalingHeartbeat_Interval_Type = Integer32
_SS7Profile_SignalingHeartbeat_Interval_Object = MibScalar
sS7Profile_SignalingHeartbeat_Interval = _SS7Profile_SignalingHeartbeat_Interval_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 25),
    _SS7Profile_SignalingHeartbeat_Interval_Type()
)
sS7Profile_SignalingHeartbeat_Interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_SignalingHeartbeat_Interval.setStatus("mandatory")


class _SS7Profile_Action_o_Type(Integer32):
    """Custom type sS7Profile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_SS7Profile_Action_o_Type.__name__ = "Integer32"
_SS7Profile_Action_o_Object = MibScalar
sS7Profile_Action_o = _SS7Profile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 26),
    _SS7Profile_Action_o_Type()
)
sS7Profile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_Action_o.setStatus("mandatory")


class _SS7Profile_ResilienceOptions_Type_Type(Integer32):
    """Custom type sS7Profile_ResilienceOptions_Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("maintainActive", 2),
          ("releaseAll", 1),
          ("timedRelease", 3))
    )


_SS7Profile_ResilienceOptions_Type_Type.__name__ = "Integer32"
_SS7Profile_ResilienceOptions_Type_Object = MibScalar
sS7Profile_ResilienceOptions_Type = _SS7Profile_ResilienceOptions_Type_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 27),
    _SS7Profile_ResilienceOptions_Type_Type()
)
sS7Profile_ResilienceOptions_Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_ResilienceOptions_Type.setStatus("mandatory")
_SS7Profile_ResilienceOptions_Duration_Type = Integer32
_SS7Profile_ResilienceOptions_Duration_Object = MibScalar
sS7Profile_ResilienceOptions_Duration = _SS7Profile_ResilienceOptions_Duration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 28),
    _SS7Profile_ResilienceOptions_Duration_Type()
)
sS7Profile_ResilienceOptions_Duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_ResilienceOptions_Duration.setStatus("mandatory")


class _SS7Profile_PriTunnelingOptions_Enabled_Type(Integer32):
    """Custom type sS7Profile_PriTunnelingOptions_Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SS7Profile_PriTunnelingOptions_Enabled_Type.__name__ = "Integer32"
_SS7Profile_PriTunnelingOptions_Enabled_Object = MibScalar
sS7Profile_PriTunnelingOptions_Enabled = _SS7Profile_PriTunnelingOptions_Enabled_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 29),
    _SS7Profile_PriTunnelingOptions_Enabled_Type()
)
sS7Profile_PriTunnelingOptions_Enabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_PriTunnelingOptions_Enabled.setStatus("mandatory")
_SS7Profile_PriTunnelingOptions_Duration_Type = Integer32
_SS7Profile_PriTunnelingOptions_Duration_Object = MibScalar
sS7Profile_PriTunnelingOptions_Duration = _SS7Profile_PriTunnelingOptions_Duration_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 30),
    _SS7Profile_PriTunnelingOptions_Duration_Type()
)
sS7Profile_PriTunnelingOptions_Duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_PriTunnelingOptions_Duration.setStatus("mandatory")
_SS7Profile_IpdcSourceAdddress_Type = IpAddress
_SS7Profile_IpdcSourceAdddress_Object = MibScalar
sS7Profile_IpdcSourceAdddress = _SS7Profile_IpdcSourceAdddress_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 32),
    _SS7Profile_IpdcSourceAdddress_Type()
)
sS7Profile_IpdcSourceAdddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_IpdcSourceAdddress.setStatus("mandatory")
_SS7Profile_Vrouter_Type = DisplayString
_SS7Profile_Vrouter_Object = MibScalar
sS7Profile_Vrouter = _SS7Profile_Vrouter_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 33),
    _SS7Profile_Vrouter_Type()
)
sS7Profile_Vrouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_Vrouter.setStatus("mandatory")


class _SS7Profile_TransportOptions_Tos_Active_Type(Integer32):
    """Custom type sS7Profile_TransportOptions_Tos_Active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_SS7Profile_TransportOptions_Tos_Active_Type.__name__ = "Integer32"
_SS7Profile_TransportOptions_Tos_Active_Object = MibScalar
sS7Profile_TransportOptions_Tos_Active = _SS7Profile_TransportOptions_Tos_Active_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 34),
    _SS7Profile_TransportOptions_Tos_Active_Type()
)
sS7Profile_TransportOptions_Tos_Active.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_Tos_Active.setStatus("mandatory")


class _SS7Profile_TransportOptions_Tos_Precedence_Type(Integer32):
    """Custom type sS7Profile_TransportOptions_Tos_Precedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              33,
              65,
              97,
              129,
              161,
              193,
              225)
        )
    )
    namedValues = NamedValues(
        *(("n-000", 1),
          ("n-001", 33),
          ("n-010", 65),
          ("n-011", 97),
          ("n-100", 129),
          ("n-101", 161),
          ("n-110", 193),
          ("n-111", 225))
    )


_SS7Profile_TransportOptions_Tos_Precedence_Type.__name__ = "Integer32"
_SS7Profile_TransportOptions_Tos_Precedence_Object = MibScalar
sS7Profile_TransportOptions_Tos_Precedence = _SS7Profile_TransportOptions_Tos_Precedence_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 35),
    _SS7Profile_TransportOptions_Tos_Precedence_Type()
)
sS7Profile_TransportOptions_Tos_Precedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_Tos_Precedence.setStatus("mandatory")


class _SS7Profile_TransportOptions_Tos_TypeOfService_Type(Integer32):
    """Custom type sS7Profile_TransportOptions_Tos_TypeOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              9,
              17)
        )
    )
    namedValues = NamedValues(
        *(("cost", 3),
          ("latency", 17),
          ("normal", 1),
          ("reliability", 5),
          ("throughput", 9))
    )


_SS7Profile_TransportOptions_Tos_TypeOfService_Type.__name__ = "Integer32"
_SS7Profile_TransportOptions_Tos_TypeOfService_Object = MibScalar
sS7Profile_TransportOptions_Tos_TypeOfService = _SS7Profile_TransportOptions_Tos_TypeOfService_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 36),
    _SS7Profile_TransportOptions_Tos_TypeOfService_Type()
)
sS7Profile_TransportOptions_Tos_TypeOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_Tos_TypeOfService.setStatus("mandatory")


class _SS7Profile_TransportOptions_Tos_ApplyTo_Type(Integer32):
    """Custom type sS7Profile_TransportOptions_Tos_ApplyTo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1025,
              2049,
              3073)
        )
    )
    namedValues = NamedValues(
        *(("both", 3073),
          ("incoming", 1025),
          ("outgoing", 2049))
    )


_SS7Profile_TransportOptions_Tos_ApplyTo_Type.__name__ = "Integer32"
_SS7Profile_TransportOptions_Tos_ApplyTo_Object = MibScalar
sS7Profile_TransportOptions_Tos_ApplyTo = _SS7Profile_TransportOptions_Tos_ApplyTo_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 37),
    _SS7Profile_TransportOptions_Tos_ApplyTo_Type()
)
sS7Profile_TransportOptions_Tos_ApplyTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_Tos_ApplyTo.setStatus("mandatory")


class _SS7Profile_TransportOptions_Tos_MarkingType_Type(Integer32):
    """Custom type sS7Profile_TransportOptions_Tos_MarkingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dscp", 2),
          ("precedenceTos", 1))
    )


_SS7Profile_TransportOptions_Tos_MarkingType_Type.__name__ = "Integer32"
_SS7Profile_TransportOptions_Tos_MarkingType_Object = MibScalar
sS7Profile_TransportOptions_Tos_MarkingType = _SS7Profile_TransportOptions_Tos_MarkingType_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 38),
    _SS7Profile_TransportOptions_Tos_MarkingType_Type()
)
sS7Profile_TransportOptions_Tos_MarkingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_Tos_MarkingType.setStatus("mandatory")
_SS7Profile_TransportOptions_Tos_Dscp_Type = DisplayString
_SS7Profile_TransportOptions_Tos_Dscp_Object = MibScalar
sS7Profile_TransportOptions_Tos_Dscp = _SS7Profile_TransportOptions_Tos_Dscp_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 121, 1, 1, 39),
    _SS7Profile_TransportOptions_Tos_Dscp_Type()
)
sS7Profile_TransportOptions_Tos_Dscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sS7Profile_TransportOptions_Tos_Dscp.setStatus("mandatory")
_MibpRITunlStatProfile_ObjectIdentity = ObjectIdentity
mibpRITunlStatProfile = _MibpRITunlStatProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 529, 23, 158)
)
_MibpRITunlStatProfileTable_Object = MibTable
mibpRITunlStatProfileTable = _MibpRITunlStatProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 158, 1)
)
if mibBuilder.loadTexts:
    mibpRITunlStatProfileTable.setStatus("mandatory")
_MibpRITunlStatProfileEntry_Object = MibTableRow
mibpRITunlStatProfileEntry = _MibpRITunlStatProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 158, 1, 1)
)
mibpRITunlStatProfileEntry.setIndexNames(
    (0, "ASCEND-MIBSS7NMI-MIB", "pRITunlStatProfile-Index-o"),
)
if mibBuilder.loadTexts:
    mibpRITunlStatProfileEntry.setStatus("mandatory")
_PRITunlStatProfile_Index_o_Type = Integer32
_PRITunlStatProfile_Index_o_Object = MibScalar
pRITunlStatProfile_Index_o = _PRITunlStatProfile_Index_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 158, 1, 1, 1),
    _PRITunlStatProfile_Index_o_Type()
)
pRITunlStatProfile_Index_o.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pRITunlStatProfile_Index_o.setStatus("mandatory")


class _PRITunlStatProfile_Action_o_Type(Integer32):
    """Custom type pRITunlStatProfile_Action_o based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("createProfile", 2),
          ("deleteProfile", 3),
          ("noAction", 1))
    )


_PRITunlStatProfile_Action_o_Type.__name__ = "Integer32"
_PRITunlStatProfile_Action_o_Object = MibScalar
pRITunlStatProfile_Action_o = _PRITunlStatProfile_Action_o_Object(
    (1, 3, 6, 1, 4, 1, 529, 23, 158, 1, 1, 2),
    _PRITunlStatProfile_Action_o_Type()
)
pRITunlStatProfile_Action_o.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pRITunlStatProfile_Action_o.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-MIBSS7NMI-MIB",
    **{"DisplayString": DisplayString,
       "mibsS7Profile": mibsS7Profile,
       "mibsS7ProfileTable": mibsS7ProfileTable,
       "mibsS7ProfileEntry": mibsS7ProfileEntry,
       "sS7Profile-Index-o": sS7Profile_Index_o,
       "sS7Profile-Enabled": sS7Profile_Enabled,
       "sS7Profile-ControlProtocol": sS7Profile_ControlProtocol,
       "sS7Profile-PrimaryIpAddress": sS7Profile_PrimaryIpAddress,
       "sS7Profile-PrimaryTcpPort": sS7Profile_PrimaryTcpPort,
       "sS7Profile-SecondaryIpAddress": sS7Profile_SecondaryIpAddress,
       "sS7Profile-SecondaryTcpPort": sS7Profile_SecondaryTcpPort,
       "sS7Profile-BayId": sS7Profile_BayId,
       "sS7Profile-SystemType": sS7Profile_SystemType,
       "sS7Profile-TransportOptions-Type": sS7Profile_TransportOptions_Type,
       "sS7Profile-TransportOptions-DeviceId": sS7Profile_TransportOptions_DeviceId,
       "sS7Profile-TransportOptions-T1Duration": sS7Profile_TransportOptions_T1Duration,
       "sS7Profile-TransportOptions-T2Duration": sS7Profile_TransportOptions_T2Duration,
       "sS7Profile-TransportOptions-T3Duration": sS7Profile_TransportOptions_T3Duration,
       "sS7Profile-TransportOptions-WindowSize": sS7Profile_TransportOptions_WindowSize,
       "sS7Profile-TransportOptions-AckThreshold": sS7Profile_TransportOptions_AckThreshold,
       "sS7Profile-TransportOptions-HeartBeat": sS7Profile_TransportOptions_HeartBeat,
       "sS7Profile-UseSystemIpAddressAsSource": sS7Profile_UseSystemIpAddressAsSource,
       "sS7Profile-CongestionControl-CongestionControlType": sS7Profile_CongestionControl_CongestionControlType,
       "sS7Profile-CongestionControl-Cl1Level": sS7Profile_CongestionControl_Cl1Level,
       "sS7Profile-CongestionControl-Cl1Action": sS7Profile_CongestionControl_Cl1Action,
       "sS7Profile-CongestionControl-Cl2Level": sS7Profile_CongestionControl_Cl2Level,
       "sS7Profile-CongestionControl-Cl2Action": sS7Profile_CongestionControl_Cl2Action,
       "sS7Profile-SignalingHeartbeat-Enabled": sS7Profile_SignalingHeartbeat_Enabled,
       "sS7Profile-SignalingHeartbeat-Interval": sS7Profile_SignalingHeartbeat_Interval,
       "sS7Profile-Action-o": sS7Profile_Action_o,
       "sS7Profile-ResilienceOptions-Type": sS7Profile_ResilienceOptions_Type,
       "sS7Profile-ResilienceOptions-Duration": sS7Profile_ResilienceOptions_Duration,
       "sS7Profile-PriTunnelingOptions-Enabled": sS7Profile_PriTunnelingOptions_Enabled,
       "sS7Profile-PriTunnelingOptions-Duration": sS7Profile_PriTunnelingOptions_Duration,
       "sS7Profile-IpdcSourceAdddress": sS7Profile_IpdcSourceAdddress,
       "sS7Profile-Vrouter": sS7Profile_Vrouter,
       "sS7Profile-TransportOptions-Tos-Active": sS7Profile_TransportOptions_Tos_Active,
       "sS7Profile-TransportOptions-Tos-Precedence": sS7Profile_TransportOptions_Tos_Precedence,
       "sS7Profile-TransportOptions-Tos-TypeOfService": sS7Profile_TransportOptions_Tos_TypeOfService,
       "sS7Profile-TransportOptions-Tos-ApplyTo": sS7Profile_TransportOptions_Tos_ApplyTo,
       "sS7Profile-TransportOptions-Tos-MarkingType": sS7Profile_TransportOptions_Tos_MarkingType,
       "sS7Profile-TransportOptions-Tos-Dscp": sS7Profile_TransportOptions_Tos_Dscp,
       "mibpRITunlStatProfile": mibpRITunlStatProfile,
       "mibpRITunlStatProfileTable": mibpRITunlStatProfileTable,
       "mibpRITunlStatProfileEntry": mibpRITunlStatProfileEntry,
       "pRITunlStatProfile-Index-o": pRITunlStatProfile_Index_o,
       "pRITunlStatProfile-Action-o": pRITunlStatProfile_Action_o}
)
