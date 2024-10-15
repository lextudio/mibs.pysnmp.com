# SNMP MIB module (CISCO-UNIFIED-COMPUTING-NWCTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-UNIFIED-COMPUTING-NWCTRL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:03 2024
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

(CiscoAlarmSeverity,
 CiscoInetAddressMask,
 CiscoNetworkAddress,
 TimeIntervalSec,
 Unsigned64) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoAlarmSeverity",
    "CiscoInetAddressMask",
    "CiscoNetworkAddress",
    "TimeIntervalSec",
    "Unsigned64")

(CucsManagedObjectDn,
 CucsManagedObjectId,
 ciscoUnifiedComputingMIBObjects) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-MIB",
    "CucsManagedObjectDn",
    "CucsManagedObjectId",
    "ciscoUnifiedComputingMIBObjects")

(CucsNwctrlAdminState,
 CucsNwctrlLinkFailAction,
 CucsNwctrlRegistrationMode,
 CucsPolicyPolicyOwner) = mibBuilder.importSymbols(
    "CISCO-UNIFIED-COMPUTING-TC-MIB",
    "CucsNwctrlAdminState",
    "CucsNwctrlLinkFailAction",
    "CucsNwctrlRegistrationMode",
    "CucsPolicyPolicyOwner")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowPointer,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowPointer",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cucsNwctrlObjects = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CucsNwctrlDefinitionTable_Object = MibTable
cucsNwctrlDefinitionTable = _CucsNwctrlDefinitionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1)
)
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionTable.setStatus("current")
_CucsNwctrlDefinitionEntry_Object = MibTableRow
cucsNwctrlDefinitionEntry = _CucsNwctrlDefinitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1)
)
cucsNwctrlDefinitionEntry.setIndexNames(
    (0, "CISCO-UNIFIED-COMPUTING-NWCTRL-MIB", "cucsNwctrlDefinitionInstanceId"),
)
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionEntry.setStatus("current")
_CucsNwctrlDefinitionInstanceId_Type = CucsManagedObjectId
_CucsNwctrlDefinitionInstanceId_Object = MibTableColumn
cucsNwctrlDefinitionInstanceId = _CucsNwctrlDefinitionInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 1),
    _CucsNwctrlDefinitionInstanceId_Type()
)
cucsNwctrlDefinitionInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionInstanceId.setStatus("current")
_CucsNwctrlDefinitionDn_Type = CucsManagedObjectDn
_CucsNwctrlDefinitionDn_Object = MibTableColumn
cucsNwctrlDefinitionDn = _CucsNwctrlDefinitionDn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 2),
    _CucsNwctrlDefinitionDn_Type()
)
cucsNwctrlDefinitionDn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionDn.setStatus("current")
_CucsNwctrlDefinitionRn_Type = SnmpAdminString
_CucsNwctrlDefinitionRn_Object = MibTableColumn
cucsNwctrlDefinitionRn = _CucsNwctrlDefinitionRn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 3),
    _CucsNwctrlDefinitionRn_Type()
)
cucsNwctrlDefinitionRn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionRn.setStatus("current")
_CucsNwctrlDefinitionCdp_Type = CucsNwctrlAdminState
_CucsNwctrlDefinitionCdp_Object = MibTableColumn
cucsNwctrlDefinitionCdp = _CucsNwctrlDefinitionCdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 4),
    _CucsNwctrlDefinitionCdp_Type()
)
cucsNwctrlDefinitionCdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionCdp.setStatus("current")
_CucsNwctrlDefinitionDescr_Type = SnmpAdminString
_CucsNwctrlDefinitionDescr_Object = MibTableColumn
cucsNwctrlDefinitionDescr = _CucsNwctrlDefinitionDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 5),
    _CucsNwctrlDefinitionDescr_Type()
)
cucsNwctrlDefinitionDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionDescr.setStatus("current")
_CucsNwctrlDefinitionIntId_Type = SnmpAdminString
_CucsNwctrlDefinitionIntId_Object = MibTableColumn
cucsNwctrlDefinitionIntId = _CucsNwctrlDefinitionIntId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 6),
    _CucsNwctrlDefinitionIntId_Type()
)
cucsNwctrlDefinitionIntId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionIntId.setStatus("current")
_CucsNwctrlDefinitionName_Type = SnmpAdminString
_CucsNwctrlDefinitionName_Object = MibTableColumn
cucsNwctrlDefinitionName = _CucsNwctrlDefinitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 7),
    _CucsNwctrlDefinitionName_Type()
)
cucsNwctrlDefinitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionName.setStatus("current")
_CucsNwctrlDefinitionUplinkFailAction_Type = CucsNwctrlLinkFailAction
_CucsNwctrlDefinitionUplinkFailAction_Object = MibTableColumn
cucsNwctrlDefinitionUplinkFailAction = _CucsNwctrlDefinitionUplinkFailAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 8),
    _CucsNwctrlDefinitionUplinkFailAction_Type()
)
cucsNwctrlDefinitionUplinkFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionUplinkFailAction.setStatus("current")
_CucsNwctrlDefinitionMacRegisterMode_Type = CucsNwctrlRegistrationMode
_CucsNwctrlDefinitionMacRegisterMode_Object = MibTableColumn
cucsNwctrlDefinitionMacRegisterMode = _CucsNwctrlDefinitionMacRegisterMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 9),
    _CucsNwctrlDefinitionMacRegisterMode_Type()
)
cucsNwctrlDefinitionMacRegisterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionMacRegisterMode.setStatus("current")
_CucsNwctrlDefinitionPolicyLevel_Type = Gauge32
_CucsNwctrlDefinitionPolicyLevel_Object = MibTableColumn
cucsNwctrlDefinitionPolicyLevel = _CucsNwctrlDefinitionPolicyLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 10),
    _CucsNwctrlDefinitionPolicyLevel_Type()
)
cucsNwctrlDefinitionPolicyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionPolicyLevel.setStatus("current")
_CucsNwctrlDefinitionPolicyOwner_Type = CucsPolicyPolicyOwner
_CucsNwctrlDefinitionPolicyOwner_Object = MibTableColumn
cucsNwctrlDefinitionPolicyOwner = _CucsNwctrlDefinitionPolicyOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 11),
    _CucsNwctrlDefinitionPolicyOwner_Type()
)
cucsNwctrlDefinitionPolicyOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionPolicyOwner.setStatus("current")
_CucsNwctrlDefinitionPropAcl_Type = Unsigned64
_CucsNwctrlDefinitionPropAcl_Object = MibTableColumn
cucsNwctrlDefinitionPropAcl = _CucsNwctrlDefinitionPropAcl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 12),
    _CucsNwctrlDefinitionPropAcl_Type()
)
cucsNwctrlDefinitionPropAcl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionPropAcl.setStatus("current")
_CucsNwctrlDefinitionLldpReceive_Type = CucsNwctrlAdminState
_CucsNwctrlDefinitionLldpReceive_Object = MibTableColumn
cucsNwctrlDefinitionLldpReceive = _CucsNwctrlDefinitionLldpReceive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 13),
    _CucsNwctrlDefinitionLldpReceive_Type()
)
cucsNwctrlDefinitionLldpReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionLldpReceive.setStatus("current")
_CucsNwctrlDefinitionLldpTransmit_Type = CucsNwctrlAdminState
_CucsNwctrlDefinitionLldpTransmit_Object = MibTableColumn
cucsNwctrlDefinitionLldpTransmit = _CucsNwctrlDefinitionLldpTransmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 719, 1, 33, 1, 1, 14),
    _CucsNwctrlDefinitionLldpTransmit_Type()
)
cucsNwctrlDefinitionLldpTransmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cucsNwctrlDefinitionLldpTransmit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-UNIFIED-COMPUTING-NWCTRL-MIB",
    **{"cucsNwctrlObjects": cucsNwctrlObjects,
       "cucsNwctrlDefinitionTable": cucsNwctrlDefinitionTable,
       "cucsNwctrlDefinitionEntry": cucsNwctrlDefinitionEntry,
       "cucsNwctrlDefinitionInstanceId": cucsNwctrlDefinitionInstanceId,
       "cucsNwctrlDefinitionDn": cucsNwctrlDefinitionDn,
       "cucsNwctrlDefinitionRn": cucsNwctrlDefinitionRn,
       "cucsNwctrlDefinitionCdp": cucsNwctrlDefinitionCdp,
       "cucsNwctrlDefinitionDescr": cucsNwctrlDefinitionDescr,
       "cucsNwctrlDefinitionIntId": cucsNwctrlDefinitionIntId,
       "cucsNwctrlDefinitionName": cucsNwctrlDefinitionName,
       "cucsNwctrlDefinitionUplinkFailAction": cucsNwctrlDefinitionUplinkFailAction,
       "cucsNwctrlDefinitionMacRegisterMode": cucsNwctrlDefinitionMacRegisterMode,
       "cucsNwctrlDefinitionPolicyLevel": cucsNwctrlDefinitionPolicyLevel,
       "cucsNwctrlDefinitionPolicyOwner": cucsNwctrlDefinitionPolicyOwner,
       "cucsNwctrlDefinitionPropAcl": cucsNwctrlDefinitionPropAcl,
       "cucsNwctrlDefinitionLldpReceive": cucsNwctrlDefinitionLldpReceive,
       "cucsNwctrlDefinitionLldpTransmit": cucsNwctrlDefinitionLldpTransmit}
)
