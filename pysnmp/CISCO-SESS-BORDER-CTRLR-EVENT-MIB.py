# SNMP MIB module (CISCO-SESS-BORDER-CTRLR-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SESS-BORDER-CTRLR-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:12 2024
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

(CiscoSbcPeriodicStatsInterval,) = mibBuilder.importSymbols(
    "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB",
    "CiscoSbcPeriodicStatsInterval")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CiscoAlarmSeverity,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSessBorderCtrlrEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 658)
)
ciscoSessBorderCtrlrEventMIB.setRevisions(
        ("2010-12-06 00:00",
         "2008-08-27 00:00",
         "2008-05-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CsbQOSAlertScopeType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adjacency", 2),
          ("global", 1))
    )



class CsbDynamicBlackListedSrcSubFamily(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blackAddress", 2),
          ("blackPort", 3),
          ("blackVPN", 1))
    )



class CsbDynamicBlackListedTransPortType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tcp", 3),
          ("udp", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSessBorderCtrlrMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSessBorderCtrlrMIBNotifs = _CiscoSessBorderCtrlrMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0)
)
_CiscoSessBorderCtrlrMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSessBorderCtrlrMIBObjects = _CiscoSessBorderCtrlrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1)
)


class _CsbAlarmSubsystem_Type(Integer32):
    """Custom type csbAlarmSubsystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cac", 3),
          ("media", 2),
          ("signaling", 1))
    )


_CsbAlarmSubsystem_Type.__name__ = "Integer32"
_CsbAlarmSubsystem_Object = MibScalar
csbAlarmSubsystem = _CsbAlarmSubsystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 1),
    _CsbAlarmSubsystem_Type()
)
csbAlarmSubsystem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbAlarmSubsystem.setStatus("current")
_CsbAlarmSeverity_Type = CiscoAlarmSeverity
_CsbAlarmSeverity_Object = MibScalar
csbAlarmSeverity = _CsbAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 2),
    _CsbAlarmSeverity_Type()
)
csbAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbAlarmSeverity.setStatus("current")


class _CsbAlarmID_Type(Integer32):
    """Custom type csbAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CsbAlarmID_Type.__name__ = "Integer32"
_CsbAlarmID_Object = MibScalar
csbAlarmID = _CsbAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 3),
    _CsbAlarmID_Type()
)
csbAlarmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbAlarmID.setStatus("current")


class _CsbAlarmTime_Type(OctetString):
    """Custom type csbAlarmTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CsbAlarmTime_Type.__name__ = "OctetString"
_CsbAlarmTime_Object = MibScalar
csbAlarmTime = _CsbAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 4),
    _CsbAlarmTime_Type()
)
csbAlarmTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbAlarmTime.setStatus("current")
_CsbSBCServiceName_Type = SnmpAdminString
_CsbSBCServiceName_Object = MibScalar
csbSBCServiceName = _CsbSBCServiceName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 5),
    _CsbSBCServiceName_Type()
)
csbSBCServiceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSBCServiceName.setStatus("current")
_CsbAlarmDescription_Type = OctetString
_CsbAlarmDescription_Object = MibScalar
csbAlarmDescription = _CsbAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 6),
    _CsbAlarmDescription_Type()
)
csbAlarmDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbAlarmDescription.setStatus("current")


class _CsbSrcAlertVdbeId_Type(SnmpAdminString):
    """Custom type csbSrcAlertVdbeId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_CsbSrcAlertVdbeId_Type.__name__ = "SnmpAdminString"
_CsbSrcAlertVdbeId_Object = MibScalar
csbSrcAlertVdbeId = _CsbSrcAlertVdbeId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 7),
    _CsbSrcAlertVdbeId_Type()
)
csbSrcAlertVdbeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSrcAlertVdbeId.setStatus("current")
_CsbSrcAlertGateId_Type = Unsigned32
_CsbSrcAlertGateId_Object = MibScalar
csbSrcAlertGateId = _CsbSrcAlertGateId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 8),
    _CsbSrcAlertGateId_Type()
)
csbSrcAlertGateId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSrcAlertGateId.setStatus("current")
_CsbSrcAlertFlowPairId_Type = Unsigned32
_CsbSrcAlertFlowPairId_Object = MibScalar
csbSrcAlertFlowPairId = _CsbSrcAlertFlowPairId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 9),
    _CsbSrcAlertFlowPairId_Type()
)
csbSrcAlertFlowPairId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSrcAlertFlowPairId.setStatus("current")
_CsbSrcAlertLocalAddressType_Type = InetAddressType
_CsbSrcAlertLocalAddressType_Object = MibScalar
csbSrcAlertLocalAddressType = _CsbSrcAlertLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 10),
    _CsbSrcAlertLocalAddressType_Type()
)
csbSrcAlertLocalAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSrcAlertLocalAddressType.setStatus("current")


class _CsbSrcAlertLocalAddress_Type(InetAddress):
    """Custom type csbSrcAlertLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CsbSrcAlertLocalAddress_Type.__name__ = "InetAddress"
_CsbSrcAlertLocalAddress_Object = MibScalar
csbSrcAlertLocalAddress = _CsbSrcAlertLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 11),
    _CsbSrcAlertLocalAddress_Type()
)
csbSrcAlertLocalAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSrcAlertLocalAddress.setStatus("current")
_CsbSrcAlertLocalPort_Type = InetPortNumber
_CsbSrcAlertLocalPort_Object = MibScalar
csbSrcAlertLocalPort = _CsbSrcAlertLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 12),
    _CsbSrcAlertLocalPort_Type()
)
csbSrcAlertLocalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSrcAlertLocalPort.setStatus("current")
_CsbSrcAlertRemoteAddressType_Type = InetAddressType
_CsbSrcAlertRemoteAddressType_Object = MibScalar
csbSrcAlertRemoteAddressType = _CsbSrcAlertRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 13),
    _CsbSrcAlertRemoteAddressType_Type()
)
csbSrcAlertRemoteAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSrcAlertRemoteAddressType.setStatus("current")


class _CsbSrcAlertRemoteAddress_Type(InetAddress):
    """Custom type csbSrcAlertRemoteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CsbSrcAlertRemoteAddress_Type.__name__ = "InetAddress"
_CsbSrcAlertRemoteAddress_Object = MibScalar
csbSrcAlertRemoteAddress = _CsbSrcAlertRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 14),
    _CsbSrcAlertRemoteAddress_Type()
)
csbSrcAlertRemoteAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSrcAlertRemoteAddress.setStatus("current")


class _CsbSrcAlertRemotePort_Type(InetPortNumber):
    """Custom type csbSrcAlertRemotePort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CsbSrcAlertRemotePort_Type.__name__ = "InetPortNumber"
_CsbSrcAlertRemotePort_Object = MibScalar
csbSrcAlertRemotePort = _CsbSrcAlertRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 15),
    _CsbSrcAlertRemotePort_Type()
)
csbSrcAlertRemotePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSrcAlertRemotePort.setStatus("current")


class _CsbSrcAlertVpnId_Type(OctetString):
    """Custom type csbSrcAlertVpnId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CsbSrcAlertVpnId_Type.__name__ = "OctetString"
_CsbSrcAlertVpnId_Object = MibScalar
csbSrcAlertVpnId = _CsbSrcAlertVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 16),
    _CsbSrcAlertVpnId_Type()
)
csbSrcAlertVpnId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSrcAlertVpnId.setStatus("current")
_CsbDynamicBlackListSubFamily_Type = CsbDynamicBlackListedSrcSubFamily
_CsbDynamicBlackListSubFamily_Object = MibScalar
csbDynamicBlackListSubFamily = _CsbDynamicBlackListSubFamily_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 17),
    _CsbDynamicBlackListSubFamily_Type()
)
csbDynamicBlackListSubFamily.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbDynamicBlackListSubFamily.setStatus("current")


class _CsbDynamicBlackListVpnId_Type(OctetString):
    """Custom type csbDynamicBlackListVpnId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CsbDynamicBlackListVpnId_Type.__name__ = "OctetString"
_CsbDynamicBlackListVpnId_Object = MibScalar
csbDynamicBlackListVpnId = _CsbDynamicBlackListVpnId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 18),
    _CsbDynamicBlackListVpnId_Type()
)
csbDynamicBlackListVpnId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbDynamicBlackListVpnId.setStatus("current")
_CsbDynamicBlackListAddressType_Type = InetAddressType
_CsbDynamicBlackListAddressType_Object = MibScalar
csbDynamicBlackListAddressType = _CsbDynamicBlackListAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 19),
    _CsbDynamicBlackListAddressType_Type()
)
csbDynamicBlackListAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbDynamicBlackListAddressType.setStatus("current")
_CsbDynamicBlackListAddress_Type = InetAddress
_CsbDynamicBlackListAddress_Object = MibScalar
csbDynamicBlackListAddress = _CsbDynamicBlackListAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 20),
    _CsbDynamicBlackListAddress_Type()
)
csbDynamicBlackListAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbDynamicBlackListAddress.setStatus("current")
_CsbDynamicBlackListTransportType_Type = CsbDynamicBlackListedTransPortType
_CsbDynamicBlackListTransportType_Object = MibScalar
csbDynamicBlackListTransportType = _CsbDynamicBlackListTransportType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 21),
    _CsbDynamicBlackListTransportType_Type()
)
csbDynamicBlackListTransportType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbDynamicBlackListTransportType.setStatus("current")
_CsbDynamicBlackListPortNumber_Type = InetPortNumber
_CsbDynamicBlackListPortNumber_Object = MibScalar
csbDynamicBlackListPortNumber = _CsbDynamicBlackListPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 22),
    _CsbDynamicBlackListPortNumber_Type()
)
csbDynamicBlackListPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbDynamicBlackListPortNumber.setStatus("current")
_CsbDynamicBlackListSrcBlocked_Type = TruthValue
_CsbDynamicBlackListSrcBlocked_Object = MibScalar
csbDynamicBlackListSrcBlocked = _CsbDynamicBlackListSrcBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 23),
    _CsbDynamicBlackListSrcBlocked_Type()
)
csbDynamicBlackListSrcBlocked.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbDynamicBlackListSrcBlocked.setStatus("current")


class _CsbAdjacencyType_Type(Integer32):
    """Custom type csbAdjacencyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("h323", 2),
          ("sip", 1))
    )


_CsbAdjacencyType_Type.__name__ = "Integer32"
_CsbAdjacencyType_Object = MibScalar
csbAdjacencyType = _CsbAdjacencyType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 24),
    _CsbAdjacencyType_Type()
)
csbAdjacencyType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbAdjacencyType.setStatus("current")


class _CsbAdjacencyState_Type(Integer32):
    """Custom type csbAdjacencyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 1),
          ("detached", 2))
    )


_CsbAdjacencyState_Type.__name__ = "Integer32"
_CsbAdjacencyState_Object = MibScalar
csbAdjacencyState = _CsbAdjacencyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 25),
    _CsbAdjacencyState_Type()
)
csbAdjacencyState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbAdjacencyState.setStatus("current")
_CsbAdjacencyName_Type = SnmpAdminString
_CsbAdjacencyName_Object = MibScalar
csbAdjacencyName = _CsbAdjacencyName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 26),
    _CsbAdjacencyName_Type()
)
csbAdjacencyName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbAdjacencyName.setStatus("current")
_CsbAdjacencyAccountName_Type = SnmpAdminString
_CsbAdjacencyAccountName_Object = MibScalar
csbAdjacencyAccountName = _CsbAdjacencyAccountName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 27),
    _CsbAdjacencyAccountName_Type()
)
csbAdjacencyAccountName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbAdjacencyAccountName.setStatus("current")


class _CsbSBCServiceState_Type(Integer32):
    """Custom type csbSBCServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("offline", 3),
          ("standby", 2))
    )


_CsbSBCServiceState_Type.__name__ = "Integer32"
_CsbSBCServiceState_Object = MibScalar
csbSBCServiceState = _CsbSBCServiceState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 28),
    _CsbSBCServiceState_Type()
)
csbSBCServiceState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSBCServiceState.setStatus("current")
_CsbSBCServiceSlot_Type = Integer32
_CsbSBCServiceSlot_Object = MibScalar
csbSBCServiceSlot = _CsbSBCServiceSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 29),
    _CsbSBCServiceSlot_Type()
)
csbSBCServiceSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSBCServiceSlot.setStatus("current")


class _CsbCongestionAlarmType_Type(Integer32):
    """Custom type csbCongestionAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cpu", 2),
          ("memory", 3),
          ("unknown", 1))
    )


_CsbCongestionAlarmType_Type.__name__ = "Integer32"
_CsbCongestionAlarmType_Object = MibScalar
csbCongestionAlarmType = _CsbCongestionAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 30),
    _CsbCongestionAlarmType_Type()
)
csbCongestionAlarmType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbCongestionAlarmType.setStatus("current")


class _CsbCongestionAlarmState_Type(Integer32):
    """Custom type csbCongestionAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 2),
          ("raised", 1))
    )


_CsbCongestionAlarmState_Type.__name__ = "Integer32"
_CsbCongestionAlarmState_Object = MibScalar
csbCongestionAlarmState = _CsbCongestionAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 31),
    _CsbCongestionAlarmState_Type()
)
csbCongestionAlarmState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbCongestionAlarmState.setStatus("current")
_CsbSLAPolicyAccountName_Type = SnmpAdminString
_CsbSLAPolicyAccountName_Object = MibScalar
csbSLAPolicyAccountName = _CsbSLAPolicyAccountName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 32),
    _CsbSLAPolicyAccountName_Type()
)
csbSLAPolicyAccountName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSLAPolicyAccountName.setStatus("current")
_CsbSLAPolicyScope_Type = SnmpAdminString
_CsbSLAPolicyScope_Object = MibScalar
csbSLAPolicyScope = _CsbSLAPolicyScope_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 33),
    _CsbSLAPolicyScope_Type()
)
csbSLAPolicyScope.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSLAPolicyScope.setStatus("current")
_CsbSLAPolicyLimit_Type = Integer32
_CsbSLAPolicyLimit_Object = MibScalar
csbSLAPolicyLimit = _CsbSLAPolicyLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 34),
    _CsbSLAPolicyLimit_Type()
)
csbSLAPolicyLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSLAPolicyLimit.setStatus("deprecated")
_CsbSLAViolationEvent_Type = SnmpAdminString
_CsbSLAViolationEvent_Object = MibScalar
csbSLAViolationEvent = _CsbSLAViolationEvent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 35),
    _CsbSLAViolationEvent_Type()
)
csbSLAViolationEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSLAViolationEvent.setStatus("current")
_CsbSLAPolicyRestriction_Type = SnmpAdminString
_CsbSLAPolicyRestriction_Object = MibScalar
csbSLAPolicyRestriction = _CsbSLAPolicyRestriction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 36),
    _CsbSLAPolicyRestriction_Type()
)
csbSLAPolicyRestriction.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSLAPolicyRestriction.setStatus("current")
_CsbSLACurrentUsage_Type = Integer32
_CsbSLACurrentUsage_Object = MibScalar
csbSLACurrentUsage = _CsbSLACurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 37),
    _CsbSLACurrentUsage_Type()
)
csbSLACurrentUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSLACurrentUsage.setStatus("deprecated")


class _CsbRadiusConnectionState_Type(Integer32):
    """Custom type csbRadiusConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CsbRadiusConnectionState_Type.__name__ = "Integer32"
_CsbRadiusConnectionState_Object = MibScalar
csbRadiusConnectionState = _CsbRadiusConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 38),
    _CsbRadiusConnectionState_Type()
)
csbRadiusConnectionState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbRadiusConnectionState.setStatus("current")


class _CsbRadiusType_Type(Integer32):
    """Custom type csbRadiusType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 1),
          ("authentication", 2))
    )


_CsbRadiusType_Type.__name__ = "Integer32"
_CsbRadiusType_Object = MibScalar
csbRadiusType = _CsbRadiusType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 39),
    _CsbRadiusType_Type()
)
csbRadiusType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbRadiusType.setStatus("current")
_CsbRadiusServerName_Type = SnmpAdminString
_CsbRadiusServerName_Object = MibScalar
csbRadiusServerName = _CsbRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 40),
    _CsbRadiusServerName_Type()
)
csbRadiusServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbRadiusServerName.setStatus("current")
_CsbRadiusServerAddressType_Type = InetAddressType
_CsbRadiusServerAddressType_Object = MibScalar
csbRadiusServerAddressType = _CsbRadiusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 41),
    _CsbRadiusServerAddressType_Type()
)
csbRadiusServerAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbRadiusServerAddressType.setStatus("current")


class _CsbRadiusServerAddress_Type(InetAddress):
    """Custom type csbRadiusServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CsbRadiusServerAddress_Type.__name__ = "InetAddress"
_CsbRadiusServerAddress_Object = MibScalar
csbRadiusServerAddress = _CsbRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 42),
    _CsbRadiusServerAddress_Type()
)
csbRadiusServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbRadiusServerAddress.setStatus("current")
_CsbRadiusServerPriority_Type = Integer32
_CsbRadiusServerPriority_Object = MibScalar
csbRadiusServerPriority = _CsbRadiusServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 43),
    _CsbRadiusServerPriority_Type()
)
csbRadiusServerPriority.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbRadiusServerPriority.setStatus("current")


class _CsbDiameterConnectionState_Type(Integer32):
    """Custom type csbDiameterConnectionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CsbDiameterConnectionState_Type.__name__ = "Integer32"
_CsbDiameterConnectionState_Object = MibScalar
csbDiameterConnectionState = _CsbDiameterConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 44),
    _CsbDiameterConnectionState_Type()
)
csbDiameterConnectionState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbDiameterConnectionState.setStatus("current")


class _CsbDiameterType_Type(Integer32):
    """Custom type csbDiameterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 1),
          ("authentication", 2))
    )


_CsbDiameterType_Type.__name__ = "Integer32"
_CsbDiameterType_Object = MibScalar
csbDiameterType = _CsbDiameterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 45),
    _CsbDiameterType_Type()
)
csbDiameterType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbDiameterType.setStatus("current")
_CsbDiameterGroupName_Type = SnmpAdminString
_CsbDiameterGroupName_Object = MibScalar
csbDiameterGroupName = _CsbDiameterGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 46),
    _CsbDiameterGroupName_Type()
)
csbDiameterGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbDiameterGroupName.setStatus("current")
_CsbDiameterServerName_Type = SnmpAdminString
_CsbDiameterServerName_Object = MibScalar
csbDiameterServerName = _CsbDiameterServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 47),
    _CsbDiameterServerName_Type()
)
csbDiameterServerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbDiameterServerName.setStatus("current")


class _CsbH248ControllerState_Type(Integer32):
    """Custom type csbH248ControllerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("attached", 1),
          ("detached", 2))
    )


_CsbH248ControllerState_Type.__name__ = "Integer32"
_CsbH248ControllerState_Object = MibScalar
csbH248ControllerState = _CsbH248ControllerState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 48),
    _CsbH248ControllerState_Type()
)
csbH248ControllerState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbH248ControllerState.setStatus("current")
_Csb248ControllerAddressType_Type = InetAddressType
_Csb248ControllerAddressType_Object = MibScalar
csb248ControllerAddressType = _Csb248ControllerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 49),
    _Csb248ControllerAddressType_Type()
)
csb248ControllerAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csb248ControllerAddressType.setStatus("current")


class _CsbH248ControllerAddress_Type(InetAddress):
    """Custom type csbH248ControllerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CsbH248ControllerAddress_Type.__name__ = "InetAddress"
_CsbH248ControllerAddress_Object = MibScalar
csbH248ControllerAddress = _CsbH248ControllerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 50),
    _CsbH248ControllerAddress_Type()
)
csbH248ControllerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbH248ControllerAddress.setStatus("current")
_CsbH248ControllerPort_Type = InetPortNumber
_CsbH248ControllerPort_Object = MibScalar
csbH248ControllerPort = _CsbH248ControllerPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 51),
    _CsbH248ControllerPort_Type()
)
csbH248ControllerPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbH248ControllerPort.setStatus("current")
_CsbSourceAlertNotifEnabled_Type = TruthValue
_CsbSourceAlertNotifEnabled_Object = MibScalar
csbSourceAlertNotifEnabled = _CsbSourceAlertNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 52),
    _CsbSourceAlertNotifEnabled_Type()
)
csbSourceAlertNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbSourceAlertNotifEnabled.setStatus("current")
_CsbBlackListNotifEnabled_Type = TruthValue
_CsbBlackListNotifEnabled_Object = MibScalar
csbBlackListNotifEnabled = _CsbBlackListNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 53),
    _CsbBlackListNotifEnabled_Type()
)
csbBlackListNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbBlackListNotifEnabled.setStatus("current")
_CsbAdjacencyStatusNotifEnabled_Type = TruthValue
_CsbAdjacencyStatusNotifEnabled_Object = MibScalar
csbAdjacencyStatusNotifEnabled = _CsbAdjacencyStatusNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 54),
    _CsbAdjacencyStatusNotifEnabled_Type()
)
csbAdjacencyStatusNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbAdjacencyStatusNotifEnabled.setStatus("current")
_CsbServiceStateNotifEnabled_Type = TruthValue
_CsbServiceStateNotifEnabled_Object = MibScalar
csbServiceStateNotifEnabled = _CsbServiceStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 55),
    _CsbServiceStateNotifEnabled_Type()
)
csbServiceStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbServiceStateNotifEnabled.setStatus("current")
_CsbCongestionAlarmNotifEnabled_Type = TruthValue
_CsbCongestionAlarmNotifEnabled_Object = MibScalar
csbCongestionAlarmNotifEnabled = _CsbCongestionAlarmNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 56),
    _CsbCongestionAlarmNotifEnabled_Type()
)
csbCongestionAlarmNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbCongestionAlarmNotifEnabled.setStatus("current")
_CsbSLAViolationNotifEnabled_Type = TruthValue
_CsbSLAViolationNotifEnabled_Object = MibScalar
csbSLAViolationNotifEnabled = _CsbSLAViolationNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 57),
    _CsbSLAViolationNotifEnabled_Type()
)
csbSLAViolationNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbSLAViolationNotifEnabled.setStatus("deprecated")
_CsbRadiusConnectionStatusNotifEnabled_Type = TruthValue
_CsbRadiusConnectionStatusNotifEnabled_Object = MibScalar
csbRadiusConnectionStatusNotifEnabled = _CsbRadiusConnectionStatusNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 58),
    _CsbRadiusConnectionStatusNotifEnabled_Type()
)
csbRadiusConnectionStatusNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbRadiusConnectionStatusNotifEnabled.setStatus("current")
_CsbDiameterConnectionStatusNotifEnabled_Type = TruthValue
_CsbDiameterConnectionStatusNotifEnabled_Object = MibScalar
csbDiameterConnectionStatusNotifEnabled = _CsbDiameterConnectionStatusNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 59),
    _CsbDiameterConnectionStatusNotifEnabled_Type()
)
csbDiameterConnectionStatusNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbDiameterConnectionStatusNotifEnabled.setStatus("current")
_CsbH248ControllerStatusNotifEnabled_Type = TruthValue
_CsbH248ControllerStatusNotifEnabled_Object = MibScalar
csbH248ControllerStatusNotifEnabled = _CsbH248ControllerStatusNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 60),
    _CsbH248ControllerStatusNotifEnabled_Type()
)
csbH248ControllerStatusNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbH248ControllerStatusNotifEnabled.setStatus("current")
_CsbSLAPolicyLimitRev1_Type = Counter64
_CsbSLAPolicyLimitRev1_Object = MibScalar
csbSLAPolicyLimitRev1 = _CsbSLAPolicyLimitRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 61),
    _CsbSLAPolicyLimitRev1_Type()
)
csbSLAPolicyLimitRev1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSLAPolicyLimitRev1.setStatus("current")
_CsbSLACurrentUsageRev1_Type = Counter64
_CsbSLACurrentUsageRev1_Object = MibScalar
csbSLACurrentUsageRev1 = _CsbSLACurrentUsageRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 62),
    _CsbSLACurrentUsageRev1_Type()
)
csbSLACurrentUsageRev1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbSLACurrentUsageRev1.setStatus("current")
_CsbSLAViolationNotifEnabledRev1_Type = TruthValue
_CsbSLAViolationNotifEnabledRev1_Object = MibScalar
csbSLAViolationNotifEnabledRev1 = _CsbSLAViolationNotifEnabledRev1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 63),
    _CsbSLAViolationNotifEnabledRev1_Type()
)
csbSLAViolationNotifEnabledRev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbSLAViolationNotifEnabledRev1.setStatus("current")
_CsbQOSAlertCurrentValue_Type = Unsigned32
_CsbQOSAlertCurrentValue_Object = MibScalar
csbQOSAlertCurrentValue = _CsbQOSAlertCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 64),
    _CsbQOSAlertCurrentValue_Type()
)
csbQOSAlertCurrentValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbQOSAlertCurrentValue.setStatus("current")
_CsbQOSAlertCurrentLevel_Type = CiscoAlarmSeverity
_CsbQOSAlertCurrentLevel_Object = MibScalar
csbQOSAlertCurrentLevel = _CsbQOSAlertCurrentLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 65),
    _CsbQOSAlertCurrentLevel_Type()
)
csbQOSAlertCurrentLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbQOSAlertCurrentLevel.setStatus("current")
_CsbQOSAlertPreviousLevel_Type = CiscoAlarmSeverity
_CsbQOSAlertPreviousLevel_Object = MibScalar
csbQOSAlertPreviousLevel = _CsbQOSAlertPreviousLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 66),
    _CsbQOSAlertPreviousLevel_Type()
)
csbQOSAlertPreviousLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbQOSAlertPreviousLevel.setStatus("current")
_CsbQOSNormalAlertCount_Type = Counter32
_CsbQOSNormalAlertCount_Object = MibScalar
csbQOSNormalAlertCount = _CsbQOSNormalAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 67),
    _CsbQOSNormalAlertCount_Type()
)
csbQOSNormalAlertCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbQOSNormalAlertCount.setStatus("current")
if mibBuilder.loadTexts:
    csbQOSNormalAlertCount.setUnits("occurrences")
_CsbQOSMinorAlertCount_Type = Counter32
_CsbQOSMinorAlertCount_Object = MibScalar
csbQOSMinorAlertCount = _CsbQOSMinorAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 68),
    _CsbQOSMinorAlertCount_Type()
)
csbQOSMinorAlertCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbQOSMinorAlertCount.setStatus("current")
if mibBuilder.loadTexts:
    csbQOSMinorAlertCount.setUnits("occurrences")
_CsbQOSCriticalAlertCount_Type = Counter32
_CsbQOSCriticalAlertCount_Object = MibScalar
csbQOSCriticalAlertCount = _CsbQOSCriticalAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 69),
    _CsbQOSCriticalAlertCount_Type()
)
csbQOSCriticalAlertCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbQOSCriticalAlertCount.setStatus("current")
if mibBuilder.loadTexts:
    csbQOSCriticalAlertCount.setUnits("occurrences")
_CsbQOSMajorAlertCount_Type = Counter32
_CsbQOSMajorAlertCount_Object = MibScalar
csbQOSMajorAlertCount = _CsbQOSMajorAlertCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 70),
    _CsbQOSMajorAlertCount_Type()
)
csbQOSMajorAlertCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbQOSMajorAlertCount.setStatus("current")
if mibBuilder.loadTexts:
    csbQOSMajorAlertCount.setUnits("occurrences")
_CsbQOSAlertType_Type = CsbQOSAlertScopeType
_CsbQOSAlertType_Object = MibScalar
csbQOSAlertType = _CsbQOSAlertType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 71),
    _CsbQOSAlertType_Type()
)
csbQOSAlertType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbQOSAlertType.setStatus("current")
_CsbQOSAlertSummaryPeriod_Type = CiscoSbcPeriodicStatsInterval
_CsbQOSAlertSummaryPeriod_Object = MibScalar
csbQOSAlertSummaryPeriod = _CsbQOSAlertSummaryPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 72),
    _CsbQOSAlertSummaryPeriod_Type()
)
csbQOSAlertSummaryPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    csbQOSAlertSummaryPeriod.setStatus("current")
_CsbQOSAlertUnansweredCallRatioNotifEnabled_Type = TruthValue
_CsbQOSAlertUnansweredCallRatioNotifEnabled_Object = MibScalar
csbQOSAlertUnansweredCallRatioNotifEnabled = _CsbQOSAlertUnansweredCallRatioNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 73),
    _CsbQOSAlertUnansweredCallRatioNotifEnabled_Type()
)
csbQOSAlertUnansweredCallRatioNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbQOSAlertUnansweredCallRatioNotifEnabled.setStatus("current")
_CsbQOSAlertPercentPktDropNotifEnabled_Type = TruthValue
_CsbQOSAlertPercentPktDropNotifEnabled_Object = MibScalar
csbQOSAlertPercentPktDropNotifEnabled = _CsbQOSAlertPercentPktDropNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 74),
    _CsbQOSAlertPercentPktDropNotifEnabled_Type()
)
csbQOSAlertPercentPktDropNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbQOSAlertPercentPktDropNotifEnabled.setStatus("current")
_CsbQOSAlertRoundTripDelayNotifEnabled_Type = TruthValue
_CsbQOSAlertRoundTripDelayNotifEnabled_Object = MibScalar
csbQOSAlertRoundTripDelayNotifEnabled = _CsbQOSAlertRoundTripDelayNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 75),
    _CsbQOSAlertRoundTripDelayNotifEnabled_Type()
)
csbQOSAlertRoundTripDelayNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbQOSAlertRoundTripDelayNotifEnabled.setStatus("current")
_CsbQOSAlertMoscqeNotifEnabled_Type = TruthValue
_CsbQOSAlertMoscqeNotifEnabled_Object = MibScalar
csbQOSAlertMoscqeNotifEnabled = _CsbQOSAlertMoscqeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 76),
    _CsbQOSAlertMoscqeNotifEnabled_Type()
)
csbQOSAlertMoscqeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbQOSAlertMoscqeNotifEnabled.setStatus("current")
_CsbQOSAlertLocalJitterNotifEnabled_Type = TruthValue
_CsbQOSAlertLocalJitterNotifEnabled_Object = MibScalar
csbQOSAlertLocalJitterNotifEnabled = _CsbQOSAlertLocalJitterNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 77),
    _CsbQOSAlertLocalJitterNotifEnabled_Type()
)
csbQOSAlertLocalJitterNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbQOSAlertLocalJitterNotifEnabled.setStatus("current")
_CsbQOSAlertRemoteJitterNotifEnabled_Type = TruthValue
_CsbQOSAlertRemoteJitterNotifEnabled_Object = MibScalar
csbQOSAlertRemoteJitterNotifEnabled = _CsbQOSAlertRemoteJitterNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 78),
    _CsbQOSAlertRemoteJitterNotifEnabled_Type()
)
csbQOSAlertRemoteJitterNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbQOSAlertRemoteJitterNotifEnabled.setStatus("current")
_CsbQOSAlertPercentPktLostNotifEnabled_Type = TruthValue
_CsbQOSAlertPercentPktLostNotifEnabled_Object = MibScalar
csbQOSAlertPercentPktLostNotifEnabled = _CsbQOSAlertPercentPktLostNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 1, 79),
    _CsbQOSAlertPercentPktLostNotifEnabled_Type()
)
csbQOSAlertPercentPktLostNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csbQOSAlertPercentPktLostNotifEnabled.setStatus("current")
_CiscoSessBorderCtrlrMIBConform_ObjectIdentity = ObjectIdentity
ciscoSessBorderCtrlrMIBConform = _CiscoSessBorderCtrlrMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2)
)
_CiscoSessBorderCtrlrMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSessBorderCtrlrMIBCompliances = _CiscoSessBorderCtrlrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 1)
)
_CiscoSessBorderCtrlrMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSessBorderCtrlrMIBGroups = _CiscoSessBorderCtrlrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2)
)

# Managed Objects groups

csbNotificationManadatoryParams = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 2)
)
csbNotificationManadatoryParams.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"))
)
if mibBuilder.loadTexts:
    csbNotificationManadatoryParams.setStatus("current")

csbSourceAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 3)
)
csbSourceAlertGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertVdbeId"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertGateId"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertFlowPairId"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertLocalAddress"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertLocalPort"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertRemoteAddressType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertRemoteAddress"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertRemotePort"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertVpnId"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertLocalAddressType"))
)
if mibBuilder.loadTexts:
    csbSourceAlertGroup.setStatus("current")

csbDynamicBlackListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 4)
)
csbDynamicBlackListGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListSubFamily"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListVpnId"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListAddressType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListAddress"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListTransportType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListPortNumber"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListSrcBlocked"))
)
if mibBuilder.loadTexts:
    csbDynamicBlackListGroup.setStatus("current")

csbAdjacencyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 5)
)
csbAdjacencyGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyAccountName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyState"))
)
if mibBuilder.loadTexts:
    csbAdjacencyGroup.setStatus("current")

csbSBCServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 6)
)
csbSBCServiceGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceSlot"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceState"))
)
if mibBuilder.loadTexts:
    csbSBCServiceGroup.setStatus("current")

csbCongestionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 7)
)
csbCongestionGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbCongestionAlarmState"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbCongestionAlarmType"))
)
if mibBuilder.loadTexts:
    csbCongestionGroup.setStatus("current")

csbSLAGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 8)
)
csbSLAGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyAccountName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyScope"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyLimit"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLACurrentUsage"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAViolationEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyRestriction"))
)
if mibBuilder.loadTexts:
    csbSLAGroup.setStatus("deprecated")

csbRadiusConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 9)
)
csbRadiusConnectionGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusConnectionState"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusServerName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusServerAddressType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusServerAddress"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusServerPriority"))
)
if mibBuilder.loadTexts:
    csbRadiusConnectionGroup.setStatus("current")

csbDiameterConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 10)
)
csbDiameterConnectionGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterConnectionState"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterGroupName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterServerName"))
)
if mibBuilder.loadTexts:
    csbDiameterConnectionGroup.setStatus("current")

csbH248StatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 11)
)
csbH248StatusGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbH248ControllerState"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csb248ControllerAddressType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbH248ControllerAddress"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbH248ControllerPort"))
)
if mibBuilder.loadTexts:
    csbH248StatusGroup.setStatus("current")

csbNotifEnabledGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 12)
)
csbNotifEnabledGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSourceAlertNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbBlackListNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyStatusNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbServiceStateNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbCongestionAlarmNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAViolationNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusConnectionStatusNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterConnectionStatusNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbH248ControllerStatusNotifEnabled"))
)
if mibBuilder.loadTexts:
    csbNotifEnabledGroup.setStatus("deprecated")

csbSLAGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 14)
)
csbSLAGroupRev1.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyAccountName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyScope"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyLimitRev1"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLACurrentUsageRev1"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAViolationEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyRestriction"))
)
if mibBuilder.loadTexts:
    csbSLAGroupRev1.setStatus("current")

csbNotifEnabledGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 15)
)
csbNotifEnabledGroupRev1.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSourceAlertNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbBlackListNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyStatusNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbServiceStateNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbCongestionAlarmNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAViolationNotifEnabledRev1"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusConnectionStatusNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterConnectionStatusNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbH248ControllerStatusNotifEnabled"))
)
if mibBuilder.loadTexts:
    csbNotifEnabledGroupRev1.setStatus("current")

csbQOSAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 16)
)
csbQOSAlertGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"))
)
if mibBuilder.loadTexts:
    csbQOSAlertGroup.setStatus("current")

csbNotifEnabledGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 18)
)
csbNotifEnabledGroupSup1.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertUnansweredCallRatioNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPercentPktDropNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertRoundTripDelayNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertLocalJitterNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertRemoteJitterNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPercentPktLostNotifEnabled"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertMoscqeNotifEnabled"))
)
if mibBuilder.loadTexts:
    csbNotifEnabledGroupSup1.setStatus("current")


# Notification objects

csbSourceAlertEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 1)
)
csbSourceAlertEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertVdbeId"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertGateId"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertFlowPairId"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertLocalAddressType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertLocalAddress"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertLocalPort"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertRemoteAddressType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertRemoteAddress"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertRemotePort"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSrcAlertVpnId"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"))
)
if mibBuilder.loadTexts:
    csbSourceAlertEvent.setStatus(
        "current"
    )

csbDynamicBlackListEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 2)
)
csbDynamicBlackListEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListSubFamily"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListVpnId"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListAddressType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListAddress"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListTransportType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListPortNumber"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListSrcBlocked"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"))
)
if mibBuilder.loadTexts:
    csbDynamicBlackListEvent.setStatus(
        "current"
    )

csbAdjacencyStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 3)
)
csbAdjacencyStatus.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyState"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyAccountName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"))
)
if mibBuilder.loadTexts:
    csbAdjacencyStatus.setStatus(
        "current"
    )

csbServiceStateEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 4)
)
csbServiceStateEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceState"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceSlot"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"))
)
if mibBuilder.loadTexts:
    csbServiceStateEvent.setStatus(
        "current"
    )

csbSystemCongestionAlarmEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 5)
)
csbSystemCongestionAlarmEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbCongestionAlarmType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbCongestionAlarmState"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"))
)
if mibBuilder.loadTexts:
    csbSystemCongestionAlarmEvent.setStatus(
        "current"
    )

csbSLAViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 6)
)
csbSLAViolation.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyAccountName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyScope"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyLimit"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLACurrentUsage"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAViolationEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyRestriction"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"))
)
if mibBuilder.loadTexts:
    csbSLAViolation.setStatus(
        "deprecated"
    )

csbRadiusConnectionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 7)
)
csbRadiusConnectionStatus.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusConnectionState"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusServerName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusServerAddressType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusServerAddress"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusServerPriority"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"))
)
if mibBuilder.loadTexts:
    csbRadiusConnectionStatus.setStatus(
        "current"
    )

csbDiameterConnectionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 8)
)
csbDiameterConnectionStatus.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterConnectionState"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterGroupName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterServerName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"))
)
if mibBuilder.loadTexts:
    csbDiameterConnectionStatus.setStatus(
        "current"
    )

csbH248ControllerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 9)
)
csbH248ControllerStatus.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbH248ControllerState"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csb248ControllerAddressType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbH248ControllerAddress"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbH248ControllerPort"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"))
)
if mibBuilder.loadTexts:
    csbH248ControllerStatus.setStatus(
        "current"
    )

csbSLAViolationRev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 10)
)
csbSLAViolationRev1.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyAccountName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyScope"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyLimitRev1"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLACurrentUsageRev1"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAViolationEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAPolicyRestriction"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"))
)
if mibBuilder.loadTexts:
    csbSLAViolationRev1.setStatus(
        "current"
    )

csbQOSUnansweredCallRatioEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 11)
)
csbQOSUnansweredCallRatioEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSUnansweredCallRatioEvent.setStatus(
        "current"
    )

csbQOSUnansweredCallRatioClearEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 12)
)
csbQOSUnansweredCallRatioClearEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSUnansweredCallRatioClearEvent.setStatus(
        "current"
    )

csbQOSPercentPktLostEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 13)
)
csbQOSPercentPktLostEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSPercentPktLostEvent.setStatus(
        "current"
    )

csbQOSPercentPktLostClearEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 14)
)
csbQOSPercentPktLostClearEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSPercentPktLostClearEvent.setStatus(
        "current"
    )

csbQOSPercentPktDropEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 15)
)
csbQOSPercentPktDropEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSPercentPktDropEvent.setStatus(
        "current"
    )

csbQOSPercentPktDropClearEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 16)
)
csbQOSPercentPktDropClearEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSPercentPktDropClearEvent.setStatus(
        "current"
    )

csbQOSRoundTripDelayEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 17)
)
csbQOSRoundTripDelayEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSRoundTripDelayEvent.setStatus(
        "current"
    )

csbQOSRoundTripDelayClearEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 18)
)
csbQOSRoundTripDelayClearEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSRoundTripDelayClearEvent.setStatus(
        "current"
    )

csbQOSLocalJitterEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 19)
)
csbQOSLocalJitterEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSLocalJitterEvent.setStatus(
        "current"
    )

csbQOSLocalJitterClearEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 20)
)
csbQOSLocalJitterClearEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSLocalJitterClearEvent.setStatus(
        "current"
    )

csbQOSRemoteJitterEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 21)
)
csbQOSRemoteJitterEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSRemoteJitterEvent.setStatus(
        "current"
    )

csbQOSRemoteJitterClearEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 22)
)
csbQOSRemoteJitterClearEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSRemoteJitterClearEvent.setStatus(
        "current"
    )

csbQOSMoscqeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 23)
)
csbQOSMoscqeEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSMoscqeEvent.setStatus(
        "current"
    )

csbQOSMoscqeClearEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 0, 24)
)
csbQOSMoscqeClearEvent.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSubsystem"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmSeverity"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmID"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmTime"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSBCServiceName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertType"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyName"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertSummaryPeriod"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertCurrentValue"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSAlertPreviousLevel"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSNormalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMinorAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSCriticalAlertCount"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAlarmDescription"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMajorAlertCount"))
)
if mibBuilder.loadTexts:
    csbQOSMoscqeClearEvent.setStatus(
        "current"
    )


# Notifications groups

csbNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 1)
)
csbNotificationGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSourceAlertEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyStatus"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbServiceStateEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSystemCongestionAlarmEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAViolation"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusConnectionStatus"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterConnectionStatus"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbH248ControllerStatus"))
)
if mibBuilder.loadTexts:
    csbNotificationGroup.setStatus(
        "deprecated"
    )

csbNotificationGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 13)
)
csbNotificationGroupRev1.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSourceAlertEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDynamicBlackListEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbAdjacencyStatus"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbServiceStateEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSystemCongestionAlarmEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbSLAViolationRev1"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbRadiusConnectionStatus"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbDiameterConnectionStatus"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbH248ControllerStatus"))
)
if mibBuilder.loadTexts:
    csbNotificationGroupRev1.setStatus(
        "current"
    )

csbNotificationGroupSup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 2, 17)
)
csbNotificationGroupSup1.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSUnansweredCallRatioClearEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSPercentPktLostEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSPercentPktLostClearEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSPercentPktDropEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSPercentPktDropClearEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSRoundTripDelayEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSRoundTripDelayClearEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSLocalJitterEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSLocalJitterClearEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSRemoteJitterEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSRemoteJitterClearEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMoscqeEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSMoscqeClearEvent"),
        ("CISCO-SESS-BORDER-CTRLR-EVENT-MIB", "csbQOSUnansweredCallRatioEvent"))
)
if mibBuilder.loadTexts:
    csbNotificationGroupSup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

csbCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 1, 1)
)
if mibBuilder.loadTexts:
    csbCompliance.setStatus(
        "deprecated"
    )

csbComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 1, 2)
)
if mibBuilder.loadTexts:
    csbComplianceRev1.setStatus(
        "deprecated"
    )

csbComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 658, 2, 1, 3)
)
if mibBuilder.loadTexts:
    csbComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SESS-BORDER-CTRLR-EVENT-MIB",
    **{"CsbQOSAlertScopeType": CsbQOSAlertScopeType,
       "CsbDynamicBlackListedSrcSubFamily": CsbDynamicBlackListedSrcSubFamily,
       "CsbDynamicBlackListedTransPortType": CsbDynamicBlackListedTransPortType,
       "ciscoSessBorderCtrlrEventMIB": ciscoSessBorderCtrlrEventMIB,
       "ciscoSessBorderCtrlrMIBNotifs": ciscoSessBorderCtrlrMIBNotifs,
       "csbSourceAlertEvent": csbSourceAlertEvent,
       "csbDynamicBlackListEvent": csbDynamicBlackListEvent,
       "csbAdjacencyStatus": csbAdjacencyStatus,
       "csbServiceStateEvent": csbServiceStateEvent,
       "csbSystemCongestionAlarmEvent": csbSystemCongestionAlarmEvent,
       "csbSLAViolation": csbSLAViolation,
       "csbRadiusConnectionStatus": csbRadiusConnectionStatus,
       "csbDiameterConnectionStatus": csbDiameterConnectionStatus,
       "csbH248ControllerStatus": csbH248ControllerStatus,
       "csbSLAViolationRev1": csbSLAViolationRev1,
       "csbQOSUnansweredCallRatioEvent": csbQOSUnansweredCallRatioEvent,
       "csbQOSUnansweredCallRatioClearEvent": csbQOSUnansweredCallRatioClearEvent,
       "csbQOSPercentPktLostEvent": csbQOSPercentPktLostEvent,
       "csbQOSPercentPktLostClearEvent": csbQOSPercentPktLostClearEvent,
       "csbQOSPercentPktDropEvent": csbQOSPercentPktDropEvent,
       "csbQOSPercentPktDropClearEvent": csbQOSPercentPktDropClearEvent,
       "csbQOSRoundTripDelayEvent": csbQOSRoundTripDelayEvent,
       "csbQOSRoundTripDelayClearEvent": csbQOSRoundTripDelayClearEvent,
       "csbQOSLocalJitterEvent": csbQOSLocalJitterEvent,
       "csbQOSLocalJitterClearEvent": csbQOSLocalJitterClearEvent,
       "csbQOSRemoteJitterEvent": csbQOSRemoteJitterEvent,
       "csbQOSRemoteJitterClearEvent": csbQOSRemoteJitterClearEvent,
       "csbQOSMoscqeEvent": csbQOSMoscqeEvent,
       "csbQOSMoscqeClearEvent": csbQOSMoscqeClearEvent,
       "ciscoSessBorderCtrlrMIBObjects": ciscoSessBorderCtrlrMIBObjects,
       "csbAlarmSubsystem": csbAlarmSubsystem,
       "csbAlarmSeverity": csbAlarmSeverity,
       "csbAlarmID": csbAlarmID,
       "csbAlarmTime": csbAlarmTime,
       "csbSBCServiceName": csbSBCServiceName,
       "csbAlarmDescription": csbAlarmDescription,
       "csbSrcAlertVdbeId": csbSrcAlertVdbeId,
       "csbSrcAlertGateId": csbSrcAlertGateId,
       "csbSrcAlertFlowPairId": csbSrcAlertFlowPairId,
       "csbSrcAlertLocalAddressType": csbSrcAlertLocalAddressType,
       "csbSrcAlertLocalAddress": csbSrcAlertLocalAddress,
       "csbSrcAlertLocalPort": csbSrcAlertLocalPort,
       "csbSrcAlertRemoteAddressType": csbSrcAlertRemoteAddressType,
       "csbSrcAlertRemoteAddress": csbSrcAlertRemoteAddress,
       "csbSrcAlertRemotePort": csbSrcAlertRemotePort,
       "csbSrcAlertVpnId": csbSrcAlertVpnId,
       "csbDynamicBlackListSubFamily": csbDynamicBlackListSubFamily,
       "csbDynamicBlackListVpnId": csbDynamicBlackListVpnId,
       "csbDynamicBlackListAddressType": csbDynamicBlackListAddressType,
       "csbDynamicBlackListAddress": csbDynamicBlackListAddress,
       "csbDynamicBlackListTransportType": csbDynamicBlackListTransportType,
       "csbDynamicBlackListPortNumber": csbDynamicBlackListPortNumber,
       "csbDynamicBlackListSrcBlocked": csbDynamicBlackListSrcBlocked,
       "csbAdjacencyType": csbAdjacencyType,
       "csbAdjacencyState": csbAdjacencyState,
       "csbAdjacencyName": csbAdjacencyName,
       "csbAdjacencyAccountName": csbAdjacencyAccountName,
       "csbSBCServiceState": csbSBCServiceState,
       "csbSBCServiceSlot": csbSBCServiceSlot,
       "csbCongestionAlarmType": csbCongestionAlarmType,
       "csbCongestionAlarmState": csbCongestionAlarmState,
       "csbSLAPolicyAccountName": csbSLAPolicyAccountName,
       "csbSLAPolicyScope": csbSLAPolicyScope,
       "csbSLAPolicyLimit": csbSLAPolicyLimit,
       "csbSLAViolationEvent": csbSLAViolationEvent,
       "csbSLAPolicyRestriction": csbSLAPolicyRestriction,
       "csbSLACurrentUsage": csbSLACurrentUsage,
       "csbRadiusConnectionState": csbRadiusConnectionState,
       "csbRadiusType": csbRadiusType,
       "csbRadiusServerName": csbRadiusServerName,
       "csbRadiusServerAddressType": csbRadiusServerAddressType,
       "csbRadiusServerAddress": csbRadiusServerAddress,
       "csbRadiusServerPriority": csbRadiusServerPriority,
       "csbDiameterConnectionState": csbDiameterConnectionState,
       "csbDiameterType": csbDiameterType,
       "csbDiameterGroupName": csbDiameterGroupName,
       "csbDiameterServerName": csbDiameterServerName,
       "csbH248ControllerState": csbH248ControllerState,
       "csb248ControllerAddressType": csb248ControllerAddressType,
       "csbH248ControllerAddress": csbH248ControllerAddress,
       "csbH248ControllerPort": csbH248ControllerPort,
       "csbSourceAlertNotifEnabled": csbSourceAlertNotifEnabled,
       "csbBlackListNotifEnabled": csbBlackListNotifEnabled,
       "csbAdjacencyStatusNotifEnabled": csbAdjacencyStatusNotifEnabled,
       "csbServiceStateNotifEnabled": csbServiceStateNotifEnabled,
       "csbCongestionAlarmNotifEnabled": csbCongestionAlarmNotifEnabled,
       "csbSLAViolationNotifEnabled": csbSLAViolationNotifEnabled,
       "csbRadiusConnectionStatusNotifEnabled": csbRadiusConnectionStatusNotifEnabled,
       "csbDiameterConnectionStatusNotifEnabled": csbDiameterConnectionStatusNotifEnabled,
       "csbH248ControllerStatusNotifEnabled": csbH248ControllerStatusNotifEnabled,
       "csbSLAPolicyLimitRev1": csbSLAPolicyLimitRev1,
       "csbSLACurrentUsageRev1": csbSLACurrentUsageRev1,
       "csbSLAViolationNotifEnabledRev1": csbSLAViolationNotifEnabledRev1,
       "csbQOSAlertCurrentValue": csbQOSAlertCurrentValue,
       "csbQOSAlertCurrentLevel": csbQOSAlertCurrentLevel,
       "csbQOSAlertPreviousLevel": csbQOSAlertPreviousLevel,
       "csbQOSNormalAlertCount": csbQOSNormalAlertCount,
       "csbQOSMinorAlertCount": csbQOSMinorAlertCount,
       "csbQOSCriticalAlertCount": csbQOSCriticalAlertCount,
       "csbQOSMajorAlertCount": csbQOSMajorAlertCount,
       "csbQOSAlertType": csbQOSAlertType,
       "csbQOSAlertSummaryPeriod": csbQOSAlertSummaryPeriod,
       "csbQOSAlertUnansweredCallRatioNotifEnabled": csbQOSAlertUnansweredCallRatioNotifEnabled,
       "csbQOSAlertPercentPktDropNotifEnabled": csbQOSAlertPercentPktDropNotifEnabled,
       "csbQOSAlertRoundTripDelayNotifEnabled": csbQOSAlertRoundTripDelayNotifEnabled,
       "csbQOSAlertMoscqeNotifEnabled": csbQOSAlertMoscqeNotifEnabled,
       "csbQOSAlertLocalJitterNotifEnabled": csbQOSAlertLocalJitterNotifEnabled,
       "csbQOSAlertRemoteJitterNotifEnabled": csbQOSAlertRemoteJitterNotifEnabled,
       "csbQOSAlertPercentPktLostNotifEnabled": csbQOSAlertPercentPktLostNotifEnabled,
       "ciscoSessBorderCtrlrMIBConform": ciscoSessBorderCtrlrMIBConform,
       "ciscoSessBorderCtrlrMIBCompliances": ciscoSessBorderCtrlrMIBCompliances,
       "csbCompliance": csbCompliance,
       "csbComplianceRev1": csbComplianceRev1,
       "csbComplianceRev2": csbComplianceRev2,
       "ciscoSessBorderCtrlrMIBGroups": ciscoSessBorderCtrlrMIBGroups,
       "csbNotificationGroup": csbNotificationGroup,
       "csbNotificationManadatoryParams": csbNotificationManadatoryParams,
       "csbSourceAlertGroup": csbSourceAlertGroup,
       "csbDynamicBlackListGroup": csbDynamicBlackListGroup,
       "csbAdjacencyGroup": csbAdjacencyGroup,
       "csbSBCServiceGroup": csbSBCServiceGroup,
       "csbCongestionGroup": csbCongestionGroup,
       "csbSLAGroup": csbSLAGroup,
       "csbRadiusConnectionGroup": csbRadiusConnectionGroup,
       "csbDiameterConnectionGroup": csbDiameterConnectionGroup,
       "csbH248StatusGroup": csbH248StatusGroup,
       "csbNotifEnabledGroup": csbNotifEnabledGroup,
       "csbNotificationGroupRev1": csbNotificationGroupRev1,
       "csbSLAGroupRev1": csbSLAGroupRev1,
       "csbNotifEnabledGroupRev1": csbNotifEnabledGroupRev1,
       "csbQOSAlertGroup": csbQOSAlertGroup,
       "csbNotificationGroupSup1": csbNotificationGroupSup1,
       "csbNotifEnabledGroupSup1": csbNotifEnabledGroupSup1}
)
