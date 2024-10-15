# SNMP MIB module (ATDHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ATDHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:43:39 2024
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

(alliedTelesyn,
 atiProduct,
 atswitchMib,
 mibObject) = mibBuilder.importSymbols(
    "ATSWTCH2-MIB",
    "alliedTelesyn",
    "atiProduct",
    "atswitchMib",
    "mibObject")

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
 NotificationType,
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
    "NotificationType",
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class BridgeId(OctetString):
    """Custom type BridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )





class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtswitchDHCPGroup_ObjectIdentity = ObjectIdentity
atswitchDHCPGroup = _AtswitchDHCPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 11)
)
_AtswitchDHCPSysGroup_ObjectIdentity = ObjectIdentity
atswitchDHCPSysGroup = _AtswitchDHCPSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1)
)
_AtswitchDHCPCurrentDHCPClientAddress_Type = IpAddress
_AtswitchDHCPCurrentDHCPClientAddress_Object = MibScalar
atswitchDHCPCurrentDHCPClientAddress = _AtswitchDHCPCurrentDHCPClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 1),
    _AtswitchDHCPCurrentDHCPClientAddress_Type()
)
atswitchDHCPCurrentDHCPClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchDHCPCurrentDHCPClientAddress.setStatus("mandatory")
_AtswitchDHCPSubnetMask_Type = IpAddress
_AtswitchDHCPSubnetMask_Object = MibScalar
atswitchDHCPSubnetMask = _AtswitchDHCPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 2),
    _AtswitchDHCPSubnetMask_Type()
)
atswitchDHCPSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchDHCPSubnetMask.setStatus("mandatory")
_AtswitchDHCPCurrentRelayAgentAddress_Type = IpAddress
_AtswitchDHCPCurrentRelayAgentAddress_Object = MibScalar
atswitchDHCPCurrentRelayAgentAddress = _AtswitchDHCPCurrentRelayAgentAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 3),
    _AtswitchDHCPCurrentRelayAgentAddress_Type()
)
atswitchDHCPCurrentRelayAgentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchDHCPCurrentRelayAgentAddress.setStatus("mandatory")
_AtswitchDHCPNextDHCPServerAddress_Type = IpAddress
_AtswitchDHCPNextDHCPServerAddress_Object = MibScalar
atswitchDHCPNextDHCPServerAddress = _AtswitchDHCPNextDHCPServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 1, 4),
    _AtswitchDHCPNextDHCPServerAddress_Type()
)
atswitchDHCPNextDHCPServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchDHCPNextDHCPServerAddress.setStatus("mandatory")
_AtswitchDHCPTimerGroup_ObjectIdentity = ObjectIdentity
atswitchDHCPTimerGroup = _AtswitchDHCPTimerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2)
)
_AtswitchDHCPLeaseTimer_Type = TimeTicks
_AtswitchDHCPLeaseTimer_Object = MibScalar
atswitchDHCPLeaseTimer = _AtswitchDHCPLeaseTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2, 1),
    _AtswitchDHCPLeaseTimer_Type()
)
atswitchDHCPLeaseTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchDHCPLeaseTimer.setStatus("mandatory")
_AtswitchDHCPReacquisitionTimer_Type = TimeTicks
_AtswitchDHCPReacquisitionTimer_Object = MibScalar
atswitchDHCPReacquisitionTimer = _AtswitchDHCPReacquisitionTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2, 2),
    _AtswitchDHCPReacquisitionTimer_Type()
)
atswitchDHCPReacquisitionTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchDHCPReacquisitionTimer.setStatus("mandatory")
_AtswitchDHCPExpirationTimer_Type = TimeTicks
_AtswitchDHCPExpirationTimer_Object = MibScalar
atswitchDHCPExpirationTimer = _AtswitchDHCPExpirationTimer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 10, 11, 2, 3),
    _AtswitchDHCPExpirationTimer_Type()
)
atswitchDHCPExpirationTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atswitchDHCPExpirationTimer.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ATDHCP-MIB",
    **{"MacAddress": MacAddress,
       "BridgeId": BridgeId,
       "Timeout": Timeout,
       "atswitchDHCPGroup": atswitchDHCPGroup,
       "atswitchDHCPSysGroup": atswitchDHCPSysGroup,
       "atswitchDHCPCurrentDHCPClientAddress": atswitchDHCPCurrentDHCPClientAddress,
       "atswitchDHCPSubnetMask": atswitchDHCPSubnetMask,
       "atswitchDHCPCurrentRelayAgentAddress": atswitchDHCPCurrentRelayAgentAddress,
       "atswitchDHCPNextDHCPServerAddress": atswitchDHCPNextDHCPServerAddress,
       "atswitchDHCPTimerGroup": atswitchDHCPTimerGroup,
       "atswitchDHCPLeaseTimer": atswitchDHCPLeaseTimer,
       "atswitchDHCPReacquisitionTimer": atswitchDHCPReacquisitionTimer,
       "atswitchDHCPExpirationTimer": atswitchDHCPExpirationTimer}
)
