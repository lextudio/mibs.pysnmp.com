# SNMP MIB module (CISCO-ASPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ASPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:43 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoAsppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 55)
)
ciscoAsppMIB.setRevisions(
        ("2003-02-10 00:00",
         "1995-08-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AsppObjects_ObjectIdentity = ObjectIdentity
asppObjects = _AsppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1)
)
_AsppPorts_ObjectIdentity = ObjectIdentity
asppPorts = _AsppPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1)
)
_AsppPortTable_Object = MibTable
asppPortTable = _AsppPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1)
)
if mibBuilder.loadTexts:
    asppPortTable.setStatus("current")
_AsppPortEntry_Object = MibTableRow
asppPortEntry = _AsppPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1)
)
asppPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    asppPortEntry.setStatus("current")


class _AsppPortProtocol_Type(Integer32):
    """Custom type asppPortProtocol based on Integer32"""
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
        *(("adplex", 1),
          ("adtPollSelect", 2),
          ("adtVariPoll", 3),
          ("apos", 9),
          ("asyncGeneric", 5),
          ("diebold", 4),
          ("gddb", 8),
          ("mdi", 6),
          ("mosec", 7))
    )


_AsppPortProtocol_Type.__name__ = "Integer32"
_AsppPortProtocol_Object = MibTableColumn
asppPortProtocol = _AsppPortProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 1),
    _AsppPortProtocol_Type()
)
asppPortProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortProtocol.setStatus("current")


class _AsppPortRole_Type(Integer32):
    """Custom type asppPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_AsppPortRole_Type.__name__ = "Integer32"
_AsppPortRole_Object = MibTableColumn
asppPortRole = _AsppPortRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 2),
    _AsppPortRole_Type()
)
asppPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortRole.setStatus("current")


class _AsppPortReceiveInterFrameTimeout_Type(Integer32):
    """Custom type asppPortReceiveInterFrameTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AsppPortReceiveInterFrameTimeout_Type.__name__ = "Integer32"
_AsppPortReceiveInterFrameTimeout_Object = MibTableColumn
asppPortReceiveInterFrameTimeout = _AsppPortReceiveInterFrameTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 3),
    _AsppPortReceiveInterFrameTimeout_Type()
)
asppPortReceiveInterFrameTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortReceiveInterFrameTimeout.setStatus("current")
if mibBuilder.loadTexts:
    asppPortReceiveInterFrameTimeout.setUnits("milliseconds")


class _AsppPortDeviceAddressOffset_Type(Integer32):
    """Custom type asppPortDeviceAddressOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsppPortDeviceAddressOffset_Type.__name__ = "Integer32"
_AsppPortDeviceAddressOffset_Object = MibTableColumn
asppPortDeviceAddressOffset = _AsppPortDeviceAddressOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 4),
    _AsppPortDeviceAddressOffset_Type()
)
asppPortDeviceAddressOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortDeviceAddressOffset.setStatus("current")
if mibBuilder.loadTexts:
    asppPortDeviceAddressOffset.setUnits("bytes")


class _AsppPortEOFCharacter_Type(Integer32):
    """Custom type asppPortEOFCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AsppPortEOFCharacter_Type.__name__ = "Integer32"
_AsppPortEOFCharacter_Object = MibTableColumn
asppPortEOFCharacter = _AsppPortEOFCharacter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 5),
    _AsppPortEOFCharacter_Type()
)
asppPortEOFCharacter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortEOFCharacter.setStatus("current")


class _AsppPortSOFCharacter_Type(Integer32):
    """Custom type asppPortSOFCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AsppPortSOFCharacter_Type.__name__ = "Integer32"
_AsppPortSOFCharacter_Object = MibTableColumn
asppPortSOFCharacter = _AsppPortSOFCharacter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 6),
    _AsppPortSOFCharacter_Type()
)
asppPortSOFCharacter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortSOFCharacter.setStatus("current")


class _AsppPortIgnoreSequenceNumber_Type(TruthValue):
    """Custom type asppPortIgnoreSequenceNumber based on TruthValue"""


_AsppPortIgnoreSequenceNumber_Object = MibTableColumn
asppPortIgnoreSequenceNumber = _AsppPortIgnoreSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 7),
    _AsppPortIgnoreSequenceNumber_Type()
)
asppPortIgnoreSequenceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortIgnoreSequenceNumber.setStatus("current")


class _AsppPortRspTimer_Type(Integer32):
    """Custom type asppPortRspTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsppPortRspTimer_Type.__name__ = "Integer32"
_AsppPortRspTimer_Object = MibTableColumn
asppPortRspTimer = _AsppPortRspTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 8),
    _AsppPortRspTimer_Type()
)
asppPortRspTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortRspTimer.setStatus("current")
if mibBuilder.loadTexts:
    asppPortRspTimer.setUnits("seconds")


class _AsppPortRxTimer_Type(Integer32):
    """Custom type asppPortRxTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_AsppPortRxTimer_Type.__name__ = "Integer32"
_AsppPortRxTimer_Object = MibTableColumn
asppPortRxTimer = _AsppPortRxTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 9),
    _AsppPortRxTimer_Type()
)
asppPortRxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortRxTimer.setStatus("current")
if mibBuilder.loadTexts:
    asppPortRxTimer.setUnits("seconds")


class _AsppPortHostTimer_Type(Integer32):
    """Custom type asppPortHostTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 120),
    )


_AsppPortHostTimer_Type.__name__ = "Integer32"
_AsppPortHostTimer_Object = MibTableColumn
asppPortHostTimer = _AsppPortHostTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 10),
    _AsppPortHostTimer_Type()
)
asppPortHostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortHostTimer.setStatus("current")
if mibBuilder.loadTexts:
    asppPortHostTimer.setUnits("seconds")


class _AsppPortConnectTimer_Type(Integer32):
    """Custom type asppPortConnectTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsppPortConnectTimer_Type.__name__ = "Integer32"
_AsppPortConnectTimer_Object = MibTableColumn
asppPortConnectTimer = _AsppPortConnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 11),
    _AsppPortConnectTimer_Type()
)
asppPortConnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortConnectTimer.setStatus("current")
if mibBuilder.loadTexts:
    asppPortConnectTimer.setUnits("seconds")


class _AsppPortRetryCount_Type(Integer32):
    """Custom type asppPortRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AsppPortRetryCount_Type.__name__ = "Integer32"
_AsppPortRetryCount_Object = MibTableColumn
asppPortRetryCount = _AsppPortRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 12),
    _AsppPortRetryCount_Type()
)
asppPortRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortRetryCount.setStatus("current")


class _AsppPortDelayEnq_Type(Integer32):
    """Custom type asppPortDelayEnq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AsppPortDelayEnq_Type.__name__ = "Integer32"
_AsppPortDelayEnq_Object = MibTableColumn
asppPortDelayEnq = _AsppPortDelayEnq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 13),
    _AsppPortDelayEnq_Type()
)
asppPortDelayEnq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortDelayEnq.setStatus("current")
if mibBuilder.loadTexts:
    asppPortDelayEnq.setUnits("milliseconds")


class _AsppPortDisableEnq_Type(TruthValue):
    """Custom type asppPortDisableEnq based on TruthValue"""


_AsppPortDisableEnq_Object = MibTableColumn
asppPortDisableEnq = _AsppPortDisableEnq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 14),
    _AsppPortDisableEnq_Type()
)
asppPortDisableEnq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortDisableEnq.setStatus("current")


class _AsppPortSendAck_Type(TruthValue):
    """Custom type asppPortSendAck based on TruthValue"""


_AsppPortSendAck_Object = MibTableColumn
asppPortSendAck = _AsppPortSendAck_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 15),
    _AsppPortSendAck_Type()
)
asppPortSendAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortSendAck.setStatus("current")


class _AsppPortDirect_Type(TruthValue):
    """Custom type asppPortDirect based on TruthValue"""


_AsppPortDirect_Object = MibTableColumn
asppPortDirect = _AsppPortDirect_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 16),
    _AsppPortDirect_Type()
)
asppPortDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortDirect.setStatus("current")


class _AsppPortDCDAlways_Type(TruthValue):
    """Custom type asppPortDCDAlways based on TruthValue"""


_AsppPortDCDAlways_Object = MibTableColumn
asppPortDCDAlways = _AsppPortDCDAlways_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 1, 1, 1, 1, 17),
    _AsppPortDCDAlways_Type()
)
asppPortDCDAlways.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asppPortDCDAlways.setStatus("current")
_AsppMibConformance_ObjectIdentity = ObjectIdentity
asppMibConformance = _AsppMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 3)
)
_AsppMibCompliances_ObjectIdentity = ObjectIdentity
asppMibCompliances = _AsppMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 1)
)
_AsppMibGroups_ObjectIdentity = ObjectIdentity
asppMibGroups = _AsppMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 2)
)

# Managed Objects groups

asppPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 2, 1)
)
asppPortsGroup.setObjects(
      *(("CISCO-ASPP-MIB", "asppPortProtocol"),
        ("CISCO-ASPP-MIB", "asppPortRole"),
        ("CISCO-ASPP-MIB", "asppPortReceiveInterFrameTimeout"),
        ("CISCO-ASPP-MIB", "asppPortDeviceAddressOffset"))
)
if mibBuilder.loadTexts:
    asppPortsGroup.setStatus("current")

asppPortsGenericGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 2, 2)
)
asppPortsGenericGroup.setObjects(
      *(("CISCO-ASPP-MIB", "asppPortEOFCharacter"),
        ("CISCO-ASPP-MIB", "asppPortSOFCharacter"),
        ("CISCO-ASPP-MIB", "asppPortIgnoreSequenceNumber"))
)
if mibBuilder.loadTexts:
    asppPortsGenericGroup.setStatus("current")

asppPortsAposGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 2, 3)
)
asppPortsAposGroup.setObjects(
      *(("CISCO-ASPP-MIB", "asppPortRspTimer"),
        ("CISCO-ASPP-MIB", "asppPortRxTimer"),
        ("CISCO-ASPP-MIB", "asppPortHostTimer"),
        ("CISCO-ASPP-MIB", "asppPortConnectTimer"),
        ("CISCO-ASPP-MIB", "asppPortRetryCount"),
        ("CISCO-ASPP-MIB", "asppPortDelayEnq"),
        ("CISCO-ASPP-MIB", "asppPortDisableEnq"),
        ("CISCO-ASPP-MIB", "asppPortSendAck"),
        ("CISCO-ASPP-MIB", "asppPortDirect"),
        ("CISCO-ASPP-MIB", "asppPortDCDAlways"))
)
if mibBuilder.loadTexts:
    asppPortsAposGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

asppMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 1, 1)
)
if mibBuilder.loadTexts:
    asppMibCompliance.setStatus(
        "deprecated"
    )

asppMibComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 55, 3, 1, 2)
)
if mibBuilder.loadTexts:
    asppMibComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ASPP-MIB",
    **{"ciscoAsppMIB": ciscoAsppMIB,
       "asppObjects": asppObjects,
       "asppPorts": asppPorts,
       "asppPortTable": asppPortTable,
       "asppPortEntry": asppPortEntry,
       "asppPortProtocol": asppPortProtocol,
       "asppPortRole": asppPortRole,
       "asppPortReceiveInterFrameTimeout": asppPortReceiveInterFrameTimeout,
       "asppPortDeviceAddressOffset": asppPortDeviceAddressOffset,
       "asppPortEOFCharacter": asppPortEOFCharacter,
       "asppPortSOFCharacter": asppPortSOFCharacter,
       "asppPortIgnoreSequenceNumber": asppPortIgnoreSequenceNumber,
       "asppPortRspTimer": asppPortRspTimer,
       "asppPortRxTimer": asppPortRxTimer,
       "asppPortHostTimer": asppPortHostTimer,
       "asppPortConnectTimer": asppPortConnectTimer,
       "asppPortRetryCount": asppPortRetryCount,
       "asppPortDelayEnq": asppPortDelayEnq,
       "asppPortDisableEnq": asppPortDisableEnq,
       "asppPortSendAck": asppPortSendAck,
       "asppPortDirect": asppPortDirect,
       "asppPortDCDAlways": asppPortDCDAlways,
       "asppMibConformance": asppMibConformance,
       "asppMibCompliances": asppMibCompliances,
       "asppMibCompliance": asppMibCompliance,
       "asppMibComplianceRev1": asppMibComplianceRev1,
       "asppMibGroups": asppMibGroups,
       "asppPortsGroup": asppPortsGroup,
       "asppPortsGenericGroup": asppPortsGenericGroup,
       "asppPortsAposGroup": asppPortsAposGroup}
)
