# SNMP MIB module (HIRSCHMANN-GENERIC-ERROR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HIRSCHMANN-GENERIC-ERROR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:35 2024
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

(AutonomousType,
 DisplayString,
 TextualConvention,
 TestAndIncr) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention",
    "TestAndIncr")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hirschmann_ObjectIdentity = ObjectIdentity
hirschmann = _Hirschmann_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248)
)
_HmMgmtSEEErrorIDGroup_ObjectIdentity = ObjectIdentity
hmMgmtSEEErrorIDGroup = _HmMgmtSEEErrorIDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2)
)
_HmRedundancyConflict_ObjectIdentity = ObjectIdentity
hmRedundancyConflict = _HmRedundancyConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 1)
)
if mibBuilder.loadTexts:
    hmRedundancyConflict.setStatus("current")
_HmRedundancyConflictPort_ObjectIdentity = ObjectIdentity
hmRedundancyConflictPort = _HmRedundancyConflictPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 2)
)
if mibBuilder.loadTexts:
    hmRedundancyConflictPort.setStatus("current")
_HmMaxNumExceeded_ObjectIdentity = ObjectIdentity
hmMaxNumExceeded = _HmMaxNumExceeded_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 3)
)
if mibBuilder.loadTexts:
    hmMaxNumExceeded.setStatus("current")
_HmAlreadyCreated_ObjectIdentity = ObjectIdentity
hmAlreadyCreated = _HmAlreadyCreated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 4)
)
if mibBuilder.loadTexts:
    hmAlreadyCreated.setStatus("current")
_HmRedundancyConflictFpgaPort_ObjectIdentity = ObjectIdentity
hmRedundancyConflictFpgaPort = _HmRedundancyConflictFpgaPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 5)
)
if mibBuilder.loadTexts:
    hmRedundancyConflictFpgaPort.setStatus("current")
_HmVlanUnawareConflict_ObjectIdentity = ObjectIdentity
hmVlanUnawareConflict = _HmVlanUnawareConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 6)
)
if mibBuilder.loadTexts:
    hmVlanUnawareConflict.setStatus("current")
_HmRedundancyConflictPortShort_ObjectIdentity = ObjectIdentity
hmRedundancyConflictPortShort = _HmRedundancyConflictPortShort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 7)
)
if mibBuilder.loadTexts:
    hmRedundancyConflictPortShort.setStatus("current")
_HmTableFullError_ObjectIdentity = ObjectIdentity
hmTableFullError = _HmTableFullError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 8)
)
if mibBuilder.loadTexts:
    hmTableFullError.setStatus("current")
_HmFunctionNotUsableWithInterface_ObjectIdentity = ObjectIdentity
hmFunctionNotUsableWithInterface = _HmFunctionNotUsableWithInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 9)
)
if mibBuilder.loadTexts:
    hmFunctionNotUsableWithInterface.setStatus("current")
_HmGeneralConflict_ObjectIdentity = ObjectIdentity
hmGeneralConflict = _HmGeneralConflict_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 10)
)
if mibBuilder.loadTexts:
    hmGeneralConflict.setStatus("current")
_HmGeneralExceededRange_ObjectIdentity = ObjectIdentity
hmGeneralExceededRange = _HmGeneralExceededRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 11)
)
if mibBuilder.loadTexts:
    hmGeneralExceededRange.setStatus("current")
_HmRmonAlarmTableFullErrorReturn_ObjectIdentity = ObjectIdentity
hmRmonAlarmTableFullErrorReturn = _HmRmonAlarmTableFullErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 100)
)
if mibBuilder.loadTexts:
    hmRmonAlarmTableFullErrorReturn.setStatus("current")
_HmMgmtUdpPortInUse_ObjectIdentity = ObjectIdentity
hmMgmtUdpPortInUse = _HmMgmtUdpPortInUse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 200)
)
if mibBuilder.loadTexts:
    hmMgmtUdpPortInUse.setStatus("current")
_HmMgmtTcpPortInUse_ObjectIdentity = ObjectIdentity
hmMgmtTcpPortInUse = _HmMgmtTcpPortInUse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 201)
)
if mibBuilder.loadTexts:
    hmMgmtTcpPortInUse.setStatus("current")
_HmMgmtIPAddressConflictWithMgmtIP_ObjectIdentity = ObjectIdentity
hmMgmtIPAddressConflictWithMgmtIP = _HmMgmtIPAddressConflictWithMgmtIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 202)
)
if mibBuilder.loadTexts:
    hmMgmtIPAddressConflictWithMgmtIP.setStatus("current")
_HmMgmtIPAddressConflictWithOobIP_ObjectIdentity = ObjectIdentity
hmMgmtIPAddressConflictWithOobIP = _HmMgmtIPAddressConflictWithOobIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 203)
)
if mibBuilder.loadTexts:
    hmMgmtIPAddressConflictWithOobIP.setStatus("current")
_HmMgmtIPAddressConflictWithRouterIP_ObjectIdentity = ObjectIdentity
hmMgmtIPAddressConflictWithRouterIP = _HmMgmtIPAddressConflictWithRouterIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 204)
)
if mibBuilder.loadTexts:
    hmMgmtIPAddressConflictWithRouterIP.setStatus("current")
_Hm2NetIPAddrInvalid_ObjectIdentity = ObjectIdentity
hm2NetIPAddrInvalid = _Hm2NetIPAddrInvalid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 300)
)
if mibBuilder.loadTexts:
    hm2NetIPAddrInvalid.setStatus("current")
_Hm2NetIPAddrAndGateway_ObjectIdentity = ObjectIdentity
hm2NetIPAddrAndGateway = _Hm2NetIPAddrAndGateway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 301)
)
if mibBuilder.loadTexts:
    hm2NetIPAddrAndGateway.setStatus("current")
_Hm2NetIPAddrAndSubnet_ObjectIdentity = ObjectIdentity
hm2NetIPAddrAndSubnet = _Hm2NetIPAddrAndSubnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 302)
)
if mibBuilder.loadTexts:
    hm2NetIPAddrAndSubnet.setStatus("current")
_Hm2NetPrefixLengthInvalid_ObjectIdentity = ObjectIdentity
hm2NetPrefixLengthInvalid = _Hm2NetPrefixLengthInvalid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 2, 303)
)
if mibBuilder.loadTexts:
    hm2NetPrefixLengthInvalid.setStatus("current")
_HmMgmtSEInfoIDGroup_ObjectIdentity = ObjectIdentity
hmMgmtSEInfoIDGroup = _HmMgmtSEInfoIDGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 3)
)
_HmMgmtSEInfoValueChanged_ObjectIdentity = ObjectIdentity
hmMgmtSEInfoValueChanged = _HmMgmtSEInfoValueChanged_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 16, 3, 1)
)
if mibBuilder.loadTexts:
    hmMgmtSEInfoValueChanged.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HIRSCHMANN-GENERIC-ERROR-MIB",
    **{"hirschmann": hirschmann,
       "hmMgmtSEEErrorIDGroup": hmMgmtSEEErrorIDGroup,
       "hmRedundancyConflict": hmRedundancyConflict,
       "hmRedundancyConflictPort": hmRedundancyConflictPort,
       "hmMaxNumExceeded": hmMaxNumExceeded,
       "hmAlreadyCreated": hmAlreadyCreated,
       "hmRedundancyConflictFpgaPort": hmRedundancyConflictFpgaPort,
       "hmVlanUnawareConflict": hmVlanUnawareConflict,
       "hmRedundancyConflictPortShort": hmRedundancyConflictPortShort,
       "hmTableFullError": hmTableFullError,
       "hmFunctionNotUsableWithInterface": hmFunctionNotUsableWithInterface,
       "hmGeneralConflict": hmGeneralConflict,
       "hmGeneralExceededRange": hmGeneralExceededRange,
       "hmRmonAlarmTableFullErrorReturn": hmRmonAlarmTableFullErrorReturn,
       "hmMgmtUdpPortInUse": hmMgmtUdpPortInUse,
       "hmMgmtTcpPortInUse": hmMgmtTcpPortInUse,
       "hmMgmtIPAddressConflictWithMgmtIP": hmMgmtIPAddressConflictWithMgmtIP,
       "hmMgmtIPAddressConflictWithOobIP": hmMgmtIPAddressConflictWithOobIP,
       "hmMgmtIPAddressConflictWithRouterIP": hmMgmtIPAddressConflictWithRouterIP,
       "hm2NetIPAddrInvalid": hm2NetIPAddrInvalid,
       "hm2NetIPAddrAndGateway": hm2NetIPAddrAndGateway,
       "hm2NetIPAddrAndSubnet": hm2NetIPAddrAndSubnet,
       "hm2NetPrefixLengthInvalid": hm2NetPrefixLengthInvalid,
       "hmMgmtSEInfoIDGroup": hmMgmtSEInfoIDGroup,
       "hmMgmtSEInfoValueChanged": hmMgmtSEInfoValueChanged}
)
