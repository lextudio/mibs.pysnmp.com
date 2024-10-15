# SNMP MIB module (CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:48 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeInterval) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval")


# MODULE-IDENTITY

ciscoDot11CscMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 109)
)
ciscoDot11CscMIB.setRevisions(
        ("2004-06-02 00:00",
         "2003-05-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDot11CscMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11CscMIBObjects = _CiscoDot11CscMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 1)
)
_CiscoDot11CscConfigGlobal_ObjectIdentity = ObjectIdentity
ciscoDot11CscConfigGlobal = _CiscoDot11CscConfigGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1)
)
_CDot11CscAddressType_Type = InetAddressType
_CDot11CscAddressType_Object = MibScalar
cDot11CscAddressType = _CDot11CscAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 1),
    _CDot11CscAddressType_Type()
)
cDot11CscAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CscAddressType.setStatus("current")
_CDot11CscParentWdsAddress_Type = InetAddress
_CDot11CscParentWdsAddress_Object = MibScalar
cDot11CscParentWdsAddress = _CDot11CscParentWdsAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 2),
    _CDot11CscParentWdsAddress_Type()
)
cDot11CscParentWdsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CscParentWdsAddress.setStatus("current")
_CDot11CscRootNodeAddress_Type = InetAddress
_CDot11CscRootNodeAddress_Object = MibScalar
cDot11CscRootNodeAddress = _CDot11CscRootNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 3),
    _CDot11CscRootNodeAddress_Type()
)
cDot11CscRootNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CscRootNodeAddress.setStatus("current")
_CDot11CscMnAuthenticatorAddress_Type = InetAddress
_CDot11CscMnAuthenticatorAddress_Object = MibScalar
cDot11CscMnAuthenticatorAddress = _CDot11CscMnAuthenticatorAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 4),
    _CDot11CscMnAuthenticatorAddress_Type()
)
cDot11CscMnAuthenticatorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CscMnAuthenticatorAddress.setStatus("current")


class _CDot11CscOperMode_Type(Integer32):
    """Custom type cDot11CscOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("distributed", 2),
          ("infrastructure", 1))
    )


_CDot11CscOperMode_Type.__name__ = "Integer32"
_CDot11CscOperMode_Object = MibScalar
cDot11CscOperMode = _CDot11CscOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 5),
    _CDot11CscOperMode_Type()
)
cDot11CscOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CscOperMode.setStatus("current")
_CDot11CscMnInactivityTime_Type = TimeInterval
_CDot11CscMnInactivityTime_Object = MibScalar
cDot11CscMnInactivityTime = _CDot11CscMnInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 6),
    _CDot11CscMnInactivityTime_Type()
)
cDot11CscMnInactivityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CscMnInactivityTime.setStatus("current")
_CDot11CscRegistrationLifeTime_Type = TimeInterval
_CDot11CscRegistrationLifeTime_Object = MibScalar
cDot11CscRegistrationLifeTime = _CDot11CscRegistrationLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 7),
    _CDot11CscRegistrationLifeTime_Type()
)
cDot11CscRegistrationLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CscRegistrationLifeTime.setStatus("current")
_CDot11CscStateTransitions_Type = Counter32
_CDot11CscStateTransitions_Object = MibScalar
cDot11CscStateTransitions = _CDot11CscStateTransitions_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 1, 1, 8),
    _CDot11CscStateTransitions_Type()
)
cDot11CscStateTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11CscStateTransitions.setStatus("current")
_CiscoDot11CscMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDot11CscMIBConformance = _CiscoDot11CscMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 2)
)
_CiscoDot11CscMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11CscMIBCompliances = _CiscoDot11CscMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 1)
)
_CiscoDot11CscMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11CscMIBGroups = _CiscoDot11CscMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 2)
)

# Managed Objects groups

ciscoDot11CscConfigGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 2, 1)
)
ciscoDot11CscConfigGlobalGroup.setObjects(
      *(("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscAddressType"),
        ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscParentWdsAddress"),
        ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscRootNodeAddress"),
        ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscMnAuthenticatorAddress"),
        ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscOperMode"),
        ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscMnInactivityTime"),
        ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscRegistrationLifeTime"),
        ("CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB", "cDot11CscStateTransitions"))
)
if mibBuilder.loadTexts:
    ciscoDot11CscConfigGlobalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDot11CscMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 109, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDot11CscMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-CONTEXT-SERVICES-CLIENT-MIB",
    **{"ciscoDot11CscMIB": ciscoDot11CscMIB,
       "ciscoDot11CscMIBObjects": ciscoDot11CscMIBObjects,
       "ciscoDot11CscConfigGlobal": ciscoDot11CscConfigGlobal,
       "cDot11CscAddressType": cDot11CscAddressType,
       "cDot11CscParentWdsAddress": cDot11CscParentWdsAddress,
       "cDot11CscRootNodeAddress": cDot11CscRootNodeAddress,
       "cDot11CscMnAuthenticatorAddress": cDot11CscMnAuthenticatorAddress,
       "cDot11CscOperMode": cDot11CscOperMode,
       "cDot11CscMnInactivityTime": cDot11CscMnInactivityTime,
       "cDot11CscRegistrationLifeTime": cDot11CscRegistrationLifeTime,
       "cDot11CscStateTransitions": cDot11CscStateTransitions,
       "ciscoDot11CscMIBConformance": ciscoDot11CscMIBConformance,
       "ciscoDot11CscMIBCompliances": ciscoDot11CscMIBCompliances,
       "ciscoDot11CscMIBCompliance": ciscoDot11CscMIBCompliance,
       "ciscoDot11CscMIBGroups": ciscoDot11CscMIBGroups,
       "ciscoDot11CscConfigGlobalGroup": ciscoDot11CscConfigGlobalGroup}
)
