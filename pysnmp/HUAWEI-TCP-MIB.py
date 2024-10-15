# SNMP MIB module (HUAWEI-TCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-TCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:12 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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

(tcpConnLocalAddress,
 tcpConnLocalPort,
 tcpConnRemAddress,
 tcpConnRemPort) = mibBuilder.importSymbols(
    "TCP-MIB",
    "tcpConnLocalAddress",
    "tcpConnLocalPort",
    "tcpConnRemAddress",
    "tcpConnRemPort")


# MODULE-IDENTITY

hwTCP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwTCPObjects_ObjectIdentity = ObjectIdentity
hwTCPObjects = _HwTCPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 1)
)
_HwTCPProtocol_Type = DisplayString
_HwTCPProtocol_Object = MibScalar
hwTCPProtocol = _HwTCPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 1, 1),
    _HwTCPProtocol_Type()
)
hwTCPProtocol.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTCPProtocol.setStatus("current")
_HwTCPVrfName_Type = DisplayString
_HwTCPVrfName_Object = MibScalar
hwTCPVrfName = _HwTCPVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 1, 2),
    _HwTCPVrfName_Type()
)
hwTCPVrfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTCPVrfName.setStatus("current")
_HwTCPTraps_ObjectIdentity = ObjectIdentity
hwTCPTraps = _HwTCPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 2)
)
_HwTCPConformance_ObjectIdentity = ObjectIdentity
hwTCPConformance = _HwTCPConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3)
)
_HwTCPCompliances_ObjectIdentity = ObjectIdentity
hwTCPCompliances = _HwTCPCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 1)
)
_HwTCPGroups_ObjectIdentity = ObjectIdentity
hwTCPGroups = _HwTCPGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 2)
)

# Managed Objects groups

hwTCPForTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 2, 2)
)
hwTCPForTrapGroup.setObjects(
      *(("HUAWEI-TCP-MIB", "hwTCPProtocol"),
        ("HUAWEI-TCP-MIB", "hwTCPVrfName"))
)
if mibBuilder.loadTexts:
    hwTCPForTrapGroup.setStatus("current")


# Notification objects

hwTCPMD5AuthenFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 2, 1)
)
hwTCPMD5AuthenFail.setObjects(
      *(("TCP-MIB", "tcpConnLocalAddress"),
        ("TCP-MIB", "tcpConnLocalPort"),
        ("TCP-MIB", "tcpConnRemAddress"),
        ("TCP-MIB", "tcpConnRemPort"),
        ("HUAWEI-TCP-MIB", "hwTCPProtocol"),
        ("HUAWEI-TCP-MIB", "hwTCPVrfName"))
)
if mibBuilder.loadTexts:
    hwTCPMD5AuthenFail.setStatus(
        "current"
    )


# Notifications groups

hwTCPTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 2, 1)
)
hwTCPTrapGroup.setObjects(
    ("HUAWEI-TCP-MIB", "hwTCPMD5AuthenFail")
)
if mibBuilder.loadTexts:
    hwTCPTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwTCPCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 34, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwTCPCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-TCP-MIB",
    **{"hwTCP": hwTCP,
       "hwTCPObjects": hwTCPObjects,
       "hwTCPProtocol": hwTCPProtocol,
       "hwTCPVrfName": hwTCPVrfName,
       "hwTCPTraps": hwTCPTraps,
       "hwTCPMD5AuthenFail": hwTCPMD5AuthenFail,
       "hwTCPConformance": hwTCPConformance,
       "hwTCPCompliances": hwTCPCompliances,
       "hwTCPCompliance": hwTCPCompliance,
       "hwTCPGroups": hwTCPGroups,
       "hwTCPTrapGroup": hwTCPTrapGroup,
       "hwTCPForTrapGroup": hwTCPForTrapGroup}
)
