# SNMP MIB module (WWP-SYSTEM-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-SYSTEM-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:26 2024
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

(dot1dStpPort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dStpPort")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules")


# MODULE-IDENTITY

wwpSysCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 30)
)
wwpSysCtrlMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpSysCtrlMIBObjects_ObjectIdentity = ObjectIdentity
wwpSysCtrlMIBObjects = _WwpSysCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 30, 1)
)
_WwpSysCtrl_ObjectIdentity = ObjectIdentity
wwpSysCtrl = _WwpSysCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1)
)


class _WwpSysCtrlBridgeRSTPEnable_Type(TruthValue):
    """Custom type wwpSysCtrlBridgeRSTPEnable based on TruthValue"""


_WwpSysCtrlBridgeRSTPEnable_Object = MibScalar
wwpSysCtrlBridgeRSTPEnable = _WwpSysCtrlBridgeRSTPEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1, 1),
    _WwpSysCtrlBridgeRSTPEnable_Type()
)
wwpSysCtrlBridgeRSTPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSysCtrlBridgeRSTPEnable.setStatus("current")


class _WwpSysCtrlLacpEnable_Type(TruthValue):
    """Custom type wwpSysCtrlLacpEnable based on TruthValue"""


_WwpSysCtrlLacpEnable_Object = MibScalar
wwpSysCtrlLacpEnable = _WwpSysCtrlLacpEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 30, 1, 1, 2),
    _WwpSysCtrlLacpEnable_Type()
)
wwpSysCtrlLacpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpSysCtrlLacpEnable.setStatus("current")
_WwpSysCtrlMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpSysCtrlMIBNotificationPrefix = _WwpSysCtrlMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 30, 2)
)
_WwpSysCtrlMIBNotifications_ObjectIdentity = ObjectIdentity
wwpSysCtrlMIBNotifications = _WwpSysCtrlMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 30, 2, 0)
)
_WwpSysCtrlMIBConformance_ObjectIdentity = ObjectIdentity
wwpSysCtrlMIBConformance = _WwpSysCtrlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 30, 3)
)
_WwpSysCtrlMIBCompliances_ObjectIdentity = ObjectIdentity
wwpSysCtrlMIBCompliances = _WwpSysCtrlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 30, 3, 1)
)
_WwpSysCtrlMIBGroups_ObjectIdentity = ObjectIdentity
wwpSysCtrlMIBGroups = _WwpSysCtrlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 30, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpPvstBpduReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 30, 2, 0, 1)
)
wwpPvstBpduReceived.setObjects(
    ("BRIDGE-MIB", "dot1dStpPort")
)
if mibBuilder.loadTexts:
    wwpPvstBpduReceived.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-SYSTEM-CONTROL-MIB",
    **{"wwpSysCtrlMIB": wwpSysCtrlMIB,
       "wwpSysCtrlMIBObjects": wwpSysCtrlMIBObjects,
       "wwpSysCtrl": wwpSysCtrl,
       "wwpSysCtrlBridgeRSTPEnable": wwpSysCtrlBridgeRSTPEnable,
       "wwpSysCtrlLacpEnable": wwpSysCtrlLacpEnable,
       "wwpSysCtrlMIBNotificationPrefix": wwpSysCtrlMIBNotificationPrefix,
       "wwpSysCtrlMIBNotifications": wwpSysCtrlMIBNotifications,
       "wwpPvstBpduReceived": wwpPvstBpduReceived,
       "wwpSysCtrlMIBConformance": wwpSysCtrlMIBConformance,
       "wwpSysCtrlMIBCompliances": wwpSysCtrlMIBCompliances,
       "wwpSysCtrlMIBGroups": wwpSysCtrlMIBGroups}
)
