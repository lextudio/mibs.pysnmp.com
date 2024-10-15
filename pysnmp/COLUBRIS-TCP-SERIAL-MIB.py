# SNMP MIB module (COLUBRIS-TCP-SERIAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COLUBRIS-TCP-SERIAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:27 2024
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

(colubrisMgmtV2,) = mibBuilder.importSymbols(
    "COLUBRIS-SMI",
    "colubrisMgmtV2")

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

colubrisTCPSerialMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ColubrisTCPSerialMIBObjects_ObjectIdentity = ObjectIdentity
colubrisTCPSerialMIBObjects = _ColubrisTCPSerialMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 1)
)
_CoTCPSerialStatusGroup_ObjectIdentity = ObjectIdentity
coTCPSerialStatusGroup = _CoTCPSerialStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1)
)


class _CoTCPSerialConnectionStatus_Type(Integer32):
    """Custom type coTCPSerialConnectionStatus based on Integer32"""
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
        *(("active", 3),
          ("closed", 1),
          ("connect", 5),
          ("idle", 4),
          ("listen", 2))
    )


_CoTCPSerialConnectionStatus_Type.__name__ = "Integer32"
_CoTCPSerialConnectionStatus_Object = MibScalar
coTCPSerialConnectionStatus = _CoTCPSerialConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 1),
    _CoTCPSerialConnectionStatus_Type()
)
coTCPSerialConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coTCPSerialConnectionStatus.setStatus("current")
_CoTCPSerialRemoteIPAddress_Type = IpAddress
_CoTCPSerialRemoteIPAddress_Object = MibScalar
coTCPSerialRemoteIPAddress = _CoTCPSerialRemoteIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 2),
    _CoTCPSerialRemoteIPAddress_Type()
)
coTCPSerialRemoteIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coTCPSerialRemoteIPAddress.setStatus("current")
_CoTCPSerialRemoteTCPPort_Type = Unsigned32
_CoTCPSerialRemoteTCPPort_Object = MibScalar
coTCPSerialRemoteTCPPort = _CoTCPSerialRemoteTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 3),
    _CoTCPSerialRemoteTCPPort_Type()
)
coTCPSerialRemoteTCPPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coTCPSerialRemoteTCPPort.setStatus("current")
_CoTCPSerialConnectTime_Type = Counter32
_CoTCPSerialConnectTime_Object = MibScalar
coTCPSerialConnectTime = _CoTCPSerialConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 4),
    _CoTCPSerialConnectTime_Type()
)
coTCPSerialConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coTCPSerialConnectTime.setStatus("current")
if mibBuilder.loadTexts:
    coTCPSerialConnectTime.setUnits("seconds")
_CoTCPSerialTxBytes_Type = Counter32
_CoTCPSerialTxBytes_Object = MibScalar
coTCPSerialTxBytes = _CoTCPSerialTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 5),
    _CoTCPSerialTxBytes_Type()
)
coTCPSerialTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coTCPSerialTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    coTCPSerialTxBytes.setUnits("bytes")
_CoTCPSerialRxBytes_Type = Counter32
_CoTCPSerialRxBytes_Object = MibScalar
coTCPSerialRxBytes = _CoTCPSerialRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 1, 1, 6),
    _CoTCPSerialRxBytes_Type()
)
coTCPSerialRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coTCPSerialRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    coTCPSerialRxBytes.setUnits("bytes")
_ColubrisTCPSerialMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
colubrisTCPSerialMIBNotificationPrefix = _ColubrisTCPSerialMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 2)
)
_ColubrisTCPSerialMIBNotifications_ObjectIdentity = ObjectIdentity
colubrisTCPSerialMIBNotifications = _ColubrisTCPSerialMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 2, 0)
)
_ColubrisTCPSerialMIBConformance_ObjectIdentity = ObjectIdentity
colubrisTCPSerialMIBConformance = _ColubrisTCPSerialMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 3)
)
_ColubrisTCPSerialMIBCompliances_ObjectIdentity = ObjectIdentity
colubrisTCPSerialMIBCompliances = _ColubrisTCPSerialMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 1)
)
_ColubrisTCPSerialMIBGroups_ObjectIdentity = ObjectIdentity
colubrisTCPSerialMIBGroups = _ColubrisTCPSerialMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 2)
)

# Managed Objects groups

colubrisTCPSerialConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 2, 1)
)
colubrisTCPSerialConfigMIBGroup.setObjects(
      *(("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialConnectionStatus"),
        ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialRemoteIPAddress"),
        ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialRemoteTCPPort"),
        ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialConnectTime"),
        ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialTxBytes"),
        ("COLUBRIS-TCP-SERIAL-MIB", "coTCPSerialRxBytes"))
)
if mibBuilder.loadTexts:
    colubrisTCPSerialConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

colubrisTCPSerialMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8744, 5, 37, 3, 1, 1)
)
if mibBuilder.loadTexts:
    colubrisTCPSerialMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COLUBRIS-TCP-SERIAL-MIB",
    **{"colubrisTCPSerialMIB": colubrisTCPSerialMIB,
       "colubrisTCPSerialMIBObjects": colubrisTCPSerialMIBObjects,
       "coTCPSerialStatusGroup": coTCPSerialStatusGroup,
       "coTCPSerialConnectionStatus": coTCPSerialConnectionStatus,
       "coTCPSerialRemoteIPAddress": coTCPSerialRemoteIPAddress,
       "coTCPSerialRemoteTCPPort": coTCPSerialRemoteTCPPort,
       "coTCPSerialConnectTime": coTCPSerialConnectTime,
       "coTCPSerialTxBytes": coTCPSerialTxBytes,
       "coTCPSerialRxBytes": coTCPSerialRxBytes,
       "colubrisTCPSerialMIBNotificationPrefix": colubrisTCPSerialMIBNotificationPrefix,
       "colubrisTCPSerialMIBNotifications": colubrisTCPSerialMIBNotifications,
       "colubrisTCPSerialMIBConformance": colubrisTCPSerialMIBConformance,
       "colubrisTCPSerialMIBCompliances": colubrisTCPSerialMIBCompliances,
       "colubrisTCPSerialMIBCompliance": colubrisTCPSerialMIBCompliance,
       "colubrisTCPSerialMIBGroups": colubrisTCPSerialMIBGroups,
       "colubrisTCPSerialConfigMIBGroup": colubrisTCPSerialConfigMIBGroup}
)
